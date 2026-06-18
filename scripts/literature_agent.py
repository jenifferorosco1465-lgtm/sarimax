#!/usr/bin/env python3
"""Search Crossref and OpenAlex and build an auditable SARIMAX literature matrix."""
from __future__ import annotations

import argparse
import csv
import json
import re
import time
from datetime import datetime, timezone
from pathlib import Path
from typing import Any
from urllib.parse import quote

import requests
import yaml

UA = "sarimax-replica-ecuador/0.2 (mailto:replace-with-your-email@example.com)"


def norm_text(value: str | None) -> str:
    return re.sub(r"[^a-z0-9]+", " ", (value or "").lower()).strip()


def doi_norm(value: str | None) -> str:
    value = (value or "").lower().strip()
    return value.replace("https://doi.org/", "").replace("http://doi.org/", "")


def get_json(url: str, timeout: int = 45) -> dict[str, Any]:
    response = requests.get(url, headers={"User-Agent": UA}, timeout=timeout)
    response.raise_for_status()
    return response.json()


def crossref(query: str, rows: int, from_year: int) -> list[dict[str, Any]]:
    url = (
        "https://api.crossref.org/works?query.bibliographic="
        f"{quote(query)}&rows={rows}&filter=from-pub-date:{from_year}-01-01"
    )
    payload = get_json(url)
    out = []
    for item in payload.get("message", {}).get("items", []):
        title = (item.get("title") or [""])[0]
        abstract = re.sub("<[^>]+>", " ", item.get("abstract", ""))
        year_parts = item.get("published-print", item.get("published-online", {})).get("date-parts", [[None]])
        authors = [" ".join(filter(None, [a.get("given"), a.get("family")])) for a in item.get("author", [])]
        out.append({
            "source": "Crossref",
            "title": title,
            "year": year_parts[0][0] if year_parts and year_parts[0] else None,
            "authors": "; ".join(authors),
            "doi": doi_norm(item.get("DOI")),
            "venue": (item.get("container-title") or [""])[0],
            "url": item.get("URL", ""),
            "abstract": abstract,
            "cited_by": item.get("is-referenced-by-count"),
        })
    return out


def openalex(query: str, per_page: int, from_year: int) -> list[dict[str, Any]]:
    url = (
        "https://api.openalex.org/works?search="
        f"{quote(query)}&filter=from_publication_date:{from_year}-01-01&per-page={per_page}"
    )
    payload = get_json(url)
    out = []
    for item in payload.get("results", []):
        authors = [a.get("author", {}).get("display_name", "") for a in item.get("authorships", [])]
        primary = item.get("primary_location") or {}
        source = primary.get("source") or {}
        out.append({
            "source": "OpenAlex",
            "title": item.get("display_name", ""),
            "year": item.get("publication_year"),
            "authors": "; ".join(filter(None, authors)),
            "doi": doi_norm(item.get("doi")),
            "venue": source.get("display_name", ""),
            "url": primary.get("landing_page_url") or item.get("id", ""),
            "abstract": "",  # inverted index intentionally not reconstructed here
            "cited_by": item.get("cited_by_count"),
        })
    return out


def relevant(record: dict[str, Any]) -> bool:
    haystack = norm_text(f"{record.get('title')} {record.get('abstract')}")
    methods = any(k in haystack for k in ("sarimax", "arimax", "seasonal arima", "dynamic regression"))
    domains = any(k in haystack for k in ("forecast", "hydro", "energy", "rain", "precip", "inflation", "climate", "enso"))
    return methods and domains


def dedupe(records: list[dict[str, Any]]) -> list[dict[str, Any]]:
    selected: dict[str, dict[str, Any]] = {}
    for r in records:
        key = f"doi:{r['doi']}" if r.get("doi") else f"title:{norm_text(r.get('title'))}:{r.get('year')}"
        if key not in selected or len(json.dumps(r)) > len(json.dumps(selected[key])):
            selected[key] = r
    return list(selected.values())


def write_outputs(records: list[dict[str, Any]], root: Path, queries: list[str]) -> None:
    raw_dir = root / "references/search_results"
    lit_dir = root / "references/literature"
    raw_dir.mkdir(parents=True, exist_ok=True)
    lit_dir.mkdir(parents=True, exist_ok=True)
    stamp = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
    (raw_dir / f"literature_raw_{stamp}.json").write_text(json.dumps(records, ensure_ascii=False, indent=2), encoding="utf-8")
    fields = ["source", "title", "year", "authors", "doi", "venue", "url", "cited_by", "verified_status"]
    for r in records:
        r["verified_status"] = "metadata_only"
    with (lit_dir / "literature_matrix.csv").open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fields, extrasaction="ignore")
        writer.writeheader(); writer.writerows(records)
    lines = ["# Lista corta de literatura SARIMAX", "", f"Generada: {stamp}", "", "## Consultas", *[f"- {q}" for q in queries], "", "## Resultados"]
    for r in sorted(records, key=lambda x: (x.get("cited_by") or 0), reverse=True)[:20]:
        lines += ["", f"### {r.get('title','Sin título')}", f"- Año: {r.get('year')}", f"- Fuente: {r.get('venue') or r.get('source')}", f"- DOI: {r.get('doi') or 'No identificado'}", f"- Estado: metadata_only; requiere validación de texto completo"]
    (lit_dir / "shortlist.md").write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--config", default="config/literature_search.yaml")
    parser.add_argument("--root", default=".")
    args = parser.parse_args()
    root = Path(args.root).resolve()
    cfg = yaml.safe_load((root / args.config).read_text(encoding="utf-8"))
    queries = cfg["search"]["queries"]
    limit = int(cfg["search"].get("max_results_per_query", 30))
    from_year = int(cfg["search"].get("from_year", 2000))
    records: list[dict[str, Any]] = []
    for query in queries:
        if cfg.get("sources", {}).get("crossref", True):
            records.extend(crossref(query, limit, from_year)); time.sleep(0.2)
        if cfg.get("sources", {}).get("openalex", True):
            records.extend(openalex(query, limit, from_year)); time.sleep(0.2)
    shortlisted = dedupe([r for r in records if relevant(r)])
    write_outputs(shortlisted, root, queries)
    print(f"Saved {len(shortlisted)} deduplicated candidate references.")


if __name__ == "__main__":
    main()

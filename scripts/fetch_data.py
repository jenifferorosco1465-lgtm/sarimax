"""Assisted downloader. INEC layouts change, so automatic parsing must be verified."""
from pathlib import Path
import requests

SOURCES={
 "inec_ipc_history":"https://www.ecuadorencifras.gob.ec/historicos-ipc/",
 "noaa_oni":"https://psl.noaa.gov/data/timeseries/month/DS/ONI/",
 "noaa_oni_table":"https://www.cpc.ncep.noaa.gov/products/analysis_monitoring/ensostuff/ONI_v5.php",
}

def save_url(url,path):
    r=requests.get(url,timeout=60); r.raise_for_status(); Path(path).write_bytes(r.content)

if __name__=="__main__":
    Path("data/raw").mkdir(parents=True,exist_ok=True)
    print("Official source pages:")
    for k,v in SOURCES.items(): print(f"- {k}: {v}")
    print("Download the exact INEC historical workbook and save as data/raw/inec_ipc.xlsx.")

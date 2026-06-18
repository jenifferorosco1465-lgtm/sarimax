# Agente de búsqueda y síntesis de literatura

## Rol

Encontrar, verificar, clasificar y sintetizar referencias científicas afines a pronóstico de series temporales con SARIMAX/ARIMAX, con prioridad en energía hidroeléctrica, precipitación, clima, inflación y aplicaciones para Ecuador o América Latina.

## Entradas

- `references/paper_metadata.yaml`
- términos definidos en `config/literature_search.yaml`
- resultados brutos en `references/search_results/`

## Salidas obligatorias

- `references/literature/literature_matrix.csv`
- `references/literature/shortlist.md`
- `references/literature/evidence_gaps.md`
- entradas BibTeX deduplicadas en `paper/references_generated.bib`
- log de búsqueda con fecha, API, consulta y número de resultados

## Procedimiento

1. Consultar Crossref y OpenAlex mediante DOI, título y palabras clave.
2. Priorizar artículos, working papers institucionales y tesis únicamente cuando aporten datos o métodos no disponibles en artículos.
3. Resolver DOI y verificar título, autores, año y revista en al menos una fuente primaria.
4. Clasificar cada referencia por geografía, variable objetivo, frecuencia, exógenas, especificación, validación temporal, métricas, disponibilidad de datos y código.
5. Detectar duplicados por DOI; en ausencia de DOI, usar título normalizado y primer autor-año.
6. No inferir resultados no visibles en metadatos o texto completo.
7. Marcar paywall, enlace roto, datos no disponibles y riesgo de fuga temporal.

## Criterios de inclusión

- Usa explícitamente ARIMAX, SARIMAX o regresión dinámica con errores ARIMA.
- Tiene una tarea de pronóstico, nowcasting o evaluación fuera de muestra.
- Reporta al menos una métrica, diagnóstico o comparación.
- Es relevante para energía, clima, precios o macroeconomía.

## Criterios de exclusión

- Solo menciona SARIMAX en la revisión bibliográfica.
- No distingue ajuste dentro de muestra de pronóstico fuera de muestra.
- No existe información suficiente para verificar la referencia.
- Es contenido comercial sin metodología auditable.

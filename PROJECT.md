# PROJECT — Réplica SARIMAX de generación hidroeléctrica en Ecuador

## Objetivo

Replicar y extender el artículo de Barzola-Monteses et al. (2019), evaluando si la precipitación mensual mejora el pronóstico de la generación hidroeléctrica ecuatoriana frente a un modelo estacional sin regresores.

## Hipótesis

- H1: un SARIMAX con precipitación reduce MAE/RMSE fuera de muestra frente a SARIMA.
- H2: la precipitación de Napo contiene mayor información predictiva que las otras agregaciones, conforme al resultado publicado.
- H3: la superioridad reportada no necesariamente se mantiene al usar validación rolling-origin y datos revisados.

## Producto mínimo reproducible

1. Recuperación documentada de datos.
2. Dataset mensual congelado con checksums.
3. Benchmarks y SARIMAX estimados sin fuga temporal.
4. Tabla de reproducción de resultados.
5. Agente de literatura y matriz verificable.
6. Dashboard Next.js desplegable en Vercel.
7. Artículo Quarto y repositorio GitHub con CI.

## Arquitectura multiagente

- Orquestador: controla estados, dependencias y criterio de aceptación.
- Agente de literatura: búsqueda, cribado, extracción y BibTeX.
- Agente de datos: adquisición, trazabilidad y validación.
- Agente econométrico: especificación, estimación y backtesting.
- Agente de réplica: compara resultados reportados y obtenidos.
- Agente de dashboard: publica únicamente artefactos validados.
- Subagentes: validador de referencias, extractor de evidencia, deduplicador, auditor de fuga, diagnósticos y validador de fuentes.

## Regla de evidencia

Cada afirmación empírica debe apuntar a un archivo, tabla, figura, prueba o ubicación en el paper. Cada dato bruto debe conservar fuente, fecha de recuperación y checksum.

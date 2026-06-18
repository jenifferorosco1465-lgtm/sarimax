# Backlog ejecutable

## Épica 0 — Gobernanza
- [ ] T000 fijar DOI, metadatos y versión del paper base.
- [ ] T001 crear registro de decisiones y convenciones de nombres.
- [ ] T002 registrar entorno Python/Node y checksums.

## Épica 1 — Literatura
- [ ] T100 ejecutar `python scripts/literature_agent.py`.
- [ ] T101 validar texto completo de las 20 referencias mejor clasificadas.
- [ ] T102 completar matriz con muestra, frecuencia, exógenas, orden, validación y métricas.
- [ ] T103 identificar al menos cinco estudios de América Latina y tres de Ecuador.
- [ ] T104 generar mapa de vacíos y contribución de la extensión.

## Épica 2 — Recuperación de datos originales
- [ ] T200 localizar series ARCONEL 2000–2015 y registrar documento/fuente.
- [ ] T201 solicitar o descargar datos INAMHI de estaciones de Napo, Pastaza y Santiago.
- [ ] T202 reconstruir catálogo de estaciones y cobertura temporal.
- [ ] T203 generar SHA-256 de cada archivo bruto.
- [ ] T204 documentar divergencias entre datos originales, revisados y proxies.

## Épica 3 — Ingeniería de datos
- [ ] T300 validar unidades, frecuencia, duplicados y faltantes.
- [ ] T301 agregar precipitación por cuenca y mes.
- [ ] T302 construir precipitación total media.
- [ ] T303 unir generación y precipitación sin interpolación silenciosa.
- [ ] T304 congelar dataset analítico y diccionario.

## Épica 4 — Réplica econométrica
- [ ] T400 reproducir SARIMA/ARIMA benchmark.
- [ ] T401 estimar ARIMAX (1,1,1)(1,0,0)[12] para cada cuenca.
- [ ] T402 validar 2015 como holdout intacto.
- [ ] T403 calcular MAE, RMSE, MAPE y MASE.
- [ ] T404 ejecutar Ljung–Box, normalidad, heterocedasticidad y estabilidad.
- [ ] T405 comparar resultados con tablas reportadas y explicar diferencias.

## Épica 5 — Extensión
- [ ] T500 actualizar muestra hasta el último mes disponible.
- [ ] T501 evaluar rezagos de precipitación definidos antes del holdout.
- [ ] T502 ejecutar rolling-origin para horizontes 1, 3, 6 y 12.
- [ ] T503 comparar con seasonal naïve, ETS y SARIMA sin exógenas.
- [ ] T504 evaluar pronósticos bajo escenarios de precipitación futura.

## Épica 6 — Dashboard y publicación
- [ ] T600 exportar JSON auditado al dashboard.
- [ ] T601 mostrar datos, faltantes, ajuste, forecast, intervalos y diagnósticos.
- [ ] T602 publicar dashboard en Vercel desde `dashboard/`.
- [ ] T603 crear repositorio GitHub y activar CI.
- [ ] T604 generar release con código, datos permitidos, resultados y artículo Quarto.

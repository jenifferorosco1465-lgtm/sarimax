# Paper base seleccionado

## Referencia

Barzola-Monteses, J., Martínez-López, M., Espinoza-Andaluz, M., Gómez-Romero, J., & Fajardo, W. (2019). *Time Series Analysis for Predicting Hydroelectric Power Production: The Ecuador Case*. Sustainability, 11(23), 6539. https://doi.org/10.3390/su11236539

## Por qué es el paper base

1. Es un artículo revisado por pares y de acceso abierto.
2. La aplicación es directamente para Ecuador.
3. Usa frecuencia mensual, estacionalidad anual y una variable exógena económicamente interpretable.
4. Compara ARIMA/SARIMA frente a ARIMAX, lo que permite una réplica escalonada.
5. Reporta orden, ventana de estimación, muestra de validación y métricas de pronóstico.

## Diseño reportado

- Objetivo: producción hidroeléctrica mensual bruta, en GWh.
- Periodo de modelación: enero de 2000 a diciembre de 2014.
- Validación: los doce meses de 2015.
- Regresores: precipitación media mensual de las cuencas Napo, Pastaza y Santiago.
- Especificación destacada: ARIMAX (1,1,1)(1,0,0)[12] con precipitación de Napo.
- Resultado reportado: MAE 70.81 GWh, MAPE 10.17% y MASE 0.57.

## Clasificación honesta de la réplica

- **Exacta**: solo cuando se recuperen las mismas series de ARCONEL e INAMHI, se documenten las estaciones y se reproduzcan las transformaciones.
- **Reconstruida**: si se usan series oficiales equivalentes, pero con revisiones o agregaciones posteriores.
- **Conceptual**: si se emplean proxies públicos, por ejemplo generación de CENACE y precipitación satelital CHIRPS/ERA5.
- **Extensión**: actualización de la muestra y comparación con SARIMAX moderno, ETS, Prophet, XGBoost o modelos bayesianos.

No se etiquetará como réplica exacta por entusiasmo administrativo. La etiqueta la deciden los datos y los checksums.

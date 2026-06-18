# Metodología

Se estimará un modelo SARIMAX(p,d,q)(P,D,Q)[12] con regresores exógenos X_t:

 y_t = c + β'X_t + n_t,

 φ(B)Φ(B^12)(1-B)^d(1-B^12)^D n_t = θ(B)Θ(B^12)ε_t.

La selección inicial usa AIC dentro de una rejilla acotada. La comparación sustantiva se basa en evaluación fuera de muestra con origen móvil. Se reportan MAE, RMSE, MASE, sMAPE, cobertura de intervalos y, cuando exista suficiente número de errores, prueba Diebold-Mariano.

Precauciones: no usar variables exógenas futuras observadas al evaluar un escenario realista; separar el escenario “exógena conocida” del escenario “exógena pronosticada”; evitar selección de rezagos usando toda la muestra; verificar raíces, residuos, cambios estructurales y sensibilidad a 2020.

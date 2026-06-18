from itertools import product
import warnings
from statsmodels.tsa.statespace.sarimax import SARIMAX

def grid_search(y, X, grid: dict, seasonal_period: int, criterion: str = "aic"):
    best=None
    for p,d,q,P,D,Q in product(grid["p"],grid["d"],grid["q"],grid["P"],grid["D"],grid["Q"]):
        try:
            with warnings.catch_warnings():
                warnings.simplefilter("ignore")
                fit=SARIMAX(y, exog=X, order=(p,d,q), seasonal_order=(P,D,Q,seasonal_period),
                            enforce_stationarity=False, enforce_invertibility=False).fit(disp=False)
            score=float(getattr(fit, criterion))
            if best is None or score < best["score"]:
                best={"fit":fit,"score":score,"order":(p,d,q),"seasonal_order":(P,D,Q,seasonal_period)}
        except Exception:
            continue
    if best is None:
        raise RuntimeError("No SARIMAX specification converged")
    return best

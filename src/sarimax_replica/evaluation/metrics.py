import numpy as np

def forecast_metrics(actual, pred, seasonal_scale=None):
    a=np.asarray(actual,float); p=np.asarray(pred,float); e=a-p
    mae=float(np.mean(np.abs(e))); rmse=float(np.sqrt(np.mean(e**2)))
    denom=(np.abs(a)+np.abs(p))/2
    smape=float(np.mean(np.where(denom==0,0,np.abs(e)/denom))*100)
    out={"mae":mae,"rmse":rmse,"smape":smape}
    if seasonal_scale and seasonal_scale>0: out["mase"]=mae/seasonal_scale
    return out

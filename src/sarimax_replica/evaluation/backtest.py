import pandas as pd
from sarimax_replica.models.baselines import seasonal_naive
from sarimax_replica.models.sarimax import grid_search
from sarimax_replica.evaluation.metrics import forecast_metrics

def run_backtest(df, feature_cols, cfg):
    initial=cfg["validation"]["initial_train"]; horizon=cfg["validation"]["horizon"]; step=cfg["validation"]["step"]
    season=cfg["features"]["seasonal_period"]; rows=[]; forecasts=[]
    for end in range(initial, len(df)-horizon+1, step):
        tr=df.iloc[:end]; te=df.iloc[end:end+horizon]
        naive=seasonal_naive(tr.y, horizon, season)
        candidates={"seasonal_naive":naive}
        best=grid_search(tr.y, tr[feature_cols], cfg["models"]["sarima_grid"], season, cfg["models"]["criterion"] )
        candidates["sarimax"]=best["fit"].get_forecast(steps=horizon, exog=te[feature_cols]).predicted_mean.to_numpy()
        for model,pred in candidates.items():
            met=forecast_metrics(te.y,pred)
            rows.append({"origin":str(tr.date.iloc[-1].date()),"model":model,**met})
            for date,a,p in zip(te.date,te.y,pred): forecasts.append({"origin":str(tr.date.iloc[-1].date()),"date":str(date.date()),"model":model,"actual":float(a),"forecast":float(p)})
    return pd.DataFrame(rows), pd.DataFrame(forecasts)

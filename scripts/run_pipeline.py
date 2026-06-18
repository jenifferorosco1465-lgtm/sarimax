import argparse, json, sys
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/"src"))
import pandas as pd
from sarimax_replica.utils.config import load_config
from sarimax_replica.data.loaders import load_table
from sarimax_replica.data.validation import validate_monthly
from sarimax_replica.features.build import build_features
from sarimax_replica.evaluation.backtest import run_backtest
from sarimax_replica.reporting.export import export_records

def main(config_path):
    cfg=load_config(config_path); d=cfg["data"]
    target=load_table(d["target_file"]); exog=load_table(d["exog_file"])
    target[d["date_column"]]=pd.to_datetime(target[d["date_column"]]); exog[d["date_column"]]=pd.to_datetime(exog[d["date_column"]])
    cols=[d["date_column"],d["target_column"]]
    if Path(d["target_file"]).resolve()==Path(d["exog_file"]).resolve():
        df=target[[*cols,*d["exog_columns"]]].copy()
    else:
        df=target[cols].merge(exog[[d["date_column"],*d["exog_columns"]]],on=d["date_column"],how="inner")
    df=df.sort_values(d["date_column"]).rename(columns={d["date_column"]:"date"})
    issues=validate_monthly(df,"date",[d["target_column"],*d["exog_columns"]])
    if issues: raise ValueError("; ".join(issues))
    f=build_features(df,d["target_column"],d["exog_columns"],cfg["features"]["exog_lags"],cfg["features"]["target_transform"] )
    feature_cols=[c for c in f if "_lag_" in c]
    metrics, forecasts=run_backtest(f,feature_cols,cfg)
    out=Path(cfg["outputs"]["root"]); out.mkdir(exist_ok=True)
    metrics.to_csv(out/"tables/backtest_metrics.csv",index=False); forecasts.to_csv(out/"forecasts/backtest_forecasts.csv",index=False)
    dash=Path(cfg["outputs"]["dashboard"]); export_records(metrics,dash/"metrics.json"); export_records(forecasts,dash/"forecasts.json")
    summary=metrics.groupby("model")[["mae","rmse","smape"]].mean().reset_index()
    export_records(summary,dash/"summary.json")
    print(summary.to_string(index=False))

if __name__=="__main__":
    p=argparse.ArgumentParser(); p.add_argument("--config",required=True); a=p.parse_args(); main(a.config)

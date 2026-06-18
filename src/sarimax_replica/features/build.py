import pandas as pd
import numpy as np

def build_features(df: pd.DataFrame, target: str, exogs: list[str], lags: list[int], transform: str) -> pd.DataFrame:
    out=df.copy()
    if transform == "log_diff_100":
        out["y"] = 100 * np.log(out[target]).diff()
    elif transform == "level":
        out["y"] = out[target]
    else:
        raise ValueError(f"Unknown target transform: {transform}")
    for col in exogs:
        for lag in lags:
            out[f"{col}_lag_{lag}"] = out[col].shift(lag)
    return out.dropna().reset_index(drop=True)

import pandas as pd
from sarimax_replica.features.build import build_features

def test_lags_created():
    df=pd.DataFrame({"ipc":[100,101,102,103],"oni":[0,1,2,3]})
    out=build_features(df,"ipc",["oni"],[0,1],"level")
    assert {"oni_lag_0","oni_lag_1","y"}.issubset(out.columns)

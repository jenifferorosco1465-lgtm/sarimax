from pathlib import Path
import numpy as np, pandas as pd
rng=np.random.default_rng(2026)
date=pd.date_range("2005-01-01","2025-12-01",freq="MS")
t=np.arange(len(date)); oni=0.8*np.sin(2*np.pi*t/48)+rng.normal(0,.25,len(t))
infl=.18+.15*np.sin(2*np.pi*t/12)+.08*np.roll(oni,3)+rng.normal(0,.12,len(t))
ipc=100*np.exp(np.cumsum(infl/100))
df=pd.DataFrame({"date":date,"ipc":ipc,"oni":oni})
Path("data/raw").mkdir(parents=True,exist_ok=True)
df.to_csv("data/raw/demo_monthly.csv",index=False)
print("Created data/raw/demo_monthly.csv")

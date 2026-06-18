from pathlib import Path
import json

def export_records(df, path):
    path=Path(path); path.parent.mkdir(parents=True,exist_ok=True)
    path.write_text(json.dumps(df.to_dict(orient="records"),ensure_ascii=False,indent=2),encoding="utf-8")

import pandas as pd

def validate_monthly(df: pd.DataFrame, date_col: str, required: list[str]) -> list[str]:
    issues=[]
    if date_col not in df: issues.append(f"missing date column: {date_col}")
    for col in required:
        if col not in df: issues.append(f"missing column: {col}")
    if issues: return issues
    dates=pd.to_datetime(df[date_col], errors="coerce")
    if dates.isna().any(): issues.append("invalid dates")
    if dates.duplicated().any(): issues.append("duplicate dates")
    if not dates.is_monotonic_increasing: issues.append("dates not sorted")
    return issues

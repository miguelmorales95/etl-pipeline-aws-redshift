import pandas as pd

def clean_dataframe(df: pd.DataFrame) -> pd.DataFrame:
    """Simple cleaning logic: drop nulls, cast columns."""
    df = df.dropna()
    # Example: ensure column names are lowercase
    df.columns = [c.lower() for c in df.columns]
    return df

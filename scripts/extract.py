import pandas as pd

def extract_from_csv(path: str) -> pd.DataFrame:
    """Read a CSV file into a DataFrame."""
    return pd.read_csv(path)

import pandas as pd
from scripts.transform import clean_dataframe

def test_clean_dataframe():
    raw = pd.DataFrame({
        "ID": [1, 2, None],
        "Name": ["Alice", "Bob", "Charlie"]
    })
    clean = clean_dataframe(raw)
    assert "id" in clean.columns
    assert "name" in clean.columns
    assert clean.shape[0] == 2

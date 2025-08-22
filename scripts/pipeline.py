from scripts.extract import extract_from_csv
from scripts.transform import clean_dataframe
from scripts.load import load_to_redshift

def run_pipeline():
    df = extract_from_csv("data/input.csv")
    df_clean = clean_dataframe(df)
    load_to_redshift(df_clean, table="demo_table")

if __name__ == "__main__":
    run_pipeline()

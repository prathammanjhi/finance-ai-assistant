import pandas as pd

from pathlib import Path

BASE_DIR = Path(__file__).resolve().parents[3]

file_path = BASE_DIR / "data" / "healthy.xlsx"

def load_commitments():
    # file_path = "data/finance.xlsx"

    df = pd.read_excel(file_path, sheet_name="Financial Commitments")
    df = df.dropna(how="all")

    return df
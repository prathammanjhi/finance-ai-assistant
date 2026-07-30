import pandas as pd

from pathlib import Path

BASE_DIR = Path(__file__).resolve().parents[3]

file_path = BASE_DIR / "data" / "healthy.xlsx"

def load_assets():
    df = pd.read_excel(file_path, sheet_name="Assets")
    df = df.dropna(how="all")

    return df
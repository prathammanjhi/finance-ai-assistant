import pandas as pd

from pathlib import Path

BASE_DIR = Path(__file__).resolve().parents[3]

file_path = BASE_DIR / "data" / "healthy.xlsx"


def load_transactions():
    # file_path = "data/finance.xlsx"

    df = pd.read_excel(file_path, sheet_name="Transactions")
    df = df.dropna(how="all")
    df = df[df["Date"].notna()]
    df["Need/Want"] = df["Need/Want"].astype(str).str.strip().str.title()
    df["Date"] = pd.to_datetime(df["Date"])

    return df

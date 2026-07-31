import pandas as pd

from src.shared.paths import DATA_FILE


def load_transactions():
    # file_path = "data/finance.xlsx"

    df = pd.read_excel(DATA_FILE, sheet_name="Transactions")
    df = df.dropna(how="all")
    df = df[df["Date"].notna()]
    df["Need/Want"] = df["Need/Want"].astype(str).str.strip().str.title()
    df["Date"] = pd.to_datetime(df["Date"])

    return df

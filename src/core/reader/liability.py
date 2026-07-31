import pandas as pd

from src.shared.paths import DATA_FILE

def load_liabilities():
    df = pd.read_excel(DATA_FILE, sheet_name="Liabilities")
    df = df.dropna(how="all")
    df["Category"] = df["Category"].fillna("Other").astype(str).str.strip()
    return df
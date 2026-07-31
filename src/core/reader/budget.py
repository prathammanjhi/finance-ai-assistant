import pandas as pd

from src.shared.paths import DATA_FILE

def load_budget():
    # file_path = "data/finance.xlsx"

    df = pd.read_excel(DATA_FILE, sheet_name="Budget Sheet")
    df = df.dropna(how="all")

    return df
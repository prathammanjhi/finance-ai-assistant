import pandas as pd

from src.shared.paths import DATA_FILE

def load_investments():
    df = pd.read_excel(DATA_FILE, sheet_name="Investments")
    df = df.dropna(how="all")

    return df

import pandas as pd


def load_transactions():
    file_path = "data/finance.xlsx"

    df = pd.read_excel(file_path, sheet_name="Transactions")
    df = df.dropna(how="all")
    df = df[df["Date"].notna()]
    df["Need/Want"] = (
    df["Need/Want"]
    .astype(str)
    .str.strip()
    .str.title()
    )

    return df

def load_income():
    file_path = "data/finance.xlsx"

    df = pd.read_excel(file_path, sheet_name="Dashboard")

    return df

def load_commitments():
    file_path = "data/finance.xlsx"

    df = pd.read_excel(
        file_path,
        sheet_name="Finance Commitments"
    )
    df = df.dropna(how="all")

    return df
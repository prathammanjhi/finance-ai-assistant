import pandas as pd

file_path = "data/finance.xlsx"


def load_transactions():
    # file_path = "data/finance.xlsx"

    df = pd.read_excel(file_path, sheet_name="Transactions")
    df = df.dropna(how="all")
    df = df[df["Date"].notna()]
    df["Need/Want"] = df["Need/Want"].astype(str).str.strip().str.title()
    df["Date"] = pd.to_datetime(df["Date"])

    return df


def load_income():
    # file_path = "data/finance.xlsx"

    df = pd.read_excel(file_path, sheet_name="Income")
    df = df.dropna(how="all")

    return df


def load_commitments():
    # file_path = "data/finance.xlsx"

    df = pd.read_excel(file_path, sheet_name="Financial Commitments")
    df = df.dropna(how="all")

    return df


def load_budget():
    # file_path = "data/finance.xlsx"

    df = pd.read_excel(file_path, sheet_name="Budget Sheet")
    df = df.dropna(how="all")

    return df

def load_goals():
    # file_path = "data/finance.xlsx"

    df = pd.read_excel(file_path, sheet_name="Financial Goals")
    df = df.dropna(how="all")

    return df

def load_investments():
    df = pd.read_excel(file_path, sheet_name="Investments")
    df = df.dropna(how="all")

    return df

def load_assets():
    df = pd.read_excel(file_path, sheet_name="Assets")
    df = df.dropna(how="all")

    return df

def load_liabilities():
    df = pd.read_excel(file_path, sheet_name="Liabilities")
    df = df.dropna(how="all")
    df["Category"] = (
    df["Category"]
        .fillna("Other")
        .astype(str)
        .str.strip()
    )
    return df
def calculate_summary(transactions):
    total_expense = transactions["Amount"].sum()

    total_need = transactions.loc[
        transactions["Need/Want"] == "Need", "Amount"
    ].sum()

    total_want = transactions.loc[
        transactions["Need/Want"] == "Want", "Amount"
    ].sum()

    return {
        "total_expense": total_expense,
        "total_need": total_need,
        "total_want": total_want,
    }
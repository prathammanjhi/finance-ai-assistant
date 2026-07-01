def calculate_summary(transactions):
    total_expense = transactions["Amount"].sum()

    total_need = transactions.loc[transactions["Need/Want"] == "Need", "Amount"].sum()

    total_want = transactions.loc[transactions["Need/Want"] == "Want", "Amount"].sum()

    return {
        "total_expense": total_expense,
        "total_need": total_need,
        "total_want": total_want,
    }


def calculate_income(income):

    received_income = income.loc[income["Status"] == "Received", "Amount"].sum()

    pending_income = income.loc[income["Status"] == "Pending", "Amount"].sum()

    return {"received_income": received_income, "pending_income": pending_income}


def calculate_commitments(commitments):

    total_borrowed = commitments["Amount"].sum()

    total_repaid = commitments["Repaid"].sum()

    outstanding_debt = commitments["Remaining"].sum()

    active_commitments = len(commitments.loc[commitments["Status"] == "Active"])

    return {
        "total_borrowed": total_borrowed,
        "total_repaid": total_repaid,
        "outstanding_debt": outstanding_debt,
        "active_commitments": active_commitments,
    }


def calculate_net_balance(received_income, total_expense, total_commitments):
    return received_income - total_expense - total_commitments

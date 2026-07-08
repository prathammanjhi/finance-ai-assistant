import pandas as pd


# ==========================
# Expense Analytics
# ==========================
def calculate_summary(transactions):
    total_expense = transactions["Amount"].sum()

    total_need = transactions.loc[transactions["Need/Want"] == "Need", "Amount"].sum()

    total_want = transactions.loc[transactions["Need/Want"] == "Want", "Amount"].sum()

    return {
        "total_expense": total_expense,
        "total_need": total_need,
        "total_want": total_want,
    }


def calculate_expense_distribution(calculate_summary):

    total_expense = calculate_summary["total_expense"]
    total_need = calculate_summary["total_need"]
    total_want = calculate_summary["total_want"]
    if total_expense == 0:
        return {
            "need_amount": total_need,
            "want_amount": total_want,
            "need_percentage": 0,
            "want_percentage": 0,
        }
    else:
        need_percentage = (total_need / total_expense) * 100
        want_percentage = (total_want / total_expense) * 100

        return {
            "need_amount": total_need,
            "want_amount": total_want,
            "need_percentage": need_percentage,
            "want_percentage": want_percentage,
        }


# ==========================
# Income Analytics
# ==========================
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


def calculate_net_position(income_summary, expense_summary, commitment_summary):
    net_position = (
        income_summary["received_income"]
        - expense_summary["total_expense"]
        - commitment_summary["outstanding_debt"]
    )
    cash_position = income_summary["received_income"] - expense_summary["total_expense"]
    expected_position = (
        cash_position
        - commitment_summary["outstanding_debt"]
        + income_summary["pending_income"]
    )

    return {
        "net_position": net_position,
        "cash_position": cash_position,
        "expected_position": expected_position,
    }


def calculate_expense_by_category(transactions):
    expense_by_category = transactions.groupby("Category")["Amount"].sum()
    return expense_by_category


def calculate_highest_spending_category(category_summary):
    if not category_summary.empty:
        highest_category = category_summary.idxmax()
        highest_amount = category_summary.max()
        return {
            "category": highest_category,
            "amount": highest_amount,
        }
    else:
        return {
            "category": None,
            "amount": 0,
        }


def calculate_top_categories(category_summary):
    sorted_categories = category_summary.sort_values(ascending=False)
    top_categories = sorted_categories[:3]
    return {"categories": top_categories}


# ==========================
# Date Filtering
# ==========================
def filter_transactions_by_date(transactions, month=None, year=None):
    """
    Filters transactions by month and year.

    If no month or year is provided,
    current month and year are used.
    """

    today = pd.Timestamp.now()

    # Case 1
    if month is not None and year is not None:
        return transactions[
            (transactions["Date"].dt.month == month)
            & (transactions["Date"].dt.year == year)
        ]

    # Case 2
    if month is not None:
        return transactions[
            (transactions["Date"].dt.month == month)
            & (transactions["Date"].dt.year == today.year)
        ]

    # Case 3
    if year is not None:
        return transactions[transactions["Date"].dt.year == year]

    # Case 4 (Default)
    return transactions[
        (transactions["Date"].dt.month == today.month)
        & (transactions["Date"].dt.year == today.year)
    ]


def generate_financial_snapshot(
    monthly_summary,
    monthly_distribution,
    income_summary,
    commitment_summary,
    financial_position,
):
    snapshot = {
        "monthly_summary": monthly_summary,
        "monthly_distribution": monthly_distribution,
        "income_summary": income_summary,
        "commitment_summary": commitment_summary,
        "financial_position": financial_position,
    }

    return snapshot


def generate_financial_insights(financial_snapshot):

    monthly_distribution = financial_snapshot["monthly_distribution"]
    need_percentage = monthly_distribution["need_percentage"]

    if need_percentage > 70:
        need_status = "Healthy"
        need_priority = "Low"
        need_reason = "You are spending a significant portion of your income on essential needs, which is a positive financial behavior."
    elif 50 <= need_percentage <= 70:
        need_status = "Balanced"
        need_priority = "Medium"
        need_reason = (
            "You are balancing your spending between essential needs and wants."
        )
    else:
        need_status = "Low"
        need_priority = "High"
        need_reason = "Your Essential spending is lower than recommended."

    want_percentage = monthly_distribution["want_percentage"]

    if want_percentage < 30:
        want_status = "Excellent"
        want_priority = "Low"
        want_reason = "You are spending a smaller portion of your income on discretionary wants, which is a positive financial behavior."
    elif 30 <= want_percentage <= 50:
        want_status = "Balanced"
        want_priority = "Medium"
        want_reason = (
            "You are balancing your spending between essential needs and wants."
        )
    else:
        want_status = "Unhealthy"
        want_priority = "High"
        want_reason = (
            "You are spending a large portion of your income on discretionary wants."
        )

    cash_position = financial_snapshot["financial_position"]["cash_position"]

    if cash_position > 0:
        cash_flow_status = "Positive Cash Flow"
        cash_flow_priority = "Low"
        cash_flow_reason = "You have a positive cash flow, indicating that your income exceeds your expenses. This is a healthy financial situation."
    elif cash_position == 0:
        cash_flow_status = "Break-even"
        cash_flow_priority = "Medium"
        cash_flow_reason = (
            "Your income equals your expenses, resulting in no net gain or loss."
        )
    else:
        cash_flow_status = "Negative Cash Flow"
        cash_flow_priority = "High"
        cash_flow_reason = (
            "Your expenses exceed your income, leading to a negative cash flow."
        )

    net_position = financial_snapshot["financial_position"]["net_position"]

    if net_position > 0:
        net_position_status = "Financially Healthy"
        net_position_priority = "Low"
        net_position_reason = "You have a positive net position, indicating that your assets exceed your liabilities. This is a healthy financial situation."
    elif net_position == 0:
        net_position_status = "Neutral"
        net_position_priority = "Medium"
        net_position_reason = "Your assets equal your liabilities."
    else:
        net_position_status = "Financially Stressed"
        net_position_priority = "High"
        net_position_reason = "Your liabilities exceed your assets, indicating a financially stressful situation."

    outstanding_debt = financial_snapshot["commitment_summary"]["outstanding_debt"]

    if outstanding_debt == 0:
        outstanding_debt_status = "Debt-Free"
        outstanding_debt_priority = "Low"
        outstanding_debt_reason = "You are not carrying any outstanding debt."
    else:
        outstanding_debt_status = "Active Debt"
        outstanding_debt_priority = "High"
        outstanding_debt_reason = (
            "You have outstanding debt that needs to be addressed."
        )

    insights = {
        "📌 Need Spending": {
            "status": need_status,
            "priority": need_priority,
            "reason": need_reason,
        },
        "📌 Want Spending": {
            "status": want_status,
            "priority": want_priority,
            "reason": want_reason,
        },
        "📌 Cash Flow": {
            "status": cash_flow_status,
            "priority": cash_flow_priority,
            "reason": cash_flow_reason,
        },
        "📌 Net Position": {
            "status": net_position_status,
            "priority": net_position_priority,
            "reason": net_position_reason,
        },
        "📌 Debt Status": {
            "status": outstanding_debt_status,
            "priority": outstanding_debt_priority,
            "reason": outstanding_debt_reason,
        },
    }

    return insights

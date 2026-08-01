from src.core.reader import (
    load_transactions,
    load_income,
    load_commitments,
)

from src.core.analyzer import (
    calculate_summary,
    calculate_income,
    calculate_commitments,
    calculate_net_position,
    calculate_expense_by_category,
    calculate_highest_spending_category,
    calculate_top_categories,
    filter_transactions_by_date,
    calculate_expense_distribution,
    calculate_savings,
    generate_financial_snapshot,
    generate_financial_insights,
)

def process_financial():
    transactions = load_transactions()
    income = load_income()
    commitments = load_commitments()
    summary = calculate_summary(transactions)
    income_summary = calculate_income(income)
    commitment_summary = calculate_commitments(commitments)
    financial_position = calculate_net_position(
        income_summary,
        summary,
        commitment_summary,
    )
    category_summary = calculate_expense_by_category(transactions)
    highest_spending = calculate_highest_spending_category(category_summary)
    top_three_categories = calculate_top_categories(category_summary)

    monthly_transactions = filter_transactions_by_date(transactions)
    monthly_summary = calculate_summary(monthly_transactions)
    monthly_distribution = calculate_expense_distribution(monthly_summary)
    savings_summary = calculate_savings(
        income_summary, 
        summary, 
        commitment_summary,
        )
    financial_snapshot = generate_financial_snapshot(
        monthly_summary,
        monthly_distribution,
        income_summary,
        commitment_summary,
        financial_position,
        savings_summary,
        highest_spending,
        top_three_categories,
    )
    financial_insights = generate_financial_insights(financial_snapshot)

    financial_snapshot["insights"] = financial_insights

    return {
        "summary": summary,
        "income_summary": income_summary,
        "commitment_summary": commitment_summary,
        "financial_position": financial_position,
        "monthly_summary": monthly_summary,
        "monthly_distribution": monthly_distribution,
        "savings_summary": savings_summary,
        "financial_snapshot": financial_snapshot,
    }
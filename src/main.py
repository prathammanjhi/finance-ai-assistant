from reader import (
    load_transactions,
    load_income,
    load_commitments,
)
from analyzer import (
    calculate_summary,
    calculate_income,
    calculate_commitments,
    calculate_net_position,
    calculate_expense_by_category,
    calculate_highest_spending_category,
    calculate_top_categories,
)


def main():
    print("=" * 40)
    print("📊 Finance AI Assistant")
    print("=" * 40)

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

    print("\n📊 Summary")
    print(f"Total Expense : ₹{summary['total_expense']:,.2f}")
    print(f"Need Spending : ₹{summary['total_need']:,.2f}")
    print(f"Want Spending : ₹{summary['total_want']:,.2f}")
    print("\n💵 Income Summary")
    print(f"Received Income : ₹{income_summary['received_income']:,.2f}")
    print(f"Pending Income : ₹{income_summary['pending_income']:,.2f}")
    print("\n💳 Commitments Summary")
    print(f"Total Borrowed : ₹{commitment_summary['total_borrowed']:,.2f}")
    print(f"Total Repaid : ₹{commitment_summary['total_repaid']:,.2f}")
    print(f"Outstanding Debt : ₹{commitment_summary['outstanding_debt']:,.2f}")
    print(f"Active Commitments : {commitment_summary['active_commitments']}")
    print("\n📈 Net Position")
    print(f"Net Position : ₹{financial_position['net_position']:,.2f}")
    print(f"Cash Position : ₹{financial_position['cash_position']:,.2f}")
    print(f"Expected Position : ₹{financial_position['expected_position']:,.2f}")
    print("\n📊 Expense by Category")
    for category, amount in category_summary.items():
        print(f"{category:<15} : ₹{amount:,.2f}")
    print("\n🏆 Highest Spending Category")
    print(highest_spending["category"])
    print(f"₹{highest_spending['amount']:,.2f}")
    print("\n🏆 Top 3 Spending Categories")
    for top_three_category, amount in top_three_categories["categories"].items():
        print(f"{top_three_category:<15} : ₹{amount:,.2f}")


if __name__ == "__main__":
    main()

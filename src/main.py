from reader import (
    load_transactions,
    load_income,
    load_commitments,
)
from analyzer import (
    calculate_summary,
    calculate_income,
    calculate_commitments,
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



if __name__ == "__main__":
    main()
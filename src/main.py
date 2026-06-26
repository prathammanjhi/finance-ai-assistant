from reader import (
    load_transactions,
    load_income,
    load_commitments,
)
from analyzer import calculate_summary


def main():
    print("=" * 40)
    print("📊 Finance AI Assistant")
    print("=" * 40)

    transactions = load_transactions()
    income = load_income()
    commitments = load_commitments()

    summary = calculate_summary(transactions)

    print("\n📊 Summary")
    print(f"Total Expense : ₹{summary['total_expense']:,.2f}")
    print(f"Need Spending : ₹{summary['total_need']:,.2f}")
    print(f"Want Spending : ₹{summary['total_want']:,.2f}")

    print(transactions.head())
    print("\nTotal Transactions:", len(transactions))

    print("\nIncome Sheet")
    print(income.head())

    print("\nCommitments")
    print(commitments.head())


if __name__ == "__main__":
    main()

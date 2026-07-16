from reader import (
    load_transactions,
    load_income,
    load_commitments,
    load_budget,
    load_goals,
)
from analyzer import (
    calculate_summary,
    calculate_income,
    calculate_commitments,
    calculate_net_position,
    calculate_expense_by_category,
    calculate_highest_spending_category,
    calculate_top_categories,
    calculate_expense_distribution,
    filter_transactions_by_date,
    generate_financial_snapshot,
    generate_financial_insights,
    calculate_budget_analysis,
    filter_budget_by_date,
    budget_insights,
    calculate_savings,
    calculate_emergency_fund,
    calculate_goals,
    generate_goal_snapshot,
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
    expense_distribution = calculate_expense_distribution(summary)
    monthly_transactions = filter_transactions_by_date(transactions)
    monthly_summary = calculate_summary(monthly_transactions)
    monthly_distribution = calculate_expense_distribution(monthly_summary)
    savings_summary = calculate_savings(income_summary, summary, commitment_summary)
    financial_snapshot = generate_financial_snapshot(
        monthly_summary,
        monthly_distribution,
        income_summary,
        commitment_summary,
        financial_position,
        savings_summary,
    )
    financial_insights = generate_financial_insights(financial_snapshot)
    budget = load_budget()
    budget_analysis = calculate_budget_analysis(budget, monthly_summary)
    filtered_budget = filter_budget_by_date(budget)
    budget_analysis = calculate_budget_analysis(
        filtered_budget,
        monthly_summary,
    )
    budget_insight = budget_insights(budget_analysis)
    emergency_fund = calculate_emergency_fund(
        summary, commitment_summary, savings_summary
    )
    goals = load_goals()
    goal_analysis = calculate_goals(goals)
    goal_analysis, goal_summary = calculate_goals(goals)
    goal_snapshot = generate_goal_snapshot(
    goal_analysis,
    goal_summary
)

    print("\n📊 Summary")
    print(f"Total Expense : ₹{summary['total_expense']:,.2f}")
    print(f"Need Spending : ₹{summary['total_need']:,.2f}")
    print(f"Want Spending : ₹{summary['total_want']:,.2f}")

    print("\n💵 Income Summary")
    print(f"Received Income : ₹{income_summary['received_income']:,.2f}")
    print(f"Pending Income : ₹{income_summary['pending_income']:,.2f}")

    print("\n💳 Commitments Summary")
    print(f"total_borrowed : ₹{commitment_summary['total_borrowed']:,.2f}")
    print(f"total_repaid : ₹{commitment_summary['total_repaid']:,.2f}")
    print(f"outstanding_debt : ₹{commitment_summary['outstanding_debt']:,.2f}")
    print(f"monthly_commitments : ₹{commitment_summary['monthly_commitments']:,.2f}")
    print(f"active_commitments : {commitment_summary['active_commitments']}")

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

    print("\n📊 Expense Distribution")
    if summary["total_expense"] == 0:
        print("No spending made this month.")
    else:
        print(f"Need Amount : ₹{expense_distribution['need_amount']:,.2f}")
        print(f"Want Amount : ₹{expense_distribution['want_amount']:,.2f}")
        print(f"Need Spending : {expense_distribution['need_percentage']:.2f}%")
        print(f"Want Spending : {expense_distribution['want_percentage']:.2f}%")

    print("\n📅 Monthly Summary")
    print(f"Total Expense : ₹{monthly_summary['total_expense']:,.2f}")
    print(f"Need Spending : ₹{monthly_summary['total_need']:,.2f}")
    print(f"Want Spending : ₹{monthly_summary['total_want']:,.2f}")

    print("\n📊 Monthly Expense Distribution")
    if monthly_summary["total_expense"] == 0:
        print("No spending made this month.")
    else:
        print(f"Need Amount : ₹{monthly_distribution['need_amount']:,.2f}")
        print(f"Want Amount : ₹{monthly_distribution['want_amount']:,.2f}")
        print(f"Need Spending : {monthly_distribution['need_percentage']:.2f}%")
        print(f"Want Spending : {monthly_distribution['want_percentage']:.2f}%")

    print("\n📊 Financial insights")
    for category, insight in financial_insights.items():
        print(f"\n{category}:")
        print(f"  Status: {insight['status']}")
        print(f"  Priority: {insight['priority']}")
        print(f"  Reason: {insight['reason']}")

    budget = load_budget()

    print("\n📊 Budget Analysis")

    print(f"Budgeted Amount : ₹{budget_analysis['monthly_budget']:,.2f}")
    print(f"Actual Spending : ₹{budget_analysis['spent']:,.2f}")
    print(f"Budget Remaining : ₹{budget_analysis['budget_remaining']:,.2f}")
    print(
        f"Budget Utilization : {budget_analysis['budget_utilization_percentage']:.2f}%"
    )
    print(f"Status : {budget_analysis['status']}")

    for category, insight in budget_insight.items():
        print(f"\n{category}:\n")
        print(f"  Status: {insight['status']}")
        print(f"  Priority: {insight['priority']}")
        print(f"  Reason: {insight['reason']}")
        print(f"  Recommendation: {insight['recommendation']}\n")

    print("\n💰 Savings Summary")
    print(f"gross_savings : ₹{savings_summary['gross_savings']:,.2f}")
    print(f"net_savings : ₹{savings_summary['net_savings']:,.2f}")
    print(f"savings_rate : {savings_summary['savings_rate']:.2f}%")
    print(f"commitment_ratio : {savings_summary['commitment_ratio']:.2f}%")
    print(f"expense_ratio : {savings_summary['expense_ratio']:.2f}%")

    print("\n🚨 Emergency Fund Summary")
    print(f"Current Emergency Fund : ₹{emergency_fund['current_emergency_fund']:,.2f}")
    print(f"Monthly Survival Cost : ₹{emergency_fund['monthly_survival_cost']:,.2f}")
    print(f"Required 3-Months Fund : ₹{emergency_fund['required_3_months_fund']:,.2f}")
    print(f"Required 6-Months Fund : ₹{emergency_fund['required_6_months_fund']:,.2f}")
    print(
        f"Required 12-Months Fund : ₹{emergency_fund['required_12_months_fund']:,.2f}"
    )
    print(f"Coverage Months : {emergency_fund['coverage_months']:.2f}")
    print(f"Emergency Fund Gap : ₹{emergency_fund['emergency_fund_gap']:,.2f}")
    
    print("\n📊 Goal Portfolio Summary")

    for key, value in goal_summary.items():
        print(f"{key} : {value}")

    print(goal_snapshot)


if __name__ == "__main__":
    main()

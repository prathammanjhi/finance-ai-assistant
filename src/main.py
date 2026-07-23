from reader import (
    load_transactions,
    load_income,
    load_commitments,
    load_budget,
    load_goals,
    load_investments,
    load_assets,
    load_liabilities,
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
    generate_goal_insights,
    calculate_investments,
    generate_investment_insights,
    generate_investment_snapshot,
    calculate_assets,
    generate_asset_snapshot,
    generate_asset_insights,
    calculate_liabilities,
    generate_liability_insights,
    generate_liability_snapshot,
    calculate_net_worth,
    generate_net_worth_insights,
    generate_net_worth_snapshot,
)


def main():
    print("=" * 40)
    print("📊 Finance AI Assistant")
    print("=" * 40)

    transactions = load_transactions()
    income = load_income()
    commitments = load_commitments()
    investments = load_investments()
    investment_summary = calculate_investments(investments)
    temp_snapshot = {
        "investment_summary": investment_summary,
        "investment_insights": {},
    }

    investment_insights = generate_investment_insights(temp_snapshot)

    investment_snapshot = generate_investment_snapshot(
        investment_summary,
        investment_insights,
    )
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

    temp_goal_snapshot = {
        "goal_analysis": goal_analysis,
        "goal_summary": goal_summary,
    }

    goal_insights = generate_goal_insights(temp_goal_snapshot)

    goal_snapshot = generate_goal_snapshot(
        goal_analysis,
        goal_summary,
        goal_insights,
    )

    assets = load_assets()

    asset_summary = calculate_assets(assets)

    temp_asset_snapshot = {
        "asset_summary": asset_summary,
        "asset_insights": {},
    }

    asset_insights = generate_asset_insights(temp_asset_snapshot)

    asset_snapshot = generate_asset_snapshot(
        asset_summary,
        asset_insights,
    )

    liabilities = load_liabilities()

    liability_summary = calculate_liabilities(
        liabilities,
        asset_snapshot,
    )

    temp_liability_snapshot = {
        "liability_summary": liability_summary,
        "liability_insights": {},
    }

    liability_insights = generate_liability_insights(
        temp_liability_snapshot,
    )

    liability_snapshot = generate_liability_snapshot(
        liability_summary,
        liability_insights,
    )

    net_worth_summary = calculate_net_worth(
        asset_snapshot,
        liability_snapshot,
    )

    net_worth_insights = generate_net_worth_insights(
        net_worth_summary,
    )

    net_worth_snapshot = generate_net_worth_snapshot(
        net_worth_summary,
        net_worth_insights,
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

    print("\n🎯 Goal Insights")

    for insight in goal_insights:
        print(f"\nGoal : {insight['goal']}")
        print(f"Status : {insight['status']}")
        print(f"Priority : {insight['priority']}")
        print(f"Reason : {insight['reason']}")
        print(f"Recommendation : {insight['recommendation']}")

    print("\n📈 Investment Summary")

    for key, value in investment_summary.items():
        if isinstance(value, (int, float)):
            print(f"{key} : ₹{value:,.2f}")

        else:
            print(f"{key} : {value}")

    print("\n📈 Investment Insights")

    for key, value in investment_insights.items():
        if isinstance(value, (int, float)):
            print(f"{key} : ₹{value:,.2f}")

        else:
            print(f"{key} : {value}")

    print("\n📦 Asset Summary")

    print(f"Total Asset Value : ₹{asset_summary['total_asset_value']:,.2f}")
    print(f"Purchase Value : ₹{asset_summary['purchase_value']:,.2f}")
    print(f"Asset Profit/Loss : ₹{asset_summary['asset_profit_loss']:,.2f}")
    print(f"Asset Return : {asset_summary['asset_return_percentage']:.2f}%")
    print(f"Active Assets : {asset_summary['active_assets']}")

    largest = asset_summary["largest_asset"]

    if largest is not None:
        print(f"Largest Asset : {largest['asset']}")
        print(f"Category : {largest['category']}")
        print(f"Current Value : ₹{largest['current_value']:,.2f}")

    print("\n📄 Liability Summary")
    print(f"Total Original Loan : ₹{liability_summary['total_original_loan']:,.2f}")
    print(
        f"Outstanding Balance : ₹{liability_summary['total_outstanding_balance']:,.2f}"
    )
    print(f"Total Repaid : ₹{liability_summary['total_repaid']:,.2f}")
    print(f"Loan Paid : {liability_summary['repayment_percentage']:.2f}%")
    print(
        f"Monthly Liability Payment : ₹{liability_summary['monthly_liability_payment']:,.2f}"
    )
    print(f"Largest Monthly EMI : ₹{liability_summary['largest_monthly_emi']:,.2f}")
    print(f"Active Liabilities : {liability_summary['active_liabilities']}")
    print(
        f"Liability Ratio (Debt / Assets) : {liability_summary['liability_ratio']:.2f}%"
    )
    print(f"Average Liability : ₹{liability_summary['average_liability']:,.2f}")
    print(
        f"Loan Outstanding : {liability_summary['remaining_repayment_percentage']:.2f}%"
    )

    highest = liability_summary["highest_liability"]

    if highest is not None:
        print("\n💳 Highest Liability")
        print(f"Liability : {highest['liability']}")
        print(f"Category : {highest['category']}")
        print(f"Original Loan : ₹{highest['original_loan']:,.2f}")
        print(f"Outstanding Balance : ₹{highest['outstanding_balance']:,.2f}")
        print(f"Monthly EMI : ₹{highest['monthly_emi']:,.2f}")


    print("\n💰 Net Worth Summary")
    print(f"Total Assets : ₹{net_worth_summary['total_assets']:,.2f}")
    print(f"Total Liabilities : ₹{net_worth_summary['total_liabilities']:,.2f}")
    print(f"Net Worth : ₹{net_worth_summary['net_worth']:,.2f}")
    print(f"Equity : ₹{net_worth_summary['equity']:,.2f}")
    print(f"Debt Percentage : {net_worth_summary['debt_percentage']:.2f}%")
    print(f"Asset Coverage Ratio : {net_worth_summary['asset_coverage_ratio']:.2f}")
    print(f"Wealth Category : {net_worth_summary['wealth_category']}")
    print(f"Wealth Score : {net_worth_summary['wealth_score']:.2f}")
    print(f"Asset/Liability Ratio : {net_worth_summary['asset_to_liability_ratio']:.2f}")
    print(f"Financial Leverage : {net_worth_summary['financial_leverage']:.2f}")
    print(f"Net Assets : ₹{net_worth_summary['net_assets']:,.2f}")
    print(f"Debt Free : {net_worth_summary['debt_free_percentage']:.2f}%")
    print(f"Wealth Efficiency : {net_worth_summary['wealth_efficiency']:.2f}%")
    print(f"Wealth Growth : {net_worth_summary['wealth_growth']:.2f}%")


    print("\n💡 Net Worth Insights")
    print(f"Status : {net_worth_insights['status']}")
    print(f"Priority : {net_worth_insights['priority']}")
    print(f"Reason : {net_worth_insights['reason']}")
    print(f"Recommendation : {net_worth_insights['recommendation']}")


if __name__ == "__main__":
    main()

def calculate_financial_health(
    financial_snapshot,
    budget_analysis,
    savings_summary,
    emergency_summary,
    goal_snapshot,
    investment_snapshot,
    asset_snapshot,
    liability_snapshot,
    net_worth_snapshot,
    wealth_health_snapshot,
):
    financial_position = financial_snapshot["financial_position"]
    goal_summary = goal_snapshot["goal_summary"]
    investment_summary = investment_snapshot["investment_summary"]
    asset_summary = asset_snapshot["asset_summary"]
    liability_summary = liability_snapshot["liability_summary"]
    net_worth_summary = net_worth_snapshot["net_worth_summary"]
    wealth_health_summary = wealth_health_snapshot["wealth_health_summary"]

    # Financial Snapshot
    cash_flow = financial_position["cash_position"]
    net_position = financial_position["net_position"]
    # Budget
    budget_utilization = budget_analysis["budget_utilization_percentage"]
    # Savings
    savings_rate = savings_summary["savings_rate"]
    # Emergency
    coverage_months = emergency_summary["coverage_months"]
    # Goals
    goal_progress = goal_summary["overall_progress_percentage"]
    # Investments
    investment_return = investment_summary["return_percentage"]
    active_investments = investment_summary["active_investments"]
    # Assets
    asset_return = asset_summary["asset_return_percentage"]
    # Liabilities
    liability_ratio = liability_summary["liability_ratio"]
    # Net Worth
    net_worth = net_worth_summary["net_worth"]
    # Wealth Health
    wealth_score = wealth_health_summary["wealth_score"]

    # Financial Snapshot Score (15)
    if cash_flow > 0 and net_position > 0:
        financial_score = 15

    elif cash_flow > 0:
        financial_score = 10

    elif net_position > 0:
        financial_score = 6

    else:
        financial_score = 0

    # Budget Score (10)
    if budget_utilization <= 50:
        budget_score = 10

    elif budget_utilization <= 75:
        budget_score = 8

    elif budget_utilization <= 100:
        budget_score = 5

    else:
        budget_score = 0

    # Savings Score (15)
    if savings_rate >= 50:
        savings_score = 15

    elif savings_rate >= 30:
        savings_score = 10

    elif savings_rate >= 15:
        savings_score = 5

    else:
        savings_score = 0

    # Emergency Score (10)
    if coverage_months >= 6:
        emergency_score = 10

    elif coverage_months >= 3:
        emergency_score = 7

    elif coverage_months >= 1:
        emergency_score = 4

    else:
        emergency_score = 0

    # Goal Score (10)
    if goal_progress >= 75:
        goal_score = 10

    elif goal_progress >= 50:
        goal_score = 7

    elif goal_progress >= 25:
        goal_score = 4

    else:
        goal_score = 0

    # Investment Score (10)
    if active_investments == 0:
        investment_score = 4

    elif investment_return < 0:
        investment_score = 2

    elif investment_return < 8:
        investment_score = 6

    else:
        investment_score = 10

    # Asset Score (5)
    if asset_return < 0:
        asset_score = 2

    elif asset_return < 10:
        asset_score = 3

    elif asset_return < 25:
        asset_score = 4

    else:
        asset_score = 5

    # Liability Score (10)
    if liability_ratio < 30:
        liability_score = 10

    elif liability_ratio < 60:
        liability_score = 7

    elif liability_ratio < 80:
        liability_score = 4

    else:
        liability_score = 0

    # Net Worth Score (5)
    if net_worth >= 2000000:
        net_worth_score = 5

    elif net_worth >= 1000000:
        net_worth_score = 4

    elif net_worth >= 500000:
        net_worth_score = 3

    elif net_worth >= 100000:
        net_worth_score = 2

    else:
        net_worth_score = 0

    # Wealth Health Score (10)
    wealth_health_score = round((wealth_score / 100) * 10)

    # Final Score
    financial_health_score = (
        financial_score
        + budget_score
        + savings_score
        + emergency_score
        + goal_score
        + investment_score
        + asset_score
        + liability_score
        + net_worth_score
        + wealth_health_score
    )

    # Grade
    if financial_health_score >= 95:
        financial_grade = "A+"

    elif financial_health_score >= 90:
        financial_grade = "A"

    elif financial_health_score >= 80:
        financial_grade = "B+"

    elif financial_health_score >= 70:
        financial_grade = "B"

    elif financial_health_score >= 60:
        financial_grade = "C"

    elif financial_health_score >= 40:
        financial_grade = "D"

    else:
        financial_grade = "F"

    # Risk
    if financial_health_score >= 90:
        financial_risk = "Very Low"

    elif financial_health_score >= 75:
        financial_risk = "Low"

    elif financial_health_score >= 60:
        financial_risk = "Medium"

    elif financial_health_score >= 40:
        financial_risk = "High"

    else:
        financial_risk = "Critical"

    # Financial Health
    if financial_health_score >= 85:
        financial_strength = "Excellent"

    elif financial_health_score >= 70:
        financial_strength = "Strong"

    elif financial_health_score >= 50:
        financial_strength = "Average"

    else:
        financial_strength = "Weak"

    financial_health_summary = {
        "financial_health_score": financial_health_score,
        "financial_grade": financial_grade,
        "financial_risk": financial_risk,
        "financial_strength": financial_strength,
        "financial_score": financial_score,
        "budget_score": budget_score,
        "savings_score": savings_score,
        "emergency_score": emergency_score,
        "goal_score": goal_score,
        "investment_score": investment_score,
        "asset_score": asset_score,
        "liability_score": liability_score,
        "net_worth_score": net_worth_score,
        "wealth_health_score": wealth_health_score,
    }

    return financial_health_summary

def generate_financial_health_insights(financial_health_summary):
    score = financial_health_summary["financial_health_score"]

    if score >= 90:
        status = "Excellent"

        priority = "Low"

        reason = (
            "Your overall financial position is excellent. "
            "You have built a strong financial foundation with healthy cash flow, "
            "good financial discipline, and sustainable wealth-building habits."
        )

        recommendation = (
            "• Continue investing consistently.\n"
            "• Maintain a 6-month emergency fund.\n"
            "• Increase investments as your income grows.\n"
            "• Focus on long-term wealth creation and financial independence."
        )

    elif score >= 75:
        status = "Healthy"

        priority = "Low"

        reason = (
            "Your finances are in a healthy position with strong fundamentals. "
            "Although your financial habits are good, there is still room to "
            "strengthen long-term wealth and improve overall financial resilience."
        )

        recommendation = (
            "• Increase your investment contributions.\n"
            "• Continue building your emergency fund.\n"
            "• Reduce remaining liabilities whenever possible.\n"
            "• Stay consistent with your financial goals."
        )

    elif score >= 60:
        status = "Developing"

        priority = "Medium"

        reason = (
            "Your financial foundation is developing, but several areas require "
            "attention before achieving long-term financial stability."
        )

        recommendation = (
            "• Increase your monthly savings rate.\n"
            "• Build a 3–6 month emergency fund.\n"
            "• Begin or expand long-term investments.\n"
            "• Continue reducing outstanding liabilities."
        )

    elif score >= 40:
        status = "Needs Improvement"

        priority = "High"

        reason = (
            "Your current financial position needs improvement. "
            "Limited savings, weak financial reserves, or higher liabilities "
            "may reduce your ability to handle unexpected financial situations."
        )

        recommendation = (
            "• Improve your monthly savings discipline.\n"
            "• Reduce unnecessary discretionary spending.\n"
            "• Build your emergency fund before taking additional financial risks.\n"
            "• Create a consistent monthly investment plan after improving cash flow."
        )

    else:
        status = "Critical"

        priority = "Critical"

        reason = (
            "Your financial health is currently weak due to low financial reserves, "
            "limited emergency savings, high financial risk, or insufficient long-term wealth."
        )

        recommendation = (
            "• Build a 3–6 month emergency fund.\n"
            "• Reduce outstanding liabilities as quickly as possible.\n"
            "• Avoid unnecessary purchases until your financial health improves.\n"
            "• Start investing after establishing financial stability."
        )

    financial_health_insights = {
        "status": status,
        "priority": priority,
        "reason": reason,
        "recommendation": recommendation,
        "focus_area": "Emergency Fund",
    }

    return financial_health_insights

def generate_financial_health_snapshot(
    financial_health_summary,
    financial_health_insights,
):
    financial_health_snapshot = {
        "financial_health_summary": financial_health_summary,
        "financial_health_insights": financial_health_insights,
    }

    return financial_health_snapshot
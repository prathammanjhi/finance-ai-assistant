def calculate_wealth_health(
    emergency_summary,
    goal_snapshot,
    investment_snapshot,
    asset_snapshot,
    liability_snapshot,
    net_worth_snapshot,
):
    goal_summary = goal_snapshot["goal_summary"]
    investment_summary = investment_snapshot["investment_summary"]
    asset_summary = asset_snapshot["asset_summary"]
    liability_summary = liability_snapshot["liability_summary"]
    net_worth_summary = net_worth_snapshot["net_worth_summary"]
    emergency_months = emergency_summary["coverage_months"]

    goal_progress = goal_summary["overall_progress_percentage"]
    investment_return = investment_summary["return_percentage"]
    asset_return = asset_summary["asset_return_percentage"]
    debt_percentage = liability_summary["liability_ratio"]
    net_worth = net_worth_summary["net_worth"]
    active_investments = investment_summary["active_investments"]

    MAX_EMERGENCY_SCORE = 20
    MAX_GOAL_SCORE = 15
    MAX_INVESTMENT_SCORE = 10
    MAX_ASSET_SCORE = 15
    MAX_LIABILITY_SCORE = 20
    MAX_NET_WORTH_SCORE = 20

    # Emergency Fund Score (20)

    if emergency_months < 1:
        emergency_score = 0

    elif emergency_months < 3:
        emergency_score = 8

    elif emergency_months < 6:
        emergency_score = 15

    else:
        emergency_score = 20

    # Goal Score (15)

    if goal_progress < 25:
        goal_score = 4

    elif goal_progress < 50:
        goal_score = 8

    elif goal_progress < 75:
        goal_score = 12

    else:
        goal_score = 15

    # Investment Score (10)

    if active_investments == 0:
        investment_score = 4  # No investments yet

    elif investment_return < 0:
        investment_score = 2

    elif investment_return < 8:
        investment_score = 6

    else:
        investment_score = 10

    # Asset Score (15)

    if asset_return < 0:
        asset_score = 5

    elif asset_return < 10:
        asset_score = 8

    elif asset_return < 25:
        asset_score = 12

    else:
        asset_score = 15

    # Outstanding Liabilities / Total Assets × 100

    # Liability Score (20)

    if debt_percentage > 80:
        liability_score = 0

    elif debt_percentage > 60:
        liability_score = 8

    elif debt_percentage > 30:
        liability_score = 15

    else:
        liability_score = 20

    # Net Worth Score (20)

    if net_worth < 100000:
        net_worth_score = 0

    elif net_worth < 250000:
        net_worth_score = 5

    elif net_worth < 500000:
        net_worth_score = 8

    elif net_worth < 750000:
        net_worth_score = 10

    elif net_worth < 1000000:
        net_worth_score = 12

    elif net_worth < 1250000:
        net_worth_score = 14

    elif net_worth < 1500000:
        net_worth_score = 16

    elif net_worth < 2000000:
        net_worth_score = 18

    else:
        net_worth_score = 20

    wealth_score = (
        emergency_score
        + goal_score
        + investment_score
        + asset_score
        + liability_score
        + net_worth_score
    )

    # Wealth Grade #

    if wealth_score >= 95:
        wealth_grade = "A+"

    elif wealth_score >= 90:
        wealth_grade = "A"

    elif wealth_score >= 80:
        wealth_grade = "B+"

    elif wealth_score >= 70:
        wealth_grade = "B"

    elif wealth_score >= 60:
        wealth_grade = "C"

    elif wealth_score >= 40:
        wealth_grade = "D"

    else:
        wealth_grade = "F"

    # Wealth Risk #

    if wealth_score >= 90:
        wealth_risk = "Very Low"

    elif wealth_score >= 75:
        wealth_risk = "Low"

    elif wealth_score >= 60:
        wealth_risk = "Medium"

    elif wealth_score >= 40:
        wealth_risk = "High"

    else:
        wealth_risk = "Critical"

    # Capital Strength #

    capital_score = net_worth_score + asset_score + emergency_score
    if capital_score >= 50:
        capital_strength = "Excellent"

    elif capital_score >= 40:
        capital_strength = "Strong"

    elif capital_score >= 25:
        capital_strength = "Average"

    else:
        capital_strength = "Weak"

    # for future use #

    growth_readiness = "Excellent" if goal_score >= 12 else "Moderate"

    liquidity_strength = "Strong" if emergency_score >= 15 else "Weak"

    wealth_momentum = "Positive" if goal_score >= 8 else "Slow"

    financial_stability = "Stable" if liability_score >= 15 else "Needs Improvement"

    long_term_sustainability = "Excellent" if wealth_score >= 80 else "Developing"

    wealth_health_summary = {
        "wealth_score": wealth_score,
        "wealth_grade": wealth_grade,
        "wealth_risk": wealth_risk,
        "capital_strength": capital_strength,
        "emergency_score": emergency_score,
        "goal_score": goal_score,
        "investment_score": investment_score,
        "asset_score": asset_score,
        "liability_score": liability_score,
        "net_worth_score": net_worth_score,
        "growth_readiness": growth_readiness,
        "liquidity_strength": liquidity_strength,
        "wealth_momentum": wealth_momentum,
        "financial_stability": financial_stability,
        "long_term_sustainability": long_term_sustainability,
    }

    return wealth_health_summary

def generate_wealth_health_insights(wealth_health_summary):

    wealth_score = wealth_health_summary["wealth_score"]

    if wealth_score >= 90:
        status = "Excellent"

        priority = "Low"

        reason = "Your financial foundation is excellent with strong wealth growth, healthy liquidity, and disciplined financial management."

        recommendation = "Maintain your current financial discipline while continuing to invest for long-term wealth creation."

    elif wealth_score >= 75:
        status = "Healthy"
        priority = "Low"
        reason = "Your financial position is healthy and continues to move in the right direction."

        recommendation = "Continue improving your investments and savings while maintaining your current financial habits."

    elif wealth_score >= 60:
        status = "Developing"
        priority = "Medium"
        reason = "Your financial foundation is developing well, although a few key areas still need improvement."

        recommendation = "Increase your savings rate, strengthen your emergency fund, and continue investing consistently."

    elif wealth_score >= 40:
        status = "Needs Improvement"
        priority = "High"
        reason = "Your financial foundation needs improvement. While some areas are healthy, liabilities or limited reserves are reducing your overall financial strength."

        recommendation = "Reduce unnecessary discretionary spending, improve monthly savings, and continue building your emergency fund before taking additional financial risks."

    else:
        status = "Critical"
        priority = "Critical"
        reason = "Your overall financial position is weak because liabilities outweigh assets and your financial safety margin remains limited."

        recommendation = "Prioritize building an emergency fund, reduce outstanding liabilities, and avoid major discretionary purchases until your financial position improves."

    wealth_health_insights = {
        "status": status,
        "priority": priority,
        "reason": reason,
        "recommendation": recommendation,
    }

    return wealth_health_insights

def generate_wealth_health_snapshot(
    wealth_health_summary,
    wealth_health_insights,
):

    wealth_health_snapshot = {
        "wealth_health_summary": wealth_health_summary,
        "wealth_health_insights": wealth_health_insights,
    }

    return wealth_health_snapshot
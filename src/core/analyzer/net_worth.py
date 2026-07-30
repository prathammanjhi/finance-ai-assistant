def calculate_net_worth(
    asset_snapshot,
    liability_snapshot,
):
    asset_summary = asset_snapshot["asset_summary"]
    liability_summary = liability_snapshot["liability_summary"]
    total_assets = asset_summary["total_asset_value"]
    total_liabilities = liability_summary["total_outstanding_balance"]

    net_worth = total_assets - total_liabilities
    equity = net_worth
    debt_percentage = (
        (total_liabilities / total_assets) * 100 if total_assets > 0 else 0
    )
    asset_coverage_ratio = (
        total_assets / total_liabilities if total_liabilities > 0 else 0
    )
    if net_worth < 0:
        wealth_category = "Negative"

    elif net_worth < 500000:
        wealth_category = "Building"

    elif net_worth < 2500000:
        wealth_category = "Growing"

    else:
        wealth_category = "Strong"

    wealth_score = max(0, min(100, 100 - debt_percentage))
    asset_to_liability_ratio = (
        total_assets / total_liabilities if total_liabilities > 0 else float("inf")
    )
    financial_leverage = total_liabilities / total_assets if total_assets > 0 else 0
    wealth_growth = 0
    net_assets = total_assets - total_liabilities
    debt_free_percentage = (net_assets / total_assets) * 100 if total_assets > 0 else 0
    wealth_score = (debt_free_percentage * 0.5) + (asset_coverage_ratio * 25)

    wealth_score = max(0, min(100, wealth_score))

    wealth_efficiency = (net_assets / total_assets) * 100 if total_assets > 0 else 0

    net_worth_summary = {
        "total_assets": total_assets,
        "total_liabilities": total_liabilities,
        "net_worth": net_worth,
        "equity": equity,
        "asset_coverage_ratio": asset_coverage_ratio,
        "debt_percentage": debt_percentage,
        "wealth_category": wealth_category,
        "wealth_score": wealth_score,
        # Future Proofing
        "asset_to_liability_ratio": asset_to_liability_ratio,
        "financial_leverage": financial_leverage,
        "wealth_growth": wealth_growth,
        "net_assets": net_assets,
        "debt_free_percentage": debt_free_percentage,
        "wealth_score": wealth_score,
        "wealth_efficiency": wealth_efficiency,
    }

    return net_worth_summary

def generate_net_worth_insights(net_worth_summary):

    net_worth = net_worth_summary["net_worth"]
    debt_percentage = net_worth_summary["debt_percentage"]
    net_assets = net_worth_summary["net_assets"]
    total_assets = net_worth_summary["total_assets"]

    if net_worth < 0:
        insight_status = "Negative Net Worth"

        insight_priority = "High"

        reason = "Your liabilities exceed your total assets."

        recommendation = "Reduce liabilities and build appreciating assets."

    elif debt_percentage >= 70:
        insight_status = "Highly Leveraged"

        insight_priority = "High"

        reason = "Debt represents a large portion of your assets."

        recommendation = "Prioritize loan repayment before taking additional debt."

    elif debt_percentage >= 30:
        insight_status = "Balanced"

        insight_priority = "Medium"

        reason = "Your debt is currently manageable."

        recommendation = "Continue increasing assets while reducing liabilities."

    else:
        insight_status = "Strong Net Worth"

        insight_priority = "Low"

        reason = "You have a healthy balance between assets and liabilities."

        recommendation = "Continue growing appreciating assets."

    net_worth_insights = {
        "status": insight_status,
        "priority": insight_priority,
        "reason": reason,
        "recommendation": recommendation,
    }

    return net_worth_insights

def generate_net_worth_snapshot(
    net_worth_summary,
    net_worth_insights,
):

    net_worth_snapshot = {
        "net_worth_summary": net_worth_summary,
        "net_worth_insights": net_worth_insights,
    }

    return net_worth_snapshot
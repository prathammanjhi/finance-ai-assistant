def calculate_investments(investments):
    total_invested = investments["Invested Amount"].sum()

    current_value = investments["Current Value"].sum()

    active_investments = (investments["Status"] == "Active").sum()

    total_profit_loss = current_value - total_invested

    return_percentage = (
        (total_profit_loss / total_invested) * 100 if total_invested > 0 else 0
    )

    if total_invested == 0:
        investment_growth = "No Investments"

    elif total_profit_loss > 0:
        investment_growth = "Profit"

    elif total_profit_loss < 0:
        investment_growth = "Loss"

    else:
        investment_growth = "Break Even"

    return {
        "total_invested": total_invested,
        "current_value": current_value,
        "total_profit_loss": total_profit_loss,
        "return_percentage": return_percentage,
        "active_investments": active_investments,
        "investment_growth": investment_growth,
    }

def generate_investment_insights(investment_summary):


    return_percentage = investment_summary["return_percentage"]
    active_investments = investment_summary["active_investments"]

    if active_investments == 0:
        insight_status = "No Investments"
        insight_priority = "Medium"
        reason = "No Active Investments found."
        recommendation = "Start Investing to build Long-term wealth."
    elif return_percentage < 0:
        insight_status = "Loss"
        insight_priority = "High"
        reason = "Investment portfolio is currently in loss."
        recommendation = "Review investments before making new allocations."
    elif 0 <= return_percentage < 8:
        insight_status = "Growing Slowly"
        insight_priority = "Medium"
        reason = "Portfolio is generating modest returns."
        recommendation = "Review diversification and long-term strategy."
    elif return_percentage >= 8:
        insight_status = "Healthy Growth"
        insight_priority = "Low"
        reason = "Portfolio is performing well."
        recommendation = "Continue disciplined investing."
    elif return_percentage > 15:
        insight_status = "Excellent Growth"
        insight_priority = "Low"
        reason = "Portfolio is performing Great."
        recommendation = "Continue disciplined investing."

    return {
        "status": insight_status,
        "priority": insight_priority,
        "reason": reason,
        "recommendation": recommendation,
    }

def generate_investment_snapshot(
    investment_summary,
    investment_insights,
):
    investment_snapshot = {
        "investment_summary": investment_summary,
        "investment_insights": investment_insights,
    }

    return investment_snapshot
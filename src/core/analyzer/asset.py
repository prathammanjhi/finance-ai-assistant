def calculate_assets(assets):

    total_asset_value = assets["Current Value"].sum()

    purchase_value = assets["Purchase Value"].sum()

    asset_profit_loss = total_asset_value - purchase_value

    active_assets = (assets["Status"] == "Active").sum()

    emergency_fund = assets.loc[
        assets["Asset"] == "Emergency Fund", "Current Value"
    ].sum()

    largest_asset_row = (
        assets.loc[assets["Current Value"].idxmax()] if not assets.empty else None
    )

    if largest_asset_row is not None:
        largest_asset = {
            "asset": largest_asset_row["Asset"],
            "category": largest_asset_row["Category"],
            "purchase_value": largest_asset_row["Purchase Value"],
            "current_value": largest_asset_row["Current Value"],
        }
    else:
        largest_asset = None


    asset_return_percentage = round(
        (asset_profit_loss / purchase_value) * 100 if purchase_value > 0 else 0
    )

    asset_summary = {
        "total_asset_value": total_asset_value,
        "purchase_value": purchase_value,
        "asset_profit_loss": asset_profit_loss,
        "active_assets": active_assets,
        "largest_asset": largest_asset,
        "asset_return_percentage": asset_return_percentage,
        "emergency_fund": emergency_fund,
    }

    return asset_summary

def calculate_emergency_fund(expense_summary, commitment_summary, asset_summary):

    current_emergency_fund = max(0, asset_summary["emergency_fund"])
    # current_emergency_fund = 100000
    total_monthly_expenses = expense_summary["total_expense"]
    # total_monthly_expenses = 0
    total_monthly_commitments = commitment_summary["monthly_commitments"]
    # total_monthly_commitments = 0

    monthly_survival_cost = total_monthly_expenses + total_monthly_commitments
    required_3_months_fund = monthly_survival_cost * 3
    required_6_months_fund = monthly_survival_cost * 6
    required_12_months_fund = monthly_survival_cost * 12
    coverage_months = (
        round(
            current_emergency_fund /
            monthly_survival_cost,
            2,
        )
        if monthly_survival_cost > 0
        else None
    )
    gap = required_6_months_fund - current_emergency_fund
    emergency_fund_gap = max(0, gap)

    emergency_summary = {
        "current_emergency_fund": current_emergency_fund,
        "total_monthly_expenses": total_monthly_expenses,
        "total_monthly_commitments": total_monthly_commitments,
        "monthly_survival_cost": monthly_survival_cost,
        "required_3_months_fund": required_3_months_fund,
        "required_6_months_fund": required_6_months_fund,
        "required_12_months_fund": required_12_months_fund,
        "coverage_months": coverage_months,
        "emergency_fund_gap": emergency_fund_gap,
    }

    return emergency_summary


def generate_asset_insights(asset_summary):

    active_assets = asset_summary["active_assets"]
    asset_profit_loss = asset_summary["asset_profit_loss"]
    largest_asset = asset_summary["largest_asset"]

    # -------------------------------------------------
    # Asset Health
    # -------------------------------------------------

    asset_health = (
        "below the purchase value due to normal depreciation."
        if asset_profit_loss < 0
        else "maintaining or increasing its overall value."
    )

    # -------------------------------------------------
    # No Assets
    # -------------------------------------------------

    if active_assets == 0:
        insight_status = "No Assets"
        insight_priority = "High"

        reason = "No active assets found."

        recommendation = (
            "Start building personal assets to improve your financial strength."
        )

    # -------------------------------------------------
    # Limited Asset Base
    # -------------------------------------------------

    elif active_assets <= 3:
        insight_status = "Limited Assets"
        insight_priority = "Medium"

        reason = f"Your asset base is still limited and is currently {asset_health}"

        if largest_asset is not None:
            recommendation = (
                f"Continue acquiring productive assets. "
                f"Current largest asset: {largest_asset['asset']} "
                f"(₹{largest_asset['current_value']:,.2f})."
            )

        else:
            recommendation = "Continue acquiring productive assets."

    # -------------------------------------------------
    # Healthy Asset Base
    # -------------------------------------------------

    else:
        insight_status = "Healthy Asset Base"
        insight_priority = "Low"

        reason = (
            f"You have a diversified asset portfolio that is currently {asset_health}"
        )

        if largest_asset is not None:
            recommendation = (
                f"Maintain and grow your assets. "
                f"Your largest asset is {largest_asset['asset']} "
                f"(₹{largest_asset['current_value']:,.2f}). "
                f"Gradually increase appreciating assets such as investments, "
                f"gold, property, or business assets."
            )

        else:
            recommendation = "Maintain your existing assets and gradually increase appreciating assets."

    return {
        "status": insight_status,
        "priority": insight_priority,
        "reason": reason,
        "recommendation": recommendation,
    }


def generate_asset_snapshot(
    asset_summary,
    asset_insights,
):
    asset_snapshot = {
        "asset_summary": asset_summary,
        "asset_insights": asset_insights,
    }

    return asset_snapshot

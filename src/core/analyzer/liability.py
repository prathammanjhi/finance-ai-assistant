def calculate_liabilities(liabilities, asset_snapshot):

    asset_summary = asset_snapshot["asset_summary"]
    total_asset_value = asset_summary["total_asset_value"]
    total_original_loan = liabilities["Original Loan"].sum()

    total_outstanding_balance = liabilities["Outstanding Balance"].sum()

    monthly_liability_payment = liabilities.loc[
        liabilities["Status"] == "Active",
        "Monthly EMI",
    ].sum()
    active_liabilities = len(liabilities.loc[liabilities["Status"] == "Active"])

    highest_liability_row = (
        liabilities.loc[liabilities["Outstanding Balance"].idxmax()]
        if not liabilities.empty
        else None
    )

    highest_liability = (
        {
            "liability": highest_liability_row["Liability"],
            "category": highest_liability_row["Category"],
            "original_loan": highest_liability_row["Original Loan"],
            "outstanding_balance": highest_liability_row["Outstanding Balance"],
            "monthly_emi": highest_liability_row["Monthly EMI"],
        }
        if highest_liability_row is not None
        else None
    )

    liability_ratio = round(
        (total_outstanding_balance / total_asset_value) * 100
        if total_asset_value > 0
        else 0
    )

    average_liability = round(
        total_outstanding_balance / active_liabilities if active_liabilities > 0 else 0
    )

    total_repaid = total_original_loan - total_outstanding_balance

    repayment_percentage = round(
        (total_repaid / total_original_loan) * 100 if total_original_loan > 0 else 0
    )

    largest_monthly_emi = (
        liabilities["Monthly EMI"].max() if not liabilities.empty else 0
    )

    remaining_repayment_percentage = max(
        0,
        round(
            100 - repayment_percentage,
            2,
        ),
    )

    liability_summary = {
        "total_original_loan": total_original_loan,
        "total_outstanding_balance": total_outstanding_balance,
        "total_repaid": total_repaid,
        "repayment_percentage": repayment_percentage,
        "monthly_liability_payment": monthly_liability_payment,
        "largest_monthly_emi": largest_monthly_emi,
        "active_liabilities": active_liabilities,
        "highest_liability": highest_liability,
        "liability_ratio": liability_ratio,
        "average_liability": average_liability,
        "remaining_repayment_percentage": remaining_repayment_percentage,
    }

    return liability_summary

def generate_liability_insights(liability_summary):


    active_liabilities = liability_summary["active_liabilities"]
    liability_ratio = liability_summary["liability_ratio"]
    highest_liability = liability_summary["highest_liability"]

    # -------------------------------------------------
    # No Liabilities
    # -------------------------------------------------

    if active_liabilities == 0:
        insight_status = "No Liabilities"
        insight_priority = "Low"

        reason = "No active liabilities found."

        recommendation = "Maintain a debt-free financial position."

    # -------------------------------------------------
    # Few Liabilities
    # -------------------------------------------------

    elif active_liabilities <= 2:
        insight_status = "Manageable Liabilities"
        insight_priority = "Medium"

        if liability_ratio >= 50:
            reason = (
                "You have a manageable number of liabilities, "
                "but they represent a significant portion of your assets."
            )

        else:
            reason = "Your liabilities are currently manageable."

        if highest_liability is not None:
            recommendation = (
                f"Prioritize paying down your largest liability "
                f"({highest_liability['liability']}) "
                f"(₹{highest_liability['outstanding_balance']:,.2f})."
            )

        else:
            recommendation = "Continue paying liabilities on time."

    # -------------------------------------------------
    # High Liability Load
    # -------------------------------------------------

    else:
        insight_status = "High Liability Load"
        insight_priority = "High"

        reason = "You currently have multiple active liabilities."

        if highest_liability is not None:
            recommendation = (
                f"Reduce your highest liability "
                f"({highest_liability['liability']}) "
                f"before taking additional debt."
            )

        else:
            recommendation = (
                "Avoid taking additional liabilities until existing ones are reduced."
            )

    return {
        "status": insight_status,
        "priority": insight_priority,
        "reason": reason,
        "recommendation": recommendation,
    }

def generate_liability_snapshot(
    liability_summary,
    liability_insights,
):

    liability_snapshot = {
        "liability_summary": liability_summary,
        "liability_insights": liability_insights,
    }

    return liability_snapshot
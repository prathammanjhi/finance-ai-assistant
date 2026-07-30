from datetime import datetime
import pandas as pd
import math


def filter_budget_by_date(
    budget,
    month=None,
    year=None,
):
    """
    Filters budget by month and year.

    If no month or year is provided,
    current month and year are used.
    """

    today = pd.Timestamp.now()

    # Case 1
    if month is not None and year is not None:
        return budget[(budget["Month"] == month) & (budget["Year"] == year)]

    # Case 2
    if month is not None:
        return budget[(budget["Month"] == month) & (budget["Year"] == today.year)]

    # Case 3
    if year is not None:
        return budget[budget["Year"] == year]

    # Case 4 (Default)
    return budget[(budget["Month"] == today.month) & (budget["Year"] == today.year)]


def calculate_budget_analysis(
    filtered_budget,
    monthly_summary,
):
    monthly_budget = filtered_budget["Monthly_Budget"].iloc[0]
    spent = monthly_summary["total_expense"]
    budget_remaining = monthly_budget - spent
    spent = monthly_summary["total_expense"]
    budget_utilization_percentage = (spent / monthly_budget) * 100
    status = "Under Budget" if spent <= monthly_budget else "Over Budget"

    return {
        "monthly_budget": monthly_budget,
        "spent": spent,
        "budget_remaining": budget_remaining,
        "budget_utilization_percentage": budget_utilization_percentage,
        "status": status,
    }


def generate_budget_insights(budget_analysis):
    budget_utilization_percentage = budget_analysis["budget_utilization_percentage"]

    if budget_utilization_percentage < 50:
        status = "Excellent"
        priority = "Low"
        reason = f"You have utilized only {budget_utilization_percentage:.2f}% of your budget, which indicates excellent financial management."
        recommendation = "Continue spending at this pace."
    elif 50 <= budget_utilization_percentage <= 100:
        status = "Balanced"
        priority = "Medium"
        reason = f"You have utilized {budget_utilization_percentage:.2f}% of your budget, which indicates balanced financial management."
        recommendation = "Maintain your current spending habits."
    else:
        status = "Over Budget"
        priority = "High"
        reason = f"You have exceeded your budget by utilizing {budget_utilization_percentage:.2f}% of your budget, which indicates poor financial management."
        recommendation = "Consider reviewing your expenses and cutting down on non-essential spending."

    insights = {
        "budget_health": {
            "status": status,
            "priority": priority,
            "reason": reason,
            "recommendation": recommendation,
        }
    }

    return insights


def generate_budget_snapshot(
    budget_analysis,
    budget_insights,
):

    return {
        "summary": {
            "monthly_budget": budget_analysis["monthly_budget"],
            "spent": budget_analysis["spent"],
            "remaining": budget_analysis["budget_remaining"],
            "utilization": budget_analysis["budget_utilization_percentage"],
            "status": budget_analysis["status"],
        },
        "insights": budget_insights["budget_health"],
    }

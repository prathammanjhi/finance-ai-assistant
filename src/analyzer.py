from datetime import datetime
import pandas as pd
import math


# ==========================
# Expense Analytics
# ==========================
def calculate_summary(transactions):
    total_expense = transactions["Amount"].sum()

    total_need = transactions.loc[transactions["Need/Want"] == "Need", "Amount"].sum()

    total_want = transactions.loc[transactions["Need/Want"] == "Want", "Amount"].sum()

    return {
        "total_expense": total_expense,
        "total_need": total_need,
        "total_want": total_want,
    }


def calculate_expense_distribution(calculate_summary):

    total_expense = calculate_summary["total_expense"]
    total_need = calculate_summary["total_need"]
    total_want = calculate_summary["total_want"]
    if total_expense == 0:
        return {
            "need_amount": total_need,
            "want_amount": total_want,
            "need_percentage": 0,
            "want_percentage": 0,
        }
    else:
        need_percentage = (total_need / total_expense) * 100
        want_percentage = (total_want / total_expense) * 100

        return {
            "need_amount": total_need,
            "want_amount": total_want,
            "need_percentage": need_percentage,
            "want_percentage": want_percentage,
        }


# ==========================
# Income Analytics
# ==========================
def calculate_income(income):

    received_income = income.loc[income["Status"] == "Received", "Amount"].sum()

    pending_income = income.loc[income["Status"] == "Pending", "Amount"].sum()

    return {"received_income": received_income, "pending_income": pending_income}


# ==========================
# Commitment Engine
# ==========================
def calculate_commitments(commitments):

    total_borrowed = commitments["Total Amount"].sum()

    total_repaid = commitments["Repaid"].sum()

    outstanding_debt = commitments["Remaining"].sum()

    active_commitments = len(commitments.loc[commitments["Status"] == "Active"])

    monthly_commitments = commitments.loc[
        commitments["Status"] == "Active", "Monthly Payment"
    ].sum()

    return {
        "total_borrowed": total_borrowed,
        "total_repaid": total_repaid,
        "outstanding_debt": outstanding_debt,
        "monthly_commitments": monthly_commitments,
        "active_commitments": active_commitments,
    }


def calculate_net_position(income_summary, expense_summary, commitment_summary):
    net_position = (
        income_summary["received_income"]
        - expense_summary["total_expense"]
        - commitment_summary["outstanding_debt"]
    )
    cash_position = income_summary["received_income"] - expense_summary["total_expense"]
    expected_position = (
        cash_position
        - commitment_summary["outstanding_debt"]
        + income_summary["pending_income"]
    )

    return {
        "net_position": net_position,
        "cash_position": cash_position,
        "expected_position": expected_position,
    }


def calculate_expense_by_category(transactions):
    expense_by_category = transactions.groupby("Category")["Amount"].sum()
    return expense_by_category


def calculate_highest_spending_category(category_summary):
    if not category_summary.empty:
        highest_category = category_summary.idxmax()
        highest_amount = category_summary.max()
        return {
            "category": highest_category,
            "amount": highest_amount,
        }
    else:
        return {
            "category": None,
            "amount": 0,
        }


def calculate_top_categories(category_summary):
    sorted_categories = category_summary.sort_values(ascending=False)
    top_categories = sorted_categories[:3]
    return {"categories": top_categories}


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


# ==========================
# Date Filtering
# ==========================
def filter_transactions_by_date(transactions, month=None, year=None):
    """
    Filters transactions by month and year.

    If no month or year is provided,
    current month and year are used.
    """

    today = pd.Timestamp.now()

    # Case 1
    if month is not None and year is not None:
        return transactions[
            (transactions["Date"].dt.month == month)
            & (transactions["Date"].dt.year == year)
        ]

    # Case 2
    if month is not None:
        return transactions[
            (transactions["Date"].dt.month == month)
            & (transactions["Date"].dt.year == today.year)
        ]

    # Case 3
    if year is not None:
        return transactions[transactions["Date"].dt.year == year]

    # Case 4 (Default)
    return transactions[
        (transactions["Date"].dt.month == today.month)
        & (transactions["Date"].dt.year == today.year)
    ]


# =========================
# Snapshot and Insights
# =========================


def generate_financial_snapshot(
    monthly_summary,
    monthly_distribution,
    income_summary,
    commitment_summary,
    financial_position,
    savings_summary,
):
    snapshot = {
        "monthly_summary": monthly_summary,
        "monthly_distribution": monthly_distribution,
        "income_summary": income_summary,
        "commitment_summary": commitment_summary,
        "financial_position": financial_position,
        "savings_summary": savings_summary,
    }

    return snapshot


def generate_financial_insights(financial_snapshot):

    monthly_distribution = financial_snapshot["monthly_distribution"]
    need_percentage = monthly_distribution["need_percentage"]

    if need_percentage > 70:
        need_status = "Healthy"
        need_priority = "Low"
        need_reason = "You are spending a significant portion of your income on essential needs, which is a positive financial behavior."
    elif 50 <= need_percentage <= 70:
        need_status = "Balanced"
        need_priority = "Medium"
        need_reason = (
            "You are balancing your spending between essential needs and wants."
        )
    else:
        need_status = "Low"
        need_priority = "High"
        need_reason = "Your Essential spending is lower than recommended."

    want_percentage = monthly_distribution["want_percentage"]

    if want_percentage < 30:
        want_status = "Excellent"
        want_priority = "Low"
        want_reason = "You are spending a smaller portion of your income on discretionary wants, which is a positive financial behavior."
    elif 30 <= want_percentage <= 50:
        want_status = "Balanced"
        want_priority = "Medium"
        want_reason = (
            "You are balancing your spending between essential needs and wants."
        )
    else:
        want_status = "Unhealthy"
        want_priority = "High"
        want_reason = (
            "You are spending a large portion of your income on discretionary wants."
        )

    cash_position = financial_snapshot["financial_position"]["cash_position"]

    if cash_position > 0:
        cash_flow_status = "Positive Cash Flow"
        cash_flow_priority = "Low"
        cash_flow_reason = "You have a positive cash flow, indicating that your income exceeds your expenses. This is a healthy financial situation."
    elif cash_position == 0:
        cash_flow_status = "Break-even"
        cash_flow_priority = "Medium"
        cash_flow_reason = (
            "Your income equals your expenses, resulting in no net gain or loss."
        )
    else:
        cash_flow_status = "Negative Cash Flow"
        cash_flow_priority = "High"
        cash_flow_reason = (
            "Your expenses exceed your income, leading to a negative cash flow."
        )

    net_position = financial_snapshot["financial_position"]["net_position"]

    if net_position > 0:
        net_position_status = "Financially Healthy"
        net_position_priority = "Low"
        net_position_reason = "You have a positive net position, indicating that your assets exceed your liabilities. This is a healthy financial situation."
    elif net_position == 0:
        net_position_status = "Neutral"
        net_position_priority = "Medium"
        net_position_reason = "Your assets equal your liabilities."
    else:
        net_position_status = "Financially Stressed"
        net_position_priority = "High"
        net_position_reason = "Your liabilities exceed your assets, indicating a financially stressful situation."

    outstanding_debt = financial_snapshot["commitment_summary"]["outstanding_debt"]

    if outstanding_debt == 0:
        outstanding_debt_status = "Debt-Free"
        outstanding_debt_priority = "Low"
        outstanding_debt_reason = "You are not carrying any outstanding debt."
    else:
        outstanding_debt_status = "Active Debt"
        outstanding_debt_priority = "High"
        outstanding_debt_reason = (
            "You have outstanding debt that needs to be addressed."
        )

    insights = {
        "📌 Need Spending": {
            "status": need_status,
            "priority": need_priority,
            "reason": need_reason,
        },
        "📌 Want Spending": {
            "status": want_status,
            "priority": want_priority,
            "reason": want_reason,
        },
        "📌 Cash Flow": {
            "status": cash_flow_status,
            "priority": cash_flow_priority,
            "reason": cash_flow_reason,
        },
        "📌 Net Position": {
            "status": net_position_status,
            "priority": net_position_priority,
            "reason": net_position_reason,
        },
        "📌 Debt Status": {
            "status": outstanding_debt_status,
            "priority": outstanding_debt_priority,
            "reason": outstanding_debt_reason,
        },
    }

    return insights


"""
Analyzes the current month's budget and
returns spending metrics.
"""


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


def budget_insights(budget_analysis):
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
        "💰 Budget Health ": {
            "status": status,
            "priority": priority,
            "reason": reason,
            "recommendation": recommendation,
        }
    }

    return insights

def generate_investment_snapshot(
        investment_summary,
        investment_insights,
):
    investment_snapshot = {
        "investment_summary": investment_summary,
        "investment_insights": investment_insights,
    }

    return investment_snapshot
    
def generate_investment_insights(investment_snapshot):

    investment_summary = investment_snapshot["investment_summary"]

    # total_invested = investment_summary["total_invested"]
    # current_value = investment_summary["current_value"]
    # total_profit_loss = investment_summary["total_profit_loss"]
    # investment_growth = investment_summary["investment_growth"]
    return_percentage = investment_summary["return_percentage"]
    active_investments = investment_summary["active_investments"]

    if active_investments == 0 :
        insight_status = "No Investments"
        insight_priority = "Medium"
        reason = "No Active Investments found."
        recommendation = "Start Investing to build Long-term wealth."
    elif return_percentage < 0 :
        insight_status = "Loss"
        insight_priority = "High"
        reason = "Investment portfolio is currently in loss."
        recommendation = "Review investments before making new allocations."
    elif 0 <= return_percentage < 8 :
        insight_status = "Growing Slowly"
        insight_priority = "Medium"
        reason = "Portfolio is generating modest returns."
        recommendation = "Review diversification and long-term strategy."
    elif return_percentage >= 8 :
        insight_status = "Healthy Growth"
        insight_priority = "Low"
        reason = "Portfolio is performing well."
        recommendation = "Continue disciplined investing."
    elif return_percentage > 15  :
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
            

# ==========================================================
# Engine Name : Savings Engine
# Layer       : Calculation Layer
#
# Responsibility
# Calculates savings-related financial metrics.
#
# Inputs
# - Income Summary
# - Expense Summary
# - Commitment Summary
#
# Outputs
# - Savings Summary Dictionary
#
# Dependencies
# - Income Engine
# - Expense Engine
# - Commitment Engine
#
# Used By
# - Emergency Fund Engine
# - Goal Engine
# - Financial Health Score
# - Recommendation Engine
# ==========================================================


# Savings Summary
def calculate_savings(income_summary, expense_summary, commitment_summary):
    total_income = income_summary["received_income"]
    total_expense = expense_summary["total_expense"]
    total_commitments = (
        commitment_summary["monthly_commitments"]
        if "monthly_commitments" in commitment_summary
        else 0
    )

    gross_savings = total_income - total_expense
    net_savings = gross_savings - total_commitments
    expense_ratio = (total_expense / total_income) * 100 if total_income > 0 else 0
    commitment_ratio = (
        (total_commitments / total_income) * 100 if total_income > 0 else 0
    )
    savings_rate = (net_savings / total_income) * 100 if total_income > 0 else 0

    return {
        "total_income": total_income,
        "total_expense": total_expense,
        "total_commitments": total_commitments,
        "gross_savings": gross_savings,
        "net_savings": net_savings,
        "expense_ratio": expense_ratio,
        "commitment_ratio": commitment_ratio,
        "savings_rate": savings_rate,
    }


# ==========================================================
# Engine Name : Emergency Fund Engine
# Layer       : Calculation Layer
#
# Responsibility
# Calculates emergency fund and financial survival metrics.
#
# Inputs
# - Expense Summary
# - Commitment Summary
# - Savings Summary
#
# Outputs
# - Emergency Fund Summary Dictionary
#
# Dependencies
# - Expense Engine
# - Commitment Engine
# - Savings Engine
#
# Used By
# - Financial Health Score
# - Recommendation Engine
# - Goal Engine
# - Cash Flow Forecast Engine
#
# Temporary Assumption
# Net Savings is used as the current emergency fund balance.
# Future versions will use liquid assets or a dedicated
# emergency fund balance source.
# ==========================================================


def calculate_emergency_fund(expense_summary, commitment_summary, savings_summary):
    current_emergency_fund = max(0, savings_summary["net_savings"])
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
        current_emergency_fund / monthly_survival_cost
        if monthly_survival_cost > 0
        else 0
    )
    gap = required_6_months_fund - current_emergency_fund
    emergency_fund_gap = max(0, gap)

    return {
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


# ==========================================================
# Engine Name : Financial Goal Engine
# Layer       : Calculation Layer

# Responsibility
# Calculates individual and portfolio-level
# financial goal progress metrics.

# Inputs
# - Financial Goals DataFrame

# Outputs
# - Goal Analysis
# - Goal Portfolio Summary

# Dependencies
# - Financial Goals Reader

# Used By
# - Financial Health Score
# - Recommendation Engine
# - Finance Context Builder
# - Dashboard
# - Monthly Review

# Does Not
# - Allocate savings
# - Assign recommendations
# - Change user priorities
# - Generate financial advice
# ==========================================================


def calculate_goals(goals):
    goal_analysis = []

    for index, goal in goals.iterrows():
        # 1. Extract values
        goal_name = goal["Goal"]
        goal_type = goal["Type"]
        target_amount = goal["Target Amount"]
        current_amount = goal["Current Amount"]
        target_date = goal["Target Date"]
        priority = goal["Priority"]
        status = goal["Status"]

        # 2. Calculations
        remaining_amount = max(0, target_amount - current_amount)
        progress_percentage = round(
            min(100, max(0, (current_amount / target_amount) * 100))
            if target_amount > 0
            else 0,
            2,
        )
        today = datetime.today()
        days_remaining = (target_date - today).days
        months_remaining = max(0, math.ceil(days_remaining / 30))
        required_monthly_contribution = math.ceil(remaining_amount / months_remaining)

        # 3. Append dictionary
        goal_analysis.append(
            {
                "goal": goal_name,
                "type": goal_type,
                "target_amount": target_amount,
                "current_amount": current_amount,
                "remaining_amount": remaining_amount,
                "progress_percentage": progress_percentage,
                "target_date": target_date,
                "priority": priority,
                "status": status,
                "months_remaining": months_remaining,
                "required_monthly_contribution": required_monthly_contribution,
            }
        )

    # ============================
    # Goal Portfolio Summary
    # ============================

    total_goals = len(goals)

    active_goals = len(goals.loc[goals["Status"] == "Active"])

    completed_goals = len(goals.loc[goals["Status"] == "Completed"])

    paused_goals = len(goals.loc[goals["Status"] == "Paused"])

    cancelled_goals = len(goals.loc[goals["Status"] == "Cancelled"])

    completion_rate = (completed_goals / total_goals) * 100 if total_goals > 0 else 0

    active_goal_rate = (active_goals / total_goals) * 100 if total_goals > 0 else 0

    total_target_amount = goals["Target Amount"].sum()

    total_current_amount = goals["Current Amount"].sum()

    total_remaining_amount = max(0, total_target_amount - total_current_amount)

    overall_progress_percentage = round(
        min(100, max(0, (total_current_amount / total_target_amount) * 100))
        if total_target_amount > 0
        else 0,
        2,
    )

    goal_summary = {
        # Goal Counts
        "total_goals": total_goals,
        "active_goals": active_goals,
        "completed_goals": completed_goals,
        "paused_goals": paused_goals,
        "cancelled_goals": cancelled_goals,
        # Goal Rates
        "completion_rate": completion_rate,
        "active_goal_rate": active_goal_rate,
        # Financial Totals
        "total_target_amount": total_target_amount,
        "total_current_amount": total_current_amount,
        "total_remaining_amount": total_remaining_amount,
        # Portfolio Progress
        "overall_progress_percentage": overall_progress_percentage,
    }

    return goal_analysis, goal_summary


def generate_goal_insights(goal_snapshot):
    goal_insights = []
    goal_analysis = goal_snapshot["goal_analysis"]
    for goal in goal_analysis:
        goal_name = goal["goal"]
        progress = goal["progress_percentage"]
        months_remaining = goal["months_remaining"]
        goal_priority = goal["priority"]
        status = goal["status"]

        if status == "Completed":
            insight_status = "Completed"
            insight_priority = "None"
            reason = "Goal has been achieved."
            recommendation = "Create a new financial goal."

        elif progress < 20 and months_remaining <= 3:
            insight_status = "Critical"
            insight_priority = "High"
            reason = "Goal is significantly behind schedule."
            recommendation = "Increase monthly contribution immediately."

        elif progress < 50 and goal_priority == "High":
            insight_status = "Critical"
            insight_priority = "High"
            reason = "Goal progress is below expected pace."
            recommendation = "Increase monthly savings toward this goal."

        elif progress < 50 and goal_priority == "Medium":
            insight_status = "Behind"
            insight_priority = "Medium"
            reason = "Goal progress is below expected pace."
            recommendation = "Increase monthly savings toward this goal."

        elif progress < 50:
            insight_status = "Behind"
            insight_priority = "Medium"
            reason = "Goal progress is below expected pace."
            recommendation = "Increase monthly savings toward this goal."

        elif goal_priority == "High":
            insight_status = "Behind"
            insight_priority = "Medium"
            reason = "Goal progress is below expected pace."
            recommendation = "Increase monthly savings toward this goal."

        else:
            insight_status = "On Track"
            insight_priority = "Normal"
            reason = "Goal is progressing steadily."
            recommendation = "Continue current contribution."

        goal_insights.append(
            {
                "goal": goal_name,
                "goal_priority": goal_priority,
                "status": insight_status,
                "priority": insight_priority,
                "reason": reason,
                "recommendation": recommendation,
            }
        )
    return goal_insights


def generate_goal_snapshot(
    goal_analysis,
    goal_summary,
    goal_insights,
):
    goal_snapshot = {
        "goal_analysis": goal_analysis,
        "goal_summary": goal_summary,
        "goal_insights": goal_insights,
    }

    return goal_snapshot

#====================================================
#Assets
#====================================================

def calculate_assets(assets):

    total_asset_value = assets["Current Value"].sum()

    purchase_value = assets["Purchase Value"].sum()

    asset_profit_loss = total_asset_value - purchase_value

    active_assets = (
        assets["Status"] == "Active"
    ).sum()

    largest_asset_row = assets.loc[
        assets["Current Value"].idxmax()
    ] if not assets.empty else None

    largest_asset = {
        "asset": largest_asset_row["Asset"],
        "category": largest_asset_row["Category"],
        "purchase_value": largest_asset_row["Purchase Value"],
        "current_value": largest_asset_row["Current Value"],
    }

    asset_return_percentage = (
    (asset_profit_loss / purchase_value) * 100
    if purchase_value > 0
    else 0
    )
    

    asset_summary = {
        "total_asset_value": total_asset_value,
        "purchase_value": purchase_value,
        "asset_profit_loss": asset_profit_loss,
        "active_assets": active_assets,
        "largest_asset": largest_asset,
        "asset_return_percentage": asset_return_percentage,
    }


    return asset_summary

def generate_asset_snapshot(
    asset_summary,
    asset_insights,
):
    asset_snapshot = {
    "asset_summary": asset_summary,
    "asset_insights": asset_insights,
}

    return asset_snapshot

# ==========================================================
# Asset Insight Engine
# ==========================================================

def generate_asset_insights(asset_snapshot):

    asset_summary = asset_snapshot["asset_summary"]

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

        reason = (
            f"Your asset base is still limited and is currently {asset_health}"
        )

        if largest_asset is not None:

            recommendation = (
                f"Continue acquiring productive assets. "
                f"Current largest asset: {largest_asset['asset']} "
                f"(₹{largest_asset['current_value']:,.2f})."
            )

        else:

            recommendation = (
                "Continue acquiring productive assets."
            )

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

            recommendation = (
                "Maintain your existing assets and gradually increase appreciating assets."
            )

    return {

        "status": insight_status,
        "priority": insight_priority,
        "reason": reason,
        "recommendation": recommendation,

    }

##########################################################
# Liabilities Engine
#########################################################

def calculate_liabilities(liabilities, asset_snapshot):

    asset_summary = asset_snapshot["asset_summary"]
    total_asset_value = asset_summary["total_asset_value"]
    total_original_loan = liabilities["Original Loan"].sum()

    total_outstanding_balance = liabilities["Outstanding Balance"].sum()

    monthly_liability_payment = (
        liabilities.loc[
            liabilities["Status"] == "Active",
            "Monthly EMI",
        ].sum()
    )
    active_liabilities = len(liabilities.loc[liabilities["Status"] == "Active"])
    monthly_liability_payment = liabilities.loc[
        liabilities["Status"] == "Active",
        "Monthly EMI",
    ].sum()
    
    highest_liability_row = (
    liabilities.loc[
        liabilities["Outstanding Balance"].idxmax()
    ]
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

    liability_ratio = (
        (total_outstanding_balance / total_asset_value) * 100
        if total_asset_value > 0
        else 0
    )

    average_liability = (
        total_outstanding_balance / active_liabilities
        if active_liabilities > 0
        else 0
    )

    total_repaid = (
        total_original_loan
        - total_outstanding_balance
    )

    repayment_percentage = (
        (
            total_repaid
            / total_original_loan
        )
        * 100
        if total_original_loan > 0
        else 0
    )

    largest_monthly_emi = (
        liabilities["Monthly EMI"].max()
        if not liabilities.empty
        else 0
    )

    remaining_repayment_percentage = (
        100
        - repayment_percentage
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

def generate_liability_insights(liability_snapshot):

    liability_summary = liability_snapshot["liability_summary"]

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

        recommendation = (
            "Maintain a debt-free financial position."
        )

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

            reason = (
                "Your liabilities are currently manageable."
            )

        if highest_liability is not None:

            recommendation = (
                f"Prioritize paying down your largest liability "
                f"({highest_liability['liability']}) "
                f"(₹{highest_liability['outstanding_balance']:,.2f})."
            )

        else:

            recommendation = (
                "Continue paying liabilities on time."
            )

    # -------------------------------------------------
    # High Liability Load
    # -------------------------------------------------

    else:

        insight_status = "High Liability Load"
        insight_priority = "High"

        reason = (
            "You currently have multiple active liabilities."
        )

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
    
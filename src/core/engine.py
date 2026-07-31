from src.core.reader import (
    load_transactions,
    load_income,
    load_commitments,
    load_budget,
    load_goals,
    load_investments,
    load_assets,
    load_liabilities,
)
from src.core.analyzer import (
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
    generate_budget_insights,
    generate_budget_snapshot,
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
    generate_wealth_health_snapshot,
    generate_wealth_health_insights,
    calculate_wealth_health,
    generate_financial_health_snapshot,
    generate_financial_health_insights,
    calculate_financial_health,
)

from src.core.processors import *

def process_investments():

    investments = load_investments()

    investment_summary = calculate_investments(investments)

    investment_insights = generate_investment_insights(
        investment_summary,
    )

    investment_snapshot = generate_investment_snapshot(
        investment_summary,
        investment_insights,
    )

    return investment_snapshot


def process_budget(monthly_summary):

    budget = load_budget()

    filtered_budget = filter_budget_by_date(
        budget,
    )

    budget_analysis = calculate_budget_analysis(
        filtered_budget,
        monthly_summary,
    )

    budget_insights = generate_budget_insights(
        budget_analysis,
    )

    budget_snapshot = generate_budget_snapshot(
        budget_analysis,
        budget_insights,
    )

    return budget_analysis, budget_snapshot


def process_assets():

    assets = load_assets()

    asset_summary = calculate_assets(
        assets,
    )

    asset_insights = generate_asset_insights(
        asset_summary,
    )

    asset_snapshot = generate_asset_snapshot(
        asset_summary,
        asset_insights,
    )

    return asset_summary, asset_snapshot


def process_goals():

    goals = load_goals()

    goal_analysis, goal_summary = calculate_goals(
        goals,
    )

    goal_insights = generate_goal_insights(
        goal_analysis,
    )

    goal_snapshot = generate_goal_snapshot(
        goal_analysis,
        goal_summary,
        goal_insights,
    )

    return goal_snapshot


def process_liabilities(asset_snapshot):

    liabilities = load_liabilities()

    liability_summary = calculate_liabilities(
        liabilities,
        asset_snapshot,
    )

    liability_insights = generate_liability_insights(
        liability_summary,
    )

    liability_snapshot = generate_liability_snapshot(
        liability_summary,
        liability_insights,
    )

    return liability_snapshot


def process_net_worth(
    asset_snapshot,
    liability_snapshot,
):

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

    return net_worth_snapshot


def process_wealth_health(
    emergency_summary,
    goal_snapshot,
    investment_snapshot,
    asset_snapshot,
    liability_snapshot,
    net_worth_snapshot,
):

    wealth_health_summary = calculate_wealth_health(
        emergency_summary,
        goal_snapshot,
        investment_snapshot,
        asset_snapshot,
        liability_snapshot,
        net_worth_snapshot,
    )

    wealth_health_insights = generate_wealth_health_insights(
        wealth_health_summary,
    )

    wealth_health_snapshot = generate_wealth_health_snapshot(
        wealth_health_summary,
        wealth_health_insights,
    )

    return wealth_health_snapshot


def process_financial_health(
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

    financial_health_summary = calculate_financial_health(
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
    )

    financial_health_insights = generate_financial_health_insights(
        financial_health_summary,
    )

    financial_health_snapshot = generate_financial_health_snapshot(
        financial_health_summary,
        financial_health_insights,
    )

    return financial_health_snapshot



def analyze_finances(workbook_path=None):

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

    monthly_transactions = filter_transactions_by_date(transactions)
    monthly_summary = calculate_summary(monthly_transactions)
    monthly_distribution = calculate_expense_distribution(monthly_summary)
    savings_summary = calculate_savings(
        income_summary, 
        summary, 
        commitment_summary,
        )
    print(savings_summary)
    financial_snapshot = generate_financial_snapshot(
        monthly_summary,
        monthly_distribution,
        income_summary,
        commitment_summary,
        financial_position,
        savings_summary,
        highest_spending,
        top_three_categories,
    )
    financial_insights = generate_financial_insights(financial_snapshot)

    financial_snapshot["insights"] = financial_insights


    # Assets
    asset_summary, asset_snapshot = process_assets()

    # Emergency Fund
    emergency_summary = calculate_emergency_fund(
        summary,
        commitment_summary,
        asset_summary,
    )

    # Investments
    investment_snapshot = process_investments()

    # Budget
    budget_analysis, budget_snapshot = process_budget(
        monthly_summary,
    )

    # Goals
    goal_snapshot = process_goals()

    # Liabilities
    liability_snapshot = process_liabilities(
        asset_snapshot,
    )

    # Net Worth
    net_worth_snapshot = process_net_worth(
        asset_snapshot,
        liability_snapshot,
    )

    # Wealth Health
    wealth_health_snapshot = process_wealth_health(
        emergency_summary,
        goal_snapshot,
        investment_snapshot,
        asset_snapshot,
        liability_snapshot,
        net_worth_snapshot,
    )

    # Financial Health
    financial_health_snapshot = process_financial_health(
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
    )


    results = {}

    # Core Financial Overview
    results["summary"] = summary
    results["income_summary"] = income_summary
    results["commitment_summary"] = commitment_summary
    results["financial_position"] = financial_position
    results["financial_snapshot"] = financial_snapshot

    # Budget
    results["budget"] = budget_snapshot

    # Savings & Emergency
    results["savings"] = savings_summary
    results["emergency_fund"] = emergency_summary

    # Goals
    results["goals"] = goal_snapshot

    # Investments
    results["investment"] = investment_snapshot

    # Assets & Liabilities
    results["assets"] = asset_snapshot
    results["liabilities"] = liability_snapshot

    # Net Worth
    results["net_worth"] = net_worth_snapshot

    # Overall Scores
    results["wealth_health"] = wealth_health_snapshot
    results["financial_health"] = financial_health_snapshot

    return results



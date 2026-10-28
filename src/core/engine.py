from src.core.processors import *


def analyze_finances(workbook_path=None, month=None, year=None):
    # Load Data
    financial = process_financial(
        month=month,
        year=year,
    )

    # Assets
    asset_summary, asset_snapshot = process_assets()

    # Emergency Fund
    emergency_summary = process_emergency_fund(
        financial["summary"],
        financial["commitment_summary"],
        asset_summary,
    )

    # Investments
    investment_snapshot = process_investments()

    # Budget
    budget_analysis, budget_snapshot = process_budget(
        financial["monthly_summary"],
        month=month,
        year=year,
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
        financial["financial_snapshot"],
        budget_analysis,
        financial["savings_summary"],
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
    results["summary"] = financial["summary"]
    results["income_summary"] = financial["income_summary"]
    results["commitment_summary"] = financial["commitment_summary"]
    results["financial_position"] = financial["financial_position"]
    results["financial_snapshot"] = financial["financial_snapshot"]

    # Budget
    results["budget"] = budget_snapshot

    # Savings & Emergency
    results["savings"] = financial["savings_summary"]
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

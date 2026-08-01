from src.core.analyzer import (
    calculate_financial_health,
    generate_financial_health_insights,
    generate_financial_health_snapshot,
)


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

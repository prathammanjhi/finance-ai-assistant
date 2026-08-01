from src.core.analyzer import (
    calculate_wealth_health,
    generate_wealth_health_insights,
    generate_wealth_health_snapshot,
)


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

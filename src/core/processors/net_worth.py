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


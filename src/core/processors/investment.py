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


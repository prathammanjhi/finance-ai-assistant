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


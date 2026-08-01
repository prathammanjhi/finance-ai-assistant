from src.core.reader.budget import *

from src.core.analyzer import (
    calculate_budget_analysis,
    generate_budget_insights,
    generate_budget_snapshot,
    filter_budget_by_date,
)


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

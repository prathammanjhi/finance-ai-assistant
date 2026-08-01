from src.core.reader.liability import *

from src.core.analyzer import (
    calculate_liabilities,
    generate_liability_insights,
    generate_liability_snapshot,
)


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

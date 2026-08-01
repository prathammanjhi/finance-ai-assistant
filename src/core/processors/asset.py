from src.core.reader.asset import *

from src.core.analyzer import (
    calculate_assets,
    generate_asset_insights,
    generate_asset_snapshot,
)


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

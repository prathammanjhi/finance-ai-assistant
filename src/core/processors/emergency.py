from src.core.analyzer import calculate_emergency_fund

def process_emergency_fund(
    summary,
    commitment_summary,
    asset_summary,
):

    emergency_summary = calculate_emergency_fund(
        summary,
        commitment_summary,
        asset_summary,
    )

    return emergency_summary
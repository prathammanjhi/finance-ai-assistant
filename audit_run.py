from src.core.engine import analyze_finances

r = analyze_finances(month=7, year=2026)
fp = r["financial_position"]

print("=== Financial Position ===")
print("net_position:", fp["net_position"])
print("cash_position:", fp["cash_position"])
print("expected_position:", fp["expected_position"])

print("\n=== Monthly Summary ===")
ms = r["financial_snapshot"]["monthly_summary"]
print("total_expense:", ms["total_expense"])
print("total_need:", ms["total_need"])
print("total_want:", ms["total_want"])

print("\n=== Monthly Distribution ===")
md = r["financial_snapshot"]["monthly_distribution"]
print("need_percentage:", md["need_percentage"])
print("want_percentage:", md["want_percentage"])

print("\n=== Income Summary ===")
inc = r["income_summary"]
print("received_income:", inc["received_income"])
print("pending_income:", inc["pending_income"])

print("\n=== Savings ===")
sv = r["savings"]
print("total_income:", sv["total_income"])
print("total_expense:", sv["total_expense"])
print("total_commitments:", sv["total_commitments"])
print("gross_savings:", sv["gross_savings"])
print("net_savings:", sv["net_savings"])
print("savings_rate:", sv["savings_rate"])

print("\n=== Commitment Summary ===")
cs = r["commitment_summary"]
print("outstanding_debt:", cs["outstanding_debt"])
print("monthly_commitments:", cs["monthly_commitments"])
print("active_commitments:", cs["active_commitments"])

print("\n=== Financial Snapshot Insights ===")
for k, v in r["financial_snapshot"]["insights"].items():
    print(f"  {k}: status={v['status']}, priority={v['priority']}")

print("\n=== Budget ===")
b = r["budget"]
print("monthly_budget:", b["summary"]["monthly_budget"])
print("spent:", b["summary"]["spent"])
print("utilization:", b["summary"]["utilization"])
print("status:", b["summary"]["status"])
print("insight status:", b["insights"]["status"])

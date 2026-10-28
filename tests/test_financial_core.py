import pytest
import pandas as pd
from datetime import datetime
from src.core.analyzer.financial import (
    calculate_summary, 
    calculate_net_position,
    calculate_savings,
    generate_financial_insights
)
from src.shared.config import FinanceConfig

def test_calculate_summary():
    data = {
        "Amount": [1000, 200, 300],
        "Need/Want": ["Need", "Want", "Need"],
        "is_anomaly": [False, True, False]
    }
    df = pd.DataFrame(data)
    res = calculate_summary(df)
    
    assert res["total_expense"] == 1500
    assert res["total_need"] == 1300
    assert res["total_want"] == 200
    assert res["anomaly_count"] == 1

def test_net_position():
    inc = {"received_income": 5000, "pending_income": 1000}
    exp = {"total_expense": 2000}
    com = {"monthly_commitments": 500, "outstanding_debt": 90000}
    
    res = calculate_net_position(inc, exp, com)
    
    assert res["cash_position"] == 3000
    assert res["net_position"] == 4000
    assert res["expected_position"] == 3500

def test_calculate_savings():
    inc = {"received_income": 10000, "pending_income": 0}
    exp = {"total_expense": 4000}
    com = {"monthly_commitments": 2000}
    
    res = calculate_savings(inc, exp, com)
    
    assert res["gross_savings"] == 6000
    assert res["net_savings"] == 4000
    assert res["savings_rate"] == 60.0
    assert res["expense_ratio"] == 40.0
    assert res["commitment_ratio"] == 20.0

def test_zero_income_savings():
    inc = {"received_income": 0, "pending_income": 0}
    exp = {"total_expense": 4000}
    com = {"monthly_commitments": 2000}
    
    res = calculate_savings(inc, exp, com)
    
    assert res["savings_rate"] == 0.0

def test_financial_insights_insufficient_data():
    res = generate_financial_insights({}, insufficient_data=True)
    assert res["Need Spending"]["status"] == "INSUFFICIENT_DATA"

def test_financial_insights_logic():
    snapshot = {
        "monthly_distribution": {"need_percentage": 75.0, "want_percentage": 20.0},
        "financial_position": {"cash_position": 5000, "net_position": 6000},
        "income_summary": {"received_income": 10000, "pending_income": 0},
        "savings_summary": {"commitment_ratio": 10.0, "savings_rate": 30.0},
        "commitment_summary": {"outstanding_debt": 10000}
    }
    
    insights = generate_financial_insights(snapshot)
    
    assert insights["Need Spending"]["status"] == "NEED_HIGH"
    assert insights["Want Spending"]["status"] == "WANT_LOW"
    assert insights["Cash Flow"]["status"] == "CASH_FLOW_POSITIVE"
    assert insights["Net Position"]["status"] == "NET_POSITION_POSITIVE"
    assert insights["Debt Status"]["status"] == "DEBT_BURDEN_LOW"
    assert insights["Savings Rate"]["status"] == "SAVINGS_RATE_GOOD"

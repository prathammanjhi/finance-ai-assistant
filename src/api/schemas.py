from pydantic import BaseModel
from datetime import datetime



class Summary(BaseModel):
    total_expense: int
    total_need: int
    total_want: int

class IncomeSummary(BaseModel):
    received_income: int
    pending_income: int

class FinanceResponse(BaseModel):
    summary: Summary
    income_summary: IncomeSummary
    commitment_summary: CommitmentSummary
    financial_position: FinancialPosition
    financial_snapshot: FinancialSnapshot
    budget: Budget
    savings: SavingsSummary
    emergency_fund: EmergencyFund
    goals: Goals
    investment: Investment
    assets: Assets
    liabilities: Liabilities
    net_worth: NetWorth
    wealth_health: WealthHealth
    financial_health: FinancialHealth

class CommitmentSummary(BaseModel):
    total_borrowed: int
    total_repaid: int
    outstanding_debt: int
    monthly_commitments: int
    active_commitments: int

class FinancialPosition(BaseModel):
    net_position: int
    cash_position: int
    expected_position: int

class MonthlySummary(BaseModel):
    total_expense: int
    total_need: int
    total_want: int


class MonthlyDistribution(BaseModel):
    need_amount: int
    want_amount: int
    need_percentage: float
    want_percentage: float


class SavingsSummary(BaseModel):
    total_income: int
    total_expense: int
    total_commitments: int
    gross_savings: int
    net_savings: int
    expense_ratio: float
    commitment_ratio: float
    savings_rate: float

class HighestSpending(BaseModel):
    category: str
    amount: int


class TopThreeCategories(BaseModel):
    categories: dict[str, int]

class FinancialInsight(BaseModel):
    status: str
    priority: str
    reason: str

class FinancialSnapshot(BaseModel):
    monthly_summary: MonthlySummary
    monthly_distribution: MonthlyDistribution
    income_summary: IncomeSummary
    commitment_summary: CommitmentSummary
    financial_position: FinancialPosition
    savings_summary: SavingsSummary
    highest_spending: HighestSpending
    top_three_categories: TopThreeCategories
    insights: dict[str, FinancialInsight]

class BudgetSummary(BaseModel):
    monthly_budget: int
    spent: int
    remaining: int
    utilization: float
    status: str


class BudgetInsight(BaseModel):
    status: str
    priority: str
    reason: str
    recommendation: str


class Budget(BaseModel):
    summary: BudgetSummary
    insights: BudgetInsight

class EmergencyFund(BaseModel):
    current_emergency_fund: int
    total_monthly_expenses: int
    total_monthly_commitments: int
    monthly_survival_cost: int
    required_3_months_fund: int
    required_6_months_fund: int
    required_12_months_fund: int
    coverage_months: float
    emergency_fund_gap: int

class GoalAnalysis(BaseModel):
    goal: str
    type: str
    target_amount: int
    current_amount: int
    remaining_amount: int
    progress_percentage: float
    target_date: datetime
    priority: str
    status: str
    months_remaining: int
    required_monthly_contribution: int


class GoalSummary(BaseModel):
    total_goals: int
    active_goals: int
    completed_goals: int
    paused_goals: int
    cancelled_goals: int
    completion_rate: float
    active_goal_rate: float
    total_target_amount: int
    total_current_amount: int
    total_remaining_amount: int
    overall_progress_percentage: float


class GoalInsight(BaseModel):
    goal: str
    goal_priority: str
    status: str
    priority: str
    reason: str
    recommendation: str


class Goals(BaseModel):
    goal_analysis: list[GoalAnalysis]
    goal_summary: GoalSummary
    goal_insights: list[GoalInsight]

class InvestmentSummary(BaseModel):
    total_invested: int
    current_value: int
    total_profit_loss: int
    return_percentage: float
    active_investments: int
    investment_growth: str


class InvestmentInsight(BaseModel):
    status: str
    priority: str
    reason: str
    recommendation: str


class Investment(BaseModel):
    investment_summary: InvestmentSummary
    investment_insights: InvestmentInsight

class LargestAsset(BaseModel):
    asset: str
    category: str
    purchase_value: int
    current_value: int


class AssetSummary(BaseModel):
    total_asset_value: int
    purchase_value: int
    asset_profit_loss: int
    active_assets: int
    largest_asset: LargestAsset
    asset_return_percentage: float
    emergency_fund: int


class AssetInsight(BaseModel):
    status: str
    priority: str
    reason: str
    recommendation: str


class Assets(BaseModel):
    asset_summary: AssetSummary
    asset_insights: AssetInsight

class HighestLiability(BaseModel):
    liability: str
    category: str
    original_loan: int
    outstanding_balance: int
    monthly_emi: int


class LiabilitySummary(BaseModel):
    total_original_loan: int
    total_outstanding_balance: int
    total_repaid: int
    repayment_percentage: float
    monthly_liability_payment: int
    largest_monthly_emi: int
    active_liabilities: int
    highest_liability: HighestLiability
    liability_ratio: float
    average_liability: float
    remaining_repayment_percentage: float


class LiabilityInsight(BaseModel):
    status: str
    priority: str
    reason: str
    recommendation: str


class Liabilities(BaseModel):
    liability_summary: LiabilitySummary
    liability_insights: LiabilityInsight

class NetWorthSummary(BaseModel):
    total_assets: int
    total_liabilities: int
    net_worth: int
    equity: int
    asset_coverage_ratio: float
    debt_percentage: float
    wealth_category: str
    asset_to_liability_ratio: float
    financial_leverage: float
    wealth_growth: float
    net_assets: int
    debt_free_percentage: float
    wealth_score: float
    wealth_efficiency: float


class NetWorthInsight(BaseModel):
    status: str
    priority: str
    reason: str
    recommendation: str


class NetWorth(BaseModel):
    net_worth_summary: NetWorthSummary
    net_worth_insights: NetWorthInsight

class WealthHealthSummary(BaseModel):
    wealth_score: int
    wealth_grade: str
    wealth_risk: str
    capital_strength: str
    emergency_score: int
    goal_score: int
    investment_score: int
    asset_score: int
    liability_score: int
    net_worth_score: int
    growth_readiness: str
    liquidity_strength: str
    wealth_momentum: str
    financial_stability: str
    long_term_sustainability: str


class WealthHealthInsight(BaseModel):
    status: str
    priority: str
    reason: str
    recommendation: str


class WealthHealth(BaseModel):
    wealth_health_summary: WealthHealthSummary
    wealth_health_insights: WealthHealthInsight

class FinancialHealthSummary(BaseModel):
    financial_health_score: int
    financial_grade: str
    financial_risk: str
    financial_strength: str
    financial_score: int
    budget_score: int
    savings_score: int
    emergency_score: int
    goal_score: int
    investment_score: int
    asset_score: int
    liability_score: int
    net_worth_score: int
    wealth_health_score: int


class FinancialHealthInsight(BaseModel):
    status: str
    priority: str
    reason: str
    recommendation: str
    focus_area: str


class FinancialHealth(BaseModel):
    financial_health_summary: FinancialHealthSummary
    financial_health_insights: FinancialHealthInsight

class AvailablePeriod(BaseModel):
    month: int
    year: int


class AvailablePeriodsResponse(BaseModel):
    periods: list[AvailablePeriod]
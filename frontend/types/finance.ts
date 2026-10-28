export interface Summary {
  total_expense: number;
  total_need: number;
  total_want: number;
}

export interface IncomeSummary {
  received_income: number;
  pending_income: number;
}

export interface CommitmentSummary {
  total_borrowed: number;
  total_repaid: number;
  outstanding_debt: number;
  monthly_commitments: number;
  active_commitments: number;
}

export interface FinancialPosition {
  net_position: number;
  cash_position: number;
  expected_position: number;
}

export interface MonthlySummary {
  total_expense: number;
  total_need: number;
  total_want: number;
  projected_expense?: number;
  anomaly_count?: number;
}

export interface MonthlyDistribution {
  need_amount: number;
  want_amount: number;
  need_percentage: number;
  want_percentage: number;
}

export interface SavingsSummary {
  total_income: number;
  total_expense: number;
  total_commitments: number;
  gross_savings: number;
  net_savings: number;
  expense_ratio: number;
  commitment_ratio: number;
  savings_rate: number;
}

export interface HighestSpending {
  category: string;
  amount: number;
}

export interface TopThreeCategories {
  categories: Record<string, number>;
}

export interface FinancialInsight {
  status: string;
  priority: string;
  reason: string;
  metric_value?: number | null;
  threshold?: number | null;
  period?: string | null;
  rule_version?: string | null;
}

export interface FinancialSnapshot {
  monthly_summary: MonthlySummary;
  monthly_distribution: MonthlyDistribution;
  income_summary: IncomeSummary;
  commitment_summary: CommitmentSummary;
  financial_position: FinancialPosition;
  savings_summary: SavingsSummary;
  highest_spending: HighestSpending;
  top_three_categories: TopThreeCategories;
  insights: Record<string, FinancialInsight>;
}

export interface BudgetSummary {
  monthly_budget: number;
  spent: number;
  remaining: number;
  utilization: number;
  status: string;
}

export interface BudgetInsight {
  status: string;
  priority: string;
  reason: string;
  recommendation: string;
}

export interface Budget {
  summary: BudgetSummary;
  insights: BudgetInsight;
}

export interface EmergencyFund {
  current_emergency_fund: number;
  total_monthly_expenses: number;
  total_monthly_commitments: number;
  monthly_survival_cost: number;
  required_3_months_fund: number;
  required_6_months_fund: number;
  required_12_months_fund: number;
  coverage_months: number;
  emergency_fund_gap: number;
}

export interface GoalAnalysis {
  goal: string;
  type: string;
  target_amount: number;
  current_amount: number;
  remaining_amount: number;
  progress_percentage: number;
  target_date: string;
  priority: string;
  status: string;
  months_remaining: number;
  required_monthly_contribution: number;
}

export interface GoalSummary {
  total_goals: number;
  active_goals: number;
  completed_goals: number;
  paused_goals: number;
  cancelled_goals: number;
  completion_rate: number;
  active_goal_rate: number;
  total_target_amount: number;
  total_current_amount: number;
  total_remaining_amount: number;
  overall_progress_percentage: number;
}

export interface GoalInsight {
  goal: string;
  goal_priority: string;
  status: string;
  priority: string;
  reason: string;
  recommendation: string;
}

export interface Goals {
  goal_analysis: GoalAnalysis[];
  goal_summary: GoalSummary;
  goal_insights: GoalInsight[];
}

export interface InvestmentSummary {
  total_invested: number;
  current_value: number;
  total_profit_loss: number;
  return_percentage: number;
  active_investments: number;
  investment_growth: string;
}

export interface InvestmentInsight {
  status: string;
  priority: string;
  reason: string;
  recommendation: string;
}

export interface Investment {
  investment_summary: InvestmentSummary;
  investment_insights: InvestmentInsight;
}

export interface LargestAsset {
  asset: string;
  category: string;
  purchase_value: number;
  current_value: number;
}

export interface AssetSummary {
  total_asset_value: number;
  purchase_value: number;
  asset_profit_loss: number;
  active_assets: number;
  largest_asset: LargestAsset;
  asset_return_percentage: number;
  emergency_fund: number;
}

export interface AssetInsight {
  status: string;
  priority: string;
  reason: string;
  recommendation: string;
}

export interface Assets {
  asset_summary: AssetSummary;
  asset_insights: AssetInsight;
}

export interface HighestLiability {
  liability: string;
  category: string;
  original_loan: number;
  outstanding_balance: number;
  monthly_emi: number;
}

export interface LiabilitySummary {
  total_original_loan: number;
  total_outstanding_balance: number;
  total_repaid: number;
  repayment_percentage: number;
  monthly_liability_payment: number;
  largest_monthly_emi: number;
  active_liabilities: number;
  highest_liability: HighestLiability;
  liability_ratio: number;
  average_liability: number;
  remaining_repayment_percentage: number;
}

export interface LiabilityInsight {
  status: string;
  priority: string;
  reason: string;
  recommendation: string;
}

export interface Liabilities {
  liability_summary: LiabilitySummary;
  liability_insights: LiabilityInsight;
}

export interface NetWorthSummary {
  total_assets: number;
  total_liabilities: number;
  net_worth: number;
  equity: number;
  asset_coverage_ratio: number;
  debt_percentage: number;
  wealth_category: string;
  asset_to_liability_ratio: number;
  financial_leverage: number;
  wealth_growth: number;
  net_assets: number;
  debt_free_percentage: number;
  wealth_score: number;
  wealth_efficiency: number;
}

export interface NetWorthInsight {
  status: string;
  priority: string;
  reason: string;
  recommendation: string;
}

export interface NetWorth {
  net_worth_summary: NetWorthSummary;
  net_worth_insights: NetWorthInsight;
}

export interface WealthHealthSummary {
  wealth_score: number;
  wealth_grade: string;
  wealth_risk: string;
  capital_strength: string;
  emergency_score: number;
  goal_score: number;
  investment_score: number;
  asset_score: number;
  liability_score: number;
  net_worth_score: number;
  growth_readiness: string;
  liquidity_strength: string;
  wealth_momentum: string;
  financial_stability: string;
  long_term_sustainability: string;
}

export interface WealthHealthInsight {
  status: string;
  priority: string;
  reason: string;
  recommendation: string;
}

export interface WealthHealth {
  wealth_health_summary: WealthHealthSummary;
  wealth_health_insights: WealthHealthInsight;
}

export interface FinancialHealthSummary {
  financial_health_score: number;
  financial_grade: string;
  financial_risk: string;
  financial_strength: string;
  financial_score: number;
  budget_score: number;
  savings_score: number;
  emergency_score: number;
  goal_score: number;
  investment_score: number;
  asset_score: number;
  liability_score: number;
  net_worth_score: number;
  wealth_health_score: number;
}

export interface FinancialHealthInsight {
  status: string;
  priority: string;
  reason: string;
  recommendation: string;
  focus_area: string;
}

export interface FinancialHealth {
  financial_health_summary: FinancialHealthSummary;
  financial_health_insights: FinancialHealthInsight;
}

export interface FinanceData {
  summary: Summary;
  income_summary: IncomeSummary;
  commitment_summary: CommitmentSummary;
  financial_position: FinancialPosition;
  financial_snapshot: FinancialSnapshot;
  budget: Budget;
  savings: SavingsSummary;
  emergency_fund: EmergencyFund;
  goals: Goals;
  investment: Investment;
  assets: Assets;
  liabilities: Liabilities;
  net_worth: NetWorth;
  wealth_health: WealthHealth;
  financial_health: FinancialHealth;
}

export interface AvailablePeriod {
  month: number;
  year: number;
}

export interface AvailablePeriodsResponse {
  periods: AvailablePeriod[];
}
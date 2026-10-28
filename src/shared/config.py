class FinanceConfig:
    RULE_VERSION = "v1"
    
    # Minimum transaction history days to provide confident insights
    INSUFFICIENT_DATA_DAYS = 10
    
    # Cash flow tolerance as a percentage of income
    CASH_FLOW_TOLERANCE_PCT = 0.02
    
    # Need/Want thresholds (Percentage of Total Expense)
    NEED_HEALTHY_MAX = 70.0
    NEED_BALANCED_MIN = 50.0
    
    WANT_EXCELLENT_MAX = 30.0
    WANT_BALANCED_MAX = 50.0
    
    # Debt-to-Income (DTI) thresholds (Percentage of Monthly Income)
    DTI_LOW_MAX = 20.0
    DTI_HIGH_MIN = 40.0
    
    # Savings Rate thresholds (Percentage of Income)
    SAVINGS_RATE_GOOD_MIN = 20.0
    SAVINGS_RATE_MODERATE_MIN = 5.0

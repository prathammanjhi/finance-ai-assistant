# Finance AI Changelog

All notable changes to Finance AI will be documented in this file.

---

## v0.4.2

### Added
- Top 3 Spending Categories
- Category ranking using descending sort
- Professional category analytics report

### Learned
- sort_values()
- Python Slicing (`[:3]`)

### Engineering Notes
- Reused existing Category Summary instead of recalculating data.
- Followed layered architecture:
  - Reader → Read data
  - Analyzer → Business Logic
  - Main → Display

---

## v0.4.1

### Added
- Highest Spending Category

### Learned
- idxmax()
- Edge case handling using `.empty`

### Engineering Notes
- Defensive Programming
- Reused Category Summary

---

## v0.4.0

### Added
- Expense by Category Analytics

### Learned
- groupby()
- Pandas Series

### Engineering Notes
- First analytics module built on top of Expense Engine.

---

## v0.3.0

### Added
- Income Engine
- Commitment Engine
- Net Position Engine

### Learned
- Functions returning dictionaries
- Passing data between modules

---

## v0.2.0

### Added
- Expense Summary
- Need Spending
- Want Spending

### Learned
- DataFrame filtering using `loc()`
- `sum()`

---

## v0.1.0

### Added
- Project Setup
- UV Environment
- GitHub Repository
- Reader Module

### Learned
- Python Modules
- Functions
- Layered Architecture

## v0.5.0

### Added
- Expense Distribution Engine
- Need Spending Percentage
- Want Spending Percentage
- Empty expense handling
- Improved expense analytics report

### Learned
- Percentage calculations
- Defensive programming for division by zero
- Data reuse across analyzer functions

### Engineering Notes
- Reused Expense Summary instead of recalculating transactions.
- Kept business logic inside Analyzer.
- Kept presentation logic inside Main.
- Continued following layered architecture:
  - Reader → Read Data
  - Analyzer → Business Logic
  - Main → Display

## v0.6.0

### Added
- Monthly Transaction Filtering
- Monthly Expense Summary
- Flexible date filtering by month and year

### Learned
- pd.to_datetime()
- Pandas Datetime Accessor (.dt)
- Timestamp Objects
- Default Parameters

### Engineering Notes
- Introduced reusable date filtering pipeline.
- Reused existing Expense Engine for monthly analytics.
- Followed Single Source of Truth by deriving month/year from Date.

# v0.7.0

## Added

- Financial Snapshot Engine
- Financial Insights Engine
- Rule-based financial decision system
- Structured insight objects (status, priority, reason)

## Architecture

Reader
↓

Financial Engines
↓

Financial Snapshot
↓

Financial Insights
↓

Main

## Learned

- Nested Dictionaries
- Aggregator Pattern
- Rule Engine
- Decision Trees
- Structured Knowledge Objects

## Engineering Principles

- Aggregator engines never calculate.
- Insights consume snapshots instead of raw engine outputs.
- One engine = One business responsibility.
- Structured outputs over plain text.

## v0.8.0

Added:
- Budget Sheet support
- Budget Reader
- Budget Filter Engine
- Budget Analysis Engine
- Budget Insight Engine
- Budget Health **recommendations**

### Savings Intelligence (v0.9.1)

- Gross Savings Calculation
- Net Savings Calculation
- Savings Rate
- Expense Ratio
- Commitment Ratio

### Financial Intelligence

- Financial Snapshot Engine
- Financial Insights Engine
- Budget Insight Engine

### Filtering

- Current Month
- Month
- Year
- Month + Year

### Architecture

- Modular Engine Architecture
- Separation of Responsibilities
- Snapshot-Based Data Flow
- Future-Proof Design

## [v0.9.2] - Emergency Fund Engine

### Added

- Emergency Fund Engine (`calculate_emergency_fund()`)
- Monthly Survival Cost calculation
- Current Emergency Fund calculation
- 3-month emergency fund requirement
- 6-month emergency fund requirement
- 12-month emergency fund requirement
- Emergency Fund Coverage calculation
- Emergency Fund Gap calculation
- Emergency Fund Summary CLI output
- Monthly Commitment metric
- Active Commitments metric

### Changed

- Updated the Financial Commitments data schema.
- Added `Start Date` to financial commitments.
- Renamed commitment amount field to `Total Amount`.
- Added `Commitment` field.
- Added `Monthly Payment` field.
- Added `End Date` field.
- Commitment Engine now distinguishes total outstanding debt from monthly financial obligations.
- Savings Engine now uses monthly commitments instead of outstanding debt when calculating Net Savings.
- Financial Snapshot now includes Emergency Fund Summary.

### Fixed

- Fixed incorrect use of total outstanding debt as a monthly commitment.
- Fixed Net Savings calculation to subtract monthly commitments instead of total outstanding debt.
- Prevented negative temporary emergency fund balances.
- Prevented division-by-zero errors in Emergency Fund Coverage calculation.
- Prevented negative Emergency Fund Gap values.

### Engineering Improvements

- Evolved the Financial Commitments schema to support monthly obligation tracking.
- Improved semantic separation between total liabilities and monthly commitments.
- Added direct engine-to-engine data flow between the Commitment, Savings, and Emergency Fund engines.
- Maintained calculation-only responsibility inside the Emergency Fund Engine.
- Designed Emergency Fund Engine for future migration from Net Savings to Liquid Assets or a dedicated Emergency Fund Balance.

### Known Limitations

- Current Emergency Fund Balance is temporarily derived from Net Savings.
- Monthly Survival Cost currently uses the Expense Summary total as its expense baseline.
- Future versions will use liquid assets or a dedicated emergency fund balance.
- Future versions should use a normalized monthly essential expense baseline for emergency survival calculations.

### Future

Next Version:

- Goal Engine (v0.9.3)
# v0.9.3

## Added

### Goal Reader
- Added Financial Goals sheet reader
- Integrated Goal data into Finance AI pipeline

### Goal Calculation Engine
- Goal Progress Calculation
- Remaining Amount Calculation
- Months Remaining Calculation
- Required Monthly Contribution Calculation

### Goal Portfolio Summary
- Total Goals
- Active Goals
- Completed Goals
- Paused Goals
- Cancelled Goals
- Completion Rate
- Active Goal Rate
- Total Target Amount
- Total Current Amount
- Total Remaining Amount
- Overall Progress Percentage

### Goal Snapshot Engine
- Added generate_goal_snapshot()
- Unified Goal Analysis and Goal Summary into a single structured object

## Improvements
- Added defensive calculations for division-by-zero
- Improved calculation consistency using shared variables
- Rounded portfolio progress output
- Extended Goal Engine architecture for future Insight and Recommendation layers

## Internal
- Goal module now follows the standard PrathamOS Engine Architecture:
  Reader → Calculation → Decision → Insight

# v0.9.4

## Added

### Goal Intelligence

- Added Goal Insight Engine
- Added goal interpretation layer
- Added recommendation generation for every financial goal

### Goal Insight Rules

The engine now evaluates every goal based on:

- Progress Percentage
- Months Remaining
- Goal Priority
- Goal Status

and generates:

- Insight Status
- Insight Priority
- Reason
- Recommendation

### Goal Snapshot

Goal Snapshot now includes:

- Goal Analysis
- Goal Portfolio Summary
- Goal Insights

## Improvements

- Separated Goal Priority from Insight Priority
- Improved Goal Snapshot architecture
- Established reusable Insight Engine pattern for future modules

## Internal

Finance AI now supports:

Reader
→ Calculation
→ Snapshot
→ Insight

for the complete Goal module.
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
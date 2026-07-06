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
"use client";

import { useEffect, useState } from "react";

import Greeting from "@/components/home/greeting";
import { LoadingState } from "@/components/ui/LoadingState";
import { ErrorState } from "@/components/ui/ErrorState";

import AIInsightCard from "./components/AIInsightCard";
import FinancialSnapshot from "./components/FinancialSnapshot";
import OpportunityCard from "./components/OpportunityCard";
import BudgetSummary from "./components/BudgetSummary";
import GoalsSummary from "./components/GoalsSummary";

import {
  getAvailablePeriods,
  getFinance,
} from "@/lib/api";

import { formatCurrency } from "@/lib/formatters/currency";
import type {
  FinanceData,
  AvailablePeriod,
} from "@/types/finance";

export default function HomeScreen() {
  const [finance, setFinance] = useState<FinanceData | null>(null);
  const [periods, setPeriods] = useState<AvailablePeriod[]>([]);
  const [selectedPeriod, setSelectedPeriod] =
    useState<AvailablePeriod | null>(null);

  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);

  // Load available financial periods
  useEffect(() => {
    async function loadPeriods() {
      try {
        setLoading(true);
        setError(null);

        const availablePeriods = await getAvailablePeriods();

        setPeriods(availablePeriods);

        if (availablePeriods.length > 0) {
          setSelectedPeriod(
            availablePeriods[availablePeriods.length - 1]
          );
        }
      } catch (err) {
        setError(
          err instanceof Error
            ? err.message
            : "Unable to load financial periods."
        );
      } finally {
        setLoading(false);
      }
    }

    loadPeriods();
  }, []);

  // Load finance data for selected period
  useEffect(() => {
    if (!selectedPeriod) return;

    const period = selectedPeriod;

    async function loadFinance() {
      try {
        setLoading(true);
        setError(null);

        const data = await getFinance(
          period.month,
          period.year
        );

        setFinance(data);
      } catch (err) {
        setError(
          err instanceof Error
            ? err.message
            : "Unable to load financial data."
        );
      } finally {
        setLoading(false);
      }
    }

    loadFinance();
  }, [selectedPeriod]);

  if (loading && !finance) {
    return <LoadingState />;
  }

  if (error && !finance) {
    return <ErrorState message={error} />;
  }

  if (!finance || !selectedPeriod) {
    return null;
  }

  const snapshot = finance.financial_snapshot;

  /*
   * Finance Core already decides the insight.
   * Frontend only displays it.
   */
  const insights = Object.values(snapshot.insights);

  const primaryInsight = insights[0];

  return (
    <div className="space-y-8">
      <Greeting />

      {/* Period selector */}
      {periods.length > 1 && (
        <div className="flex justify-end">
          <select
            value={
              selectedPeriod
                ? `${selectedPeriod.month}-${selectedPeriod.year}`
                : ""
            }
            onChange={(event) => {
              const [month, year] = event.target.value
                .split("-")
                .map(Number);

              const period = periods.find(
                (item) =>
                  item.month === month &&
                  item.year === year
              );

              if (period) {
                setSelectedPeriod(period);
              }
            }}
            className="rounded-xl border border-white/[0.08] bg-white/[0.04] px-3 py-2 text-sm text-[#e1e2e8] outline-none"
          >
            {periods.map((period) => (
              <option
                key={`${period.month}-${period.year}`}
                value={`${period.month}-${period.year}`}
                className="bg-[#0b0d12]"
              >
                {period.month}/{period.year}
              </option>
            ))}
          </select>
        </div>
      )}

      {/* =========================================================
          1. FINANCIAL INTELLIGENCE
         ========================================================= */}

      <section>
        <div className="mb-3">
          <h2 className="text-sm font-medium text-[#e1e2e8]">
            Financial Intelligence
          </h2>
        </div>

        {primaryInsight && (
          <AIInsightCard
            priority={primaryInsight.priority}
            title={primaryInsight.reason}
            reason={primaryInsight.reason}
            recommendation={
              finance.budget.insights.recommendation
            }
          />
        )}
      </section>

      {/* =========================================================
          2. FINANCIAL SNAPSHOT
         ========================================================= */}

      <FinancialSnapshot
        netPosition={formatCurrency(
          snapshot.financial_position.net_position
        )}
        cashPosition={formatCurrency(
          snapshot.financial_position.cash_position
        )}
        financialHealth={
          finance.financial_health
            .financial_health_summary
            .financial_health_score
        }
      />

      {/* =========================================================
          3. TODAY'S OPPORTUNITY
         ========================================================= */}

      <OpportunityCard
        title={
          finance.budget.insights.recommendation
        }
        description={
          finance.budget.insights.reason
        }
        impact={
          finance.budget.insights.status
        }
      />

      {/* =========================================================
          4. BUDGET
         ========================================================= */}

      <BudgetSummary
        monthlyBudget={
          finance.budget.summary.monthly_budget
        }
        spent={finance.budget.summary.spent}
        remaining={finance.budget.summary.remaining}
        utilization={
          finance.budget.summary.utilization
        }
        status={finance.budget.summary.status}
      />

      {/* =========================================================
          5. GOALS
         ========================================================= */}

      <GoalsSummary
        activeGoals={
          finance.goals.goal_summary.active_goals
        }
        completedGoals={
          finance.goals.goal_summary.completed_goals
        }
        totalTargetAmount={
          finance.goals.goal_summary.total_target_amount
        }
        totalCurrentAmount={
          finance.goals.goal_summary.total_current_amount
        }
        progressPercentage={
          finance.goals.goal_summary
            .overall_progress_percentage
        }
      />

      {error && (
        <p className="text-sm text-amber-400">
          {error}
        </p>
      )}
    </div>
  );
} 
"use client";

import { useEffect, useState } from "react";
import { getAvailablePeriods, getFinance } from "@/lib/api";
import { LoadingState } from "@/components/ui/LoadingState";
import { ErrorState } from "@/components/ui/ErrorState";
import { formatCurrency } from "@/lib/formatters/currency";
import type { AvailablePeriod, FinanceData } from "@/types/finance";

const statusColor = (s: string) => {
  if (s === "ON_TRACK" || s === "COMPLETED") return "bg-[#4ade80]/10 text-[#4ade80]";
  if (s === "BEHIND") return "bg-[#ffca7b]/10 text-[#ffca7b]";
  if (s === "PAUSED" || s === "CANCELLED") return "bg-white/[0.06] text-[#8b919b]";
  return "bg-white/[0.06] text-[#8b919b]";
};

const priorityColor = (p: string) => {
  if (p === "HIGH") return "bg-[#ffb4ab]/10 text-[#ffb4ab]";
  if (p === "MEDIUM") return "bg-[#ffca7b]/10 text-[#ffca7b]";
  return "bg-white/[0.06] text-[#8b919b]";
};

const insightIcon = (priority: string) => {
  if (priority === "HIGH") return { icon: "warning", bg: "bg-[#ffb4ab]/10", color: "text-[#ffb4ab]" };
  if (priority === "MEDIUM") return { icon: "info", bg: "bg-[#ffca7b]/10", color: "text-[#ffca7b]" };
  return { icon: "lightbulb", bg: "bg-[#7abcff]/10", color: "text-[#7abcff]" };
};

export default function GoalsScreen() {
  const [finance, setFinance] = useState<FinanceData | null>(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    async function load() {
      try {
        setLoading(true);
        const periods: AvailablePeriod[] = await getAvailablePeriods();
        if (!periods || periods.length === 0) throw new Error("No periods available.");
        const latest = periods[periods.length - 1];
        const data = await getFinance(latest.year, latest.month);
        setFinance(data);
      } catch (err: unknown) {
        setError(err instanceof Error ? err.message : "Failed to load goals data.");
      } finally {
        setLoading(false);
      }
    }
    load();
  }, []);

  if (loading) return <LoadingState />;
  if (error || !finance) return <ErrorState message={error ?? "No data available."} />;

  const summary = finance.goals?.goal_summary;
  const analyses = finance.goals?.goal_analysis ?? [];
  const insights = finance.goals?.goal_insights ?? [];

  return (
    <div className="min-h-screen bg-[#0b0d12] px-6 py-10">
      <div className="mx-auto max-w-5xl space-y-8">

        {/* Page Header */}
        <div>
          <p className="text-xs font-medium uppercase tracking-[0.14em] text-[#8b919b]">Financial Goals</p>
          <h1 className="mt-2 text-3xl font-medium tracking-[-0.03em] text-[#e1e2e8]">Goals</h1>
          <p className="mt-2 text-sm text-[#8b919b]">Monitor progress toward your financial milestones.</p>
        </div>

        {/* Summary Chips — 4 cols */}
        {summary && (
          <div className="grid grid-cols-2 gap-4 md:grid-cols-4">
            <div className="rounded-[18px] border border-white/[0.07] bg-[#101419] p-5">
              <p className="text-[11px] font-medium uppercase tracking-[0.12em] text-[#8b919b]">Total Goals</p>
              <p className="mt-3 text-3xl font-medium tracking-[-0.03em] text-[#e1e2e8]">{summary.total_goals}</p>
            </div>
            <div className="rounded-[18px] border border-white/[0.07] bg-[#101419] p-5">
              <p className="text-[11px] font-medium uppercase tracking-[0.12em] text-[#8b919b]">Active</p>
              <p className="mt-3 text-3xl font-medium tracking-[-0.03em] text-[#7abcff]">{summary.active_goals}</p>
            </div>
            <div className="rounded-[18px] border border-white/[0.07] bg-[#101419] p-5">
              <p className="text-[11px] font-medium uppercase tracking-[0.12em] text-[#8b919b]">Completed</p>
              <p className="mt-3 text-3xl font-medium tracking-[-0.03em] text-[#4ade80]">{summary.completed_goals}</p>
            </div>
            <div className="rounded-[18px] border border-white/[0.07] bg-[#101419] p-5">
              <p className="text-[11px] font-medium uppercase tracking-[0.12em] text-[#8b919b]">Overall Progress</p>
              <p className="mt-3 text-3xl font-medium tracking-[-0.03em] text-[#e1e2e8]">
                {summary.overall_progress_percentage ?? 0}%
              </p>
            </div>
          </div>
        )}

        {/* Goal Cards */}
        {analyses.length > 0 && (
          <div className="space-y-4">
            {analyses.map((goal, idx) => (
              <div
                key={idx}
                className="rounded-[20px] border border-white/[0.08] bg-[#101419] p-6 shadow-[0_4px_20px_rgba(0,0,0,0.12)]"
              >
                {/* Header Row */}
                <div className="flex items-start justify-between gap-4">
                  <p className="text-[15px] font-medium text-[#e1e2e8]">{goal.goal}</p>
                  <span className={`shrink-0 rounded-full px-3 py-1 text-xs font-medium ${statusColor(goal.status)}`}>
                    {goal.status}
                  </span>
                </div>

                {/* Progress Bar */}
                <div className="mt-4 h-1.5 rounded-full bg-white/[0.08]">
                  <div
                    className="h-full rounded-full bg-[#7abcff]"
                    style={{ width: `${Math.min(goal.progress_percentage, 100)}%` }}
                  />
                </div>
                <p className="mt-1 text-right text-xs text-[#8b919b]">{goal.progress_percentage}%</p>

                {/* Current / Target */}
                <div className="mt-4 grid grid-cols-2 gap-4">
                  <div className="rounded-[14px] bg-white/[0.035] p-4">
                    <p className="text-[11px] font-medium uppercase tracking-[0.12em] text-[#8b919b]">Current Amount</p>
                    <p className="mt-2 text-xl font-medium tracking-[-0.02em] text-[#e1e2e8]">
                      {formatCurrency(goal.current_amount)}
                    </p>
                  </div>
                  <div className="rounded-[14px] bg-white/[0.035] p-4">
                    <p className="text-[11px] font-medium uppercase tracking-[0.12em] text-[#8b919b]">Target Amount</p>
                    <p className="mt-2 text-xl font-medium tracking-[-0.02em] text-[#e1e2e8]">
                      {formatCurrency(goal.target_amount)}
                    </p>
                  </div>
                </div>

                {/* Footer */}
                <div className="mt-4 flex flex-wrap items-center justify-between gap-3">
                  <div className="flex flex-wrap gap-4">
                    <div>
                      <p className="text-[11px] font-medium uppercase tracking-[0.12em] text-[#8b919b]">Required / Month</p>
                      <p className="mt-1 text-sm font-medium text-[#7abcff]">
                        {formatCurrency(goal.required_monthly_contribution)}
                      </p>
                    </div>
                    <div>
                      <p className="text-[11px] font-medium uppercase tracking-[0.12em] text-[#8b919b]">Months Remaining</p>
                      <p className="mt-1 text-sm font-medium text-[#e1e2e8]">{goal.months_remaining}</p>
                    </div>
                  </div>
                  <span className={`rounded-full px-3 py-1 text-xs font-medium ${priorityColor(goal.priority)}`}>
                    {goal.priority}
                  </span>
                </div>
              </div>
            ))}
          </div>
        )}

        {/* Goal Insights */}
        {insights.length > 0 && (
          <div className="space-y-4">
            <p className="text-[11px] font-medium uppercase tracking-[0.12em] text-[#8b919b]">Goal Insights</p>
            {insights.map((insight, idx) => {
              const { icon, bg, color } = insightIcon(insight.priority);
              return (
                <div key={idx} className="rounded-[20px] border border-white/[0.08] bg-[#101419] p-6">
                  <div className="flex items-start gap-4">
                    <div className={`flex h-10 w-10 shrink-0 items-center justify-center rounded-full ${bg}`}>
                      <span className={`material-symbols-outlined text-[18px] ${color}`}>{icon}</span>
                    </div>
                    <div>
                      <p className="text-[11px] font-medium uppercase tracking-[0.12em] text-[#8b919b]">
                        {insight.priority} Priority · {insight.goal}
                      </p>
                      <p className="mt-1 text-[15px] font-medium text-[#e1e2e8]">{insight.status}</p>
                      <p className="mt-1 text-sm leading-6 text-[#8b919b]">{insight.reason}</p>
                      {insight.recommendation && (
                        <p className="mt-2 text-sm text-[#7abcff]">{insight.recommendation}</p>
                      )}
                    </div>
                  </div>
                </div>
              );
            })}
          </div>
        )}
      </div>
    </div>
  );
}

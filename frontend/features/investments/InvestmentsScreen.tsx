"use client";

import { useEffect, useState } from "react";
import { getAvailablePeriods, getFinance } from "@/lib/api";
import { LoadingState } from "@/components/ui/LoadingState";
import { ErrorState } from "@/components/ui/ErrorState";
import { formatCurrency } from "@/lib/formatters/currency";
import type { AvailablePeriod, FinanceData } from "@/types/finance";

interface InvestmentSummary {
  total_invested: number;
  current_value: number;
  total_profit_loss: number;
  return_percentage: number;
  active_investments: number;
  investment_growth: string;
}

interface InvestmentInsight {
  status: string;
  priority: string;
  reason: string;
  recommendation: string;
}

function growthPillColor(growth: string): string {
  switch (growth?.toUpperCase()) {
    case "GROWING":
      return "bg-[#4ade80]/10 text-[#4ade80] border border-[#4ade80]/20";
    case "DECLINING":
      return "bg-[#ffb4ab]/10 text-[#ffb4ab] border border-[#ffb4ab]/20";
    default:
      return "bg-[#8b919b]/10 text-[#8b919b] border border-[#8b919b]/20";
  }
}

function priorityIconBg(priority: string): string {
  switch (priority?.toUpperCase()) {
    case "HIGH":
      return "bg-[#ffb4ab]/10 text-[#ffb4ab]";
    case "MEDIUM":
      return "bg-[#ffca7b]/10 text-[#ffca7b]";
    default:
      return "bg-[#4ade80]/10 text-[#4ade80]";
  }
}

function priorityIcon(priority: string): string {
  switch (priority?.toUpperCase()) {
    case "HIGH":
      return "warning";
    case "MEDIUM":
      return "info";
    default:
      return "check_circle";
  }
}

export default function InvestmentsScreen() {
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);
  const [summary, setSummary] = useState<InvestmentSummary | null>(null);
  const [insight, setInsight] = useState<InvestmentInsight | null>(null);

  useEffect(() => {
    async function load() {
      try {
        setLoading(true);
        const periods: AvailablePeriod[] = await getAvailablePeriods();
        if (!periods.length) throw new Error("No periods available.");
        const latest = periods[periods.length - 1];
        const finance: FinanceData = await getFinance(latest.month, latest.year);
        setSummary(finance.investment.investment_summary as InvestmentSummary);
        const insights = finance.investment.investment_insights as InvestmentInsight[];
        setInsight(insights?.[0] ?? null);
      } catch (e: unknown) {
        setError(e instanceof Error ? e.message : "Failed to load investment data.");
      } finally {
        setLoading(false);
      }
    }
    load();
  }, []);

  if (loading) return <LoadingState />;
  if (error || !summary) return <ErrorState message={error ?? "No data available."} />;

  const returnPositive = summary.return_percentage > 0;
  const returnNegative = summary.return_percentage < 0;
  const plPositive = summary.total_profit_loss > 0;

  return (
    <div className="space-y-6">
      {/* Page Header */}
      <div>
        <p className="text-xs font-medium uppercase tracking-[0.14em] text-[#8b919b]">Portfolio</p>
        <h1 className="mt-2 text-3xl font-medium tracking-[-0.03em] text-[#e1e2e8]">Investments</h1>
        <p className="mt-2 text-sm text-[#8b919b]">Track your portfolio performance and returns.</p>
      </div>

      {/* Hero Card */}
      <div className="rounded-[20px] border border-white/[0.08] bg-[#101419] p-6 shadow-[0_4px_20px_rgba(0,0,0,0.12)]">
        <div className="flex flex-wrap items-start justify-between gap-4">
          <div>
            <p className="text-[11px] font-medium uppercase tracking-[0.12em] text-[#8b919b]">Current Portfolio Value</p>
            <p className="mt-2 text-3xl font-medium tracking-[-0.03em] text-[#e1e2e8]">
              {formatCurrency(summary.current_value)}
            </p>
            <p
              className={`mt-2 text-sm font-medium ${
                returnPositive ? "text-[#4ade80]" : returnNegative ? "text-[#ffb4ab]" : "text-[#8b919b]"
              }`}
            >
              {returnPositive
                ? `+${summary.return_percentage.toFixed(2)}%`
                : `${summary.return_percentage.toFixed(2)}%`}
              &nbsp;overall return
            </p>
          </div>
          <span
            className={`rounded-full px-3 py-1 text-xs font-medium ${growthPillColor(summary.investment_growth)}`}
          >
            {summary.investment_growth}
          </span>
        </div>
      </div>

      {/* 3-col Stat Chips */}
      <div className="grid grid-cols-1 gap-4 sm:grid-cols-3">
        {/* Total Invested */}
        <div className="rounded-[18px] border border-white/[0.07] bg-[#101419] p-5">
          <p className="text-[11px] font-medium uppercase tracking-[0.12em] text-[#8b919b]">Total Invested</p>
          <p className="mt-2 text-2xl font-medium tracking-[-0.03em] text-[#e1e2e8]">
            {formatCurrency(summary.total_invested)}
          </p>
        </div>

        {/* Total P&L */}
        <div className="rounded-[18px] border border-white/[0.07] bg-[#101419] p-5">
          <p className="text-[11px] font-medium uppercase tracking-[0.12em] text-[#8b919b]">Total P&amp;L</p>
          <p
            className={`mt-2 text-2xl font-medium tracking-[-0.03em] ${
              plPositive ? "text-[#4ade80]" : summary.total_profit_loss < 0 ? "text-[#ffb4ab]" : "text-[#e1e2e8]"
            }`}
          >
            {formatCurrency(summary.total_profit_loss)}
          </p>
        </div>

        {/* Active Investments */}
        <div className="rounded-[18px] border border-white/[0.07] bg-[#101419] p-5">
          <p className="text-[11px] font-medium uppercase tracking-[0.12em] text-[#8b919b]">Active Investments</p>
          <p className="mt-2 text-2xl font-medium tracking-[-0.03em] text-[#e1e2e8]">
            {summary.active_investments}
          </p>
        </div>
      </div>

      {/* Sub-Breakdown Card */}
      <div className="rounded-[20px] border border-white/[0.08] bg-[#101419] p-6 shadow-[0_4px_20px_rgba(0,0,0,0.12)]">
        <p className="text-[11px] font-medium uppercase tracking-[0.12em] text-[#8b919b]">Portfolio Breakdown</p>
        <div className="mt-4 grid grid-cols-1 gap-4 sm:grid-cols-2">
          <div className="rounded-[14px] bg-white/[0.035] p-4">
            <p className="text-xs text-[#8b919b]">Amount Invested</p>
            <p className="mt-2 text-xl font-medium tracking-[-0.02em] text-[#e1e2e8]">
              {formatCurrency(summary.total_invested)}
            </p>
          </div>
          <div className="rounded-[14px] bg-white/[0.035] p-4">
            <p className="text-xs text-[#8b919b]">Current Value</p>
            <p className="mt-2 text-xl font-medium tracking-[-0.02em] text-[#e1e2e8]">
              {formatCurrency(summary.current_value)}
            </p>
          </div>
        </div>
      </div>

      {/* Insight Card */}
      {insight && (
        <div className="rounded-[20px] border border-white/[0.08] bg-[#101419] p-6">
          <div className="flex items-start gap-4">
            <div
              className={`flex h-10 w-10 shrink-0 items-center justify-center rounded-full ${priorityIconBg(insight.priority)}`}
            >
              <span className="material-symbols-outlined text-[18px]">{priorityIcon(insight.priority)}</span>
            </div>
            <div>
              <p className="text-[11px] font-medium uppercase tracking-[0.12em] text-[#8b919b]">
                {insight.priority} Priority
              </p>
              <p className="mt-1 text-[15px] font-medium text-[#e1e2e8]">{insight.status}</p>
              <p className="mt-1 text-sm leading-6 text-[#8b919b]">{insight.reason}</p>
              {insight.recommendation && (
                <p className="mt-2 text-sm text-[#7abcff]">{insight.recommendation}</p>
              )}
            </div>
          </div>
        </div>
      )}
    </div>
  );
}

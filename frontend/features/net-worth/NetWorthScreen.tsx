"use client";

import { useEffect, useState } from "react";
import { getAvailablePeriods, getFinance } from "@/lib/api";
import { LoadingState } from "@/components/ui/LoadingState";
import { ErrorState } from "@/components/ui/ErrorState";
import { formatCurrency } from "@/lib/formatters/currency";
import type { AvailablePeriod, FinanceData } from "@/types/finance";

interface NetWorthSummary {
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

interface NetWorthInsight {
  status: string;
  priority: string;
  reason: string;
  recommendation: string;
}

function insightIconBg(priority: string): string {
  switch (priority?.toLowerCase()) {
    case "high":
      return "bg-[#ffb4ab]/10";
    case "medium":
      return "bg-[#ffca7b]/10";
    default:
      return "bg-[#4ade80]/10";
  }
}

function insightIconColor(priority: string): string {
  switch (priority?.toLowerCase()) {
    case "high":
      return "text-[#ffb4ab]";
    case "medium":
      return "text-[#ffca7b]";
    default:
      return "text-[#4ade80]";
  }
}

function insightIcon(priority: string): string {
  switch (priority?.toLowerCase()) {
    case "high":
      return "warning";
    case "medium":
      return "info";
    default:
      return "check_circle";
  }
}

export default function NetWorthScreen() {
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);
  const [summary, setSummary] = useState<NetWorthSummary | null>(null);
  const [insights, setInsights] = useState<NetWorthInsight[]>([]);

  useEffect(() => {
    async function load() {
      try {
        const periods: AvailablePeriod[] = await getAvailablePeriods();
        if (!periods.length) throw new Error("No periods available.");
        const latest = periods[periods.length - 1];
        const finance: FinanceData = await getFinance(latest.month, latest.year);
        setSummary(finance.net_worth.net_worth_summary as NetWorthSummary);
        setInsights(finance.net_worth.net_worth_insights as NetWorthInsight[]);
      } catch (e: unknown) {
        setError(e instanceof Error ? e.message : "Failed to load data.");
      } finally {
        setLoading(false);
      }
    }
    load();
  }, []);

  if (loading) return <LoadingState />;
  if (error || !summary) return <ErrorState message={error ?? "No data available."} />;

  const netWorthColor = summary.net_worth >= 0 ? "text-[#4ade80]" : "text-[#ffb4ab]";

  return (
    <div className="min-h-screen bg-[#0b0d12] p-6 md:p-8">
      <div className="mx-auto max-w-5xl space-y-6">
        {/* Page Header */}
        <div>
          <p className="text-xs font-medium uppercase tracking-[0.14em] text-[#8b919b]">
            Wealth Overview
          </p>
          <h1 className="mt-2 text-3xl font-medium tracking-[-0.03em] text-[#e1e2e8]">
            Net Worth
          </h1>
          <p className="mt-2 text-sm text-[#8b919b]">
            Your total financial position — assets minus liabilities.
          </p>
        </div>

        {/* Hero Card */}
        <div
          className="rounded-[20px] p-8 text-center"
          style={{
            background:
              "linear-gradient(135deg, rgba(122,188,255,0.08) 0%, rgba(16,20,24,0.95) 100%)",
            border: "1px solid rgba(122,188,255,0.15)",
          }}
        >
          <p className="text-[11px] font-medium uppercase tracking-[0.12em] text-[#8b919b]">
            Total Net Worth
          </p>
          <p className={`mt-4 text-5xl font-bold tracking-[-0.03em] ${netWorthColor}`}>
            {formatCurrency(summary.net_worth)}
          </p>
          <div className="mt-4 flex items-center justify-center">
            <span className="rounded-full bg-[#7abcff]/10 px-4 py-1.5 text-sm font-medium text-[#7abcff]">
              {summary.wealth_category}
            </span>
          </div>
        </div>

        {/* Assets vs Liabilities 2-col */}
        <div className="grid grid-cols-1 gap-4 md:grid-cols-2">
          <div className="rounded-[20px] border border-white/[0.08] bg-[#101419] p-6 shadow-[0_4px_20px_rgba(0,0,0,0.12)]">
            <p className="text-[11px] font-medium uppercase tracking-[0.12em] text-[#8b919b]">
              Total Assets
            </p>
            <p className="mt-3 text-3xl font-medium tracking-[-0.03em] text-[#4ade80]">
              {formatCurrency(summary.total_assets)}
            </p>
          </div>
          <div className="rounded-[20px] border border-white/[0.08] bg-[#101419] p-6 shadow-[0_4px_20px_rgba(0,0,0,0.12)]">
            <p className="text-[11px] font-medium uppercase tracking-[0.12em] text-[#8b919b]">
              Total Liabilities
            </p>
            <p className="mt-3 text-3xl font-medium tracking-[-0.03em] text-[#ffb4ab]">
              {formatCurrency(summary.total_liabilities)}
            </p>
          </div>
        </div>

        {/* Stat Chips Row */}
        <div className="grid grid-cols-2 gap-4 md:grid-cols-4">
          <div className="rounded-[18px] border border-white/[0.07] bg-[#101419] p-5">
            <p className="text-[11px] font-medium uppercase tracking-[0.12em] text-[#8b919b]">
              Equity
            </p>
            <p className="mt-2 text-xl font-semibold text-[#e1e2e8]">
              {formatCurrency(summary.equity)}
            </p>
          </div>
          <div className="rounded-[18px] border border-white/[0.07] bg-[#101419] p-5">
            <p className="text-[11px] font-medium uppercase tracking-[0.12em] text-[#8b919b]">
              Asset Coverage
            </p>
            <p className="mt-2 text-xl font-semibold text-[#e1e2e8]">
              {summary.asset_coverage_ratio.toFixed(2)}x
            </p>
          </div>
          <div className="rounded-[18px] border border-white/[0.07] bg-[#101419] p-5">
            <p className="text-[11px] font-medium uppercase tracking-[0.12em] text-[#8b919b]">
              Debt %
            </p>
            <p className="mt-2 text-xl font-semibold text-[#e1e2e8]">
              {summary.debt_percentage.toFixed(1)}%
            </p>
          </div>
          <div className="rounded-[18px] border border-white/[0.07] bg-[#101419] p-5">
            <p className="text-[11px] font-medium uppercase tracking-[0.12em] text-[#8b919b]">
              Debt-Free %
            </p>
            <p className="mt-2 text-xl font-semibold text-[#e1e2e8]">
              {summary.debt_free_percentage.toFixed(1)}%
            </p>
          </div>
        </div>

        {/* Additional Metrics Card */}
        <div className="rounded-[20px] border border-white/[0.08] bg-[#101419] p-6 shadow-[0_4px_20px_rgba(0,0,0,0.12)]">
          <p className="text-[11px] font-medium uppercase tracking-[0.12em] text-[#8b919b]">
            Additional Metrics
          </p>
          <div className="mt-4 grid grid-cols-1 gap-4 md:grid-cols-3">
            <div className="rounded-[14px] bg-white/[0.035] p-4">
              <p className="text-[11px] font-medium uppercase tracking-[0.12em] text-[#8b919b]">
                Asset-to-Liability Ratio
              </p>
              <p className="mt-2 text-2xl font-semibold text-[#e1e2e8]">
                {summary.asset_to_liability_ratio.toFixed(2)}x
              </p>
            </div>
            <div className="rounded-[14px] bg-white/[0.035] p-4">
              <p className="text-[11px] font-medium uppercase tracking-[0.12em] text-[#8b919b]">
                Wealth Score
              </p>
              <p className="mt-2 text-2xl font-semibold text-[#e1e2e8]">
                {summary.wealth_score.toFixed(2)}
              </p>
            </div>
            <div className="rounded-[14px] bg-white/[0.035] p-4">
              <p className="text-[11px] font-medium uppercase tracking-[0.12em] text-[#8b919b]">
                Wealth Efficiency
              </p>
              <p className="mt-2 text-2xl font-semibold text-[#e1e2e8]">
                {summary.wealth_efficiency.toFixed(2)}
              </p>
            </div>
          </div>
        </div>

        {/* Insight Cards */}
        {insights.length > 0 && (
          <div className="space-y-3">
            <p className="text-[11px] font-medium uppercase tracking-[0.12em] text-[#8b919b]">
              Net Worth Insights
            </p>
            {insights.map((insight, i) => (
              <div
                key={i}
                className="rounded-[20px] border border-white/[0.08] bg-[#101419] p-6"
              >
                <div className="flex items-start gap-4">
                  <div
                    className={`flex h-10 w-10 shrink-0 items-center justify-center rounded-full ${insightIconBg(insight.priority)}`}
                  >
                    <span
                      className={`material-symbols-outlined text-[18px] ${insightIconColor(insight.priority)}`}
                    >
                      {insightIcon(insight.priority)}
                    </span>
                  </div>
                  <div>
                    <p className="text-[11px] font-medium uppercase tracking-[0.12em] text-[#8b919b]">
                      {insight.priority} Priority
                    </p>
                    <p className="mt-1 text-[15px] font-medium text-[#e1e2e8]">
                      {insight.status}
                    </p>
                    <p className="mt-1 text-sm leading-6 text-[#8b919b]">
                      {insight.reason}
                    </p>
                    {insight.recommendation && (
                      <p className="mt-2 text-sm text-[#7abcff]">
                        {insight.recommendation}
                      </p>
                    )}
                  </div>
                </div>
              </div>
            ))}
          </div>
        )}
      </div>
    </div>
  );
}

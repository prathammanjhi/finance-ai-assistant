"use client";

import { useEffect, useState } from "react";
import { getAvailablePeriods, getFinance } from "@/lib/api";
import { LoadingState } from "@/components/ui/LoadingState";
import { ErrorState } from "@/components/ui/ErrorState";
import { formatCurrency } from "@/lib/formatters/currency";
import type { AvailablePeriod, FinanceData } from "@/types/finance";

interface HighestLiability {
  liability: string;
  category: string;
  original_loan: number;
  outstanding_balance: number;
  monthly_emi: number;
}

interface LiabilitySummary {
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

interface LiabilityInsight {
  status: string;
  priority: string;
  reason: string;
  recommendation: string;
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

export default function LiabilitiesScreen() {
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);
  const [summary, setSummary] = useState<LiabilitySummary | null>(null);
  const [insight, setInsight] = useState<LiabilityInsight | null>(null);

  useEffect(() => {
    async function load() {
      try {
        setLoading(true);
        const periods: AvailablePeriod[] = await getAvailablePeriods();
        if (!periods.length) throw new Error("No periods available.");
        const latest = periods[periods.length - 1];
        const finance: FinanceData = await getFinance(latest.month, latest.year);
        setSummary(finance.liabilities.liability_summary as LiabilitySummary);
        const insights = finance.liabilities.liability_insights as LiabilityInsight[];
        setInsight(insights?.[0] ?? null);
      } catch (e: unknown) {
        setError(e instanceof Error ? e.message : "Failed to load liabilities data.");
      } finally {
        setLoading(false);
      }
    }
    load();
  }, []);

  if (loading) return <LoadingState />;
  if (error || !summary) return <ErrorState message={error ?? "No data available."} />;

  const { highest_liability: hl } = summary;

  return (
    <div className="space-y-6">
      {/* Page Header */}
      <div>
        <p className="text-xs font-medium uppercase tracking-[0.14em] text-[#8b919b]">Debt Management</p>
        <h1 className="mt-2 text-3xl font-medium tracking-[-0.03em] text-[#e1e2e8]">Liabilities</h1>
        <p className="mt-2 text-sm text-[#8b919b]">
          Understand your outstanding obligations and repayment progress.
        </p>
      </div>

      {/* Hero Card */}
      <div className="rounded-[20px] border border-white/[0.08] bg-[#101419] p-6 shadow-[0_4px_20px_rgba(0,0,0,0.12)]">
        <p className="text-[11px] font-medium uppercase tracking-[0.12em] text-[#8b919b]">Total Outstanding Balance</p>
        <p className="mt-2 text-3xl font-medium tracking-[-0.03em] text-[#e1e2e8]">
          {formatCurrency(summary.total_outstanding_balance)}
        </p>
        {/* Repayment Progress Bar */}
        <div className="mt-4">
          <div className="flex items-center justify-between mb-2">
            <p className="text-xs text-[#8b919b]">Repayment Progress</p>
            <p className="text-xs font-medium text-[#4ade80]">
              {summary.repayment_percentage.toFixed(1)}% repaid
            </p>
          </div>
          <div className="h-2 w-full rounded-full bg-white/[0.06]">
            <div
              className="h-2 rounded-full bg-[#4ade80] transition-all duration-500"
              style={{ width: `${summary.repayment_percentage}%` }}
            />
          </div>
        </div>
      </div>

      {/* 3-col Stat Chips */}
      <div className="grid grid-cols-1 gap-4 sm:grid-cols-3">
        <div className="rounded-[18px] border border-white/[0.07] bg-[#101419] p-5">
          <p className="text-[11px] font-medium uppercase tracking-[0.12em] text-[#8b919b]">Total Original Loan</p>
          <p className="mt-2 text-2xl font-medium tracking-[-0.03em] text-[#e1e2e8]">
            {formatCurrency(summary.total_original_loan)}
          </p>
        </div>
        <div className="rounded-[18px] border border-white/[0.07] bg-[#101419] p-5">
          <p className="text-[11px] font-medium uppercase tracking-[0.12em] text-[#8b919b]">Total Repaid</p>
          <p className="mt-2 text-2xl font-medium tracking-[-0.03em] text-[#4ade80]">
            {formatCurrency(summary.total_repaid)}
          </p>
        </div>
        <div className="rounded-[18px] border border-white/[0.07] bg-[#101419] p-5">
          <p className="text-[11px] font-medium uppercase tracking-[0.12em] text-[#8b919b]">Monthly Payment</p>
          <p className="mt-2 text-2xl font-medium tracking-[-0.03em] text-[#e1e2e8]">
            {formatCurrency(summary.monthly_liability_payment)}
          </p>
        </div>
      </div>

      {/* Largest Liability Card */}
      {hl && (
        <div className="rounded-[20px] border border-white/[0.08] bg-[#101419] p-6 shadow-[0_4px_20px_rgba(0,0,0,0.12)]">
          <div className="flex flex-wrap items-center justify-between gap-3 mb-4">
            <div>
              <p className="text-[11px] font-medium uppercase tracking-[0.12em] text-[#8b919b]">Largest Liability</p>
              <p className="mt-1 text-[15px] font-medium text-[#e1e2e8]">{hl.liability}</p>
            </div>
            <span className="rounded-full border border-[#7abcff]/20 bg-[#7abcff]/10 px-3 py-1 text-xs font-medium text-[#7abcff]">
              {hl.category}
            </span>
          </div>
          <div className="grid grid-cols-1 gap-4 sm:grid-cols-3">
            <div className="rounded-[14px] bg-white/[0.035] p-4">
              <p className="text-xs text-[#8b919b]">Original Loan</p>
              <p className="mt-2 text-lg font-medium tracking-[-0.02em] text-[#e1e2e8]">
                {formatCurrency(hl.original_loan)}
              </p>
            </div>
            <div className="rounded-[14px] bg-white/[0.035] p-4">
              <p className="text-xs text-[#8b919b]">Outstanding Balance</p>
              <p className="mt-2 text-lg font-medium tracking-[-0.02em] text-[#ffca7b]">
                {formatCurrency(hl.outstanding_balance)}
              </p>
            </div>
            <div className="rounded-[14px] bg-white/[0.035] p-4">
              <p className="text-xs text-[#8b919b]">Monthly EMI</p>
              <p className="mt-2 text-lg font-medium tracking-[-0.02em] text-[#e1e2e8]">
                {formatCurrency(hl.monthly_emi)}
              </p>
            </div>
          </div>
        </div>
      )}

      {/* Summary Row — Active Liabilities + Largest Monthly EMI */}
      <div className="grid grid-cols-1 gap-4 sm:grid-cols-2">
        <div className="rounded-[18px] border border-white/[0.07] bg-[#101419] p-5">
          <p className="text-[11px] font-medium uppercase tracking-[0.12em] text-[#8b919b]">Active Liabilities</p>
          <p className="mt-2 text-2xl font-medium tracking-[-0.03em] text-[#e1e2e8]">
            {summary.active_liabilities}
          </p>
        </div>
        <div className="rounded-[18px] border border-white/[0.07] bg-[#101419] p-5">
          <p className="text-[11px] font-medium uppercase tracking-[0.12em] text-[#8b919b]">Largest Monthly EMI</p>
          <p className="mt-2 text-2xl font-medium tracking-[-0.03em] text-[#e1e2e8]">
            {formatCurrency(summary.largest_monthly_emi)}
          </p>
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

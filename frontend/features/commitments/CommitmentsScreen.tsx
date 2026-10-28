"use client";

import { useEffect, useState } from "react";
import { getAvailablePeriods, getFinance } from "@/lib/api";
import { LoadingState } from "@/components/ui/LoadingState";
import { ErrorState } from "@/components/ui/ErrorState";
import { formatCurrency } from "@/lib/formatters/currency";
import type { AvailablePeriod, FinanceData } from "@/types/finance";

export default function CommitmentsScreen() {
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
        setError(err instanceof Error ? err.message : "Failed to load commitments data.");
      } finally {
        setLoading(false);
      }
    }
    load();
  }, []);

  if (loading) return <LoadingState />;
  if (error || !finance) return <ErrorState message={error ?? "No data available."} />;

  const allTime = finance.commitment_summary;
  const monthly = finance.financial_snapshot?.commitment_summary;
  const commitmentInsight = finance.financial_snapshot?.insights?.commitment;

  return (
    <div className="min-h-screen bg-[#0b0d12] px-6 py-10">
      <div className="mx-auto max-w-5xl space-y-8">

        {/* Page Header */}
        <div>
          <p className="text-xs font-medium uppercase tracking-[0.14em] text-[#8b919b]">Debt &amp; Obligations</p>
          <h1 className="mt-2 text-3xl font-medium tracking-[-0.03em] text-[#e1e2e8]">Commitments</h1>
          <p className="mt-2 text-sm text-[#8b919b]">Track your borrowed capital and monthly repayment obligations.</p>
        </div>

        {/* Stat Chips — 3 cols */}
        <div className="grid grid-cols-1 gap-4 md:grid-cols-3">
          {/* Outstanding Debt */}
          <div className="rounded-[18px] border border-white/[0.07] bg-[#101419] p-5">
            <p className="text-[11px] font-medium uppercase tracking-[0.12em] text-[#8b919b]">All-time Outstanding Debt</p>
            <p className="mt-3 text-3xl font-medium tracking-[-0.03em] text-[#ffb4ab]">
              {formatCurrency(allTime?.outstanding_debt ?? 0)}
            </p>
          </div>

          {/* Monthly Commitments */}
          <div className="rounded-[18px] border border-white/[0.07] bg-[#101419] p-5">
            <p className="text-[11px] font-medium uppercase tracking-[0.12em] text-[#8b919b]">Monthly Commitments</p>
            <p className="mt-3 text-3xl font-medium tracking-[-0.03em] text-[#ffca7b]">
              {formatCurrency(allTime?.monthly_commitments ?? 0)}
            </p>
          </div>

          {/* Active Commitments */}
          <div className="rounded-[18px] border border-white/[0.07] bg-[#101419] p-5">
            <p className="text-[11px] font-medium uppercase tracking-[0.12em] text-[#8b919b]">Active Commitments</p>
            <p className="mt-3 text-3xl font-medium tracking-[-0.03em] text-[#e1e2e8]">
              {allTime?.active_commitments ?? 0}
            </p>
          </div>
        </div>

        {/* Total Borrowed / Total Repaid */}
        <div className="rounded-[20px] border border-white/[0.08] bg-[#101419] p-6 shadow-[0_4px_20px_rgba(0,0,0,0.12)]">
          <p className="text-[11px] font-medium uppercase tracking-[0.12em] text-[#8b919b]">All-time Summary</p>
          <div className="mt-4 grid grid-cols-1 gap-4 md:grid-cols-2">
            <div className="rounded-[14px] bg-white/[0.035] p-4">
              <p className="text-[11px] font-medium uppercase tracking-[0.12em] text-[#8b919b]">Total Borrowed</p>
              <p className="mt-2 text-3xl font-medium tracking-[-0.03em] text-[#e1e2e8]">
                {formatCurrency(allTime?.total_borrowed ?? 0)}
              </p>
            </div>
            <div className="rounded-[14px] bg-white/[0.035] p-4">
              <p className="text-[11px] font-medium uppercase tracking-[0.12em] text-[#8b919b]">Total Repaid</p>
              <p className="mt-2 text-3xl font-medium tracking-[-0.03em] text-[#4ade80]">
                {formatCurrency(allTime?.total_repaid ?? 0)}
              </p>
            </div>
          </div>
        </div>

        {/* This Month */}
        {monthly && (
          <div className="rounded-[20px] border border-white/[0.08] bg-[#101419] p-6 shadow-[0_4px_20px_rgba(0,0,0,0.12)]">
            <p className="text-[11px] font-medium uppercase tracking-[0.12em] text-[#8b919b]">This Month</p>
            <div className="mt-4 grid grid-cols-1 gap-4 md:grid-cols-2">
              <div className="rounded-[14px] bg-white/[0.035] p-4">
                <p className="text-[11px] font-medium uppercase tracking-[0.12em] text-[#8b919b]">Monthly Commitments</p>
                <p className="mt-2 text-3xl font-medium tracking-[-0.03em] text-[#ffca7b]">
                  {formatCurrency(monthly.monthly_commitments ?? 0)}
                </p>
              </div>
              <div className="rounded-[14px] bg-white/[0.035] p-4">
                <p className="text-[11px] font-medium uppercase tracking-[0.12em] text-[#8b919b]">Outstanding Debt</p>
                <p className="mt-2 text-3xl font-medium tracking-[-0.03em] text-[#ffb4ab]">
                  {formatCurrency(monthly.outstanding_debt ?? 0)}
                </p>
              </div>
            </div>
          </div>
        )}

        {/* Commitment Insight */}
        {commitmentInsight && (
          <div className="rounded-[20px] border border-white/[0.08] bg-[#101419] p-6">
            <div className="flex items-start gap-4">
              <div className="flex h-10 w-10 shrink-0 items-center justify-center rounded-full bg-[#ffca7b]/10">
                <span className="material-symbols-outlined text-[18px] text-[#ffca7b]">info</span>
              </div>
              <div>
                <p className="text-[11px] font-medium uppercase tracking-[0.12em] text-[#8b919b]">
                  {commitmentInsight.priority ?? "Info"} Priority
                </p>
                <p className="mt-1 text-[15px] font-medium text-[#e1e2e8]">{commitmentInsight.status}</p>
                <p className="mt-1 text-sm leading-6 text-[#8b919b]">{commitmentInsight.reason}</p>
                {commitmentInsight.recommendation && (
                  <p className="mt-2 text-sm text-[#7abcff]">{commitmentInsight.recommendation}</p>
                )}
              </div>
            </div>
          </div>
        )}
      </div>
    </div>
  );
}

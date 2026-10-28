"use client";

import { useEffect, useState } from "react";
import { LoadingState } from "@/components/ui/LoadingState";
import { ErrorState } from "@/components/ui/ErrorState";
import { getAvailablePeriods, getFinance } from "@/lib/api";
import type { AvailablePeriod, FinanceData } from "@/types/finance";

export default function SpendingScreen() {
    const [finance, setFinance] = useState<FinanceData | null>(null);
    const [periods, setPeriods] = useState<AvailablePeriod[]>([]);
    const [selectedPeriod, setSelectedPeriod] = useState<AvailablePeriod | null>(null);
    const [loading, setLoading] = useState(true);
    const [error, setError] = useState<string | null>(null);

    useEffect(() => {
        async function loadPeriods() {
            try {
                setLoading(true);
                const availablePeriods = await getAvailablePeriods();
                setPeriods(availablePeriods);
                if (availablePeriods.length > 0) {
                    setSelectedPeriod(availablePeriods[availablePeriods.length - 1]);
                }
            } catch (err) {
                setError(err instanceof Error ? err.message : "Unable to load financial periods.");
            } finally {
                setLoading(false);
            }
        }
        loadPeriods();
    }, []);

    useEffect(() => {
        if (!selectedPeriod) return;
        const currentPeriod = selectedPeriod;
        async function loadFinance() {
            try {
                setLoading(true);
                setError(null);
                const data = await getFinance(currentPeriod.month, currentPeriod.year);
                setFinance(data);
            } catch (err) {
                setError(err instanceof Error ? err.message : "Unable to load spending data.");
            } finally {
                setLoading(false);
            }
        }
        loadFinance();
    }, [selectedPeriod]);

    if (loading && !finance) return <LoadingState />;
    if (error && !finance) return <ErrorState message={error} />;
    if (!finance || !selectedPeriod) return null;

    const snapshot = finance.financial_snapshot;
    const { monthly_summary, monthly_distribution, highest_spending, top_three_categories } = snapshot;

    return (
        <div className="space-y-8">
            <section>
                <div className="flex flex-col gap-4 sm:flex-row sm:items-end sm:justify-between">
                    <div>
                        <p className="text-sm text-[#8b919b]">Cash & Spending Flow</p>
                        <h1 className="mt-2 text-3xl font-medium tracking-[-0.03em] text-[#e1e2e8]">Spending</h1>
                        <p className="mt-2 max-w-2xl text-[15px] leading-6 text-[#8b919b]">
                            Analyze your expenses and category breakdowns.
                        </p>
                    </div>

                    {periods.length > 0 && (
                        <select
                            value={`${selectedPeriod.month}-${selectedPeriod.year}`}
                            onChange={(event) => {
                                const [month, year] = event.target.value.split("-").map(Number);
                                const period = periods.find(item => item.month === month && item.year === year);
                                if (period) setSelectedPeriod(period);
                            }}
                            className="rounded-xl border border-white/[0.08] bg-white/[0.04] px-3 py-2 text-sm text-[#e1e2e8] outline-none"
                        >
                            {periods.map((period) => (
                                <option key={`${period.month}-${period.year}`} value={`${period.month}-${period.year}`} className="bg-[#0b0d12]">
                                    {period.month}/{period.year}
                                </option>
                            ))}
                        </select>
                    )}
                </div>
            </section>

            <section className="grid gap-4 md:grid-cols-3">
                <div className="rounded-[18px] border border-white/[0.07] bg-[#101419] p-5">
                    <p className="text-[11px] font-medium uppercase tracking-[0.12em] text-[#8b919b]">Total Expense</p>
                    <p className="mt-2 text-2xl font-medium text-[#e1e2e8]">₹{monthly_summary.total_expense.toLocaleString("en-IN")}</p>
                </div>
                <div className="rounded-[18px] border border-white/[0.07] bg-[#101419] p-5">
                    <p className="text-[11px] font-medium uppercase tracking-[0.12em] text-[#8b919b]">Projected (End of Month)</p>
                    <p className="mt-2 text-2xl font-medium text-[#e1e2e8]">₹{monthly_summary.projected_expense?.toLocaleString("en-IN") || monthly_summary.total_expense.toLocaleString("en-IN")}</p>
                </div>
                <div className="rounded-[18px] border border-white/[0.07] bg-[#101419] p-5">
                    <p className="text-[11px] font-medium uppercase tracking-[0.12em] text-[#8b919b]">Needs vs Wants</p>
                    <div className="mt-2 flex gap-4">
                        <div>
                            <span className="text-[#8b919b] text-sm">Need </span>
                            <span className="text-[#e1e2e8] font-medium">{monthly_distribution.need_percentage.toFixed(0)}%</span>
                        </div>
                        <div>
                            <span className="text-[#8b919b] text-sm">Want </span>
                            <span className="text-[#e1e2e8] font-medium">{monthly_distribution.want_percentage.toFixed(0)}%</span>
                        </div>
                    </div>
                </div>
            </section>

            <section className="grid gap-4 md:grid-cols-2">
                <div className="rounded-[20px] border border-white/[0.08] bg-[#101419] p-6 shadow-[0_4px_20px_rgba(0,0,0,0.12)]">
                    <h2 className="text-lg font-medium text-[#e1e2e8]">Top Categories</h2>
                    <div className="mt-6 space-y-4">
                        {Object.entries(top_three_categories.categories).map(([cat, amount]) => (
                            <div key={cat} className="flex justify-between items-center border-b border-white/[0.05] pb-3 last:border-0 last:pb-0">
                                <span className="text-[15px] text-[#aeb4bf]">{cat}</span>
                                <span className="font-medium text-[#e1e2e8]">₹{amount.toLocaleString("en-IN")}</span>
                            </div>
                        ))}
                    </div>
                </div>
                <div className="rounded-[20px] border border-white/[0.08] bg-[#101419] p-6 shadow-[0_4px_20px_rgba(0,0,0,0.12)]">
                    <h2 className="text-lg font-medium text-[#e1e2e8]">Highest Spending</h2>
                    <div className="mt-6">
                        <div className="rounded-[14px] bg-white/[0.035] p-5">
                            <span className="text-xs font-medium uppercase tracking-[0.12em] text-[#8b919b]">Category</span>
                            <p className="mt-1 text-xl font-medium text-[#e1e2e8]">{highest_spending.category || "N/A"}</p>
                            <p className="mt-2 text-lg text-[#7abcff]">₹{(highest_spending.amount || 0).toLocaleString("en-IN")}</p>
                        </div>
                    </div>
                    {monthly_summary.anomaly_count !== undefined && monthly_summary.anomaly_count > 0 && (
                        <div className="mt-4 rounded-[14px] bg-amber-500/[0.1] border border-amber-500/[0.2] p-4 flex gap-3 items-start">
                            <span className="material-symbols-outlined text-amber-500 text-sm mt-0.5">warning</span>
                            <div>
                                <p className="text-[13px] font-medium text-amber-500">Unusual Activity Detected</p>
                                <p className="text-xs text-amber-500/70 mt-1">We flagged {monthly_summary.anomaly_count} duplicated or anomalous transactions.</p>
                            </div>
                        </div>
                    )}
                </div>
            </section>
        </div>
    );
}

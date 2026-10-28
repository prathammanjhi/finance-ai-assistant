"use client";

import { useEffect, useState } from "react";
import { LoadingState } from "@/components/ui/LoadingState";
import { ErrorState } from "@/components/ui/ErrorState";
import { getAvailablePeriods, getFinance } from "@/lib/api";
import type { AvailablePeriod, FinanceData } from "@/types/finance";
import InsightCard from "@/features/insights/components/InsightCard";

export default function BudgetScreen() {
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
                setError(err instanceof Error ? err.message : "Unable to load budget data.");
            } finally {
                setLoading(false);
            }
        }
        loadFinance();
    }, [selectedPeriod]);

    if (loading && !finance) return <LoadingState />;
    if (error && !finance) return <ErrorState message={error} />;
    if (!finance || !selectedPeriod) return null;

    const { summary, insights } = finance.budget;
    const isNoData = summary.status === "NO_BUDGET_DATA";

    return (
        <div className="space-y-8">
            <section>
                <div className="flex flex-col gap-4 sm:flex-row sm:items-end sm:justify-between">
                    <div>
                        <p className="text-sm text-[#8b919b]">Cash & Spending Flow</p>
                        <h1 className="mt-2 text-3xl font-medium tracking-[-0.03em] text-[#e1e2e8]">Budget</h1>
                        <p className="mt-2 max-w-2xl text-[15px] leading-6 text-[#8b919b]">
                            Monitor your budget limits and pacing.
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

            {!isNoData && (
                <section className="grid gap-4 md:grid-cols-3">
                    <div className="rounded-[18px] border border-white/[0.07] bg-[#101419] p-5">
                        <p className="text-[11px] font-medium uppercase tracking-[0.12em] text-[#8b919b]">Monthly Budget</p>
                        <p className="mt-2 text-2xl font-medium text-[#e1e2e8]">₹{summary.monthly_budget.toLocaleString("en-IN")}</p>
                    </div>
                    <div className="rounded-[18px] border border-white/[0.07] bg-[#101419] p-5">
                        <p className="text-[11px] font-medium uppercase tracking-[0.12em] text-[#8b919b]">Spent</p>
                        <p className="mt-2 text-2xl font-medium text-[#e1e2e8]">₹{summary.spent.toLocaleString("en-IN")}</p>
                    </div>
                    <div className="rounded-[18px] border border-white/[0.07] bg-[#101419] p-5">
                        <p className="text-[11px] font-medium uppercase tracking-[0.12em] text-[#8b919b]">Remaining</p>
                        <p className={`mt-2 text-2xl font-medium ${summary.remaining >= 0 ? 'text-[#4ade80]' : 'text-[#ffb4ab]'}`}>
                            {summary.remaining < 0 ? '-' : ''}₹{Math.abs(summary.remaining).toLocaleString("en-IN")}
                        </p>
                    </div>
                </section>
            )}
            
            {!isNoData && (
                <section>
                    <div className="rounded-[20px] border border-white/[0.08] bg-[#101419] p-6 shadow-[0_4px_20px_rgba(0,0,0,0.12)]">
                        <div className="flex justify-between items-center mb-4">
                            <h2 className="text-lg font-medium text-[#e1e2e8]">Utilization</h2>
                            <span className="text-[#8b919b] text-sm">{summary.utilization.toFixed(1)}%</span>
                        </div>
                        <div className="h-4 w-full bg-white/[0.04] rounded-full overflow-hidden">
                            <div 
                                className={`h-full ${summary.utilization > 100 ? 'bg-[#ffb4ab]' : summary.utilization > 80 ? 'bg-[#ffca7b]' : 'bg-[#7abcff]'}`}
                                style={{ width: `${Math.min(summary.utilization, 100)}%` }}
                            />
                        </div>
                    </div>
                </section>
            )}

            <section>
                <div className="mb-4">
                    <h2 className="text-lg font-medium text-[#e1e2e8]">Budget Intelligence</h2>
                </div>
                <InsightCard
                    title="Budget Health"
                    priority={insights.priority}
                    reason={insights.reason}
                    recommendation={insights.recommendation}
                    status={insights.status}
                />
            </section>
        </div>
    );
}

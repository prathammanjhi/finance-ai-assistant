"use client";

import { useEffect, useState } from "react";

import { LoadingState } from "@/components/ui/LoadingState";
import { ErrorState } from "@/components/ui/ErrorState";

import InsightCard from "./components/InsightCard";

import {
    getAvailablePeriods,
    getFinance,
} from "@/lib/api";

import type {
    AvailablePeriod,
    FinanceData,
} from "@/types/finance";

export default function InsightsScreen() {
    const [finance, setFinance] = useState<FinanceData | null>(null);
    const [periods, setPeriods] = useState<AvailablePeriod[]>([]);
    const [selectedPeriod, setSelectedPeriod] =
        useState<AvailablePeriod | null>(null);

    const [loading, setLoading] = useState(true);
    const [error, setError] = useState<string | null>(null);

    useEffect(() => {
        async function loadPeriods() {
            try {
                setLoading(true);
                setError(null);

                const availablePeriods =
                    await getAvailablePeriods();

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
                        : "Unable to load financial insights."
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

    const insights = Object.entries(
        finance.financial_snapshot.insights
    );

    const budgetInsight = finance.budget.insights;

    return (
        <div className="space-y-8">
            {/* Header */}
            <section>
                <div className="flex flex-col gap-4 sm:flex-row sm:items-end sm:justify-between">
                    <div>
                        <p className="text-sm text-[#8b919b]">
                            Financial Intelligence
                        </p>

                        <h1 className="mt-2 text-3xl font-medium tracking-[-0.03em] text-[#e1e2e8]">
                            Insights
                        </h1>

                        <p className="mt-2 max-w-2xl text-[15px] leading-6 text-[#8b919b]">
                            Understand what is happening with your money
                            and what deserves your attention.
                        </p>
                    </div>

                    {periods.length > 0 && (
                        <select
                            value={`${selectedPeriod.month}-${selectedPeriod.year}`}
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
                    )}
                </div>
            </section>

            {/* Core insights */}
            <section>
                <div className="mb-4">
                    <h2 className="text-lg font-medium text-[#e1e2e8]">
                        What deserves your attention
                    </h2>

                    <p className="mt-1 text-sm text-[#8b919b]">
                        Insights generated by the Finance Core.
                    </p>
                </div>

                <div className="space-y-5">
                    {insights.length > 0 ? (
                        insights.map(([key, insight]) => (
                            <InsightCard
                                key={key}
                                priority={insight.priority}
                                title={insight.reason}
                                reason={insight.reason}
                                status={insight.status}
                            />
                        ))
                    ) : (
                        <div className="rounded-[20px] border border-white/[0.08] bg-[#101419] p-6 text-sm text-[#8b919b]">
                            No financial insights are available for
                            this period.
                        </div>
                    )}
                </div>
            </section>

            {/* Budget intelligence */}
            <section>
                <div className="mb-4">
                    <h2 className="text-lg font-medium text-[#e1e2e8]">
                        Budget Intelligence
                    </h2>

                    <p className="mt-1 text-sm text-[#8b919b]">
                        What your current budget position suggests.
                    </p>
                </div>

                <InsightCard
                    priority={budgetInsight.priority}
                    title={budgetInsight.reason}
                    reason={budgetInsight.reason}
                    recommendation={budgetInsight.recommendation}
                    status={budgetInsight.status}
                />
            </section>

            {/* Supporting evidence */}
            <section>
                <div className="mb-4">
                    <h2 className="text-lg font-medium text-[#e1e2e8]">
                        Supporting numbers
                    </h2>

                    <p className="mt-1 text-sm text-[#8b919b]">
                        The financial evidence behind your current
                        picture.
                    </p>
                </div>

                <div className="grid gap-4 md:grid-cols-3">
                    <div className="rounded-[18px] border border-white/[0.07] bg-[#101419] p-5">
                        <p className="text-xs text-[#8b919b]">
                            Monthly commitments
                        </p>

                        <p className="mt-2 text-xl font-medium text-[#e1e2e8]">
                            ₹
                            {finance.financial_snapshot.commitment_summary.monthly_commitments.toLocaleString(
                                "en-IN"
                            )}
                        </p>
                    </div>

                    <div className="rounded-[18px] border border-white/[0.07] bg-[#101419] p-5">
                        <p className="text-xs text-[#8b919b]">
                            Highest spending category
                        </p>

                        <p className="mt-2 text-xl font-medium text-[#e1e2e8]">
                            {finance.financial_snapshot.highest_spending.category}
                        </p>

                        <p className="mt-1 text-sm text-[#8b919b]">
                            ₹
                            {finance.financial_snapshot.highest_spending.amount.toLocaleString(
                                "en-IN"
                            )}
                        </p>
                    </div>

                    <div className="rounded-[18px] border border-white/[0.07] bg-[#101419] p-5">
                        <p className="text-xs text-[#8b919b]">
                            Savings rate
                        </p>

                        <p className="mt-2 text-xl font-medium text-[#e1e2e8]">
                            {finance.financial_snapshot.savings_summary.savings_rate}%
                        </p>
                    </div>
                </div>
            </section>

            {error && (
                <p className="text-sm text-amber-400">
                    {error}
                </p>
            )}
        </div>
    );
}
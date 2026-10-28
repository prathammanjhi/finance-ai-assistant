"use client";

import { useEffect, useState } from "react";
import { Card } from "@/components/ui/Card";
import { LoadingState } from "@/components/ui/LoadingState";
import { ErrorState } from "@/components/ui/ErrorState";
import { getAvailablePeriods, getFinance } from "@/lib/api";
import { formatCurrency } from "@/lib/formatters/currency";
import type { AvailablePeriod, FinanceData } from "@/types/finance";

export default function CashFlowScreen() {
    const [periods, setPeriods] = useState<AvailablePeriod[]>([]);
    const [selectedPeriod, setSelectedPeriod] =
        useState<AvailablePeriod | null>(null);

    const [finance, setFinance] = useState<FinanceData | null>(null);
    const [loading, setLoading] = useState(true);
    const [error, setError] = useState<string | null>(null);

    useEffect(() => {
        async function loadPeriods() {
            try {
                const data = await getAvailablePeriods();

                setPeriods(data);

                if (data.length > 0) {
                    setSelectedPeriod(data[data.length - 1]);
                }
            } catch {
                setError("Unable to load available financial periods.");
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

                const data = await getFinance(period.month, period.year);
                setFinance(data);
            } catch {
                setError("Unable to load cash flow data.");
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

    const income = snapshot.savings_summary.total_income;
    const expenses = snapshot.savings_summary.total_expense;

    // Cash flow = income - expenses.
    // This uses the Finance Core's existing savings calculation.
    const cashFlow = snapshot.savings_summary.gross_savings;

    const cashPosition = snapshot.financial_position.cash_position;
    const expectedPosition = snapshot.financial_position.expected_position;

    const commitments = snapshot.commitment_summary.monthly_commitments;

    const isPositive = cashFlow > 0;
    const isNegative = cashFlow < 0;

    return (
        <div className="space-y-8">
            <div>
                <p className="text-xs font-medium uppercase tracking-[0.14em] text-[#8b919b]">
                    Financial Overview
                </p>

                <h1 className="mt-2 text-3xl font-medium tracking-[-0.03em] text-[#e1e2e8]">
                    Cash Flow
                </h1>

                <p className="mt-2 text-sm text-[#8b919b]">
                    Understand how money moves through your finances.
                </p>
            </div>

            {/* Period selector */}
            {periods.length > 0 && (
                <div className="flex items-center gap-3">
                    <label
                        htmlFor="cash-flow-period"
                        className="text-sm text-[#8b919b]"
                    >
                        Period
                    </label>

                    <select
                        id="cash-flow-period"
                        value={`${selectedPeriod.month}-${selectedPeriod.year}`}
                        onChange={(event) => {
                            const [month, year] = event.target.value.split("-").map(Number);

                            const period = periods.find(
                                (item) => item.month === month && item.year === year
                            );

                            if (period) {
                                setSelectedPeriod(period);
                            }
                        }}
                        className="rounded-[10px] border border-white/[0.08] bg-[#101419] px-3 py-2 text-sm text-[#e1e2e8] outline-none"
                    >
                        {periods.map((period) => (
                            <option
                                key={`${period.month}-${period.year}`}
                                value={`${period.month}-${period.year}`}
                            >
                                {new Date(period.year, period.month - 1).toLocaleString(
                                    "en-IN",
                                    {
                                        month: "long",
                                        year: "numeric",
                                    }
                                )}
                            </option>
                        ))}
                    </select>
                </div>
            )}

            {/* Main cash flow */}
            <Card>
                <div className="flex flex-col gap-6">
                    <div>
                        <p className="text-xs font-medium uppercase tracking-[0.12em] text-[#8b919b]">
                            Net Cash Flow
                        </p>

                        <p
                            className={`mt-3 text-4xl font-medium tracking-[-0.03em] ${isPositive
                                ? "text-[#4ade80]"
                                : isNegative
                                    ? "text-[#ffb4ab]"
                                    : "text-[#e1e2e8]"
                                }`}
                        >
                            {formatCurrency(cashFlow)}
                        </p>

                        <p className="mt-2 text-sm text-[#8b919b]">
                            Income minus expenses for the selected period.
                        </p>
                    </div>

                    <div className="grid gap-3 sm:grid-cols-2">
                        <div className="rounded-[14px] bg-white/[0.035] p-4">
                            <p className="text-xs text-[#8b919b]">Income</p>
                            <p className="mt-2 text-lg font-medium text-[#e1e2e8]">
                                {formatCurrency(income)}
                            </p>
                        </div>

                        <div className="rounded-[14px] bg-white/[0.035] p-4">
                            <p className="text-xs text-[#8b919b]">Expenses</p>
                            <p className="mt-2 text-lg font-medium text-[#e1e2e8]">
                                {formatCurrency(expenses)}
                            </p>
                        </div>
                    </div>
                </div>
            </Card>

            {/* Position */}
            <div className="grid gap-4 md:grid-cols-2">
                <Card>
                    <p className="text-xs font-medium uppercase tracking-[0.12em] text-[#8b919b]">
                        Cash Position
                    </p>

                    <p className="mt-3 text-2xl font-medium text-[#e1e2e8]">
                        {formatCurrency(cashPosition)}
                    </p>

                    <p className="mt-2 text-sm leading-6 text-[#8b919b]">
                        Current liquid financial position reported by the Finance Core.
                    </p>
                </Card>

                <Card>
                    <p className="text-xs font-medium uppercase tracking-[0.12em] text-[#8b919b]">
                        Expected Position
                    </p>

                    <p className="mt-3 text-2xl font-medium text-[#e1e2e8]">
                        {formatCurrency(expectedPosition)}
                    </p>

                    <p className="mt-2 text-sm leading-6 text-[#8b919b]">
                        Expected position after the currently calculated commitments.
                    </p>
                </Card>
            </div>

            {/* Commitments */}
            <Card>
                <div className="flex items-center justify-between gap-4">
                    <div>
                        <p className="text-xs font-medium uppercase tracking-[0.12em] text-[#8b919b]">
                            Monthly Commitments
                        </p>

                        <p className="mt-3 text-2xl font-medium text-[#e1e2e8]">
                            {formatCurrency(commitments)}
                        </p>
                    </div>

                    <span className="rounded-full bg-white/[0.06] px-3 py-1 text-xs text-[#aeb4bf]">
                        Fixed outflow
                    </span>
                </div>
            </Card>
        </div>
    );
}
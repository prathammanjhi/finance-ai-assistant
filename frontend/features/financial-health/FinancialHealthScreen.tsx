"use client";

import { useEffect, useState } from "react";
import { getAvailablePeriods, getFinance } from "@/lib/api";
import { LoadingState } from "@/components/ui/LoadingState";
import { ErrorState } from "@/components/ui/ErrorState";
import type { AvailablePeriod, FinanceData } from "@/types/finance";

interface FinancialHealthSummary {
  financial_health_score: number;
  financial_grade: string;
  financial_risk: string;
  financial_strength: string;
  financial_score: number;
  budget_score: number;
  savings_score: number;
  emergency_score: number;
  goal_score: number;
  investment_score: number;
  asset_score: number;
  liability_score: number;
  net_worth_score: number;
  wealth_health_score: number;
}

interface FinancialHealthInsight {
  status: string;
  priority: string;
  reason: string;
  recommendation: string;
  focus_area: string;
}

const PILLARS: { key: keyof FinancialHealthSummary; label: string }[] = [
  { key: "financial_score", label: "Financial" },
  { key: "budget_score", label: "Budget" },
  { key: "savings_score", label: "Savings" },
  { key: "emergency_score", label: "Emergency" },
  { key: "goal_score", label: "Goals" },
  { key: "investment_score", label: "Investment" },
  { key: "asset_score", label: "Assets" },
  { key: "liability_score", label: "Liability" },
  { key: "net_worth_score", label: "Net Worth" },
  { key: "wealth_health_score", label: "Wealth Health" },
];

function scoreColor(score: number): string {
  if (score >= 70) return "#4ade80";
  if (score >= 40) return "#ffca7b";
  return "#ffb4ab";
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

export default function FinancialHealthScreen() {
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);
  const [summary, setSummary] = useState<FinancialHealthSummary | null>(null);
  const [insights, setInsights] = useState<FinancialHealthInsight[]>([]);

  useEffect(() => {
    async function load() {
      try {
        const periods: AvailablePeriod[] = await getAvailablePeriods();
        if (!periods.length) throw new Error("No periods available.");
        const latest = periods[periods.length - 1];
        const finance: FinanceData = await getFinance(latest.month, latest.year);
        setSummary(finance.financial_health.financial_health_summary as FinancialHealthSummary);
        setInsights(finance.financial_health.financial_health_insights as FinancialHealthInsight[]);
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

  const riskPillColor =
    summary.financial_risk?.toLowerCase() === "low"
      ? "bg-[#4ade80]/10 text-[#4ade80]"
      : summary.financial_risk?.toLowerCase() === "medium"
      ? "bg-[#ffca7b]/10 text-[#ffca7b]"
      : "bg-[#ffb4ab]/10 text-[#ffb4ab]";

  return (
    <div className="min-h-screen bg-[#0b0d12] p-6 md:p-8">
      <div className="mx-auto max-w-5xl space-y-6">
        {/* Page Header */}
        <div>
          <p className="text-xs font-medium uppercase tracking-[0.14em] text-[#8b919b]">
            Wealth Intelligence
          </p>
          <h1 className="mt-2 text-3xl font-medium tracking-[-0.03em] text-[#e1e2e8]">
            Financial Health
          </h1>
          <p className="mt-2 text-sm text-[#8b919b]">
            Your comprehensive financial wellness score across 10 pillars.
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
            Overall Score
          </p>
          <div className="mt-4 flex items-end justify-center gap-1">
            <span className="text-7xl font-bold text-[#e1e2e8]">
              {summary.financial_health_score}
            </span>
            <span className="mb-3 text-2xl text-[#8b919b]">/100</span>
          </div>

          {/* Grade Badge */}
          <div className="mt-4 flex items-center justify-center gap-3">
            <span className="rounded-full bg-[#7abcff]/10 px-4 py-1.5 font-mono text-lg font-bold text-[#7abcff]">
              {summary.financial_grade}
            </span>
          </div>

          {/* Risk & Strength pills */}
          <div className="mt-4 flex items-center justify-center gap-3">
            <span
              className={`rounded-full px-3 py-1 text-xs font-medium ${riskPillColor}`}
            >
              {summary.financial_risk} Risk
            </span>
            <span className="rounded-full bg-[#7abcff]/10 px-3 py-1 text-xs font-medium text-[#7abcff]">
              {summary.financial_strength}
            </span>
          </div>
        </div>

        {/* 10-Pillar Score Grid */}
        <div className="rounded-[20px] border border-white/[0.08] bg-[#101419] p-6 shadow-[0_4px_20px_rgba(0,0,0,0.12)]">
          <p className="text-[11px] font-medium uppercase tracking-[0.12em] text-[#8b919b]">
            Pillar Breakdown
          </p>
          <div className="mt-5 grid grid-cols-1 gap-5 md:grid-cols-2 lg:grid-cols-3">
            {PILLARS.map(({ key, label }) => {
              const score = summary[key] as number;
              const color = scoreColor(score);
              return (
                <div key={key} className="rounded-[14px] bg-white/[0.035] p-4">
                  <div className="flex items-center justify-between">
                    <p className="text-sm text-[#8b919b]">{label}</p>
                    <p
                      className="text-sm font-semibold"
                      style={{ color }}
                    >
                      {score}
                    </p>
                  </div>
                  <div className="mt-2 h-2 rounded-full bg-white/[0.08]">
                    <div
                      className="h-2 rounded-full transition-all"
                      style={{
                        width: `${score}%`,
                        backgroundColor: color,
                      }}
                    />
                  </div>
                </div>
              );
            })}
          </div>
        </div>

        {/* Insight Cards */}
        {insights.length > 0 && (
          <div className="space-y-3">
            <p className="text-[11px] font-medium uppercase tracking-[0.12em] text-[#8b919b]">
              Health Insights
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
                      {insight.priority} Priority · {insight.focus_area}
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

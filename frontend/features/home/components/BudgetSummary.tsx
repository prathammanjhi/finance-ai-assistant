import { Card } from "@/components/ui/Card";
import { ProgressBar } from "@/components/ui/ProgressBar";
import { formatCurrency } from "@/lib/formatters/currency";

interface BudgetSummaryProps {
  monthlyBudget: number;
  spent: number;
  remaining: number;
  utilization: number;
  status: string;
}

export default function BudgetSummary({
  monthlyBudget,
  spent,
  remaining,
  utilization,
  status,
}: BudgetSummaryProps) {
  return (
    <section className="space-y-3">
      <div className="flex items-end justify-between">
        <div>
          <h2 className="text-[17px] font-semibold text-[var(--text-primary)]">
            Budget
          </h2>

          <p className="mt-1 text-[13px] text-[var(--text-muted)]">
            This month
          </p>
        </div>

        <span className="text-[13px] text-[var(--text-secondary)]">
          {Math.round(utilization)}% used
        </span>
      </div>

      <Card padding="lg">
        <div className="space-y-5">
          {/* Budget amount */}
          <div>
            <p className="text-[12px] uppercase tracking-[0.08em] text-[var(--text-muted)]">
              Monthly budget
            </p>

            <p className="mt-1 text-[28px] font-semibold tracking-tight text-[var(--text-primary)]">
              {formatCurrency(monthlyBudget)}
            </p>
          </div>

          {/* Progress */}
          <div className="space-y-2">
            <ProgressBar value={utilization} />

            <div className="flex justify-end">
              <span className="text-[12px] text-[var(--text-muted)]">
                {Math.round(utilization)}%
              </span>
            </div>
          </div>

          {/* Spent / Remaining */}
          <div className="grid grid-cols-2 gap-6 border-t border-white/[0.06] pt-4">
            <div>
              <p className="text-[12px] text-[var(--text-muted)]">
                Spent
              </p>

              <p className="mt-1 text-[16px] font-medium text-[var(--text-primary)]">
                {formatCurrency(spent)}
              </p>
            </div>

            <div>
              <p className="text-[12px] text-[var(--text-muted)]">
                Remaining
              </p>

              <p className="mt-1 text-[16px] font-medium text-[var(--text-primary)]">
                {formatCurrency(remaining)}
              </p>
            </div>
          </div>

          {/* Status */}
          <div className="border-t border-white/[0.06] pt-4">
            <p className="text-[13px] text-[var(--text-secondary)]">
              Status:{" "}
              <span className="text-[var(--accent-cyan)]">
                {status}
              </span>
            </p>
          </div>
        </div>
      </Card>
    </section>
  );
}
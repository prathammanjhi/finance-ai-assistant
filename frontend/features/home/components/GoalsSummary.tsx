import { Card } from "@/components/ui/Card";
import { ProgressBar } from "@/components/ui/ProgressBar";
import { formatCurrency } from "@/lib/formatters/currency";

interface GoalsSummaryProps {
  activeGoals: number;
  completedGoals: number;
  totalTargetAmount: number;
  totalCurrentAmount: number;
  progressPercentage: number;
}

export default function GoalsSummary({
  activeGoals,
  completedGoals,
  totalTargetAmount,
  totalCurrentAmount,
  progressPercentage,
}: GoalsSummaryProps) {
  return (
    <section className="space-y-3">
      <div>
        <h2 className="text-[17px] font-semibold text-[var(--text-primary)]">
          Goals
        </h2>

        <p className="mt-1 text-[13px] text-[var(--text-muted)]">
          Your progress toward what matters
        </p>
      </div>

      <Card padding="lg">
        <div className="space-y-5">
          {/* Goal overview */}
          <div className="flex items-start justify-between gap-4">
            <div>
              <p className="text-[12px] uppercase tracking-[0.08em] text-[var(--text-muted)]">
                Overall progress
              </p>

              <p className="mt-1 text-[28px] font-semibold tracking-tight text-[var(--text-primary)]">
                {Math.round(progressPercentage)}%
              </p>
            </div>

            <div className="text-right">
              <p className="text-[12px] text-[var(--text-muted)]">
                Active goals
              </p>

              <p className="mt-1 text-[16px] font-medium text-[var(--text-primary)]">
                {activeGoals}
              </p>
            </div>
          </div>

          {/* Progress */}
          <ProgressBar value={progressPercentage} />

          {/* Current / Target */}
          <div className="grid grid-cols-2 gap-6 border-t border-white/[0.06] pt-4">
            <div>
              <p className="text-[12px] text-[var(--text-muted)]">
                Current
              </p>

              <p className="mt-1 text-[16px] font-medium text-[var(--text-primary)]">
                {formatCurrency(totalCurrentAmount)}
              </p>
            </div>

            <div>
              <p className="text-[12px] text-[var(--text-muted)]">
                Target
              </p>

              <p className="mt-1 text-[16px] font-medium text-[var(--text-primary)]">
                {formatCurrency(totalTargetAmount)}
              </p>
            </div>
          </div>

          {/* Completed */}
          <div className="border-t border-white/[0.06] pt-4">
            <p className="text-[13px] text-[var(--text-secondary)]">
              Completed goals:{" "}
              <span className="text-[var(--finance-success)]">
                {completedGoals}
              </span>
            </p>
          </div>
        </div>
      </Card>
    </section>
  );
}
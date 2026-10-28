import { Card } from "@/components/ui/Card";

interface OpportunityCardProps {
  title: string;
  description: string;
  impact: string;
  actionLabel?: string;
  onAction?: () => void;
}

export default function OpportunityCard({
  title,
  description,
  impact,
  actionLabel = "Review opportunity",
  onAction,
}: OpportunityCardProps) {
  return (
    <section>
      <div className="mb-3 flex items-center justify-between">
        <div>
          <p className="text-sm font-medium text-[#e1e2e8]">
            Today&apos;s Opportunity
          </p>
          <p className="mt-1 text-xs text-[#8b919b]">
            One action that could improve your position
          </p>
        </div>

        <span
          className="material-symbols-outlined text-[#7abcff]"
          style={{ fontSize: "20px" }}
          aria-hidden="true"
        >
          lightbulb
        </span>
      </div>

      <Card className="relative overflow-hidden">
        <div className="pointer-events-none absolute -right-12 -top-12 h-32 w-32 rounded-full bg-[#7abcff]/10 blur-3xl" />

        <div className="relative">
          <p className="text-xs font-medium uppercase tracking-[0.08em] text-[#8b919b]">
            Suggested action
          </p>

          <h3 className="mt-2 text-lg font-semibold tracking-[-0.02em] text-[#e1e2e8]">
            {title}
          </h3>

          <p className="mt-2 max-w-2xl text-sm leading-6 text-[#8b919b]">
            {description}
          </p>

          <div className="mt-5 flex flex-col gap-4 border-t border-white/[0.06] pt-4 sm:flex-row sm:items-center sm:justify-between">
            <div>
              <p className="text-xs text-[#8b919b]">
                Potential impact
              </p>

              <p className="mt-1 text-sm font-medium text-[#4ade80]">
                {impact}
              </p>
            </div>

            <button
              type="button"
              onClick={onAction}
              className="inline-flex items-center justify-center gap-2 rounded-full bg-[#7abcff] px-5 py-2.5 text-sm font-semibold text-[#0b0d12] transition-colors hover:bg-[#9bcbff]"
            >
              {actionLabel}
              <span aria-hidden="true">→</span>
            </button>
          </div>
        </div>
      </Card>
    </section>
  );
}
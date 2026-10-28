import { Card } from "@/components/ui/Card";

interface AIInsightCardProps {
    priority: string;
    title: string;
    reason: string;
    recommendation: string;
    onSeeNumbers?: () => void;
}

export default function AIInsightCard({
    priority,
    title,
    reason,
    recommendation,
    onSeeNumbers,
}: AIInsightCardProps) {
    return (
        <Card className="relative overflow-hidden">
            {/* AI accent */}
            <div className="pointer-events-none absolute -right-16 -top-16 h-40 w-40 rounded-full bg-[#7abcff]/10 blur-3xl" />

            <div className="relative">
                {/* Header */}
                <div className="flex items-center justify-between gap-4">
                    <div className="flex items-center gap-2">
                        <span
                            className="material-symbols-outlined text-[#7abcff]"
                            style={{ fontSize: "20px" }}
                            aria-hidden="true"
                        >
                            auto_awesome
                        </span>

                        <span className="text-sm font-medium text-[#e1e2e8]">
                            Financial Intelligence
                        </span>
                    </div>

                    <span className="rounded-full bg-[#ffca7b]/10 px-3 py-1 text-[11px] font-medium uppercase tracking-[0.08em] text-[#ffca7b]">
                        {priority}
                    </span>
                </div>

                {/* WHAT */}
                <div className="mt-6">
                    <p className="text-[11px] font-medium uppercase tracking-[0.1em] text-[#8b919b]">
                        What&apos;s happening
                    </p>

                    <h2 className="mt-2 max-w-3xl text-xl font-semibold leading-7 tracking-[-0.02em] text-[#e1e2e8] sm:text-2xl">
                        {title}
                    </h2>
                </div>

                {/* WHY */}
                <div className="mt-6 border-t border-white/[0.06] pt-5">
                    <p className="text-[11px] font-medium uppercase tracking-[0.1em] text-[#8b919b]">
                        Why it matters
                    </p>

                    <p className="mt-2 max-w-3xl text-sm leading-6 text-[#c1c7d1]">
                        {reason}
                    </p>
                </div>

                {/* WHAT NEXT */}
                <div className="mt-6 rounded-xl bg-white/[0.025] p-4">
                    <p className="text-[11px] font-medium uppercase tracking-[0.1em] text-[#8b919b]">
                        What you can do
                    </p>

                    <p className="mt-2 text-sm leading-6 text-[#e1e2e8]">
                        {recommendation}
                    </p>
                </div>

                {/* Evidence link */}
                <button
                    type="button"
                    onClick={onSeeNumbers}
                    className="mt-5 inline-flex items-center gap-1 text-sm font-medium text-[#7abcff] transition-colors hover:text-[#9bcbff]"
                >
                    See the numbers
                    <span aria-hidden="true">→</span>
                </button>
            </div>
        </Card>
    );
}
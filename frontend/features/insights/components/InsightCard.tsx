interface InsightCardProps {
    priority: string;
    title: string;
    reason: string;
    recommendation?: string;
    status?: string;
}

export default function InsightCard({
    priority,
    title,
    reason,
    recommendation,
    status,
}: InsightCardProps) {
    return (
        <article className="rounded-[20px] border border-white/[0.08] bg-[#101419] p-6 shadow-[0_4px_20px_rgba(0,0,0,0.12)]">
            <div className="flex items-start justify-between gap-4">
                <div className="flex items-center gap-2">
                    <span className="material-symbols-outlined text-[#7abcff]">
                        auto_awesome
                    </span>

                    <span className="text-sm font-medium text-[#e1e2e8]">
                        Financial Insight
                    </span>
                </div>

                <span className="rounded-full bg-white/[0.08] px-3 py-1 text-[11px] font-medium uppercase tracking-wide text-[#e1e2e8]">
                    {priority}
                </span>
            </div>

            <div className="mt-6">
                <p className="text-[11px] font-medium uppercase tracking-[0.12em] text-[#8b919b]">
                    What's happening
                </p>

                <h2 className="mt-3 text-xl font-medium leading-7 tracking-[-0.02em] text-[#e1e2e8]">
                    {title}
                </h2>
            </div>

            <div className="mt-6 border-t border-white/[0.07] pt-5">
                <p className="text-[11px] font-medium uppercase tracking-[0.12em] text-[#8b919b]">
                    Why it matters
                </p>

                <p className="mt-3 text-[15px] leading-6 text-[#aeb4bf]">
                    {reason}
                </p>
            </div>

            {recommendation && (
                <div className="mt-5 rounded-[14px] bg-white/[0.035] p-4">
                    <p className="text-[11px] font-medium uppercase tracking-[0.12em] text-[#8b919b]">
                        What you can do
                    </p>

                    <p className="mt-2 text-[15px] leading-6 text-[#e1e2e8]">
                        {recommendation}
                    </p>
                </div>
            )}

            {status && (
                <p className="mt-5 text-xs text-[#8b919b]">
                    Status: <span className="text-[#aeb4bf]">{status}</span>
                </p>
            )}
        </article>
    );
}
"use client";

export default function AskScreen() {
    return (
        <div className="space-y-8">
            <div>
                <p className="text-xs font-medium uppercase tracking-[0.14em] text-[#8b919b]">
                    AI CFO
                </p>
                <h1 className="mt-2 text-3xl font-medium tracking-[-0.03em] text-[#e1e2e8]">
                    Ask AI
                </h1>
                <p className="mt-2 text-sm text-[#8b919b]">
                    Chat with your personal AI CFO. Get financial clarity in seconds.
                </p>
            </div>

            <div
                className="rounded-[20px] p-8 text-center"
                style={{
                    background:
                        "linear-gradient(135deg, rgba(122,188,255,0.08) 0%, rgba(16,20,24,0.95) 100%)",
                    border: "1px solid rgba(122,188,255,0.15)",
                }}
            >
                <span
                    className="material-symbols-outlined text-[#7abcff]"
                    style={{ fontSize: "48px" }}
                    aria-hidden="true"
                >
                    smart_toy
                </span>
                <p className="mt-4 text-lg font-medium text-[#e1e2e8]">Coming Soon</p>
                <p className="mt-2 text-sm leading-6 text-[#8b919b]">
                    Your AI CFO is being trained on your financial data.
                    <br />
                    Ask AI will be available in the next release.
                </p>
                <span className="mt-6 inline-block rounded-full bg-[#7abcff]/10 px-4 py-1.5 text-xs font-medium text-[#7abcff]">
                    Under Development
                </span>
            </div>
        </div>
    );
}


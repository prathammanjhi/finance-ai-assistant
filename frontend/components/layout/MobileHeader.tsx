interface MobileHeaderProps {
    onMenuClick?: () => void;
}

export default function MobileHeader({
    onMenuClick,
}: MobileHeaderProps) {
    return (
        <header className="flex h-16 items-center justify-between border-b border-white/[0.06] bg-[#0b0d12] px-4 lg:hidden">
            <button
                type="button"
                onClick={onMenuClick}
                aria-label="Open navigation"
                className="flex h-10 w-10 items-center justify-center rounded-xl text-[#8b919b] transition-colors hover:bg-white/[0.05] hover:text-[#e1e2e8]"
            >
                <span
                    className="material-symbols-outlined"
                    style={{ fontSize: "22px" }}
                    aria-hidden="true"
                >
                    menu
                </span>
            </button>

            <div className="flex items-center gap-2">
                <div className="flex h-8 w-8 items-center justify-center rounded-lg bg-[#7abcff]/10 ring-1 ring-[#7abcff]/20">
                    <span
                        className="material-symbols-outlined text-[#7abcff]"
                        style={{ fontSize: "18px" }}
                        aria-hidden="true"
                    >
                        auto_awesome
                    </span>
                </div>

                <span className="text-sm font-semibold text-[#e1e2e8]">
                    Finance AI
                </span>
            </div>

            <button
                type="button"
                aria-label="Open profile"
                className="flex h-10 w-10 items-center justify-center rounded-full border border-white/[0.08] bg-white/[0.04] text-[#8b919b]"
            >
                <span
                    className="material-symbols-outlined"
                    style={{ fontSize: "20px" }}
                    aria-hidden="true"
                >
                    person
                </span>
            </button>
        </header>
    );
}
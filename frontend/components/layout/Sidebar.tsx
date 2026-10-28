"use client";

import { usePathname } from "next/navigation";
import NavItem, { isRouteActive } from "./NavItem";

const primaryNavigation = [
    { label: "Home", href: "/", icon: "home", available: true },
    { label: "Insights", href: "/insights", icon: "auto_awesome", available: true },
    { label: "Spending", href: "/spending", icon: "payments", available: true },
    { label: "Income", href: "/income", icon: "trending_up", available: true },
    { label: "Budget", href: "/budget", icon: "account_balance_wallet", available: true },
    { label: "Cash Flow", href: "/cash-flow", icon: "swap_vert", available: true },
    { label: "Commitments", href: "/commitments", icon: "event_repeat", available: true },
    { label: "Goals", href: "/goals", icon: "flag", available: true },
];

const wealthNavigation = [
    { label: "Financial Health", href: "/financial-health", icon: "favorite", available: false },
    { label: "Net Worth", href: "/net-worth", icon: "account_balance", available: false },
    { label: "Investments", href: "/investments", icon: "show_chart", available: false },
    { label: "Liabilities", href: "/liabilities", icon: "credit_card", available: false },
];

interface SidebarProps {
    mobileOpen?: boolean;
    onClose?: () => void;
}

export default function Sidebar({
    mobileOpen = false,
    onClose,
}: SidebarProps) {
    const pathname = usePathname();
    return (
        <aside
            className={[
                mobileOpen ? "flex" : "hidden lg:flex",
                "fixed inset-y-0 left-0 z-50 w-[280px] shrink-0 flex-col",
                "border-r border-white/[0.06] bg-[#0b0d12]",
                "lg:fixed lg:inset-y-0 lg:left-0 lg:z-40 lg:flex lg:h-screen lg:w-[248px]",
            ].join(" ")}
        >
            {/* Brand */}
            <div className="relative flex h-20 shrink-0 items-center border-b border-white/[0.06] px-5">
                <div className="flex items-center gap-3">
                    <div className="flex h-9 w-9 items-center justify-center rounded-xl bg-[#7abcff]/10 ring-1 ring-[#7abcff]/20">
                        <span
                            className="material-symbols-outlined text-[#7abcff]"
                            style={{ fontSize: "20px" }}
                            aria-hidden="true"
                        >
                            auto_awesome
                        </span>
                    </div>

                    <div>
                        <p className="text-[15px] font-semibold tracking-[-0.01em] text-[#e1e2e8]">
                            Finance AI
                        </p>
                        <p className="text-[11px] text-[#8b919b]">
                            Personal CFO
                        </p>
                    </div>

                    {/* Mobile close */}
                    <button
                        type="button"
                        onClick={onClose}
                        aria-label="Close navigation"
                        className="absolute right-4 top-4 flex h-9 w-9 items-center justify-center rounded-xl text-[#8b919b] transition-colors hover:bg-white/[0.05] hover:text-[#e1e2e8] lg:hidden"
                    >
                        <span
                            className="material-symbols-outlined"
                            style={{ fontSize: "21px" }}
                            aria-hidden="true"
                        >
                            close
                        </span>
                    </button>
                </div>
            </div>

            {/* Navigation */}
            <nav className="no-scrollbar flex-1 overflow-y-auto px-3 py-5">
                <div className="space-y-1">
                    {primaryNavigation.map((item) => (
                        <NavItem
                            key={item.href}
                            label={item.label}
                            href={item.href}
                            icon={item.icon}
                            active={isRouteActive(pathname, item.href)}
                            disabled={!item.available}
                            onClick={onClose}
                        />
                    ))}
                </div>

                <div className="my-5 border-t border-white/[0.06]" />

                <div className="space-y-1">
                    {wealthNavigation.map((item) => (
                        <NavItem
                            key={item.href}
                            label={item.label}
                            href={item.href}
                            icon={item.icon}
                            active={isRouteActive(pathname, item.href)}
                            disabled={!item.available}
                            onClick={onClose}
                        />
                    ))}
                </div>

                <div className="my-5 border-t border-white/[0.06]" />

                <div className="space-y-1">
                    <NavItem
                        label="Ask AI"
                        href="/ask"
                        icon="smart_toy"
                        active={isRouteActive(pathname, "/ask")}
                    />

                    <NavItem
                        label="Profile"
                        href="/profile"
                        icon="person"
                        active={isRouteActive(pathname, "/profile")}
                    />
                </div>
            </nav>
        </aside>
    );
}
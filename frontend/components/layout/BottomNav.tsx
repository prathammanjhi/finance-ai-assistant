"use client";

import { usePathname } from "next/navigation";
import NavItem, { isRouteActive } from "./NavItem";

const items = [
    { label: "Home", href: "/", icon: "home", available: true },
    { label: "Insights", href: "/insights", icon: "auto_awesome", available: true },
    { label: "Ask AI", href: "/ask", icon: "smart_toy", available: true },
    { label: "Profile", href: "/profile", icon: "person", available: true },
];

export default function BottomNav() {
    const pathname = usePathname();

    return (
        <nav
            aria-label="Mobile navigation"
            className="fixed inset-x-0 bottom-0 z-50 border-t border-white/[0.06] bg-[#0b0d12]/95 px-2 pb-[env(safe-area-inset-bottom)] pt-2 backdrop-blur-xl lg:hidden"
        >
            <div className="mx-auto flex max-w-md items-center justify-around">
                {items.map((item) => (
                    <NavItem
                        key={item.href}
                        label={item.label}
                        href={item.href}
                        icon={item.icon}
                        active={isRouteActive(pathname, item.href)}
                        disabled={!item.available}
                        collapsed
                    />
                ))}
            </div>
        </nav>
    );
}
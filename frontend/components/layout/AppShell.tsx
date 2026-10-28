"use client";

import { useState } from "react";
import type { ReactNode } from "react";

import Sidebar from "./Sidebar";
import MobileHeader from "./MobileHeader";
import BottomNav from "./BottomNav";

interface AppShellProps {
    children: ReactNode;
}

export default function AppShell({ children }: AppShellProps) {
    const [mobileMenuOpen, setMobileMenuOpen] = useState(false);

    const openMobileMenu = () => {
        setMobileMenuOpen(true);
    };

    const closeMobileMenu = () => {
        setMobileMenuOpen(false);
    };

    return (
        <div className="min-h-screen bg-[#0b0d12] text-[#e1e2e8]">
            <div className="min-h-screen">
                <Sidebar
                    mobileOpen={mobileMenuOpen}
                    onClose={closeMobileMenu}
                />

                {mobileMenuOpen && (
                    <button
                        type="button"
                        aria-label="Close navigation"
                        onClick={closeMobileMenu}
                        className="fixed inset-0 z-40 bg-black/60 backdrop-blur-sm lg:hidden"
                    />
                )}

                <div className="flex min-h-screen min-w-0 flex-col lg:ml-[248px]">
                    <MobileHeader onMenuClick={openMobileMenu} />

                    <main className="min-h-screen flex-1 pb-20 lg:pb-0">
                        <div className="mx-auto w-full max-w-[1600px] px-4 py-5 sm:px-6 lg:px-8 lg:py-7">
                            {children}
                        </div>
                    </main>
                </div>
            </div>

            <BottomNav />
        </div>
    );
}
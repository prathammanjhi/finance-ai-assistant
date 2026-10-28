"use client";

export default function ProfileScreen() {
    return (
        <div className="space-y-8">
            <div>
                <p className="text-xs font-medium uppercase tracking-[0.14em] text-[#8b919b]">
                    Account
                </p>
                <h1 className="mt-2 text-3xl font-medium tracking-[-0.03em] text-[#e1e2e8]">
                    Profile
                </h1>
                <p className="mt-2 text-sm text-[#8b919b]">
                    Manage your account settings and preferences.
                </p>
            </div>

            <div className="rounded-[20px] border border-white/[0.08] bg-[#101419] p-6 shadow-[0_4px_20px_rgba(0,0,0,0.12)]">
                <div className="flex items-center gap-4">
                    <div className="flex h-16 w-16 items-center justify-center rounded-full bg-[#7abcff]/10 ring-1 ring-[#7abcff]/20">
                        <span
                            className="material-symbols-outlined text-[#7abcff]"
                            style={{ fontSize: "32px" }}
                            aria-hidden="true"
                        >
                            person
                        </span>
                    </div>
                    <div>
                        <p className="text-lg font-medium text-[#e1e2e8]">Finance AI User</p>
                        <p className="text-sm text-[#8b919b]">Personal CFO Account</p>
                    </div>
                </div>
            </div>

            <div className="rounded-[20px] p-8 text-center" style={{
                background: "linear-gradient(135deg, rgba(122,188,255,0.06) 0%, rgba(16,20,24,0.95) 100%)",
                border: "1px solid rgba(122,188,255,0.12)",
            }}>
                <p className="text-[15px] text-[#8b919b]">Profile settings coming soon.</p>
                <span className="mt-4 inline-block rounded-full bg-[#7abcff]/10 px-4 py-1.5 text-xs font-medium text-[#7abcff]">
                    Under Development
                </span>
            </div>
        </div>
    );
}


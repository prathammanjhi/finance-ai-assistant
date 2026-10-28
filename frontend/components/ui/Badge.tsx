type BadgeVariant = "default" | "success" | "warning" | "error" | "ai" | "muted";

interface BadgeProps {
  variant?: BadgeVariant;
  /** Optional Material Symbols icon name */
  icon?: string;
  children: React.ReactNode;
  className?: string;
}

const variantStyles: Record<BadgeVariant, string> = {
  default: "bg-white/[0.08] text-[#e1e2e8]",
  success: "bg-[rgba(74,222,128,0.12)] text-[#4ade80]",
  warning: "bg-[rgba(255,202,123,0.12)] text-[#ffca7b]",
  error: "bg-[rgba(255,180,171,0.12)] text-[#ffb4ab]",
  ai: "bg-[rgba(122,188,255,0.12)] text-[#7abcff]",
  muted: "bg-transparent text-[#8b919b]",
};

/**
 * Badge / StatusPill — semantic status chip.
 * Uses JetBrains Mono uppercase for labels (per typography spec).
 */
export function Badge({ variant = "default", icon, children, className = "" }: BadgeProps) {
  return (
    <span
      className={[
        "inline-flex items-center gap-1.5 px-3 py-1 rounded-full",
        "font-mono text-[11px] font-semibold uppercase tracking-[0.06em] leading-4",
        variantStyles[variant],
        className,
      ]
        .filter(Boolean)
        .join(" ")}
    >
      {icon && (
        <span
          className="material-symbols-outlined"
          style={{ fontSize: "14px", lineHeight: 1 }}
          aria-hidden="true"
        >
          {icon}
        </span>
      )}
      {children}
    </span>
  );
}

export type { BadgeProps, BadgeVariant };


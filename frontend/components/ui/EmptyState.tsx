interface EmptyStateProps {
  /** Material Symbols icon name */
  icon?: string;
  title: string;
  description?: string;
  action?: React.ReactNode;
  className?: string;
}

/**
 * EmptyState — shown when a data set is empty.
 * Provides a neutral, calm placeholder with optional CTA.
 */
export function EmptyState({
  icon = "inbox",
  title,
  description,
  action,
  className = "",
}: EmptyStateProps) {
  return (
    <div
      className={`flex flex-col items-center justify-center gap-4 py-12 px-6 text-center ${className}`}
    >
      <span
        className="material-symbols-outlined text-[#8b919b]"
        style={{ fontSize: "48px" }}
        aria-hidden="true"
      >
        {icon}
      </span>
      <div className="space-y-1">
        <p
          className="text-[15px] font-semibold text-[#e1e2e8]"
          style={{ fontFamily: "var(--font-sora, sans-serif)" }}
        >
          {title}
        </p>
        {description && (
          <p className="text-[13px] text-[#8b919b] max-w-xs">{description}</p>
        )}
      </div>
      {action && <div>{action}</div>}
    </div>
  );
}

export type { EmptyStateProps };


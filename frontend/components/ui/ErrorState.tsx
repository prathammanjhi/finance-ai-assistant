interface ErrorStateProps {
  title?: string;
  message?: string;
  onRetry?: () => void;
  className?: string;
}

/**
 * ErrorState — graceful fallback shown on API or data errors.
 * Never surfaces raw error objects to the user.
 */
export function ErrorState({
  title = "Something went wrong",
  message = "We couldn't load your financial data. Please try again.",
  onRetry,
  className = "",
}: ErrorStateProps) {
  return (
    <div
      className={`flex flex-col items-center justify-center gap-4 py-12 px-6 text-center ${className}`}
      role="alert"
    >
      <div className="w-12 h-12 rounded-full bg-[rgba(255,180,171,0.12)] flex items-center justify-center">
        <span
          className="material-symbols-outlined text-[#ffb4ab]"
          style={{ fontSize: "24px" }}
          aria-hidden="true"
        >
          error_outline
        </span>
      </div>
      <div className="space-y-1">
        <p
          className="text-[15px] font-semibold text-[#e1e2e8]"
          style={{ fontFamily: "var(--font-sora, sans-serif)" }}
        >
          {title}
        </p>
        <p className="text-[13px] text-[#8b919b] max-w-xs">{message}</p>
      </div>
      {onRetry && (
        <button
          onClick={onRetry}
          className="mt-1 inline-flex items-center gap-1.5 px-5 py-2 rounded-full text-[13px] font-semibold text-[#7abcff] border border-[#7abcff]/30 hover:bg-[#7abcff]/10 transition-colors"
        >
          <span className="material-symbols-outlined" style={{ fontSize: "16px" }} aria-hidden="true">
            refresh
          </span>
          Try again
        </button>
      )}
    </div>
  );
}

export type { ErrorStateProps };


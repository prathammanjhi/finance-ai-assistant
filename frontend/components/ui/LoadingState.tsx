interface LoadingStateProps {
  /** Number of skeleton rows to show */
  rows?: number;
  className?: string;
}

/** Single shimmer skeleton line */
function Shimmer({ className = "" }: { className?: string }) {
  return (
    <div
      className={`bg-white/[0.06] rounded animate-pulse ${className}`}
      aria-hidden="true"
    />
  );
}

/**
 * LoadingState — skeleton shimmer placeholder while data is loading.
 * Used before Finance Core API data arrives.
 */
export function LoadingState({ rows = 3, className = "" }: LoadingStateProps) {
  return (
    <div
      className={`space-y-3 ${className}`}
      role="status"
      aria-label="Loading…"
    >
      {Array.from({ length: rows }).map((_, i) => (
        <div key={i} className="flex items-center gap-3">
          <Shimmer className="h-10 w-10 rounded-full flex-shrink-0" />
          <div className="flex-1 space-y-2">
            <Shimmer className="h-3.5 w-2/3" />
            <Shimmer className="h-3 w-1/2" />
          </div>
          <Shimmer className="h-4 w-16" />
        </div>
      ))}
    </div>
  );
}

/** Skeleton for a single metric chip */
export function MetricChipSkeleton() {
  return (
    <Shimmer className="h-9 w-36 rounded-full" aria-hidden="true" />
  );
}

/** Skeleton for a bento card block */
export function CardSkeleton({ className = "" }: { className?: string }) {
  return (
    <div
      className={`bg-[#101418] border border-white/[0.06] rounded-2xl p-6 space-y-4 ${className}`}
      role="status"
      aria-label="Loading…"
    >
      <Shimmer className="h-4 w-28" />
      <Shimmer className="h-8 w-1/2" />
      <Shimmer className="h-3 w-3/4" />
    </div>
  );
}

export type { LoadingStateProps };


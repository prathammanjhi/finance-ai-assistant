type ProgressVariant = "default" | "success" | "warning" | "error";

interface ProgressBarProps {
  /** Value 0–100 */
  value: number;
  variant?: ProgressVariant;
  /** Show percentage label */
  showLabel?: boolean;
  /** Custom label override */
  label?: string;
  /** Height of the track in px (default 4) */
  trackHeight?: number;
  className?: string;
}

const trackColor: Record<ProgressVariant, string> = {
  default: "bg-[#7abcff]",
  success: "bg-[#4ade80]",
  warning: "bg-[#ffca7b]",
  error: "bg-[#ffb4ab]",
};

/**
 * ProgressBar — glowing filament progress track.
 * Value is 0–100. Width is CSS-driven via inline style.
 * No JS calculation happens here — value must come from props.
 */
export function ProgressBar({
  value,
  variant = "default",
  showLabel = false,
  label,
  trackHeight = 4,
  className = "",
}: ProgressBarProps) {
  const clampedValue = Math.min(100, Math.max(0, value));
  const displayLabel = label ?? `${clampedValue}%`;

  return (
    <div className={`w-full ${className}`}>
      {showLabel && (
        <div className="flex justify-between mb-1.5">
          <span className="font-mono text-[11px] text-[#8b919b] uppercase tracking-[0.06em]">
            Progress
          </span>
          <span className="font-mono text-[11px] text-[#7abcff] tracking-wide">
            {displayLabel}
          </span>
        </div>
      )}
      <div
        className="w-full bg-white/[0.06] rounded-full overflow-hidden"
        style={{ height: `${trackHeight}px` }}
        role="progressbar"
        aria-valuenow={clampedValue}
        aria-valuemin={0}
        aria-valuemax={100}
      >
        <div
          className={`h-full rounded-full transition-all duration-700 ease-out ${trackColor[variant]}`}
          style={{ width: `${clampedValue}%` }}
        />
      </div>
    </div>
  );
}

export type { ProgressBarProps, ProgressVariant };


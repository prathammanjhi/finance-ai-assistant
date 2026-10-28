import { type HTMLAttributes, forwardRef } from "react";

interface CardProps extends HTMLAttributes<HTMLDivElement> {
  /** Nested sub-panel (Level 2 surface #161a20) instead of Level 1 */
  nested?: boolean;
  /** Apply hover state styling */
  hoverable?: boolean;
  /** Padding size override */
  padding?: "sm" | "md" | "lg" | "none";
}

const paddingMap = {
  none: "",
  sm: "p-4",
  md: "p-5",
  lg: "p-6",
};

/**
 * BentoCard — the standard Level 1 card surface.
 * Uses canvas-surface background with a subtle 0.5px border.
 * For AI-generated content surfaces, use AIGlassCard instead.
 */
const Card = forwardRef<HTMLDivElement, CardProps>(
  ({ nested = false, hoverable = false, padding = "lg", className = "", children, ...props }, ref) => {
    const base = nested
      ? "bg-[#161a20]"
      : "bg-[#101418]";

    const hover = hoverable
      ? "hover:bg-[#14181e] transition-colors duration-200 cursor-pointer"
      : "";

    const pad = paddingMap[padding];

    return (
      <div
        ref={ref}
        className={[
          base,
          "border border-white/[0.06] rounded-2xl",
          pad,
          hover,
          className,
        ]
          .filter(Boolean)
          .join(" ")}
        {...props}
      >
        {children}
      </div>
    );
  }
);

Card.displayName = "Card";

export { Card };
export type { CardProps };


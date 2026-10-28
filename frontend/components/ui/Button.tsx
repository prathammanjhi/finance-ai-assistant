import { type ButtonHTMLAttributes, forwardRef } from "react";

type ButtonVariant = "primary" | "secondary" | "ghost" | "danger";
type ButtonSize = "sm" | "md" | "lg";

interface ButtonProps extends ButtonHTMLAttributes<HTMLButtonElement> {
  variant?: ButtonVariant;
  size?: ButtonSize;
  /** Render as a full-width block */
  fullWidth?: boolean;
  /** Optional trailing icon (Material Symbols name) */
  trailingIcon?: string;
  /** Optional leading icon (Material Symbols name) */
  leadingIcon?: string;
}

const variantStyles: Record<ButtonVariant, string> = {
  /** Cyan pill — hero action only */
  primary:
    "bg-[#7abcff] text-[#0b0d12] font-bold hover:bg-[#9bcbff] active:bg-[#7abcff] transition-colors",
  /** Transparent with border — secondary actions */
  secondary:
    "bg-transparent border border-white/20 text-[#e1e2e8] hover:border-white/30 hover:bg-white/5 transition-all",
  /** No border — low-priority navigation */
  ghost:
    "bg-transparent text-[#8b919b] hover:text-[#e1e2e8] hover:bg-white/5 transition-all",
  /** Error / destructive */
  danger:
    "bg-[#ffb4ab]/10 text-[#ffb4ab] border border-[#ffb4ab]/20 hover:bg-[#ffb4ab]/20 transition-all",
};

const sizeStyles: Record<ButtonSize, string> = {
  sm: "py-1.5 px-4 text-[13px]",
  md: "py-2.5 px-5 text-[14px]",
  lg: "py-3 px-7 text-[15px]",
};

/**
 * Button — Finance AI canonical button primitives.
 * Primary = cyan pill (one hero action per view).
 * Secondary = transparent bordered.
 * Ghost = no border, muted text.
 */
const Button = forwardRef<HTMLButtonElement, ButtonProps>(
  (
    {
      variant = "secondary",
      size = "md",
      fullWidth = false,
      leadingIcon,
      trailingIcon,
      className = "",
      children,
      ...props
    },
    ref
  ) => {
    return (
      <button
        ref={ref}
        className={[
          "inline-flex items-center justify-center gap-2 rounded-full font-semibold",
          "disabled:opacity-40 disabled:cursor-not-allowed",
          "focus-visible:outline focus-visible:outline-2 focus-visible:outline-[#7abcff] focus-visible:outline-offset-2",
          variantStyles[variant],
          sizeStyles[size],
          fullWidth ? "w-full" : "",
          className,
        ]
          .filter(Boolean)
          .join(" ")}
        {...props}
      >
        {leadingIcon && (
          <span
            className="material-symbols-outlined"
            style={{ fontSize: "18px", lineHeight: 1 }}
            aria-hidden="true"
          >
            {leadingIcon}
          </span>
        )}
        {children}
        {trailingIcon && (
          <span
            className="material-symbols-outlined"
            style={{ fontSize: "18px", lineHeight: 1 }}
            aria-hidden="true"
          >
            {trailingIcon}
          </span>
        )}
      </button>
    );
  }
);

Button.displayName = "Button";

export { Button };
export type { ButtonProps, ButtonVariant, ButtonSize };


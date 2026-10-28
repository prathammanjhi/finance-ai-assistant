"use client";

import Link from "next/link";
import { usePathname } from "next/navigation";

export function isRouteActive(pathname: string | null, href: string): boolean {
  if (!pathname) return false;
  const cleanPath = pathname.replace(/\/+$/, "") || "/";
  const cleanHref = href.replace(/\/+$/, "") || "/";

  if (cleanHref === "/") {
    return cleanPath === "/";
  }

  if (cleanHref === "/cash-flow") {
    return (
      cleanPath === "/cash-flow" ||
      cleanPath === "/cashflow" ||
      cleanPath.startsWith("/cash-flow/") ||
      cleanPath.startsWith("/cashflow/")
    );
  }

  if (cleanHref === "/ask") {
    return (
      cleanPath === "/ask" ||
      cleanPath === "/ask-ai" ||
      cleanPath.startsWith("/ask/") ||
      cleanPath.startsWith("/ask-ai/")
    );
  }

  return cleanPath === cleanHref || cleanPath.startsWith(`${cleanHref}/`);
}

interface NavItemProps {
  label: string;
  href: string;
  icon: string;
  active?: boolean;
  collapsed?: boolean;
  disabled?: boolean;
  onClick?: () => void;
}

export default function NavItem({
  label,
  href,
  icon,
  active,
  collapsed = false,
  disabled = false,
  onClick,
}: NavItemProps) {
  const pathname = usePathname();
  const isItemActive = active !== undefined ? active : isRouteActive(pathname, href);

  const className = [
    "group flex items-center gap-3 rounded-xl px-3 py-2.5",
    "text-sm font-medium transition-all duration-200",
    isItemActive
      ? "bg-white/[0.08] text-[#e1e2e8]"
      : disabled
        ? "cursor-not-allowed text-[#555b65]"
        : "text-[#8b919b] hover:bg-white/[0.04] hover:text-[#e1e2e8]",
    collapsed ? "justify-center" : "",
  ]
    .filter(Boolean)
    .join(" ");

  const content = (
    <>
      <span
        className={[
          "material-symbols-outlined shrink-0",
          isItemActive
            ? "text-[#7abcff]"
            : disabled
              ? "text-[#555b65]"
              : "text-[#8b919b]",
        ].join(" ")}
        style={{
          fontSize: "20px",
          lineHeight: 1,
        }}
        aria-hidden="true"
      >
        {icon}
      </span>

      {!collapsed && <span className="truncate">{label}</span>}
    </>
  );

  if (disabled) {
    return (
      <div
        aria-disabled="true"
        title={collapsed ? `${label} — coming soon` : undefined}
        className={className}
      >
        {content}
      </div>
    );
  }

  return (
    <Link
      href={href}
      aria-current={isItemActive ? "page" : undefined}
      onClick={onClick}
      title={collapsed ? label : undefined}
      className={className}
    >
      {content}
    </Link>
  );
}
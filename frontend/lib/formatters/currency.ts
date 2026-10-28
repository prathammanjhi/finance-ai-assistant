/**
 * Shared Indian Rupee (INR) currency presentation formatter.
 * Formats numbers into standard localized currency strings (e.g. ₹45,000).
 */
export function formatCurrency(value: number): string {
  if (!Number.isFinite(value)) {
    return "₹0";
  }
  return new Intl.NumberFormat("en-IN", {
    style: "currency",
    currency: "INR",
    maximumFractionDigits: 0,
  }).format(value);
}

export const formatINR = formatCurrency;


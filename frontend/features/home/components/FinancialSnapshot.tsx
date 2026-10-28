import { Card } from "@/components/ui/Card";

interface FinancialSnapshotProps {
  netPosition: string;
  cashPosition: string;
  financialHealth: number;
}

export default function FinancialSnapshot({
  netPosition,
  cashPosition,
  financialHealth,
}: FinancialSnapshotProps) {
  const metrics = [
    {
      label: "Net Position",
      value: netPosition,
      icon: "account_balance_wallet",
    },
    {
      label: "Cash Position",
      value: cashPosition,
      icon: "payments",
    },
    {
      label: "Financial Health",
      value: `${financialHealth}/100`,
      icon: "favorite",
    },
  ];

  return (
    <section aria-labelledby="financial-snapshot-heading">
      <div className="mb-3 flex items-center justify-between">
        <h2
          id="financial-snapshot-heading"
          className="text-sm font-medium text-[#e1e2e8]"
        >
          Financial Snapshot
        </h2>

        <span className="text-xs text-[#8b919b]">
          This month
        </span>
      </div>

      <div className="grid grid-cols-1 gap-3 sm:grid-cols-3">
        {metrics.map((metric) => (
          <Card key={metric.label} padding="md">
            <div className="flex items-start justify-between">
              <div>
                <p className="text-xs font-medium uppercase tracking-[0.08em] text-[#8b919b]">
                  {metric.label}
                </p>

                <p className="mt-3 text-2xl font-semibold tracking-[-0.03em] text-[#e1e2e8]">
                  {metric.value}
                </p>
              </div>

              <div className="flex h-9 w-9 items-center justify-center rounded-xl bg-[#7abcff]/10">
                <span
                  className="material-symbols-outlined text-[#7abcff]"
                  style={{ fontSize: "19px" }}
                  aria-hidden="true"
                >
                  {metric.icon}
                </span>
              </div>
            </div>
          </Card>
        ))}
      </div>
    </section>
  );
}
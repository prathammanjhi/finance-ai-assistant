import type {
  AvailablePeriod,
  FinanceData,
} from "@/types/finance";

const API_BASE_URL = "http://localhost:8000";

async function fetchJSON<T>(url: string): Promise<T> {
  const response = await fetch(url);

  if (!response.ok) {
    let message = "Something went wrong.";

    try {
      const body = await response.json();
      message = body.detail ?? message;
    } catch {
      // Keep default message.
    }

    throw new Error(message);
  }

  return response.json();
}

export async function getAvailablePeriods(): Promise<AvailablePeriod[]> {
  const data = await fetchJSON<{
    periods: AvailablePeriod[];
  }>(`${API_BASE_URL}/api/finance/available-periods`);

  return data.periods;
}

export async function getFinance(
  month: number,
  year: number
): Promise<FinanceData> {
  return fetchJSON<FinanceData>(
    `${API_BASE_URL}/api/finance?month=${month}&year=${year}`
  );
}
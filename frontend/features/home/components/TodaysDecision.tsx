export default function TodaysDecision() {
    return (
        <section className="w-full">
            <h2 className="mb-3 text-[18px] font-medium leading-[26px] text-[#1C1B1B]">
                Today&apos;s Decision
            </h2>

            <article className="rounded-[16px] bg-white p-5 shadow-[0_4px_10px_rgba(0,0,0,0.04)]">
                <h3 className="text-[17px] font-semibold leading-[26px] text-[#461599]">
                    Delay Swiggy today
                </h3>

                <p className="mt-4 max-w-[300px] text-[15px] leading-[22px] text-[#494453]">
                    You&apos;ll save ₹420 and reach your Goa goal 2 days earlier.
                </p>

                <button
                    type="button"
                    className="mt-4 text-[14px] font-medium text-[#461599]"
                >
                    See why →
                </button>
            </article>
        </section>
    );
}
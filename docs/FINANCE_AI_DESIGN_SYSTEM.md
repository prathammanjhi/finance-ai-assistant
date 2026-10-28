# Finance AI — Canonical Design System & Frontend Architecture Specification

**Document Version:** 2.0.0-REVISED  
**Product:** Finance AI — Autonomous AI-First Personal CFO  
**Status:** Approved Specification  
**Target File:** `docs/FINANCE_AI_DESIGN_SYSTEM.md`  

---

## 1. Foundational Design Principles & Constraints

### 1.1 Core Design Principle: Unify the Design Language, Not the Page Layouts
> **"Unify the design language, not the page layouts."**
>
> Finance AI is not a generic template where every view is forced into an identical grid. Each financial domain—Home, Cash Flow, Spending, Commitments, Budget, Goals, Investments, Liabilities, Net Worth, Financial Health—addresses fundamentally different financial questions and requires tailored compositional architecture. However, every page must feel unmistakably like the exact same product through unified surface physics, consistent typography, shared brand assets, identical border treatments, and standardized AI visual language.

### 1.2 Density Principle: Stitch is the Visual Reference, Not the Density Target
> **"Stitch is the visual reference, not the density target."**
>
> The raw Stitch screens were individually generated and frequently compressed content to fit single screen captures. The production Finance AI application must be significantly more **spacious, breathable, and calm**:
> - **Generous Vertical Breathing Room:** Section spacing expands from cramped 24px/32px to a comfortable `48px`–`64px` on desktop and `32px`–`40px` on mobile.
> - **Comfortable Touch Targets:** All interactive elements maintain a minimum hit area of `44px`–`48px`.
> - **Generous Card Padding:** Card interiors use `24px`–`32px` on desktop (`16px`–`20px` on mobile) to let key figures stand out.
> - **Uncrowded Data Visualization:** Charts, donut rings, and progress tracks have dedicated breathing room rather than being squeezed into tiny card corners.
> - **Clarity Over Compression:** Never cram metrics onto a single screen simply because space exists. Information hierarchy must guide the user's eye directly to what matters.

### 1.3 Architectural Invariant: Strict Calculation Pipeline
$$\text{Reader} \longrightarrow \text{Filter} \longrightarrow \text{Calculation} \longrightarrow \text{Decision} \longrightarrow \text{Insight} \longrightarrow \text{API} \longrightarrow \text{UI}$$

- **Finance Core is the Sole Source of Truth:** All financial arithmetic, debt ratios, coverage months, net worth balances, budget utilization percentages, health scores, and rule evaluations reside exclusively in Python (`src/core/`).
- **Zero Frontend Math:** The frontend is strictly a presentation and interaction layer. It never computes or recalculates financial metrics. It accepts typed JSON contracts from the API and renders them.
- **Pure Presentation Formatting:** The frontend is only permitted to format values for display (e.g., currency formatting via `formatINR()`, relative date strings, and percentage formatting).

### 1.4 Frontend Migration Philosophy: Repair & Evolve, Do Not Discard
- The existing Next.js frontend code (`HomeScreen.tsx`, `TodaysDecision.tsx`, `OpportunityCard.tsx`, `Greeting.tsx`, and `app/layout.tsx`) is treated as valuable initial scaffolding.
- Existing components will be **migrated, restyled, and repaired** to meet this specification rather than being deleted or rebuilt from scratch.
- Structural layout and established behavior will be preserved; styling, typography classes, colors, and data bindings will be elevated to the canonical Obsidian Glass standard.

---

## 2. Design Observations vs. Design Decisions Matrix

To ensure accidental artifact generation from Stitch is never mistaken for deliberate product design, every major design dimension is analyzed through three distinct lenses:
1. **Observed in Stitch:** What the raw reference screens did.
2. **Inferred Canonical Pattern:** The underlying design intent across the collection.
3. **Explicit Engineering / Product Decision:** The justified, permanent specification for Finance AI.

| Dimension | A. Observed in Stitch | B. Inferred Canonical Pattern | C. Explicit Engineering & Product Decision |
| :--- | :--- | :--- | :--- |
| **Brand Identity** | Header on `profile/code.html` used `"Aura Finance"`; `investments_analysis` used an `"FA"` avatar; others used `"Finance AI"`. | The product is unequivocally **Finance AI**. `"Aura Finance"` was an accidental generation hallucination. | **Normalize to "Finance AI" everywhere.** Sub-brand role is **"AI CFO"**. Eradicate all instances of "Aura". Use `"FA"` solely as a compact monogram avatar on mobile headers where horizontal width is constrained. |
| **Brand Logo & Icon** | Home used `bubble_chart` icon; Financial Health used `query_stats`; Ask CFO used `smart_toy`; Onboarding used an animated glowing orb. | The product uses a geometric, molecular cluster icon representing connected financial nodes, with an energetic glowing orb representing the autonomous AI agent. | **Primary Logomark:** `bubble_chart` in `#7ABCFF` (Electric Cyan).<br>**Agent Presence:** Animated glowing orb (`ai-orb`) reserved for AI chat headers, decision hero cards, and onboarding moments. |
| **Canvas Background** | Multiple conflicting hex codes: `#0B0D12` (Base Obsidian), `#0B0E12`, `#101418` (Surface), and CSS variables. | A unified dark-mode-first deep space aesthetic with no pure pitch black (`#000000`) and no generic grey. | **Canvas Base is strictly `#0B0D12`**. Cards use `#101418` (Level 1) and `#161A20` (Level 2). This provides warm depth without ocular fatigue or harsh OLED clipping. |
| **Glassmorphism & AI Styling** | 4 different CSS implementations: (1) `::before` pseudo-element with masks; (2) `border-image` gradient; (3) `background-clip` double-gradient; (4) plain box-shadows. | Glassmorphism is **not** a general decorative style; it is strictly an **AI indicator**. Machine-generated insights look visually distinct from static human ledgers. | **Standardize on one robust CSS utility: `.ai-glass-surface`**. Uses `backdrop-filter: blur(20px)` and a subtle double-gradient stroke (`rgba(122,188,255,0.3)` to transparent). Restrict glassmorphism exclusively to AI insight surfaces and floating toolbars. |
| **Typography Scale** | Inconsistent font sizes: display hero balances varied between 80px, 64px, and 48px; labels varied between 10px and 12px; some files used uppercase classes, others lowercase. | Strict 3-tier hierarchy: **Sora** for headlines, **Hanken Grotesk** for readable body and numbers, **JetBrains Mono** for technical micro-data. | **Enforce exact font roles:**<br>1. `font-sora`: Display hero (72px), Page titles (28px), Section titles (20px).<br>2. `font-hanken`: Body copy (15px/16px), Conversational narrative, Financial values.<br>3. `font-mono`: Overline labels (11px uppercase, tracking +0.06em), Progress tags, Tickers. |
| **Primary Navigation** | Desktop headers varied between uppercase (`HOME`, `INSIGHTS`), sentence case (`Home`, `Insights`), icon+text, and hamburger menus on `ask_cfo`. | A clean persistent dual-tier navigation: desktop top navigation with subtle active indicators; mobile fixed bottom 5-tab bar. | **Eliminate hamburger menus completely** (the 5-tab bottom bar covers top-level navigation). Standardize desktop nav to **Sentence Case** (`Home`, `Insights`, `Ask AI`, `Goals`, `Profile`) with cyan filament underline indicator. |
| **First-Class Domain Navigation** | Stitch generated dedicated full screens for Spending, Budget, Income, Cash Flow, Commitments, Health, Net Worth, Investments, Liabilities, but lacked a cohesive routing model. | These 9 financial domains are deep, first-class analytical dashboards, not temporary popup modals or discarded drill-downs. | **Establish 14 first-class routes.** The 5 primary tabs anchor the user; contextual links from Home cards, Insights deep-dives, and domain badges seamlessly route users to these 9 full domain pages. |
| **Corner Radii** | Random mix of `0.25rem`, `0.5rem`, `0.75rem`, `1rem`, `1.5rem`, and `9999px` across similar cards. | A deliberate geometric nesting system where outer cards are softer and inner elements are crisper. | **Explicit Radii System:**<br>- Outer Cards: `16px` (`rounded-2xl`)<br>- Nested Sub-panels: `12px` (`rounded-xl`)<br>- Small Tags / Inputs: `8px` (`rounded-lg`)<br>- Buttons, Chips & Pills: `9999px` (`rounded-full`) |
| **Information Density** | Many Stitch cards were compressed into tight 12px gaps with tiny 12px padding to fit into single viewport mockups. | Stitch was illustrating visual tone, not ergonomic spacing for long-term daily personal finance usage. | **Apply Density Principle:** Expand bento gaps to `16px`, card padding to `24px`–`32px`, and section separation to `48px`–`64px`. Make charts legible and touch targets spacious. |

---

## 3. The 4-Tier System Separation

To prevent styling, narrative composition, data structures, and transport mechanisms from becoming entangled, the frontend is divided into four strictly isolated tiers:

```
┌─────────────────────────────────────────────────────────────┐
│ Tier 1: Shared Design System (Design Tokens & Primitives)   │
│ Atoms, colors, typography, surfaces, buttons, icons, chips │
├─────────────────────────────────────────────────────────────┤
│ Tier 2: Page-Specific Composition (Domain Layouts)          │
│ Home, Spending, Goals, Ask AI, Health, Investments, etc.    │
├─────────────────────────────────────────────────────────────┤
│ Tier 3: Financial Data Contracts (TypeScript Snapshot Types)│
│ Immutable interfaces mirroring Python Finance Core output   │
├─────────────────────────────────────────────────────────────┤
│ Tier 4: API & Client Transport Layer                        │
│ Next.js server actions, HTTP client, caching, error states  │
└─────────────────────────────────────────────────────────────┘
```

1. **Tier 1: Shared Design System:** Pure presentation primitives. Agnostic to financial domain logic. (e.g., `BentoCard`, `AIGlassCard`, `HealthGauge`, `StatusPill`, `ProgressBar`, `AppHeader`, `BottomNav`).
2. **Tier 2: Page-Specific Composition:** Assembles Tier 1 primitives into a unique visual narrative appropriate for that specific financial domain.
3. **Tier 3: Financial Data Contracts:** Pure TypeScript declarations (`types/finance.ts`) that strictly define the shape of incoming snapshots from `src/core/engine.py:analyze_finances()`.
4. **Tier 4: API & Client Transport Layer:** Handles HTTP communication with the Python backend, SWR/React Query caching, loading skeletons, and fallback states.

---

## 4. Canonical Brand & Design Tokens

### 4.1 Surface Physics & Color Palette ("Obsidian Glass")

```css
/* ==========================================================================
   Level 0: Infinite Canvas Background
   ========================================================================== */
--canvas-base: #0B0D12;              /* Primary background void */
--canvas-surface: #101418;           /* Standard Level 1 Bento Card Surface */
--canvas-surface-hover: #14181E;     /* Interactive Card Hover State */
--canvas-nested: #161A20;            /* Level 2 Sub-panel / Row Surface */
--canvas-floating: rgba(16, 20, 24, 0.85); /* Sticky headers / floating bars */

/* ==========================================================================
   Borders & Edge Lighting
   ========================================================================== */
--border-subtle: rgba(255, 255, 255, 0.06);  /* 0.5px - 1px perimeter border */
--border-medium: rgba(255, 255, 255, 0.10);  /* Card separation stroke */
--border-light: rgba(255, 255, 255, 0.16);   /* Interactive focus / active card */

/* ==========================================================================
   Primary AI Filament Accents
   ========================================================================== */
--accent-cyan: #7ABCFF;             /* Primary hero accent & AI filament */
--accent-cyan-hover: #9BCBFF;       /* CTA hover state */
--accent-cyan-soft: rgba(122, 188, 255, 0.12); /* Subtle badge background */
--accent-cyan-glow: rgba(122, 188, 255, 0.35); /* Ambient glow filter */

/* ==========================================================================
   Semantic Financial Health Accents
   ========================================================================== */
--finance-success: #4ADE80;          /* Surplus, under budget, positive cash flow */
--finance-success-soft: rgba(74, 222, 128, 0.12);
--finance-warning: #FFCA7B;          /* Budget caution, high liability ratio */
--finance-warning-soft: rgba(255, 202, 123, 0.12);
--finance-error: #FFB4AB;            /* Over budget, critical deficit, debt risk */
--finance-error-soft: rgba(255, 180, 171, 0.12);

/* ==========================================================================
   Typography Color Scale
   ========================================================================== */
--text-primary: #E1E2E8;            /* 95% contrast: Headlines, primary data */
--text-secondary: #C1C7D1;          /* 75% contrast: Body text, narrative */
--text-muted: #8B919B;              /* 50% contrast: Labels, timestamps, borders */
--text-filament: #7ABCFF;           /* Highlighted currency, AI emphasis */
```

### 4.2 The Canonical AI Glass Utility
```css
.ai-glass-surface {
  background: rgba(255, 255, 255, 0.035);
  backdrop-filter: blur(20px);
  -webkit-backdrop-filter: blur(20px);
  border: 1px solid transparent;
  background-image: 
    linear-gradient(#101418, #101418), 
    linear-gradient(135deg, rgba(122, 188, 255, 0.35) 0%, rgba(255, 255, 255, 0.05) 50%, transparent 100%);
  background-origin: border-box;
  background-clip: padding-box, border-box;
}

.ai-pulse-ambient {
  animation: pulse-ambient-glow 4s ease-in-out infinite alternate;
}

@keyframes pulse-ambient-glow {
  0% { box-shadow: 0 0 20px rgba(122, 188, 255, 0.04); }
  100% { box-shadow: 0 0 35px rgba(122, 188, 255, 0.16); }
}
```

---

## 5. Typography Scale & Application Guidelines

| Style Token | Font Family | Size | Line Height | Weight | Tracking | Purpose |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| `font-display-hero` | Sora | `72px` (`4.5rem`) | `80px` | 700 | `-0.04em` | Major Health Score (82), Net Worth total |
| `font-display-stat` | Sora | `40px` (`2.5rem`) | `48px` | 700 | `-0.03em` | Primary balance, monthly spend total |
| `font-headline-lg` | Sora | `28px` (`1.75rem`) | `36px` | 700 | `-0.03em` | Screen headers, hero greeting |
| `font-headline-md` | Sora | `20px` (`1.25rem`) | `28px` | 600 | `-0.02em` | Card titles, category headers, modal titles |
| `font-headline-sm` | Sora | `16px` (`1.0rem`) | `24px` | 600 | `-0.01em` | Nested bento subheaders |
| `font-body-lg` | Hanken Grotesk | `18px` (`1.125rem`) | `28px` | 500 | `-0.01em` | AI decision summary, featured insight |
| `font-body-md` | Hanken Grotesk | `15px` (`0.9375rem`)| `22px` | 400 | `-0.01em` | Standard descriptions, chat bubbles, list rows |
| `font-body-sm` | Hanken Grotesk | `13px` (`0.8125rem`)| `18px` | 400 | `0` | Secondary descriptions, tooltips |
| `font-label-mono` | JetBrains Mono | `11px` (`0.6875rem`)| `16px` | 600 | `+0.06em` | **UPPERCASE**: Section overlines, chips, badges |
| `font-data-mono` | JetBrains Mono | `13px` (`0.8125rem`)| `18px` | 500 | `0` | Percentages, timestamps, transaction tags |

---

## 6. Core Product Interaction Patterns

### 6.1 Core Pattern 1: The Hero AI Decision Pattern
Every financial view must prioritize **one clear decision and one clear action** before displaying data tables:
- **Location:** Top of `/` (Home) and featured prominently in `/insights`.
- **Card Styling:** `.ai-glass-surface` with `.ai-pulse-ambient`.
- **Anatomy:**
  1. *Category / AI Badge:* `smart_toy` icon + `AI DECISION` in `font-label-mono` (`#7ABCFF`).
  2. *Actionable Imperative Headline:* `"Bhai, Swiggy ko aaj skip kar."` (Sora 24px/28px).
  3. *Clear Trade-off Narrative:* `"You've already spent ₹1,240 on food this week. Skip today → ₹420 saved toward your Goa Trip."` (Hanken Grotesk 15px).
  4. *Direct Action CTA:* Pill button `#7ABCFF` (`rounded-full`, text `#0B0D12`, bold 14px) with arrow icon: `"Skip & Save →"`.

### 6.2 Core Pattern 2: Embedded Calculation Cards in Ask AI (`/ask`)
When the user converses with their AI CFO, the response must never be mere textual chatter. It must visibly substantiate its advice with a structured calculation sub-card:
- **Location:** Inside `AIMessageCard` on `/ask`.
- **Anatomy:**
  1. *Narrative Response:* `"Bhai, technically afford kar sakta hai, but let's check your upcoming commitments before booking."`
  2. *Embedded Calculation Card (Level 2 Surface `#161A20`):*
     - `Current Balance`: `₹51,000` (Cyan)
     - `Upcoming Commitments (15d)`: `-₹18,400` (Red)
     - `Safe Cash Remaining`: `₹32,600` (Text Primary)
  3. *Final Actionable Advice:* `"₹45,000 ka trip abhi cash flow ko tight karega. Diwali ke baad plan kar to balance safe rahega."`

### 6.3 Core Pattern 3: Story-Swipe Insight Carousel
- **Location:** `/insights` hero section and expandable from Home.
- **Behavior:** Instagram/Snapchat-style horizontal snap-scroll cards with segmented progress bar indicators at the top.
- **Purpose:** Allows the user to flick through bite-sized, high-signal financial discoveries (e.g. *Weekend Spike Detected*, *Recurring Subscription Anomaly*, *Goal Milestone Reached*).

### 6.4 Core Pattern 4: Conic Health Score Gauge
- **Location:** Featured on `/` (Home) and `/financial-health`.
- **Structure:** SVG or CSS conic-gradient circular meter (240px on desktop, 180px on mobile) with glowing cyan track, large center score numeral (0–100), and monospaced grade badge (`A+` to `F`). Includes smooth count-up animation.

---

## 7. Complete Product Route Architecture (14 Routes)

The product architecture provides **5 primary navigation tabs** supplemented by **9 first-class financial domain pages**. These 9 pages are full-fledged analytical destinations with dedicated URLs, breadcrumb navigation, and deep-linking capabilities.

```
                     ┌─────────────────────────────────────────┐
                     │          Primary Navigation             │
                     │  Home  |  Insights  |  Ask  |  Goals    │
                     └────────────────────┬────────────────────┘
                                          │
            ┌─────────────────────────────┴─────────────────────────────┐
            ▼                                                           ▼
┌───────────────────────┐                                   ┌───────────────────────┐
│ Cash & Spending Flow  │                                   │ Wealth & Balance Sheet│
│ ├─ /spending          │                                   │ ├─ /financial-health  │
│ ├─ /income            │                                   │ ├─ /net-worth         │
│ ├─ /budget            │                                   │ ├─ /investments       │
│ ├─ /cash-flow         │                                   │ └─ /liabilities       │
│ └─ /commitments       │                                   │                       │
└───────────────────────┘                                   └───────────────────────┘
```

### 7.1 The 5 Primary Navigation Tabs (Persistent)

| Route | Path | Icon | Purpose & Core Content |
| :--- | :--- | :--- | :--- |
| **Home** | `/` | `grid_view` | The Executive Summary. Hero AI Decision card, Health Score Ring preview, Context metric chips, Active Goals mini-carousel, and Recent Activity snippet. |
| **Insights** | `/insights` | `insights` | Story-Swipe carousel, deep-dive category anomaly cards, budget pacing forecasts, and prioritized recommendations from Finance Core. |
| **Ask AI** | `/ask` | `smart_toy` | Conversational AI CFO interface. Natural language queries, suggested scenario pills, and embedded mathematical verification cards. |
| **Goals** | `/goals` | `track_changes` | Portfolio goals overview, total target vs. current amount, days remaining, required monthly savings, and "New Goal" configuration sheet. |
| **Profile** | `/profile` | `person` | User financial profile, connected Excel data source status, AI tone preferences (Hinglish vs. English), export reports, and settings. |

### 7.2 The 9 First-Class Financial Domain Pages

| Domain Route | Path | Ingress Points | Unique Composition & Visual Focus |
| :--- | :--- | :--- | :--- |
| **Spending** | `/spending` | Home spend chip, Insights anomalies | Donut expense allocation chart (Need vs. Want vs. Category), category ranking list, transaction search and filter. |
| **Income** | `/income` | Home cash chip, Cash flow view | Received vs. pending income cards, active income source breakdown, salary credit cadence, and stability rating. |
| **Budget** | `/budget` | Home quick stats, Insights alerts | Monthly budget utilization bar, category caps, daily burn velocity, and days-remaining countdown. |
| **Cash Flow** | `/cash-flow` | Home header, Income view | Inflow vs. outflow comparison bars, net cash position, expected cash trajectory, and liquidity runway. |
| **Commitments** | `/commitments` | Ask CFO math cards, Home alerts | Upcoming 15-day liabilities/rent/EMIs schedule, "Available After Commitments" summary chip, and active commitment status tags. |
| **Financial Health** | `/financial-health` | Home Health Gauge click | Hero 240px Score Gauge, grade (`A+` to `F`), risk classification, and the **10-Pillar Breakdown Grid** mapping directly to Core's `financial_health_summary`. |
| **Net Worth** | `/net-worth` | Profile summary, Investments view | Assets vs. Liabilities balance sheet, Asset Coverage Ratio, debt-free percentage, and wealth tier classification. |
| **Investments** | `/investments` | Net Worth view, Insights | Total invested vs. current market value, portfolio return %, asset class breakdown (Mutual Funds, Stocks, Gold, Crypto), and performance glow chart. |
| **Liabilities** | `/liabilities` | Commitments view, Net Worth | Total debt load, largest monthly EMI, Debt-to-Asset ratio, loan repayment progress bars, and payoff priority recommendations. |

---

## 8. Existing Component Migration Plan

Rather than discarding existing code, the current Next.js components in `frontend/` will be systematically repaired and elevated:

### 8.1 Component Migration Mapping

| Current File in `frontend/` | Migration Action | Preserved Logic & Upgrades |
| :--- | :--- | :--- |
| `app/globals.css` | **Full Theme Overhaul** | Replace light-mode purple tokens (`#fbfbf9`, `#461599`) with canonical Obsidian Glass variables (`#0B0D12`, `#7ABCFF`), font declarations, and `.ai-glass-surface` rules. |
| `app/layout.tsx` | **Upgrade Fonts & Theme** | Add Google Fonts loader for **Sora**, **Hanken Grotesk**, and **JetBrains Mono**. Bind dark class to `<html>`. |
| `components/home/greeting.tsx` | **Repair & Clean** | Strip Figma node tags (`data-node-id`). Adopt `font-headline-lg` (Sora) for greeting and `font-body-md` (Hanken Grotesk) for subtitle. Dynamically format date. |
| `features/home/components/OpportunityCard.tsx` | **Upgrade to AI Surface** | Retain background shader concept (`opportunity-shader.png`). Upgrade card background to `.ai-glass-surface` with cyan filament accent. Replace button with canonical pill CTA. |
| `features/home/components/TodaysDecision.tsx` | **Upgrade to Hero Decision Pattern** | Preserve the core text narrative ("Delay Swiggy today... save ₹420 and reach Goa goal 2 days earlier"). Restyle into the canonical **Hero AI Decision Card** with `.ai-pulse-ambient`. |
| `features/home/HomeScreen.tsx` | **Expand to Spacious Layout** | Retain as top-level Home coordinator. Incorporate generous spacing, `HealthScoreRing` preview, `QuickStatChips`, and `GoalsMiniCarousel`. |

---

## 9. Recommended Frontend Architecture & File Structure

```
frontend/
├── app/
│   ├── layout.tsx                     # Root layout: Sora, Hanken, JetBrains Mono loaders
│   ├── globals.css                    # Tailwind v4 import + Canonical Obsidian Glass tokens
│   │
│   │── (primary-tabs)                 # The 5 Persistent Tabs
│   ├── page.tsx                       # / (Home Tab)
│   ├── insights/
│   │   └── page.tsx                   # /insights (Insights Tab)
│   ├── ask/
│   │   └── page.tsx                   # /ask (Ask AI Tab)
│   ├── goals/
│   │   └── page.tsx                   # /goals (Goals Tab)
│   ├── profile/
│   │   └── page.tsx                   # /profile (Profile Tab)
│   │
│   │── (first-class-domains)          # The 9 Dedicated Financial Domain Pages
│   ├── spending/
│   │   └── page.tsx                   # /spending (Spending Analysis)
│   ├── income/
│   │   └── page.tsx                   # /income (Income Analysis)
│   ├── budget/
│   │   └── page.tsx                   # /budget (Budget Tracking)
│   ├── cash-flow/
│   │   └── page.tsx                   # /cash-flow (Cash Flow Analysis)
│   ├── commitments/
│   │   └── page.tsx                   # /commitments (Financial Commitments)
│   ├── financial-health/
│   │   └── page.tsx                   # /financial-health (10-Pillar Health Audit)
│   ├── net-worth/
│   │   └── page.tsx                   # /net-worth (Net Worth & Leverage)
│   ├── investments/
│   │   └── page.tsx                   # /investments (Investment Portfolio)
│   └── liabilities/
│       └── page.tsx                   # /liabilities (Liabilities & Debt Payoff)
│
├── components/
│   ├── shared/                        # Tier 1: Shared Design System Primitives
│   │   ├── AppHeader.tsx              # Sticky header (Brand, Nav links, Notifications)
│   │   ├── BottomNav.tsx              # Mobile 5-tab sticky bottom navigation
│   │   ├── BentoCard.tsx              # Level 1 card surface with 0.5px subtle border
│   │   ├── AIGlassCard.tsx            # Level 2 AI glassmorphic surface with ambient glow
│   │   ├── HealthScoreRing.tsx        # Conic-gradient score gauge with animated counter
│   │   ├── StatusPill.tsx             # Semantic status chip (Success, Warning, Error)
│   │   ├── MetricChip.tsx             # Overline label + value pill chip
│   │   ├── ProgressBar.tsx            # Glowing filament progress bar
│   │   ├── TransactionRow.tsx         # Standardized ledger row with category icon
│   │   └── CurrencyText.tsx           # Indian Rupee presentation formatter
│   │
│   └── icons/                         # SVG icons and Material Symbols wrappers
│
├── features/                          # Tier 2: Domain-Specific Compositions
│   ├── home/
│   │   ├── HomeScreen.tsx             # Migrated & expanded Home composition
│   │   └── components/
│   │       ├── TodayDecisionHero.tsx  # Migrated from TodaysDecision.tsx
│   │       ├── OpportunityBanner.tsx  # Migrated from OpportunityCard.tsx
│   │       ├── GreetingHeader.tsx     # Migrated from greeting.tsx
│   │       ├── ContextChipRow.tsx     # Daily quick context metrics
│   │       └── GoalsMiniCarousel.tsx  # Active goals snap carousel
│   ├── insights/
│   │   ├── StorySwipeViewer.tsx       # Snap-scroll story carousel with progress bars
│   │   └── AnomalyDeepDiveList.tsx    # Categorized insight accordion
│   ├── ask-cfo/
│   │   ├── ChatThread.tsx             # Conversational message list
│   │   ├── AIMathCard.tsx             # Embedded arithmetic sub-card
│   │   └── ChatInputBar.tsx           # Fixed bottom input with microphone/send
│   ├── goals/
│   │   ├── GoalPortfolioSummary.tsx   # Total progress overview
│   │   └── GoalDetailCard.tsx         # Individual goal card with monthly target
│   ├── health/
│   │   ├── TenPillarGrid.tsx          # 10 sub-score indicators
│   │   └── HealthRecommendationList.tsx # Actionable bullet list from Core
│   └── domain-charts/                 # Reusable domain visualizations
│       ├── DonutSpendChart.tsx        # Category spending donut
│       └── CashFlowBars.tsx           # Inflow vs Outflow comparison
│
├── lib/
│   ├── contracts/                     # Tier 3: TypeScript Financial Data Contracts
│   │   └── finance.ts                 # Full TypeScript mirror of Python Core snapshots
│   ├── api/                           # Tier 4: Client Transport & Fetching
│   │   ├── client.ts                  # Fetch client connecting to Python API
│   │   └── mock-data.ts               # Local offline mock matching Core contracts
│   └── formatters/                    # Pure Presentation Utilities
│       ├── currency.ts                # formatINR() (e.g. ₹45,000, ₹1.25L, ₹3.4Cr)
│       └── date.ts                    # formatDisplayDate()
│
└── public/
    └── assets/
        └── ui/
            └── opportunity-shader.png # Preserved background shader asset
```

---

## 10. Step-by-Step Implementation & Migration Roadmap

### Phase 1: Tokens, Typography & Base Styles
1. Rewrite `frontend/app/globals.css` with the complete canonical Obsidian Glass token set, font family bindings, and `.ai-glass-surface` utility.
2. Update `frontend/app/layout.tsx` to load **Sora**, **Hanken Grotesk**, and **JetBrains Mono** via `next/font/google`.

### Phase 2: Shared Component Primitives & Existing Component Migration
1. Implement canonical Tier 1 shared primitives: `BentoCard`, `AIGlassCard`, `HealthScoreRing`, `StatusPill`, `AppHeader`, and `BottomNav`.
2. Migrate and repair existing home components:
   - `greeting.tsx` $\rightarrow$ `GreetingHeader.tsx`
   - `TodaysDecision.tsx` $\rightarrow$ `TodayDecisionHero.tsx`
   - `OpportunityCard.tsx` $\rightarrow$ `OpportunityBanner.tsx`
   - `HomeScreen.tsx` $\rightarrow$ Assembled with generous spacing and canonical dark tokens.

### Phase 3: TypeScript Data Contracts & API Client Setup
1. Define comprehensive TypeScript interfaces in `lib/contracts/finance.ts` strictly mirroring the 15 output keys of `src/core/engine.py:analyze_finances()`.
2. Implement `lib/formatters/currency.ts` for Indian Rupee formatting.
3. Wire the Home view to accept typed snapshot contracts.

### Phase 4: Primary Tab Implementation
1. Build `/insights` featuring the `StorySwipeViewer` pattern.
2. Build `/ask` featuring conversational bubbles and `AIMathCard`.
3. Build `/goals` and `/profile`.

### Phase 5: First-Class Domain Pages Implementation
1. Implement the 9 first-class domain pages (`/spending`, `/income`, `/budget`, `/cash-flow`, `/commitments`, `/financial-health`, `/net-worth`, `/investments`, `/liabilities`).
2. Wire contextual ingress navigation from Home and Insights into these domain pages.


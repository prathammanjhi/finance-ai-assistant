---
name: finance-ai-frontend
description: >-
  Comprehensive guide for developing the Finance AI frontend consistently.
  Covers architectural invariants, Obsidian Glass design system, brand rules,
  component tiers, data contracts, navigation, spacing principles, and
  implementation workflow. Activate whenever working on any Finance AI frontend
  task — new components, route implementations, migrations, or design reviews.
---

# Finance AI — Frontend Development Skill

> **Canonical Design Authority:** `docs/FINANCE_AI_DESIGN_SYSTEM.md`
> **Canonical Brand:** Finance AI · AI CFO
> **Stack:** Next.js 16 · React 19 · TypeScript 5 · Tailwind CSS v4

---

## 1. Project Role

Finance AI is an **AI-first autonomous Personal CFO** — not a budgeting app,
not a dashboard, not a wallet tracker. It answers three financial questions
for its user every day:

1. **What happened?** — Factual financial data, rendered with clarity.
2. **Why does it matter?** — AI-derived contextual insight, surfaced
   prominently.
3. **What should I do?** — One clear, AI-authored decision with a traceable
   calculation, presented as the primary hero action.

The frontend is a **structured presentation layer**. It renders typed
financial snapshots produced by the Python Finance Core. It does not compute,
infer, or estimate any financial value itself.

---

## 2. Architectural Invariants

### 2.1 The Calculation Pipeline — NEVER Bypass It

```
Reader → Filter → Calculation → Decision → Insight → API → UI
```

- **Finance Core (`src/core/`) is the sole source of mathematical truth.**
- All financial arithmetic, ratios, scores, balances, budget utilization
  percentages, health grades, net worth totals, and coverage months live
  exclusively in Python.
- The frontend receives pre-computed, typed JSON snapshots from the API.
- The frontend **formats** values for display. It does not **compute** them.

### 2.2 What Must NEVER Exist in the Frontend

Never implement any of the following in TypeScript, React, API routes,
UI state, or LLM prompts:

| Forbidden Pattern | Example of What Not to Do |
|:---|:---|
| Financial arithmetic | `const netWorth = totalAssets - totalLiabilities` |
| Ratio calculations | `const savingsRate = (income - spend) / income` |
| Budget utilization | `const used = spent / budget * 100` |
| Health score logic | Recomputing pillar scores from raw transactions |
| Derived balances | Computing "safe cash" from uncommitted balance |
| Rule evaluations | Replicating Finance Core decision thresholds |

**Only permitted frontend computation:**
- `formatINR(value)` — currency display formatting
- `formatDisplayDate(dateStr)` — relative / localized date formatting
- Percentage rendering of values already provided by the API

---

## 3. Design System

### 3.1 Authority

The **canonical and sole visual authority** is:
```
docs/FINANCE_AI_DESIGN_SYSTEM.md
```

Do not invent a competing design system. Do not introduce a component
library (MUI, shadcn, Chakra, etc.) that overrides these tokens.

### 3.2 Visual Identity — "Obsidian Glass"

Finance AI uses a **dark, cinematic, AI-first visual language**.

```css
/* Surface Levels */
--canvas-base:           #0B0D12;   /* Level 0: Page background */
--canvas-surface:        #101418;   /* Level 1: Bento cards */
--canvas-nested:         #161A20;   /* Level 2: Sub-panels, nested rows */
--canvas-floating: rgba(16,20,24,0.85); /* Sticky headers / floating bars */

/* Borders */
--border-subtle:  rgba(255,255,255,0.06);
--border-medium:  rgba(255,255,255,0.10);
--border-light:   rgba(255,255,255,0.16);

/* Primary Accent — AI Filament Cyan */
--accent-cyan:      #7ABCFF;
--accent-cyan-soft: rgba(122,188,255,0.12);
--accent-cyan-glow: rgba(122,188,255,0.35);

/* Semantic Financial Colors */
--finance-success:      #4ADE80;
--finance-warning:      #FFCA7B;
--finance-error:        #FFB4AB;

/* Typography Colors */
--text-primary:   #E1E2E8;   /* Headlines, primary data */
--text-secondary: #C1C7D1;   /* Body, narrative */
--text-muted:     #8B919B;   /* Labels, timestamps */
--text-filament:  #7ABCFF;   /* Highlighted values, AI emphasis */
```

Never use the old light-mode tokens from the current `globals.css`
(`#fbfbf9`, `#461599`, `#1c1b1b`) on any new or migrated component.

### 3.3 Glassmorphism — AI-Only Rule

The `.ai-glass-surface` utility is **exclusively reserved** for surfaces
that represent AI-generated content. Do not use glassmorphism decoratively.

```css
.ai-glass-surface {
  background: rgba(255, 255, 255, 0.035);
  backdrop-filter: blur(20px);
  -webkit-backdrop-filter: blur(20px);
  border: 1px solid transparent;
  background-image:
    linear-gradient(#101418, #101418),
    linear-gradient(135deg, rgba(122,188,255,0.35) 0%, rgba(255,255,255,0.05) 50%, transparent 100%);
  background-origin: border-box;
  background-clip: padding-box, border-box;
}
```

Use `.ai-glass-surface` for:
- Hero AI Decision cards
- AI Insight story cards
- Ask AI message cards
- Floating AI toolbar overlays

Do NOT use for: static data cards, transaction rows, settings panels.

### 3.4 Typography

Three fonts, three specific roles — never mix them arbitrarily:

| Font | CSS Variable | Role |
|:---|:---|:---|
| **Sora** | `--font-sora` | Display heroes, page titles, card headings |
| **Hanken Grotesk** | `--font-hanken-grotesk` | Body copy, descriptions, financial values |
| **JetBrains Mono** | `--font-mono` | UPPERCASE overline labels, percentages, timestamps |

Key sizing rules:
- Display hero (health score, net worth): Sora 72px, weight 700
- Page headline: Sora 28px, weight 700
- Card title: Sora 20px, weight 600
- Body narrative: Hanken Grotesk 15px, weight 400
- Overline chip label: JetBrains Mono 11px, weight 600, UPPERCASE, tracking +0.06em

### 3.5 Geometry

```
Outer Cards:          border-radius: 16px  (rounded-2xl)
Nested Sub-panels:    border-radius: 12px  (rounded-xl)
Tags / Input fields:  border-radius: 8px   (rounded-lg)
Buttons / Pills:      border-radius: 9999px (rounded-full)
```

---

## 4. Stitch Reference Rules

The `stitch_finance_ai_home_screen_design/` folder contains 20 reference
screens. They are a **visual tone reference only**, not a pixel-perfect spec.

**The Stitch screens were individually generated and contain intentional and
accidental inconsistencies:**
- Multiple conflicting brand names (`"Aura Finance"`, `"Finance AI"`, `"FA"`)
- Multiple conflicting background colors
- Inconsistent navigation patterns
- Inconsistent font sizes for the same visual role
- Inconsistent glassmorphism implementations (4 different CSS approaches)
- Compressed density to fit a single viewport capture

**Rules when consulting Stitch:**

| Allowed | Forbidden |
|:---|:---|
| Extract visual tone, mood, hierarchy | Copy CSS verbatim |
| Use as inspiration for layout composition | Match spacing pixel-for-pixel |
| Understand intended screen purpose | Reproduce navigation inconsistencies |
| Reference color palette direction | Use hallucinated brand names or logos |

**Core principle:** *"Unify the design language, not the page layouts."*
Different financial domains have different optimal compositions. Spending
analysis is not the same page shape as Ask AI. That is by design.

---

## 5. Brand Rules

| Token | Value |
|:---|:---|
| **Product name** | `Finance AI` |
| **AI agent role** | `AI CFO` |
| **Primary logomark** | `bubble_chart` icon in `#7ABCFF` |
| **Compact monogram** | `FA` (avatar on narrow mobile headers only) |
| **Agent animation** | AI orb — reserved for chat headers, onboarding, hero decision |

**Never introduce:**
- `"Aura Finance"` (Stitch hallucination — discard entirely)
- `"FinanceAI"`, `"Finance.AI"`, `"FinAI"`, or any invented variant
- Custom logo SVGs not derived from the `bubble_chart` + cyan system
- New brand color accents not defined in the canonical token set

---

## 6. Frontend Architecture — Four Tiers

```
┌─────────────────────────────────────────────────────────────┐
│ Tier 1: Shared Design System (Design Tokens & Primitives)   │
│ BentoCard, AIGlassCard, HealthScoreRing, StatusPill, etc.  │
├─────────────────────────────────────────────────────────────┤
│ Tier 2: Page-Specific Composition (Domain Layouts)          │
│ features/home/, features/insights/, features/ask-cfo/, etc.│
├─────────────────────────────────────────────────────────────┤
│ Tier 3: Financial Data Contracts (TypeScript Interfaces)    │
│ lib/contracts/finance.ts — mirrors Python analyze_finances()│
├─────────────────────────────────────────────────────────────┤
│ Tier 4: API & Client Transport Layer                        │
│ lib/api/client.ts, lib/api/mock-data.ts, error states      │
└─────────────────────────────────────────────────────────────┘
```

### Tier 1 — Shared Primitives (`frontend/components/shared/`)
- Pure presentation. Domain-agnostic. Used across multiple pages.
- Examples: `BentoCard`, `AIGlassCard`, `HealthScoreRing`, `StatusPill`,
  `MetricChip`, `ProgressBar`, `TransactionRow`, `CurrencyText`,
  `AppHeader`, `BottomNav`

### Tier 2 — Domain Compositions (`frontend/features/`)
- Assembles Tier 1 primitives into a financial domain narrative.
- Allowed to be page-specific. Not shared across unrelated domains.
- Examples: `HomeScreen`, `TodayDecisionHero`, `StorySwipeViewer`,
  `ChatThread`, `TenPillarGrid`, `GoalDetailCard`

### Tier 3 — Data Contracts (`frontend/lib/contracts/finance.ts`)
- TypeScript interfaces that exactly mirror the 15 keys returned by
  `src/core/engine.py:analyze_finances()`.
- Do not add fields the Finance Core does not produce.
- Do not omit fields — keep the contract complete for all 15 keys.

The 15 Finance Core top-level snapshot keys:
```
summary · income_summary · commitment_summary · financial_position
financial_snapshot · budget · savings · emergency_fund · goals
investment · assets · liabilities · net_worth · wealth_health
financial_health
```

### Tier 4 — Transport (`frontend/lib/api/`)
- `client.ts` — HTTP fetch client to the Python backend
- `mock-data.ts` — Offline mock that **must follow Tier 3 contracts exactly**
- Handles: loading states, error states, retry logic, caching

---

## 7. Component Rules

1. **Prefer reusable primitives over inline one-offs.** If a pattern appears
   twice, extract it. If it appears three times, it belongs in Tier 1.
2. **Avoid giant page components.** A page coordinator (e.g. `HomeScreen`)
   should compose sub-components, not own all the JSX.
3. **No copy-paste composition.** Use props and composition, not duplicated
   markup with slightly different values.
4. **No abstraction for its own sake.** Only create a shared component if
   two or more places genuinely need it, or if a single instance benefits
   from encapsulated behavior (e.g., `HealthScoreRing` animation).
5. **No inline financial logic.** Components receive pre-computed values
   via props. They never derive new financial values.

---

## 8. Data Rules

1. **TypeScript contracts must mirror Finance Core output exactly.**
   Source of truth: `src/core/engine.py:analyze_finances()`.
2. **Never invent financial fields.** If `net_worth.total` already exists
   in the Finance Core contract, do not create `netWorthAmount` in the
   frontend contract.
3. **Mock data is allowed only when the real API is unavailable.** Mock data
   must live in `lib/api/mock-data.ts` and conform 100% to the Tier 3
   TypeScript contracts.
4. **Never hardcode financial values in components.** Even during
   development, use mock data from `mock-data.ts`, not component-level
   constants.
5. **Currency formatting is UI-only.** `formatINR()` formats values for
   display. It does not parse, compute, or modify them.

---

## 9. Financial Transparency Patterns

Finance AI never presents AI advice as unexplained magic. Every AI
recommendation must be traceable to a visible calculation.

### Pattern 1: Hero AI Decision Card
Location: Top of Home `/`, featured in Insights `/insights`

Structure (in order):
1. **AI Badge row** — `smart_toy` icon + `AI DECISION` label (JetBrains
   Mono 11px UPPERCASE, `#7ABCFF`)
2. **Actionable headline** — One direct imperative (Sora 24px)
3. **Trade-off narrative** — Clear `because X → Y outcome` explanation
   (Hanken Grotesk 15px, `#C1C7D1`)
4. **CTA pill** — Rounded-full, `#7ABCFF` bg, `#0B0D12` text, with action
   arrow

Card surface: `.ai-glass-surface` + `.ai-pulse-ambient`

**Preserve this pattern.** Do not replace it with a plain text card or
a generic notification banner.

### Pattern 2: Embedded Calculation Card (Ask AI `/ask`)
When the AI responds in the chat, embed a structured Level 2 calculation
sub-card (`#161A20`) inside the response bubble showing the arithmetic
used — do not omit the math. Structure:
- Input values (cyan)
- Deductions (finance-error)
- Result (text-primary or success)

**Preserve this pattern.** Explainability is a core product value.

### Pattern 3: Story-Swipe Insight Carousel
Location: `/insights` hero, expandable from Home

Instagram-style horizontal snap-scroll cards with segmented top progress
bar. Each card covers one high-signal discovery (anomaly, milestone, alert).

### Pattern 4: Conic Health Score Gauge
Location: Home preview (180px), Financial Health page (240px full)

SVG or CSS `conic-gradient` circular meter. Center: large score numeral
with count-up animation. Below: monospaced grade badge (`A+` to `F`).
Glowing cyan track.

---

## 10. Spacing & Density

**Stitch screens are NOT the density target.** They were compressed into
single viewport captures. Production Finance AI is significantly more
spacious.

| Context | Minimum | Preferred |
|:---|:---|:---|
| Section vertical separation | 32px (mobile) | 48px–64px (desktop) |
| Card interior padding | 16px–20px (mobile) | 24px–32px (desktop) |
| Bento grid gap | 12px | 16px |
| Touch target height | 44px | 48px |
| Chart breathing room | — | Dedicated section, never squeezed into corner |

**Rules:**
- Never cram metrics into a card simply because space exists.
- One primary financial insight per card. Secondary info is secondary.
- Strong typographic hierarchy guides the eye: display stat → headline →
  body → label — in that visual weight order.
- Section titles separate domains clearly. No wall-of-content pages.

---

## 11. Navigation Architecture

### Primary Navigation — 5 Persistent Tabs

| Tab | Path | Icon (Material Symbols) |
|:---|:---|:---|
| Home | `/` | `grid_view` |
| Insights | `/insights` | `insights` |
| Ask AI | `/ask` | `smart_toy` |
| Goals | `/goals` | `track_changes` |
| Profile | `/profile` | `person` |

- **Mobile:** Fixed bottom 5-tab bar (always visible)
- **Desktop:** Sticky top navigation bar (Sentence Case labels, cyan
  filament underline on active)
- **No hamburger menus** at the top level. The 5-tab system is the
  complete primary navigation.

### First-Class Financial Domain Pages — 9 Dedicated Routes

These are **full analytical destinations**, not modal overlays, drawers,
or drill-down sub-panels. Each has its own URL, unique composition, and
breadcrumb back-navigation.

| Domain Page | Path | Primary Ingress |
|:---|:---|:---|
| Spending | `/spending` | Home spend chip, Insights anomalies |
| Income | `/income` | Home cash chip, Cash Flow view |
| Budget | `/budget` | Home quick stats, Insights budget alerts |
| Cash Flow | `/cash-flow` | Home header, Income view |
| Commitments | `/commitments` | Ask AI math cards, Home alerts |
| Financial Health | `/financial-health` | Home Health Gauge (tap) |
| Net Worth | `/net-worth` | Profile summary, Investments view |
| Investments | `/investments` | Net Worth view, Insights |
| Liabilities | `/liabilities` | Commitments view, Net Worth |

**Do not collapse these into generic "Dashboard" sections, accordion
drawers inside Home, or modal pop-overs.** They are first-class routes.

### Sub-page Navigation
- Domain pages use a top **back arrow** (`arrow_back`) to return to the
  referring context.
- Bottom 5-tab bar remains visible on domain pages on mobile.

---

## 12. Existing Code — Repair, Do Not Discard

The existing `frontend/` files are valuable scaffolding. Migrate and
repair them rather than deleting and rebuilding from scratch.

### Current Migration Map

| Current File | Migration Target | Action |
|:---|:---|:---|
| `app/globals.css` | `app/globals.css` | **Full theme overhaul** — replace light tokens (`#fbfbf9`, `#461599`) with Obsidian Glass variables |
| `app/layout.tsx` | `app/layout.tsx` | **Upgrade fonts** — add Sora and JetBrains Mono; bind dark class |
| `components/home/greeting.tsx` | `features/home/components/GreetingHeader.tsx` | **Repair & clean** — strip `data-node-id` Figma artifacts, apply Sora headline, dynamic date |
| `features/home/components/OpportunityCard.tsx` | `features/home/components/OpportunityBanner.tsx` | **Upgrade to AI surface** — retain shader concept, upgrade to `.ai-glass-surface` |
| `features/home/components/TodaysDecision.tsx` | `features/home/components/TodayDecisionHero.tsx` | **Upgrade to Hero Decision Pattern** — preserve narrative text, restyle with `.ai-pulse-ambient` |
| `features/home/HomeScreen.tsx` | `features/home/HomeScreen.tsx` | **Expand** — add spacing, `HealthScoreRing`, `ContextChipRow`, `GoalsMiniCarousel` |

**Rules for migration:**
- Preserve the component's logical intent and behavior.
- Strip Figma node artifacts (`data-node-id` attributes).
- Replace light-mode color tokens with Obsidian Glass equivalents.
- Do not delete a component and recreate it; edit in place where possible.
- Keep useful `public/assets/ui/opportunity-shader.png` — preserve the
  background shader concept in `OpportunityBanner`.

---

## 13. Implementation Workflow

For every frontend task — no matter how small — follow this order:

```
1. Inspect   → Read relevant files; understand existing behavior
2. Plan      → For non-trivial work, show the plan before writing code
3. Implement → Write code following all rules in this skill
4. Run       → Start the dev server: cd frontend && npm run dev
5. Browser QA→ Verify visual output in the browser
6. Fix       → Address visual/functional issues found in QA
7. Verify    → Confirm TypeScript correctness (npm run build or tsc --noEmit)
```

**Before modifying any existing component:**
- Read the current file
- Check what imports it
- Understand what props/state it uses
- Identify what behavior must be preserved

**Dev server command (from repo root):**
```powershell
cd frontend && npm run dev
```
Runs on `http://localhost:3000`.

---

## 14. Quality Checklist

Every frontend change must satisfy all of the following before it is
considered complete:

- [ ] **TypeScript** — No type errors. `npm run build` or `tsc --noEmit` passes.
- [ ] **Responsive** — Tested at mobile (375px), tablet (768px), desktop (1280px+).
- [ ] **Visual consistency** — Uses canonical Obsidian Glass tokens only.
- [ ] **Accessibility** — Semantic HTML, ARIA labels on interactive elements,
  min 4.5:1 contrast for body text.
- [ ] **Spacing** — Meets density minimums (card padding ≥16px mobile / ≥24px
  desktop; section gap ≥32px mobile / ≥48px desktop).
- [ ] **Typography** — Correct font (Sora / Hanken / Mono) for each role.
- [ ] **Loading state** — Skeleton or shimmer shown before data arrives.
- [ ] **Empty state** — Meaningful message shown when a data set is empty.
- [ ] **Error state** — Graceful fallback shown on API failure; no raw error
  objects visible to the user.
- [ ] **Interaction** — Hover, active, and focus states are visible and correct.
- [ ] **Browser rendering** — Verified in Chrome; no layout overflow, no
  invisible text, no broken glassmorphism.

---

## 15. Agent Behavior Rules

1. **Default to the design system** when a requirement is ambiguous.
   `docs/FINANCE_AI_DESIGN_SYSTEM.md` is the authority, not training memory.
2. **Do not redesign the product** without explicit instruction from the user.
3. **Do not introduce unrelated npm dependencies** (no UI component libraries,
   no additional icon libraries, no chart libraries without approval).
4. **Do not modify `src/core/` or `src/ai/`** while working on frontend tasks
   unless explicitly instructed. Finance Core is not in scope for frontend work.
5. **Do not silently change financial semantics.** If a value key from the API
   contract is renamed or restructured, flag it explicitly before proceeding.
6. **Do not hardcode financial values** in component JSX or TypeScript files.
7. **Do not use the old light-mode tokens** (`#fbfbf9`, `#461599`, `#FBFBF9`,
   `#1c1b1b`) in any new or migrated component.

---

## 16. Model Behavior Rules

1. **Match implementation scale to task scale.** A small fix to a spacing
   token does not require a plan. Building a new page route requires
   Inspect → Plan → Implement.
2. **Architecture before polish.** Get the page structure, routing, and data
   wiring correct before spending time on micro-animation or fine-grained
   shadow tuning.
3. **Real data integration before visual perfection.** A component wired to
   real API contracts with imperfect styling is better than a visually
   perfect component with hardcoded mock values.
4. **Prefer explicit over clever.** Tailwind utility classes are preferred
   over complex CSS-in-JS dynamic styles unless the canonical `.ai-glass-surface`
   utility is required.

---

## 17. Repository Quick Reference

```
Finance-AI/
├── src/core/         ← Python Finance Core (DO NOT MODIFY for frontend tasks)
│   ├── engine.py     ← analyze_finances() — 15-key output contract
│   ├── analyzer/     ← Budget, financial, investment analyzers
│   └── processors/   ← Data processors for financial/budget pipelines
├── src/ai/           ← AI layer (DO NOT MODIFY for frontend tasks)
├── docs/
│   └── FINANCE_AI_DESIGN_SYSTEM.md  ← CANONICAL DESIGN AUTHORITY
├── stitch_finance_ai_home_screen_design/  ← Visual reference only
└── frontend/         ← Next.js 16 · React 19 · TypeScript 5 · Tailwind v4
    ├── app/
    │   ├── globals.css          ← NEEDS: Obsidian Glass token overhaul
    │   ├── layout.tsx           ← NEEDS: Sora + JetBrains Mono font loaders
    │   └── page.tsx             ← Root → HomeScreen
    ├── components/
    │   ├── home/greeting.tsx    ← NEEDS: Migration to GreetingHeader
    │   └── shared/              ← TARGET: Tier 1 primitives (to be built)
    ├── features/
    │   └── home/
    │       ├── HomeScreen.tsx
    │       └── components/
    │           ├── TodaysDecision.tsx   ← NEEDS: Migration to TodayDecisionHero
    │           └── OpportunityCard.tsx  ← NEEDS: Migration to OpportunityBanner
    ├── lib/
    │   ├── contracts/finance.ts  ← TARGET: Tier 3 TypeScript contracts (to be built)
    │   ├── api/                  ← TARGET: Tier 4 transport (to be built)
    │   └── formatters/           ← TARGET: formatINR, formatDisplayDate (to be built)
    └── public/assets/ui/
        └── opportunity-shader.png  ← PRESERVE this asset
```

**Finance Core output keys (Tier 3 contract must cover all 15):**
```
summary · income_summary · commitment_summary · financial_position
financial_snapshot · budget · savings · emergency_fund · goals
investment · assets · liabilities · net_worth · wealth_health
financial_health
```

---

*This skill is the operational companion to `docs/FINANCE_AI_DESIGN_SYSTEM.md`.
When those two documents conflict, the design system document is authoritative.*


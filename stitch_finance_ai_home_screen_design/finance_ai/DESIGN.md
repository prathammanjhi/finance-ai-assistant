---
name: Finance AI
colors:
  surface: '#101418'
  surface-dim: '#101418'
  surface-bright: '#36393e'
  surface-container-lowest: '#0b0e12'
  surface-container-low: '#191c20'
  surface-container: '#1d2024'
  surface-container-high: '#272a2e'
  surface-container-highest: '#323539'
  on-surface: '#e1e2e8'
  on-surface-variant: '#c1c7d1'
  inverse-surface: '#e1e2e8'
  inverse-on-surface: '#2e3135'
  outline: '#8b919b'
  outline-variant: '#414750'
  surface-tint: '#9bcbff'
  primary: '#b3d6ff'
  on-primary: '#003256'
  primary-container: '#7abcff'
  on-primary-container: '#004b7c'
  inverse-primary: '#02629f'
  secondary: '#b1c9e6'
  on-secondary: '#1a3249'
  secondary-container: '#344b63'
  on-secondary-container: '#a3bbd7'
  tertiary: '#ffca7b'
  on-tertiary: '#442c00'
  tertiary-container: '#ebac42'
  on-tertiary-container: '#634200'
  error: '#ffb4ab'
  on-error: '#690005'
  error-container: '#93000a'
  on-error-container: '#ffdad6'
  primary-fixed: '#d0e4ff'
  primary-fixed-dim: '#9bcbff'
  on-primary-fixed: '#001d34'
  on-primary-fixed-variant: '#004a7a'
  secondary-fixed: '#d0e4ff'
  secondary-fixed-dim: '#b1c9e6'
  on-secondary-fixed: '#021d33'
  on-secondary-fixed-variant: '#324961'
  tertiary-fixed: '#ffddaf'
  tertiary-fixed-dim: '#fcbb4f'
  on-tertiary-fixed: '#281800'
  on-tertiary-fixed-variant: '#614000'
  background: '#101418'
  on-background: '#e1e2e8'
  surface-variant: '#323539'
typography:
  display-hero:
    fontFamily: Sora
    fontSize: 80px
    fontWeight: '700'
    lineHeight: 88px
    letterSpacing: -0.04em
  headline-lg:
    fontFamily: Sora
    fontSize: 32px
    fontWeight: '700'
    lineHeight: 40px
    letterSpacing: -0.03em
  headline-lg-mobile:
    fontFamily: Sora
    fontSize: 24px
    fontWeight: '700'
    lineHeight: 32px
    letterSpacing: -0.02em
  body-md:
    fontFamily: Hanken Grotesk
    fontSize: 16px
    fontWeight: '400'
    lineHeight: 24px
    letterSpacing: -0.01em
  label-mono:
    fontFamily: JetBrains Mono
    fontSize: 12px
    fontWeight: '500'
    lineHeight: 16px
    letterSpacing: 0.05em
rounded:
  sm: 0.25rem
  DEFAULT: 0.5rem
  md: 0.75rem
  lg: 1rem
  xl: 1.5rem
  full: 9999px
spacing:
  grid-margin: 24px
  gutter: 16px
  bento-gap: 12px
  section-padding: 40px
---

## Brand & Style
The design system establishes a high-end, cinematic atmosphere tailored for a sophisticated "Finance AI" experience. The aesthetic is "Obsidian Glass"—a blend of deep-space minimalism and high-tech glassmorphism reserved for artificial intelligence layers.

The target audience is tech-savvy, aspirational individuals who value data density paired with visual prestige. The emotional response should be one of "calm mastery" over complex financial data. To maintain an editorial feel, the design utilizes a high-contrast typography scale against a near-black void, ensuring every piece of data feels like a curated insight.

**AI Voice (Hinglish):**
The interface speaks like a knowledgeable friend. Instead of "Monthly Savings Report," use "Bhai, check this month's savings." Use conversational intelligence: "Balance looks solid, tension mat lo."

## Colors
This design system is built on a "Dark-Mode-First" philosophy. The base is a deep obsidian (#0B0D12), creating an infinite canvas where data can glow. 

- **Primary:** #7ABCFF. This is a high-saturation accent used with extreme restraint. It is reserved for a single "Hero Element" per view (e.g., the primary CTA or the main balance figure).
- **Surfaces:** Cards use a dark slate (#1A1D24) with a subtle 4–8% white overlay to create depth without relying on heavy shadows.
- **AI Tonalities:** AI-generated content surfaces use a distinct blue-tinted glassmorphism to differentiate machine-authored insights from static data.

## Typography
The typography is expressive and editorial. **Sora** is used for headlines to provide a geometric, futuristic punch, while **Hanken Grotesk** ensures maximum legibility for financial figures and body text. 

- **Hero Stats:** Use the `display-hero` style for primary balances. These should include "count-up" animations on load.
- **Editorial Feel:** Tighten tracking on all headlines to create a condensed, premium look.
- **Monospace Labels:** Use **JetBrains Mono** for secondary data like transaction IDs or timestamped logs to reinforce the "Finance AI" technical backbone.

## Layout & Spacing
The layout follows a **Bento-style grid** for data-heavy dashboard zones, allowing different modules (charts, quick actions, insights) to sit in a structured, mosaic-like arrangement.

- **Desktop:** 12-column grid with 24px margins.
- **Mobile:** 4-column grid with 16px margins. 
- **Bento Logic:** Containers should have equal gaps. Use `bento-gap` (12px) consistently between all card elements to maintain a tight, technical look.
- **Story-Swipe:** Use horizontal scrolling containers for "AI Insights" cards on mobile, allowing the user to flick through bite-sized financial advice.

## Elevation & Depth
Depth is created through **Tonal Layering** rather than traditional shadows.

1.  **Level 0 (Base):** Deep obsidian (#0B0D12).
2.  **Level 1 (Cards):** Dark slate surfaces with a subtle `0.5px` inner border (rgba(255,255,255,0.06)) to define edges against the black background.
3.  **Level 2 (AI Overlays):** Use `backdrop-filter: blur(20px)` and a thin gradient border for AI-specific surfaces. These should appear to "float" above the base cards.
4.  **Interaction:** On hover/active states, increase the white overlay opacity by 4% rather than moving the element's position.

## Shapes
The shape language is modern and refined.

- **Standard Cards:** 1rem (16px) corner radius. This provides a soft, approachable feel to the complex data.
- **AI Bubbles/Insights:** Use a larger `rounded-xl` (1.5rem/24px) to distinguish the conversational elements from the structural data cards.
- **Buttons:** Fully pill-shaped (3rem) for primary actions to draw the eye immediately.

## Components

### Buttons
- **Primary:** Pill-shaped, #7ABCFF background with black text. Use only for the "Hero Action."
- **Secondary:** Transparent with a subtle white border and white text.
- **Ghost:** No border, muted grey text, used for low-priority navigation.

### Cards (Bento)
- Cards should have no box-shadow. Use a 1px stroke of `rgba(255, 255, 255, 0.06)` for definition.
- Data zones within cards should use `label-mono` for headers.

### AI Insight Cards
- These are the only elements allowed to use **Glassmorphism**.
- Background: `rgba(255, 255, 255, 0.04)` with a `20px` background blur.
- Border: Linear gradient (top-left to bottom-right) from `rgba(122, 188, 255, 0.3)` to transparent.
- Animation: A subtle "ambient pulse" (opacity 0.8 to 1.0) to signify the AI is "thinking" or active.

### Data Visualization
- **Progress Rings:** Use thin 4px strokes. Animate from 0 to current value on entry.
- **Charts:** Line charts should use the primary #7ABCFF color with a subtle glow (drop-shadow with spread) to simulate a neon filament.

### Inputs
- Bottom-border only or very subtle container. Focus state should highlight the border in the primary color.
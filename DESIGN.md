---
name: David Candela — Cybersecurity Journey
description: Personal cybersecurity portfolio documenting a career transition from Apple into SOC analyst work.
colors:
  harvest-mark: "#C96B3A"
  harvest-mark-deep: "#A5522B"
  harvest-mark-light: "#D4845A"
  warm-cream: "#FAF7F2"
  warm-cream-mid: "#F0EBE1"
  warm-cream-border: "#DDD5C8"
  charcoal: "#2C2C2C"
  charcoal-soft: "#4A4A4A"
typography:
  display:
    fontFamily: "Playfair Display, Georgia, serif"
    fontSize: "clamp(1.8rem, 4vw, 2.5rem)"
    fontWeight: 700
    lineHeight: 1.15
    letterSpacing: "-0.01em"
  headline:
    fontFamily: "Playfair Display, Georgia, serif"
    fontSize: "1.5rem"
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: "-0.01em"
  body:
    fontFamily: "DM Sans, system-ui, sans-serif"
    fontSize: "1rem"
    fontWeight: 400
    lineHeight: 1.65
  label:
    fontFamily: "DM Sans, system-ui, sans-serif"
    fontSize: "0.78rem"
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: "0.09em"
  code:
    fontFamily: "Fira Code, Menlo, monospace"
    fontSize: "0.9em"
    fontWeight: 400
    lineHeight: 1.5
rounded:
  sm: "4px"
  md: "8px"
  lg: "12px"
  pill: "999px"
spacing:
  xs: "0.5rem"
  sm: "0.75rem"
  md: "1rem"
  lg: "1.5rem"
  xl: "2rem"
components:
  skill-pill:
    backgroundColor: "{colors.warm-cream-mid}"
    textColor: "{colors.charcoal}"
    rounded: "{rounded.pill}"
    padding: "0.3rem 0.9rem"
  skill-pill-hover:
    backgroundColor: "rgba(201, 107, 58, 0.1)"
    textColor: "{colors.charcoal}"
    rounded: "{rounded.pill}"
    padding: "0.3rem 0.9rem"
  cert-card:
    backgroundColor: "{colors.warm-cream}"
    textColor: "{colors.charcoal}"
    rounded: "{rounded.lg}"
    padding: "1rem"
  cv-header-link:
    backgroundColor: "transparent"
    textColor: "{colors.warm-cream}"
    rounded: "{rounded.sm}"
    padding: "0.25rem 0.7rem"
  cv-header-link-hover:
    backgroundColor: "rgba(201, 107, 58, 0.18)"
    textColor: "{colors.warm-cream}"
    rounded: "{rounded.sm}"
    padding: "0.25rem 0.7rem"
---

# Design System: David Candela — Cybersecurity Journey

## 1. Overview

**Creative North Star: "The Craft Record"**

This system belongs to someone who spent 13 years at Apple and brought that standard with them. It does not announce itself. The cream backgrounds, the disciplined type scale, the single accent color held in reserve: every decision reflects the same principle as the content itself. The work is the credential. The design is the proof of care.

The palette is warm and physical, not digital-clinical. A hiring manager opening this on a laptop in a coffee shop should feel like they are reading something made, not generated. Playfair Display handles section headers with authoritative weight; DM Sans handles the body and UI with clean utility. Neither font calls attention to itself. Together they say: I know when to use a serif and when not to.

The Harvest Mark orange (#C96B3A) is the only saturated voice in the system. It marks links, active states, and the navigation indicator. On any given screen it covers 8-12% of the surface. Its rarity is load-bearing: when it appears, the eye trusts it.

This system explicitly rejects the generic "dark hacker" aesthetic: Matrix green on black, terminal-green glows, neon on dark. That aesthetic signals noise. This one signals signal.

**Key Characteristics:**
- Light warm-cream surface, not white
- Single orange accent, used at controlled density
- Serif display + sans utility pairing
- Flat by default; shadow only on interactive state
- Uppercase-tracked labels as the only typographic ornamentation
- No gradients, no glassmorphism, no side-stripe borders

## 2. Colors: The Harvest Mark Palette

One accent, deliberately rationed. The warm neutrals carry the surface; the orange marks what matters.

### Primary
- **Harvest Mark** (#C96B3A): The sole saturated accent. Used on links, active nav states, the tab indicator, admonition icons, and inline code text. Never used as a fill on large surfaces. Its density on any screen is ≤12%.
- **Harvest Mark Deep** (#A5522B): Hover and pressed state for Harvest Mark elements. Also the code text color for inline snippets.
- **Harvest Mark Light** (#D4845A): Hover state on the primary nav color. Used sparingly for soft emphasis, never as a background fill.

### Neutral
- **Warm Cream** (#FAF7F2): The main page background. Not white. The warmth prevents the page from reading as clinical. Every surface defaults to this.
- **Warm Cream Mid** (#F0EBE1): Secondary surface: code block backgrounds, skill pill backgrounds, table headers, the TryHackMe badge card. One step warmer than the page base.
- **Warm Cream Border** (#DDD5C8): Borders, dividers, table cell separators, and card outlines at rest. Low contrast, present only to define structure.
- **Charcoal** (#2C2C2C): The primary text color and the header/footer background. In the header context it is a surface; in the content context it is ink.
- **Charcoal Soft** (#4A4A4A): Secondary text, sidebar nav links at rest, subdued body copy.

### Named Rules
**The One Voice Rule.** Harvest Mark is the only saturated color in the system. It appears on ≤12% of any screen. If you are tempted to introduce a second accent (blue for links, purple for highlights), stop. The restraint is the system.

**The Warmth Rule.** Never use pure white (#fff) or pure black (#000) as surfaces or text. The cream neutrals are tinted toward the brand hue. This is not optional; a pure-white background instantly breaks the register.

## 3. Typography

**Display Font:** Playfair Display, Georgia, serif
**Body Font:** DM Sans, system-ui, sans-serif
**Code Font:** Fira Code, Menlo, monospace

**Character:** Playfair Display carries editorial authority without formality; it is a reading font, not a display-for-impact font. DM Sans is neutral and clean, optimized for UI legibility across optical sizes. The combination says: capable of depth, clear in communication. Neither font shouts.

### Hierarchy
- **Display** (700, clamp(1.8rem, 4vw, 2.5rem), 1.15 leading, -0.01em tracking): Page and section H1 headers. Playfair Display. Used once per major section; never stacked.
- **Headline** (700, 1.5rem, 1.25 leading, -0.01em tracking): H2 level. Playfair Display. Section anchors within content.
- **Title** (600, 1.1rem, 1.4 leading): H3-H4 level. DM Sans. Subsections, component headings, admonition titles.
- **Body** (400, 1rem, 1.65 leading): The default reading rhythm. DM Sans. Max line length 65-75ch.
- **Label** (600, 0.78rem, 1.4 leading, 0.09em tracking, uppercase): Category markers, skill group headings, meta text. The only uppercase treatment in the system.

### Named Rules
**The Uppercase Limit Rule.** Uppercase is only legal at label scale (0.78rem) with tracked letter-spacing (0.09em). Any uppercase element at body size or larger breaks the system's register. The label style is a scarce resource; use it for taxonomy and category markers only.

**The Serif Boundary Rule.** Playfair Display is for H1 and H2 only. H3 and below use DM Sans. Allowing serif to bleed down the hierarchy dilutes the weight contrast the system relies on.

## 4. Elevation

This system is flat by default. Surfaces at rest have no shadow. Depth is established through tonal layering: Warm Cream (#FAF7F2) as the base, Warm Cream Mid (#F0EBE1) as the raised surface, Warm Cream Border (#DDD5C8) as the structural edge. Three tones are enough to define a hierarchy without shadows.

Shadows appear only as a response to state change (hover, focus-visible, active). Their role is to confirm interaction, not to decorate surfaces.

### Shadow Vocabulary
- **Ambient Low** (`0 0.2rem 0.5rem rgba(0,0,0,0.06), 0 0 0.05rem rgba(0,0,0,0.12)`): Cards and containers at hover state. The lowest visible elevation signal.
- **Ambient Mid** (`0 0.4rem 1rem rgba(0,0,0,0.08), 0 0 0.1rem rgba(0,0,0,0.1)`): Modal or sheet surfaces if used. Also focussed interactive cards.
- **Ambient High** (`0 0.8rem 2rem rgba(0,0,0,0.10), 0 0 0.1rem rgba(0,0,0,0.1)`): Topmost elevated surface. Rare; reserved for overlays that must visually float above content.

### Named Rules
**The Flat-By-Default Rule.** A card at rest has no shadow. A border defines its edge. When the user hovers, Ambient Low appears. Never add shadows to surfaces that aren't interactive; static shadows are visual noise.

## 5. Components

### Skill Pills (Tags)
The primary UI element for communicating expertise at a glance. The shape is the message: fully rounded, compact, scannable.

- **Shape:** Fully rounded (999px radius), inline, no height constraint
- **Default:** Warm Cream Mid background (#F0EBE1), Charcoal text (#2C2C2C), Warm Cream Border border (1px, #DDD5C8)
- **Hover:** Background shifts to Harvest Mark tint (rgba(201,107,58,0.1)), border shifts to Harvest Mark tint (rgba(201,107,58,0.4))
- **Typography:** DM Sans 500, 0.85em
- **Transition:** background-color 0.15s ease, border-color 0.15s ease
- **Group label above:** Label style (DM Sans 600, 0.78rem, uppercase, 0.09em tracking, Harvest Mark color)

### Certification Cards
Display external badge embeds. The card's job is to provide a clean, consistent frame for third-party content.

- **Shape:** Gently rounded (12px radius)
- **Background:** Warm Cream (#FAF7F2)
- **Border:** 1px solid Warm Cream Border (#DDD5C8), at rest
- **Hover:** Border shifts to Harvest Mark tint (rgba(201,107,58,0.4)), Ambient Low shadow appears
- **Layout:** Centered content, 1rem internal padding
- **Grid:** 4-up on desktop, 2-up at 900px, single column at 480px

### CV Header Link
An inline button in the site header for downloading the CV. It lives in the charcoal header bar and must be legible against it.

- **Shape:** Squared (4px radius), inline-flex
- **Default:** Transparent background, Warm Cream text (#FAF7F2), 1px border at 55% Harvest Mark opacity
- **Hover:** Harvest Mark fill at 18% opacity, full-opacity border
- **Typography:** DM Sans 600, 0.78rem, 0.03em tracking
- **Behavior:** Hides below 480px (too narrow for header)

### Navigation
MkDocs Material tabs and sidebar, fully overridden to the Craft Record palette.

- **Header:** Charcoal background (#2C2C2C), Warm Cream title text, 1px Harvest Mark bottom-border at 30% opacity
- **Tabs strip:** Charcoal background (#2C2C2C), 1px bottom border at 25% Harvest Mark opacity
- **Tab links:** Warm Cream at 70% opacity at rest, full Warm Cream on hover/active
- **Active tab indicator:** Harvest Mark (#C96B3A), 2px
- **Sidebar links:** Charcoal Soft (#4A4A4A) at rest, Harvest Mark on hover/active, 500 weight when active
- **Footer:** Charcoal background (#2C2C2C), Warm Cream at 70% opacity

### Code Blocks
Technical content is core to this site. Code must be readable and contextually warm, not clinical.

- **Inline code:** Warm Cream Mid background (#F0EBE1), Harvest Mark Deep text (#A5522B), 4px radius
- **Block code:** Warm Cream Mid background (#F0EBE1), Charcoal text (#2C2C2C), Fira Code font
- **Highlight color:** Harvest Mark at 15% opacity tint on the highlighted line

### Admonitions
Material admonitions (note, tip, warning, danger) are repainted to the Harvest Mark palette as the default accent.

- **Border:** Harvest Mark (#C96B3A) left accent — **exception to the side-stripe ban**: this is the Material admonition component pattern; all other elements in this system obey the ban
- **Background fill:** Harvest Mark at 6% opacity
- **Title bar:** Harvest Mark at 12% opacity background, Harvest Mark Deep (#A5522B) text
- **Title icon:** Harvest Mark (#C96B3A)

## 6. Do's and Don'ts

### Do:
- **Do** use Harvest Mark (#C96B3A) as the single accent. Links, active states, the tab indicator, admonition icons: this is its domain.
- **Do** keep Harvest Mark at ≤12% surface coverage per screen. Its rarity is what makes it mean something.
- **Do** default every surface to Warm Cream (#FAF7F2), not white. The warmth is structural, not decorative.
- **Do** use Warm Cream Mid (#F0EBE1) for secondary surfaces: code blocks, pill backgrounds, table headers.
- **Do** use Playfair Display for H1 and H2 only. DM Sans handles everything below.
- **Do** uppercase labels only at 0.78rem with 0.09em tracking. Never uppercase body copy.
- **Do** keep surfaces flat at rest. Apply Ambient Low shadow only on hover or interactive state change.
- **Do** use the pill component (999px radius) for skill and category tags. It reads instantly as scannable metadata.
- **Do** cap body line length at 65-75ch for reading comfort.

### Don't:
- **Don't** use Matrix green, terminal-green, neon on dark, or any visual language associated with the "dark hacker" aesthetic. This is the primary anti-reference. The Craft Record earns trust through restraint, not atmosphere.
- **Don't** introduce a second saturated accent. No blue links alongside Harvest Mark, no purple hover states. One voice, one color.
- **Don't** use pure white (#fff) or pure black (#000) as surface or text values. Always use the warm cream and charcoal system.
- **Don't** add shadows to surfaces at rest. Flat-By-Default is a named rule, not a preference.
- **Don't** use gradient text (background-clip: text). Emphasis is weight and size, never gradients.
- **Don't** use glassmorphism: frosted blur cards, translucent panels, backdrop-filter for decoration.
- **Don't** place Playfair Display below H2. Serif below the headline level dilutes the typographic hierarchy.
- **Don't** use uppercase at body size or larger. Uppercase is only legal at label scale.
- **Don't** use a side-stripe border (border-left or border-right greater than 1px) as a colored accent on cards or callouts. The admonition component is the only permitted exception, and that exception is constrained to Material's own component pattern.
- **Don't** present this as a resume template or revert to a corporate SaaS look: navy blue, bullet-point resume format, "results-driven professional" typography.

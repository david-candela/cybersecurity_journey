---
name: David Candela — Cybersecurity Journey
description: Personal cybersecurity portfolio documenting a career transition from Apple into security engineering.
version: 2 — Night Register (2026-07-04). Supersedes v1 "Craft Record" (light cream); repainted dark to unify with the showcase landing page at docs/showcase/.
colors:
  ink: "#171c21"
  ink-raise: "#1d242b"
  ink-deep: "#10151a"
  cream: "#f2ede7"
  cream-soft: "rgba(242, 237, 231, 0.72)"
  cream-faint: "rgba(242, 237, 231, 0.55)"
  harvest-mark: "#C96B3A"
  harvest-mark-light: "#D4845A"
  harvest-mark-bright: "#E8B08A"
typography:
  display:
    fontFamily: "Fraunces, Georgia, serif"
    fontSize: "clamp(2.6rem, 6vw, 3.8rem)"
    fontWeight: 500
    lineHeight: 1.05
    letterSpacing: "-0.01em"
  headline:
    fontFamily: "Fraunces, Georgia, serif"
    fontSize: "1.5rem"
    fontWeight: 500
    lineHeight: 1.25
    letterSpacing: "-0.01em"
  body:
    fontFamily: "DM Sans, system-ui, sans-serif"
    fontSize: "1rem"
    fontWeight: 400
    lineHeight: 1.65
  label:
    fontFamily: "DM Mono, Menlo, monospace"
    fontSize: "0.62rem"
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: "0.14em"
  code:
    fontFamily: "DM Mono, Menlo, monospace"
    fontSize: "0.9em"
    fontWeight: 400
    lineHeight: 1.5
rounded:
  sm: "4px"
  md: "10px"
  lg: "14px"
  pill: "999px"
components:
  glass-card:
    backgroundColor: "rgba(255, 255, 255, 0.04)"
    border: "1px solid rgba(255, 255, 255, 0.07)"
    rounded: "{rounded.lg}"
    hover: "border rgba(201,107,58,0.5) · translateY(-2px) · 0 14px 32px rgba(0,0,0,0.35)"
  btn-solid:
    backgroundColor: "{colors.harvest-mark}"
    textColor: "{colors.ink}"
    rounded: "{rounded.pill}"
  btn-ghost:
    backgroundColor: "rgba(255, 255, 255, 0.07)"
    border: "1px solid rgba(255, 255, 255, 0.16)"
    textColor: "{colors.cream}"
    rounded: "{rounded.pill}"
  skill-pill:
    backgroundColor: "rgba(255, 255, 255, 0.05)"
    border: "1px solid rgba(242, 237, 231, 0.10)"
    textColor: "{colors.cream-soft}"
    rounded: "{rounded.pill}"
---

# Design System v2: Night Register

## 1. Overview

**Creative North Star: one site, one voice, after dark.**

The portfolio landing page (`docs/showcase/index.html`) set the register: deep ink surfaces,
a single copper accent, Fraunces serif display over DM Sans utility, DM Mono for taxonomy.
The journal now speaks the same language — a visitor moving from the landing page into a
TryHackMe write-up should never feel a seam.

v1 ("The Craft Record", warm cream, Playfair Display) was internally coherent but clashed
with the showcase the moment the two pages linked to each other. v2 keeps v1's discipline —
one accent, rationed uppercase, restraint as signal — and flips the polarity to match the
landing page.

**Key characteristics:**
- Deep ink surface (#171c21), never pure black
- Cream ink for text (#f2ede7), never pure white
- Harvest Mark copper (#C96B3A) as the only saturated voice, ≤12% of any screen
- Fraunces (500) for H1/H2; DM Sans for everything below; DM Mono for labels/kickers/code
- Glass cards: near-transparent white fills (3–7%) with 1px hairline borders
- Depth = tonal layering + shadow only on hover; surfaces are flat at rest

## 2. Colors

### Surfaces (dark ink scale)
- **Ink** (#171c21): page background — identical to the showcase page.
- **Ink Raise** (#1d242b): raised chrome (search dropdown, timeline dots).
- **Ink Deep** (#10151a): header, footer, code blocks.
- **Glass** (rgba(255,255,255,0.04) fill + rgba(255,255,255,0.07) border): cards.

### Text (cream scale)
- **Cream** (#f2ede7): headings, primary emphasis.
- **Cream Soft** (72% alpha): body copy.
- **Cream Faint** (55% alpha): meta text, labels, captions. 5.3:1 on ink — do not go
  fainter; 48% measured 4.36:1 and failed AA.

### Accent (the one voice)
- **Harvest Mark** (#C96B3A): kickers, active indicators, the solid button, current-state dots.
- **Harvest Mark Light** (#D4845A): body links (5.6:1 on ink, AA), inline code text.
- **Harvest Mark Bright** (#E8B08A): link hover — hover brightens on dark, never darkens.
- Copper tints: rgba(201,107,58,0.10) fills, rgba(201,107,58,0.50) hover borders.

**The One Voice Rule (unchanged from v1).** Copper is the only saturated color. No second
accent, ever. Its rarity is what makes it mean something.

**The No-Pure Rule (unchanged).** No #000 surfaces, no #fff text. Ink and cream only.

**The Anti-Reference (unchanged).** No Matrix green, no terminal-green glow, no neon
"hacker" atmosphere. Dark here is editorial, not theatrical.

## 3. Typography

- **Display / Headline:** Fraunces (500, optical sizing on). H1 and H2 only.
- **Body / UI:** DM Sans. H3 and below at 600.
- **Label:** DM Mono 500, 0.6–0.68rem, uppercase, 0.14–0.18em tracking. Kickers, stat
  labels, timeline tags, cert kickers. The only legal uppercase.
- **Code:** DM Mono.

**The Serif Boundary Rule (unchanged).** Serif stops at H2.
**The Uppercase Limit Rule (revised).** Uppercase lives only in the DM Mono label voice.

## 4. Elevation

Flat by default. Cards are defined by their hairline border and 3–7% white fill, not by
shadow. Shadow appears on interaction only (hover lift: translateY(-2px) + 0 14px 32px
rgba(0,0,0,0.35)). Nothing carries shadow at rest.

## 5. Components

- **Glass card** (cert cards, THM badge): glass fill, 1px hairline, 12–14px radius.
- **Ledger lines** (hero facts, in-progress cert strip): the journal's native idiom for
  facts. Hero facts = one DM Mono line, copper dot separators, hairline rules above and
  below — never big-number-over-label stat tiles (banned hero-metric template). The cert
  strip = one slim dashed-copper row with the pulsing live dot.
- **Buttons:** pill (999px). Solid = copper fill, ink text. Ghost = 7% white fill, 16%
  white border, cream text; hover swaps to copper tint + copper border.
- **Kicker + headline pattern:** every section opens with a DM Mono copper kicker
  ("PROOF", "THE RECORD") followed by a Fraunces H2.
- **Timeline:** hairline spine, ink-raise dots, copper pulsing dot for "now"; each entry =
  mono tag (CERT / STUDY / TOOLS / MILESTONE / NOW) + optional mono date + DM Sans label.
- **Skill pills:** 5% white fill, hairline border, cream-soft text; copper tint on hover.
- **Difficulty tags** (`.diff-tag`, write-up tables): DM Mono label voice in a hairline
  pill, cream-faint. Neutral by design — no traffic-light colors (One Voice).
- **Header/tabs:** rgba(23,28,33,0.92) with 12px backdrop blur, copper tab indicator,
  1px copper-tinted bottom rule.

## 6. Do's and Don'ts

### Do:
- **Do** keep every token in sync with `docs/showcase/index.html` — the landing page is
  the source of truth for the register.
- **Do** use copper for meaning (active, current, verify, go-here) and nowhere else.
- **Do** brighten on hover (light copper → bright copper); darkening reads as disabled.
- **Do** keep glass fills between 3% and 8% white; above that it reads as a gray box.
- **Do** hide the sidebar/TOC on the home page (`hide: navigation, toc`) — it is a landing
  page, not a doc.

### Don't:
- **Don't** reintroduce the light cream surface on journal pages; the seam is the bug.
- **Don't** use emoji as section iconography — taxonomy is DM Mono text tags.
- **Don't** embed third-party light-themed iframes (Credly) on ink surfaces; render
  native cards that link out instead.
- **Don't** add a second accent, gradient text, or heavy backdrop blur on content cards.
- **Don't** use uppercase outside the DM Mono label voice.

# CLAUDE.md — Cybersecurity Journey

Personal cybersecurity learning portfolio for David Candela Martínez. Built with MkDocs Material, hosted on GitHub Pages, targeting a SOC Analyst career transition.

---

## Stack

| Layer | Technology |
|---|---|
| Site generator | MkDocs with `mkdocs-material` |
| Hosting | GitHub Pages (auto-deployed via Actions on push to `main`) |
| Publishing automation | `python publish.py` (interactive CLI wizard) |
| Dependencies | `pip install mkdocs-material` (no requirements.txt — install manually) |

---

## Project Structure

```
docs/
  index.md              — Portfolio homepage (certs, skills, learning log)
  stylesheets/
    extra.css           — Full theme override (do not touch lightly)
  tryhackme/
    index.md            — Table of all write-ups
    <slug>.md           — Individual challenge write-ups
  notes/
    index.md            — Index grouped by Linux / Windows / Security Tools
    <slug>.md           — Quick-reference tool/concept notes
  resources/
    index.md            — Curated external tools and platforms
mkdocs.yml              — MkDocs config (nav must be updated manually)
publish.py              — Automation script
.github/workflows/deploy.yml — GitHub Actions deploy
```

---

## Design System

Custom theme defined entirely in [docs/stylesheets/extra.css](docs/stylesheets/extra.css). It overrides the Material `slate` scheme with a warm, light palette — **not a dark theme** despite `scheme: slate`.

### Colour Palette

| Variable | Value | Role |
|---|---|---|
| `--cream` | `#FAF7F2` | Page/sidebar background |
| `--cream-mid` | `#F0EBE1` | Code blocks, table headers, cards |
| `--cream-border` | `#DDD5C8` | Borders |
| `--charcoal` | `#2C2C2C` | Body text, header/footer background |
| `--orange` | `#C96B3A` | Primary accent (links, active nav, admonitions) |
| `--orange-dark` | `#A5522B` | Hover state, inline code colour |

### Typography

- **H1, H2:** Playfair Display (serif), weight 700
- **H3–H6 + Body:** DM Sans (sans-serif), weight 600 / 400
- Both fonts loaded from Google Fonts in extra.css

### Custom HTML Components

These are raw HTML divs styled by extra.css. Use them only on the homepage (`docs/index.md`).

**Certification grid** — 4-column responsive grid of Credly badge embeds:
```html
<div class="cert-grid">
  <div class="cert-card">
    <div data-iframe-width="150" data-iframe-height="270"
         data-share-badge-id="<credly-id>"
         data-share-badge-host="https://www.credly.com"></div>
    <script type="text/javascript" async src="//cdn.credly.com/assets/utilities/embed.js"></script>
  </div>
</div>
```

**Skill pills** — labelled horizontal tag lists:
```html
<p class="skill-group-label">Category Label</p>
<div class="skill-pills">
  <span class="skill-pill">Tag Name</span>
</div>
```

**TryHackMe badge card:**
```html
<div class="thm-badge-card">
  <img src="https://tryhackme-badges.s3.amazonaws.com/Recluta.png" alt="TryHackMe Badge" />
</div>
```

---

## Writing Conventions

### TryHackMe Write-ups (`docs/tryhackme/`)

Structure every write-up in this order:
1. **Metadata table** — Date, Difficulty (with coloured circle emoji), Room Link
2. `## :clipboard: Overview` — 2–3 sentence room description
3. `## :dart: Key Learning Objectives` — checkbox tasklist (`- [x]`)
4. `## :pencil: Notes` — task-by-task subsections (`### Task N: …`)
5. `## :wrench: Tools Used` — table of Tool + Purpose
6. `## :bulb: Key Takeaways` — numbered list

Style rules:
- Write in first person, past tense ("I located…", "I used…")
- Show commands in fenced bash code blocks; explain flags inline
- Defang URLs and emails in write-ups (`hxxp[://]`, `@` → `[at]`)
- Use `!!! warning` and `!!! tip` admonitions for security notes and hints
- Difficulty uses emoji circles: `:green_circle:` Easy, `:orange_circle:` Medium, `:red_circle:` Hard

### Study Notes (`docs/notes/`)

Concise command-reference format:
- Minimal prose — explain the concept briefly, then show commands
- Use backtick inline code for commands within prose
- Fenced code blocks with language hint for multi-line examples
- No rigid section structure required; group by logical concept

### Shared Conventions

- Emoji section headers with Material/twemoji shortcodes (e.g. `## :scroll: Certifications`)
- `---` horizontal rules between major sections
- Tables for structured data (metadata, tools, commands)
- `admonition` blocks (`!!! note`, `!!! tip`, `!!! warning`, `!!! quote`) for callouts
- Do not add tags frontmatter — the tags plugin is enabled but currently unused

---

## Publishing Workflow

### Adding a new page

```bash
python publish.py
```

The wizard will:
1. Ask for room/topic name → generates a slug
2. Ask which section: **TryHackMe** or **Notes**
3. Collect metadata (category, difficulty for THM)
4. Open `$EDITOR` (or terminal paste) for content
5. Write the markdown file to the correct directory
6. Update the section's `index.md` automatically
7. Print a reminder to add the entry to `mkdocs.yml` nav
8. `git add . && git commit && git push`

**After running publish.py, you must manually add the nav entry to `mkdocs.yml`:**
```yaml
nav:
  - TryHackMe:
      - New Room Name: tryhackme/<slug>.md
```
publish.py prints the exact line to add.

### Manual deployment

```bash
mkdocs serve          # Local preview at http://127.0.0.1:8000
mkdocs gh-deploy      # Manual deploy (usually not needed — Actions handles it)
```

GitHub Actions deploys automatically on every push to `main`. Live within ~1–2 minutes at:
`https://david-candela.github.io/cybersecurity_journey/`

---

## Enabled Markdown Extensions

| Extension | Usage |
|---|---|
| `admonition` | `!!! note/tip/warning/quote "Title"` blocks |
| `pymdownx.details` | Collapsible `??? note` blocks |
| `pymdownx.superfences` | Fenced code blocks inside admonitions/tabs |
| `pymdownx.highlight` | Syntax highlighting with line numbers |
| `pymdownx.tabbed` | `=== "Tab Name"` tabbed content |
| `pymdownx.tasklist` | `- [x]` / `- [ ]` checkboxes |
| `pymdownx.emoji` | `:emoji_name:` shortcodes (twemoji) |
| `attr_list` | `{ .class }` attribute on elements |
| `md_in_html` | Markdown inside HTML divs |
| `tables` | GFM-style tables |
| `toc` | Auto TOC with permalink anchors |

---

## Content Guidelines

- **No spoiler flags** for CTF answers — document the process, not the exact flags
- Keep the Learning Log on `index.md` updated monthly with meaningful milestones
- Certifications section uses Credly embed scripts — add new badges via the cert-grid pattern above
- The `resources/index.md` page is for curated external links, not personal notes

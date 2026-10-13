# saeedsaedi.github.io

Personal portfolio and brand assets for **Saeed Saedi**, Technical Product Manager.

Live at: [saeedsaedi.github.io](https://saeedsaedi.github.io/)

## Stack

- Plain HTML and CSS, no framework, no runtime dependencies or third-party requests
- [Instrument Serif](https://github.com/Instrument/instrument-serif), [Inter](https://rsms.me/inter/) and [JetBrains Mono](https://www.jetbrains.com/lp/mono/), self-hosted in `assets/fonts/` (SIL OFL)
- A few lines of vanilla JavaScript for the mobile menu and the active nav link
- Case-study pages in `work/`, generated from one content file by `_tools/build-work.py`
- Printable résumé: `resume.html` → `RESUME.pdf`
- Hosted on GitHub Pages — push to `main` to deploy

## Local preview

```bash
python3 -m http.server 8080
# open http://localhost:8080
```

## Editing the case studies

The case-study text and diagrams live in `_tools/build-work.py`. After editing, regenerate the
pages in `work/` and the cards on the home page:

```bash
python3 _tools/build-work.py
```

The link-preview image (`assets/og-image.jpg`) and the icons are rendered from the HTML
sources in `_design/`; each file's header comment has the command to regenerate it.

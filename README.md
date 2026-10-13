# saeedsaedi.github.io

Personal portfolio and brand assets for **Saeed Saedi**, Technical Product Manager.

Live at: [saeedsaedi.github.io](https://saeedsaedi.github.io/)

## Stack

- Single `index.html`, no framework, no runtime dependencies or third-party requests
- [Tailwind CSS](https://tailwindcss.com/) v3, precompiled into `tailwind.css` (committed — nothing builds on deploy)
- [Inter](https://rsms.me/inter/) and [JetBrains Mono](https://www.jetbrains.com/lp/mono/), self-hosted in `assets/fonts/` (SIL OFL)
- Vanilla JavaScript (Intersection Observer for scroll animations and the active nav link)
- Printable résumé: `resume.html` → `RESUME.pdf`
- Hosted on GitHub Pages — push to `main` to deploy

## Local preview

```bash
python3 -m http.server 8080
# open http://localhost:8080
```

## Rebuilding the CSS

`tailwind.css` only contains the utility classes that are used. After adding or changing
classes in `index.html` or `script.js`, rebuild it:

```bash
npx tailwindcss@3.4.17 -i tailwind.input.css -o tailwind.css --minify
```

The link-preview image (`assets/og-image.jpg`) and the icons are rendered from the HTML
sources in `_design/`; each file's header comment has the command to regenerate it.

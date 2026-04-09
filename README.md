# saeedsaedi.github.io

Personal portfolio site for **Saeed Saedi**, Technical Product Manager.

Live at: [saeedsaedi.github.io](https://saeedsaedi.github.io/)

## Stack

- Single `index.html` — no build step, no framework
- [Tailwind CSS](https://tailwindcss.com/) via CDN
- [Inter](https://fonts.google.com/specimen/Inter) via Google Fonts
- Vanilla JavaScript (Intersection Observer for scroll animations)
- Hosted on GitHub Pages — push to `main` to deploy

## Local preview

```bash
python3 -m http.server 8080
# open http://localhost:8080
```

## Structure

All content is written directly in `index.html`. Sections in order:

1. **Nav** — fixed, blur backdrop, mobile-responsive
2. **Hero** — headline, key stats, CTAs
3. **About** — narrative + metric cards
4. **Experience** — timeline with rich bullet points and tech tags
5. **Skills** — categorized pill grid (Product, Backend, Infrastructure)
6. **Education** — compact row
7. **Contact** — email CTA + social links

## Updating content

Edit `index.html` directly. Content is static HTML — no data file or template engine. The `static/` directory and `info.json` are legacy files from the previous Bootstrap/jQuery version and are no longer used.

/** Tailwind build config — compiles tailwind.input.css into tailwind.css.
 *  Rebuild after changing utility classes in index.html or script.js:
 *    npx tailwindcss@3.4.17 -i tailwind.input.css -o tailwind.css --minify
 *  @type {import('tailwindcss').Config} */
module.exports = {
  content: ['./index.html', './script.js'],
  theme: {
    extend: {
      fontFamily: { sans: ['Inter', 'system-ui', 'sans-serif'] },
      // Secondary text (dates, labels, captions). Defined once in style.css :root;
      // keep it ≥ 4.5:1 against both the page (#09090b) and cards (#131316).
      colors: { dim: 'var(--text-dim)' },
    },
  },
};

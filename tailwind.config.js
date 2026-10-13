/** Tailwind build config — compiles tailwind.input.css into tailwind.css.
 *  Rebuild after changing utility classes in index.html or script.js:
 *    npx tailwindcss@3.4.17 -i tailwind.input.css -o tailwind.css --minify
 *  @type {import('tailwindcss').Config} */
module.exports = {
  content: ['./index.html', './script.js'],
  theme: {
    extend: {
      fontFamily: { sans: ['Inter', 'system-ui', 'sans-serif'] },
    },
  },
};

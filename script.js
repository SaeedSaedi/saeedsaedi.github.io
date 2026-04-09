/**
 * script.js — saeedsaedi.github.io
 *
 * Responsibilities:
 *  1. Mobile navigation menu toggle
 *  2. Scroll-triggered fade-in animations (IntersectionObserver)
 *  3. Active nav-link highlighting on scroll
 */

(function () {
  'use strict';

  /* ── 1. Mobile menu ─────────────────────────────── */
  var mobileBtn  = document.getElementById('mobile-btn');
  var mobileMenu = document.getElementById('mobile-menu');
  var iconOpen   = document.getElementById('icon-open');
  var iconClose  = document.getElementById('icon-close');

  if (mobileBtn && mobileMenu) {
    mobileBtn.addEventListener('click', function () {
      var isOpen = !mobileMenu.classList.contains('hidden');

      mobileMenu.classList.toggle('hidden', isOpen);
      iconOpen.classList.toggle('hidden', !isOpen);
      iconClose.classList.toggle('hidden', isOpen);
      mobileBtn.setAttribute('aria-expanded', String(!isOpen));
    });

    /* Close menu when any link inside is clicked */
    mobileMenu.querySelectorAll('a').forEach(function (link) {
      link.addEventListener('click', function () {
        mobileMenu.classList.add('hidden');
        iconOpen.classList.remove('hidden');
        iconClose.classList.add('hidden');
        mobileBtn.setAttribute('aria-expanded', 'false');
      });
    });
  }

  /* ── 2. Scroll-triggered fade-in ────────────────── */
  var fadeEls = document.querySelectorAll('.fade-in');

  if (fadeEls.length) {
    if ('IntersectionObserver' in window) {
      var fadeObserver = new IntersectionObserver(function (entries) {
        entries.forEach(function (entry, i) {
          if (entry.isIntersecting) {
            /* Stagger siblings that enter in the same batch */
            setTimeout(function () {
              entry.target.classList.add('visible');
            }, i * 70);
            fadeObserver.unobserve(entry.target);
          }
        });
      }, { threshold: 0.08, rootMargin: '0px 0px -40px 0px' });

      fadeEls.forEach(function (el) { fadeObserver.observe(el); });
    } else {
      /* Fallback: show immediately for browsers without IntersectionObserver */
      fadeEls.forEach(function (el) { el.classList.add('visible'); });
    }
  }

  /* ── 3. Active nav link on scroll ───────────────── */
  var sections = document.querySelectorAll('section[id]');
  var navLinks = document.querySelectorAll('nav a.nav-link');

  if (sections.length && navLinks.length && 'IntersectionObserver' in window) {
    var navObserver = new IntersectionObserver(function (entries) {
      entries.forEach(function (entry) {
        if (entry.isIntersecting) {
          var id = entry.target.getAttribute('id');
          navLinks.forEach(function (link) {
            var isActive = link.getAttribute('href') === '#' + id;
            link.classList.toggle('text-white', isActive);
            link.classList.toggle('text-zinc-400', !isActive);
          });
        }
      });
    }, { threshold: 0.4 });

    sections.forEach(function (section) { navObserver.observe(section); });
  }

})();

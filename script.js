/**
 * script.js — saeedsaedi.github.io
 *
 * Responsibilities:
 *  1. Mobile menu toggle (closes on link click and on Escape)
 *  2. Active nav link while scrolling the home page
 *  3. Footer year
 *
 * Everything works without this file: on small screens the nav links
 * simply stay visible (the .js class is set inline in <head>).
 */

(function () {
  'use strict';

  /* ── 1. Mobile menu ─────────────────────────────── */
  var nav = document.querySelector('.nav');
  var menuBtn = document.querySelector('.nav__menu');

  function setMenu(open) {
    nav.classList.toggle('is-open', open);
    menuBtn.setAttribute('aria-expanded', String(open));
  }

  if (nav && menuBtn) {
    menuBtn.addEventListener('click', function () {
      setMenu(!nav.classList.contains('is-open'));
    });
    nav.querySelectorAll('.nav__links a').forEach(function (link) {
      link.addEventListener('click', function () { setMenu(false); });
    });
    document.addEventListener('keydown', function (e) {
      if (e.key === 'Escape' && nav.classList.contains('is-open')) {
        setMenu(false);
        menuBtn.focus();
      }
    });
  }

  /* ── 2. Active nav link on scroll ───────────────── */
  /* A section is "current" while it crosses a thin band just above the middle
     of the viewport. Sections without a nav link (the hero, How I work, …)
     clear the highlight. */
  var links = document.querySelectorAll('.nav__links a[href^="#"]');
  var sections = document.querySelectorAll('main section[id]');

  if (links.length && sections.length && 'IntersectionObserver' in window) {
    var observer = new IntersectionObserver(function (entries) {
      entries.forEach(function (entry) {
        if (!entry.isIntersecting) return;
        var id = '#' + entry.target.id;
        links.forEach(function (link) {
          var active = link.getAttribute('href') === id;
          link.classList.toggle('is-active', active);
          if (active) link.setAttribute('aria-current', 'true');
          else link.removeAttribute('aria-current');
        });
      });
    }, { rootMargin: '-45% 0px -50% 0px' });

    sections.forEach(function (section) { observer.observe(section); });
  }

  /* Sections use content-visibility: auto, so sections next to a #hash target
     render (and change height) in the first frames after the jump. Re-align a
     few times while that settles; stop as soon as the visitor scrolls. */
  if (location.hash.length > 1) {
    var hashTarget = document.getElementById(decodeURIComponent(location.hash.slice(1)));
    if (hashTarget) {
      var userMoved = false;
      ['wheel', 'touchstart', 'keydown', 'mousedown'].forEach(function (type) {
        window.addEventListener(type, function () { userMoved = true; }, { once: true, passive: true });
      });
      window.addEventListener('load', function () {
        [0, 150, 400].forEach(function (delay) {
          setTimeout(function () { if (!userMoved) hashTarget.scrollIntoView(); }, delay);
        });
      });
    }
  }

  /* ── 3. Footer year ─────────────────────────────── */
  var yearEl = document.getElementById('year');
  if (yearEl) { yearEl.textContent = String(new Date().getFullYear()); }
})();

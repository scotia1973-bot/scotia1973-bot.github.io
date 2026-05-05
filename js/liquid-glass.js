/* ============================================
   GadgetHumans — Liquid Glass Interactions
   Variable blur nav, hero parallax, glass effects
   ============================================ */

(function() {
  'use strict';

  // ── 1. Variable Blur Nav ──
  const nav = document.querySelector('nav');
  if (nav) {
    let ticking = false;
    window.addEventListener('scroll', () => {
      if (!ticking) {
        window.requestAnimationFrame(() => {
          const scrollY = window.scrollY;
          if (scrollY > 20) {
            nav.classList.add('nav-solid');
          } else {
            nav.classList.remove('nav-solid');
          }
          ticking = false;
        });
        ticking = true;
      }
    });
  }

  // ── 2. Hero Orb Mouse Parallax ──
  const orbs = document.querySelectorAll('.hero-orb');
  if (orbs.length > 0) {
    const hero = document.querySelector('.hero');
    if (hero) {
      hero.addEventListener('mousemove', (e) => {
        const rect = hero.getBoundingClientRect();
        const x = (e.clientX - rect.left) / rect.width - 0.5;
        const y = (e.clientY - rect.top) / rect.height - 0.5;

        orbs.forEach((orb, i) => {
          const speed = 15 + i * 8;
          const moveX = x * speed;
          const moveY = y * speed;
          orb.style.transform = `translate(${moveX}px, ${moveY}px)`;
        });
      });
    }
  }

  // ── 3. Product Image Fallback ──
  // If a product image fails to load, show the placeholder emoji
  const productImgs = document.querySelectorAll('.product-img');
  productImgs.forEach(img => {
    img.addEventListener('error', function() {
      this.style.display = 'none';
      const placeholder = this.nextElementSibling;
      if (placeholder && placeholder.classList.contains('product-img-placeholder')) {
        placeholder.style.display = 'flex';
      }
    });
  });

  // ── 4. Glass Card Tilt Effect (optional, subtle) ──
  const glassCards = document.querySelectorAll('.gear-card, .card, .tool-card, .cat-card');
  if (glassCards.length > 0 && window.innerWidth > 768) {
    glassCards.forEach(card => {
      card.addEventListener('mousemove', (e) => {
        const rect = card.getBoundingClientRect();
        const x = e.clientX - rect.left;
        const y = e.clientY - rect.top;
        const centerX = rect.width / 2;
        const centerY = rect.height / 2;

        const rotateX = (y - centerY) / 20;
        const rotateY = (centerX - x) / 20;

        card.style.transform =
          `perspective(800px) rotateX(${rotateX}deg) rotateY(${rotateY}deg) translateY(-4px)`;
      });

      card.addEventListener('mouseleave', () => {
        card.style.transform = '';
      });
    });
  }

  // ── 5. Nav Hamburger Toggle ──
  const toggle = document.querySelector('.nav-toggle');
  const navLinks = document.querySelector('.nav-links');
  if (toggle && navLinks) {
    toggle.addEventListener('click', () => {
      navLinks.classList.toggle('open');
      toggle.textContent = navLinks.classList.contains('open') ? '✕' : '☰';
    });

    // Close on outside click
    document.addEventListener('click', (e) => {
      if (!e.target.closest('nav') && navLinks.classList.contains('open')) {
        navLinks.classList.remove('open');
        toggle.textContent = '☰';
      }
    });
  }

})();

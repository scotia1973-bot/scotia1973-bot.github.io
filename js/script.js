// GadgetHumans — Shared Scripts
(function() {
  'use strict';

  // Mobile nav toggle
  var toggle = document.querySelector('.nav-toggle');
  var links = document.querySelector('.nav-links');
  if (toggle && links) {
    toggle.addEventListener('click', function(e) {
      e.stopPropagation();
      links.classList.toggle('open');
      toggle.textContent = links.classList.contains('open') ? '✕' : '☰';
    });
    document.addEventListener('click', function(e) {
      if (!e.target.closest('nav') && links.classList.contains('open')) {
        links.classList.remove('open');
        toggle.textContent = '☰';
      }
    });
  }

  // Active nav link
  var path = window.location.pathname;
  document.querySelectorAll('.nav-links a').forEach(function(a) {
    if (path.indexOf(a.getAttribute('href')) !== -1 && a.getAttribute('href') !== '/') {
      a.classList.add('active');
    }
  });

  // Toast notification
  window.showToast = function(msg) {
    var t = document.getElementById('toast');
    if (!t) return;
    t.textContent = msg;
    t.classList.add('show');
    clearTimeout(t._hide);
    t._hide = setTimeout(function() { t.classList.remove('show'); }, 2500);
  };

  // Copy to clipboard
  window.copyToClipboard = function(text) {
    navigator.clipboard.writeText(text).then(function() {
      showToast('Copied!');
    });
  };

  // Smooth scroll for anchor links
  document.querySelectorAll('a[href^="#"]').forEach(function(a) {
    a.addEventListener('click', function(e) {
      var id = a.getAttribute('href').slice(1);
      var el = document.getElementById(id);
      if (el) {
        e.preventDefault();
        el.scrollIntoView({ behavior: 'smooth', block: 'start' });
      }
    });
  });
})();

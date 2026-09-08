// Minimal lightbox for gallery pages
document.addEventListener('DOMContentLoaded', function () {
  var links = document.querySelectorAll('[data-lightbox]');
  if (!links.length) return;

  var overlay = document.createElement('div');
  overlay.className = 'lightbox-overlay';
  overlay.innerHTML = '<button class="lightbox-close" aria-label="Close">&times;</button><img alt="">';
  document.body.appendChild(overlay);
  var imgEl = overlay.querySelector('img');

  function open(src, alt) {
    imgEl.src = src;
    imgEl.alt = alt || '';
    overlay.classList.add('open');
  }
  function close() {
    overlay.classList.remove('open');
    imgEl.src = '';
  }

  links.forEach(function (link) {
    link.addEventListener('click', function (e) {
      e.preventDefault();
      var img = link.querySelector('img');
      open(link.getAttribute('href'), img ? img.alt : '');
    });
  });

  overlay.addEventListener('click', function (e) {
    if (e.target === overlay || e.target.classList.contains('lightbox-close')) close();
  });
  document.addEventListener('keydown', function (e) {
    if (e.key === 'Escape') close();
  });
});

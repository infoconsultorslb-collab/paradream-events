// Mobile nav toggle + dropdown + cookie banner
document.addEventListener('DOMContentLoaded', function () {
  var toggle = document.querySelector('.nav-toggle');
  var nav = document.getElementById('site-nav');
  if (toggle && nav) {
    toggle.addEventListener('click', function () {
      var open = nav.classList.toggle('open');
      toggle.setAttribute('aria-expanded', open ? 'true' : 'false');
    });
  }

  document.querySelectorAll('.has-dropdown > a').forEach(function (link) {
    link.addEventListener('click', function (e) {
      if (window.innerWidth <= 900) {
        e.preventDefault();
        link.parentElement.classList.toggle('open');
      }
    });
  });

  var banner = document.getElementById('cookie-banner');
  var acceptBtn = document.getElementById('cookie-accept');
  if (banner) {
    try {
      if (!localStorage.getItem('paradream-cookie-accepted')) {
        banner.hidden = false;
      }
    } catch (e) {
      banner.hidden = false;
    }
  }
  if (acceptBtn) {
    acceptBtn.addEventListener('click', function () {
      try { localStorage.setItem('paradream-cookie-accepted', '1'); } catch (e) {}
      banner.hidden = true;
    });
  }
});

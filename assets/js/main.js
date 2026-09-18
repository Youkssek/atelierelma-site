/* Atelier ELMA — interactions (aucune dépendance) */
(function () {
  var d = document, b = d.body, root = d.documentElement;
  var reduce = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  var fine = window.matchMedia('(hover:hover) and (pointer:fine)').matches;
  root.classList.add('js');
  var vh = window.innerHeight, vw = window.innerWidth;
  window.addEventListener('resize', function () { vh = window.innerHeight; vw = window.innerWidth; });

  /* Préchargeur : une fois par session */
  var loader = d.getElementById('loader'), seen = false;
  try { seen = sessionStorage.getItem('elma-loaded') === '1'; } catch (e) {}
  function ready() { b.classList.add('ready'); }
  if (loader) {
    if (seen || reduce) { loader.remove(); ready(); }
    else {
      setTimeout(function () { loader.classList.add('done'); ready(); }, 1500);
      setTimeout(function () { loader.remove(); }, 2600);
      try { sessionStorage.setItem('elma-loaded', '1'); } catch (e) {}
    }
  } else { ready(); }

  /* Titres découpés en mots */
  d.querySelectorAll('[data-words]').forEach(function (el) {
    var i = 0;
    el.innerHTML = el.textContent.split(/\s+/).filter(Boolean).map(function (w) {
      return '<span class="w"><span style="--i:' + (i++) + '">' + w + '</span></span>';
    }).join(' ');
  });

  /* Hero en lamelles : on duplique l'image dans N lamelles */
  var hero = d.querySelector('.hero');
  var heroFrame = hero && hero.querySelector('.frame'), heroWrap = hero && hero.querySelector('.wrap');
  if (hero) {
    var src = hero.getAttribute('data-src'), alt = hero.getAttribute('data-alt') || '', n = 6, slats = '';
    for (var k = 0; k < n; k++) slats += '<div class="slat" style="--i:' + k + ';--n:' + n + '"><img src="' + src + '" alt="' + (k ? '' : alt) + '"></div>';
    heroFrame.insertAdjacentHTML('afterbegin', '<div class="slats">' + slats + '</div>');
  }

  /* Révélations */
  var io = new IntersectionObserver(function (entries) {
    entries.forEach(function (en) { if (en.isIntersecting) { en.target.classList.add('in'); io.unobserve(en.target); } });
  }, { rootMargin: '0px 0px -10% 0px', threshold: 0.08 });
  d.querySelectorAll('.reveal, .img-reveal, .line-grow, [data-words-in]').forEach(function (el) { io.observe(el); });

  /* Récit à image fixe (atelier) */
  var storyImgs = d.querySelectorAll('.story-media img');
  if (storyImgs.length) {
    var so = new IntersectionObserver(function (entries) {
      entries.forEach(function (en) {
        if (!en.isIntersecting) return;
        var i = +en.target.getAttribute('data-i');
        storyImgs.forEach(function (im, j) { im.classList.toggle('on', j === i); });
      });
    }, { rootMargin: '-40% 0px -40% 0px' });
    d.querySelectorAll('.story-block').forEach(function (bl) { so.observe(bl); });
  }

  /* Expertises (accueil) : l'image suit la ligne survolée */
  var xpRows = d.querySelectorAll('.xp-list li'), xpImgs = d.querySelectorAll('.xp-media img');
  function xpSet(i) {
    xpRows.forEach(function (r, j) { r.classList.toggle('is-active', j === i); });
    xpImgs.forEach(function (im, j) { im.classList.toggle('on', j === i); });
  }
  if (xpRows.length) {
    xpSet(0);
    xpRows.forEach(function (r, i) {
      r.addEventListener('mouseenter', function () { xpSet(i); });
      r.addEventListener('focusin', function () { xpSet(i); });
    });
  }

  /* Boucle rAF : parallaxe, mots, hero, bande horizontale */
  var plx = [].slice.call(d.querySelectorAll('[data-parallax] img'));
  var words = [].slice.call(d.querySelectorAll('.words'));
  words.forEach(function (w) {
    w.innerHTML = w.textContent.split(/\s+/).filter(Boolean).map(function (t) { return '<span>' + t + '</span>'; }).join(' ');
    w._spans = [].slice.call(w.children);
  });
  var hs = d.querySelector('.hs'), hsTrack = hs && hs.querySelector('.hs-track'), hsBar = hs && hs.querySelector('.hs-progress i');
  function sizeHs() {
    if (!hs) return;
    if (vw <= 900) { hs.style.height = ''; return; }
    var extra = hsTrack.scrollWidth - vw;
    hs.style.height = (vh + extra * 1.15) + 'px';
  }
  sizeHs(); window.addEventListener('resize', sizeHs);

  var ticking = false;
  function frame() {
    ticking = false;
    var y = window.pageYOffset;
    if (!reduce) plx.forEach(function (img) {
      var r = img.parentElement.getBoundingClientRect();
      if (r.bottom < 0 || r.top > vh) return;
      img.style.transform = 'translateY(' + (((r.top + r.height / 2 - vh / 2) / vh) * -8) + '%)';
    });
    words.forEach(function (w) {
      var r = w.getBoundingClientRect(), start = vh * 0.85, end = vh * 0.35;
      var prog = Math.min(1, Math.max(0, (start - r.top) / (start - end + r.height * 0.6)));
      var cnt = Math.round(prog * w._spans.length);
      w._spans.forEach(function (s, i) { s.classList.toggle('on', i < cnt); });
    });
    if (hero && !reduce && y < vh * 1.2) {
      var p = Math.min(1, y / vh);
      heroFrame.style.transform = 'scale(' + (1 - p * 0.08) + ') translateY(' + (p * 6) + '%)';
      heroFrame.style.borderRadius = (p * 28) + 'px';
      heroWrap.style.transform = 'translateY(' + (p * -60) + 'px)';
      heroWrap.style.opacity = 1 - p * 1.6;
    }
    if (hs && vw > 900) {
      var r2 = hs.getBoundingClientRect(), total = hs.offsetHeight - vh;
      var pr = Math.min(1, Math.max(0, -r2.top / total));
      hsTrack.style.transform = 'translateX(' + (-pr * (hsTrack.scrollWidth - vw)) + 'px)';
      if (hsBar) hsBar.style.transform = 'scaleX(' + pr + ')';
    }
  }
  function onScroll() { if (!ticking) { ticking = true; requestAnimationFrame(frame); } }
  window.addEventListener('scroll', onScroll, { passive: true });
  window.addEventListener('resize', onScroll);
  frame();

  /* En-tête */
  var header = d.querySelector('.site-header'), lastY = 0, overHero = header && header.classList.contains('over');
  function headerState() {
    var y = window.pageYOffset, limit = overHero ? vh * 0.75 : 40;
    header.classList.toggle('is-solid', y > limit);
    header.classList.toggle('is-hidden', y > lastY && y > 200 && !d.querySelector('.nav.is-open'));
    lastY = y;
  }
  if (header) { headerState(); window.addEventListener('scroll', headerState, { passive: true }); }
  var btn = d.querySelector('.menu-btn'), nav = d.querySelector('.nav');
  if (btn && nav) btn.addEventListener('click', function () {
    var open = nav.classList.toggle('is-open');
    btn.setAttribute('aria-expanded', open ? 'true' : 'false');
    btn.textContent = open ? 'Fermer' : 'Menu';
    if (open) header.classList.add('is-solid');
  });

  /* Curseur, image flottante et inclinaison : souris fine uniquement */
  if (fine && !reduce) {
    root.classList.add('has-cursor');
    var cur = d.createElement('div'); cur.className = 'cursor';
    var ring = d.createElement('div'); ring.className = 'cursor-ring'; ring.innerHTML = '<span>Voir</span>';
    b.appendChild(cur); b.appendChild(ring);
    var mx = vw / 2, my = vh / 2, rx = mx, ry = my;
    d.addEventListener('mousemove', function (e) { mx = e.clientX; my = e.clientY; cur.style.left = mx + 'px'; cur.style.top = my + 'px'; });
    var fl = d.querySelector('.float-img'), fimg = fl && fl.querySelector('img');
    (function lerp() {
      rx += (mx - rx) * 0.18; ry += (my - ry) * 0.18;
      ring.style.left = rx + 'px'; ring.style.top = ry + 'px';
      if (fl) { fl.style.left = rx + 'px'; fl.style.top = ry + 'px'; }
      requestAnimationFrame(lerp);
    })();
    d.addEventListener('mouseover', function (e) {
      var v = e.target.closest('[data-cursor]'), a = e.target.closest('a, button');
      b.classList.toggle('c-view', !!v); b.classList.toggle('c-link', !v && !!a);
      if (v) ring.querySelector('span').textContent = v.getAttribute('data-cursor') || 'Voir';
    });
    if (fl) d.querySelectorAll('.index a[data-img]').forEach(function (a) {
      a.addEventListener('mouseenter', function () { fimg.src = a.getAttribute('data-img'); fl.classList.add('on'); });
      a.addEventListener('mouseleave', function () { fl.classList.remove('on'); });
    });
    d.querySelectorAll('.tilt').forEach(function (el) {
      el.addEventListener('mousemove', function (e) {
        var r = el.getBoundingClientRect(), px = (e.clientX - r.left) / r.width - 0.5, py = (e.clientY - r.top) / r.height - 0.5;
        el.style.transform = 'perspective(1200px) rotateX(' + (-py * 4) + 'deg) rotateY(' + (px * 4) + 'deg)';
      });
      el.addEventListener('mouseleave', function () { el.style.transform = ''; });
    });
  }

  /* Transition entre pages */
  var veil = d.getElementById('veil');
  if (veil && !reduce) d.addEventListener('click', function (e) {
    var a = e.target.closest('a[href]');
    if (!a || a.target === '_blank' || e.metaKey || e.ctrlKey) return;
    var href = a.getAttribute('href');
    if (!href || /^(#|mailto:|tel:|https?:)/.test(href)) return;
    e.preventDefault(); b.classList.add('leaving');
    setTimeout(function () { window.location.href = href; }, 420);
  });
  window.addEventListener('pageshow', function () { b.classList.remove('leaving'); });
})();

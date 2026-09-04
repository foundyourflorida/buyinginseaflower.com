/* Buying in SeaFlower — site behaviors (no dependencies) */
(function () {
  'use strict';
  var d = document, w = window;
  var CFG = w.SITE_CONFIG || {};

  /* ---- analytics helper (GA4 optional) ---- */
  function track(name, params) {
    try { if (typeof w.gtag === 'function') w.gtag('event', name, params || {}); } catch (e) {}
  }

  /* ---- header shadow ---- */
  var header = d.querySelector('.header');
  function onScroll() { if (header) header.classList.toggle('is-scrolled', w.scrollY > 8); }
  w.addEventListener('scroll', onScroll, { passive: true }); onScroll();

  /* ---- mobile drawer ---- */
  var drawer = d.getElementById('drawer');
  var toggle = d.querySelector('.nav-toggle');
  function openDrawer() { if (!drawer) return; drawer.classList.add('is-open'); d.body.style.overflow = 'hidden'; toggle && toggle.setAttribute('aria-expanded', 'true'); var c = drawer.querySelector('.drawer__close'); c && c.focus(); }
  function closeDrawer() { if (!drawer) return; drawer.classList.remove('is-open'); d.body.style.overflow = ''; toggle && toggle.setAttribute('aria-expanded', 'false'); toggle && toggle.focus(); }
  if (toggle && drawer) {
    toggle.addEventListener('click', openDrawer);
    drawer.querySelectorAll('.drawer__scrim,.drawer__close').forEach(function (el) { el.addEventListener('click', closeDrawer); });
    d.addEventListener('keydown', function (e) { if (e.key === 'Escape' && drawer.classList.contains('is-open')) closeDrawer(); });
  }

  /* ---- reveal on scroll ---- */
  var reveals = d.querySelectorAll('.reveal');
  if ('IntersectionObserver' in w && reveals.length) {
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (en) { if (en.isIntersecting) { en.target.classList.add('is-visible'); io.unobserve(en.target); } });
    }, { rootMargin: '0px 0px -8% 0px', threshold: 0.08 });
    reveals.forEach(function (el) {
      var r = el.getBoundingClientRect();
      if (r.top < w.innerHeight && r.bottom > 0) { el.classList.add('is-visible'); } else { io.observe(el); }
    });
  } else { reveals.forEach(function (el) { el.classList.add('is-visible'); }); }

  /* ---- lite YouTube facade ---- */
  function activateVideo(el, autoplay) {
    if (el.classList.contains('is-active')) return;
    var id = el.getAttribute('data-id');
    var start = el.getAttribute('data-start');
    var params = 'rel=0&modestbranding=1&playsinline=1' + (autoplay ? '&autoplay=1' : '') + (start ? '&start=' + start : '');
    var iframe = d.createElement('iframe');
    iframe.setAttribute('allow', 'accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share');
    iframe.setAttribute('allowfullscreen', '');
    iframe.setAttribute('title', el.getAttribute('data-title') || 'YouTube video');
    iframe.src = 'https://www.youtube-nocookie.com/embed/' + id + '?' + params;
    el.classList.add('is-active');
    el.appendChild(iframe);
    track('video_play', { video_id: id, video_title: el.getAttribute('data-title') || '' });
  }
  d.querySelectorAll('.lite-yt').forEach(function (el) {
    el.addEventListener('click', function () { activateVideo(el, true); });
    el.addEventListener('keydown', function (e) { if (e.key === 'Enter' || e.key === ' ') { e.preventDefault(); activateVideo(el, true); } });
  });

  /* ---- FAQ search + category filter ---- */
  var faqSearch = d.getElementById('faq-search');
  var faqChips = d.querySelectorAll('[data-faq-filter]');
  var faqItems = d.querySelectorAll('.faq[data-cat]');
  var faqGroups = d.querySelectorAll('.faq-group[data-cat]');
  var faqEmpty = d.getElementById('faq-empty');
  var activeCat = 'all';
  function norm(s) { return (s || '').toLowerCase().replace(/[^a-z0-9\s$%]/g, ' '); }
  function applyFaq() {
    var q = norm(faqSearch ? faqSearch.value.trim() : '');
    var terms = q ? q.split(/\s+/).filter(Boolean) : [];
    var shown = 0;
    faqItems.forEach(function (it) {
      var text = norm(it.getAttribute('data-text') || it.textContent);
      var catOk = activeCat === 'all' || it.getAttribute('data-cat') === activeCat;
      var qOk = terms.every(function (t) { return text.indexOf(t) !== -1; });
      var ok = catOk && qOk;
      it.classList.toggle('is-hidden', !ok);
      if (ok) shown++;
      if (ok && terms.length && !it.open) it.open = true;
      if (!terms.length && it.hasAttribute('data-auto-open')) it.open = false;
    });
    faqGroups.forEach(function (g) {
      var any = g.querySelector('.faq:not(.is-hidden)');
      g.classList.toggle('is-hidden', !any);
    });
    if (faqEmpty) faqEmpty.classList.toggle('is-visible', shown === 0);
    var count = d.getElementById('faq-count');
    if (count) count.textContent = shown + ' question' + (shown === 1 ? '' : 's');
  }
  if (faqSearch) {
    var t;
    faqSearch.addEventListener('input', function () { clearTimeout(t); t = setTimeout(function () { applyFaq(); if (faqSearch.value.length > 2) track('faq_search', { search_term: faqSearch.value }); }, 120); });
  }
  faqChips.forEach(function (chip) {
    chip.addEventListener('click', function (e) {
      e.preventDefault();
      activeCat = chip.getAttribute('data-faq-filter');
      faqChips.forEach(function (c) { c.classList.toggle('is-active', c === chip); c.setAttribute('aria-pressed', c === chip ? 'true' : 'false'); });
      applyFaq();
    });
  });
  if (faqItems.length && (faqSearch || faqChips.length)) applyFaq();
  /* open FAQ from hash */
  function openHash() {
    if (!location.hash) return;
    var target = d.getElementById(decodeURIComponent(location.hash.slice(1)));
    if (target && target.tagName === 'DETAILS') { target.open = true; setTimeout(function () { target.scrollIntoView({ block: 'start' }); }, 50); }
  }
  w.addEventListener('hashchange', openHash); openHash();
  d.querySelectorAll('details.faq').forEach(function (el) {
    el.addEventListener('toggle', function () { if (el.open) track('faq_open', { question: (el.querySelector('summary') || {}).textContent || '' }); });
  });

  /* ---- generic chip filters: chips carry data-filter="group:value", items carry data-filter-group="group" data-cat="a b" ---- */
  d.querySelectorAll('[data-filter]').forEach(function (chip) {
    chip.addEventListener('click', function (e) {
      e.preventDefault();
      var parts = chip.getAttribute('data-filter').split(':'); var group = parts[0], val = parts[1];
      d.querySelectorAll('[data-filter^="' + group + ':"]').forEach(function (c) { c.classList.toggle('is-active', c === chip); c.setAttribute('aria-pressed', c === chip ? 'true' : 'false'); });
      d.querySelectorAll('[data-filter-group="' + group + '"]').forEach(function (it) { it.hidden = !(val === 'all' || (it.getAttribute('data-cat') || '').split(' ').indexOf(val) !== -1); });
      track('filter', { group: group, value: val });
    });
  });

  /* ---- sortable tables ---- */
  d.querySelectorAll('table[data-sortable]').forEach(function (tbl) {
    var ths = tbl.querySelectorAll('thead th');
    ths.forEach(function (th, idx) {
      if (!th.textContent.trim()) return;
      th.classList.add('is-sortable'); th.setAttribute('tabindex', '0'); th.setAttribute('role', 'button');
      var dir = 1;
      function sort() {
        var rows = Array.prototype.slice.call(tbl.querySelectorAll('tbody tr'));
        rows.sort(function (a, b) {
          var ca = a.children[idx], cb = b.children[idx];
          var va = ca.getAttribute('data-sort'), vb = cb.getAttribute('data-sort');
          if (va !== null && vb !== null) {
            var fa = parseFloat(va) || 0, fb = parseFloat(vb) || 0;
            if (!fa && !fb) return 0; if (!fa) return 1; if (!fb) return -1;
            return (fa - fb) * dir;
          }
          var ta = ca.textContent.trim().toLowerCase(), tb = cb.textContent.trim().toLowerCase();
          var na = parseFloat(ta.replace(/[^0-9.]/g, '')), nb = parseFloat(tb.replace(/[^0-9.]/g, ''));
          if (!isNaN(na) && !isNaN(nb) && /^\$?\d/.test(ta) && /^\$?\d/.test(tb)) return (na - nb) * dir;
          return ta < tb ? -dir : ta > tb ? dir : 0;
        });
        var tb = tbl.querySelector('tbody'); rows.forEach(function (r) { tb.appendChild(r); });
        ths.forEach(function (o) { o.removeAttribute('aria-sort'); }); th.setAttribute('aria-sort', dir === 1 ? 'ascending' : 'descending');
        dir = -dir;
      }
      th.addEventListener('click', sort);
      th.addEventListener('keydown', function (e) { if (e.key === 'Enter' || e.key === ' ') { e.preventDefault(); sort(); } });
    });
  });

  /* ---- TOC active state ---- */
  var tocLinks = d.querySelectorAll('.toc a[href^="#"]');
  if (tocLinks.length && 'IntersectionObserver' in w) {
    var map = {};
    tocLinks.forEach(function (a) { var id = a.getAttribute('href').slice(1); var sec = d.getElementById(id); if (sec) map[id] = a; });
    var tio = new IntersectionObserver(function (entries) {
      entries.forEach(function (en) {
        if (en.isIntersecting) { tocLinks.forEach(function (a) { a.classList.remove('is-active'); }); var a = map[en.target.id]; a && a.classList.add('is-active'); }
      });
    }, { rootMargin: '-20% 0px -70% 0px', threshold: 0 });
    Object.keys(map).forEach(function (id) { tio.observe(d.getElementById(id)); });
  }

  /* ---- lead forms ---- */
  function getUTM() {
    var out = {}; try { var p = new URLSearchParams(location.search); ['utm_source', 'utm_medium', 'utm_campaign', 'utm_content', 'utm_term', 'gclid'].forEach(function (k) { if (p.get(k)) out[k] = p.get(k); }); } catch (e) {}
    return out;
  }
  d.querySelectorAll('form[data-lead-form]').forEach(function (form) {
    var status = form.querySelector('.form__status');
    var btn = form.querySelector('button[type="submit"]');
    var endpoint = form.getAttribute('action') || CFG.formEndpoint || '';
    var pageField = form.querySelector('input[name="page"]'); if (pageField) pageField.value = location.href;
    var utm = getUTM(); Object.keys(utm).forEach(function (k) { var i = d.createElement('input'); i.type = 'hidden'; i.name = k; i.value = utm[k]; form.appendChild(i); });
    form.addEventListener('submit', function (e) {
      e.preventDefault();
      var hp = form.querySelector('input[name="_gotcha"]'); if (hp && hp.value) return;
      var consent = form.querySelector('input[name="consent"]');
      if (consent && !consent.checked) { show('err', 'Please tick the consent box so I can reply to you.'); consent.focus(); return; }
      if (!endpoint || endpoint.indexOf('YOUR_FORM_ID') !== -1) {
        /* No endpoint configured yet: fall back to email so no lead is lost. */
        var fd = new FormData(form); var lines = [];
        fd.forEach(function (v, k) { if (k.charAt(0) !== '_' && v) lines.push(k + ': ' + v); });
        location.href = 'mailto:' + (CFG.email || '') + '?subject=' + encodeURIComponent('SeaFlower inquiry from ' + (fd.get('name') || 'website')) + '&body=' + encodeURIComponent(lines.join('\n'));
        show('ok', 'Opening your email app with the details filled in. If nothing opens, call or text ' + (CFG.phoneDisplay || '') + '.');
        return;
      }
      btn && (btn.disabled = true);
      var raw = {}; new FormData(form).forEach(function (v, k) { raw[k] = v; });
      /* Payload in the shape of the Found Your Florida lead API (foundyourflorida.com/api/leads). */
      var extras = [];
      if (raw.timeline) extras.push('Timeline: ' + raw.timeline);
      if (raw.interest) extras.push('Interest: ' + raw.interest);
      if (raw.builder) extras.push('Builder: ' + raw.builder);
      if (raw.message) extras.push('Message: ' + raw.message);
      extras.push('Page: ' + location.href);
      var payload;
      if (endpoint.indexOf('formsubmit.co') !== -1) {
        /* FormSubmit: emails the submission to the address in the endpoint. */
        payload = {
          _subject: 'SeaFlower lead: ' + (raw.name || 'unknown') + ' (' + (raw.interest || 'inquiry') + ')',
          _template: 'table', _captcha: 'false', _replyto: raw.email, _honey: hp ? hp.value : '',
          name: raw.name, email: raw.email, phone: raw.phone || '', timeline: raw.timeline || '', interest: raw.interest || 'SeaFlower',
          builder: raw.builder || '', message: raw.message || '', form: raw.form || 'lead', page: location.href,
          sms_consent: (consent && consent.checked) ? 'yes' : 'no', submitted_at: new Date().toISOString(),
          utm_source: utm.utm_source || '', utm_medium: utm.utm_medium || '', utm_campaign: utm.utm_campaign || ''
        };
      } else {
        /* Found Your Florida lead API shape (foundyourflorida.com/api/leads). */
        payload = {
          name: raw.name, email: raw.email, phone: raw.phone || null,
          sourcePage: 'buyinginseaflower-' + (raw.form || 'lead'),
          interestType: raw.interest || 'SeaFlower',
          communityInterest: 'SeaFlower',
          message: '[buyinginseaflower.com] ' + extras.join(' | '),
          utmSource: utm.utm_source || 'buyinginseaflower.com', utmMedium: utm.utm_medium || 'website', utmCampaign: utm.utm_campaign || (raw.form || 'lead'), utmContent: utm.utm_content || location.pathname
        };
      }
      fetch(endpoint, { method: 'POST', headers: { 'Accept': 'application/json', 'Content-Type': 'application/json' }, body: JSON.stringify(payload) })
        .then(function (r) { if (!r.ok) throw new Error('bad status ' + r.status); return r.json().catch(function () { return {}; }); })
        .then(function () {
          form.reset();
          show('ok', form.getAttribute('data-success') || 'Got it — I will reach out shortly. Want to skip the wait? Book a time on the calendar or text me.');
          track('generate_lead', { form_id: form.id || 'lead', page: location.pathname });
          var next = form.getAttribute('data-redirect'); if (next) setTimeout(function () { location.href = next; }, 900);
        })
        .catch(function () {
          /* Never lose a lead: fall back to a pre-filled email. */
          var lines = ['Name: ' + raw.name, 'Email: ' + raw.email, 'Phone: ' + (raw.phone || '')].concat(extras);
          location.href = 'mailto:' + (CFG.email || '') + '?subject=' + encodeURIComponent('SeaFlower inquiry from ' + (raw.name || 'website')) + '&body=' + encodeURIComponent(lines.join('\n'));
          show('ok', 'The form service did not respond, so I opened an email with your details filled in. You can also call or text ' + (CFG.phoneDisplay || '') + '.');
        })
        .finally(function () { btn && (btn.disabled = false); });
    });
    function show(kind, msg) { if (!status) return; status.className = 'form__status is-' + kind; status.textContent = msg; status.setAttribute('role', 'status'); }
  });

  /* ---- outbound + call tracking ---- */
  d.querySelectorAll('a[href^="tel:"]').forEach(function (a) { a.addEventListener('click', function () { track('click_call', { page: location.pathname }); }); });
  d.querySelectorAll('a[href^="sms:"]').forEach(function (a) { a.addEventListener('click', function () { track('click_text', { page: location.pathname }); }); });
  d.querySelectorAll('a[data-cta]').forEach(function (a) { a.addEventListener('click', function () { track('cta_click', { cta: a.getAttribute('data-cta'), page: location.pathname }); }); });

  /* ---- current year ---- */
  d.querySelectorAll('[data-year]').forEach(function (el) { el.textContent = new Date().getFullYear(); });
})();

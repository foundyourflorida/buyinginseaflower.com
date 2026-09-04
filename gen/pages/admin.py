"""Private admin dashboard at /admin/ (noindex, excluded from sitemap/llms, disallowed in robots).
Client-side password gate: the page compares a SHA-256 hash of the entered password. This keeps casual visitors out;
it is not bank-grade security, and nothing on the page is secret (every link requires its own Google/Calendly login)."""
from ..config import SITE
from ..components import *  # noqa
from ..html import esc

PW_HASH = "b69539cf376f06e98a761d9a5806fe346ce6b58ad153b6f6020b762b801dc8ea"


def pages():
    dash = f"""
<section class="section section--flush-top" style="padding-top:30px"><div class="container">
  <div class="grid grid-3" id="admin-grid">
    <div class="card"><div class="card__icon">{icon('trending')}</div><h3>Traffic</h3><p>Google Analytics 4 is installed on every page (measurement ID {esc(SITE['ga_id'])}). Events tracked: form submissions (<code>generate_lead</code>), calls, texts, CTA clicks, video plays, FAQ opens and searches, filters.</p>
      <ul class="stack" style="padding-left:1.1em;margin-top:12px;font-size:15px"><li><a href="https://analytics.google.com/analytics/web/" target="_blank" rel="noopener">Open Google Analytics</a> (Reports &rarr; Realtime for live visitors; Engagement &rarr; Events for leads and calls)</li><li><a href="https://search.google.com/search-console" target="_blank" rel="noopener">Google Search Console</a> (add <code>buyinginseaflower.com</code> as a Domain property; verifying through the Google Analytics tag works automatically)</li><li><a href="https://www.bing.com/webmasters" target="_blank" rel="noopener">Bing Webmaster Tools</a> (ChatGPT search reads Bing&rsquo;s index; import from Search Console in one click)</li></ul></div>
    <div class="card"><div class="card__icon">{icon('mail')}</div><h3>Where leads go</h3><p>Every form posts to FormSubmit, which emails the lead to <b>{esc(SITE['email'])}</b> with name, email, phone, timeline, interest, builder, message, page, consent and campaign tags. Reply-to is the lead&rsquo;s email.</p>
      <ul class="stack" style="padding-left:1.1em;margin-top:12px;font-size:15px"><li><a href="https://mail.google.com/mail/u/0/#search/from%3Aformsubmit.co" target="_blank" rel="noopener">Open the lead emails in Gmail</a></li><li>Bookings: <a href="https://calendly.com/app/scheduled_events/user/me" target="_blank" rel="noopener">Calendly scheduled events</a></li><li>If FormSubmit is ever unreachable, the form opens a pre-filled email to you instead, so nothing is lost.</li></ul>
      <p class="note" style="margin-top:12px">One-time step: click <b>Activate Form</b> in the FormSubmit email if you have not yet.</p></div>
    <div class="card"><div class="card__icon">{icon('layers')}</div><h3>Deploy and content</h3><p id="build-info">Build info loading&hellip;</p>
      <ul class="stack" style="padding-left:1.1em;margin-top:12px;font-size:15px"><li><a href="https://github.com/foundyourflorida/buyinginseaflower.com" target="_blank" rel="noopener">GitHub repository</a> (source and deploy history)</li><li><a href="https://github.com/foundyourflorida/buyinginseaflower.com/settings/pages" target="_blank" rel="noopener">GitHub Pages settings</a> (domain, HTTPS)</li><li>Source lives at <code>~/buyinginseaflower</code> on your Mac. Prices, fees, FAQ and posts are data files; run <code>python3 build.py</code> and push, or ask Claude.</li></ul></div>
  </div>

  <div class="grid grid-2 mt-4" style="align-items:start">
    <div class="card"><h3>Site health</h3><p>Checks every page in the sitemap from your browser and shows the status.</p>
      <div class="btn-row"><button class="btn btn--primary btn--sm" type="button" id="health-run">Check all pages</button><span id="health-summary" class="note"></span></div>
      <div class="table-wrap mt-2" id="health-wrap" hidden><table><thead><tr><th>Page</th><th>Status</th></tr></thead><tbody id="health-body"></tbody></table></div></div>
    <div class="card"><h3>Ad link builder</h3><p>Tag every ad, post and email with campaign parameters so Google Analytics shows which source produced each lead.</p>
      <div class="form">
        <div class="field"><label for="utm-page">Landing page</label><select id="utm-page"><option value="/">Home</option><option value="/buyers-guide/">Buyer&rsquo;s Guide (lead magnet)</option><option value="/book/">Book a call</option><option value="/builders/">Builders compared</option><option value="/homes/">Homes &amp; prices</option><option value="/costs/">Costs &amp; fees</option><option value="/faq/">FAQ</option><option value="/videos/">Videos</option></select></div>
        <div class="form__row"><div class="field"><label for="utm-source">Source</label><select id="utm-source"><option>facebook</option><option>instagram</option><option>google</option><option>youtube</option><option>newsletter</option><option>tiktok</option><option>nextdoor</option><option>zillow</option></select></div><div class="field"><label for="utm-medium">Medium</label><select id="utm-medium"><option>cpc</option><option>social</option><option>video</option><option>email</option><option>referral</option></select></div></div>
        <div class="field"><label for="utm-campaign">Campaign name</label><input id="utm-campaign" type="text" placeholder="e.g. seaflower-guide-sept"></div>
        <div class="field"><label for="utm-out">Your link</label><input id="utm-out" type="text" readonly></div>
        <div class="btn-row"><button class="btn btn--coral btn--sm" type="button" id="utm-copy">Copy link</button><span id="utm-copied" class="note"></span></div>
      </div></div>
  </div>

  <div class="card mt-4"><h3>Launch checklist for advertising</h3>
    <ul class="checklist">
      <li><b>Domain and HTTPS.</b> DNS points at GitHub Pages. HTTPS enforcement turns on once GitHub issues the certificate (automatic; usually within the hour).</li>
      <li><b>Search Console.</b> Add the domain property, submit <code>https://buyinginseaflower.com/sitemap.xml</code>, request indexing for the home page.</li>
      <li><b>Google Business Profile.</b> Add buyinginseaflower.com as a secondary website link; keep name and phone identical to foundyourflorida.com.</li>
      <li><b>Cross-link.</b> Link to this site from the SeaFlower page on foundyourflorida.com and from your YouTube video descriptions.</li>
      <li><b>Test a lead.</b> Submit the home-page guide form once with your own details and confirm the email arrives.</li>
      <li><b>Tag your ads.</b> Use the link builder above for every campaign; the landing page for cold traffic is the Buyer&rsquo;s Guide, for warm traffic the Book page.</li>
    </ul></div>
</div></section>
"""
    body = f"""
<section class="page-hero" style="padding-bottom:20px"><div class="container">
  {eyebrow("Private")}
  <h1 style="font-size:clamp(32px,4vw,44px)">Admin: traffic, leads and deploy</h1>
  <p class="lead" id="admin-status">Enter the admin password to continue.</p>
  <form id="admin-gate" class="form" style="max-width:420px" autocomplete="off">
    <div class="field"><label for="admin-pw">Password</label><input id="admin-pw" type="password" autocomplete="current-password" required></div>
    <button class="btn btn--primary" type="submit">Unlock</button>
    <div class="form__status" id="admin-err"></div>
  </form>
</div></section>
<template id="admin-dash">{dash}</template>
<script>
(function(){{
  var HASH='{PW_HASH}';
  var gate=document.getElementById('admin-gate'), err=document.getElementById('admin-err'), status=document.getElementById('admin-status');
  function sha(s){{ return crypto.subtle.digest('SHA-256', new TextEncoder().encode(s)).then(function(b){{ return Array.from(new Uint8Array(b)).map(function(x){{return x.toString(16).padStart(2,'0');}}).join(''); }}); }}
  function unlock(){{
    gate.hidden=true; err.className='form__status'; err.textContent=''; status.textContent='Signed in. This page is private and not indexed.';
    var t=document.getElementById('admin-dash'); document.querySelector('main').appendChild(t.content.cloneNode(true));
    try{{ sessionStorage.setItem('bis-admin','1'); }}catch(e){{}}
    init();
  }}
  gate.addEventListener('submit', function(e){{ e.preventDefault(); sha(document.getElementById('admin-pw').value).then(function(h){{ if(h===HASH){{ unlock(); }} else {{ err.className='form__status is-err'; err.textContent='That password is not right.'; }} }}); }});
  try{{ if(sessionStorage.getItem('bis-admin')==='1') unlock(); }}catch(e){{}}
  function init(){{
    fetch('/build-info.json',{{cache:'no-store'}}).then(function(r){{return r.json();}}).then(function(b){{ document.getElementById('build-info').innerHTML='Last build <b>'+b.built_at+'</b> · commit <code>'+b.commit+'</code> · '+b.pages+' pages · data verified '+b.updated; }}).catch(function(){{ document.getElementById('build-info').textContent='Build info unavailable.'; }});
    var run=document.getElementById('health-run');
    run.addEventListener('click', function(){{
      run.disabled=true; var body=document.getElementById('health-body'); body.innerHTML=''; document.getElementById('health-wrap').hidden=false;
      fetch('/sitemap.xml',{{cache:'no-store'}}).then(function(r){{return r.text();}}).then(function(x){{
        var urls=Array.from(x.matchAll(/<loc>([^<]+)<\/loc>/g)).map(function(m){{return m[1];}}); var ok=0, done=0;
        urls.forEach(function(u){{ var path=u.replace(/^https?:\/\/[^/]+/,''); fetch(path,{{method:'GET',cache:'no-store'}}).then(function(r){{ return r.status; }}).catch(function(){{ return 'error'; }}).then(function(s){{ done++; if(s===200) ok++; var tr=document.createElement('tr'); tr.innerHTML='<td><a href="'+path+'" target="_blank">'+path+'</a></td><td>'+(s===200?'<span class="chip chip--green">200 OK</span>':'<span class="chip chip--coral">'+s+'</span>')+'</td>'; body.appendChild(tr); document.getElementById('health-summary').textContent=ok+' of '+done+' pages OK'+(done<urls.length?' (checking…)':''); if(done===urls.length) run.disabled=false; }}); }});
      }});
    }});
    function utm(){{ var page=document.getElementById('utm-page').value, s=document.getElementById('utm-source').value, m=document.getElementById('utm-medium').value, c=(document.getElementById('utm-campaign').value||'seaflower').trim().toLowerCase().replace(/[^a-z0-9-]+/g,'-'); document.getElementById('utm-out').value='https://buyinginseaflower.com'+page+'?utm_source='+s+'&utm_medium='+m+'&utm_campaign='+c; }}
    ['utm-page','utm-source','utm-medium','utm-campaign'].forEach(function(id){{ document.getElementById(id).addEventListener('input', utm); document.getElementById(id).addEventListener('change', utm); }}); utm();
    document.getElementById('utm-copy').addEventListener('click', function(){{ var o=document.getElementById('utm-out'); o.select(); navigator.clipboard.writeText(o.value).then(function(){{ document.getElementById('utm-copied').textContent='Copied.'; }}); }});
  }}
}})();
</script>
"""
    return [dict(path="/admin/", title="Admin", description="Private admin page.", body=body, noindex=True, nav="/", extra_head='<meta name="robots" content="noindex, nofollow, noarchive">')]

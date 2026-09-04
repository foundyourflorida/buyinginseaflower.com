"""Ad landing page: /guide/ — interactive 60-second SeaFlower match quiz that unlocks a personalized report and the Buyer's Guide."""
import json
from ..config import SITE, LEGAL
from ..components import *  # noqa
from ..content import facts as F
from ..content.builders_index import BUILDERS
from ..content.testimonials import TESTIMONIALS
from ..html import esc

BUILDER_DATA = {b["slug"]: {"name": b["name"], "short": b["short"], "tier": b.get("tier", ""), "price": b["price_phrase"].split("(")[0].split(";")[0].strip()[:60],
                            "sqft": b["sqft_range"].split(" A/C")[0], "lots": ", ".join(b.get("lot_widths") or []) or "attached", "plans": sum(len(c["plans"]) for c in b["collections"]),
                            "qmi": len(b["quick_move_ins"]), "url": f"/builders/{b['slug']}/"} for b in BUILDERS}

QUIZ = [
    {"key": "type", "q": "What kind of home are you picturing?", "hint": "There is a right answer for every lifestyle here; this narrows the builders.",
     "opts": [("attached", "Lock-and-leave townhome or villa", "No yard to keep; exterior in the HOA"), ("bungalow", "Bungalow with a porch and alley garage", "45' lots, the classic SeaFlower street"), ("cottage", "Cottage or Classic home with a yard", "50' and 60' lots, front or rear garage"), ("estate", "Lakefront estate home", "80' lots on Lake Flores"), ("unsure", "Not sure yet", "Show me what fits my budget")]},
    {"key": "budget", "q": "What total budget are you working with?", "hint": "Base price plus lot and options; I will show you the monthly number too.",
     "opts": [("b1", "Under $450,000", ""), ("b2", "$450,000 to $600,000", ""), ("b3", "$600,000 to $800,000", ""), ("b4", "$800,000 and up", "")]},
    {"key": "timeline", "q": "When would you like to be in the home?", "hint": "This decides whether a quick move-in or a build makes sense.",
     "opts": [("t1", "Within 3 months", "Quick move-in territory"), ("t2", "3 to 6 months", ""), ("t3", "6 to 12 months", ""), ("t4", "More than a year, still researching", "")]},
    {"key": "origin", "q": "Where are you coming from?", "hint": "Out-of-state buyers get a different playbook (remote tours, closings, homestead timing).",
     "opts": [("local", "Bradenton or Sarasota area", ""), ("florida", "Elsewhere in Florida", ""), ("oos", "Another state", ""), ("intl", "Canada or another country", "")]},
    {"key": "priority", "q": "What matters most to you?", "hint": "Pick one; it shapes the insider notes in your report.",
     "opts": [("beach", "Being close to the beach", ""), ("cost", "The lowest monthly cost", ""), ("yard", "A yard, a pool, space between homes", ""), ("adu", "A guest suite or ADU", ""), ("movein", "Moving in as soon as possible", "")]},
]


def pages():
    quiz_steps = ""
    for i, st in enumerate(QUIZ):
        opts = "".join(f'<button type="button" class="quiz__opt" data-key="{st["key"]}" data-val="{v}"><span><b>{esc(l)}</b>{("<small>" + esc(h) + "</small>") if h else ""}</span></button>' for v, l, h in st["opts"])
        quiz_steps += f'<div class="quiz__step{" is-active" if i == 0 else ""}" data-step="{i}"><p class="quiz__q">{esc(st["q"])}</p><p class="quiz__hint">{esc(st["hint"])}</p><div class="quiz__opts">{opts}</div><div class="quiz__nav"><button type="button" class="quiz__back"{" hidden" if i == 0 else ""}>&larr; Back</button><span>Question {i + 1} of {len(QUIZ)}</span></div></div>'
    consent_full = esc(LEGAL["consent"])
    step1_form = f"""
<form class="form" id="guide-quiz" data-lead-form data-form-name="seaflower_match_quiz" action="{esc(SITE['form_endpoint'])}" method="post" data-redirect="#report" data-success="Unlocked. Your full report is below, and the guide is on its way to your inbox." novalidate>
  <input type="hidden" name="source" value="buyinginseaflower.com/guide"><input type="hidden" name="interest" value="SeaFlower match quiz + Buyer's Guide"><input type="hidden" name="form" value="guide-quiz"><input type="hidden" name="message" id="quiz-answers" value=""><input type="hidden" name="page" value=""><input class="hp" type="text" name="_gotcha" tabindex="-1" autocomplete="off" aria-hidden="true">
  <div class="form__row"><div class="field"><label for="gq-name">First name</label><input id="gq-name" name="name" type="text" autocomplete="given-name" required placeholder="First name"></div><div class="field"><label for="gq-email">Email</label><input id="gq-email" name="email" type="email" autocomplete="email" required placeholder="you@example.com"></div></div>
  <button class="btn btn--coral btn--lg btn--block" type="submit">Unlock my report + send the guide</button>
  <div class="form__status" aria-live="polite"></div>
  <p class="note" style="margin:8px 0 0;font-size:12.5px">No spam. You will hear from Trenton personally, not a call center. {SITE['agent']}, {SITE['brokerage']}.</p>
</form>"""
    step2_form = f"""
<form class="form step2" id="guide-quiz-phone" data-lead-form data-no-conversion action="{esc(SITE['form_endpoint'])}" method="post" data-success="Thanks. I will text you the current incentives for your match." novalidate>
  <input type="hidden" name="source" value="buyinginseaflower.com/guide"><input type="hidden" name="interest" value="SeaFlower match quiz: phone follow-up"><input type="hidden" name="form" value="guide-quiz-phone"><input type="hidden" name="message" class="quiz-answers-copy" value=""><input type="hidden" name="page" value=""><input type="hidden" name="name" class="copy-name" value=""><input type="hidden" name="email" class="copy-email" value=""><input class="hp" type="text" name="_gotcha" tabindex="-1" autocomplete="off" aria-hidden="true">
  <p style="margin:0 0 10px;font-weight:600;color:var(--green-900)">Optional: want the current incentives for your match by text?</p>
  <div class="form__row"><div class="field"><label for="gq-phone">Mobile number</label><input id="gq-phone" name="phone" type="tel" autocomplete="tel" placeholder="(555) 555-5555" required></div><div class="field"><label for="gq-timeline">Timeline</label><select id="gq-timeline" name="timeline"><option value="">Timeline</option><option>Within 3 months</option><option>3 to 6 months</option><option>6 to 12 months</option><option>12+ months</option></select></div></div>
  <label class="field field--check consent-short"><input type="checkbox" name="consent" value="yes" required><span>Yes, text and call me about SeaFlower homes; consent is not a condition of purchase and I can reply STOP any time.<details><summary>Full terms</summary><span class="full">{consent_full}</span></details></span></label>
  <button class="btn btn--primary btn--block" type="submit">Text me the incentives</button>
  <div class="form__status" aria-live="polite"></div>
</form>"""
    body = f"""
<section class="landing-hero"><div class="container">
  <div class="landing-copy">
    {eyebrow("Free 60-second match · Bradenton, FL")}
    <h1>Which SeaFlower home actually fits you?</h1>
    <p class="lead">Answer five quick questions and get a personalized match: the builders and lot types that fit your budget, the real monthly number with HOA, CDD and taxes, and insider notes from someone who used to run this community. The full Buyer&rsquo;s Guide comes with it, free.</p>
    <div class="trust-row"><span>{icon('check')} Every builder, priced as published</span><span>{icon('check')} HOA + CDD + taxes, by lot</span><span>{icon('check')} From a former David Weekley operations manager</span></div>
    <div class="guide-preview mt-4"><img src="/assets/images/guide-cover.jpg" alt="The SeaFlower Buyer's Guide cover" width="260" height="338" loading="lazy"><div><p class="eyebrow" style="margin-bottom:8px">Included with your match</p><h3 style="font-size:24px;margin-bottom:8px">The SeaFlower Buyer&rsquo;s Guide, 2026 edition</h3><ul class="checklist" style="font-size:15px"><li>All five builders, 62 plans, prices and lot sizes</li><li>The Lake Flores CDD table by phase and lot</li><li>Incentive and contract negotiation checklist</li><li>Out-of-state buying timeline</li></ul></div></div>
  </div>
  <div class="quiz" id="quiz">
    <div class="quiz__progress"><i id="quiz-bar"></i></div>
    {quiz_steps}
    <div class="result" id="result">
      <div class="result__match"><p class="eyebrow">Your SeaFlower match</p><h3 id="match-title">&nbsp;</h3><p id="match-sub">&nbsp;</p></div>
      <div class="result__lock" id="result-lock"><ul class="result__list result__blur" id="result-preview"></ul><div class="result__lockmsg"><span>Enter your name and email to unlock the full report and get the guide</span></div></div>
      {step1_form}
      <div class="result__full" id="report"><h3 style="font-size:22px;margin:18px 0 10px">Your full report</h3><ul class="result__list" id="result-full"></ul><div class="btn-row mt-3"><a class="btn btn--primary" href="/buyers-guide/print/" target="_blank" rel="noopener">Open the guide now</a>{btn("Book a free strategy call", SITE['booking_page'], "ghost", icon_name="calendar", cta="guide-book")}</div>{step2_form}</div>
    </div>
  </div>
</div></section>

<section class="section bg-shell reveal"><div class="container">
  {section_head("What buyers say", eyebrow_text="Reviews", center=True)}
  <div class="testimonials">{"".join(testimonial(q, w, l) for q, w, l in TESTIMONIALS[:3])}</div>
</div></section>

<section class="section reveal"><div class="container"><div class="split">
  <div><div class="card" style="padding:14px;background:linear-gradient(160deg,#fff,var(--sand))"><img src="/assets/images/trenton-miller-800.jpg" alt="Trenton Miller" width="800" height="800" style="border-radius:12px" loading="lazy"></div></div>
  <div>{eyebrow("Who is behind this")}<h2 style="font-size:clamp(28px,3.4vw,40px)">I sold homes for the builder. Now I make sure the builder treats you right.</h2><p class="lead">Six years as a top producer with Pulte and Del Webb, a year in operations with David Weekley Homes, and a stretch overseeing SeaFlower itself. The builder still pays the commission; the difference is who I work for.</p><p class="note">{SITE['agent_credentials']}, licensed Florida sales associate, {SITE['brokerage']}.</p></div>
</div></div></section>
"""
    quiz_js = """
<script>
(function(){
  var B = %s;
  var steps = [].slice.call(document.querySelectorAll('.quiz__step')), bar = document.getElementById('quiz-bar'), result = document.getElementById('result');
  var answers = {}, idx = 0, labels = {};
  function show(i){ steps.forEach(function(s, j){ s.classList.toggle('is-active', j === i); }); bar.style.width = Math.round((i / steps.length) * 100) + '%%'; idx = i; }
  document.querySelectorAll('.quiz__opt').forEach(function(btn){
    btn.addEventListener('click', function(){
      var k = btn.getAttribute('data-key'), v = btn.getAttribute('data-val');
      answers[k] = v; labels[k] = btn.querySelector('b').textContent;
      btn.parentNode.querySelectorAll('.quiz__opt').forEach(function(o){ o.classList.toggle('is-selected', o === btn); });
      setTimeout(function(){ if (idx < steps.length - 1) show(idx + 1); else finish(); }, 180);
    });
  });
  document.querySelectorAll('.quiz__back').forEach(function(b){ b.addEventListener('click', function(){ if (idx > 0) show(idx - 1); }); });
  var TYPE = { attached: ['mi-homes'], bungalow: ['david-weekley-homes','pulte-homes'], cottage: ['cardel-homes','david-weekley-homes','pulte-homes'], estate: ['issa-homes'], unsure: [] };
  var BUDGET = { b1: ['mi-homes','pulte-homes'], b2: ['david-weekley-homes','pulte-homes','cardel-homes','mi-homes'], b3: ['david-weekley-homes','cardel-homes','pulte-homes'], b4: ['cardel-homes','issa-homes','david-weekley-homes'] };
  var MID = { b1: 420000, b2: 525000, b3: 700000, b4: 950000 };
  var CDD = { b1: 1750, b2: 2100, b3: 2660, b4: 3400 };
  function money(x){ return '$' + Math.round(x).toLocaleString(); }
  function pi(price){ var L = price * 0.8, r = 0.065/12, n = 360; return L * r / (1 - Math.pow(1 + r, -n)); }
  function finish(){
    var t = TYPE[answers.type] || [], b = BUDGET[answers.budget] || [];
    var m = t.length ? t.filter(function(x){ return b.indexOf(x) !== -1; }) : b.slice();
    if (!m.length) m = t.length ? t : b;
    m = m.slice(0, 3);
    var price = MID[answers.budget] || 525000, hoa = (m[0] === 'mi-homes') ? 308.43 : 300.88, cdd = CDD[answers.budget] || 2100, ins = price < 500000 ? 2600 : (price < 750000 ? 3400 : 4200);
    var tax = Math.max(price - 50000, 0) * 14.61 / 1000 / 12, monthly = pi(price) + tax + hoa + cdd/12 + ins/12;
    var names = m.map(function(s){ return B[s].short; });
    document.getElementById('match-title').textContent = names.join(' + ');
    document.getElementById('match-sub').textContent = m.map(function(s){ return B[s].short + ': ' + B[s].price; }).join(' · ');
    var full = [];
    m.forEach(function(s){ full.push('<b>' + B[s].name + '</b>: ' + B[s].plans + ' plans, ' + B[s].sqft + ' sq ft, ' + B[s].lots + ' lots, ' + B[s].qmi + ' quick move-ins listed. <a href="' + B[s].url + '">Profile</a>'); });
    full.push('<b>Estimated monthly at ' + money(price) + '</b>: about ' + money(monthly) + ' with 20%% down at 6.5%%, taxes at full value, HOA ' + money(hoa) + ', CDD about ' + money(cdd) + '/yr and insurance estimated.');
    var notes = { beach: 'Beach note: 3.2 miles to the sand, 8 minutes to Bradenton Beach off-peak; in season go before 10 a.m. or after 1:30 p.m.', cost: 'Cost note: Phase 1B lots carry a lower CDD than Phase 1C for the same width; ask which phase before you compare two lots.', yard: 'Yard note: 50\\' and 60\\' front-garage lots (Cardel, Pulte) give the deepest back yards and the easiest pool; rear-load lots trade yard for porch.', adu: 'ADU note: Cardel garage suites, Pulte\\'s Mabel II and Issa\\'s garage-apartment plans are the built-in options; one year owner occupancy before renting.', movein: 'Move-in note: 35 quick move-in homes were listed on ' + '%s' + '; the biggest discounts and rate buydowns are on inventory past its ready date.' };
    full.push(notes[answers.priority] || notes.cost);
    if (answers.timeline === 't1' || answers.timeline === 't2') full.push('Timing note: your window points to a quick move-in; the last two weeks of a fiscal quarter (September, December) are when builders clear inventory.');
    else full.push('Timing note: a to-be-built home takes 7 to 14 months depending on builder; lot releases and structural options are decided before the slab.');
    if (answers.origin === 'oos' || answers.origin === 'intl') full.push('Relocation note: Florida allows remote online notarization, so you can close from home; occupy by January 1 and file homestead by March 1 to get the exemption.');
    document.getElementById('result-full').innerHTML = full.map(function(x){ return '<li>' + x + '</li>'; }).join('');
    document.getElementById('result-preview').innerHTML = full.slice(0, 3).map(function(x){ return '<li>' + x.replace(/<[^>]+>/g, '') + '</li>'; }).join('');
    var summary = Object.keys(answers).map(function(k){ return k + ': ' + labels[k]; }).join(' | ') + ' | match: ' + names.join(', ') + ' | est. monthly: ' + money(monthly);
    document.getElementById('quiz-answers').value = summary;
    document.querySelectorAll('.quiz-answers-copy').forEach(function(e){ e.value = summary; });
    steps.forEach(function(s){ s.classList.remove('is-active'); }); bar.style.width = '100%%'; result.classList.add('is-active');
  }
  document.addEventListener('bis:lead-sent', function(e){
    if (e.detail.form === 'guide-quiz') {
      document.getElementById('result-lock').style.display = 'none';
      document.getElementById('guide-quiz').style.display = 'none';
      document.getElementById('report').classList.add('is-active');
      document.getElementById('report').scrollIntoView({ block: 'start' });
    }
  });
  var f1 = document.getElementById('guide-quiz');
  f1.addEventListener('submit', function(){ var n = document.getElementById('gq-name').value, em = document.getElementById('gq-email').value; document.querySelectorAll('.copy-name').forEach(function(x){ x.value = n; }); document.querySelectorAll('.copy-email').forEach(function(x){ x.value = em; }); }, true);
})();
</script>
""" % (json.dumps(BUILDER_DATA), F.AS_OF)
    return [dict(path="/guide/", title="Which SeaFlower Home Fits You? Free 60-Second Match + Buyer's Guide",
                 description="Answer five quick questions and get a personalized SeaFlower match: the builders and lot types for your budget, the real monthly number with HOA, CDD and taxes, insider notes, and the free Buyer's Guide.",
                 body=body, extra_body=quiz_js, body_class="is-landing", nav="/guide/", noindex=False, priority="0.9", changefreq="weekly",
                 og_image="/assets/images/guide-cover.jpg",
                 schema=[{"@type": "WebPage", "@id": SITE["domain"] + "/guide/#page", "url": SITE["domain"] + "/guide/", "name": "SeaFlower home match quiz", "about": {"@id": SITE["domain"] + "/#seaflower"}}])]

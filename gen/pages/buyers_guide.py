from ..config import SITE
from ..components import *  # noqa
from ..content.testimonials import TESTIMONIALS


def pages():
    inside = [
        ("layers", "Builder-by-builder comparison", "Every SeaFlower builder side by side: collections, lot widths, square footage, starting prices and who each one is really for."),
        ("dollar", "The real monthly number", "HOA, CDD, property tax and insurance worked through on a real SeaFlower price so you can budget honestly."),
        ("map-pin", "Lot and phase notes", "Which sections are selling now, what is coming, and what to ask about the land behind a lot before you pay a premium."),
        ("percent", "Incentive negotiation checklist", "What builders can move on, in what order to ask, and the questions that tell you whether an incentive is real."),
        ("shield", "Build-quality checklist", "The pre-drywall and final-walk items I checked as a David Weekley operations manager."),
        ("plane", "Out-of-state timeline", "A week-by-week plan for buying from Buffalo, Boston, Jersey, Chicago or Canada without three flights."),
    ]
    cards = "".join(f'<div class="card"><div class="card__icon">{icon(i)}</div><h3 style="font-size:21px">{t}</h3><p>{b}</p></div>' for i, t, b in inside)
    body = f"""
<section class="page-hero"><div class="container">
  {breadcrumb([("Home", "/"), ("SeaFlower Buyer's Guide", None)])}
  <div class="split">
    <div>
      {eyebrow("Free download")}
      <h1>The SeaFlower <em style="font-style:italic;color:var(--coral-700)">Buyer&rsquo;s Guide</em></h1>
      <p class="lead">Every builder, every fee and every question buyers ask me, in one document you can read on the plane. Written by the guy who used to oversee the community for David Weekley, not by a marketing department.</p>
      <ul class="checklist" style="margin:18px 0 0;font-size:16px">
        <li>Builder comparison with prices and lot sizes</li>
        <li>HOA, CDD, tax and insurance worksheet</li>
        <li>Incentive and contract negotiation checklist</li>
        <li>Updated as builders release phases and pricing</li>
      </ul>
    </div>
    <div id="get-guide">{lead_form("guide", "Send me the guide", "Enter your details and I&rsquo;ll email the current edition personally, usually within a few hours.", submit="Email me the guide", interest="SeaFlower Buyer's Guide", compact=True, redirect="/thank-you/", success="On its way. Check your inbox (and the promotions tab) for the guide.")}</div>
  </div>
</div></section>

<section class="section bg-shell reveal"><div class="container">
  {section_head("What&rsquo;s inside", eyebrow_text="Six sections, no fluff")}
  <div class="grid grid-3">{cards}</div>
</div></section>

<section class="section reveal"><div class="container container--narrow">
  {section_head("Why it&rsquo;s free", eyebrow_text="Straight talk")}
  <p class="lead">Because informed buyers make better clients, and some of you will want me on your side when you tour. If you don&rsquo;t, you still get the guide. No drip campaign, no daily emails. One follow-up to see if it helped, and that&rsquo;s it.</p>
  <div class="testimonials mt-4">{"".join(testimonial(q, w, l) for q, w, l in TESTIMONIALS[:2])}</div>
</div></section>
"""
    return [dict(
        path="/buyers-guide/", title="Free SeaFlower Buyer's Guide (PDF): Builders, Fees, Lots and Negotiation",
        description="Download the free SeaFlower Buyer's Guide: a builder-by-builder comparison, the real monthly cost with HOA, CDD, taxes and insurance, lot and phase notes, and an incentive negotiation checklist from a former builder insider.",
        body=body, priority="0.8", changefreq="monthly", schema=[breadcrumb_schema([("Home", "/"), ("SeaFlower Buyer's Guide", "/buyers-guide/")])],
    )]

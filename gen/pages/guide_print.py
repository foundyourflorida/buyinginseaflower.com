"""Print edition of the SeaFlower Buyer's Guide: /buyers-guide/print/ (noindex). Open in a browser, Cmd/Ctrl+P, Save as PDF."""
from ..config import SITE, LEGAL
from ..components import *  # noqa
from ..content import facts as F
from ..content.builders_index import BUILDERS, TIER_LABEL, all_plans
from ..content.faqs import FAQS
from ..html import esc, md
from .costs import EXAMPLES, payment, money, RATE, DOWN

CHECKLIST = """
## Before your first visit
- Call or text Trenton so you are registered with every builder before you walk into a model.
- Decide the product first: townhome or villa, 42' or 45' rear-load bungalow, 50' cottage, 60' classic, or 80' estate.
- Know your all-in monthly budget with HOA, CDD, taxes at full value and insurance, not just principal and interest.

## Questions to ask at every model
- Which phase is this lot in, and what is the CDD assessment for it this year?
- What is the lot premium, and which lots nearby carry none?
- What is the base elevation, and what do the others cost?
- Which structural options must be chosen before the slab?
- What are the deposit amounts, when are they due, and what happens to them if my financing fails?
- What incentive is tied to your lender, and what is available if I use my own?
- What is the completion window, and what happens if you miss it?

## Negotiate in this order
1. Lot premium. 2. Closing-cost credit. 3. Rate buydown depth. 4. Design-center and structural credits. 5. CDD debt paydown. 6. Base price, last.

## Inspections and walkthroughs
- Pre-construction meeting: confirm plan, elevation, options and lot orientation in writing.
- Pre-drywall: independent inspector for framing, strapping, flashing, plumbing, electrical and duct sealing.
- Final walkthrough: blue-tape every defect; nothing gets fixed faster than before closing.
- Eleven-month warranty walk: a second inspection before the one-year workmanship warranty expires.

## Out-of-state timeline
- 12+ months out: strategy call, budget, product decision, watch the quick move-in list.
- 6 to 12 months: one visit to tour all five builders in a day; shortlist two; get lender quotes both ways.
- 3 to 6 months: contract on a quick move-in, or lot and plan selection on a build; design appointment.
- 1 to 3 months: video walkthroughs at each stage; insurance quotes; homestead paperwork prepared.
- Closing: remote online notarization or mail-away; occupy by January 1 and file homestead by March 1.
"""


def pages():
    b_rows = [(b["name"], TIER_LABEL.get(b.get("tier", ""), ""), ", ".join(b["home_types"])[:60], ", ".join(b["lot_widths"]) if b.get("lot_widths") else "attached", b["sqft_range"], b["price_phrase"][:60], b["sales_office"].get("phone", "")) for b in BUILDERS]
    plan_rows = [(b["short"], p["name"], c.get("lot_width", ""), p.get("sqft", ""), p.get("beds", ""), p.get("baths", ""), p.get("price", "")) for b, c, p in all_plans()]
    ex_rows = []
    for label, price, hoa, cdd, ins in EXAMPLES:
        pi = payment(price); tax = max(price - 50000, 0) * F.TAXES["millage"] / 1000 / 12
        ex_rows.append((label, money(price), money(pi), money(tax), money(hoa), money(cdd / 12), money(ins / 12), money(pi + tax + hoa + cdd / 12 + ins / 12)))
    top_faq = [(q, a) for cat in ("costs", "process", "safety") for q, a, t in FAQS[cat][:5]]
    faq_html = "".join(f"<h4>{esc(q)}</h4>{md(a, heading_ids=False)}" for q, a in top_faq)
    body = f"""
<div class="print-doc">
<section class="print-cover">
  <div class="print-cover__brand">{flower_mark(56, cls="")}<div><div class="brand__name" style="font-size:30px">Buying in <em>SeaFlower</em></div><div class="brand__sub">A Found Your Florida guide</div></div></div>
  <h1>The SeaFlower Buyer&rsquo;s Guide</h1>
  <p class="lead">Every builder, every fee, every question. Bradenton, Florida. Edition of {esc(F.AS_OF)}.</p>
  <p>By {SITE['agent_credentials']}, buyer&rsquo;s agent with {SITE['brokerage']}. Seven years on the builder side, including operations at David Weekley Homes, where he briefly oversaw SeaFlower.<br>{SITE['phone_display']} · {SITE['email']} · buyinginseaflower.com</p>
  <p class="disclosure">{LEGAL['not_affiliated']} Full disclosures at buyinginseaflower.com/terms/.</p>
</section>

<section class="print-section">
  <h2>1. The community at a glance</h2>
  {table(["Item", "Fact"], [("Location", F.COMMUNITY["location"]), ("Size", F.COMMUNITY["acres"] + " acres; " + F.COMMUNITY["buildout"]["homes"] + " homes at buildout"), ("Phase One", F.COMMUNITY["phase_one"]["homes"] + " homes on " + F.COMMUNITY["phase_one"]["acres"] + " acres; 784 released as of Apr 2026"), ("Developer", F.COMMUNITY["developer"]), ("Beach", F.COMMUNITY["beach"]), ("Amenities", "The Garden Club (opening fall 2026), " + F.COMMUNITY["trail"] + ", " + F.COMMUNITY["lake"] + ", two dog parks, pocket parks"), ("Village Center", F.VILLAGE_CENTER["anchor"] + "; " + F.VILLAGE_CENTER["timeline"]), ("Gated / age-restricted", "No / No"), ("Golf carts", F.COMMUNITY["golf_carts"]), ("ADUs", F.COMMUNITY["adu"]), ("Welcome Center", F.COMMUNITY["welcome_center"]["address"] + ", " + F.COMMUNITY["welcome_center"]["phone"])])}
</section>

<section class="print-section">
  <h2>2. The five builders</h2>
  {table(["Builder", "Tier", "Product", "Lots", "Sq ft", "Starting price (as phrased)", "Phone"], b_rows)}
  <h3>Every floor plan and base price</h3>
  {table(["Builder", "Plan", "Lot", "Sq ft", "Beds", "Baths", "Base price"], plan_rows, numeric_cols=(3, 6), note="As published by the builders on " + F.AS_OF + "; excludes lot premiums and options.")}
</section>

<section class="print-section">
  <h2>3. What it costs per month</h2>
  {table(["Home type", "Monthly HOA"], F.HOA["fees"], note=F.HOA["includes"] + " " + F.HOA["abated"])}
  <h3>Lake Flores CDD, FY2027 proposed, per year</h3>
  {table(["Phase", "Lot", "Per year"], F.CDD["fy2027"], numeric_cols=(2,))}
  <h3>Worked examples</h3>
  {table(["Home", "Price", "P&I", "Taxes", "HOA", "CDD", "Insurance", "Total / mo"], ex_rows, numeric_cols=(1, 2, 3, 4, 5, 6, 7), note=f"{int(DOWN*100)}% down, 30-year fixed at {RATE*100:.1f}%, taxes at {F.TAXES['millage']} mills less a $50,000 homestead exemption, insurance estimated.")}
  <p>{esc(F.TAXES['new_construction'])} {esc(F.TAXES['homestead'])}</p>
</section>

<section class="print-section">
  <h2>4. Location, schools, flood and evacuation</h2>
  {dist_list(F.DRIVE_TIMES)}
  <p class="note">{esc(F.DRIVE_TIMES_SOURCE)}</p>
  {table(["School", "Address", "Listed by"], F.SCHOOLS, note=F.SCHOOLS_NOTE)}
  <p>{esc(F.INSURANCE['flood'])} {esc(F.INSURANCE['note'])}</p>
</section>

<section class="print-section">
  <h2>5. The checklist</h2>
  <div class="prose">{md(CHECKLIST)}</div>
</section>

<section class="print-section">
  <h2>6. Fifteen questions, answered</h2>
  {faq_html}
</section>

<section class="print-section">
  <h2>Talk to Trenton</h2>
  <p>Free strategy call: {SITE['booking_url']}<br>Call or text {SITE['phone_display']} · {SITE['email']}<br>{SITE['agent_credentials']}, Licensed Florida real estate sales associate, {SITE['brokerage']}</p>
  <p class="disclosure">{LEGAL['accuracy']}</p>
  <p class="disclosure">{LEGAL['brokerage_line']} {LEGAL['fair_housing']}</p>
</section>
</div>
"""
    return [dict(path="/buyers-guide/print/", title="SeaFlower Buyer's Guide, print edition", description="Printable edition of the SeaFlower Buyer's Guide.",
                 body=body, noindex=True, nav="/buyers-guide/", body_class="is-print-doc", extra_head='<style>.is-print-doc .header,.is-print-doc .footer,.is-print-doc .mobile-bar,.is-print-doc .drawer{display:none!important}.print-doc{max-width:900px;margin:0 auto;padding:40px var(--gutter) 80px}.print-cover{padding:40px 0 30px;border-bottom:2px solid var(--coral);margin-bottom:30px}.print-cover__brand{display:flex;align-items:center;gap:14px;margin-bottom:26px}.print-cover h1{font-size:54px}.print-section{margin:34px 0;page-break-inside:avoid}.print-section h2{font-size:30px;border-bottom:1px solid var(--line);padding-bottom:6px}.print-section h3{font-size:22px;margin-top:1.4em}.print-section h4{font-size:17px;margin:1.2em 0 .2em}.print-section table{font-size:12.5px}.print-section th,.print-section td{padding:7px 9px}@media print{body{background:#fff;font-size:12px}.print-doc{padding:0;max-width:none}.print-section{break-inside:avoid}.table-wrap{border:0;box-shadow:none}a{text-decoration:none;color:inherit}.print-cover h1{font-size:44px}}</style>')]

from ..config import SITE
from ..components import *  # noqa
from ..content import facts as F
from ..content.videos import by_id
from ..html import esc, md

RATE = 0.065      # assumed 30-year fixed rate for the worked examples
DOWN = 0.20       # assumed down payment


def payment(price):
    loan = price * (1 - DOWN)
    r = RATE / 12
    n = 360
    return loan * r / (1 - (1 + r) ** -n)


def money(x):
    return "${:,.0f}".format(x)


EXAMPLES = [
    ("M/I Homes townhome (Row Home), Phase N1", 410000, 308.43, 1473.49, 2200),
    ("Pulte Scenic-series home on a 42' lot, Phase 1C", 430000, 300.88, 3334.52, 3000),
    ("David Weekley Bungalow on a 45' lot, Phase 1B2", 486000, 300.88, 2091.63, 3200),
    ("David Weekley Classic on a 60' lot, Phase 1B2", 655000, 300.88, 2656.01, 3800),
    ("Cardel Classic on a 60' lot, Phase 1C", 700000, 300.88, 4604.78, 4000),
]

INTRO = (
    "<strong>A SeaFlower home carries four recurring costs on top of the mortgage:</strong> an HOA fee of $300.88 a month for a single-family home "
    "($308.43 townhome, $327.70 villa) that includes 1-Gig fiber and full yard maintenance; a Lake Flores CDD assessment of roughly $1,475 to $4,605 a year "
    "depending on your phase and lot width, billed on the tax bill; Manatee County property taxes at about 14.61 mills; and homeowner's insurance. "
    "On a $486,000 bungalow with 20% down at 6.5%, that works out to roughly " + "{TOTAL_EXAMPLE}" + " a month all-in. Figures verified " + F.AS_OF + "."
)

HOA_MD = """
## HOA: what $300.88 a month buys

The SeaFlower Homeowners Association is managed by ICON Management. The monthly assessment covers 1-Gig fiber internet to every home, front and rear yard landscape maintenance, the parks and trails, and operation of The Garden Club once it opens. Townhome and villa owners pay a little more because their fee also funds exterior maintenance, insurance and reserves on the shared structures.

| Home type | Monthly HOA | What is different |
|---|---|---|
| Single-family home | $300.88 | Yard maintenance front and back, 1-Gig fiber, common areas, Garden Club |
| Townhome (Row Home) | $308.43 | Adds exterior maintenance, insurance and reserves |
| Twin villa (Village Home) | $327.70 | Adds exterior maintenance, insurance and reserves |

Two things to know. First, the clubhouse portion of the assessment is currently abated; it gets added when The Garden Club is substantially complete, which is scheduled for fall 2026, so the fee will step up. Second, the developer's information sheet calls the budget "conceptual" and the figures "good faith estimates." Ask for the current adopted HOA budget, the CC&Rs and any capital contribution or transfer fee before contract; the capital contribution is not published.

:::trent
Compare apples to apples. Some communities quote a $150 HOA and then charge you $100 a month for internet and $150 for lawn care. SeaFlower bundles both. When buyers compare it to Lakewood Ranch villages, I make them add the lawn and fiber back in before they decide which is cheaper.
:::
"""

CDD_MD = """
## CDD: the line item out-of-state buyers miss

A Community Development District is a special-purpose government that sells tax-exempt bonds to build a community's infrastructure and pays them back through an annual assessment on each lot. At SeaFlower the district is the **Lake Flores Community Development District**, created by Manatee County in January 2022 and managed by Wrathell, Hunt and Associates. It paid for stormwater management, the wetlands and conservation areas, the multi-modal trail, the alleys and the streetlights.

Your assessment has two parts: debt service on the bonds for your phase, and an operations-and-maintenance charge (about $400 a year). It shows up as a non-ad valorem line on your Manatee County tax bill every November, with up to a 4% discount for paying early. Because the debt is fixed to the lot, it does not go up with your home's value, and it can be prepaid in a lump sum.

The number depends on which phase your lot is in and how wide it is. Phase 1C lots carry the Series 2026 bonds, which is why they are noticeably higher than Phase 1B lots of the same width.
"""

TAX_MD = """
## Property taxes

The tax district covering SeaFlower (Cedar Hammock Fire Control District, unincorporated Manatee County) adopted a total rate of 14.6100 mills for 2025; David Weekley's pages show 14.671, which is the 2024 rate. That is about **$1,461 per $100,000 of taxable value**. A Florida homestead exemption removes up to $50,000 of assessed value on your primary residence and caps future assessment increases at 3% a year.

Two new-construction quirks. If your home was not finished on January 1, your first bill is usually based on the land only, and the following year jumps to the full value; your lender's escrow estimate should already assume the full value, so check it. And you must own and occupy by January 1, then file for homestead by March 1, to get the exemption that year. Buyers closing in December and buyers closing in January live in very different tax years.

:::trent
The single most common budgeting mistake I see: the buyer takes the first year's tax bill on a quick move-in home, which was assessed as dirt, and assumes that is the number. Use the full purchase price times 1.467%, minus the homestead savings, and you will not be surprised in year two.
:::

## Insurance

Every SeaFlower builder is building to the current Florida Building Code, and the developer's materials describe impact glass or shutters, reinforced block first floors and underground utilities. New construction earns wind-mitigation credits that older homes cannot, so premiums are typically well below the numbers people read about for 1980s houses near the coast. Budget roughly $2,500 to $7,000 a year for a single-family home depending on coverage, elevation and features, and get a real quote from an agent before you go under contract; it is a contingency worth writing in.

Flood insurance depends on the lot's FEMA zone. FEMA's flood hazard layer shows the interior of SeaFlower as Zone X (minimal hazard), with coastal AE and VE zones west of 86th Street and small Zone A pockets near 75th Street. Lenders do not require flood coverage in Zone X, but a Zone X policy is inexpensive and worth pricing three miles from the Gulf. Confirm your specific lot on Manatee County's flood map.
"""

ONE_TIME_MD = """
## One-time costs people forget

- **Earnest money and builder deposits.** Builders typically ask for a deposit at contract (often a percentage of the base price on a to-be-built home) plus deposits on design selections. These are negotiable in amount and, more importantly, in what happens to them if financing falls through. Read the default clause.
- **Lot premiums.** Lake, park, corner and oversize lots carry premiums that are quoted separately from the base price. The same plan can differ by tens of thousands of dollars across the street.
- **Design center and structural options.** Base price buys the base specification. Structural options must be chosen before the slab; finishes come later. This is where budgets drift.
- **Closing costs.** Roughly 2% to 3% of price for a financed purchase, before any builder credit. Most SeaFlower builders tie their biggest closing-cost credits and rate buydowns to their affiliated lender; you are never required to use that lender, and the math should be run both ways.
- **CDD is not an upfront cost.** Unlike an impact fee, the district debt is already spread across the annual assessment. You can prepay it later if you want a lower tax bill.
"""

FAQ = [
    ("Does SeaFlower have a CDD?", "Yes. SeaFlower sits in the Lake Flores Community Development District, created by Manatee County in January 2022. The annual assessment ranges from about $1,475 for a townhome to about $4,605 for a 60-foot lot in Phase 1C, based on the FY2027 proposed budget, and it is billed on your property-tax bill."),
    ("How much is the HOA at SeaFlower?", "$300.88 a month for a single-family home, $308.43 for a townhome and $327.70 for a twin villa, per the developer's December 2025 information sheet and David Weekley's community pages. The fee includes 1-Gig fiber internet and front and rear yard maintenance. The clubhouse portion is abated until The Garden Club opens."),
    ("What is the property-tax rate at SeaFlower?", "About 14.61 mills for 2025 in the Cedar Hammock Fire Control District that covers west Bradenton (David Weekley's pages show 14.671, the 2024 rate), or roughly $1,461 per $100,000 of taxable value before the homestead exemption. Confirm with the Manatee County Property Appraiser."),
    ("Is the CDD fee the same for every home?", "No. It depends on the phase and lot width. In the FY2027 proposed budget a 50-foot lot is $2,011 in Phase 1B1, $2,280 in Phase 1B2 and $3,899 in Phase 1C. Ask the builder which phase your lot is in."),
    ("Can I prepay the CDD?", "Yes. The bond portion is attached to the lot and can be paid off in a lump sum, which removes the debt-service part of the annual assessment. The operations-and-maintenance portion continues. Ask the district manager, Wrathell, Hunt and Associates, for a payoff figure."),
]


def pages():
    rows = []
    total_example = None
    for label, price, hoa, cdd, ins in EXAMPLES:
        pi = payment(price)
        tax = max(price - 50000, 0) * F.TAXES["millage"] / 1000 / 12
        total = pi + tax + hoa + cdd / 12 + ins / 12
        if "45' lot, Phase 1B2" in label:
            total_example = total
        rows.append((label, money(price), money(pi), money(tax), money(hoa), money(cdd / 12), money(ins / 12), f"<b>{money(total)}</b>"))
    intro = INTRO.replace("{TOTAL_EXAMPLE}", money(total_example))
    cdd26 = [(p, v) for p, v in F.CDD["fy2026"]]
    cdd27 = [(ph, lot, v) for ph, lot, v in F.CDD["fy2027"]]
    faq_html = "".join(faq_item(q, a, "costs") for q, a in FAQ)
    cdd_video = by_id("8E3fPi_pTcA")
    toc_items = [("worked-examples", "Worked monthly examples"), ("hoa-what-300-88-a-month-buys", "HOA"), ("cdd-the-line-item-out-of-state-buyers-miss", "CDD"), ("cdd-tables", "CDD tables by phase"),
                 ("property-taxes", "Property taxes"), ("insurance", "Insurance"), ("one-time-costs-people-forget", "One-time costs"), ("faq", "FAQ")]
    body = f"""
<section class="page-hero"><div class="container">
  {breadcrumb([("Home", "/"), ("Costs & fees", None)])}
  {eyebrow("Costs, HOA, CDD, taxes and insurance")}
  <h1>What a SeaFlower home <em style="font-style:italic;color:var(--coral-700)">really costs per month</em></h1>
  {speakable(intro)}
  <div class="page-hero__meta">{updated_badge()}<span>Sources: Lake Flores CDD budgets, developer HOA sheet, builder pages</span></div>
  {independent_note()}
</div></section>

<section class="section section--flush-top reveal"><div class="container"><div class="grid grid-sidebar">
  <div>
    <h2 id="worked-examples">Worked monthly examples</h2>
    <p class="lead">Five real product types at SeaFlower, using the builders' own base prices and the district's own assessment tables. Change the assumptions and the total moves, but the proportions hold.</p>
    {table(["Home", "Price", "Principal & interest", "Taxes", "HOA", "CDD", "Insurance", "Total / month"], rows, cls="pricing-table", numeric_cols=(1, 2, 3, 4, 5, 6, 7),
           note=f"Assumptions: {int(DOWN*100)}% down, 30-year fixed at {RATE*100:.1f}% (builder-lender buydowns are often lower), taxes at {F.TAXES['millage']} mills on price less a $50,000 homestead exemption, insurance estimated. CDD from the FY2027 proposed budget. Prices are illustrative base prices near each builder's published starting point; lot premiums and options are extra.")}
    {trent_take("Builders advertise a monthly payment on quick move-ins using a bought-down rate. That payment is real, but it usually leaves out the CDD, which lands in your escrow the first November. Ask for the payment with taxes at full value, CDD included, and insurance quoted. If the rep cannot produce it, I can.")}

    <div class="prose">{md(HOA_MD)}</div>
    <div class="prose">{md(CDD_MD)}</div>

    <h3 id="cdd-tables">Lake Flores CDD assessments by phase and lot</h3>
    <div class="grid grid-2" style="align-items:start">
      <div>{table(["Product (FY2026)", "Per year"], cdd26, numeric_cols=(1,), note="FY2026 amounts from the developer's HOA and CDD information sheet dated Dec 8, 2025 (includes $402.29 operations and maintenance).")}</div>
      <div>{table(["Phase", "Lot", "Per year (FY2027 proposed)"], cdd27, numeric_cols=(2,), note="FY2027 proposed budget presented May 2026, public hearing Aug 17, 2026. Phase N1 and 1B include $398.48 O&M; Phase 1C includes $370.58.")}</div>
    </div>
    <p class="note">{esc(F.CDD['builder_quotes'])} Bonds outstanding: {esc(F.CDD['bonds'])}. District manager: {esc(F.CDD['manager'])}.</p>
    <div class="grid grid-2 mt-3" style="align-items:start">
      <div>{lite_yt(cdd_video['id'], cdd_video['title'], cdd_video['duration'])}</div>
      <div>{callout("Florida law requires the CDD disclosure in bold type in your purchase contract (Fla. Stat. 190.048) and an HOA disclosure summary before you sign (Fla. Stat. 720.401), with a three-day right to cancel if it is missing. Read both; they are the most honest documents in the package.", "note", "The disclosures you will sign")}</div>
    </div>

    <div class="prose">{md(TAX_MD)}</div>
    <div class="prose">{md(ONE_TIME_MD)}</div>

    <h2 id="faq" style="margin-top:2em">Cost questions, answered</h2>
    {faq_html}
    {sources_list([
        ("Lake Flores CDD FY2027 proposed budget (assessment roll, p.14)", F.CDD['site'] + "/_assets/documents/fy-2027/2027-LFCDD-budget-proposed.pdf", "May 2026"),
        ("Lake Flores CDD FY2026 adopted budget", F.CDD['site'] + "/_assets/documents/fy-2026/2026-LFCDD-budget.pdf", "2025"),
        ("Lake Flores CDD: about the district", F.CDD['site'] + "/about", "Sep 3, 2026"),
        ("2026 SeaFlower HOA and CDD information sheet", "https://online.flippingbook.com/view/1053165353/1/", "Dec 8, 2025"),
        ("David Weekley Homes: SeaFlower Classic Homes (HOA, CDD, tax rate)", "https://www.davidweekleyhomes.com/new-homes/fl/sarasota/bradenton/seaflower-classic-homes", "Sep 3, 2026"),
        ("David Weekley Homes: SeaFlower Bungalow Homes", "https://www.davidweekleyhomes.com/new-homes/fl/sarasota/bradenton/seaflower-bungalow-homes", "Sep 3, 2026"),
        ("SeaFlower HOA portal (ICON Management)", F.HOA['portal'], "Sep 3, 2026"),
        ("Florida Statutes 190.048 (CDD disclosure) and 720.401 (HOA disclosure)", "https://www.leg.state.fl.us/statutes/", "Sep 3, 2026"),
    ])}
  </div>
  <aside>{toc(toc_items)}{sidebar_cta("Want the real number for a specific lot?", "Send me the builder, plan and lot and I will build the full monthly picture, incentives included.", "Ask Trenton")}</aside>
</div></div></section>

<section class="section section--sm reveal"><div class="container">{cta_band(title="Negotiating the numbers is the whole game.", text="Base price, lot premium, closing-cost credit, rate buydown, design credit: each builder moves on different ones. I know which, and when. Free strategy call, no obligation.")}</div></section>
"""
    schema = [breadcrumb_schema([("Home", "/"), ("Costs & fees", "/costs/")]), faq_schema(FAQ),
              {"@type": "Article", "@id": SITE["domain"] + "/costs/#article", "headline": "What a SeaFlower home really costs per month: HOA, CDD, taxes and insurance",
               "author": {"@id": SITE["domain"] + "/#trenton"}, "publisher": {"@id": SITE["domain"] + "/#org"}, "datePublished": F.AS_OF_ISO, "dateModified": F.AS_OF_ISO,
               "mainEntityOfPage": SITE["domain"] + "/costs/", "about": {"@id": SITE["domain"] + "/#seaflower"}, "speakable": {"@type": "SpeakableSpecification", "cssSelector": [".speakable"]}}]
    return [dict(
        path="/costs/", title="SeaFlower HOA Fees, Lake Flores CDD, Taxes and Insurance: The Real Monthly Cost",
        description="SeaFlower's HOA is $300.88 a month for single-family homes and includes fiber and yard care; the Lake Flores CDD runs about $1,475 to $4,605 a year by phase and lot width. Worked monthly examples, official CDD tables, tax and insurance math, verified Sept 2026.",
        body=body, schema=schema, priority="0.9", changefreq="monthly", type="article", published=F.AS_OF_ISO, modified=F.AS_OF_ISO,
    )]

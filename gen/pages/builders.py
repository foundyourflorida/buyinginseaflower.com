import re
from ..config import SITE
from ..components import *  # noqa
from ..content import facts as F
from ..content.builders_index import BUILDERS, TIER_LABEL, by_slug
from ..content.videos import by_id
from ..html import esc, md

# Trent's editorial per builder (first person). Keep grounded in the data modules.
TAKES = {
    "mi-homes": """
M/I is the entry ticket to SeaFlower and, right now, the builder with the most standing inventory. Townhomes and twin villas from $399,999, rear-load detached garages, and a long list of quick move-ins carrying "was" prices. Inventory carrying cost is leverage; a builder with twenty finished or nearly finished homes is a builder that negotiates. The attached-product HOA is a little higher because it covers exterior maintenance and insurance, which is exactly what a lock-and-leave buyer wants to pay for. Watch the advertised FHA rate offers: they are real, but they apply to specific homes and specific closing windows, and the APR is the number that matters.
""",
    "pulte-homes": """
I sold for Pulte for six years, so I will be blunt: this is the value engine of the community. The Scenic series is the lowest entry into a detached home here, the Veranda and Front Porch series add the porches and the ADU option that make SeaFlower feel like SeaFlower, and the Distinctive series is where the bigger single-story plans live. Pulte's published "savings" on quick move-ins are a starting point, not a ceiling. Pulte moves most on price and incentives in the last two weeks of a quarter, and division leadership can approve things the on-site rep cannot ask for. Run the affiliated-lender math against an outside quote every time.
""",
    "david-weekley-homes": """
I ran operations for this builder and did the final quality walk on homes before they were handed to buyers, so I know what a good Weekley build looks like. The Bungalow collection is the most photogenic product in SeaFlower: rear-load garages, porches on the street, one- and two-story plans on 45-foot lots. The Classic collection is all single-story plans with optional bonus rooms, up to a four-car garage on the Colston. Two things to know. Weekley's September 7% promotion explicitly excludes SeaFlower, which tells you this community is selling without help; ask about lot-specific and design-center credits instead. And Grace Home Lending is 75% owned by the builder, so compare its offer with an outside lender before you decide.
""",
    "cardel-homes": """
Cardel is the design-forward builder here, and the one that took the coastal-village brief most literally: front-garage and rear-garage versions of most plans, natural gas, and garage suites that add roughly 800 square feet on many models. I walked every Cardel model on camera; realistically you are shopping $700,000 to $1.2 million once you add the lot and the options people actually pick, even though base prices start lower. Cardel runs design-option promotions in cash amounts rather than rate buydowns, which suits buyers paying cash or bringing their own lender. Build times are longer than the production builders, so ask for the construction schedule in writing.
""",
    "issa-homes": """
Issa builds the estate tier: 80-foot lakefront lots on Lake Flores, semi-custom plans in the Lakeshore and Preserve collections, and a Hemingway model that won Best Overall at the 2026 Suncoast Parade of Homes. Read the pricing carefully. "From $1,250,000" excludes the homesite premium, and on a lakefront lot the premium is a real number that is only quoted on request. The two quick move-ins on Lake Flores Avenue are listed above $1.5 million. This is a longer build with a different deposit and draw structure than the production builders; get the contract reviewed before you sign it, not after.
""",
}


def badge(status):
    cls = {"active": "chip--green", "expired": "", "excluded": "chip--coral"}.get(status, "")
    return f'<span class="chip {cls}" style="font-size:11px;padding:3px 8px">{esc(status.title())}</span>'


def nice_date(iso):
    try:
        import datetime
        return datetime.datetime.strptime(iso[:10], "%Y-%m-%d").strftime("%b %-d, %Y")
    except Exception:
        return iso


def clean_name(n):
    return re.sub(r"^SeaFlower\s*[–-]\s*", "", n or "").strip()


def tidy(v, n=18):
    v = re.sub(r"\s*\(.*?\)", "", str(v or "")).split(";")[0].strip()
    return v[:n]


def short_note(p):
    n = re.sub(r"Plan #[A-Z0-9]+\.?\s*", "", p.get("notes", "") or "").split(".")[0].strip()
    return n[:58] + ("…" if len(n) > 58 else "")


def plan_table(c):
    rows = []
    for p in c["plans"]:
        baths = tidy(p.get("baths", ""), 12) + (f" + {tidy(p['half_baths'], 4)} half" if p.get("half_baths") and p["half_baths"] not in ("", "0") else "")
        link = f'<a href="{esc(p["url"])}" target="_blank" rel="noopener nofollow">Plan</a>' if p.get("url") else ""
        price = p.get("price", "").strip()
        price = price if price.startswith("$") and len(price) <= 14 else "On request"
        name = f"<b>{esc(p['name'])}</b>" + (f'<span class="plan-note">{esc(short_note(p))}</span>' if short_note(p) else "")
        rows.append((name, esc(price), esc(tidy(p.get("sqft", ""), 16)), esc(tidy(p.get("stories", ""), 3)), esc(tidy(p.get("beds", ""), 8)), esc(baths), esc(tidy(p.get("garage", ""), 16)), link))
    return table(["Plan", "Base price", "Sq ft", "Stories", "Beds", "Baths", "Garage", ""], rows, numeric_cols=(1, 2))


def qmi_table(b):
    rows = []
    for q in b["quick_move_ins"]:
        link = f'<a href="{esc(q["url"])}" target="_blank" rel="noopener nofollow">listing</a>' if q.get("url") else ""
        addr = re.sub(r",?\s*Bradenton,?\s*FL\s*34210", "", q.get("address", "")).split("(")[0].strip(" ,")
        rows.append((f"<b>{esc(tidy(q['plan'], 28))}</b>", esc(addr), esc(tidy(q.get("price", ""), 22)), esc(tidy(q.get("sqft", ""), 8)), f"{esc(tidy(q.get('beds', ''), 4))} / {esc(tidy(q.get('baths', ''), 10))}", esc(tidy(q.get("ready", ""), 24)), link))
    return table(["Plan", "Address", "Price", "Sq ft", "Beds / baths", "Status", ""], rows, numeric_cols=(2, 3), note=f"As listed by {esc(b['name'])} on {esc(nice_date(b['verified']))}. Inventory and pricing change weekly; I keep a current list, ask for it.")


def builder_page(b):
    slug = b["slug"]
    plan_count = sum(len(c["plans"]) for c in b["collections"])
    qmi_count = len(b["quick_move_ins"])
    price_low = "${:,}".format(b["price_low"]) if b.get("price_low") else ""
    fs = next((x for x in F.BUILDERS_SUMMARY if x["slug"] == slug), None) or {}
    product = fs.get("product", b["tagline"]).rstrip(".")
    price_txt = fs.get("price", b["price_phrase"].split("(")[0]).strip()
    price_txt = price_txt[0].lower() + price_txt[1:] if price_txt else ""
    office = re.sub(r",?\s*Bradenton,?\s*FL\s*34210", "", b["sales_office"].get("address", "")).strip(" ,.")
    lots_txt = fs.get("lots", ", ".join(b.get("lot_widths") or []))
    summary = (f"<strong>{esc(b['name'])} builds {esc(product)} in SeaFlower, {esc(price_txt)}.</strong> "
               f"{plan_count} floor plans on {esc(lots_txt)} lots, {esc(fs.get('sqft', b['sqft_range']))} square feet, {esc(b['beds'])} bedrooms, {qmi_count} quick move-in homes listed. "
               f"Sales office at {esc(office)}. Verified {esc(nice_date(b['verified']))}.")
    collections_html = ""
    for c in b["collections"]:
        cid = "collection-" + re.sub(r"[^a-z0-9]+", "-", c["name"].lower()).strip("-")
        lot = tidy(c.get("lot_width", ""), 14)
        collections_html += (f'<h3 id="{cid}">{esc(clean_name(c["name"]))} <span style="font-family:var(--font-body);font-size:14px;font-weight:600;color:var(--muted)">· {esc(lot)} · {esc(tidy(c.get("price_phrase", ""), 40))}</span></h3>'
                             f'<p class="note">{len(c["plans"])} plans' + (f' on {esc(lot)} homesites' if lot and lot != "—" else "") + f', {esc(tidy(c.get("price_phrase", ""), 40).lower())}. Base prices as published by the builder' + (f'; <a href="{esc(c["url"])}" target="_blank" rel="noopener nofollow">collection page</a>' if c.get("url") else "") + '.</p>' + plan_table(c))
    so = b["sales_office"]
    models = "".join(f"<li><b>{esc(m['name'])}</b> ({esc(clean_name(m.get('collection', '')))}) · {esc(re.sub(r',?\s*Bradenton,?\s*FL\s*34210', '', m.get('address', '')))}" + (f" · opened {esc(nice_date(m['opened']))}" if m.get("opened") else "") + (f" · {esc(m['sqft'])} sq ft" if m.get("sqft") else "") + "</li>" for m in b.get("models", []))
    consultants = ", ".join(so.get("consultants", [])) if so.get("consultants") else ""
    inc = b.get("incentives", [])
    inc_html = "".join(f'<li>{badge(i.get("status", ""))} <b>{esc(i["title"])}</b> <span class="small" style="color:var(--faint)">(as of {esc(i.get("as_of", ""))})</span><br><span class="small">{esc(i.get("detail", ""))[:420]}</span>' + (f' <a class="small" href="{esc(i["url"])}" target="_blank" rel="noopener nofollow">source</a>' if i.get("url") else "") + "</li>" for i in inc) or "<li>No incentive is currently published by the builder for SeaFlower. That does not mean nothing is available; it means it is negotiated on site.</li>"
    features = "".join(f"<li>{esc(x)}</li>" for x in b.get("features", []))
    watch = "".join(f"<li>{esc(x)}</li>" for x in b.get("watch_outs", []))
    schools = "".join(f"<li>{esc(x)}</li>" for x in b.get("schools", [])) or "<li>Not listed on the builder's page. See the <a href='/location/'>location guide</a> for zoned schools.</li>"
    news = "".join(f"<li><span class='small' style='color:var(--faint)'>{esc(n.get('date', ''))}</span> · " + (f'<a href="{esc(n["url"])}" target="_blank" rel="noopener nofollow">{esc(n["title"])}</a>' if n.get("url") else esc(n["title"])) + "</li>" for n in b.get("awards_news", [])[:8])
    fees = b.get("fees", {})
    fee_rows = [("HOA (as quoted by builder)", esc(fees.get("hoa", "") or "Not listed")), ("CDD (as quoted by builder)", esc(fees.get("cdd", "") or "Not listed")), ("Tax rate (as quoted)", esc(fees.get("tax_rate", "") or "Not listed"))]
    program_rows = [(k, esc(b.get(v, "") or "Not published")) for k, v in [("Warranty", "warranty"), ("Energy / construction", "energy"), ("Structure", "construction"), ("ADU / casita option", "adu"), ("Design center", "design_center"), ("Affiliated lender", "lender"), ("Build timeline", "build_timeline")]]
    video = by_id("mpxbdiSlNuw") if slug == "cardel-homes" else by_id("kCjttf-puQQ")
    others = "".join(f'<li><a href="/builders/{o["slug"]}/">{esc(o["name"])}</a> <span class="small" style="color:var(--faint)">{esc(o["price_phrase"][:48])}</span></li>' for o in BUILDERS if o["slug"] != slug)
    take = TAKES.get(slug, "")
    toc_items = [("take", "Trent's take"), ("plans", "Floor plans and prices"), ("quick-move-ins", "Quick move-ins"), ("model", "Model homes and sales office"), ("incentives", "Incentives"), ("fees", "Fees as quoted"), ("programs", "Warranty, lender, design"), ("watch-outs", "Watch-outs"), ("ask", "Ask about this builder")]
    body = f"""
<section class="page-hero"><div class="container">
  {breadcrumb([("Home", "/"), ("Builders", "/builders/"), (b["name"], None)])}
  {eyebrow("Builder profile · " + TIER_LABEL.get(b.get("tier", ""), "") + " tier")}
  <h1>{esc(b['name'])} at SeaFlower: <em style="font-style:italic;color:var(--coral-700)">plans, prices and what to know before you sign</em></h1>
  {speakable(summary)}
  <div class="page-hero__meta">{updated_badge(nice_date(b['verified']))}<span><a href="{esc(b['urls'].get('community', '#'))}" target="_blank" rel="noopener nofollow">Builder&rsquo;s SeaFlower page</a></span></div>
  {independent_note("Builder names are used to identify the builder only; plan and price data are quoted from the builder's public pages and belong to the builder.")}
</div></section>

<section class="section section--flush-top reveal"><div class="container">
  {fact_strip([(esc(b['price_phrase'].split('(')[0].split(';')[0].replace('Priced from: ', 'From ').replace('Estate Homes starting from ', 'From ').strip()[:18]), "starting price", "as phrased by builder"), (esc(", ".join(b['lot_widths'])) if b.get('lot_widths') else "See plans", "lot widths", esc(b.get('garage_orientation', ''))[:40]), (str(plan_count), "floor plans", esc(b['sqft_range']) + " sq ft"), (str(qmi_count), "quick move-ins", "listed " + esc(nice_date(b['verified']))), (esc(b['beds']), "bedrooms", esc(b['baths']) + " baths")])}
</div></section>

<section class="section reveal"><div class="container"><div class="grid grid-sidebar">
  <div>
    <h2 id="take">Trent&rsquo;s take</h2>
    {trent_take(take)}

    <h2 id="plans" style="margin-top:2em">Floor plans and base prices</h2>
    <p class="lead">Base prices as published by {esc(b['name'])} on {esc(nice_date(b['verified']))}. They exclude the lot premium, structural options and design selections. Square footage can vary by elevation and options.</p>
    {collections_html}

    <h2 id="quick-move-ins" style="margin-top:2em">Quick move-in homes</h2>
    {qmi_table(b) if qmi_count else "<p>No quick move-in homes were listed by the builder on " + esc(nice_date(b['verified'])) + ". Inventory turns over quickly; ask me for the current list.</p>"}

    <h2 id="model" style="margin-top:2em">Model homes and sales office</h2>
    <div class="card"><p style="margin:0 0 8px"><b>{esc(so.get('address', ''))}</b></p><p style="margin:0 0 8px">{esc(so.get('hours', '') or 'Hours not published')}</p>{('<p style="margin:0 0 8px">On-site consultants as published: ' + esc(consultants) + '</p>') if consultants else ''}{('<ul style="margin:8px 0 0">' + models + '</ul>') if models else ''}</div>
    {callout("If you plan to visit a model, tell me first. Builders register the agent who introduces you, and some will not let you add representation after a first unaccompanied visit. A five-minute call protects your options; it costs nothing.", "warn", "Before your first visit")}

    <h2 id="incentives" style="margin-top:2em">Incentives and promotions</h2>
    <ul class="stack" style="padding-left:0;list-style:none">{inc_html}</ul>
    {trent_take("Published incentives are the floor. The real conversation is about lot premium, closing-cost credits tied to the lender, design-center credits and structural options, and it happens with the sales manager, not the website. Timing matters: builders push hardest at the end of their fiscal quarters.")}

    <h2 id="fees" style="margin-top:2em">Fees as quoted by the builder</h2>
    {table(["Item", "As quoted"], fee_rows, note=(esc(fees.get('note', '')) + " Full HOA and CDD tables by phase and lot are on the <a href='/costs/'>costs and fees page</a>."))}

    <h2 id="programs" style="margin-top:2em">Warranty, lender, design center and construction</h2>
    {table(["Program", "Details"], program_rows)}
    {('<h3>What stands out</h3><ul class="checklist">' + features + '</ul>') if features else ''}

    <h2 id="watch-outs" style="margin-top:2em">Watch-outs</h2>
    <aside class="callout callout--warn"><ul style="margin:0">{watch}</ul></aside>

    <h3 style="margin-top:2em">Schools as listed by the builder</h3>
    <ul>{schools}</ul>
    <p class="note">{esc(F.SCHOOLS_NOTE)}</p>

    {('<h3 style="margin-top:2em">News and awards</h3><ul>' + news + '</ul>') if news else ''}
    {('<p class="note">' + esc(b['reviews']) + '</p>') if b.get('reviews') else ''}

    <h2 style="margin-top:2em">On video</h2>
    {lite_yt(video['id'], video['title'], video['duration'])}

    <h2 id="ask" style="margin-top:2em">Ask about {esc(b['short'])} at SeaFlower</h2>
    {lead_form("ask-" + slug, "Questions about " + b['name'] + "?", "Lot availability, real incentives, contract terms, build timelines. I answer personally.", submit="Send my question", interest="SeaFlower: " + b['name'], extra_hidden={"builder": b['name']}, message_label="What do you want to know about " + b['short'] + "?")}
    {sources_list([(s.get('title', ''), s.get('url', ''), s.get('date', '')) for s in b.get('sources', [])][:20])}
  </div>
  <aside>{toc(toc_items)}{sidebar_cta("Touring " + b['short'] + " models?", "Register me as your agent before your first visit and bring me along. I know their contracts and their playbook.")}<div class="card mt-2"><h4 style="font-size:18px">Compare with</h4><ul style="padding-left:1.1em;margin:0;font-size:15px">{others}</ul><a class="link-arrow" href="/homes/" style="margin-top:12px;font-size:14px">All plans side by side</a></div></aside>
</div></div></section>

<section class="section section--sm reveal"><div class="container">{cta_band()}</div></section>
"""
    schema = [breadcrumb_schema([("Home", "/"), ("Builders", "/builders/"), (b["name"], f"/builders/{slug}/")]),
              {"@type": "Article", "@id": SITE["domain"] + f"/builders/{slug}/#article", "headline": f"{b['name']} at SeaFlower: plans, prices and what to know",
               "author": {"@id": SITE["domain"] + "/#trenton"}, "publisher": {"@id": SITE["domain"] + "/#org"}, "datePublished": F.AS_OF_ISO, "dateModified": F.AS_OF_ISO,
               "mainEntityOfPage": SITE["domain"] + f"/builders/{slug}/", "about": [{"@id": SITE["domain"] + "/#seaflower"}, {"@type": "Organization", "name": b["name"], "url": b["urls"].get("community", "")}],
               "speakable": {"@type": "SpeakableSpecification", "cssSelector": [".speakable"]}}]
    return dict(
        path=f"/builders/{slug}/", title=f"{b['name']} at SeaFlower: Plans, Prices, Lot Sizes and Incentives (Sept 2026)",
        description=(f"{b['name']} at SeaFlower, Bradenton: {b['price_phrase'].split('(')[0].split(';')[0].strip()[:70]}. {plan_count} floor plans, {b['sqft_range'].split(' A/C')[0].replace(' sq ft', '')} sq ft, {qmi_count} quick move-ins, model address, fees as quoted, incentives and watch-outs from a former builder insider.")[:300],
        body=body, schema=schema, priority="0.8", changefreq="weekly", nav="/builders/", type="article", published=F.AS_OF_ISO, modified=F.AS_OF_ISO,
    )


INDEX_FAQ = [
    ("Which SeaFlower builder is the least expensive?", "M/I Homes, with townhomes and twin villas priced from $399,999, followed closely by Pulte's Scenic series from $404,990. Both are attached or compact detached products; the least expensive detached single-family homes are Pulte's."),
    ("Which builder has the most expensive homes?", "Issa Homes. Its estate homes on 80-foot lakefront lots start from $1,250,000 excluding the homesite premium, and its quick move-in homes were listed above $1.5 million in September 2026."),
    ("Who builds townhomes and villas in SeaFlower?", "Only M/I Homes. Its Row Homes are townhomes and its Village Homes are twin villas, together 158 units in Phase N1. Every other builder builds detached single-family homes."),
    ("Which builders offer an ADU or garage apartment?", "Cardel offers garage suites on many plans, Pulte's Front Porch series includes an ADU version of the Mabel II, and Issa offers garage-apartment versions of two plans. David Weekley's ADU availability at SeaFlower is not published. Every single-family lot in SeaFlower is zoned to allow one."),
    ("Can I use my own agent with every builder?", "Yes. All five builders cooperate with buyer's agents and the builder pays the commission. The catch is registration: most builders require the agent to accompany you or register you before your first visit. Call me before you tour and it is handled."),
]


def index_page():
    rows = []
    for fs in F.BUILDERS_SUMMARY:
        rows.append((f'<a href="/builders/{fs["slug"]}/"><b>{esc(fs["name"])}</b></a>', esc(fs["tier"]), esc(fs["product"]), esc(fs["lots"]), esc(fs["sqft"]), esc(fs["beds"]), esc(fs["price"])))
    cards = "".join(
        f'<a class="card card--hover card--link" href="/builders/{fs["slug"]}/"><div class="card__kicker">{esc(fs["tier"])} tier · {esc(fs["lots"])}</div><h3>{esc(fs["name"])}</h3><p>{esc(fs["product"])}. {esc(fs["sqft"])} sq ft, {esc(fs["beds"])} bedrooms.</p><p style="color:var(--green-900);font-weight:600;margin-top:10px">{esc(fs["price"])}</p><span class="link-arrow">Full profile</span></a>'
        for fs in F.BUILDERS_SUMMARY)
    faq_html = "".join(faq_item(q, a, "builders") for q, a in INDEX_FAQ)
    tour = by_id("kCjttf-puQQ")
    intro = ("<strong>Five builders sell new homes in SeaFlower:</strong> M/I Homes (townhomes and twin villas from $399,999), Pulte Homes (single-family from $404,990), "
             "David Weekley Homes (Bungalow homes from the $500s and Classic homes from the $600s), Cardel Homes (Cottage and Classic homes from the $500s) and Issa Homes "
             "(estate homes from $1,250,000 excluding homesite premium). Together they offer more than 60 floor plans from 1,486 to about 3,800 square feet. Verified " + F.AS_OF + ".")
    HOW = """
## How I would choose

1. **Start with the monthly number, not the base price.** Lot phase changes the CDD, product type changes the HOA, and lender tie-ins change the rate. Two homes with the same sticker can differ by $300 a month. The <a href="/costs/">costs page</a> has the math.
2. **Pick the lot type before the builder.** Rear-load 42' and 45' lots put porches on the street and driveways in the alley. 50' and 60' lots give you a yard and a front garage option. 80' lots are lakefront and semi-custom. The lot decides which two or three builders you are really choosing between.
3. **Decide whether time or price matters more.** Quick move-ins close in 30 to 120 days and carry the biggest discounts and rate buydowns. To-be-built homes get you the lot and the finishes you want, at base price plus options, six to fourteen months out.
4. **Ask what the builder is proud of.** Weekley talks warranty and energy testing. Cardel talks design and the garage suite. Pulte talks price and process. M/I talks inventory and the lock-and-leave HOA. Issa talks the lake. They are all right about themselves.
5. **Negotiate the things that are actually negotiable.** Closing-cost credits through the affiliated lender, design-center credits, lot premiums on slower-moving lots, structural option pricing, and appraisal-gap language. Base price moves least, and moves last.
"""
    body = f"""
<section class="page-hero"><div class="container">
  {breadcrumb([("Home", "/"), ("Builders", None)])}
  {eyebrow("The builders")}
  <h1>Five builders, one community: <em style="font-style:italic;color:var(--coral-700)">how they actually compare</em></h1>
  {speakable(intro)}
  <div class="page-hero__meta">{updated_badge()}<span>Two of these five builders I worked for directly.</span></div>
  {independent_note()}
</div></section>

<section class="section section--flush-top reveal"><div class="container">
  {table(["Builder", "Tier", "Product", "Lots", "Sq ft", "Beds", "Starting price (as phrased)"], rows, note="Prices as published by each builder on " + esc(F.AS_OF) + ". Exclude lot premiums and options. Click a builder for plans, quick move-ins, incentives and watch-outs.")}
</div></section>

<section class="section reveal"><div class="container">
  <div class="grid grid-3">{cards}</div>
</div></section>

<section class="section bg-shell reveal"><div class="container"><div class="grid grid-sidebar">
  <div class="prose">{md(HOW)}</div>
  <aside>{sidebar_cta("Not sure which builder?", "Tell me your budget, timeline and how you plan to live in the home. I will tell you which two to tour and why.", "Book a free call")}</aside>
</div></div></section>

<section class="section reveal"><div class="container">
  <div class="split">
    <div>{lite_yt(tour['id'], tour['title'], tour['duration'])}</div>
    <div>{eyebrow("Every builder, one afternoon")}<h2 style="font-size:clamp(28px,3.4vw,44px)">I toured all of them so you can shortlist from your couch</h2><p class="lead">Eight models, five builders, the amenities and my honest verdict. Chapters in the video description.</p>{btn("See every plan side by side", "/homes/", "primary", icon_name="layers")}</div>
  </div>
</div></section>

<section class="section section--sm reveal"><div class="container container--narrow">
  {section_head("Builder questions, answered", eyebrow_text="FAQ")}
  {faq_html}
  <p class="mt-3"><a class="link-arrow" href="/faq/">All buyer questions</a></p>
</div></section>

<section class="section section--sm reveal"><div class="container">{cta_band()}</div></section>
"""
    schema = [breadcrumb_schema([("Home", "/"), ("Builders", "/builders/")]), faq_schema(INDEX_FAQ),
              {"@type": "ItemList", "name": "Home builders in SeaFlower, Bradenton FL", "itemListElement": [{"@type": "ListItem", "position": i + 1, "name": b["name"], "url": SITE["domain"] + f"/builders/{b['slug']}/"} for i, b in enumerate(BUILDERS)]}]
    return dict(
        path="/builders/", title="SeaFlower Builders Compared: M/I, Pulte, David Weekley, Cardel and Issa Homes (Sept 2026)",
        description="All five SeaFlower builders side by side: products, lot widths, square footage, starting prices as each builder phrases them, sales offices and phones, plus how to choose between them from a former Pulte and David Weekley insider.",
        body=body, schema=schema, priority="0.9", changefreq="weekly",
    )


def pages():
    return [index_page()] + [builder_page(b) for b in BUILDERS]

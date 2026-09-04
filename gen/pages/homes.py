import re
from ..config import SITE
from ..components import *  # noqa
from ..content import facts as F
from ..content.builders_index import BUILDERS, all_plans, all_qmis
from ..content.videos import by_id
from ..html import esc, md


def num(s):
    m = re.search(r"\d[\d,]*", s or "")
    return int(m.group(0).replace(",", "")) if m else 0


def pages():
    plans = all_plans()
    qmis = all_qmis()
    prices = [num(p.get("price", "")) for _, _, p in plans if p.get("price", "").strip().startswith("$") and num(p.get("price", "")) > 100000]
    sqfts = [num(p.get("sqft", "")) for _, _, p in plans if num(p.get("sqft", ""))]
    chips = '<a href="#" class="chip is-active" data-filter="plan:all" role="button" aria-pressed="true">All builders</a>' + "".join(
        f'<a href="#" class="chip" data-filter="plan:{b["slug"]}" role="button" aria-pressed="false">{esc(b["short"])}</a>' for b in BUILDERS)
    qchips = '<a href="#" class="chip is-active" data-filter="qmi:all" role="button" aria-pressed="true">All builders</a>' + "".join(
        f'<a href="#" class="chip" data-filter="qmi:{b["slug"]}" role="button" aria-pressed="false">{esc(b["short"])}</a>' for b in BUILDERS if b["quick_move_ins"])
    def short_sqft(v):
        v = (v or "").split(" A/C")[0].split("(")[0].replace(" sq ft", "").strip()
        return v
    def short_price(v):
        v = (v or "").strip()
        return v if v.startswith("$") and len(v) <= 14 else ("On request" if not v.startswith("$") else v.split("(")[0].strip())
    def tidy(v, n=16):
        v = re.sub(r"\s*\(.*?\)", "", str(v or "")).split(";")[0].strip()
        return "—" if v.lower() in ("unverified", "") else v[:n]
    def coll(name):
        name = name.replace("SeaFlower – ", "").replace("Homes", "").replace(" – ", " ").replace("front garage", "front").replace("rear garage", "rear").replace("Series", "").strip()
        return re.sub(r"\s+", " ", name)[:22]
    prow = []
    for b, c, p in plans:
        stm = re.match(r"\d+", str(p.get("stories", "")))
        st = stm.group() if stm else "—"
        baths = tidy(p.get("baths", ""), 10) + (f" + {tidy(p['half_baths'], 4)}½" if p.get("half_baths") and p["half_baths"] not in ("", "0") else "")
        link = f'<a href="{esc(p["url"])}" target="_blank" rel="noopener nofollow">plan</a>' if p.get("url") else ""
        prow.append(f'<tr data-filter-group="plan" data-cat="{b["slug"]}"><td><a href="/builders/{b["slug"]}/">{esc(b["short"])}</a></td><td><b>{esc(p["name"])}</b></td><td>{esc(coll(c["name"]))}</td><td>{esc(tidy(c.get("lot_width", ""), 12))}</td>'
                    f'<td class=num data-sort="{num(p.get("sqft", ""))}" title="{esc(p.get("sqft", ""))}">{esc(short_sqft(p.get("sqft", "")))}</td><td>{esc(st)}</td><td>{esc(tidy(p.get("beds", ""), 8))}</td><td>{esc(baths)}</td><td>{esc(tidy(p.get("garage", ""), 14))}</td><td class=num data-sort="{num(p.get("price", "")) if p.get("price", "").strip().startswith("$") else 0}" title="{esc(p.get("price", ""))}">{esc(short_price(p.get("price", "")))}</td><td>{link}</td></tr>')
    qrow = []
    for b, q in qmis:
        link = f'<a href="{esc(q["url"])}" target="_blank" rel="noopener nofollow">listing</a>' if q.get("url") else ""
        addr = re.sub(r",?\s*Bradenton,?\s*FL\s*34210", "", q.get("address", "")).split("(")[0].strip(" ,")
        qrow.append(f'<tr data-filter-group="qmi" data-cat="{b["slug"]}"><td><a href="/builders/{b["slug"]}/">{esc(b["short"])}</a></td><td><b>{esc(tidy(q["plan"], 26))}</b></td><td>{esc(addr[:40])}</td><td class=num data-sort="{num(q.get("price", ""))}">{esc(q.get("price", ""))[:34]}</td><td class=num data-sort="{num(q.get("sqft", ""))}">{esc(q.get("sqft", ""))[:14]}</td><td>{esc(q.get("beds", ""))} / {esc(q.get("baths", ""))}</td><td>{esc(q.get("ready", ""))[:40]}</td><td>{link}</td></tr>')
    plan_table = (f'<div class="table-wrap"><table data-sortable><thead><tr><th>Builder</th><th>Plan</th><th>Collection</th><th>Lot</th><th class=num>Sq ft</th><th>Stories</th><th>Beds</th><th>Baths</th><th>Garage</th><th class=num>Base price</th><th></th></tr></thead><tbody>{"".join(prow)}</tbody></table></div>'
                  f'<p class="table-note">Click a column heading to sort. {len(plans)} plans as published by the builders on {esc(F.AS_OF)}; base prices exclude lot premiums and options. Square footage may vary by elevation.</p>')
    qmi_table = (f'<div class="table-wrap"><table data-sortable><thead><tr><th>Builder</th><th>Plan</th><th>Address</th><th class=num>Price</th><th class=num>Sq ft</th><th>Beds / baths</th><th>Status</th><th></th></tr></thead><tbody>{"".join(qrow)}</tbody></table></div>'
                 f'<p class="table-note">{len(qmis)} homes as listed by the builders on {esc(F.AS_OF)}. Inventory changes weekly; some builders show a "was" price, which is a negotiation signal, not a floor.</p>')
    intro = (f"<strong>SeaFlower offers {len(plans)} floor plans from five builders, from about {min(sqfts):,} to {max(sqfts):,} square feet, with published base prices from "
             f"${min(prices):,} to ${max(prices):,}.</strong> Issa Homes estate plans are priced on request above $1.25 million. {len(qmis)} quick move-in homes were listed on {F.AS_OF}. "
             "Every price below is quoted exactly as the builder publishes it and excludes lot premiums, options and closing costs.")
    PRICE_MD = """
## What "base price" leaves out

- **Lot premium.** Quoted separately, often $10,000 to $80,000 and more on lake or park lots. Same plan, different street, different number.
- **Structural options.** Extra garage bay, extended lanai, bonus room, pool bath, ADU or garage suite. Chosen before the slab is poured.
- **Design selections.** Cabinets, counters, flooring, lighting, tile. Base spec is livable; most buyers spend 5% to 15% of base price here.
- **Elevation.** Some exterior styles cost more. Ask which elevation the base price assumes.
- **Closing costs and prepaid items.** Typically 2% to 3% of price before builder credits, plus escrow for taxes and insurance.

:::trent
Quick move-in homes have the options already in them, so their price is closer to the real number. To-be-built homes look cheaper on the sign and rarely stay that way. When I compare a $585,000 quick move-in to a $486,000 base-price plan, I add the lot, the options the inventory home already has, and the timeline before I call one of them the better deal.
:::
"""
    body = f"""
<section class="page-hero"><div class="container">
  {breadcrumb([("Home", "/"), ("Homes & pricing", None)])}
  {eyebrow("Homes and pricing")}
  <h1>Every SeaFlower floor plan and price, <em style="font-style:italic;color:var(--coral-700)">side by side</em></h1>
  {speakable(intro)}
  <div class="page-hero__meta">{updated_badge()}<span>Sortable. Filter by builder.</span></div>
  {independent_note("Plan names and prices belong to the builders and are quoted for identification and comparison.")}
</div></section>

<section class="section section--flush-top reveal" id="plans"><div class="container">
  {section_head("All floor plans", "Base plans by builder and collection. Click through to the builder page for the plan drawing; drawings are the builders' copyright and are not reproduced here.", "Floor plans")}
  <div class="chip-row" style="margin-bottom:18px" role="group" aria-label="Filter plans by builder">{chips}</div>
  {plan_table}
</div></section>

<section class="section bg-shell reveal" id="quick-move-ins"><div class="container">
  {section_head("Quick move-in homes", "Finished or under-construction homes with a listed price and completion date. These are where the biggest discounts and rate buydowns live.", "Move in sooner")}
  <div class="chip-row" style="margin-bottom:18px" role="group" aria-label="Filter quick move-ins by builder">{qchips}</div>
  {qmi_table}
  <div class="grid grid-2 mt-4" style="align-items:start">
    <div>{lead_form("qmi-list", "Get this week's quick move-in list with incentives", "I update the inventory list weekly with the incentives builders are not putting on the website. I will send the current one.", submit="Send me the list", interest="SeaFlower quick move-in list", compact=True, success="On its way. I will send the current list and flag the two or three homes I would actually look at.")}</div>
    <div>{trent_take("The builders' own pages update on their schedule; mine updates when I walk the community, which is every couple of weeks. If a home has been sitting past its ready date, that is when the conversation about price and credits gets interesting.")}{lite_yt(by_id("fx345crY-mo")["id"], by_id("fx345crY-mo")["title"], by_id("fx345crY-mo")["duration"])}</div>
  </div>
</div></section>

<section class="section reveal"><div class="container"><div class="grid grid-sidebar">
  <div class="prose">{md(PRICE_MD)}</div>
  <aside>{sidebar_cta("Want a plan compared?", "Send me two or three plans and I will compare lot options, real pricing and build timing.", "Ask Trenton")}</aside>
</div></div></section>

<section class="section section--sm reveal"><div class="container">{cta_band(title="Shortlist made? Let&rsquo;s price it properly.", text="Base price, lot premium, options, incentives and the monthly number with taxes and CDD. I build the whole picture before you sign anything.")}</div></section>
"""
    schema = [breadcrumb_schema([("Home", "/"), ("Homes & pricing", "/homes/")]),
              {"@type": "Dataset", "name": "SeaFlower floor plans and base prices", "description": f"{len(plans)} floor plans from five builders in SeaFlower, Bradenton FL, with base prices as published on {F.AS_OF}.", "url": SITE["domain"] + "/homes/", "creator": {"@id": SITE["domain"] + "/#org"}, "dateModified": F.AS_OF_ISO, "license": "https://creativecommons.org/licenses/by/4.0/"}]
    return [dict(
        path="/homes/", title=f"SeaFlower Floor Plans and Prices: {len(plans)} Plans and {len(qmis)} Quick Move-Ins Compared (Sept 2026)",
        description=f"Every SeaFlower floor plan from M/I, Pulte, David Weekley, Cardel and Issa in one sortable table: square footage, beds, baths, garage and base price as published, plus {len(qmis)} quick move-in homes and what base price leaves out.",
        body=body, schema=schema, priority="0.9", changefreq="weekly",
    )]

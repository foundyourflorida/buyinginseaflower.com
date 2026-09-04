from ..config import SITE
from ..components import *  # noqa
from ..content import facts as F
from ..content.videos import by_id
from ..html import esc, md

INTRO = (
    "<strong>SeaFlower&reg; is a 1,175-acre master-planned coastal village in west Bradenton, Manatee County, Florida (ZIP 34210), "
    "south of Cortez Road West and west of 75th Street West, about three miles from Anna Maria Island.</strong> Lake Flores Land Company is developing it "
    "on the former Preston family flower farm. Phase One covers 400 acres with 1,063 homes from five builders, a resident-only amenity campus "
    "called The Garden Club, a 2.5-mile golf-cart trail around the 19-acre Lake Flores, and a Publix-anchored Village Center with apartments "
    "and a hotel. Full buildout is planned at about 4,000 homes."
)

STORY = """
## The story behind the name

For nearly 90 years the Preston family grew flowers here, mostly gladiolus, under the Manatee Fruit Company name. When farming stopped being viable in the early 2000s the family began planning something else for the land. Manatee County approved the plan in 2015 under the working name Lake Flores, a nod to Whiting Preston's mother, Flavia Florez Preston. The community was renamed SeaFlower before launch to tie the flower history to its position on the coastal mainland near Sarasota Bay.

The developer is Lake Flores Land Company, led by principal Ed Hill, with LAMB Properties as investment partner. Walter Preston still sits on the community development district board. The Welcome Center at 4505 Flower Fields Trail is itself a Cardel-built home with an 800-square-foot accessory dwelling unit, which tells you a lot about the design intent.

## What "coastal village" actually means

SeaFlower is heavily influenced by traditional neighborhood design without being a strict TND. In practice that means narrower streets designed for slower traffic, front porches close to the sidewalk, garages pushed to the rear on alleys for many products, pocket parks within a short walk, and a mixed-use center you can reach by golf cart. Four architectural styles are permitted: Coastal, West Indies, Craftsman and Transitional Farmhouse, in a palette of whites with warm accents.

Every single-family homesite is allowed an accessory dwelling unit, either a garage apartment or a detached casita connected by a breezeway. That is unusual for a Florida master plan and it changes the math for buyers who want a separate suite for guests, an office, or a rental income line.

:::trent
Rear-load garages are why the streets photograph so well: the street side is porches and windows, not garage doors. They also mean your driveway is in the alley. Bring your longest vehicle to the model and check the turning radius before you fall in love with a 42-foot lot.
:::
"""

RULES = [
    ("Is it gated?", F.COMMUNITY["gated"]),
    ("Is there an age restriction?", F.COMMUNITY["age_restricted"]),
    ("Are golf carts allowed?", F.COMMUNITY["golf_carts"]),
    ("Can I add or rent an ADU?", F.COMMUNITY["adu"]),
    ("Can I rent the whole house?", F.COMMUNITY["rentals"]),
    ("What about pets?", F.COMMUNITY["pets"]),
]


def pages():
    mayor = by_id("rU7t_DDvMkc")
    toc_items = [("at-a-glance", "At a glance"), ("the-story-behind-the-name", "The story"), ("master-plan", "Master plan and phases"), ("amenities", "The Garden Club and trail"),
                 ("village-center", "Village Center"), ("timeline", "Timeline"), ("rules", "Rules people ask about"), ("sales-pace", "Sales pace"), ("video", "Video")]
    lot_rows = "".join(f"<tr><td><b>{p}</b></td><td>{prod}</td><td class=num>{n}</td></tr>" for p, prod, n, w in F.LOT_MIX)
    ladder = "".join(
        f'<div class="card"><h4>{esc(n)}</h4><p style="margin:0 0 6px"><b>{esc(desc)}</b></p><p style="margin:0 0 6px">{esc(b)}</p><p style="margin:0;color:var(--green-900);font-weight:600;font-size:14.5px">{esc(price)}</p><a class="link-arrow" href="{href}" style="margin-top:10px;font-size:14px">Builder details</a></div>'
        for n, desc, b, price, href in F.PRODUCT_LADDER)
    amen = "".join(f'<div class="card"><h4>{esc(t)}</h4><p style="margin:0">{esc(d)}</p></div>' for t, d in F.GARDEN_CLUB)
    tenants = "".join(f'<span class="chip">{esc(t)}</span>' for t in F.VILLAGE_CENTER["tenants"])
    timeline = "".join(f'<li class="{"is-future" if any(k in d for k in ("Fall 2026", "About 2027")) else ""}"><b>{esc(d)}</b><span>{esc(t)}</span></li>' for d, t in F.TIMELINE)
    pace = "".join(f"<tr><td><b>{esc(d)}</b></td><td>{esc(t)}</td><td>{esc(s)}</td></tr>" for d, t, s in F.SALES_PACE)
    rules = "".join(faq_item(q, a, "community") for q, a in RULES)

    body = f"""
<section class="page-hero"><div class="container">
  {breadcrumb([("Home", "/"), ("Community", None)])}
  {eyebrow("The community")}
  <h1>SeaFlower, explained: <em style="font-style:italic;color:var(--coral-700)">a coastal village three miles from the Gulf</em></h1>
  {speakable(INTRO)}
  <div class="page-hero__meta">{updated_badge()}<span>Welcome Center: {esc(F.COMMUNITY['welcome_center']['address'])} · {esc(F.COMMUNITY['welcome_center']['phone'])}</span></div>
  {independent_note()}
  {photo_banner("resort-pool", "The Garden Club resort pool on Lake Flores (rendering courtesy of the developer)", cls="photo-banner--tall")}
</div></section>

<section class="section section--flush-top reveal" id="at-a-glance"><div class="container">
  {fact_strip([("1,175", "acres", "former flower farm"), ("1,063", "Phase One homes", "on 400 acres"), ("~4,000", "homes at buildout", "plus 600 apartments"), ("3.2", "miles to the beach", "per the site plan"), ("5", "builders", "$400s to $1.5M+"), ("Fall 2026", "Garden Club opens", "Publix too")])}
</div></section>

<section class="section reveal"><div class="container"><div class="grid grid-sidebar">
  <div>
    <div class="prose">{md(STORY)}</div>

    <h2 id="master-plan" style="margin-top:2.2em">Master plan and phases</h2>
    {photo_banner("aerial-lake-flores", "Phase One around Lake Flores, looking west to the Gulf (rendering courtesy of the developer)")}
    <p class="lead">Phase One is 1,063 homes in four sub-phases around Lake Flores. As of April 2026, 784 of those homesites had been released, with 400 lots finished and 384 more under construction through 2026. Phase Two is expected to start around 2027.</p>
    <div class="grid grid-2" style="align-items:start">
      <div>{table(["Phase", "Product", "Lots"], [(p, prod, n) for p, prod, n, w in F.LOT_MIX], numeric_cols=(2,), note="Lot counts from the Lake Flores CDD FY2027 assessment roll. Phase 1C is financed by the Series 2026 bonds, which is why its CDD assessment is higher.")}</div>
      <div>
        {trent_take("Ask which phase your lot sits in before you sign. It changes your CDD line by more than $1,500 a year between Phase 1B2 and Phase 1C on the same 50-foot lot, and it tells you whether the streets around you are finished or still a construction zone. The best premium lots in each release, lake, park and corner, go in the first few weeks.")}
        <p class="note" style="margin-top:12px">Full buildout: {esc(F.COMMUNITY['buildout']['homes'])} homes, {esc(F.COMMUNITY['buildout']['apartments'])} apartments, {esc(F.COMMUNITY['buildout']['hotel_rooms'])} hotel rooms and {esc(F.COMMUNITY['buildout']['commercial'])}.</p>
      </div>
    </div>
    <h3 style="margin-top:2em">The product ladder</h3>
    <p>Six home types map to five builders and five lot widths. Prices are as the builders phrase them on {esc(F.AS_OF)}.</p>
    <div class="lot-grid">{ladder}</div>

    <h2 id="amenities" style="margin-top:2.2em">The Garden Club, Lake Flores and the trail</h2>
    {photo_grid(["resort-pool", "fitness-center", "plumeria-hall", "gathering-hall", "fitness-studio"], ["The Garden Club resort pool on Lake Flores", "The fitness center", "Plumeria Hall, the resident lounge", "The Gathering Hall for events and clubs", "Fitness studio opening onto the lawn"])}
    <p class="lead">The Garden Club is the resident-only amenity campus designed by LRK on the shore of the 25-acre Lake Flores Park. It broke ground July 9, 2025 and is scheduled to open in fall 2026. An Art of Living Director programs the calendar.</p>
    <div class="amenity-list">{amen}</div>
    <p style="margin-top:18px">Around it: the {esc(F.COMMUNITY['lake'])}, the {esc(F.COMMUNITY['trail'])}, a nature trail through the wetland and upland preserves, two dog parks, pocket parks and a village green. The trail is maintained by the community development district; the Garden Club by the HOA.</p>
    {callout("The clubhouse portion of the HOA assessment is abated until The Garden Club is substantially complete. Budget for the monthly fee to step up after opening. Details on the <a href='/costs/'>costs and fees page</a>.", "info", "Fee note")}

    <h2 id="village-center" style="margin-top:2.2em">SeaFlower Village Center</h2>
    {photo_banner("event-lawn-evening", "The event lawn at dusk (rendering courtesy of the developer)")}
    <p class="lead">{esc(F.VILLAGE_CENTER['size'])}, developed by {esc(F.VILLAGE_CENTER['developers'])}. Anchored by {esc(F.VILLAGE_CENTER['anchor'])}. {esc(F.VILLAGE_CENTER['timeline'])}.</p>
    <div class="tenant-chips">{tenants}</div>
    <p class="note" style="margin-top:12px">Also planned: {esc(F.VILLAGE_CENTER['apartments'])}; {esc(F.VILLAGE_CENTER['hotel'])}. Tenant list as announced by the developer and CASTO; openings are staggered.</p>

    <h2 id="timeline" style="margin-top:2.2em">Timeline: built, building, coming</h2>
    <ol class="timeline">{timeline}</ol>

    <h2 id="rules" style="margin-top:2.2em">Rules people ask about</h2>
    {rules}

    <h2 id="sales-pace" style="margin-top:2.2em">How fast is it selling?</h2>
    {table(["Date", "Reported", "Source"], F.SALES_PACE, note="Cumulative counts from the developer, local press and RCLCO. Figures are as reported; the developer's and third-party counts do not always reconcile.")}
    {trent_take("Roughly 200 contracts in six months across five builders is a healthy pace for a community that is still building its amenity center. It is not a frenzy. That matters for you: builders here are competing with each other for the same buyer, which is exactly the environment where incentives and lot-premium negotiations happen. See <a href='/homes/'>homes and pricing</a>.")}

    <h2 id="video" style="margin-top:2.2em">Hear it from the person selling the most homes here</h2>
    <p>I sat down with David Weekley's Tina Seaman, who has sold so many homes in SeaFlower that buyers started calling her the mayor, and asked the questions you would ask.</p>
    {lite_yt(mayor['id'], mayor['title'], mayor['duration'])}

    {sources_list(F.SOURCES_COMMUNITY)}
  </div>
  <aside>{toc(toc_items)}{sidebar_cta()}</aside>
</div></div></section>

<section class="section section--sm reveal"><div class="container">{cta_band(title="Want to walk it with someone who used to run it?", text="I will tour SeaFlower with you, model by model, and tell you what the on-site reps cannot: which phase and lot fit your budget, what the true monthly number is, and what to negotiate.")}</div></section>
"""
    schema = [breadcrumb_schema([("Home", "/"), ("Community", "/community/")]),
              {"@type": "Residence", "@id": SITE["domain"] + "/#seaflower", "name": "SeaFlower", "alternateName": F.COMMUNITY["aka"],
               "description": "1,175-acre master-planned coastal village in west Bradenton, Florida, with about 4,000 homes planned at buildout.",
               "url": "https://seaflower.com", "telephone": "+19412120801",
               "address": {"@type": "PostalAddress", "streetAddress": "4505 Flower Fields Trail", "addressLocality": "Bradenton", "addressRegion": "FL", "postalCode": "34210", "addressCountry": "US"},
               "geo": {"@type": "GeoCoordinates", "latitude": SITE["geo"]["lat"], "longitude": SITE["geo"]["lng"]},
               "containedInPlace": {"@type": "AdministrativeArea", "name": "Manatee County, Florida"},
               "amenityFeature": [{"@type": "LocationFeatureSpecification", "name": n, "value": True} for n in ["The Garden Club amenity center", "Lake Flores Trail (2.5 miles, golf-cart friendly)", "Lake Flores Park", "Resort pool with lap lanes", "Pickleball courts", "Dog parks", "Village Center with Publix"]]},
              faq_schema(RULES),
              {"@type": "WebPage", "@id": SITE["domain"] + "/community/#page", "url": SITE["domain"] + "/community/", "name": "SeaFlower community guide", "about": {"@id": SITE["domain"] + "/#seaflower"}, "dateModified": F.AS_OF_ISO, "speakable": {"@type": "SpeakableSpecification", "cssSelector": [".speakable"]}}]
    return [dict(
        path="/community/", title="SeaFlower Bradenton Community Guide: Master Plan, Amenities, Village Center and Rules",
        description="What SeaFlower in Bradenton actually is: 1,175 acres, 1,063 Phase One homes, The Garden Club opening fall 2026, the Lake Flores golf-cart trail, the Publix-anchored Village Center, plus rules on gates, golf carts, ADUs and rentals. Verified Sept 2026.",
        body=body, schema=schema, priority="0.9", changefreq="weekly", nav="/community/",
    )]

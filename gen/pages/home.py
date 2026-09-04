from ..config import SITE
from ..components import *  # noqa
from ..content import facts as F
from ..content.builders_index import BUILDERS, TIER_LABEL
from ..content.videos import by_id
from ..content.testimonials import TESTIMONIALS
from ..html import esc, md

TEASER_FAQ = [
    ("Do I need a buyer's agent to buy new construction in SeaFlower?", "You are allowed to buy without one, but the builder's sales consultant works for the builder. A buyer's agent costs you nothing extra on new construction because the builder pays the commission, and the agent negotiates incentives, reviews the contract and walks the build. Most builders require your agent to register you before or at your first visit, so call before you tour."),
    ("How much are the HOA and CDD fees at SeaFlower?", "The HOA is $300.88 a month for a single-family home ($308.43 townhome, $327.70 villa) and includes 1-Gig fiber and yard maintenance. The Lake Flores CDD adds roughly $1,475 to $4,605 a year depending on phase and lot width, billed on the tax bill. Full tables are on the costs page."),
    ("How far is SeaFlower from the beach?", "The developer's site plan measures 3.2 miles to the beach. Bradenton Beach is about an 8-minute drive, Coquina Beach about 12, and Longboat Key about 18, per Cardel's published drive times."),
    ("Which builders are in SeaFlower and what do homes cost?", "M/I Homes (townhomes and villas from $399,999), Pulte (from $404,990), David Weekley (Bungalow homes from the $500s, Classic from the $600s), Cardel (from the $500s) and Issa Homes (estate homes from $1,250,000 excluding homesite premium), as published in September 2026."),
    ("Is SeaFlower gated or age-restricted?", "Neither. No gates appear on the site plan and streets are being turned over to Manatee County as public roads. It is an all-ages community."),
]


def pages():
    hero_video = by_id("kCjttf-puQQ")
    vids = [by_id(v) for v in ("rU7t_DDvMkc", "mpxbdiSlNuw", "XMQCzXI7Sow")]
    start = [
        ("The community", "1,175 acres, 1,063 Phase One homes, The Garden Club, the golf-cart trail, the Village Center and the rules people ask about.", "/community/", "map-pin"),
        ("The builders", "M/I, Pulte, David Weekley, Cardel and Issa compared: products, lots, prices, models, incentives and watch-outs.", "/builders/", "layers"),
        ("Homes and pricing", "Every floor plan and every quick move-in home in one sortable table, with what base price leaves out.", "/homes/", "home"),
        ("Costs and fees", "HOA, the Lake Flores CDD by phase and lot, property taxes, insurance and worked monthly examples.", "/costs/", "dollar"),
        ("Buyer FAQ", "Sixty-plus questions from real buyers, answered with sources and a former insider's perspective.", "/faq/", "book"),
        ("Location", "Beaches, schools, shopping, hospitals, airports, flood and evacuation zones, and drive times.", "/location/", "compass"),
    ]
    start_cards = "".join(card(t, b, h, i, link_label="Read the guide") for t, b, h, i in start)
    brow = "".join(f'<tr><td><a href="/builders/{fs["slug"]}/"><b>{esc(fs["name"])}</b></a></td><td>{esc(fs["product"])}</td><td>{esc(fs["lots"])}</td><td>{esc(fs["sqft"])}</td><td>{esc(fs["price"])}</td></tr>' for fs in F.BUILDERS_SUMMARY)
    video_cards = "".join(video_card(v) for v in vids)
    faq_html = "".join(faq_item(q, a, "home") for q, a in TEASER_FAQ)
    try:
        from .blog import POSTS
        latest = sorted(POSTS, key=lambda p: p["date"], reverse=True)[:3]
        post_cards = "".join(f'<a class="card card--hover card--link" href="/blog/{p["slug"]}/"><div class="card__kicker">{esc(p["category"])} · {esc(p["date_display"])}</div><h3 style="font-size:22px">{esc(p["title"])}</h3><p>{esc(p["excerpt"])}</p><span class="link-arrow">Read</span></a>' for p in latest)
        posts_section = f'<section class="section reveal"><div class="container">{section_head("From the blog", "Long-form answers to the questions that come up on every strategy call.", "Latest")}<div class="grid grid-3">{post_cards}</div><p class="mt-3"><a class="link-arrow" href="/blog/">All articles</a></p></div></section>'
    except Exception:
        posts_section = ""
    why = [
        ("A village, not a subdivision", "Narrow streets, porches on the sidewalk, garages in the alley, pocket parks, and a 2.5-mile trail you can ride a golf cart on to a Publix. It is traditional neighborhood design on Florida's coastal mainland.", "trees"),
        ("An ADU on every single-family lot", "Garage apartments and detached casitas are allowed on every single-family homesite, an unusual county approval. That means a guest suite, a home office, or a rental income line, with a one-year owner-occupancy rule before renting.", "key"),
        ("Three miles from the Gulf", "Anna Maria Island and Bradenton Beach are a short drive, Longboat Key under ten miles, Sarasota and Tampa within an hour, and IMG Academy is next door.", "umbrella"),
    ]
    why_cards = "".join(f'<div class="card"><div class="card__icon">{icon(i)}</div><h3>{t}</h3><p>{b}</p></div>' for t, b, i in why)
    body = f"""
<section class="hero"><div class="container hero__inner">
  <div>
    {eyebrow("Independent buyer&rsquo;s guide · Bradenton, Florida")}
    <h1>Buying in SeaFlower? <em>Start with someone who used to run it.</em></h1>
    <p class="lead">Every builder, every floor plan, every fee and every question buyers ask, verified and explained by a former builder insider who now represents buyers only. When you are ready, a free strategy call.</p>
    <div class="btn-row">{btn("Book a free strategy call", SITE['booking_page'], "coral", "lg", "calendar", cta="hero-book")}{btn("Watch the full tour", "/videos/", "ghost", "lg", "video", cta="hero-video")}</div>
    <div class="hero__meta"><span>{icon('check')} 5 builders compared</span><span>{icon('check')} 60+ floor plans and prices</span><span>{icon('check')} HOA, CDD and tax math</span><span>{icon('check')} Verified {esc(F.AS_OF)}</span></div>
  </div>
  <div class="hero__media">
    {lite_yt(hero_video['id'], hero_video['title'], hero_video['duration'])}
    <div class="hero__badge"><img src="{SITE['headshot']}" alt="Trenton Miller" width="48" height="48"><div><strong>Trenton Miller, MBA</strong><span>Seven years on the builder side. David Weekley operations manager who briefly oversaw SeaFlower. Now a buyer&rsquo;s agent with LPT Realty.</span></div></div>
  </div>
</div></section>

<section class="section section--sm section--flush-top reveal" id="trust"><div class="container">
  <div class="stats">
    {stat("7", "years inside builders", "Pulte, Del Webb and David Weekley")}
    {stat("$150M", "in new-home sales", "as a builder top producer", small="+")}
    {stat("300", "buyers represented", "most from out of state", small="+")}
    {stat("#1", "Salesperson of the Year", "Tampa Bay Builders Association")}
  </div>
  {independent_note()}
</div></section>

<section class="section bg-shell reveal" id="start-here"><div class="container">
  {section_head("Start here", "Six guides that answer what the model-home visit will not. Each one is dated and sourced.", "The guide")}
  <div class="grid grid-3">{start_cards}</div>
</div></section>

<section class="section reveal" id="at-a-glance"><div class="container">
  {section_head("SeaFlower at a glance", eyebrow_text="The numbers")}
  {fact_strip([("1,175", "acres", "on the former Preston flower farm"), ("1,063", "Phase One homes", "784 released as of Apr 2026"), ("3.2", "miles to the beach", "per the site plan"), ("$400s", "to $1.5M+", "as published by builders"), ("Fall 2026", "The Garden Club opens", "Publix too"), ("270", "homes sold", "as of June 2026", )])}
</div></section>

<section class="section section--flush-top reveal" id="builders"><div class="container">
  {section_head("Five builders, compared", "Prices as each builder phrases them on " + esc(F.AS_OF) + ". Click through for plans, quick move-ins, incentives and my take.", "Builders")}
  <div class="table-wrap"><table><thead><tr><th>Builder</th><th>Product</th><th>Lots</th><th>Sq ft</th><th>Starting price</th></tr></thead><tbody>{brow}</tbody></table></div>
  <div class="btn-row mt-3">{btn("Compare all five", "/builders/", "primary", icon_name="layers")}{btn("Every floor plan and price", "/homes/", "ghost")}</div>
</div></section>

<section class="section bg-green reveal" id="videos"><div class="container">
  {section_head("Watch before you tour", "I toured every builder, put the community&rsquo;s own leadership on camera, and walked every Cardel model. Filmed for buyers, not for the builders.", "Videos")}
  <div class="grid grid-3">{video_cards}</div>
  <p class="mt-3">{btn("All videos", "/videos/", "white", icon_name="video")}</p>
</div></section>

<section class="section reveal" id="guide"><div class="container"><div class="split">
  <div>
    {eyebrow("Free download")}
    <h2>The SeaFlower Buyer&rsquo;s Guide</h2>
    <p class="lead">Builder comparison, the real monthly number, lot and phase notes, and the negotiation checklist I use with clients. Updated as builders release phases and pricing.</p>
    <ul class="checklist"><li>All five builders, prices and lot widths in one table</li><li>HOA, CDD, tax and insurance worksheet</li><li>Incentive and contract checklist from a former builder rep</li><li>Out-of-state buying timeline</li></ul>
  </div>
  <div>{lead_form("home-guide", "Send me the guide", "I email it personally, usually within a few hours.", submit="Email me the guide", interest="SeaFlower Buyer's Guide", compact=True, success="On its way. Check your inbox (and the promotions tab).")}</div>
</div></div></section>

<section class="section bg-sand reveal" id="why"><div class="container">
  {section_head("Why SeaFlower is different", "Three things that are true here and not true of most new communities on the Gulf Coast.", "The case for it", center=True)}
  <div class="grid grid-3">{why_cards}</div>
  <p class="center mt-3"><a class="link-arrow" href="/community/">The full community guide</a></p>
</div></section>

<section class="section reveal" id="about"><div class="container"><div class="split">
  <div><div class="card" style="padding:14px;background:linear-gradient(160deg,#fff,var(--sand))"><img src="/assets/images/trenton-miller-800.jpg" alt="Trenton Miller, buyer's agent, Found Your Florida" width="800" height="800" style="border-radius:12px" loading="lazy"></div></div>
  <div>
    {eyebrow("Who is behind this")}
    <h2>I sold homes for the builder. Now I make sure the builder treats you right.</h2>
    <p class="lead">Six years as a top producer with Pulte and Del Webb, then a year in operations with David Weekley Homes doing the final quality walk on every home, and for a stretch overseeing SeaFlower itself. I left to represent buyers only. The builder still pays the commission; the difference is who I work for.</p>
    <div class="btn-row">{btn("About Trenton", "/about/", "primary")}{btn("Book a free call", SITE['booking_page'], "ghost", icon_name="calendar", cta="home-about-book")}</div>
  </div>
</div></div></section>

<section class="section bg-shell reveal" id="reviews"><div class="container">
  {section_head("What buyers say", eyebrow_text="Reviews", center=True)}
  <div class="testimonials">{"".join(testimonial(q, w, l) for q, w, l in TESTIMONIALS[:3])}</div>
</div></section>

<section class="section reveal" id="faq"><div class="container container--narrow">
  {section_head("Questions buyers ask first", eyebrow_text="FAQ")}
  {faq_html}
  <p class="mt-3"><a class="link-arrow" href="/faq/">All sixty-plus questions</a></p>
</div></section>

{posts_section}

<section class="section section--sm reveal"><div class="container">{cta_band()}</div></section>
"""
    schema = [faq_schema(TEASER_FAQ),
              {"@type": "WebPage", "@id": SITE["domain"] + "/#webpage", "url": SITE["domain"] + "/", "name": "SeaFlower Bradenton buyer's guide", "isPartOf": {"@id": SITE["domain"] + "/#website"}, "about": {"@id": SITE["domain"] + "/#seaflower"}, "dateModified": F.AS_OF_ISO, "speakable": {"@type": "SpeakableSpecification", "cssSelector": [".speakable", ".hero .lead"]}},
              {"@type": "VideoObject", "name": hero_video["title"], "description": hero_video["blurb"], "thumbnailUrl": f"https://i.ytimg.com/vi/{hero_video['id']}/maxresdefault.jpg", "uploadDate": hero_video["date"], "duration": f"PT{hero_video['seconds']//60}M{hero_video['seconds']%60}S", "embedUrl": f"https://www.youtube-nocookie.com/embed/{hero_video['id']}", "author": {"@id": SITE["domain"] + "/#trenton"}}]
    return [dict(
        path="/", title="SeaFlower Bradenton Buyer's Guide: Builders, Prices, HOA and CDD Fees (2026)", title_full=False,
        description="The independent guide to buying in SeaFlower, Bradenton FL: all five builders compared, 60+ floor plans and prices, HOA and Lake Flores CDD fees, location, videos and 60+ buyer questions, from a former David Weekley operations manager who now represents buyers.",
        body=body, schema=schema, priority="1.0", changefreq="weekly", nav="/",
        og_image=f"https://i.ytimg.com/vi/{hero_video['id']}/maxresdefault.jpg",
    )]

from ..config import SITE
from ..components import *  # noqa
from ..content import facts as F
from ..content.posts import POSTS
from ..content.videos import by_id
from ..html import esc, md


POST_PHOTOS = {"golf-carts-at-seaflower": "golf-cart", "the-garden-club-seaflower-amenity-center": "resort-pool", "seaflower-village-center-publix": "event-lawn-evening",
               "seaflower-site-plan-phases-explained": "aerial-lake-flores", "history-of-seaflower-preston-farm-lake-flores": "aerial-lake-flores", "rear-load-vs-front-load-lots-seaflower": "model-home",
               "hurricane-preparedness-new-seaflower-home": "model-home", "adus-garage-apartments-seaflower": "model-home", "honest-pros-and-cons-of-buying-in-seaflower": "aerial-lake-flores",
               "seaflower-vs-lakewood-ranch": "aerial-lake-flores", "seaflower-vs-wellen-park-vs-parrish": "golf-cart", "moving-to-west-bradenton": "golf-cart", "second-home-seasonal-buying-seaflower": "resort-pool",
               "seaflower-construction-timeline": "event-lawn-evening", "manatee-county-growth-and-seaflower": "aerial-lake-flores", "new-construction-inspections-seaflower": "model-home", "design-center-strategy-seaflower": "plumeria-hall"}


def post_page(p, others):
    ph = POST_PHOTOS.get(p["slug"])
    try:
        v = by_id(p["video"]) if p.get("video") else None
    except Exception:
        v = None
    related = "".join(f'<li><a href="/blog/{o["slug"]}/">{esc(o["title"])}</a></li>' for o in others[:4])
    body = f"""
<section class="page-hero"><div class="container container--narrow">
  {breadcrumb([("Home", "/"), ("Blog", "/blog/"), (p["category"], None)])}
  {eyebrow(p["category"])}
  <h1 style="font-size:clamp(32px,4.4vw,54px)">{esc(p['title'])}</h1>
  <p class="lead">{esc(p['excerpt'])}</p>
  <div class="post-meta" style="margin-top:18px"><img src="{SITE['headshot']}" alt="" width="36" height="36"><span>By <a href="/about/">{SITE['agent_credentials']}</a></span><span>{esc(p['date_display'])}</span><span>{updated_badge()}</span></div>
  {independent_note()}
  {photo_banner(ph) if ph else ''}
</div></section>

<section class="section section--flush-top"><div class="container container--narrow">
  <div class="prose">{md(p['body'])}</div>
  {('<div class="mt-4">' + lite_yt(v['id'], v['title'], v['duration']) + '</div>') if v else ''}
  {author_box()}
  <div class="grid grid-2 mt-4" style="align-items:start">
    <div class="card"><h4 style="font-size:20px">Keep reading</h4><ul style="padding-left:1.1em;margin:0;font-size:15px">{related}</ul></div>
    <div>{lead_form("post-" + p['slug'][:20], "Have a question about this?", "Ask it here and I will answer personally.", submit="Ask Trenton", interest="Blog: " + p['title'][:60], compact=True)}</div>
  </div>
</div></section>

<section class="section section--sm reveal"><div class="container">{cta_band()}</div></section>
"""
    schema = [breadcrumb_schema([("Home", "/"), ("Blog", "/blog/"), (p["title"], f"/blog/{p['slug']}/")]),
              {"@type": "BlogPosting", "@id": SITE["domain"] + f"/blog/{p['slug']}/#post", "headline": p["title"], "description": p["excerpt"],
               "image": SITE["domain"] + (photo_src(ph) if ph else SITE["og_default"]), "author": {"@id": SITE["domain"] + "/#trenton"}, "publisher": {"@id": SITE["domain"] + "/#org"},
               "datePublished": p["date"], "dateModified": p["date"], "mainEntityOfPage": SITE["domain"] + f"/blog/{p['slug']}/", "about": {"@id": SITE["domain"] + "/#seaflower"},
               "articleSection": p["category"], "inLanguage": "en-US"}]
    return dict(path=f"/blog/{p['slug']}/", title=p["title"], description=p["excerpt"], body=body, schema=schema, type="article", published=p["date"], modified=p["date"],
                priority="0.7", changefreq="monthly", nav="/blog/", og_image=(photo_src(ph) if ph else None))


def index_page():
    posts = sorted(POSTS, key=lambda p: p["date"], reverse=True)
    cards = "".join(f'<a class="card card--hover card--link" href="/blog/{p["slug"]}/"><div class="card__kicker">{esc(p["category"])} · {esc(p["date_display"])}</div><h3 style="font-size:22px">{esc(p["title"])}</h3><p>{esc(p["excerpt"])}</p><span class="link-arrow">Read</span></a>' for p in posts)
    cats = sorted(set(p["category"] for p in posts))
    chips = '<a href="#" class="chip is-active" data-filter="post:all" role="button" aria-pressed="true">All</a>' + "".join(f'<a href="#" class="chip" data-filter="post:{esc(c.lower().replace(" ", "-").replace("&", "and"))}" role="button" aria-pressed="false">{esc(c)}</a>' for c in cats)
    cards = "".join(f'<div data-filter-group="post" data-cat="{esc(p["category"].lower().replace(" ", "-").replace("&", "and"))}"><a class="card card--hover card--link" href="/blog/{p["slug"]}/" style="height:100%"><div class="card__kicker">{esc(p["category"])} · {esc(p["date_display"])}</div><h3 style="font-size:22px">{esc(p["title"])}</h3><p>{esc(p["excerpt"])}</p><span class="link-arrow">Read</span></a></div>' for p in posts)
    body = f"""
<section class="page-hero"><div class="container">
  {breadcrumb([("Home", "/"), ("Blog", None)])}
  {eyebrow("The blog")}
  <h1>Long answers to the questions <em style="font-style:italic;color:var(--coral-700)">that come up on every call</em></h1>
  <p class="lead">Fees, builders, contracts, flood zones, comparisons and monthly market updates, written by a former builder insider and sourced to the primary documents.</p>
  <div class="page-hero__meta"><span>{len(posts)} articles</span><span><a href="/feed.xml">RSS</a></span></div>
</div></section>
<section class="section section--flush-top"><div class="container">
  <div class="chip-row" style="margin-bottom:22px" role="group" aria-label="Filter by category">{chips}</div>
  <div class="grid grid-3">{cards}</div>
</div></section>
<section class="section section--sm reveal"><div class="container">{cta_band()}</div></section>
"""
    return dict(path="/blog/", title="SeaFlower Blog: Fees, Builders, Contracts, Comparisons and Market Updates",
                description="Long-form answers about buying in SeaFlower, Bradenton: HOA and CDD fees explained, builder deep dives, flood zone facts, SeaFlower vs Lakewood Ranch, incentives, quick move-ins and monthly market updates from a former builder insider.",
                body=body, schema=[breadcrumb_schema([("Home", "/"), ("Blog", "/blog/")])], priority="0.7", changefreq="weekly")


def pages():
    out = [index_page()]
    for i, p in enumerate(POSTS):
        others = [o for o in POSTS if o["slug"] != p["slug"]]
        others = others[i:] + others[:i]
        out.append(post_page(p, others))
    return out

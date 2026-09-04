from ..config import SITE
from ..components import *  # noqa
from ..content.videos import VIDEOS, LONGFORM, SHORTS, CATEGORIES, by_id
from ..html import esc


def video_schema(v):
    return {
        "@type": "VideoObject", "name": v["title"], "description": v["blurb"],
        "thumbnailUrl": [f"https://i.ytimg.com/vi/{v['id']}/maxresdefault.jpg", f"https://i.ytimg.com/vi/{v['id']}/hqdefault.jpg"],
        "uploadDate": v["date"], "duration": f"PT{v['seconds'] // 60}M{v['seconds'] % 60}S",
        "embedUrl": f"https://www.youtube-nocookie.com/embed/{v['id']}", "contentUrl": f"https://www.youtube.com/watch?v={v['id']}",
        "author": {"@id": SITE["domain"] + "/#trenton"}, "publisher": {"@id": SITE["domain"] + "/#org"},
    }


def pages():
    featured = by_id("kCjttf-puQQ")
    chips = "".join(
        f'<a href="#" class="chip{" is-active" if c == "all" else ""}" data-filter="video:{c}" role="button" aria-pressed="{"true" if c == "all" else "false"}">{esc(l)}</a>'
        for c, l in CATEGORIES
    )
    long_cards = "".join(video_card(v, show_desc=True) for v in LONGFORM if v["id"] != featured["id"])
    short_cards = "".join(video_card(v) for v in SHORTS)
    body = f"""
<section class="page-hero"><div class="container">
  {breadcrumb([("Home", "/"), ("Videos", None)])}
  {eyebrow("Watch before you tour")}
  <h1>SeaFlower on video, <em style="font-style:italic;color:var(--coral-700)">without the sales script</em></h1>
  <p class="lead">Every builder toured, the community leadership interviewed, and the new-construction lessons I learned in seven years on the builder side. All of it filmed on my own time, for buyers.</p>
  <div class="page-hero__meta"><span>{len(LONGFORM)} full-length videos</span><span>{len(SHORTS)} shorts</span><span><a href="{SITE['youtube_channel']}" target="_blank" rel="noopener">Subscribe on YouTube</a></span></div>
</div></section>

<section class="section section--flush-top reveal"><div class="container">
  <div class="split">
    <div>{lite_yt(featured['id'], featured['title'], featured['duration'], cls="reveal")}</div>
    <div>
      {eyebrow("Start here")}
      <h2 style="font-size:clamp(28px,3.4vw,44px)">{esc(featured['title'])}</h2>
      <p class="lead">{esc(featured['blurb'])}</p>
      <p class="note">{featured['date_display']} · {featured['duration']} · Chapters cover each builder, The Garden Club, Lake Flores Trail and the Village Center plan.</p>
      <div class="btn-row mt-2">{btn("Compare the builders", "/builders/", "primary", icon_name="layers")}{btn("Read the FAQ", "/faq/", "ghost")}</div>
    </div>
  </div>
</div></section>

<section class="section bg-shell reveal" id="library"><div class="container">
  {section_head("The library", "Filter by what you are trying to figure out. New videos are added as I tour and as builders release phases and incentives.", "Full-length videos")}
  <div class="chip-row video-filter" role="group" aria-label="Filter videos">{chips}</div>
  <div class="grid grid-3">{long_cards}</div>
</div></section>

<section class="section reveal" id="shorts"><div class="container">
  {section_head("Sixty-second answers", "Quick hits on fees, incentives, contracts and relocation. Tap any one to play.", "Shorts")}
  <div class="grid grid-4">{short_cards}</div>
</div></section>

<section class="section section--sm reveal"><div class="container">{cta_band(
    title="Want a tour with someone who used to run this community?",
    text="I will walk SeaFlower with you, model by model, and tell you what the on-site reps cannot: which lots are worth the premium, which incentives are real, and what to negotiate.")}</div></section>
"""
    schema = [breadcrumb_schema([("Home", "/"), ("Videos", "/videos/")]),
              {"@type": "ItemList", "name": "SeaFlower and new-construction videos by Trenton Miller",
               "itemListElement": [{"@type": "ListItem", "position": i + 1, "item": video_schema(v)} for i, v in enumerate(VIDEOS[:12])]}]
    return [dict(
        path="/videos/", title="SeaFlower Videos: Builder Tours, Community Q&A and Buying Tips",
        description="Watch Trenton Miller's SeaFlower Bradenton videos: every builder toured, the community leadership interviewed, plus short answers on HOA and CDD fees, incentives, contracts and relocating to Florida's Gulf Coast.",
        body=body, schema=schema, priority="0.8", changefreq="weekly",
        og_image=f"https://i.ytimg.com/vi/{featured['id']}/maxresdefault.jpg",
    )]

from ..config import SITE
from ..components import *  # noqa
from ..content.testimonials import TESTIMONIALS
from ..content.videos import by_id
from ..html import esc, md

STORY = """
## Seven years on the builder side

I grew up in Buffalo, New York, which explains the phone number and the enthusiasm for January in Florida. I spent seven years working for the biggest names in new construction on the Gulf Coast: six in sales and one in operations.

On the sales side I was a top producer with Pulte and Del Webb, closing more than $150 million in new-home sales and earning the Tampa Bay Builders Association Salesperson of the Year award. I sat at the sales-center desk you sit across from. I wrote the contracts, ran the incentives, priced the lots, and watched what happened to buyers who walked in without anyone in their corner.

Then I moved to operations as an Operations Manager with David Weekley Homes. One of my jobs was the final quality-control walk on every home before it was handed to a buyer. For a stretch, I oversaw the SeaFlower community itself for David Weekley: the lots, the models, the trades, the handoffs. I know what a good SeaFlower build looks like because signing off on them was my job.

## Why I switched sides

The on-site sales consultant is paid by the builder, works for the builder, and is measured on the builder's numbers. That is not a criticism. It is just the job, and I did it well. But it means the person explaining the contract to you is not the person negotiating for you.

I left to become that person. Found Your Florida is my buyer-representation practice, built entirely on new construction. I only represent buyers. I never list homes for builders. The builder still pays my commission, exactly as they budget for on every sale, so representation does not raise your price by a dollar.

## How I work with SeaFlower buyers

- **Before you tour.** Builders track who brought you. If you walk into a model unrepresented, some builders will not let an agent join later. A five-minute call before your first visit protects your options.
- **Choosing a builder and lot.** I walk SeaFlower every few weeks. I know which builder fits which budget and lifestyle, which lots carry premiums that hold value, and what is planned behind that "preserve" view.
- **Negotiating.** Incentives are a starting point, not a menu. I know what each builder's division can move on and when (fiscal quarter-ends matter more than anyone admits).
- **During the build.** I attend pre-construction, pre-drywall and final walkthroughs, and I bring an independent inspector. Problems get fixed while the builder still has to fix them.
- **Out of state?** Most of my clients are. I do video walkthroughs of the lot and the build, and I coordinate remote closings.

## What I am not

I am not affiliated with SeaFlower, its developer, or any builder in the community. Nobody pays me to recommend them. If SeaFlower is not the right fit for you, I will tell you, and I will point you to a community that is. I am a licensed Florida sales associate with LPT Realty, LLC, and I hold an MBA. Real estate is a licensed profession; the details are in the footer.
"""


def pages():
    meet = by_id("GFtGiJU5sB0")
    body = f"""
<section class="page-hero"><div class="container">
  {breadcrumb([("Home", "/"), ("About Trenton", None)])}
  <div class="split">
    <div>
      {eyebrow("About Trenton Miller, MBA")}
      <h1>I sold homes for the builder. <em style="font-style:italic;color:var(--coral-700)">Now I make sure the builder treats you right.</em></h1>
      <p class="lead">Former Pulte top producer and David Weekley operations manager who briefly oversaw SeaFlower. Now an independent buyer&rsquo;s agent for new construction on Florida&rsquo;s Gulf Coast.</p>
      <div class="btn-row mt-3">{btn("Book a free strategy call", SITE['booking_page'], "coral", icon_name="calendar", cta="about-book")}{btn("Text " + SITE['phone_display'], "sms:" + SITE['phone_e164'], "ghost", icon_name="message")}</div>
    </div>
    <div>
      <div class="card" style="padding:14px;background:linear-gradient(160deg,#fff,var(--sand))"><img src="/assets/images/trenton-miller-800.jpg" alt="Trenton Miller, buyer's agent and founder of Found Your Florida" width="800" height="800" style="border-radius:12px" loading="eager" fetchpriority="high"></div>
    </div>
  </div>
</div></section>

<section class="section section--flush-top reveal"><div class="container">
  <div class="stats">
    {stat("7", "years on the builder side", "Pulte, Del Webb and David Weekley")}
    {stat("$150M", "in new-home sales", "as a builder top producer", small="+")}
    {stat("300", "clients helped", "most relocating from out of state", small="+")}
    {stat("#1", "Salesperson of the Year", "Tampa Bay Builders Association")}
  </div>
</div></section>

<section class="section reveal"><div class="container">
  <div class="grid grid-sidebar">
    <div class="prose">{md(STORY)}</div>
    <aside>
      {toc([("seven-years-on-the-builder-side", "Seven years on the builder side"), ("why-i-switched-sides", "Why I switched sides"), ("how-i-work-with-seaflower-buyers", "How I work with buyers"), ("what-i-am-not", "What I am not")])}
      {sidebar_cta()}
    </aside>
  </div>
</div></section>

<section class="section bg-shell reveal"><div class="container">
  <div class="split">
    <div>{lite_yt(meet['id'], meet['title'], meet['duration'])}</div>
    <div>{eyebrow("Three minutes")}<h2 style="font-size:clamp(28px,3.4vw,42px)">Why I left the builder side</h2><p class="lead">The short version, on camera. Then go watch the SeaFlower tour and decide for yourself whether I know the community.</p>{btn("Watch the SeaFlower videos", "/videos/", "primary", icon_name="video")}</div>
  </div>
</div></section>

<section class="section reveal"><div class="container">
  {section_head("What clients say", "Quoted as written. More on Google and Zillow.", "Reviews", center=True)}
  <div class="testimonials">{"".join(testimonial(q, w, l) for q, w, l in TESTIMONIALS)}</div>
</div></section>

<section class="section section--sm reveal"><div class="container">{cta_band(eyebrow_text="Let&rsquo;s talk SeaFlower")}</div></section>
"""
    schema = [breadcrumb_schema([("Home", "/"), ("About Trenton", "/about/")]),
              {"@type": "AboutPage", "@id": SITE["domain"] + "/about/#page", "url": SITE["domain"] + "/about/", "name": "About Trenton Miller", "mainEntity": {"@id": SITE["domain"] + "/#trenton"}}]
    return [dict(
        path="/about/", title="About Trenton Miller: Former Builder Insider, SeaFlower Buyer's Agent",
        description="Trenton Miller spent seven years on the builder side, six in sales with Pulte and Del Webb and one in operations with David Weekley Homes, where he briefly oversaw SeaFlower. Now he represents buyers only.",
        body=body, schema=schema, priority="0.6", changefreq="monthly", og_image="/assets/images/og-about.jpg",
    )]

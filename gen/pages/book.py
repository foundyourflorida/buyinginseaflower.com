from ..config import SITE
from ..components import *  # noqa
from ..content.testimonials import TESTIMONIALS
from ..html import esc


def pages():
    cal_url = SITE["booking_url"] + "?hide_gdpr_banner=1&background_color=fffcf6&text_color=1b2420&primary_color=1e5540"
    body = f"""
<section class="page-hero"><div class="container">
  {breadcrumb([("Home", "/"), ("Book a call", None)])}
  {eyebrow("Free strategy call")}
  <h1>Buying in SeaFlower? <em style="font-style:italic;color:var(--coral-700)">Talk to someone who ran it.</em></h1>
  <p class="lead">A free, no-pressure call with a former Pulte top producer and David Weekley operations manager who briefly oversaw SeaFlower. Pick a time below. I&rsquo;ll send a confirmation and one quick prep question by email.</p>
</div></section>

<section class="section section--flush-top"><div class="container">
  <div class="grid grid-sidebar">
    <div class="form-card" style="padding:10px">
      <div class="calendly-inline-widget" data-url="{esc(cal_url)}" style="min-width:300px;height:780px" aria-label="Scheduling calendar"></div>
      <noscript><p style="padding:20px">Calendar needs JavaScript. Book directly at <a href="{SITE['booking_url']}">{SITE['booking_url']}</a> or text {SITE['phone_display']}.</p></noscript>
    </div>
    <aside>
      <div class="card">
        <h3 style="font-size:22px">What we&rsquo;ll cover</h3>
        <ol style="padding-left:1.2em;color:var(--text);font-size:15.5px">
          <li><strong>Where you are.</strong> Touring, under contract, or a year out, and what is actually negotiable from here.</li>
          <li><strong>Which builder and lot.</strong> Given your budget, timeline and how you plan to live in the home.</li>
          <li><strong>Whether working together makes sense.</strong> If it doesn&rsquo;t, I&rsquo;ll point you to someone who fits better.</li>
        </ol>
        <p class="note" style="margin:0">No pitch. No drip campaign unless you ask for one.</p>
      </div>
      <div class="card mt-2">
        <h3 style="font-size:22px">Not ready for a call?</h3>
        <p>Text me your situation and I&rsquo;ll send back a two-minute video answer.</p>
        {btn("Text " + SITE['phone_display'], "sms:" + SITE['phone_e164'], "ghost", icon_name="message", cta="book-text")}
        <p class="note" style="margin:14px 0 0">Or email <a href="mailto:{SITE['email']}">{SITE['email']}</a></p>
      </div>
    </aside>
  </div>
</div></section>

<section class="section bg-shell reveal"><div class="container">
  {section_head("Why buyers bring me in", "Builder-paid representation costs you nothing extra. What you get is someone who has sat on the other side of the table.", "Read this before you sign anything")}
  <div class="compare">
    <div class="card"><h4>{icon('hammer')} On the deal</h4><ul>
      <li>Seven years inside Pulte and David Weekley, over $150M in new-home sales.</li>
      <li>I know what builders will move on (closing costs, rate buydowns, lot premiums, design-center credits) and what they won&rsquo;t.</li>
      <li>I read the fine print: escalation clauses, deposit terms, completion windows, appraisal gaps.</li></ul></div>
    <div class="card"><h4>{icon('shield')} On the build</h4><ul>
      <li>As Operations Manager at David Weekley, I did final quality-control walks before homes were delivered.</li>
      <li>I know what to flag at framing, pre-drywall and final walkthrough, and I bring an independent inspector.</li>
      <li>Most buyers find problems after closing. Mine find them while the builder still has to fix them.</li></ul></div>
  </div>
</div></section>

<section class="section reveal"><div class="container">
  {section_head("What buyers have said", eyebrow_text="Reviews", center=True)}
  <div class="testimonials">{"".join(testimonial(q, w, l) for q, w, l in TESTIMONIALS[:3])}</div>
</div></section>
"""
    return [dict(
        path="/book/", title="Book a Free SeaFlower Buyer Strategy Call with Trenton Miller",
        description="Schedule a free, no-pressure call with Trenton Miller, a former Pulte top producer and David Weekley operations manager who briefly oversaw SeaFlower. Get straight answers on builders, lots, incentives and contracts.",
        body=body, schema=[breadcrumb_schema([("Home", "/"), ("Book a call", "/book/")])], priority="0.9", changefreq="monthly",
        extra_body='<script src="https://assets.calendly.com/assets/external/widget.js" async></script>',
    )]

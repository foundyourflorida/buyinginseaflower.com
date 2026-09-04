from ..config import SITE
from ..components import *  # noqa
from ..content.videos import by_id


def pages():
    thanks = f"""
<section class="page-hero"><div class="container container--narrow center">
  {eyebrow("Message received", plain=True)}
  <h1>Thanks. I read every one of these myself.</h1>
  <p class="lead">You&rsquo;ll hear from me personally, usually within a few hours during the day. If it&rsquo;s urgent, text me at <a href="sms:{SITE['phone_e164']}">{SITE['phone_display']}</a>.</p>
</div></section>
<section class="section section--flush-top"><div class="container container--narrow">
  <div class="grid grid-2">
    {card("Skip the wait", "Grab a time on my calendar and we&rsquo;ll talk SeaFlower builders, lots and incentives.", SITE['booking_page'], "calendar", link_label="Book a call")}
    {card("Watch the full tour", "One hour, every builder, the amenities and my honest verdict.", "/videos/", "video", link_label="Go to videos")}
  </div>
  <div class="mt-4">{lite_yt("kCjttf-puQQ", by_id("kCjttf-puQQ")["title"], by_id("kCjttf-puQQ")["duration"])}</div>
</div></section>
"""
    notfound = f"""
<section class="page-hero"><div class="container container--narrow center">
  {eyebrow("404", plain=True)}
  <h1>That page moved, or never existed.</h1>
  <p class="lead">Try one of these instead, or text me at <a href="sms:{SITE['phone_e164']}">{SITE['phone_display']}</a> and I&rsquo;ll point you the right way.</p>
  <div class="btn-row mt-3" style="justify-content:center">{btn("Home", "/", "primary")}{btn("Buyer FAQ", "/faq/", "ghost")}{btn("Builders", "/builders/", "ghost")}{btn("Videos", "/videos/", "ghost")}</div>
</div></section>
"""
    return [
        dict(path="/thank-you/", title="Thanks, I'll be in touch", description="Your message is on its way to Trenton Miller.", body=thanks, noindex=True),
        dict(path="/404/", file="404.html", title="Page not found", description="Page not found.", body=notfound, noindex=True, nav="/"),
    ]

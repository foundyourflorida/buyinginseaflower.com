"""Page shell: <head> with SEO/OG/JSON-LD, header, footer, mobile bar, scripts."""
import json
from .config import SITE, NAV, FOOTER_EXPLORE, FOOTER_BUILDERS, LEGAL
from .components import flower_mark, icon, btn, eho_svg
from .html import esc

VERSION = "dev"  # replaced by build.py with a content hash for cache busting

FONTS = "https://fonts.googleapis.com/css2?family=Newsreader:ital,opsz,wght@0,6..72,400..600;1,6..72,400..600&family=Inter:wght@400;500;600;700&display=swap"


def abs_url(path):
    if path.startswith("http"):
        return path
    return SITE["domain"] + path


def base_graph():
    d = SITE["domain"]
    same_as = [SITE["youtube_channel"], SITE["instagram"], SITE["facebook"], SITE["linkedin"], SITE["brand_url"]]
    website = {
        "@type": "WebSite", "@id": d + "/#website", "url": d + "/", "name": SITE["name"],
        "description": SITE["description"], "inLanguage": "en-US", "publisher": {"@id": d + "/#org"},
    }
    org = {
        "@type": "RealEstateAgent", "@id": d + "/#org", "name": "Found Your Florida", "alternateName": "Buying in SeaFlower",
        "url": d + "/", "logo": abs_url(SITE["logo"]), "image": abs_url(SITE["headshot"]),
        "telephone": SITE["phone_e164"], "email": SITE["email"], "priceRange": "Free buyer representation",
        "description": "Independent new-construction buyer representation for SeaFlower and Florida's Gulf Coast, led by former builder insider Trenton Miller.",
        "areaServed": [{"@type": "City", "name": "Bradenton"}, {"@type": "City", "name": "Sarasota"}, {"@type": "Place", "name": "Lakewood Ranch"}, {"@type": "City", "name": "Parrish"}, {"@type": "AdministrativeArea", "name": "Manatee County, Florida"}],
        "founder": {"@id": d + "/#trenton"}, "employee": {"@id": d + "/#trenton"},
        "parentOrganization": {"@type": "Organization", "name": SITE["brokerage"], "telephone": SITE["brokerage_phone"],
                                "address": {"@type": "PostalAddress", "streetAddress": "400 S International Parkway, Suite 1020", "addressLocality": "Lake Mary", "addressRegion": "FL", "postalCode": "32746", "addressCountry": "US"}},
        "sameAs": same_as,
        "knowsAbout": ["SeaFlower Bradenton FL", "New construction homes", "David Weekley Homes", "M/I Homes", "Pulte Homes", "Cardel Homes", "Issa Homes", "Builder incentives", "CDD and HOA fees"],
    }
    person = {
        "@type": "Person", "@id": d + "/#trenton", "name": "Trenton Miller", "honorificSuffix": "MBA",
        "jobTitle": "Real estate buyer's agent, new construction specialist", "url": d + "/about/", "image": abs_url(SITE["headshot"]),
        "telephone": SITE["phone_e164"], "email": SITE["email"], "worksFor": {"@type": "Organization", "name": SITE["brokerage"]},
        "memberOf": {"@id": d + "/#org"},
        "alumniOf": [{"@type": "Organization", "name": "PulteGroup"}, {"@type": "Organization", "name": "David Weekley Homes"}],
        "award": "Tampa Bay Builders Association Salesperson of the Year",
        "hasCredential": {"@type": "EducationalOccupationalCredential", "credentialCategory": "license", "name": "Florida Real Estate Sales Associate SL3627498"},
        "knowsAbout": ["SeaFlower Bradenton", "New construction home buying", "Home builder sales and operations", "Florida Gulf Coast relocation"],
        "sameAs": same_as,
    }
    return [website, org, person]


def head(p):
    title = p["title"] if p.get("title_full") else f'{p["title"]} | {SITE["name"]}'
    desc = p.get("description", SITE["description"])
    url = abs_url(p["path"])
    og_image = abs_url(p.get("og_image") or SITE["og_default"])
    robots = "noindex, nofollow" if p.get("noindex") else "index, follow, max-image-preview:large, max-snippet:-1, max-video-preview:-1"
    graph = base_graph() + list(p.get("schema", []))
    jsonld = json.dumps({"@context": "https://schema.org", "@graph": graph}, ensure_ascii=False, separators=(",", ":"))
    ga = ""
    if SITE.get("ga_id"):
        ga = (f'<script async src="https://www.googletagmanager.com/gtag/js?id={SITE["ga_id"]}"></script>'
              f'<script>window.dataLayer=window.dataLayer||[];function gtag(){{dataLayer.push(arguments)}}gtag("js",new Date());gtag("config","{SITE["ga_id"]}",{{anonymize_ip:true}});</script>')
    article_meta = ""
    if p.get("type") == "article":
        article_meta = (f'<meta property="article:published_time" content="{esc(p.get("published", SITE["updated_iso"]))}">'
                        f'<meta property="article:modified_time" content="{esc(p.get("modified", SITE["updated_iso"]))}">'
                        f'<meta property="article:author" content="{SITE["agent"]}">')
    return f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{esc(title)}</title>
<meta name="description" content="{esc(desc)}">
<link rel="canonical" href="{esc(url)}">
<meta name="robots" content="{robots}">
<meta name="author" content="{SITE['agent']}">
<meta name="theme-color" content="#FAF0DE">
{('<meta name="google-site-verification" content="' + esc(SITE['google_site_verification']) + '">') if SITE.get('google_site_verification') else ''}
{('<meta name="msvalidate.01" content="' + esc(SITE['bing_site_verification']) + '">') if SITE.get('bing_site_verification') else ''}
<link rel="alternate" type="text/plain" title="llms.txt" href="/llms.txt">
<meta property="og:type" content="{'article' if p.get('type') == 'article' else 'website'}">
<meta property="og:site_name" content="{esc(SITE['name'])}">
<meta property="og:locale" content="{SITE['locale']}">
<meta property="og:url" content="{esc(url)}">
<meta property="og:title" content="{esc(p.get('og_title') or title)}">
<meta property="og:description" content="{esc(desc)}">
<meta property="og:image" content="{esc(og_image)}">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
{article_meta}
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="{esc(p.get('og_title') or title)}">
<meta name="twitter:description" content="{esc(desc)}">
<meta name="twitter:image" content="{esc(og_image)}">
<link rel="icon" href="/favicon.svg" type="image/svg+xml">
<link rel="icon" href="/favicon.ico" sizes="32x32">
<link rel="apple-touch-icon" href="/apple-touch-icon.png">
<link rel="manifest" href="/site.webmanifest">
<link rel="alternate" type="application/rss+xml" title="{esc(SITE['name'])} blog" href="/feed.xml">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="preconnect" href="https://i.ytimg.com">
<link rel="stylesheet" href="{FONTS}">
<link rel="stylesheet" href="/assets/css/main.css?v={VERSION}">
<script type="application/ld+json">{jsonld}</script>
{ga}
{p.get('extra_head', '')}
</head>"""


def header(current):
    links = "".join(
        f'<a href="{esc(h)}"{" aria-current=page" if current and current.startswith(h) else ""}>{esc(l)}</a>' for l, h in NAV
    )
    drawer_links = "".join(f'<a class="nav-link" href="{esc(h)}">{esc(l)}</a>' for l, h in NAV) + '<a class="nav-link" href="/location/">Location</a><a class="nav-link" href="/buyers-guide/">Free Buyer&rsquo;s Guide</a>'
    return f"""<a class="skip-link" href="#main">Skip to content</a>
<header class="header">
  <div class="topbar"><div class="container topbar__inner"><span>{SITE['agent_credentials']} · Licensed sales associate, {SITE['brokerage']}</span><span><a href="tel:{SITE['phone_e164']}">{SITE['phone_display']}</a> · <a href="mailto:{SITE['email']}">{SITE['email']}</a> · <a href="/location/">Location</a> · <a href="/buyers-guide/">Free guide</a></span></div></div>
  <div class="container header__inner">
    <a class="brand" href="/" aria-label="{esc(SITE['name'])} home">{flower_mark(40)}<span class="brand__text"><span class="brand__name">Buying in <em>SeaFlower</em></span><span class="brand__sub">A Found Your Florida guide</span></span></a>
    <nav class="nav" aria-label="Primary">{links}</nav>
    <div class="header__cta">
      {btn("Book a call", SITE['booking_page'], "coral", "sm", "calendar", cta="header-book")}
      <button class="nav-toggle" type="button" aria-label="Open menu" aria-expanded="false" aria-controls="drawer">{icon("list")}</button>
    </div>
  </div>
</header>
<div class="drawer" id="drawer" aria-hidden="true">
  <div class="drawer__scrim"></div>
  <div class="drawer__panel" role="dialog" aria-modal="true" aria-label="Menu">
    <button class="drawer__close" type="button" aria-label="Close menu">&times;</button>
    {drawer_links}
    {btn("Book a free strategy call", SITE['booking_page'], "coral", icon_name="calendar", cta="drawer-book")}
    {btn("Text " + SITE['phone_display'], "sms:" + SITE['phone_e164'], "ghost", icon_name="message", cta="drawer-text")}
    <p class="drawer__contact">{SITE['agent_credentials']} · Licensed sales associate, {SITE['brokerage']}<br><a href="mailto:{SITE['email']}">{SITE['email']}</a> · <a href="tel:{SITE['phone_e164']}">{SITE['phone_display']}</a></p>
  </div>
</div>"""


def footer():
    explore = "".join(f'<li><a href="{esc(h)}">{esc(l)}</a></li>' for l, h in FOOTER_EXPLORE)
    builders = "".join(f'<li><a href="{esc(h)}">{esc(l)}</a></li>' for l, h in FOOTER_BUILDERS)
    return f"""<footer class="footer">
  <div class="container">
    <div class="footer__grid">
      <div class="footer__brand">
        <a class="brand" href="/">{flower_mark(40)}<span class="brand__text"><span class="brand__name">Buying in <em>SeaFlower</em></span><span class="brand__sub">A Found Your Florida guide</span></span></a>
        <p>An independent, buyer-side guide to SeaFlower in Bradenton, Florida, written by a former builder insider who now represents buyers only.</p>
        <a href="{SITE['brand_url']}" target="_blank" rel="me noopener"><img class="footer__logo" src="{SITE['logo']}" alt="Found Your Florida Real Estate" width="150" height="80" loading="lazy"></a>
      </div>
      <div><h4>Explore</h4><ul>{explore}</ul></div>
      <div><h4>Builders</h4><ul>{builders}</ul></div>
      <div>
        <h4>Talk to Trenton</h4>
        <ul>
          <li><a href="tel:{SITE['phone_e164']}">{icon('phone', size=14)} &nbsp;Call {SITE['phone_display']}</a></li>
          <li><a href="sms:{SITE['phone_e164']}">{icon('message', size=14)} &nbsp;Text {SITE['phone_display']}</a></li>
          <li><a href="mailto:{SITE['email']}">{icon('mail', size=14)} &nbsp;{SITE['email']}</a></li>
          <li><a href="{SITE['booking_page']}">{icon('calendar', size=14)} &nbsp;Book a free strategy call</a></li>
          <li><a href="{SITE['youtube_channel']}" target="_blank" rel="noopener">{icon('video', size=14)} &nbsp;YouTube @foundyourflorida</a></li>
          <li><a href="{SITE['instagram']}" target="_blank" rel="noopener">Instagram</a> · <a href="{SITE['facebook']}" target="_blank" rel="noopener">Facebook</a> · <a href="{SITE['linkedin']}" target="_blank" rel="noopener">LinkedIn</a></li>
        </ul>
      </div>
    </div>
    <div class="footer__legal">
      <p>{LEGAL['brokerage_line']}</p>
      <p>{LEGAL['not_affiliated']}</p>
      <p>{LEGAL['accuracy']}</p>
      <div class="footer__eho">{eho_svg()}<span>{LEGAL['fair_housing']}</span></div>
      <div class="footer__bottom">
        <span>&copy; <span data-year>2026</span> Trenton Miller, Found Your Florida. All rights reserved.</span>
        <span><a href="/privacy/">Privacy &amp; SMS terms</a> · <a href="/terms/">Terms</a> · <a href="/accessibility/">Accessibility</a> · <a href="/sitemap.xml">Sitemap</a> · <a href="/llms.txt">llms.txt</a></span>
      </div>
    </div>
  </div>
</footer>
<div class="mobile-bar" aria-label="Quick contact">
  <span class="mobile-bar__label">{SITE['agent']} · {SITE['brokerage']}</span>
  <a href="tel:{SITE['phone_e164']}">{icon('phone')} Call</a>
  <a href="sms:{SITE['phone_e164']}">{icon('message')} Text</a>
  <a class="is-primary" href="{SITE['booking_page']}" data-cta="mobile-bar-book">{icon('calendar')} Book a call</a>
</div>"""


def render_page(p):
    cfg = json.dumps({"formEndpoint": SITE.get("form_endpoint", ""), "email": SITE["email"], "phoneDisplay": SITE["phone_display"], "bookingUrl": SITE["booking_url"]})
    return (head(p) + f'\n<body class="{esc(p.get("body_class", ""))}">\n' + header(p.get("nav") or p["path"]) +
            f'\n<main id="main">\n{p["body"]}\n</main>\n' + footer() +
            f'\n<script>window.SITE_CONFIG={cfg};</script>\n<script src="/assets/js/main.js?v={VERSION}" defer></script>\n{p.get("extra_body", "")}\n</body>\n</html>\n')

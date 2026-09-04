from ..config import SITE
from ..components import *  # noqa
from ..content import facts as F
from ..content.faqs import CATEGORIES, FAQS, all_pairs
from ..html import esc


def pages():
    pairs = all_pairs()
    chips = '<a href="#" class="chip is-active" data-faq-filter="all" role="button" aria-pressed="true">All</a>' + "".join(
        f'<a href="#" class="chip" data-faq-filter="{c}" role="button" aria-pressed="false">{esc(t)}</a>' for c, t, i in CATEGORIES)
    groups = "".join(faq_group(t, FAQS[c], c, intro=i) for c, t, i in CATEGORIES)
    n = len(pairs)
    intro = (f"<strong>{n} questions buyers ask about SeaFlower in Bradenton, answered.</strong> Public facts are sourced to the developer, the builders, the Lake Flores CDD, "
             "Manatee County and FEMA as of " + F.AS_OF + ". Answers marked as insider perspective are mine, from seven years on the builder side and time overseeing this "
             "community for David Weekley. Search, or filter by topic.")
    body = f"""
<section class="page-hero"><div class="container">
  {breadcrumb([("Home", "/"), ("FAQ", None)])}
  {eyebrow("Buyer FAQ")}
  <h1>Every question buyers ask about SeaFlower, <em style="font-style:italic;color:var(--coral-700)">answered straight</em></h1>
  {speakable(intro)}
  <div class="page-hero__meta">{updated_badge()}<span id="faq-count">{n} questions</span></div>
  {independent_note()}
</div></section>

<section class="section section--flush-top"><div class="container"><div class="grid grid-sidebar">
  <div>
    <div class="faq-tools">
      <div class="faq-search">{icon('search')}<label class="visually-hidden" for="faq-search">Search questions</label><input id="faq-search" type="search" placeholder="Search: CDD, flood zone, golf cart, Pulte, deposit…" autocomplete="off"></div>
    </div>
    <div class="chip-row" style="margin-bottom:26px" role="group" aria-label="Filter by topic">{chips}</div>
    {groups}
    <div class="faq-empty" id="faq-empty">Nothing matched. Try a different word, or <a href="sms:{SITE['phone_e164']}">text me the question</a> and I will answer it and add it here.</div>
    <div class="mt-5">{lead_form("faq-ask", "Ask a question I have not answered yet", "If it is not on this page, it should be. Send it and I will reply personally and add it to the list.", submit="Ask Trenton", interest="SeaFlower FAQ question", message_label="Your question")}</div>
  </div>
  <aside>{toc([("faq-" + c, t) for c, t, i in CATEGORIES], "Topics")}{sidebar_cta("Rather just talk it through?", "Fifteen minutes on the phone usually answers a week of research.", "Book a free call")}</aside>
</div></div></section>

<section class="section section--sm reveal"><div class="container">{cta_band()}</div></section>
"""
    schema = [breadcrumb_schema([("Home", "/"), ("FAQ", "/faq/")]), faq_schema([(q, a) for c, q, a, t in pairs]),
              {"@type": "WebPage", "@id": SITE["domain"] + "/faq/#page", "url": SITE["domain"] + "/faq/", "name": "SeaFlower buyer FAQ", "about": {"@id": SITE["domain"] + "/#seaflower"}, "dateModified": F.AS_OF_ISO, "speakable": {"@type": "SpeakableSpecification", "cssSelector": [".speakable"]}}]
    return [dict(
        path="/faq/", title=f"SeaFlower Bradenton FAQ: {n} Buyer Questions on HOA, CDD, Builders, Flood Zone and More",
        description=f"{n} straight answers about buying in SeaFlower, Bradenton: HOA and CDD fees, builders and prices, flood zone and evacuation level, golf carts, ADUs and rentals, schools, incentives, deposits and contracts. Sourced and dated, with insider perspective from a former builder operations manager.",
        body=body, schema=schema, priority="0.9", changefreq="weekly",
    )]

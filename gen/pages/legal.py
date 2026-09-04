from ..config import SITE, LEGAL
from ..components import *  # noqa
from ..html import md

PRIVACY = f"""
Effective {SITE['updated']}. This policy covers buyinginseaflower.com, published by Trenton Miller, Found Your Florida (LPT Realty, LLC).

## What we collect

- **Information you send us.** When you submit a form, book a call, or text or email me, I receive what you provide: typically your name, email, phone number, timeline and message. Forms note the page you were on and, if present, the marketing campaign that brought you (UTM parameters).
- **Analytics.** The site uses Google Analytics 4 with IP anonymization to understand which pages help people. It sets cookies and records device, browser, approximate location and pages viewed. Google's use of this data is described in its privacy policy.
- **Embedded services.** Videos are embedded from YouTube in privacy-enhanced mode (youtube-nocookie.com), which does not set tracking cookies until you press play. The booking page loads Calendly, which has its own privacy policy. If you book, Calendly collects the details you enter.

## How we use it

- To answer your questions and follow up about your home search, including by phone, text and email.
- To keep notes about your search in a customer-relationship system so I do not ask you the same questions twice.
- To send occasional market updates if you opt in. Every email has an unsubscribe link, and you can reply STOP to any text message.
- To improve the site.

I do not sell your personal information. I share it only with services needed to run this site and my practice (for example, email, scheduling, CRM and analytics providers) and with my brokerage as required for real estate transactions.

## Text messages

By providing a phone number and ticking the consent box, you agree to receive calls and texts from Trenton Miller / Found Your Florida (LPT Realty, LLC) about your home search, which may be sent using automated technology. Consent is not a condition of purchase. Message frequency varies. Message and data rates may apply. Reply STOP to opt out or HELP for help. Mobile information will not be shared with third parties for marketing purposes.

## Cookies and your choices

You can block cookies in your browser and the site will still work. You can request a copy of the information I hold about you, ask me to correct it, or ask me to delete it by emailing [{SITE['email']}](mailto:{SITE['email']}).

## Children

This site is not directed to children under 13 and I do not knowingly collect their information.

## Changes

If this policy changes, the effective date at the top will change with it. Questions: [{SITE['email']}](mailto:{SITE['email']}) or {SITE['phone_display']}.
"""

TERMS = f"""
Effective {SITE['updated']}.

## Informational only

buyinginseaflower.com is an independent resource for people considering a home in SeaFlower, Bradenton, Florida. Content reflects public information from developers, builders and government sources, plus the professional opinions of Trenton Miller. It is not legal, tax, lending or engineering advice. Confirm every figure with the builder, developer, county or your own advisors before relying on it.

## Not affiliated

{LEGAL['not_affiliated']}

## Accuracy

{LEGAL['accuracy']}

## No agency relationship by browsing

Reading this site, submitting a form or having a call does not create a client relationship. Buyer representation begins only when we sign a written agreement. Until then, no duty of representation is owed.

## Brokerage

{LEGAL['brokerage_line']}

## Fair Housing

{LEGAL['fair_housing']} Descriptions of communities and homes are about the property, not about who should live there.

## Intellectual property

Text, page design and original graphics on this site are © Trenton Miller. Videos are © Found Your Florida and embedded from YouTube under YouTube's terms. Third-party names, logos and marks belong to their owners. You may quote short excerpts with a link back; please do not republish pages wholesale.

## Links

Links to builder, developer, county and news sites are provided for convenience. I do not control them and am not responsible for their content.

## Limitation of liability

To the fullest extent permitted by Florida law, this site is provided as is, and I am not liable for decisions made in reliance on it.

## Governing law

These terms are governed by the laws of the State of Florida. Questions: [{SITE['email']}](mailto:{SITE['email']}).
"""


def legal_page(path, title, desc, body_md, crumb):
    body = f"""
<section class="page-hero"><div class="container container--narrow">{breadcrumb([("Home", "/"), (crumb, None)])}<h1>{title}</h1></div></section>
<section class="section section--flush-top"><div class="container container--narrow"><div class="prose">{md(body_md)}</div></div></section>
"""
    return dict(path=path, title=title, description=desc, body=body, priority="0.2", changefreq="yearly", nav="/",
                schema=[breadcrumb_schema([("Home", "/"), (crumb, path)])])


ACCESS = LEGAL["accessibility"] + """

## What we have done

- Semantic headings, landmarks and a skip link on every page.
- Keyboard-operable menus, accordions, filters, sortable tables and video players, with visible focus states.
- Text alternatives for images and a schematic map with a written description.
- Color contrast checked against WCAG 2.1 AA for body text and buttons.
- Videos are hosted on YouTube with captions available through the player.
- No pop-ups that block the page, and no third-party overlay widgets.

## Tell us

If something does not work with your screen reader, magnifier or keyboard, email """ + SITE["email"] + " or call " + SITE["phone_display"] + ". We will fix it and, in the meantime, get you the information another way."


def pages():
    return [
        legal_page("/accessibility/", "Accessibility", "Accessibility statement for buyinginseaflower.com and how to request information in another format.", ACCESS, "Accessibility"),
        legal_page("/privacy/", "Privacy Policy", "How buyinginseaflower.com collects and uses information, including text-message consent and your choices.", PRIVACY, "Privacy"),
        legal_page("/terms/", "Terms of Use", "Terms of use for buyinginseaflower.com: informational content, no affiliation with SeaFlower or builders, Fair Housing, and brokerage disclosures.", TERMS, "Terms"),
    ]

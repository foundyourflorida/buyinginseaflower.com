"""Site-wide configuration. Edit this file to change contact details, links, or legal text."""

SITE = {
    "name": "Buying in SeaFlower",
    "short_name": "Buying in SeaFlower",
    "domain": "https://buyinginseaflower.com",
    "tagline": "The independent buyer's guide to SeaFlower in Bradenton, Florida",
    "description": (
        "Everything buyers ask about SeaFlower in Bradenton, FL: builders, floor plans, pricing, HOA and CDD fees, "
        "location, schools, flood zones and the buying process, from a former builder insider who represents buyers."
    ),
    "locale": "en_US",
    "brand": "Found Your Florida",
    "brand_url": "https://foundyourflorida.com",
    "agent": "Trenton Miller",
    "agent_credentials": "Trenton Miller, MBA",
    "agent_title": "Buyer's agent and former builder insider",
    "phone_display": "716-949-5557",
    "phone_e164": "+17169495557",
    "email": "trenton@foundyourflorida.com",
    "booking_url": "https://calendly.com/trenton-foundyourflorida/30min",
    "booking_page": "/book/",
    # Lead form endpoint. Formspree/Basin-style JSON POST endpoint. If empty or still a placeholder,
    # forms fall back to opening a pre-filled email so no lead is ever lost.
    "form_endpoint": "https://formsubmit.co/ajax/trenton@foundyourflorida.com",
    "ga_id": "G-CEZJP71SJH",
    "ads_id": "AW-18430676225",
    # Optional search-engine verification tokens (Search Console can also verify via the GA4 tag, so these may stay empty).
    "google_site_verification": "",
    "bing_site_verification": "",
    "brokerage": "LPT Realty, LLC",
    "license": "SL3627498",
    "brokerage_office": "400 S International Parkway, Suite 1020, Lake Mary, FL 32746",
    "brokerage_phone": "(877) 366-2213",
    "brokerage_license": "CQ1064576",
    "broker_of_record": "Natalie Cox (BK3378992)",
    "service_area": "Bradenton, Sarasota, Lakewood Ranch, Parrish and Florida's Gulf Coast",
    "youtube_channel": "https://www.youtube.com/@foundyourflorida",
    "youtube_channel_id": "UCeNTSsfvSZy-RNOluPRvWNg",
    "instagram": "https://www.instagram.com/foundyourflorida",
    "facebook": "https://www.facebook.com/foundyourflorida",
    "linkedin": "https://www.linkedin.com/in/trenton-miller/",
    "headshot": "/assets/images/trenton-miller.jpg",
    "logo": "/assets/images/found-your-florida-logo.png",
    "og_default": "/assets/images/og-default.jpg",
    "updated": "September 3, 2026",
    "updated_iso": "2026-09-03",
    "geo": {"lat": 27.4589, "lng": -82.6210},
}

# Header navigation (label, path). Keep to eight items so it fits on one line at 1180px.
NAV = [
    ("Community", "/community/"),
    ("Builders", "/builders/"),
    ("Homes & Prices", "/homes/"),
    ("Costs", "/costs/"),
    ("FAQ", "/faq/"),
    ("Videos", "/videos/"),
    ("Blog", "/blog/"),
    ("About", "/about/"),
]

FOOTER_EXPLORE = [
    ("SeaFlower community", "/community/"),
    ("Location & area guide", "/location/"),
    ("Homes & pricing", "/homes/"),
    ("Costs, HOA & CDD fees", "/costs/"),
    ("Buyer FAQ", "/faq/"),
    ("Video library", "/videos/"),
    ("Blog", "/blog/"),
    ("Free SeaFlower Buyer's Guide", "/buyers-guide/"),
]

FOOTER_BUILDERS = [
    ("All builders compared", "/builders/"),
    ("David Weekley Homes", "/builders/david-weekley-homes/"),
    ("M/I Homes", "/builders/mi-homes/"),
    ("Pulte Homes", "/builders/pulte-homes/"),
    ("Cardel Homes", "/builders/cardel-homes/"),
    ("Issa Homes", "/builders/issa-homes/"),
]

LEGAL = {
    "fair_housing": (
        "Equal Housing Opportunity. Trenton Miller and LPT Realty, LLC are pledged to the letter and spirit of U.S. policy for the achievement "
        "of equal housing opportunity throughout the Nation. We encourage and support an affirmative advertising and marketing program in which "
        "there are no barriers to obtaining housing because of race, color, religion, sex, handicap, familial status, or national origin. "
        "Every home and community described on this site is available to all persons on an equal-opportunity basis."
    ),
    "not_affiliated": (
        "Independent site. Information on this website is provided by Trenton Miller of Found Your Florida, a licensed Florida real estate sales "
        "associate with LPT Realty, LLC. This is not the official website of the SeaFlower\u00ae community. We are not associated with or affiliated "
        "with the SeaFlower\u00ae community or its developer, and the developer has not prepared or approved this website. The developer's official "
        "website is www.SeaFlower.com. We are likewise not affiliated with, sponsored by or endorsed by Cortez75W Investors, LLC, Lake Flores Land "
        "Company, LAMB Properties, or any builder in the community, including David Weekley Homes, M/I Homes, Pulte Homes, Cardel Homes and Issa Homes. "
        "Trenton Miller was previously employed by David Weekley Homes and PulteGroup and is no longer associated with either company. All trademarks "
        "and service marks related to the SeaFlower\u00ae community are owned by the developer and its affiliates; builder and product names are "
        "trademarks of their respective owners and are used here only to identify the community and its builders."
    ),
    "accuracy": (
        "Information disclaimer. Prices, floor plans, square footages, lot sizes, availability, incentives, HOA and CDD assessments, taxes, amenities, "
        "school assignments and completion dates are provided by builders, the developer and public sources. They are believed reliable but are not "
        "guaranteed, change without notice, may contain errors, and must be verified directly with the builder, developer or county before you rely "
        "on them. Prices shown are base prices as of the date noted on each page and exclude lot premiums, options, upgrades, closing costs and fees. "
        "Nothing on this site is an offer to sell or a solicitation of an offer to buy real property; offers can be made only through a builder's or "
        "seller's written purchase agreement. Buyer representation is by written agreement; broker compensation is not set by law and is fully negotiable."
    ),
    "brokerage_line": (
        "Trenton Miller is a licensed Florida real estate sales associate (SL3627498) with LPT Realty, LLC, "
        "400 S International Parkway, Suite 1020, Lake Mary, FL 32746, (877) 366-2213, office license CQ1064576, "
        "broker of record Natalie Cox (BK3378992). Found Your Florida is a marketing name used by Trenton Miller; all brokerage services are provided "
        "by LPT Realty, LLC. Contact: trenton@foundyourflorida.com, 716-949-5557, LPT Realty, LLC."
    ),
    "consent": (
        "Yes, text and call me. By checking this box and providing my phone number, I give my express written consent for Trenton Miller / Found Your "
        "Florida, on behalf of LPT Realty, LLC, to call and send text messages to that number about SeaFlower, new-construction homes and real estate in "
        "the Bradenton area, including messages sent using an automated system for the selection and dialing of telephone numbers or a prerecorded voice. "
        "Consent is not a condition of purchasing any property, goods or services. Message frequency varies; message and data rates may apply. Reply STOP "
        "to opt out or HELP for help at any time. My mobile number and SMS consent will not be shared with or sold to third parties for their marketing."
    ),
    "accessibility": (
        "Buying in SeaFlower is committed to making this site usable by everyone, including people who use assistive technology. We aim to conform to "
        "the Web Content Accessibility Guidelines (WCAG) 2.1 Level AA and test the site on an ongoing basis. Videos are captioned on YouTube, images "
        "include text descriptions, and all forms and menus can be operated by keyboard. If you have difficulty using any part of this site or need "
        "information in an alternative format, email trenton@foundyourflorida.com or call 716-949-5557 and we will provide it promptly."
    ),
}

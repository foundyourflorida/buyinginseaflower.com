from ..config import SITE
from ..components import *  # noqa
from ..content import facts as F
from ..content.videos import by_id
from ..html import esc, md

DISTANCES = [
    ("Bradenton Beach (Anna Maria Island)", "8 min · ~5 mi"), ("Coquina Beach", "12 min"), ("Cortez fishing village and Bridge Street", "10 min"),
    ("HCA Florida Blake Hospital", "8 min"), ("Manatee County Golf Course", "5 min"), ("IMG Academy Golf Club", "8 min"), ("Robinson Preserve", "14 min"),
    ("LECOM Park (Pirates spring training)", "15 min"), ("Bradenton Riverwalk / downtown", "16 min · ~6 mi"), ("Manatee Memorial Hospital", "16 min"),
    ("Longboat Key", "18 min"), ("Sarasota-Bradenton Intl. Airport (SRQ)", "18 min · ~8 mi"), ("Ringling Museum", "18 min"), ("Anna Maria Bayfront Park", "24 min"),
    ("Selby Gardens / Van Wezel (downtown Sarasota)", "24 min · ~13 mi"), ("UTC mall / Lakewood Ranch Main Street", "26 min"), ("St. Armands Circle", "28 min"),
    ("Mote Marine", "30 min"), ("St. Pete-Clearwater Airport (PIE)", "55 min"), ("Tampa International Airport (TPA)", "65 min · ~37 mi"),
]

MAP_SVG = """
<svg viewBox="0 0 760 520" role="img" aria-labelledby="map-title map-desc" xmlns="http://www.w3.org/2000/svg">
  <title id="map-title">Schematic map of SeaFlower and the surrounding area</title>
  <desc id="map-desc">SeaFlower sits south of Cortez Road and west of 75th Street West in west Bradenton, about three miles east of Anna Maria Island across the Cortez bridge, with Sarasota Bay to the south-west, IMG Academy to the east and Sarasota-Bradenton airport to the south-east.</desc>
  <defs><pattern id="water" width="10" height="10" patternUnits="userSpaceOnUse"><path d="M0 5 q2.5 -3 5 0 t5 0" fill="none" stroke="#6FAFA6" stroke-width="1" opacity=".5"/></pattern></defs>
  <rect width="760" height="520" fill="#FFFCF6"/>
  <path d="M0 0 H150 Q170 120 120 220 Q80 330 140 440 Q160 500 130 520 H0 Z" fill="#E1EFEB"/>
  <path d="M0 0 H150 Q170 120 120 220 Q80 330 140 440 Q160 500 130 520 H0 Z" fill="url(#water)"/>
  <text x="34" y="300" font-family="Inter, system-ui, sans-serif" font-size="13" fill="#4F8F86" transform="rotate(-80 34 300)">Gulf of Mexico</text>
  <path d="M60 40 Q90 60 82 140 Q74 230 96 320 Q104 380 88 440" fill="none" stroke="#F1E3CB" stroke-width="22" stroke-linecap="round"/>
  <text x="46" y="150" font-family="Inter, system-ui, sans-serif" font-size="11" fill="#5F6D66" transform="rotate(-82 46 150)">Anna Maria Island</text>
  <path d="M200 330 Q300 300 420 360 Q520 420 640 380 Q720 350 760 380 V520 H200 Z" fill="#E1EFEB"/>
  <path d="M200 330 Q300 300 420 360 Q520 420 640 380 Q720 350 760 380 V520 H200 Z" fill="url(#water)"/>
  <text x="380" y="470" font-family="Inter, system-ui, sans-serif" font-size="13" fill="#4F8F86">Sarasota Bay</text>
  <path d="M96 230 H760" stroke="#D3C2A0" stroke-width="6" stroke-linecap="round"/>
  <text x="600" y="220" font-family="Inter, system-ui, sans-serif" font-size="12" fill="#5F6D66">Cortez Rd W (SR 684)</text>
  <path d="M96 230 Q120 236 150 232" stroke="#B94D3C" stroke-width="6" stroke-dasharray="6 5" fill="none"/>
  <text x="104" y="256" font-family="Inter, system-ui, sans-serif" font-size="10" fill="#B94D3C">Cortez bridge</text>
  <path d="M470 60 V400" stroke="#D3C2A0" stroke-width="5" stroke-linecap="round"/>
  <text x="478" y="80" font-family="Inter, system-ui, sans-serif" font-size="12" fill="#5F6D66">75th St W</text>
  <path d="M330 230 V330" stroke="#D3C2A0" stroke-width="4" stroke-linecap="round"/>
  <text x="270" y="345" font-family="Inter, system-ui, sans-serif" font-size="11" fill="#5F6D66">86th St W</text>
  <path d="M330 340 Q400 336 470 340" stroke="#D3C2A0" stroke-width="4" fill="none"/>
  <text x="352" y="362" font-family="Inter, system-ui, sans-serif" font-size="11" fill="#5F6D66">El Conquistador Pkwy</text>
  <path d="M610 60 V400" stroke="#D3C2A0" stroke-width="4" stroke-linecap="round"/>
  <text x="618" y="80" font-family="Inter, system-ui, sans-serif" font-size="12" fill="#5F6D66">34th St W</text>
  <path d="M330 232 H470 V340 Q400 336 330 340 Z" fill="#DCE9E1" stroke="#1E5540" stroke-width="2.5"/>
  <circle cx="400" cy="290" r="14" fill="#E1EFEB" stroke="#6FAFA6"/>
  <text x="352" y="262" font-family="Fraunces, Georgia, serif" font-size="20" font-weight="600" fill="#0F2E24">SeaFlower</text>
  <text x="364" y="322" font-family="Inter, system-ui, sans-serif" font-size="10" fill="#1E5540">Lake Flores</text>
  <rect x="452" y="238" width="16" height="12" fill="#E8796B"/>
  <text x="424" y="226" font-family="Inter, system-ui, sans-serif" font-size="10" fill="#B94D3C">Village Center</text>
  <rect x="478" y="250" width="120" height="80" rx="6" fill="#F1E3CB"/>
  <text x="498" y="296" font-family="Inter, system-ui, sans-serif" font-size="12" fill="#5F6D66">IMG Academy</text>
  <circle cx="690" cy="470" r="7" fill="#1E5540"/>
  <text x="636" y="496" font-family="Inter, system-ui, sans-serif" font-size="11" fill="#1E5540">SRQ airport</text>
  <circle cx="640" cy="110" r="7" fill="#1E5540"/>
  <text x="600" y="98" font-family="Inter, system-ui, sans-serif" font-size="11" fill="#1E5540">Downtown Bradenton</text>
  <circle cx="90" cy="230" r="6" fill="#B94D3C"/>
  <text x="26" y="212" font-family="Inter, system-ui, sans-serif" font-size="11" fill="#B94D3C">Bradenton Beach</text>
  <path d="M120 232 Q220 210 330 232" fill="none" stroke="#B94D3C" stroke-width="1.5" stroke-dasharray="4 4"/>
  <text x="180" y="204" font-family="Inter, system-ui, sans-serif" font-size="11" fill="#B94D3C">~3.2 miles to the beach</text>
  <path d="M700 40 l0 -20 M700 20 l-6 8 M700 20 l6 8" stroke="#5F6D66" stroke-width="1.5" fill="none"/><text x="708" y="34" font-family="Inter, system-ui, sans-serif" font-size="10" fill="#5F6D66">N</text>
</svg>
"""

AREA_MD = """
## What west Bradenton is, and is not

West Bradenton is the older, established side of Manatee County: the Cortez fishing village and its restaurants at the foot of the bridge, the causeway to Anna Maria Island, Palma Sola Bay, the Robinson Preserve trails, IMG Academy, spring-training baseball at LECOM Park and a downtown Riverwalk on the Manatee River. It is not the manicured, everything-new landscape of Lakewood Ranch, and until SeaFlower it had almost no new construction. That contrast is most of why SeaFlower is selling: new homes on the beach side of the county.

## Beaches and the honest traffic note

The developer's site plan measures 3.2 miles to the beach and every builder quotes a short drive: Bradenton Beach in about 8 minutes, Coquina Beach in 12, Longboat Key in 18. All true, off-peak. Cortez Road is the only bridge road to Anna Maria Island, and in season, mid-February through mid-April with March the worst, beach traffic backs up. Locals go before 10 a.m. or after 1:30 p.m. The Cortez bridge replacement is a pending state project, which will help eventually and hurt during construction.

:::trent
I timed it for the community video: on a weekday morning it is a ten-minute drive to the sand, and on a Saturday in March it is not. If a beach commute is your daily routine, drive it at the worst time before you buy, then decide. Most buyers here go early, stay late, and come home on the trail.
:::

## Schools

Manatee County assigns schools by address, and the builders do not agree on the middle school, so confirm the zone with the district locator before you rely on it.

| School | Grades | Address | Listed by |
|---|---|---|---|
| Sea Breeze Elementary | PK–5 | 3601 71st St W | every builder |
| W. D. Sugg Middle | 6–8 | 5602 38th Ave W | Pulte, Cardel |
| Electa Lee Magnet Middle | 6–8 | 4000 53rd Ave W | David Weekley |
| Bayshore High | 9–12 | 5401 34th St W | every builder |

Third-party ratings for these schools are modest (GreatSchools scored Sea Breeze 4 of 10 and the middle and high schools 2 of 10 in September 2026). Manatee County offers school choice and magnet programs, and the private options within a short drive are strong: IMG Academy next door, Bradenton Christian, Saint Stephen's Episcopal, St. Joseph Catholic and Cardinal Mooney. This is the question I get most from relocating buyers with school-age children, and the honest answer is that most of them choose a magnet, charter or private school.

## Healthcare

HCA Florida Blake Hospital is about eight minutes away. Manatee Memorial is about sixteen, Sarasota Memorial about twenty-five, and Tampa General and Moffitt roughly an hour and ten. Dental and urgent care are among the announced Village Center tenants.

## Shopping and dining

Until the Village Center opens, everyday retail is on Cortez Road and Manatee Avenue West, including the nearest Publix. The Village Center brings a Publix and Publix Liquors, Dutch Bros, Whataburger, Playa Bowls, Potbelly, Dave's Hot Chicken and a dozen more announced tenants, targeted for late 2026. For a night out, Cortez and Bridge Street are ten minutes, downtown Bradenton sixteen, downtown Sarasota and St. Armands about half an hour.

## Getting around

Sarasota-Bradenton International (SRQ) is about 18 minutes and serves most of the country nonstop in season. Tampa International is about 65 minutes and St. Pete-Clearwater about 55. Inside the community, the 2.5-mile Lake Flores Trail connects the neighborhoods to The Garden Club and the Village Center for walkers, cyclists and golf carts; internal streets are public county roads.

## Flood zone, evacuation level and elevation

Three separate things, often confused. The FEMA flood zone determines whether a lender requires flood insurance: FEMA's flood hazard layer shows the interior of SeaFlower as Zone X, minimal hazard, with coastal AE and VE zones west of 86th Street toward Palma Sola Bay and small Zone A pockets near 75th Street. The county evacuation level (A through E) determines who is told to leave ahead of a surge event, and is looked up by address on Manatee County's Learn Your Level map. Elevation is on the elevation certificate for a finished home. Ask for all three for your specific lot; a community-wide answer is not good enough.

## Property taxes and insurance

SeaFlower is in the Cedar Hammock Fire Control District tax district of unincorporated Manatee County, which adopted a total rate of 14.61 mills for 2025. Homeowner's insurance on new construction benefits from the wind-mitigation credits Florida requires insurers to give for current-code homes. The full math, with worked examples, is on the <a href="/costs/">costs and fees page</a>.
"""

FAQ = [
    ("How far is SeaFlower from Anna Maria Island?", "About 3.2 miles to the beach per the developer's site plan, roughly 8 minutes to Bradenton Beach and 7.2 road miles to Anna Maria Island per builder drive times, off-peak. In season, Cortez Road beach traffic can stretch that considerably."),
    ("What schools are zoned for SeaFlower?", "Sea Breeze Elementary and Bayshore High per every builder. The middle school is listed as W.D. Sugg by Pulte and Cardel and as Electa Lee Magnet Middle by David Weekley; confirm with the Manatee County School District locator."),
    ("Is SeaFlower in a flood zone?", "FEMA's flood hazard layer shows the interior of the site as Zone X, minimal flood hazard, with coastal AE and VE zones west of 86th Street and small Zone A pockets near the 75th Street edge. Confirm your specific lot on the county flood map."),
    ("How far is SeaFlower from the airport?", "Sarasota-Bradenton International (SRQ) is about 18 minutes and 8 miles. Tampa International is about 65 minutes and 37 miles; St. Pete-Clearwater about 55 minutes."),
    ("Which hospital is closest to SeaFlower?", "HCA Florida Blake Hospital, about 8 minutes away. Manatee Memorial is about 16 minutes and Sarasota Memorial about 25."),
]


def pages():
    short = by_id("XMQCzXI7Sow")
    intro = ("<strong>SeaFlower is in west Bradenton, Florida 34210, on the coastal mainland of Manatee County, about 3.2 miles from the beach at Anna Maria Island.</strong> "
             "It sits south of Cortez Road West and west of 75th Street West, 8 miles from Sarasota-Bradenton airport, 13 miles from downtown Sarasota and 37 miles from Tampa International. "
             "IMG Academy is next door. FEMA maps the interior of the site as Zone X. Zoned schools are Sea Breeze Elementary, W.D. Sugg or Electa Lee Middle, and Bayshore High.")
    toc_items = [("map", "Map and drive times"), ("what-west-bradenton-is-and-is-not", "West Bradenton"), ("beaches-and-the-honest-traffic-note", "Beaches and traffic"), ("schools", "Schools"), ("healthcare", "Healthcare"), ("shopping-and-dining", "Shopping and dining"), ("getting-around", "Getting around"), ("flood-zone-evacuation-level-and-elevation", "Flood zone and evacuation"), ("property-taxes-and-insurance", "Taxes and insurance")]
    body = f"""
<section class="page-hero"><div class="container">
  {breadcrumb([("Home", "/"), ("Location", None)])}
  {eyebrow("Location and the area")}
  <h1>Where SeaFlower is, <em style="font-style:italic;color:var(--coral-700)">and what is around it</em></h1>
  {speakable(intro)}
  <div class="page-hero__meta">{updated_badge()}<span>Drive times as published by the builders, off-peak</span></div>
  {independent_note()}
  {photo_banner("aerial-lake-flores", "Looking west over Lake Flores toward Anna Maria Island and the Gulf (rendering courtesy of the developer)", cls="photo-banner--tall")}
</div></section>

<section class="section section--flush-top reveal" id="map"><div class="container">
  <div class="grid grid-2" style="align-items:start">
    <figure class="map-figure" style="margin:0">{MAP_SVG}<figcaption>Schematic, not to scale. SeaFlower occupies the land between 86th Street West, 75th Street West, Cortez Road and El Conquistador Parkway.</figcaption></figure>
    <div>
      <h2 style="font-size:clamp(26px,3vw,36px)">Drive times from SeaFlower</h2>
      {dist_list(DISTANCES)}
      <p class="note" style="margin-top:10px">{esc(F.DRIVE_TIMES_SOURCE)} Airport and city distances from M/I Homes and Cardel. Add time in season.</p>
    </div>
  </div>
</div></section>

<section class="section reveal"><div class="container"><div class="grid grid-sidebar">
  <div>
    <div class="prose">{md(AREA_MD)}</div>
    <div class="mt-4">{lite_yt(short['id'], short['title'], short['duration'])}</div>
    <h2 style="margin-top:2em">Location questions</h2>
    {"".join(faq_item(q, a, "location") for q, a in FAQ)}
    {sources_list([
        ("Cardel Homes SeaFlower page (drive times)", "https://www.cardelhomes.com/florida/seaflower/", "Sep 3, 2026"),
        ("M/I Homes SeaFlower page (distances)", "https://www.mihomes.com/new-homes/florida/sarasota-metro/bradenton/seaflower", "Sep 3, 2026"),
        ("SeaFlower Phase One site plan (3.2 miles to beach)", "https://seaflower.com/wp-content/uploads/SeaFlower-Phase1-Sitemap_040826.pdf", "Apr 2026"),
        ("SeaFlower location page", "https://seaflower.com/location/", "Sep 3, 2026"),
        ("FEMA National Flood Hazard Layer (panel 12081C0284F)", "https://msc.fema.gov/portal/home", "Sep 3, 2026"),
        ("Manatee County floodplain management and flood map", "https://www.mymanatee.org/departments/building___development_services/floodplain_management", "Sep 3, 2026"),
        ("Manatee County evacuation levels (Learn Your Level)", "https://www.mymanatee.org/departments/public_safety/emergency_management/evacuation_levels", "Sep 3, 2026"),
        ("Manatee County 2025 adopted millage rates", "https://www.manateepao.gov/data/Tax_Roll_Data/Millages/2025%20Final%20Adopted%20Millage%20Rates.pdf", "2025"),
        ("Manatee County School District school locator", "https://www.manateeschools.net/", "Sep 3, 2026"),
        ("GreatSchools profiles: Sea Breeze, Sugg, Electa Lee, Bayshore", "https://www.greatschools.org/florida/bradenton/", "Sep 3, 2026"),
    ])}
  </div>
  <aside>{toc(toc_items)}{sidebar_cta("Want to see it in person?", "I will drive you the beach route, the airport route and the school route, then walk the community.", "Plan a visit with me")}</aside>
</div></div></section>

<section class="section section--sm reveal"><div class="container">{cta_band(title="Relocating from out of state?", text="Most of my clients are. I do the drive-time reality check, the flood and evacuation lookups, and the video walkthroughs so you can decide from home.")}</div></section>
"""
    schema = [breadcrumb_schema([("Home", "/"), ("Location", "/location/")]), faq_schema(FAQ),
              {"@type": "WebPage", "@id": SITE["domain"] + "/location/#page", "url": SITE["domain"] + "/location/", "name": "SeaFlower location and area guide", "about": {"@id": SITE["domain"] + "/#seaflower"}, "dateModified": F.AS_OF_ISO, "speakable": {"@type": "SpeakableSpecification", "cssSelector": [".speakable"]}}]
    return [dict(
        path="/location/", title="SeaFlower Location: Distance to Anna Maria Island, Schools, Airports, Flood Zone and Drive Times",
        description="SeaFlower is in west Bradenton 34210, 3.2 miles from the beach, 18 minutes from SRQ and 65 from Tampa. Drive times to beaches, hospitals and shopping, zoned schools (Sea Breeze, Sugg or Electa Lee, Bayshore), the FEMA flood zone, evacuation levels and the honest Cortez Road traffic note.",
        body=body, schema=schema, priority="0.8", changefreq="monthly",
    )]

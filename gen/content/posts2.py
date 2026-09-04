"""Second batch of blog posts (Sept 4, 2026). Same format as posts.py."""
from . import facts as F
from .builders_index import by_slug

DATE = "2026-09-04"
DATE_DISPLAY = "September 4, 2026"


def payment(price, rate=0.065, down=0.20):
    loan = price * (1 - down); r = rate / 12
    return loan * r / (1 - (1 + r) ** -360)


def money(x):
    return "${:,.0f}".format(x)


def plans_table(slug, collection_filter=None):
    b = by_slug(slug); out = ""
    for c in b["collections"]:
        if collection_filter and collection_filter not in c["name"]:
            continue
        rows = "".join(f"<tr><td><b>{p['name']}</b></td><td class=num>{p['price'] if p['price'].strip().startswith('$') else 'On request'}</td><td class=num>{p['sqft'].split(' A/C')[0].split('(')[0].strip()}</td><td>{p['beds']}</td><td>{p['baths']}</td><td>{p['garage']}</td></tr>" for p in c["plans"])
        out += f'<h3>{c["name"]} · {c.get("lot_width", "")} · {c.get("price_phrase", "")}</h3><div class="table-wrap"><table><thead><tr><th>Plan</th><th class=num>Base price</th><th class=num>Sq ft</th><th>Beds</th><th>Baths</th><th>Garage</th></tr></thead><tbody>{rows}</tbody></table></div>'
    return out


def monthly_rows():
    rows = ""
    for label, price, hoa, cdd, ins in [("M/I townhome (Row Home), Phase N1", 410000, 308.43, 1473.49, 2200), ("David Weekley Bungalow, 45' lot, Phase 1B2", 486000, 300.88, 2091.63, 3200), ("Cardel Classic, 60' lot, Phase 1C", 700000, 300.88, 4604.78, 4000)]:
        pi = payment(price); tax = (price - 50000) * F.TAXES["millage"] / 1000 / 12
        rows += f"<tr><td>{label}</td><td class=num>{money(price)}</td><td class=num>{money(pi)}</td><td class=num>{money(tax)}</td><td class=num>{money(hoa)}</td><td class=num>{money(cdd/12)}</td><td class=num>{money(ins/12)}</td><td class=num><b>{money(pi+tax+hoa+cdd/12+ins/12)}</b></td></tr>"
    return f'<div class="table-wrap"><table><thead><tr><th>Home</th><th class=num>Price</th><th class=num>P&amp;I</th><th class=num>Taxes</th><th class=num>HOA</th><th class=num>CDD</th><th class=num>Insurance</th><th class=num>Total / mo</th></tr></thead><tbody>{rows}</tbody></table></div>'


def lot_mix_table():
    rows = "".join(f"<tr><td>{ph}</td><td>{prod}</td><td class=num>{n}</td></tr>" for ph, prod, n, w in F.LOT_MIX)
    return f'<div class="table-wrap"><table><thead><tr><th>Phase</th><th>Product</th><th class=num>Homesites</th></tr></thead><tbody>{rows}</tbody></table></div>'


POSTS2 = [
    dict(slug="mi-homes-townhomes-villas-seaflower", category="Builders", title="M/I Homes at SeaFlower: townhomes and villas from $399,999, what's included and what to watch",
         excerpt="The only attached product in SeaFlower: 68 townhomes and 90 twin villas, five plans, a lock-and-leave HOA, and the biggest quick move-in inventory in the community.",
         video="kCjttf-puQQ", body=f"""
## Quick answer

M/I Homes builds SeaFlower's only townhomes and villas: 68 Row Homes (townhomes, 3 bedrooms, 2.5 baths) and 90 Village Homes (twin villas, 2 bedrooms, 2 baths) in Phase N1, priced from $399,999 as of September 2026, 1,486 to 2,406 square feet, with rear-load detached two-car garages. It is the entry price into the community and the product built for lock-and-leave owners.

## What M/I builds here

{plans_table("mi-homes")}

Both series are attached, single-level or two-level, with the garage off the alley behind the home. Townhome and villa owners pay a slightly higher HOA than single-family owners, $308.43 and $327.70 a month respectively against $300.88, because the fee also covers exterior maintenance, insurance and reserves on the shared structures. That is the whole point of the product: nothing to mow, paint or roof.

## Where the model and sales center are

M/I's sales center is at 8015 SeaFlower Parkway. Showcase homes for the Topaz villa and Bay Harbor townhome opened with the community's public model grand opening on March 7, 2026.

## Inventory and incentives

On September 3, 2026, M/I listed 21 quick move-in homes, the most of any SeaFlower builder: townhomes from $399,999 to $659,352 and villas from $429,999 to $464,999, many with a "was" price shown. M/I also advertised a 4.875% FHA 30-year rate (5.644% APR) through M/I Financial on select inventory. A "was" price is inventory pressure, and inventory pressure is leverage.

## Warranty and programs

M/I publishes a 10-year transferable structural warranty and one-year customer care coverage. M/I Financial is the affiliated lender; you are not required to use it, but the advertised rate offers depend on it.

:::trent
If your goal is a second home you can lock and leave for three months, this is the SeaFlower product I show first, and September is the month I show it, because M/I clears inventory before its fiscal quarter closes. Verify which specific homes carry the FHA rate offer; it is not every listing, and the APR is the number that matters.
:::

Sources: M/I Homes SeaFlower community page and quick move-in listings (Sep 3, 2026); SeaFlower HOA and CDD information sheet (Dec 8, 2025); seaflower.com model grand opening post (Mar 2026).
"""),
    dict(slug="pulte-homes-seaflower-series-explained", category="Builders", title="Pulte Homes at SeaFlower: Scenic, Veranda, Front Porch and Distinctive series explained",
         excerpt="Thirteen plans from $404,990 to $641,990, which series has the ADU option, how Pulte's incentives work, and what a former Pulte top producer would tell you.",
         video="kCjttf-puQQ", body=f"""
## Quick answer

Pulte sells four series of single-family homes in SeaFlower: Scenic (the value line, from $404,990), Veranda (porch-forward plans from $439,990), Front Porch (the Arbordale II and a Mabel II with an accessory dwelling unit, from $514,990) and Distinctive (the larger Coral, Prestige and Burbank plans, from $579,990). Thirteen plans, 1,405 to 2,369 square feet, front- or alley-loaded homesites, sales office at 7634 Addison Avenue.

## The four series

{plans_table("pulte-homes")}

## Where Pulte fits

Pulte is the lowest entry into a detached home in SeaFlower and the most process-driven builder in the community. The Scenic series is the plan people buy when the monthly number is the constraint. The Front Porch series is where the ADU lives: a Mabel II with a separate suite over the garage, which is the feature that makes SeaFlower different from most master plans. The Distinctive plans are the ones with the room counts for a full household.

## Inventory and incentives

Six quick move-ins were listed on September 3, 2026, all under construction with completion dates from October 2026 to January 2027, priced $568,895 to $756,090; three carried "$10,000 in savings" flags. Pulte's rate offers run through Pulte Mortgage's forward-commitment program; you are not required to finance with Pulte Mortgage, but the rate offers are only available if you do.

## Warranty

Pulte publishes a 10-year limited structural warranty that transfers to later owners within the period.

:::trent
I sold for Pulte for six years. The published "savings" on a quick move-in is a starting point; the last two weeks of a fiscal quarter and a division manager's signature are where the real numbers come from, and the request has to go through your agent. Run the Pulte Mortgage offer against an outside lender every time; sometimes the outside rate wins once fees are compared, and it always improves your position.
:::

Sources: Pulte SeaFlower community page, plan pages and quick move-in listings (Sep 3, 2026); Pulte 10-year warranty page; seaflower.com builder posts (2025–2026).
"""),
    dict(slug="cardel-homes-seaflower-all-19-plans", category="Builders", title="Cardel Homes at SeaFlower: all 19 plans, 50' vs 60' lots, garage suites and natural gas",
         excerpt="Cardel's Cottage and Classic collections in front-garage and rear-garage versions, base prices from $579,990, the garage-suite option, and what a full model tour showed me.",
         video="mpxbdiSlNuw", body=f"""
## Quick answer

Cardel Homes builds 19 single-family plans in SeaFlower across four sub-series: Cottage Homes on 50-foot lots (front-garage from $579,990, rear-garage from $589,990) and Classic Homes on 60-foot lots (front-garage from $667,990, rear-garage from $726,990), 1,909 to 3,122 square feet, with garage suites that add about 800 square feet on many plans, natural gas, and yard maintenance and internet inside the HOA. Sales center at 4521 Flower Fields Trail.

## Every plan

{plans_table("cardel-homes")}

## What makes Cardel different here

Cardel took the coastal-village brief most literally. Most plans come in a front-garage and a rear-garage version, so you can choose between a deeper back yard and a porch-forward street face. Garage suites, a separate apartment over the garage with its own entrance, are offered on many plans and are the reason Cardel's Bali showcase home became the community's ADU example. The community is served by TECO natural gas, and Cardel markets itself as a natural-gas builder.

## Process, timing and money

Cardel's own FAQ says a build takes 9 to 14 months from a fully signed contract, that buyers typically spend 10% to 20% of base price in the design center, that a $5,000 lot deposit plus a pre-approval reserves a homesite, and that no structural changes are accepted after contract. In September 2026 Cardel advertised up to $20,000 toward design options and listed two Coral quick move-ins on Merritt Avenue at $723,781 and $739,481, both completing that month. Cardel's Palma won Best Kitchen in its category at the 2026 Suncoast Parade of Homes.

:::trent
I walked every Cardel model on camera. Base prices start in the high $500,000s, but the homes people actually buy, with the lot, the suite and the finishes they fall for in the models, land between $700,000 and $1.2 million. Cardel negotiates in design dollars rather than rate buydowns, which suits cash buyers and anyone bringing their own lender. Get the construction schedule in writing; it is longer than the production builders'.
:::

Sources: Cardel Homes SeaFlower page, plan pages and FAQ (Sep 3, 2026); Suncoast Builders Association 2026 Parade of Homes winners; seaflower.com ADU post (Feb 5, 2026).
"""),
    dict(slug="issa-homes-estate-homes-seaflower", category="Builders", title="Issa Homes at SeaFlower: lakefront estate homes from $1.25 million, and what that price leaves out",
         excerpt="The Lakeshore and Preserve collections on 80-foot lots, the homesite premium that is only quoted on request, the Parade-winning Hemingway, and the two homes listed above $1.5 million.",
         video="kCjttf-puQQ", body=f"""
## Quick answer

Issa Homes builds SeaFlower's estate tier: semi-custom homes on 80-foot lakefront lots on Lake Flores, marketed "starting from $1,250,000, excluding homesite premium" (other Issa pages say $1.29 million and $1.3 million). Two collections, The Lakeshore (Addison, Preston, Kingston, Hemingway, Flagler) and The Preserve (Amelia, Hatteras, Key West, Palm Beach, Sanibel), about 2,905 to 3,755 square feet of air-conditioned space, more with the optional garage apartment. Per-plan base prices are not published.

## The collections

{plans_table("issa-homes")}

## The Hemingway

Issa's Hemingway showcase home won Best Overall in its category at the 2026 Suncoast Builders Association Parade of Homes. It is the model most buyers see first, and it sets expectations for finish level across the collection.

## What the price leaves out

"Starting from $1,250,000" excludes the homesite premium, and on an 80-foot lakefront lot the premium is significant and quoted only on request. It also excludes structural options, the garage apartment or casita, and design selections, which on a semi-custom home are a larger share of the final number than on a production home. The two quick move-ins listed on September 3, 2026, a Flagler at 7804 Lake Flores Avenue for $1,720,000 (ready by March 2027) and an Amelia at 7808 Lake Flores Avenue for $1,567,560 (ready by February 2027), show where finished homes actually land.

## Warranty and build

Issa publishes one year of materials and workmanship coverage, two years on roofing, plumbing, electrical and HVAC, and a ten-year structural warranty through RWC. Build times and the deposit and draw structure differ from the production builders; expect a longer schedule and a contract that deserves a review before you sign, not after.

:::trent
This is the one SeaFlower product where I bring a real estate attorney into the contract review as a matter of course. The homes are excellent and the lake lots are the best dirt in the community; the paperwork is a custom-build agreement, not a production contract, and the premium and option pricing deserve a line-by-line read.
:::

Sources: Issa Homes SeaFlower microsite and plan pages (Sep 3, 2026); Issa Homes press release on SeaFlower pricing (Mar 27, 2025); Suncoast Builders Association 2026 Parade of Homes winners; Issa warranty page.
"""),
    dict(slug="seaflower-schools-zoned", category="Location", title="Which schools are SeaFlower homes zoned for? Sea Breeze, Sugg or Electa Lee, and Bayshore",
         excerpt="What the builders list, where they disagree, the third-party ratings, the private and magnet options nearby, and how to confirm a specific address.",
         video="rU7t_DDvMkc", body="""
## Quick answer

Every SeaFlower builder lists Sea Breeze Elementary (3601 71st Street West) and Bayshore High (5401 34th Street West). The middle school is disputed: Pulte and Cardel list W. D. Sugg Middle (5602 38th Avenue West) while David Weekley lists Electa Lee Magnet Middle (4000 53rd Avenue West). Manatee County assigns schools by address, so confirm the zone for a specific lot with the district's school locator before you rely on any builder's page.

## The zoned schools

| School | Grades | Address | Listed by |
|---|---|---|---|
| Sea Breeze Elementary | PK–5 | 3601 71st St W | every builder |
| W. D. Sugg Middle | 6–8 | 5602 38th Ave W | Pulte, Cardel |
| Electa Lee Magnet Middle | 6–8 | 4000 53rd Ave W | David Weekley |
| Bayshore High | 9–12 | 5401 34th St W | every builder |

## What the ratings say

Third-party ratings for these schools are modest. In September 2026 GreatSchools scored Sea Breeze Elementary 4 of 10 and Sugg, Electa Lee and Bayshore 2 of 10. Ratings are one lens; visit the schools and talk to the district before deciding.

## The options most relocating buyers actually use

Manatee County offers school choice and magnet programs, and Electa Lee is itself a magnet middle school. Within a short drive are IMG Academy (next door to the community), Bradenton Christian School, Saint Stephen's Episcopal School, St. Joseph Catholic School and Cardinal Mooney Catholic High School. Most of my clients with school-age children choose a magnet, charter or private school rather than the default zone, and they decide before they pick a lot.

## How to confirm

Use the Manatee County School District school locator for the exact address, then call the school. If a builder's page and the locator disagree, the locator wins.

:::trent
Ask me about schools on the first call and I will tell you what the zone is, what the ratings say, and which private and magnet options families in the community are using. Then go tour two of them before you go under contract; nobody regrets that hour.
:::

Sources: David Weekley, Pulte and Cardel SeaFlower community pages (Sep 3, 2026); GreatSchools profiles (Sep 3, 2026); Manatee County School District; seaflower.com location page.
"""),
    dict(slug="golf-carts-at-seaflower", category="Community", title="Golf carts at SeaFlower: where you can drive, what Florida law allows, and getting to the beach",
         excerpt="The 2.5-mile multi-modal trail, the difference between a golf cart and a street-legal LSV, the rules on public streets, and the honest answer about Cortez Road.",
         video="rU7t_DDvMkc", body="""
## Quick answer

SeaFlower is designed around golf carts: the 2.5-mile, 16-foot-wide Lake Flores Trail connects the neighborhoods to The Garden Club and the Village Center and is built for walking, biking and carts, and streets are designed for 20 mph. On public roads, Florida Statute 316.212 allows golf carts only where the county has designated them, and a street-legal low-speed vehicle (LSV) with lights, signals, a windshield, a VIN and insurance is the safe answer for anything beyond the trail. Driving to Anna Maria Island means Cortez Road, a state highway; that is LSV territory at best, and traffic in season is real.

## Inside the community

The trail is the spine of the plan. It loops the 19-acre Lake Flores and Lake Flores Park, reaches the amenity campus, and runs to the Village Center where Publix opens in fall 2026. Rear-load lots put your garage on the alley, which is where most residents will park a cart.

## On the streets

SeaFlower's internal streets are being turned over to Manatee County as public roads. Florida law lets a county designate roads as safe for golf carts; until that designation is confirmed for these streets, treat a plain golf cart as a trail vehicle. Under state law, drivers under 18 need a learner's or driver license, adults need government photo ID, and carts without headlights, brake lights, turn signals and a windshield are restricted to daylight hours.

## Golf cart versus LSV

A golf cart is limited to about 20 mph and cannot be titled for the road. A low-speed vehicle is built or converted to travel 20 to 25 mph, carries a VIN, title, registration and insurance, and may be driven on roads posted 35 mph or less. A David Weekley buyer in the community described her street-legal cart and the insurance that comes with it in a public comment on my community video; that is the setup to copy if you want to leave the trail.

## The beach

Cortez Road to the island is a state road with a bridge, not a golf-cart route. Residents who ride to the beach do it on an LSV, early, and outside the mid-February-to-mid-April peak.

:::trent
Buy the cart after you close and after you have asked the HOA for the current rules in writing. The trail alone makes a cart worth having here; the street question is being settled as the county accepts roads.
:::

Sources: seaflower.com community pages; Bradenton Herald via Yahoo News (May 22, 2024); Florida Statute 316.212 and 316.2122; public comments on the SeaFlower leadership interview video (2026).
"""),
    dict(slug="adus-garage-apartments-seaflower", category="Community", title="ADUs and garage apartments at SeaFlower: which builders offer them, the rental rules, and the math",
         excerpt="Why every single-family lot here can have an accessory dwelling unit, what Cardel, Pulte, Issa and David Weekley offer, the one-year owner-occupancy rule, and how to think about rental income.",
         video="rU7t_DDvMkc", body="""
## Quick answer

SeaFlower received Manatee County zoning in 2015 that permits an accessory dwelling unit, a garage apartment or detached casita, on every single-family homesite, which is unusual for a new master plan. Cardel offers garage suites on many plans, Pulte's Front Porch series includes an ADU version of the Mabel II, Issa offers garage-apartment versions of the Flagler and Key West, and the Welcome Center itself is a Cardel home with an 800-square-foot ADU. To rent an ADU, the owner must occupy the main home for one year first, and leases must be six months or longer.

## Why it matters

An ADU changes what a lot can do: a private suite for a relative or guests, a home office with its own door, or a long-term rental that offsets the mortgage. Most communities in the region do not allow them at all; SeaFlower designed for them from the first plan.

## Who builds what

- **Cardel**: garage suites of roughly 800 square feet over the garage on many Cottage and Classic plans; the Bali showcase home is the community's ADU example.
- **Pulte**: the Mabel II in the Front Porch series is offered with an ADU on 50-foot lots.
- **Issa**: garage-apartment versions of the Flagler (Lakeshore) and Key West (Preserve) plans, plus casita options.
- **David Weekley**: the developer's materials describe an alley-loaded garage with an ADU option on the Classic collection; Weekley's own pages do not publish it, so confirm on site.

## The rules

Per WUSF's February 2026 reporting on the community: one year of owner occupancy in the primary home before the ADU can be rented, and a minimum six-month lease. A 2026 state bill proposed letting local governments allow shorter ADU rentals; check its status before you plan around short-term income. Whole-home leasing rules are in the HOA covenants.

## The math, honestly

A garage suite adds real cost; my Cardel tour put the option in the $150,000 to $200,000 range once finished. At a plausible long-term rent for a one-bedroom suite in west Bradenton, the payback is measured in years, not months. It pencils best for people who want the space anyway and treat the rent as a bonus, or who plan for a family member to live there.

:::trent
The buyers who are happiest with an ADU here bought it for a person, not a spreadsheet: a parent, an adult child, a caregiver, a visiting family that comes for a month. If you are buying it purely for rent, run the numbers with the option cost, the extra insurance and the one-year wait, and buy the smaller house if they do not work.
:::

Sources: WUSF (Feb 5, 2026); seaflower.com ADU and options posts (Dec 15, 2025; Feb 5, 2026); Cardel, Pulte and Issa plan pages (Sep 3, 2026).
"""),
    dict(slug="seaflower-site-plan-phases-explained", category="Community", title="SeaFlower site plan explained: phases N1, 1B1, 1B2 and 1C, lot widths, and where each product sits",
         excerpt="The 1,063 Phase One homesites by phase and product, why the phase matters for your CDD bill, how lots are released, and what Phase Two means.",
         video="kCjttf-puQQ", body=f"""
## Quick answer

Phase One of SeaFlower is 400 acres and 1,063 homesites around Lake Flores, split into four sub-phases: N1 (the M/I townhomes and twin villas), 1B1 and 1B2 (single-family lots from 42 to 80 feet wide on the 2023 bond series) and 1C (384 lots financed by the Series 2026 bonds). 784 of the 1,063 homesites had been released by April 2026. The phase your lot sits in sets your CDD assessment and tells you how finished the streets around you will be.

## The homesite mix

{lot_mix_table()}

Source: Lake Flores CDD assessment roll (FY2027 proposed budget).

## The product ladder

Row Homes (townhomes) and Village Homes (twin villas) are M/I's attached products in N1. Bungalow lots at 42 and 45 feet, rear-loaded, are built by Pulte and David Weekley. Cottage lots at 50 feet are Cardel and Pulte. Classic lots at 60 feet are Cardel and David Weekley. Estate lots at 80 feet, on the lake, are Issa Homes. Lot width, not builder, is the first decision; it decides which two or three builders you are really choosing between.

## Why phase matters

Phase 1B lots were financed by the 2023 bonds, much of which builders prepaid at lot closing, so their FY2027 assessments run roughly $1,750 to $3,409 a year by width. Phase 1C lots carry the new $20.9 million Series 2026 bonds and run roughly $3,335 to $4,605. Same width, different phase, different bill. Phase also tells you construction sequence: N1 and 1B have the first residents and finished streets; 1C is where the 2026 lot releases and the newest models are.

## Releases and Phase Two

Builders release lots in batches, and the premium lots in each release (lake, park, corner, quiet street) go first. Phase Two, the second of three roughly 400-acre phases, is expected to start around 2027 depending on market conditions.

:::trent
Ask two questions about any lot: which phase, and what backs up to it. The first sets your CDD for decades. The second is the difference between a preserve view and a future street. The developer's official site plan is the reference; I keep a marked-up copy with phase lines and release status for clients.
:::

Sources: SeaFlower Phase One site plan (April 2026); Lake Flores CDD FY2027 proposed budget and Series 2026 bond documents; seaflower.com expansion posts (Jan 28 and Apr 10, 2026); Business Observer (Oct 31, 2025).
"""),
    dict(slug="seaflower-vs-wellen-park-vs-parrish", category="Comparisons", title="SeaFlower vs Wellen Park vs Parrish: which Gulf Coast new-construction market fits you",
         excerpt="The three places I tour most with relocating buyers, compared on beach distance, price, stage of buildout, and who each one is really for.",
         video="OlP4BZUWXDI", body="""
## Quick answer

SeaFlower (west Bradenton) is the beach-side option: 3.2 miles to the sand, five builders, entry at $399,999 for attached homes and $404,990 for detached, amenities opening fall 2026. Wellen Park (Venice/North Port) is a large, established master plan with a built downtown and 727 new-home contracts in the first half of 2026, inland off I-75. Parrish (North River Ranch, Del Webb, Rye Ranch and others) is the value market northeast of Bradenton, with the lowest entry prices on the coast and a 30-to-45-minute drive to the nearest Gulf beach.

## Beach distance

This is the sorting question. SeaFlower is a short drive, or an LSV ride, to Anna Maria Island. Wellen Park's beaches are a drive down to Venice and Manasota Key. Parrish is inland; the beach is a day trip, not a routine.

## Price and product

SeaFlower runs from M/I townhomes at $399,999 through Cardel and David Weekley in the $500,000s and $600,000s to Issa estates above $1.25 million. Wellen Park spans a wide range across many builders and villages, with a large 55-plus component. Parrish has the lowest entry: Explore by Del Webb released pricing from $354,990 in May 2026, and Lennar and D.R. Horton communities start in the $300,000s.

## Stage of buildout

Wellen Park has a finished downtown, restaurants and years of built amenities. Parrish is mid-build with new communities opening every quarter and infrastructure catching up. SeaFlower is early: The Garden Club and the Village Center open in late 2026, and Phase Two is a 2027 story.

## Fees

All three carry district assessments plus HOA. SeaFlower's HOA is $300.88 a month including fiber and yard care, with a CDD of roughly $1,475 to $4,605 a year by lot. Wellen Park and Parrish communities vary widely by village and builder; the fair comparison is total recurring cost, run village by village.

## Who chooses which

Beach-in-your-week buyers choose SeaFlower. Buyers who want everything finished and a walkable downtown today choose Wellen Park. Buyers optimizing price per square foot, or looking at 55-plus product, choose Parrish.

:::trent
I sell in all three and I tour clients through two of them in a day whenever I can. My rule of thumb: decide how often you will really go to the beach, decide whether you can live with construction for a couple of years, and let those two answers pick the market before you fall in love with a model home.
:::

Sources: RCLCO mid-year 2026 rankings via Sarasota Magazine (Jul 31, 2026); builder pages for SeaFlower (Sep 3, 2026); Explore by Del Webb pricing release (May 2026); Lake Flores CDD FY2027 budget.
"""),
    dict(slug="seaflower-monthly-cost-three-budgets", category="Costs & fees", title="What a SeaFlower home costs per month at three budgets: $410K, $486K and $700K",
         excerpt="Three real product types with the builders' own prices and the district's own assessment tables, all the way down to a monthly number.",
         video="8E3fPi_pTcA", body=f"""
## Quick answer

At 20% down and a 6.5% 30-year rate, a $410,000 M/I townhome runs about {money(payment(410000) + (410000-50000)*F.TAXES['millage']/1000/12 + 308.43 + 1473.49/12 + 2200/12)} a month all-in, a $486,000 David Weekley Bungalow about {money(payment(486000) + (486000-50000)*F.TAXES['millage']/1000/12 + 300.88 + 2091.63/12 + 3200/12)}, and a $700,000 Cardel Classic in Phase 1C about {money(payment(700000) + (700000-50000)*F.TAXES['millage']/1000/12 + 300.88 + 4604.78/12 + 4000/12)}, including taxes at full value, HOA, the Lake Flores CDD and estimated insurance.

## The three examples

{monthly_rows()}

Assumptions: 20% down, 30-year fixed at 6.5% (builder buydowns are often lower), Manatee County taxes at {F.TAXES['millage']} mills on price less a $50,000 homestead exemption, CDD from the FY2027 proposed budget, insurance estimated.

## What moves the number

- **Rate.** A one-point builder buydown on the $486,000 example saves roughly $250 a month. That is why quick move-ins with lender incentives price so well.
- **Phase.** The Cardel example sits in Phase 1C on the Series 2026 bonds; the same lot width in Phase 1B2 would cut the CDD line by about $160 a month.
- **Product.** The townhome's HOA is $7.55 higher than single-family, but it includes exterior maintenance and insurance on the structure.
- **Taxes at full value.** The first-year bill on a new home is often land-only; budget from the full price, not the first bill.
- **Insurance.** New code and impact openings earn wind-mitigation credits; get a real quote before contract.

## What is not in the table

Lot premiums, structural options and design selections, which raise the price and every line that depends on it; closing costs of 2% to 3% before builder credits; and any HOA capital contribution at closing, which is not published.

:::trent
When a builder's website shows you a monthly payment, it is usually principal and interest on a bought-down rate with taxes estimated low and no CDD. Ask for the payment with taxes at full value, CDD included and insurance quoted. If the on-site team cannot produce it, I will, for any lot in the community, in an afternoon.
:::

Sources: builder base prices (Sep 3, 2026); SeaFlower HOA and CDD information sheet (Dec 8, 2025); Lake Flores CDD FY2027 proposed budget; Manatee County 2025 adopted millage rates.
"""),
    dict(slug="new-construction-inspections-seaflower", category="Buying process", title="New-construction inspections at SeaFlower: pre-drywall, blue tape and the 11-month walk",
         excerpt="What an independent inspector checks at each stage of a build, what I looked for when signing off homes for David Weekley, and why a new home still needs one.",
         video="kCjttf-puQQ", body="""
## Quick answer

Every new home in SeaFlower should get three independent inspections: at pre-drywall (framing, strapping, flashing, plumbing, electrical and ducts are all visible), at the final walkthrough (blue-tape every defect before closing), and at eleven months (before the one-year workmanship warranty expires). No SeaFlower builder prohibits it, and the builder's own quality checks are not a substitute.

## Why a brand-new home needs an inspector

A builder's construction manager and the county inspector both check the home, against the builder's standards and the code respectively. Neither works for you. I did the final quality-control walk for David Weekley for a living, and I still hire an independent inspector for every client, because a second set of eyes with no schedule pressure finds things.

## Pre-drywall

The most valuable inspection, because everything is exposed. What a good inspector checks: hurricane strapping and roof-to-wall connections, window and door flashing, plumbing rough-in and drain slopes, electrical box placement against the plan, duct routing and sealing, insulation baffles, and that structural options you paid for are actually framed. Weekley's EnergySaver program adds a duct-leakage test and a third-party insulation inspection before drywall; ask every builder what testing they do at this stage.

## Final walkthrough and blue tape

Walk every room with tape in hand: paint, drywall, trim, cabinet alignment, door swings, window operation, grout, caulk, appliance function, HVAC balance, exterior grading and drainage. The builder fixes tape items before closing far faster than after. Photograph everything.

## Eleven months

Drywall cracks, nail pops, settling, warranty items that surfaced through a full cycle of seasons. Submit the list before the one-year workmanship warranty ends. Warranties in SeaFlower: David Weekley 1-2-10, M/I 10-year structural with one-year customer care, Pulte 10-year structural, Issa 1-2-10 through RWC. Cardel's terms are not on its public pages; get them in writing.

## Cost and logistics

Independent inspections in the area typically run a few hundred dollars each; the pre-drywall one is the most valuable. Builders require scheduling with the construction manager, which I handle, and for out-of-state clients I attend and video the walk.

:::trent
The mistake I saw most often from the builder side: buyers skipping pre-drywall because the home "looked fine." Everything that matters is inside the walls at that point. Spend the money there first.
:::

Sources: David Weekley EnergySaver and warranty pages; Pulte, M/I and Issa warranty pages (Sep 3, 2026); Cardel FAQ.
"""),
    dict(slug="seaflower-village-center-publix", category="Community", title="The SeaFlower Village Center: Publix, the tenant list, apartments, the hotel and the opening timeline",
         excerpt="What CASTO and Redstone are building on 47 acres at Cortez Road and 75th Street, who has signed, and what opens when.",
         video="rU7t_DDvMkc", body=f"""
## Quick answer

The SeaFlower Village Center is a 47-acre mixed-use district at the community's front door, developed by CASTO and Redstone Investments with apartments by NDC Development. Phase one is about 140,000 square feet of retail, dining and office anchored by a 50,000-square-foot Publix with a separate Publix Liquors, plus 332 to 362 apartments and a 120-room hotel. It broke ground in September 2025; retail completion is targeted for the fourth quarter of 2026 and Publix for fall 2026.

## Who has signed

{"".join("- " + t + chr(10) for t in F.VILLAGE_CENTER["tenants"])}

## Apartments and hotel

The apartments (developer and CASTO figures differ, 332 versus 362) are NDC's project, with no leasing date or rents published yet; 600 apartments are planned at full buildout. The 120-room hotel has no announced brand or start date; the master plan calls for 250 rooms at buildout.

## What it means for residents

The center sits at the north edge of the community, reachable on the Lake Flores Trail by foot, bike or golf cart. It is the piece that turns SeaFlower from a subdivision into a village: groceries, coffee, a dentist and a bank without getting on Cortez Road. It also brings traffic to the front door; the plan's answer is the trail network that keeps daily trips internal.

## Timeline

Groundbreaking September 2025; Dutch Bros filed for its drive-thru on Cortez Road; Publix targeted for fall 2026; overall completion targeted for the fourth quarter of 2026, with openings staggered by tenant.

:::trent
I watch the Publix date more than any other milestone here, because it changes daily life for residents and it changes how buyers feel about the community on a tour. Until it opens, everyday retail is on Cortez Road and Manatee Avenue West, a few minutes away.
:::

Sources: CASTO and Redstone groundbreaking release (Sep 10, 2025); seaflower.com Village Center posts (Sep 22, 2025; Jan 28, 2026); Bradenton Herald tenant reporting (Aug 31, 2025); Pulse of Manatee (Nov 3, 2025).
"""),
    dict(slug="the-garden-club-seaflower-amenity-center", category="Community", title="The Garden Club at SeaFlower: what is inside the amenity center and when it opens",
         excerpt="Plumeria Hall, the Gathering Hall, the fitness center, the resort pool, four pickleball courts, the event lawn, and the HOA fee change that comes with opening day.",
         video="rU7t_DDvMkc", body=f"""
## Quick answer

The Garden Club is SeaFlower's resident-only amenity campus in Lake Flores Park, designed by LRK. It includes Plumeria Hall (lounge, catering kitchen, conference room), a Gathering Hall for events, a fitness center with a studio, a zero-entry resort pool with lap lanes and spa, a bath house, four pickleball courts, an event lawn and amphitheater, a fire pit and a playground. It broke ground on July 9, 2025 and is scheduled to open in fall 2026. An Art of Living Director programs the calendar.

## Inside the campus

{"".join("### " + n + chr(10) + d + chr(10) + chr(10) for n, d in F.GARDEN_CLUB)}

## Around it

The Garden Club anchors the 25-acre Lake Flores Park on the 19-acre lake, with the 2.5-mile multi-modal trail running past it, a nature trail through the wetland preserves, two dog parks and pocket parks throughout the neighborhoods.

## What changes when it opens

The clubhouse portion of the HOA assessment is currently abated. When The Garden Club is substantially complete, that portion is added to the monthly fee, so expect the $300.88 single-family assessment to step up after opening. The amount is not published; ask for the projected budget before contract.

## One pool for Phase One

Yes, this is the amenity campus for the 1,063 Phase One homes. Later phases have not published their amenity plans yet; buy for what is funded and on a plan.

:::trent
For buyers moving from a community with a finished clubhouse, the wait is the hardest part of buying here in 2026. For everyone who closes before it opens, the upside is simple: you bought before the amenity premium showed up in prices, and the fee step-up is the trade.
:::

Sources: seaflower.com Garden Club groundbreaking and amenities pages (Jul 14, 2025; 2026); Discover Bradenton 2026 update (May 1, 2026); Bradenton Magazine (Jun 1, 2026); SeaFlower HOA and CDD information sheet (Dec 8, 2025).
"""),
    dict(slug="homestead-exemption-new-construction-manatee", category="Costs & fees", title="Homestead exemption and the property-tax timeline on a new SeaFlower home",
         excerpt="Why the first tax bill is small and the second is not, the January 1 and March 1 deadlines, what to file with the Manatee County Property Appraiser, and portability.",
         video="VIPe5gI3oEU", body=f"""
## Quick answer

Florida assesses property as of January 1 and taxes it at the county's millage, about {F.TAXES['millage']} mills for SeaFlower's tax district in 2025. To get the homestead exemption, which removes up to $50,000 of assessed value and caps future assessment increases at 3% a year, you must own and occupy the home as your permanent residence on January 1 and file with the Manatee County Property Appraiser by March 1. A home not substantially complete on January 1 is taxed on the land only for that first year, which is why the first bill looks tiny and the second does not.

## The calendar that decides your bill

- **Close in December, occupy by January 1, file by March 1**: you get the exemption and the 3% cap for the coming year.
- **Close in January**: you wait a year for both. Buyers closing in late December and early January live in very different tax years.
- **Home finished after January 1**: first-year bill is land only. Set your escrow on the full value from day one; the lender's estimate should already assume it.

## What to bring

A Florida driver license or ID card, Florida vehicle registration, either voter registration or a declaration of domicile, and Social Security numbers for all owners. Manatee County accepts homestead applications online.

## Portability

If you are selling a Florida homestead to move here, you can transfer part of your old Save Our Homes cap to the new home, which can meaningfully lower the taxable value. Out-of-state buyers do not have a cap to bring; their first homestead year sets the baseline.

## The CDD is separate

The Lake Flores CDD assessment appears on the same tax bill as a non-ad valorem line, is not reduced by homestead, and is not capped; it is a fixed amount tied to the lot.

:::trent
Two dates matter more than any other on a Florida new build: the day the house is complete relative to January 1, and March 1. I put both on every client's closing checklist, and for a build finishing in late fall I raise the December-versus-January question with the builder early.
:::

Sources: Manatee County Property Appraiser exemptions and Save Our Homes FAQ; Florida Statute 192.042; Manatee County 2025 adopted millage rates; Lake Flores CDD FY2027 budget.
"""),
    dict(slug="insurance-on-a-new-seaflower-home", category="Costs & fees", title="Homeowners insurance on a new SeaFlower home: wind mitigation, impact glass and the Zone X flood policy",
         excerpt="Why new construction three miles from the Gulf insures for less than the headlines suggest, which credits Florida requires insurers to give, and what to do before contract.",
         video="Ju81eWneMUA", body="""
## Quick answer

A new SeaFlower home is built to the current Florida Building Code with impact-rated openings or shutters, reinforced block first floors and underground utilities, and Florida Statute 627.0629 requires insurers to discount premiums for code compliance and wind-mitigation features. That is why new construction here insures for meaningfully less than an older home at the same address. Budget roughly $2,500 to $7,000 a year for a single-family home depending on coverage, elevation and features, get a real quote before contract, and price an inexpensive Zone X flood policy even though a lender will not require one.

## What drives the premium

Wind is the cost driver on the Gulf Coast. A wind-mitigation inspection form documents roof shape, roof-to-wall connections, roof deck attachment, secondary water resistance and opening protection; new homes score well on all of them. Ask the builder for the elevation certificate and the wind-mitigation form at closing; your agent will need both.

## Flood

FEMA's flood hazard layer shows the interior of SeaFlower as Zone X, minimal hazard, with coastal AE and VE zones west of 86th Street and small Zone A pockets near 75th Street. In Zone X flood coverage is optional and inexpensive, and roughly one in three flood claims come from low- and moderate-risk zones. Manatee County's Community Rating System participation discounts NFIP premiums 10% outside the special flood hazard area.

## Attached homes

Townhome and villa owners in M/I's product carry HOA-provided coverage on the shared structure, funded inside the $308.43 and $327.70 monthly fees, plus their own policy for contents and interior. Confirm exactly what the association master policy covers before you buy an interior-only policy.

## What to do before contract

Get a quote from an independent agent, not only the builder's partner; compare the two; and write an insurance contingency into the offer. If the quotes are far apart, the wind-mitigation form usually explains why.

:::trent
Insurance is the objection I hear most from relocating buyers, and new construction is the best answer to it. On a recent client's new single-family home here, the independent quote came in well under the number the family had been bracing for after reading the news. The elevation certificate and the mitigation form did that work.
:::

Sources: Florida Statutes 553.73 and 627.0629; FEMA National Flood Hazard Layer (panel 12081C0284F); FloodSmart.gov; Manatee County floodplain management; SeaFlower developer materials on construction features.
"""),
]

for p in POSTS2:
    p.setdefault("date", DATE)
    p.setdefault("date_display", DATE_DISPLAY)

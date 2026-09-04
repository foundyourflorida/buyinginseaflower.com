"""Blog posts. Bodies use the site's markdown subset (see gen/html.py). Raw HTML lines are allowed (start the line with <)."""
from . import facts as F
from .builders_index import by_slug

DATE = "2026-09-03"
DATE_DISPLAY = "September 3, 2026"


def cdd_table_html():
    rows = "".join(f"<tr><td>{ph}</td><td>{lot}</td><td class=num>{v}</td></tr>" for ph, lot, v in F.CDD["fy2027"])
    return f'<div class="table-wrap"><table><thead><tr><th>Phase</th><th>Lot</th><th class=num>FY2027 proposed, per year</th></tr></thead><tbody>{rows}</tbody></table></div>'


def dw_plans_html():
    b = by_slug("david-weekley-homes")
    out = ""
    for c in b["collections"]:
        rows = "".join(f"<tr><td><b>{p['name']}</b></td><td class=num>{p['price']}</td><td class=num>{p['sqft']}</td><td>{p['beds']}</td><td>{p['baths']}{(' + ' + p['half_baths'] + ' half') if p.get('half_baths') and p['half_baths'] not in ('', '0') else ''}</td><td>{p['garage']}</td></tr>" for p in c["plans"])
        out += f'<h3>{c["name"]} · {c["lot_width"]} · {c["price_phrase"]}</h3><div class="table-wrap"><table><thead><tr><th>Plan</th><th class=num>Base price</th><th class=num>Sq ft</th><th>Beds</th><th>Baths</th><th>Garage</th></tr></thead><tbody>{rows}</tbody></table></div>'
    return out


POSTS = [
    dict(slug="seaflower-hoa-fees-explained", category="Costs & fees", title="SeaFlower HOA fees explained: what $300.88 a month actually covers, by home type",
         excerpt="The official numbers, what is inside them, why the internet shows five different figures, and the one thing that will change after The Garden Club opens.",
         video="8E3fPi_pTcA", body=f"""
If you search "SeaFlower HOA fees" you will find $163, $277, $300, $380, $526 and $983. Only one set of those numbers comes from the association itself. Here it is, and here is why the others exist.

## The official figures

The developer's HOA and CDD information sheet dated December 8, 2025, and David Weekley's community pages, both list the same monthly assessments:

| Home type | Monthly HOA |
|---|---|
| Single-family home | $300.88 |
| Townhome (M/I Row Home) | $308.43 |
| Twin villa (M/I Village Home) | $327.70 |

The association is SeaFlower Homeowners Association, Inc., managed by ICON Management. The fee is billed by the HOA, separately from the CDD assessment that appears on your tax bill.

## What is inside the number

Every home's fee includes 1-Gig fiber internet from Bluestream, front and rear yard landscape maintenance, upkeep of the parks, trails and common areas, and operation of The Garden Club once it opens. Townhome and villa fees add exterior maintenance, insurance and reserves for the shared structures, which is why they are slightly higher and why they suit owners who are away part of the year.

Two items are not inside it. The Lake Flores CDD assessment is separate and runs roughly $1,475 to $4,605 a year depending on phase and lot; it is on the tax bill. And the clubhouse portion of the HOA is currently abated. The sheet says it will be added at substantial completion of The Garden Club, scheduled for fall 2026. Expect the fee to step up then. How much is not published.

## Why the internet disagrees

Listing portals compute HOA fees from MLS entries, which agents enter as monthly, quarterly or annual amounts and which the portals convert inconsistently. A $925 to $983 "townhome" figure is almost certainly a quarterly amount ($308.43 times three is $925.29). A $163 low end is a partial figure. A $380 villa figure came from an agent blog written before the information sheet was published. When a number does not match the HOA's own sheet, trust the sheet.

## How to compare it with other communities

Add back what the fee includes. A community with a $150 HOA that leaves you paying $90 a month for internet and $150 for lawn care costs more than SeaFlower's $300.88. Lakewood Ranch villages vary widely and most sit inside a Stewardship District assessment on top of the HOA. The fair comparison is total recurring cost: HOA plus district assessment plus what you would buy separately.

:::trent
When I compare communities for a client I build one column: HOA, CDD or stewardship assessment, lawn, internet, and any amenity or gate fee. SeaFlower usually lands in the middle of the pack for a single-family home and near the top for what you get. The abated clubhouse portion is the number to ask about; I would budget for a meaningful increase after opening rather than be surprised.
:::

## What to get in writing before contract

Florida law requires the builder to give you an HOA disclosure summary before you sign, with a three-day right to cancel if it is missing. Ask for the current adopted budget, the declaration of covenants, the architectural guidelines, the amount of any capital contribution or working-capital fee at closing, and the projected assessment once the clubhouse portion is added. The last two are not published anywhere.

Sources: SeaFlower HOA and CDD information sheet (Dec 8, 2025); David Weekley SeaFlower Classic and Bungalow pages (Sep 3, 2026); ICON Management resident portal; Florida Statute 720.401.
"""),
    dict(slug="lake-flores-cdd-assessments-explained", category="Costs & fees", title="Lake Flores CDD: the official per-lot assessment table and what it means for your tax bill",
         excerpt="The district's own FY2027 numbers by phase and lot width, why Phase 1C costs more, and the answer to 'are CDD fees forever?'",
         video="V-BUVHpi6lQ", body=f"""
Out-of-state buyers meet the CDD on their first Florida new-construction purchase, usually on the first tax bill. Here is what the Lake Flores Community Development District is, what it costs on each SeaFlower lot, and how to read it.

## What a CDD is

A Community Development District is a special-purpose local government created under Chapter 190 of the Florida Statutes. It sells tax-exempt bonds to pay for a community's infrastructure and repays them through an annual assessment on every lot, collected on the county tax bill. At SeaFlower the district is the Lake Flores CDD, created by Manatee County Ordinance 22-04 on January 11, 2022, covering about 1,181 acres and managed by Wrathell, Hunt and Associates. It paid for stormwater management, wetlands and conservation areas, the multi-modal trail, the alleys and the streetlights.

## The bonds behind the number

Three bond series are outstanding: Series 2023A-1 ($23,375,000, maturing in 2054), Series 2023A-2 (largely prepaid by builders at lot closings in 2025 and 2026), and Series 2026 ($20,885,000, issued February 24, 2026 for Phase 1C). Your lot's annual debt assessment depends on which series financed it, plus an operations-and-maintenance charge of about $400 a year for everyone.

## The FY2027 proposed assessments

Presented in May 2026 and heard in August 2026. Per lot, per year, including operations and maintenance:

{cdd_table_html()}

Two patterns matter. Phase 1B lots dropped in FY2027 because builders prepaid much of the 2023A-2 series at lot closing. Phase 1C lots are higher because the Series 2026 bonds are new and not prepaid; a 50-foot lot is $3,899 in Phase 1C versus $2,280 in Phase 1B2. David Weekley quotes $2,095.84 (Bungalow) and $2,660.36 (Classic) on its pages, which line up with the Phase 1B2 45- and 60-foot figures.

## Are CDD fees forever?

The debt portion ends when the bonds mature, 2054 for the 2023 series and 2056 for the 2026 series, and it can be prepaid in a lump sum at any time, which many buyers do when they pay off a mortgage. The operations-and-maintenance portion continues indefinitely, because the district keeps maintaining the lakes, wetlands, trail and lights. So: the big part ends or can be ended; the small part is permanent.

## How it shows up

As a non-ad valorem line on your Manatee County tax bill every November, with up to a 4% discount for early payment. Because it is a fixed amount tied to the lot, it does not rise with your home's value. Lenders include it in escrow, which is why the first November surprises people who budgeted from a builder's payment estimate.

:::trent
The single most useful question to ask a sales consultant is "which phase is this lot in?" It changes the CDD by more than $1,500 a year on identical lots and it tells you how finished the streets around you will be when you move in. The second most useful question is whether the builder will pay down any of the debt assessment as an incentive; a few production builders will on slower-moving lots, and it is worth more than a design credit because it compounds every year.
:::

## The disclosure you will sign

Florida Statute 190.048 requires a bold-type notice in the purchase contract that the Lake Flores Community Development District may levy taxes or assessments. Read it as a prompt to ask for the current assessment for your specific lot, in writing.

Sources: Lake Flores CDD FY2027 proposed budget and FY2026 adopted budget (lakeflorescdd.net); district ordinance 22-04; developer HOA and CDD information sheet (Dec 8, 2025); David Weekley SeaFlower pages (Sep 3, 2026).
"""),
    dict(slug="david-weekley-bungalow-vs-classic-seaflower", category="Builders", title="David Weekley at SeaFlower: Bungalow vs Classic, from a former Weekley operations manager",
         excerpt="Twelve plans on two lot sizes, what each collection is really for, and what I checked on these homes when signing them off was my job.",
         video="kCjttf-puQQ", body=f"""
I spent a year in operations with David Weekley Homes, doing the final quality-control walk before homes were handed to buyers, and for a stretch I oversaw SeaFlower itself. So this is the one builder page where I can tell you not just what they sell but how the homes go together.

## Two collections, two lot widths

{dw_plans_html()}

Base prices as published on September 3, 2026, excluding lot premium and options. The Bungalow collection sits on 45-foot rear-load lots: garage in the alley, porch on the street, one- and two-story plans from 1,615 to 2,193 square feet. The Classic collection is on 60-foot lots, all one-story plans with optional bonus rooms that push square footage as high as 3,777, and a four-car garage on the Colston.

## Who each one fits

Bungalow buyers want the village experience: a short walk to the trail and parks, a porch they will use, a garage they do not have to look at. The Marina is the only two-story plan, and it is the one for anyone who needs a fourth bedroom on a 45-foot lot. The Malone at 1,615 square feet is the most efficient plan in the community for a single-level home with a study.

Classic buyers want a yard, a three-car garage, and single-level living with room to spare. The Borrelli's separate guest suite with its own bath is the plan people ask about when they need a second private suite; the Cecelia and Del Ray are the entertaining plans; the Colston is for the car collection.

## Models and quick move-ins

The Bellmeade (Bungalow) opened July 8, 2025 at 7650 Seaflower Parkway and the Rubytail (Classic) opened August 27, 2025 at 7635 Addison Avenue, which is also the sales office. On September 3, 2026 Weekley listed three Bungalow quick move-ins on Reflection Parkway from $574,990 to $599,990 (ready October 2026 to January 2027) and one Classic Rubytail at 8202 Merritt Avenue for $882,990 (ready November 2026).

## Incentives, the honest version

Weekley's September 2026 promotion, 7% off base price up to $40,000, explicitly excludes SeaFlower. That is the builder telling you this community sells without help. It does not mean nothing is negotiable; it means the conversation is about the lot premium, design-center credits and closing costs through Grace Home Lending, which Weekley owns 75% of and which you are not required to use. Compare its offer with an outside lender before you decide.

## What I checked on these homes, and still check

Weekley's EnergySaver program is real: duct leakage tested before drywall, blower-door tested at completion, third-party inspection of insulation and air sealing, with a Tampa-average HERS score of 71. What I add for clients is an independent inspector at pre-drywall and at final, a review of the warranty document itself (one year workmanship, two years systems, ten years structural), and a walk of the alley and driveway with the buyer's actual vehicle on the rear-load lots.

:::trent
The Weekley trades at SeaFlower are the same crews that built the models, and the models are honest examples of the product. My advice is simple: pick the plan by how you live, pick the lot by which phase it is in and what backs up to it, and let me handle the lender comparison and the credits. Bring me in before your first visit so I can be registered.
:::

Sources: David Weekley SeaFlower Bungalow and Classic collection pages, plan pages and quick move-in listings (Sep 3, 2026); David Weekley promotion pages (Sep 3, 2026); David Weekley EnergySaver and warranty pages.
"""),
    dict(slug="is-seaflower-in-a-flood-zone", category="Location", title="Is SeaFlower in a flood zone? FEMA zone, evacuation level and what insurance really costs",
         excerpt="What FEMA's map actually shows for the site, why the flood zone and the evacuation level are different questions, and the three documents to demand for your lot.",
         video="Ju81eWneMUA", body="""
"Is SeaFlower in a flood zone?" is one of the most-searched questions about the community, and most of the answers online are a single word from a blog. Here is what the official sources say, and what they cannot say.

## What FEMA's map shows

FEMA's National Flood Hazard Layer, on flood insurance rate map panel 12081C0284F effective August 10, 2021, shows the interior of the SeaFlower site as Zone X, the designation for areas of minimal flood hazard. West of 86th Street, toward Palma Sola Bay, the map moves through the 0.2%-annual-chance zone into coastal AE and VE zones. Near the 75th Street West edge there are isolated Zone A returns, which usually mark ponds and wetlands rather than homesites. So the honest summary is: the homes are in Zone X, the community's western and eastern edges are not, and your lot is what matters.

## Three questions, three answers

The FEMA zone determines whether a lender requires flood insurance. In Zone X it does not. The Manatee County evacuation level, A through E, determines who is told to leave ahead of a storm surge and is looked up by address on the county's Learn Your Level map; it is not the same as the flood zone and a Zone X home can sit in an evacuation level. The elevation certificate records the finished floor height of a specific home. Ask for all three for your lot. One agent video claims a 17-foot elevation for the community; I have not seen a document that supports a single number, and I would not repeat one until I had.

## Should you buy flood insurance anyway?

Probably. FEMA's own data say roughly one in three flood claims come from low- and moderate-risk zones, and a Zone X policy through the NFIP or a private carrier is inexpensive. Manatee County participates in the Community Rating System, which discounts NFIP premiums 10% outside the special flood hazard area. Three miles from the Gulf, I recommend pricing one.

## Wind insurance is the bigger line

Homeowner's insurance on the Gulf Coast is mostly about wind, and here new construction has a structural advantage. Every SeaFlower builder is building to the current Florida Building Code, which is updated every three years and cannot be weakened locally, and Florida law requires insurers to credit code compliance and mitigation features such as roof-to-wall connections and impact-rated openings. A wind-mitigation inspection form documents those credits. That is why a new home here insures for far less than a 1980s house at the same address. Get a real quote before contract and write an insurance contingency into your offer.

## What happened in 2024

Hurricanes Helene and Milton hit before SeaFlower's first homes were built; construction started in early 2025. Nearby, Anna Maria Island and the low-lying Cortez village took surge damage, while Zone X neighborhoods two to four miles inland reported wind and debris but not water. Every home in SeaFlower is being built to the code that came after those storms, with impact glass or shutters, reinforced block first floors and underground utilities described in the developer's materials.

:::trent
Two things I do for every client here: I pull the FEMA zone and evacuation level for the specific lot, in writing, and I get an insurance quote from an independent agent before we sign. The builders' partners are fine, but a second quote has saved clients real money more than once. And yes, I buy the cheap Zone X flood policy on my own house.
:::

Sources: FEMA National Flood Hazard Layer (panel 12081C0284F); FloodSmart.gov; Manatee County floodplain management and evacuation level pages; Florida Statutes 553.73 and 627.0629; Pulse of Manatee (Nov 3, 2025) on construction timing.
"""),
    dict(slug="seaflower-vs-lakewood-ranch", category="Comparisons", title="SeaFlower vs Lakewood Ranch: fees, commute, beach distance and what you are really choosing",
         excerpt="I have sold in both. One is finished infrastructure an hour from the sand; the other is the beach side of the county with the amenity center still under construction.",
         video="jHzcFHPQGas", body="""
I get this comparison on most strategy calls, and it usually comes down to one question I will get to at the end. First the facts.

## Scale and stage

Lakewood Ranch is a 30,000-plus-acre master plan that has been building for three decades, with dozens of villages, two town centers, and 1,064 new-home contracts in the first half of 2026, the second-best-selling community in the country. SeaFlower is 1,175 acres, started sales in May 2025, and posted 198 contracts in the same period, which tied it for 51st nationally in its first full year. One is a finished city with new villages at the edges; the other is a first phase around a lake with the amenity center opening this fall.

## Beach distance

This is the whole reason SeaFlower exists. The site plan measures 3.2 miles to the beach; builders quote 8 minutes to Bradenton Beach off-peak. From most of Lakewood Ranch the nearest Gulf beach is 30 to 45 minutes, longer in season, and that is the drive people underestimate when they buy for the weather and then never see the water.

## Fees

Both carry district assessments on top of the HOA. Lakewood Ranch villages sit inside the Lakewood Ranch Stewardship District, with HOA fees that vary widely by village and by whether lawn care and gates are included. SeaFlower's HOA is $300.88 a month for a single-family home and includes fiber and full yard maintenance; the Lake Flores CDD runs roughly $1,475 to $4,605 a year by phase and lot. The fair comparison is total recurring cost, and it is village-specific; I run it for clients with the actual villages they are considering.

## Builders and product

Lakewood Ranch has most of the national builders and price points from the $300s to several million. SeaFlower has five builders on one plan, from M/I townhomes at $399,999 to Issa estates above $1.25 million, with a coastal-village design code and an ADU allowance on every single-family lot that Lakewood Ranch villages do not offer.

## Amenities today versus amenities eventually

Lakewood Ranch has decades of built amenities, parks, sports campuses and a hospital. SeaFlower's Garden Club and Village Center open in late 2026, and later-phase amenities are not yet on a plan. If you need everything working on move-in day, that is a real difference for the next year or two.

## Resale

Lakewood Ranch has a deep, liquid resale market. SeaFlower's is just starting: the MLS shows about two dozen closings in the past year at roughly 99% of asking and $229 per square foot, mostly new-construction resales. Early buyers in first phases of well-executed master plans have generally done well over time; I will not promise that here, but the sales pace and rising lot premiums are the right early signs.

:::trent
The question I ask: do you want the beach to be part of your week, or a place you visit? If it is part of your week, SeaFlower is the only new-construction answer at this price on the beach side of Manatee County. If you want finished infrastructure, more restaurants tonight and a shorter drive to the interstate, Lakewood Ranch wins and I will happily show you the villages that fit. Plenty of my clients tour both in one day; I recommend it.
:::

Sources: RCLCO mid-year 2026 rankings via Sarasota Magazine (Jul 31, 2026); SeaFlower site plan and builder pages (Sep 3, 2026); Lake Flores CDD FY2027 budget; BEX Realty MLS summary (Sep 2026).
"""),
    dict(slug="do-you-need-a-buyers-agent-for-new-construction", category="Buying process", title="Do you need a buyer's agent for new construction in Bradenton? What the sales counselor won't tell you",
         excerpt="The on-site consultant is good at the job, and the job is selling the builder's homes. What representation actually does, what it costs, and the registration rule that trips people up.",
         video="gV6DH7M5iEU", body="""
I sat at the builder's sales desk for six years. I liked the buyers who came in with an agent and I liked the ones who did not, and I was measured the same way either way: on the builder's numbers. That is the whole answer, but here is the longer version.

## Who the sales consultant works for

The builder. In Florida, licensees are presumed to be transaction brokers unless a different relationship is put in writing, and the on-site consultant is either the builder's employee or the builder's agent. They will be friendly, knowledgeable and genuinely helpful, and they will not tell you the lot premium is negotiable, which incentive the division manager can approve, or which paragraph of the contract you should push back on. It is not their job.

## What it costs you

Nothing extra, in practice. Builders budget a co-broke commission on every sale and pay it to the buyer's agent at closing; they do not lower the price if you show up alone. Under the rules in place since August 2024 you will sign a written buyer agreement that states what you owe your agent, and compensation is negotiable; my agreements provide that the builder's payment satisfies it. The myth that you get a better deal without an agent is a line I heard on the sales floor, and it is not true.

## What representation does on a new build

It reads the contract, which is the builder's document, not the standard Florida form: deposit and default clauses, completion windows, cost-escalation language, appraisal-gap terms, arbitration. It negotiates the things that move: lot premium, closing-cost credits, rate buydowns, design credits, structural option pricing, and timing. It compares the affiliated lender against an outside quote. It brings an independent inspector at pre-drywall and final, and attends the walkthroughs. And for out-of-state buyers it is the person on the ground every couple of weeks with a camera.

## The registration rule

This is where buyers lose representation without knowing it. Most builders require your agent to accompany you or register you before your first visit to a model. If you tour on your own, some builders will not allow an agent to be added later, and you have just committed to buying that builder's home unrepresented. The fix takes five minutes: call or text me before your first visit and I register you with every builder in the community.

## Single agent or transaction broker?

Ask any agent which relationship they are offering. Florida's default is transaction broker, a limited form of representation. A single agent owes fiduciary duties and must give you a written notice before showing property. I explain the difference on every first call so you can choose.

:::trent
I am not an on-site rep anymore, so I will say the quiet part: the best consultants in SeaFlower are very good, and a couple of them are friends of mine. Use them for what they know. Use me for what they cannot say. It costs you nothing and it changes the contract you sign.
:::

Sources: Florida Statute 475.278; NAR consumer guides on written buyer agreements and offers of compensation (2024); builder realtor pages (Sep 3, 2026).
"""),
    dict(slug="quick-move-in-vs-to-be-built-seaflower", category="Buying process", title="Quick move-in or to-be-built at SeaFlower: which is the better deal right now",
         excerpt="Finished inventory carries the discounts and rate buydowns. To-be-built gets you the lot. How to decide, with the September 2026 numbers.",
         video="fx345crY-mo", body="""
Every builder in SeaFlower sells both: homes already under construction with a price and a completion date, and lots you can pick a plan for. They are priced differently, negotiated differently and financed differently.

## Why quick move-ins are cheaper than they look

A finished home costs the builder money every month it sits: construction loan interest, taxes, insurance, the sales team's attention. That is why inventory carries the incentives you see advertised. In September 2026, Pulte listed quick move-ins with "$10,000 in savings" (one Mabel II was cut from $675,405 to $665,405), M/I advertised a 4.875% FHA rate (5.644% APR) on select inventory, and M/I's townhome listings carried "was" prices. A quick move-in's price also already includes the lot premium and the options in the house, so it is closer to the real number than a base-price sign.

## What to-be-built gets you

The lot you want, in the phase you want, with the structural options you want: the extra garage bay, the extended lanai, the ADU or garage suite, the pool bath. And finishes chosen by you rather than by the builder's design team for resale appeal. You pay base price plus lot plus options, you wait seven to fourteen months depending on the builder, and you carry rate risk during the build unless you lock with a forward commitment through the builder's lender.

## The math I run

Take the quick move-in's price and subtract the value of its included options and lot premium to get an apples-to-apples base. Then add what you would actually spend on the to-be-built version: lot premium, the options you would choose, and the design-center budget (builders' own guidance runs 10% to 20% of base; most of my clients land at 5% to 15%). Compare the totals, then compare the monthly payments with each lender's incentive. A quick move-in with the right lot and 80% of the finishes you would have picked wins that comparison most of the time.

## When to-be-built wins

When the lot matters: a lake, park or corner lot in a phase with a lower CDD assessment. When you need a structural feature no inventory home has, an ADU especially. When you are a year out anyway and can use the build time to sell a house elsewhere. And when the builder is releasing a new phase and pricing it to move.

## Timing

Builders push hardest in the last two weeks of a fiscal quarter, and September and December are the months when inventory gets cleared before reporting. Homes that have passed their listed ready date without a contract are where the conversation about price and credits gets interesting.

:::trent
My honest bias: I steer most clients toward a quick move-in when one fits, because the incentive money is real and the home is inspectable before you close. I steer them to build when they want an ADU, a specific lot, or a plan the inventory does not cover. Either way I bring an inspector, and either way I run the lender math both ways before we sign.
:::

Sources: Pulte, M/I Homes and David Weekley SeaFlower quick move-in listings and promotions (Sep 3, 2026); Cardel Homes FAQ on build times and design-center spend; Fannie Mae selling guide on interested-party contributions.
"""),
    dict(slug="honest-pros-and-cons-of-buying-in-seaflower", category="Community", title="The honest pros and cons of buying in SeaFlower",
         excerpt="Traffic, density, CDD debt, construction years and one pool for the first phase, weighed against the beach, the design and the sales pace.",
         video="rU7t_DDvMkc", body="""
I make a living helping people buy here, which is exactly why I owe you the case against it. Here are the objections I hear most, with what is true about each, and then the case for.

## The cons

**Cortez Road traffic.** It is the only bridge road to Anna Maria Island, and in season, mid-February to mid-April, beach traffic backs up. Four thousand more homes will add trips. The plan mitigates it with the internal trail and a Village Center that keeps errands off the road, and the Cortez bridge replacement is a pending state project. There is no published traffic study I have found. If your daily routine crosses that bridge, drive it at the worst time before you buy.

**Density.** Most single-family lots are 42 to 60 feet wide. That is closer than a 1990s subdivision and it is the price of walkability, porches and parks within a block. Rear-load lots feel tighter in the back and more open on the street. The 60- and 80-foot lots exist for people who want space.

**Paying for amenities before they open.** HOA dues start at closing and the CDD lands on the first tax bill, while The Garden Club opens in fall 2026. The developer has abated the clubhouse portion of the HOA until then, which is the one concession, and the trail, parks and lawn service you are paying for exist now.

**One pool for Phase One.** True: one amenity campus serves 1,063 homes. Later-phase amenities are not yet on a plan. Do not buy on the assumption of a second pool until it is.

**CDD debt.** Roughly $1,475 to $4,605 a year by phase and lot, for decades, with bonds totaling tens of millions of dollars. It is disclosed, it is fixed, it can be prepaid, and it built the infrastructure you are enjoying. It is also money.

**Construction years.** A community this size takes a decade or more. You will live near active construction, and the Village Center, apartments and hotel will build out around you. Some people find that energizing. Some do not.

## The pros

**The beach side of the county.** 3.2 miles to the sand and almost no other new construction on this side of Manatee County. That scarcity is the whole thesis.

**The design.** Four architectural styles, porches on the street, alleys, pocket parks, a golf-cart trail to a Publix, and an ADU allowed on every single-family lot. It is the most deliberate plan I have worked on.

**Five builders competing on one plan.** M/I, Pulte, David Weekley, Cardel and Issa at prices from $399,999 to above $1.25 million, all competing for the same buyer, which keeps incentives honest.

**Sales pace and early recognition.** About 270 homes sold in the first year and a national top-selling ranking from RCLCO in the first half of 2026. Builders do not release Phase 1C lots into a community that is not moving.

**New code, new systems.** Impact openings, reinforced block first floors, underground utilities, current energy standards, and warranties from one to ten years. Insurance reflects it.

:::trent
My honest read: SeaFlower is a good buy for someone who wants the beach in their week, likes the village pattern of living, and can hold the home through the construction years at a payment that includes the CDD. It is a bad buy for someone who needs everything finished, wants a half-acre, or will resent the bridge traffic. I tell people which one they are on the first call, and I lose some of them to Lakewood Ranch. That is fine.
:::

Sources: SeaFlower developer pages and press releases (2025–2026); Lake Flores CDD budgets; RCLCO mid-year 2026 report; YouTube and Reddit comment threads reviewed Sep 3, 2026.
"""),
    dict(slug="seaflower-construction-timeline", category="Community", title="SeaFlower construction timeline: Garden Club, Publix, Village Center, apartments, hotel and Phase Two",
         excerpt="A living page of what is built, what is under construction and what is promised, with dates as published. Updated as milestones land.",
         video="rU7t_DDvMkc", body="".join([
             "Buyers in a first phase are buying a plan as much as a place, so here is the plan with dates as the developer, its partners and the press have published them. I update this page when a milestone changes.\n\n## What is built\n\n",
             "- The Welcome Center at 4505 Flower Fields Trail, a Cardel-built home with an 800-square-foot ADU, opened fall 2025.\n- Models from all five builders; the last showcase homes (Issa and M/I) opened March 7, 2026.\n- 400 finished lots in Phases N1 and 1B, with the first residents moved in since September 2025.\n- The 2.5-mile Lake Flores Trail sections around the first neighborhoods, lakes, pocket parks and streetlights (maintained by the CDD).\n\n## Under construction\n\n",
             "- The Garden Club: broke ground July 9, 2025; scheduled to open fall 2026.\n- The Village Center: broke ground September 2025; retail, dining and office completion targeted for the fourth quarter of 2026, with Publix and Publix Liquors slated for fall 2026. Dutch Bros has filed for its drive-thru on Cortez Road.\n- Phase 1C: 384 lots under development through 2026, financed by the $20.9 million Series 2026 bonds issued February 24, 2026.\n- Apartments: 332 to 362 units in the Village Center by NDC Development (sources differ on the count); delivery date not published.\n\n## Promised, not yet dated\n\n",
             "- The 120-room hotel in the Village Center; brand and start date unpublished.\n- Phase Two, expected to begin around 2027 depending on market conditions, as the second of three roughly 400-acre phases.\n- Amenities for later phases; none are on a published plan yet.\n- Full buildout: about 4,000 homes, 600 apartments, 250 hotel rooms and 350,000 square feet of commercial space.\n\n## The dated timeline\n\n",
             "<ol class=\"timeline\">" + "".join(f"<li><b>{d}</b><span>{t}</span></li>" for d, t in F.TIMELINE) + "</ol>\n\n",
             ":::trent\nWhat I watch, in order: the Garden Club opening, because it ends the abated HOA period and changes the fee; the Publix opening, because it changes daily life; and the pricing of Phase 1C lots relative to Phase 1B, because it tells you what the builders think demand looks like. I will update this page as each one lands.\n:::\n\nSources: seaflower.com news posts (2024–2026); CASTO and Redstone releases (Sep 2025); Lake Flores CDD agendas and budgets (2026); Business Observer (Oct 31, 2025); Pulse of Manatee (Nov 3, 2025); Bradenton Magazine (Apr and Jun 2026).\n",
         ])),
    dict(slug="how-builder-incentives-work-at-seaflower", category="Buying process", title="How builder incentives really work at SeaFlower, and how to stack them",
         excerpt="Rate buydowns, closing-cost credits, design credits and lot premiums: the mechanics, the September 2026 offers by builder, and the order to ask in.",
         video="XboFwTIlusw", body="""
Incentives are the part of new construction that looks generous and is actually a system. Once you understand the system you can work it.

## The mechanics

Most incentives are paid through the builder's affiliated lender: Pulte Mortgage for Pulte, M/I Financial for M/I, Grace Home Lending (75% builder-owned) for David Weekley, a preferred bank for Cardel. The builder contributes money toward your closing costs or discount points; the lender books it as an interested-party contribution, which Fannie Mae caps at 3%, 6% or 9% of price depending on your down payment (2% on investment property). A permanent buydown lowers the note rate for the life of the loan. A temporary 2-1 buydown lowers it for the first two years; you must qualify at the full rate. Forward commitments let the builder lock a block of below-market rates months ahead and offer them on specific homes with specific closing windows.

You are never required to use the affiliated lender. The incentive usually disappears if you do not. So the comparison is total cost with the incentive versus an outside lender's rate and fees, not rate versus rate.

## What was published in September 2026

David Weekley's 7%-off promotion (up to $40,000) explicitly excluded SeaFlower, with no SeaFlower-specific offer published. Pulte listed "$10,000 in savings" on select quick move-ins and rate offers through Pulte Mortgage's forward commitment. M/I advertised a 4.875% FHA 30-year rate (5.644% APR) on select quick move-ins plus a "Summer Savings" campaign. Cardel offered up to $20,000 toward design options. Issa published nothing. Published offers are the floor, not the ceiling.

## What is negotiable, in order

1. **Lot premium.** Quoted separately, and the most negotiable number on a lot that has been sitting.
2. **Closing-cost credit.** Often expandable beyond the advertised amount at quarter-end.
3. **Rate buydown depth.** Points cost the builder less than price cuts and mean more to your payment.
4. **Design-center and structural option credits.** Cardel's $20,000 design offer is the pattern; others do it quietly.
5. **CDD debt paydown.** Rare, valuable, and worth asking for on slower lots.
6. **Base price.** Moves last, and mostly on inventory that has missed its ready date.

## Timing

Fiscal quarter-ends: the last two weeks of March, June, September and December. September and December are the strongest because builders clear inventory before year-end reporting. Division managers can approve what on-site consultants cannot request, and the request has to come through your agent to reach them.

:::trent
The mistake I saw most often from the builder's side of the desk: buyers negotiating the base price, losing, and leaving the closing-cost credit and lot premium on the table because nobody told them those were the levers. The second mistake: taking the bought-down rate without an outside quote. I run both numbers on every deal, and I ask for the CDD paydown every time, because occasionally the answer is yes.
:::

Sources: Pulte, M/I Homes, David Weekley and Cardel SeaFlower pages and promotions (Sep 3, 2026); Fannie Mae selling guide sections on interested-party contributions and temporary buydowns.
"""),
    dict(slug="moving-to-west-bradenton", category="Relocation", title="Moving to west Bradenton: living three miles from Anna Maria Island",
         excerpt="What this side of the county is like, the homestead calendar that decides your first tax bill, and the things I tell every relocating buyer from Buffalo.",
         video="OlP4BZUWXDI", body="""
I moved here from Buffalo knowing nothing about the area, which is why I am patient with people who ask what west Bradenton actually is. Here is the version I wish someone had given me.

## The place

West Bradenton is the coastal mainland of Manatee County: the Cortez fishing village at the foot of the bridge, the causeway to Anna Maria Island, Palma Sola Bay, the trails of Robinson Preserve, IMG Academy's campus, Pirates spring training at LECOM Park and a Riverwalk downtown on the Manatee River. It is older Florida, established and a little worn in places, and it had almost no new construction until SeaFlower. Sarasota-Bradenton airport is 18 minutes; downtown Sarasota about 25; Tampa about an hour.

## The beach, honestly

3.2 miles from SeaFlower to the sand, about 8 minutes to Bradenton Beach off-peak. In season, mid-February to mid-April, the bridge road backs up, and the locals' rule is before 10 a.m. or after 1:30 p.m. Most people who live here go early, stay late, and stop noticing it.

## Weather and the year

May through September is hot and humid with afternoon storms; it is the trade for January. Snowbird season runs January through April and it changes traffic, restaurant waits and the sales floor. Hurricane season is June through November, and the practical answer is a new-code home, a Zone X flood policy and a plan; the location page covers the flood and evacuation lookups.

## The calendar that decides your taxes

Florida assesses property as of January 1 and the homestead exemption requires you to own and occupy by January 1 and file by March 1. Close in December and you get the exemption and the 3% assessment cap for the coming year; close in January and you wait a year. A new home not finished on January 1 is taxed on the land only for that first year, which makes the first bill look tiny and the second bill a surprise. Set your escrow on the full value from day one.

## Becoming a Floridian

A Florida driver license or ID, Florida vehicle registration, and voter registration or a declaration of domicile are what the Property Appraiser wants to see for homestead. No state income tax changes the math for retirement withdrawals and remote work; it also means property taxes and insurance carry more of the load, which is why the costs page exists.

## Starting over socially

Nobody warns you about this part. Moving here means new neighbors, new routines and no built-in circle. SeaFlower's answer is the Art of Living Director and the calendar of events at The Garden Club, the pickleball courts, and a village pattern that puts you on a porch within talking distance of the sidewalk. It works better than a gated cul-de-sac for meeting people; that is the honest reason people choose this pattern.

:::trent
Three things I tell every relocating client. Come in July once before you commit. Do not buy the first weekend; tour SeaFlower and Lakewood Ranch in the same day and feel the difference. And decide where you will actually spend your weekends, because that decides whether the beach side of the county is worth it to you. For most of my clients from Buffalo, Boston and New Jersey, it is.
:::

Sources: SeaFlower location page and site plan; Cardel and M/I drive times (Sep 3, 2026); Manatee County Property Appraiser homestead FAQ; Florida Statute 192.042.
"""),
    dict(slug="seaflower-market-update-september-2026", category="Market update", title="SeaFlower market update, September 2026: sales pace, inventory, incentives and what opens next",
         excerpt="The first full year in numbers, what is listed right now by builder, what builders are offering, and what I am watching this fall.",
         video="6AAxoU8RHek", body=f"""
A monthly read on where the community stands, with numbers as published.

## Sales pace

Sales opened in May 2025. The developer reported 60-plus homes by August 2025, 138-plus before the late-October grand opening, and 200-plus with 90-plus residents by March 2026. Bradenton Magazine reported 238 sold by March 30 (79 in 2026) and more than 270 by June 1. RCLCO counted 198 new-home contracts in the first half of 2026, which tied SeaFlower for 51st best-selling master-planned community in the country and 17th in Florida. For context, Lakewood Ranch posted 1,064 and Wellen Park 727 in the same period.

## Lots and phases

784 of 1,063 Phase One homesites had been released by April 2026. 400 lots are finished and 384 more are under development through 2026 in Phase 1C, financed by the $20.9 million Series 2026 bonds issued in February. Phase Two is expected around 2027.

## Inventory by builder

On September 3, 2026 the builders listed about three dozen quick move-in homes: M/I Homes 21 (townhomes from $399,999 and villas from $429,999, many with "was" prices), Pulte 6 ($568,895 to $756,090, completing October 2026 to January 2027), David Weekley 4 ($574,990 to $882,990, October 2026 to January 2027), Cardel 2 (Coral plans in the low $700,000s, September 2026), Issa 2 (lakefront estates at $1,567,560 and $1,720,000, early 2027). The full list is on the homes page.

## Incentives

David Weekley's September 7%-off promotion excludes SeaFlower. Pulte is showing $10,000 in savings on select inventory. M/I is advertising a 4.875% FHA rate (5.644% APR) on select quick move-ins. Cardel is offering up to $20,000 toward design options. Issa has published nothing. Read the incentives post for how to work these.

## Rates and resale

Freddie Mac's 30-year average ran in the mid-6% range through late summer; builder buydowns are running one to two points below that on inventory. On the MLS, roughly two dozen SeaFlower closings in the past twelve months averaged about 99% of asking, $229 per square foot and 30 days on market, all new-construction resales; most builder sales never hit the MLS.

## What opens next

The Garden Club and Publix are both scheduled for fall 2026, with Village Center completion targeted for the fourth quarter. The clubhouse portion of the HOA assessment is abated until the Garden Club is substantially complete, so expect the fee to step up after opening.

:::trent
My read for September: this is the best month of the year to buy inventory here. Builders are clearing quick move-ins before quarter- and year-end reporting, five of them are competing for the same buyer, and the amenity center opening will take some negotiating room off the table by winter. If you have been waiting, this is the window I would use.
:::

Sources: seaflower.com news posts and press releases (2025–2026); Bradenton Magazine (Apr 1 and Jun 1, 2026); RCLCO via Sarasota Magazine (Jul 31, 2026); builder listings and promotions (Sep 3, 2026); BEX Realty MLS summary (Sep 2026); Lake Flores CDD agendas (2026).
"""),
]

for p in POSTS:
    p.setdefault("date", DATE)
    p.setdefault("date_display", DATE_DISPLAY)

from .posts2 import POSTS2  # noqa: E402
POSTS = POSTS + POSTS2
from .posts3 import POSTS3  # noqa: E402
POSTS = POSTS + POSTS3

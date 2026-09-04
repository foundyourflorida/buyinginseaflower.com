"""Community-level facts for SeaFlower, Bradenton FL. Every value traces to the research notes (sources listed per section).
Update the AS_OF date when you re-verify."""

AS_OF = "September 3, 2026"
AS_OF_ISO = "2026-09-03"

COMMUNITY = {
    "name": "SeaFlower",
    "aka": ["Seaflower", "SeaFlower Florida", "Lake Flores"],
    "acres": "1,175",
    "location": "west Bradenton, Manatee County, Florida 34210, south of Cortez Road West and west of 75th Street West (86th Street West on the west, El Conquistador Parkway on the south)",
    "developer": "Lake Flores Land Company (principal Ed Hill) with investment partner LAMB Properties; the brand and site plan are held by Cortez75W Investors, LLC",
    "history": "the former Preston family gladiolus farm (Manatee Fruit Company), farmed for nearly 90 years; approved by Manatee County in 2015 as Lake Flores and renamed SeaFlower",
    "buildout": {"homes": "about 4,000", "apartments": "600", "hotel_rooms": "250", "commercial": "350,000 sq ft of retail and office"},
    "phase_one": {"acres": "400", "homes": "1,063", "apartments": "332 to 362 (sources differ)", "hotel_rooms": "120", "commercial": "about 140,000 sq ft"},
    "beach": "3.2 miles to the beach per the developer's site plan; just over three miles to Anna Maria Island; Longboat Key under 10 miles",
    "lake": "19-acre Lake Flores inside the 25-acre Lake Flores Park",
    "trail": "2.5-mile multi-modal Lake Flores Trail for walking, biking and golf carts",
    "styles": ["Coastal", "West Indies", "Craftsman", "Transitional Farmhouse"],
    "welcome_center": {"address": "4505 Flower Fields Trail, Bradenton, FL 34210", "phone": "(941) 212-0801", "hours": "Monday to Saturday 9:30 a.m. to 5:30 p.m., Sunday 12 to 6 p.m.", "url": "https://seaflower.com/contact/"},
    "official_site": "https://seaflower.com",
    "gated": "No gates appear on the site plan or in any developer material; streets are being turned over to Manatee County as public roads.",
    "age_restricted": "No. SeaFlower is an all-ages community marketed for every stage of life.",
    "golf_carts": "The Lake Flores Trail is designed for golf carts and the developer calls the community golf-cart-friendly. Rules for carts on the public streets follow Florida low-speed-vehicle law; confirm with the HOA before you buy a cart.",
    "adu": "Every single-family homesite is permitted to add an accessory dwelling unit (garage apartment or detached casita). To rent an ADU, the owner must occupy the main home for one year first, and leases must be at least six months.",
    "pets": "No published pet rules were found. Two dog parks are planned. Ask for the HOA covenants before contract.",
    "rentals": "Whole-home leasing rules are in the HOA covenants (a third-party blog claims one year of owner occupancy before leasing; not confirmed in official documents). Ask for the CC&Rs before contract.",
}

LOT_MIX = [
    # phase, product, count, lot width
    ("N1", "Row Homes (townhomes, M/I Homes)", 68, "attached"),
    ("N1", "Village Homes (twin villas, M/I Homes)", 90, "attached"),
    ("1B1", "Bungalow 42'", 66, "42'"), ("1B1", "Bungalow 45'", 32, "45'"), ("1B1", "Cottage 50'", 77, "50'"), ("1B1", "Classic 60'", 46, "60'"), ("1B1", "Estate 80'", 21, "80'"),
    ("1B2", "Bungalow 45'", 94, "45'"), ("1B2", "Cottage 50'", 54, "50'"), ("1B2", "Classic 60'", 90, "60'"), ("1B2", "Estate 80'", 27, "80'"),
    ("1C", "Bungalow 42'", 85, "42'"), ("1C", "Bungalow 45'", 37, "45'"), ("1C", "Cottage 50'", 140, "50'"), ("1C", "Classic 60'", 136, "60'"),
]

PRODUCT_LADDER = [
    ("Row Homes", "Townhomes", "M/I Homes", "Priced from $399,999", "/builders/mi-homes/"),
    ("Village Homes", "Twin villas", "M/I Homes", "Priced from $399,999", "/builders/mi-homes/"),
    ("Bungalow Homes", "42' and 45' lots, rear-load garages", "Pulte Homes, David Weekley Homes", "From the $400s (Pulte) and the $500s (David Weekley, base plans from $469,990)", "/builders/"),
    ("Cottage Homes", "50' lots", "Cardel Homes, Pulte Homes", "From the $500s (Cardel); Pulte Veranda and Distinctive series from $439,990", "/builders/"),
    ("Classic Homes", "60' lots", "Cardel Homes, David Weekley Homes", "From the $600s (David Weekley, base plans from $624,990); Cardel mid-$500s to over $680,000", "/builders/"),
    ("Estate Homes", "80' lakefront lots", "Issa Homes", "Starting from $1,250,000, excluding homesite premium", "/builders/issa-homes/"),
]

TIMELINE = [
    ("2015", "Manatee County approves the Lake Flores plan, including ADU zoning on every single-family lot."),
    ("Jan 2022", "Lake Flores Community Development District created (Ordinance 22-04)."),
    ("May 2024", "Plans unveiled under the SeaFlower name; Publix announced as the first Village Center tenant in September 2024."),
    ("Jan 28, 2025", "Preview Center opens at 8114 Cortez Road West."),
    ("Mar 2025", "Builder plans and prices released; home sales begin in May 2025."),
    ("Jul 9, 2025", "The Garden Club amenity center breaks ground."),
    ("Sep 2025", "First residents move in; Village Center (CASTO and Redstone) breaks ground."),
    ("Late Oct 2025", "Official grand opening; more than 138 homes sold by December."),
    ("Feb 24, 2026", "CDD issues $20,885,000 Series 2026 bonds for Phase 1C."),
    ("Mar 7, 2026", "Public model grand opening for new Issa Homes and M/I Homes showcase homes; 200+ homes sold in the first year."),
    ("Apr 10, 2026", "784 of 1,063 Phase One homesites released; 384 more lots under development through 2026."),
    ("Jul 30, 2026", "RCLCO ranks SeaFlower tied for 51st best-selling master-planned community in the U.S. with 198 contracts in the first half of 2026."),
    ("Fall 2026", "The Garden Club and Publix scheduled to open; Village Center completion targeted for the fourth quarter of 2026."),
    ("About 2027", "Phase Two expected to begin, timing dependent on market conditions."),
]

SALES_PACE = [
    ("Aug 11, 2025", "60+ homes sold since sales began in May", "developer press release"),
    ("Nov 3, 2025", "110 sold, about 65 under construction", "Pulse of Manatee"),
    ("Dec 10, 2025", "138+ sold before the grand opening", "developer release via BusinessWire"),
    ("Mar 10, 2026", "200+ sold, 90+ residents", "seaflower.com"),
    ("Mar 30, 2026", "238 sold (79 in 2026), 150+ residents", "Bradenton Magazine"),
    ("Jun 1, 2026", "270+ sold", "Bradenton Magazine"),
    ("Jun 30, 2026", "198 contracts in the first half of 2026 (tied 51st nationally)", "RCLCO mid-year report"),
]

GARDEN_CLUB = [
    ("Plumeria Hall", "Social lounge, demonstration and catering kitchen, conference room for remote work, covered veranda on three sides. Home base for the Art of Living Director who programs the events calendar."),
    ("Gathering Hall", "Indoor-outdoor event hall for clubs, celebrations and HOA meetings, with catering kitchen and outdoor barbecue area."),
    ("Fitness Center", "Workout equipment, a virtual fitness studio, a dedicated studio for classes and a lawn for outdoor yoga; a kids' activity center is also listed."),
    ("Resort pool and Bath House", "Zero-entry pool with lap lanes, sun shelves, covered cabanas, outdoor summer kitchen and spa."),
    ("Courts, lawn and play", "Four pickleball courts, event lawn and amphitheater with a food-truck area, community fire pit and a children's playground."),
]

VILLAGE_CENTER = {
    "developers": "CASTO and Redstone Investments (their third partnership); apartments by Bradenton's NDC Development",
    "size": "About 47 acres; roughly 140,000 sq ft of retail, dining and office in phase one (161,500 sq ft total leasable planned)",
    "anchor": "Publix (about 50,000 sq ft) with a separate Publix Liquors, opening fall 2026",
    "tenants": ["Publix and Publix Liquors", "Dutch Bros Coffee (first in Manatee County)", "Whataburger", "Playa Bowls", "Potbelly Sandwich Works", "Dave's Hot Chicken", "Pecan Jacks", "Nothing Bundt Cakes", "PacDental / PDS Health", "Club Pilates", "Well Groomed Pets", "Glitz Nail Salon and Boutique", "Men's Luxe Barbershop", "PNC Bank", "Suncoast Credit Union", "Degree Wellness"],
    "apartments": "332 to 362 apartments (developer and CASTO figures differ)",
    "hotel": "120-room hotel in phase one (brand not announced); 250 rooms at buildout",
    "timeline": "Groundbreaking September 2025; completion targeted for the fourth quarter of 2026",
}

HOA = {
    "name": "SeaFlower Homeowners Association, Inc.",
    "manager": "ICON Management (Community Association Manager Alicia Green, (512) 336-9112)",
    "portal": "https://icon.cincwebaxis.com/seaflower/home/",
    "fees": [("Single-family home", "$300.88 per month"), ("Townhome", "$308.43 per month"), ("Twin villa", "$327.70 per month")],
    "includes": "1-Gig fiber internet to each home, front and rear yard landscape maintenance, common areas, parks, trails and The Garden Club operations. Townhome and villa fees add exterior maintenance, insurance and reserves.",
    "abated": "The clubhouse portion of the assessment is abated until The Garden Club is substantially complete, so expect the fee to step up after the fall 2026 opening.",
    "source": "2026 SeaFlower HOA and CDD Information Sheet dated Dec 8, 2025; David Weekley community pages ($300.88, front and rear lawn maintenance, excludes amenity fees)",
}

CDD = {
    "name": "Lake Flores Community Development District",
    "created": "Manatee County Ordinance 22-04, January 11, 2022; about 1,181 acres",
    "manager": "Wrathell, Hunt and Associates, LLC, (877) 276-0889, info@lakeflorescdd.net",
    "site": "https://lakeflorescdd.net",
    "pays_for": "stormwater management, wetlands and conservation areas, the multi-modal trail, alleys and streetlights",
    "bonds": "Series 2023A-1 ($23,375,000, final maturity 2054), Series 2023A-2, and Series 2026 ($20,885,000 issued Feb 24, 2026 for Phase 1C)",
    "om": "$402.29 per unit in FY2026; about $398 (Phases 1B and N1) or $371 (Phase 1C) in the proposed FY2027 budget",
    "collection": "Billed on the Manatee County property-tax bill each November, with up to a 4% discount for early payment",
    "fy2026": [("Row Homes / townhomes", "$1,477.30"), ("Village Homes / twin villas", "$1,584.80"), ("Bungalow 42'", "$1,756.81"), ("Bungalow 45'", "$1,853.56"), ("Cottage 50'", "$2,014.81"), ("Classic 60'", "$2,337.31"), ("Estate 80'", "$2,982.32")],
    "fy2027": [
        ("Phase N1", "Townhome", "$1,473.49"), ("Phase N1", "Twin villa", "$1,580.99"),
        ("Phase 1B1", "42'", "$1,753.00"), ("Phase 1B1", "45'", "$1,849.75"), ("Phase 1B1", "50'", "$2,011.00"), ("Phase 1B1", "60'", "$2,333.50"), ("Phase 1B1", "80'", "$2,978.51"),
        ("Phase 1B2", "45'", "$2,091.63"), ("Phase 1B2", "50'", "$2,279.75"), ("Phase 1B2", "60'", "$2,656.01"), ("Phase 1B2", "80'", "$3,408.52"),
        ("Phase 1C", "42'", "$3,334.52"), ("Phase 1C", "45'", "$3,546.24"), ("Phase 1C", "50'", "$3,899.09"), ("Phase 1C", "60'", "$4,604.78"),
    ],
    "builder_quotes": "David Weekley quotes $2,095.84 per year (Bungalow) and $2,660.36 (Classic) on its pages, which line up with the Phase 1B2 45' and 60' figures plus a small difference.",
    "source": "Lake Flores CDD FY2026 adopted budget and FY2027 proposed budget (lakeflorescdd.net); developer HOA/CDD information sheet dated Dec 8, 2025",
}

TAXES = {
    "millage": 14.61,
    "millage_note": "2025 adopted total millage for the Cedar Hammock Fire Control District tax district in unincorporated west Bradenton (14.6100); David Weekley's pages show 14.671, the 2024 rate, and the 2026 proposed rate is 14.5666. Confirm the district for a specific parcel with the Manatee County Property Appraiser.",
    "homestead": "Florida homestead exemption removes up to $50,000 of assessed value for a primary residence and caps annual assessment increases at 3% (Save Our Homes). File by March 1 of the year after you move in; you must own and occupy by January 1.",
    "new_construction": "Your first tax bill is usually based on the land only if the home was not complete on January 1. Lenders escrow on the full value, so the second-year jump surprises people.",
}

INSURANCE = {
    "note": "Homes are built to the current Florida Building Code with impact glass or shutters and reinforced block first floors (developer materials), which earns wind-mitigation credits. Budget roughly $2,500 to $7,000 per year for a single-family home depending on coverage, elevation and features; get a real quote before contract.",
    "flood": "FEMA's National Flood Hazard Layer (FIRM panel 12081C0284F, effective Aug 10, 2021) shows the interior of the site as Zone X, minimal flood hazard, with 0.2%-annual-chance and coastal AE/VE zones west of 86th Street toward Palma Sola Bay and isolated Zone A pockets near the 75th Street edge. Confirm your specific lot on Manatee County's flood map; Zone X policies are optional and inexpensive.",
}

SCHOOLS = [
    ("Sea Breeze Elementary", "3601 71st St W, Bradenton", "listed by every builder"),
    ("W. D. Sugg Middle", "5602 38th Ave W, Bradenton", "listed by Pulte and Cardel"),
    ("Electa Lee Magnet Middle", "4000 53rd Ave W, Bradenton", "listed by David Weekley (magnet program)"),
    ("Bayshore High", "5401 34th St W, Bradenton", "listed by every builder"),
]
SCHOOLS_NOTE = "Builders disagree on the middle school. Confirm the assigned zone for a specific address with the Manatee County School District locator before you rely on it. IMG Academy is adjacent to the community."

DRIVE_TIMES = [
    ("Bradenton Beach", "8 min"), ("HCA Florida Blake Hospital", "8 min"), ("Coquina Beach", "12 min"), ("Longboat Key", "18 min"),
    ("Ringling Museum", "18 min"), ("Anna Maria Bayfront Park", "24 min"), ("Selby Gardens", "24 min"), ("Van Wezel Performing Arts Hall", "24 min"), ("Mote Marine", "30 min"),
]
DRIVE_TIMES_SOURCE = "Drive times as published by Cardel Homes for its SeaFlower sales center; typical off-peak traffic."

BUILDERS_SUMMARY = [
    {"slug": "mi-homes", "name": "M/I Homes", "tier": "Entry", "product": "Townhomes (Row Homes) and twin villas (Village Homes)", "lots": "Attached, Phase N1", "sqft": "1,486–2,406", "beds": "2–3", "price": "Priced from $399,999", "office": "8015 SeaFlower Pkwy"},
    {"slug": "pulte-homes", "name": "Pulte Homes", "tier": "Entry to mid", "product": "Single-family in the Scenic, Veranda and Distinctive series", "lots": "42' to 50'", "sqft": "1,405–2,369+", "beds": "2–5", "price": "From $404,990", "office": "7634 Addison Ave."},
    {"slug": "david-weekley-homes", "name": "David Weekley Homes", "tier": "Mid", "product": "Bungalow Homes (rear-load) and Classic Homes", "lots": "45' and 60'", "sqft": "1,615–3,777", "beds": "2–5", "price": "From the $500s (Bungalow) and the $600s (Classic)", "office": "7635 Addison Ave."},
    {"slug": "cardel-homes", "name": "Cardel Homes", "tier": "Upper", "product": "Cottage and Classic single-family, natural gas, ADU options", "lots": "50' and 60'", "sqft": "1,909–3,122", "beds": "3–5", "price": "From the $500s", "office": "4521 Flower Fields Trail"},
    {"slug": "issa-homes", "name": "Issa Homes", "tier": "Estate", "product": "Estate homes on lakefront lots", "lots": "80'", "sqft": "2,905–3,474+", "beds": "3–5", "price": "From $1,250,000, excluding homesite premium", "office": "Hemingway model, SeaFlower"},
]

SOURCES_COMMUNITY = [
    ("SeaFlower community overview and FAQ", "https://seaflower.com/community/", "Sep 3, 2026"),
    ("SeaFlower Phase One site plan (PDF, April 2026)", "https://seaflower.com/wp-content/uploads/SeaFlower-Phase1-Sitemap_040826.pdf", "Apr 2026"),
    ("The Garden Club groundbreaking release", "https://seaflower.com/seaflower-breaks-ground-on-the-garden-club-amenity-center-in-bradenton/", "Jul 14, 2025"),
    ("CASTO: Village Center groundbreaking", "https://castoinfo.com/news/casto-and-redstone-investments-to-break-ground-on-seaflower-village-center-in-bradenton-florida/", "Sep 10, 2025"),
    ("Village Center tenants (Bradenton Herald via seaflower.com)", "https://seaflower.com/whats-coming-to-this-new-bradenton-shopping-center/", "Sep 22, 2025"),
    ("Strong demand drives expansion (784 of 1,063 lots released)", "https://seaflower.com/strong-demand-is-driving-expansion-at-seaflower-in-west-bradenton/", "Apr 10, 2026"),
    ("RCLCO mid-year 2026 rankings", "https://www.rclco.com/publication/the-top-selling-master-planned-communities-of-mid-year-2026/", "Jul 30, 2026"),
    ("WUSF: ADU rules at SeaFlower", "https://www.wusf.org/politics-issues/2026-02-05/granny-flats-bradenton-community-home-design-legislature-could-make-more-common", "Feb 5, 2026"),
    ("Lake Flores CDD FY2027 proposed budget", "https://lakeflorescdd.net/_assets/documents/fy-2027/2027-LFCDD-budget-proposed.pdf", "May 2026"),
    ("Lake Flores CDD FY2026 adopted budget", "https://lakeflorescdd.net/_assets/documents/fy-2026/2026-LFCDD-budget.pdf", "2025"),
    ("SeaFlower HOA and CDD information sheet", "https://online.flippingbook.com/view/1053165353/1/", "Dec 8, 2025"),
    ("Pulse of Manatee: residents begin moving in", "https://www.pulseofmanatee.com/p/residents-begin-moving-into-seaflower", "Nov 3, 2025"),
    ("Business Observer: master-planned community starts blooming", "https://www.businessobserverfl.com/news/2025/oct/31/seaflower-development-bradenton/", "Oct 31, 2025"),
]

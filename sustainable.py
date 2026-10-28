"""Sustainable-landscape service pages (2026-10-27, from Ty's handoff).

Four pages: permaculture (hub), native habitat, food forests, natural pools.
Copy comes from ~/projects/terramorph/04-marketing/ty-sustainable-handoff-2026-10-27/
and only states facts from its research/facts-sourced.md. Photos are credited
public-domain / CC reference photos, never shown as Terramorph work. No AI
illustrations. No prices, certifications, project counts, partnerships or rebates.

build_pages.py imports this module and calls build(globals()) after the other
service pages are written; svc_v2.py lays the pages out in the v2 design.
"""

PERMACULTURE = 'permaculture-design-toledo-ohio.html'
NATIVE = 'native-landscaping-toledo-ohio.html'
FOOD_FOREST = 'food-forest-edible-landscaping-toledo-ohio.html'
POOLS = 'natural-swimming-pools-ponds-ohio.html'
FILES = [PERMACULTURE, NATIVE, FOOD_FOREST, POOLS]

# (file, short label, blurb) - used by the homepage band, footer group and services hub.
LINKS = [
    (PERMACULTURE, 'Permaculture design', 'Whole-property plans that work with water, soil and sun.'),
    (NATIVE, 'Native habitat and pollinator gardens', 'Native beds, meadows, rain gardens and invasive removal.'),
    (FOOD_FOREST, 'Food forests and edible gardens', 'Fruit and nut trees, berry patches, kitchen gardens.'),
    (POOLS, 'Natural pools, ponds and water features', 'Chemical-free swim ponds, wildlife ponds, waterfalls.'),
]

# Credit lines. The CC BY 3.0 pond photo legally needs its credit near the image.
_CREDIT = {
    'ref-native-pollinator-garden': 'Photo: Courtney Celley/USFWS (public domain)',
    'ref-monarch-milkweed': 'Photo: Tom Koerner/USFWS (public domain)',
    'ref-chipmunk-leaves': 'Photo: Courtney Celley/USFWS (public domain)',
    'ref-blueberries': 'Photo: Mark Ehlenfeldt, USDA ARS (public domain)',
    'ref-agroforestry-rows': 'Photo: Krisann McElvain, USDA NRCS (public domain)',
    'ref-mushroom-log': 'USDA photo by Lance Cheung (public domain)',
    'ref-raised-bed-greens': 'USDA photo by Lance Cheung (public domain)',
    'ref-vegetable-garden-hoops': 'NRCS photo by Carly Whitmore (public domain)',
    'ref-forest-floor-logs': 'Photo: Tina Shaw/USFWS (public domain)',
    'ref-rain-garden-river-rock': 'U.S. Army photo by Elizabeth Fraser (public domain)',
    'ref-river-wetlands-aerial': 'Photo: Steve Hillebrand/USFWS (public domain)',
    'ref-natural-swimming-pond': 'Photo: Peter Funk via Wikimedia Commons (public domain)',
    'ref-wildlife-pond-lilies': 'Photo: Mshort1803, CC BY 3.0',
    'ref-soil-ribbon-test': 'Photo: USDA NRCS Iowa (public domain)',
}
NOT_OURS = 'Reference photo, not a Terramorph project.'


def media(stem, alt, what):
    """(src, alt, caption) for a chapter figure. Caption says what it is and who shot it."""
    return (f'assets/{stem}.webp', alt, f'{what} {NOT_OURS} {_CREDIT[stem]}')


def hero_credit(stem):
    return f'{NOT_OURS} {_CREDIT[stem]}'


AREA = 'Perrysburg, Toledo, Maumee, Sylvania, Waterville, Whitehouse, Holland, Monclova, Rossford, Oregon, Bowling Green and the rest of Wood and Lucas County'

# ---------------------------------------------------------------------------
# FAQs (visible text and FAQPage JSON-LD are the same strings)
# ---------------------------------------------------------------------------
FAQS = {
    'Permaculture Design': [
        ('What is permaculture design?', 'Permaculture is a way of designing a landscape so it works like a natural system: it catches and stores water, builds soil, mixes plants that help each other, and makes room for wildlife. Unlike a traditional yard of lawn and shrubs, it is designed to produce food, habitat or both, with less mowing and watering over time.'),
        ('What does a permaculture designer do?', 'A permaculture designer studies your property first (water flow, soil, sun, wind and how you use the space) and then lays out zones, water features, plantings and paths that work together. Terramorph also installs the design with our own crews.'),
        ('How much does a permaculture design cost?', 'It depends on the size of the property and how much you want installed at once. Terramorph starts with a free estimate, then prices the design and the installation phases separately so you can build in stages.'),
        ("Does permaculture work in Ohio's clay soil and zone 6b winters?", "Yes, if it's designed for them. On Northwest Ohio clay we test drainage before digging swales, use rain gardens with compost-amended soil, and choose plants proven in zone 6b and heavy soil."),
        ('Can I do permaculture on a small yard or a front yard?', 'Yes. Small lots often get the most out of it: a rain garden for the downspout, a few fruit trees with companion plants, native beds and a kitchen garden. In front yards we keep clean edges and a clear layout so it looks designed and fits neighborhood expectations.'),
        ('Is permaculture the same as a food forest?', 'No. A food forest is one thing a permaculture design can include: a layered planting of fruit and nut trees, shrubs and ground covers. Permaculture is the whole-property plan, including water, soil, habitat and how you live in the space.'),
        ('Do you install the design or just draw it?', 'Both. Terramorph designs the property and our crews install it, from grading and drainage to planting, mulch and paths, then we follow up while it establishes.'),
        ('How long until a permaculture yard is productive and low-maintenance?', 'Water features and beds work right away. Perennials fill in over the first two to three growing seasons, and fruit and nut trees take several years to bear. Weeding and watering are heaviest in the first seasons and drop as plants close in.'),
        ('Is permaculture sustainable and regenerative?', "That's the goal: a permaculture yard holds rainwater on site, builds soil with compost and mulch, supports pollinators and birds, and cuts down on mowing, watering and fertilizer."),
    ],
    'Native Landscaping': [
        ('How much does native landscaping cost?', 'It depends on the size of the area, site prep (removing lawn or invasives, soil and drainage work), plant sizes and whether you want an establishment-care plan. Terramorph gives free estimates and can phase larger projects over several seasons.'),
        ('Are native gardens really low maintenance?', 'Lower, not zero. The first one to two seasons need watering and weeding while roots establish. By the third season most beds fill in, weeding drops and they need far less water, mowing and fertilizer than lawn.'),
        ('Will a native garden look messy or get me a weed notice?', "Not when it's designed. Clean bed edges, mown borders or paths, plants grouped in drifts and a clear layout make native gardens read as intentional. We design front-yard native beds with neighbors and city expectations in mind."),
        ('How big should a rain garden be, and how deep?', 'It depends on the roof or driveway area draining to it and how fast your soil absorbs water. On Northwest Ohio clay we run a percolation test, keep the basin shallower, and mix compost into the top few inches so water soaks in within a few days.'),
        ('Do rain gardens attract mosquitoes?', 'A properly built rain garden drains within a few days, and mosquitoes need standing water for about a week to develop from egg to adult. If water stands longer than that, the design needs adjusting, and we check that during establishment.'),
        ('Can you convert part of my lawn to a meadow or native garden?', 'Yes. Most properties do best with a mix: lawn where you play and walk, and native beds or meadow in low-use areas, edges and wet spots. We remove the turf, prepare the soil, plant, and leave clean edges and paths.'),
        ('Which plants are native to Northwest Ohio?', "It depends on your soil. Clay sites suit plants like swamp milkweed, switchgrass, coneflowers and native asters. The sandy Oak Openings area west of Toledo has its own palette, like wild lupine, which won't grow in clay. We match plants to your site."),
        ('When is the best time to plant a native or pollinator garden in Ohio?', 'Spring and fall are both good. Fall planting lets roots grow in cool, moist soil, and many native seeds need a winter to sprout. Spring planting works well for potted plants with good follow-up watering.'),
        ('Can you remove invasive honeysuckle and buckthorn?', "Yes. We cut and treat invasive shrubs like bush honeysuckle and buckthorn, haul them away, check for resprouts, and replant with native shrubs so the area doesn't fill back in with invasives."),
        ('Do you work with clay soil and wet yards?', "Yes. Most of our area is heavy clay from the old Great Black Swamp. We choose plants that tolerate wet clay, use rain gardens where they fit, and handle regrading or drainage when that's the real fix."),
    ],
    'Food Forests and Edible Landscaping': [
        ('How much does a food forest or edible landscape cost?', 'It depends on the number and size of trees and shrubs, soil and drainage prep, and how many layers you plant at once. Terramorph gives a free estimate and can phase the project, starting with trees and shrubs and adding lower layers later.'),
        ('What fruit trees grow well in Northwest Ohio?', 'In our zone 6b climate, apples and pears (with a pollination partner), pawpaw, American persimmon, serviceberry and elderberry all do well when planted in well-drained spots. We pick varieties for your soil and space.'),
        ('Which nut trees can I grow in Ohio?', 'Hazelnuts and chestnuts are good choices for home plantings. Both need at least two compatible plants for pollination, and for chestnuts we use Chinese or blight-resistant hybrid trees.'),
        ('How long until a food forest produces fruit?', 'Vegetables and herbs produce the first season. Berries like elderberry give a light crop in the second year and a full crop by years three to four. Grafted pawpaw and persimmon trees often take three to six years.'),
        ('How much space do I need?', 'Less than most people think. A small yard can hold a couple of fruit trees with companion plants, a berry hedge and raised beds. Larger lots can hold a full layered food forest.'),
        ('What is a food forest guild?', 'A guild is a group of plants placed around a fruit tree where each one helps: nitrogen fixers like clover, flowers that attract pollinators, bulbs that hold back grass, and mulch plants like comfrey.'),
        ("What's the difference between a food forest and permaculture?", 'A food forest is a layered edible planting. Permaculture is the bigger design approach for the whole property, including water, soil, habitat and how you use the space. A food forest is often one part of a permaculture design.'),
        ('Do you install raised garden beds and kitchen gardens?', "Yes. We design and build raised beds and vegetable gardens, fill them with quality soil, and place them close to the house where they're easy to use and water."),
        ('Will fruit trees attract deer and rabbits?', 'They can. We use tree guards and fencing where needed, and choose and place plants to reduce browsing.'),
        ('Can you maintain and prune the fruit trees?', 'Yes. We offer care plans for establishment watering, mulching and pruning so young trees get off to a strong start.'),
    ],
    'Natural Swimming Pools and Ponds': [
        ('How much does a natural swimming pool cost in Ohio?', 'Every natural pool is custom, so cost depends on size, the swim-to-plant-zone split, excavation and soil, liner and edging, pumps and planting. Terramorph gives a free estimate and a clear scope for your site.'),
        ('How does a natural swimming pool work?', 'Water moves between a swimming zone and a shallow planted regeneration zone. Settling, microbes in the gravel, plant roots and a natural biofilm clean the water, so no chlorine is used. Many designs use a small pump to keep water circulating through the plants.'),
        ('Are natural swimming pools clean and safe to swim in?', "A well-designed and well-maintained natural pool has clear, clean water, but it's a living system, so it needs regular water testing and care. Chlorine-free doesn't mean maintenance-free."),
        ('What happens to a natural pool in an Ohio winter?', 'It freezes over like any pond. Plants go dormant, pumps are winterized or kept running depending on the design, and the pool comes back to life in spring.'),
        ('Do natural swimming pools attract mosquitoes?', "Mosquitoes need still water to breed, and their larvae can't develop in moving water. Circulation, waterfalls and native fish that eat larvae keep mosquitoes down."),
        ('How big does a natural swimming pool need to be?', "It needs room for both the swimming zone and the planted regeneration zone. In plant-driven designs the planted zone is often around half the surface area, while designs with more filtration equipment can be more compact. We size it to your yard and how you'll use it."),
        ('How much maintenance does a natural pool need?', 'Skimming leaves, trimming plants, checking the pump, regular water testing, and spring start-up and fall shutdown. We offer seasonal care plans.'),
        ('Can you convert my existing chlorine pool to a natural pool?', "Sometimes. It depends on the pool's shape, condition and the space around it for a regeneration zone. We'll assess it and tell you honestly whether conversion or a new build makes more sense."),
        ("What's the difference between a natural pool, a swim pond and a wildlife pond?", 'A natural pool has a defined swimming zone and a planted filter zone. A swim pond is larger and more pond-like, built for both swimming and wildlife. A wildlife pond is built for frogs, birds and insects, not for swimming.'),
        ('Why choose a pondless waterfall?', 'You get the sound and look of moving water without an open pond, since the water recirculates from a hidden underground basin. It takes less space and is a good fit for homes with young children.'),
        ('Do I need a permit or a fence?', 'It depends on your city or township, because Ohio leaves pool barrier rules to local codes. Terramorph checks your local zoning, fence and permit requirements before we build.'),
    ],
}

# Short answer card under each hero (what Google and AI assistants quote first).
ANSWERS = {
    PERMACULTURE: 'Terramorph designs and installs permaculture landscapes for homes in Perrysburg, Toledo, Maumee, Sylvania and across Wood and Lucas County, Ohio: rain gardens and water-smart grading, food-producing beds and fruit trees, native habitat and soil building, planned for heavy clay and zone 6b winters. One local crew draws the plan and builds it in phases. Estimates are free.',
    NATIVE: 'Terramorph designs and installs native plant gardens, pollinator habitat, meadows, rain gardens and invasive-plant replacements for homes across Wood and Lucas County, Ohio. Plants are matched to your soil (Black Swamp clay or Oak Openings sand), beds get clean edges and a clear layout so they look designed, and we offer establishment care for the first seasons. Estimates are free.',
    FOOD_FOREST: 'Terramorph designs and installs food forests, fruit and nut trees, berry patches, kitchen gardens and raised beds for homes in Perrysburg, Toledo and across Wood and Lucas County, Ohio. Varieties and pollination partners are chosen for zone 6b and clay soil, trees go in well-drained spots, and projects can be phased, starting with trees and shrubs. Estimates are free.',
    POOLS: 'Terramorph designs and builds natural swimming pools, swim ponds, wildlife ponds, pondless waterfalls and bog filters for homes across Wood and Lucas County, Ohio. Plants, gravel and microbes clean the water instead of chlorine, the system is built for Ohio winters and Northwest Ohio clay, and we check local permit and barrier rules before building. Estimates are free.',
}

# ---------------------------------------------------------------------------
# Page specs
# ---------------------------------------------------------------------------
PAGES = [
    {
        'file': PERMACULTURE,
        'title': 'Permaculture Design',
        'service_name': 'Permaculture Design and Installation',
        'extra_services': [],
        'seo_title': 'Permaculture Design &amp; Installation Toledo, OH | Terramorph',
        'seo_desc': 'Permaculture yard design and installation in Toledo, Perrysburg and NW Ohio: water harvesting, food forests, native habitat, clay-soil fixes. Free quote.',
        'crumb': 'Permaculture Design',
        'eyebrow': 'Sustainable landscape design and installation',
        'image': 'ref-rain-garden-river-rock.webp',
        'hero_alt': 'Rain garden of native grasses and black-eyed Susans with a river-rock edge beside a path',
        'hero_credit': hero_credit('ref-rain-garden-river-rock'),
        'headline': 'Permaculture Design &amp; Installation in Toledo and Northwest Ohio',
        'lead': 'Permaculture is landscape design that works with water, soil, sun and plants instead of fighting them. Terramorph designs it and our crews install it: rain gardens, food-producing beds, native habitat and water-smart grading, built for Northwest Ohio clay.',
        'problem': 'The yard takes constant mowing, watering and fixing, floods every spring, and gives almost nothing back.',
        'outcome': 'A yard that holds its own water, feeds pollinators and your family, and needs less work every year.',
        'cta': 'Plan My Permaculture Yard',
        'process': ('Our process', 'Permaculture starts with watching the site, not with a plant list. Here is how a Terramorph project runs from the first call to the follow-up visit.', [
            ('Consult and site walk', 'Your goals, how you use the yard, budget and timeline.'),
            ('Site analysis', 'Water flow, soil and percolation test, sun, wind, existing plants and access.'),
            ('Design', 'A layout you can react to, with zones, water plan, planting plan and phases.'),
            ('Phased install', 'Start with water and soil, then trees and shrubs, then the layers that fill in.'),
            ('Follow-up', 'Establishment watering, weeding and a seasonal check-in plan.'),
        ]),
        'chapters': [
            {'eyebrow': 'Design and build', 'h2': 'Permaculture design, built by a local landscaping crew',
             'paras': ['Most permaculture designers draw a plan and hand it to you. Terramorph does both halves: we design the property, then our crews install it, from grading and drainage to planting and mulch, and we come back to check how it is settling in. You get one team that understands the plan because they wrote it.',
                       "Permaculture isn't a style or a plant list. It's a way of designing. The word was coined in Tasmania in the mid-1970s by Bill Mollison and David Holmgren, and it has grown into a set of design principles used on farms, schools and backyards around the world. The goal is simple: a landscape that works like a natural system, so it keeps producing with less input from you."],
             'media': media('ref-soil-ribbon-test', 'Hand pressing a soil ribbon to test texture beside rows of young corn', 'A soil ribbon test: the design starts with what the ground is actually doing.')},
            {'eyebrow': 'What it means', 'h2': 'What permaculture means for a Toledo-area yard',
             'paras': ['In plain English, a permaculture design answers five questions about your property. Good design starts with watching the site before building anything: where the water goes after a storm, which way the wind comes from, and where the sun falls in June versus December.'],
             'cards': [('Water', 'Where does rain land, where does it run, and how do we slow it down and soak it in instead of sending it to the street?'),
                       ('Soil', 'What is the soil doing now, and how do we build it up instead of stripping it every year?'),
                       ('Zones', 'What do you use every day, and what can be left a little wilder? Permaculture places things by how often you visit them, from the kitchen herbs by the back door (Zone 1) to vegetable beds (Zone 2), fruit trees and berry shrubs (Zone 3), and a quiet wild corner for wildlife (Zone 5).'),
                       ('Plants', 'Which plants can do more than one job? A fruit tree "guild" surrounds a tree with companions that each help: clover to add nitrogen, flowers to bring in bees, bulbs to hold back grass.'),
                       ('Habitat', 'How do we make room for the bees, birds and beneficial insects that do a lot of the pest control for free?')]},
            {'eyebrow': 'Built for here', 'h2': 'Designing for Northwest Ohio: clay, wet springs and zone 6b',
             'paras': ['Permaculture advice online is often written for somewhere else. Northwest Ohio has its own rules, and we design for the soil you actually have. See <a href="best-plants-for-ohio-clay-soil.html">best plants for Ohio clay soil</a>.'],
             'cards': [('Heavy clay', 'Much of Wood and Lucas County sits on the old Great Black Swamp. Clay soils like the Hoytville series, which was first described right here in Wood County, drain very slowly. That changes how we handle water and which plants we choose.'),
                       ('Wet springs, dry Augusts', 'Yards here often sit soggy in April and bake by midsummer, so designs have to handle both.'),
                       ('Zone 6b winters', 'Perrysburg and Toledo are in USDA hardiness zone 6b on the 2023 map, so plants have to handle average winter lows of -5 to 0 &deg;F.'),
                       ('Sand pockets', 'West of Toledo, the Oak Openings region is sandy and drains fast. Plants that thrive there can fail on clay a few miles away.')]},
            {'eyebrow': 'Water first', 'h2': 'Water first: rain gardens, swales and drainage on clay',
             'paras': ['Permaculture is famous for swales, shallow ditches on contour that slow water so it soaks in. On our clay, a swale dug without testing can just make a long puddle. So we test first. We run a simple percolation test (dig a hole, fill it, check how fast it drains), then pick the right tool.',
                       'Rain gardens stay at least 10 feet from foundations and away from septic systems, and every dig starts with an OHIO811 utility locate.'],
             'cards': [('Rain gardens', 'For roof and driveway runoff: shallow planted basins that soak water in within a few days. On clay we make them shallower and mix 2 to 6 inches of compost into the top layer.'),
                       ('Swales and berms', 'Only where the soil test says water will actually soak in.'),
                       ('Conventional drainage', "Where it's the honest answer. Sometimes a French drain or regrading is the right first step. See <a href=\"drainage-solutions.html\">drainage solutions</a>."),
                       ('Rainwater harvesting', 'One inch of rain on 1,000 square feet of roof is about 623 gallons, and the design decides where that water goes.')],
             'media': media('ref-river-wetlands-aerial', 'Aerial view of a river meandering through green and gold wetlands', 'Water slowed and spread across a wetland, the pattern swales and rain gardens copy at yard scale (Selawik refuge, Alaska).')},
            {'eyebrow': 'What we build', 'h2': 'What we design and install',
             'paras': ['A permaculture plan pulls together several things we build. Each one has its own page.'],
             'cards': [('Native habitat and pollinator gardens', 'Native plant beds, meadows, rain gardens and invasive plant removal. See <a href="native-landscaping-toledo-ohio.html">native habitat design and installation</a>.'),
                       ('Food forests and edible gardens', 'Fruit and nut trees, berry shrubs, guilds, kitchen gardens and raised beds. See <a href="food-forest-edible-landscaping-toledo-ohio.html">food forests and edible landscaping</a>.'),
                       ('Natural pools, ponds and water features', 'Wildlife ponds, swim ponds and chemical-free natural swimming pools. See <a href="natural-swimming-pools-ponds-ohio.html">natural swimming pools and ponds</a>.'),
                       ('Soil building', 'Compost, mulch and plantings that feed the soil instead of stripping it.'),
                       ('Hardscape that fits the plan', 'Paths, seat walls and patios placed where the design needs them. See <a href="paver-patios-hardscapes.html">paver patios and hardscapes</a>.')],
             'media': media('ref-forest-floor-logs', 'Decaying logs, ferns and fallen leaves building soil on a forest floor', "Nature's soil-building model: logs, leaves and ferns feeding a forest floor. Soil building copies this with compost and mulch.")},
            {'eyebrow': 'Small lots', 'h2': 'Front yards, small lots and neighborhoods with rules',
             'paras': ['Permaculture works on a small suburban lot, not just acreage. The key in town is making it look intentional: clean bed edges, a mown path or border, plants grouped in drifts, and a clear front-yard design so it reads as a garden, not neglect. We keep lawn where it has a job (play, pets, paths) and plant the rest. See <a href="native-plants-vs-lawn-ohio.html">native plants vs. lawn</a>.'],
             'media': media('ref-native-pollinator-garden', 'Native pollinator garden with purple coneflowers, prairie clover and black-eyed Susans in full summer bloom', 'Natives grouped in drifts read as a garden, not a vacant lot.')},
            {'eyebrow': 'Why it matters', 'h2': 'The values behind it',
             'paras': ["Permaculture is built on three simple ethics: care for the earth, care for people, and share the surplus. For a homeowner that means a yard that costs less to keep up, gives back food and habitat, and does its part for local water. In our area that matters: runoff carrying phosphorus into the Maumee River feeds Lake Erie's summer algae blooms, the same blooms that shut down Toledo's tap water in August 2014. Yards that soak in rain and skip excess fertilizer are a small part of the fix."]},
            {'eyebrow': 'Where we work', 'h2': 'Permaculture design and installation across Wood and Lucas County',
             'paras': [f'Permaculture design and installation across {AREA}. Free estimates: 419-873-6801. Start with <a href="landscape-design.html">landscape design</a> if you want the whole property planned, and see <a href="financing.html">financing</a> for larger phased projects.'],
             'links': [('native-landscaping-toledo-ohio.html', 'Native habitat and pollinator gardens'),
                       ('food-forest-edible-landscaping-toledo-ohio.html', 'Food forests and edible landscaping'),
                       ('natural-swimming-pools-ponds-ohio.html', 'Natural swimming pools and ponds'),
                       ('drainage-solutions.html', 'Drainage solutions'),
                       ('best-plants-for-ohio-clay-soil.html', 'Best plants for Ohio clay soil'),
                       ('native-plants-vs-lawn-ohio.html', 'Native plants vs. lawn'),
                       ('landscape-design.html', 'Landscape design'),
                       ('process.html', 'How we work')]},
        ],
    },
    {
        'file': NATIVE,
        'title': 'Native Landscaping',
        'service_name': 'Native Landscaping Design and Installation',
        'extra_services': ['Pollinator Garden Installation', 'Rain Garden Installation', 'Lawn-to-Meadow Conversion', 'Invasive Plant Removal'],
        'seo_title': 'Native Landscaping &amp; Pollinator Gardens Toledo | Terramorph',
        'seo_desc': 'Native plant gardens, pollinator habitat, meadows and rain gardens designed and installed in Toledo, Perrysburg and NW Ohio. Local natives, clay-ready.',
        'crumb': 'Native Landscaping',
        'eyebrow': 'Native gardens, pollinator habitat and rain gardens',
        'image': 'ref-native-pollinator-garden.webp',
        'hero_alt': 'Native pollinator garden with purple coneflowers, prairie clover and black-eyed Susans in full summer bloom',
        'hero_credit': hero_credit('ref-native-pollinator-garden'),
        'headline': 'Native Habitat Design &amp; Installation in Toledo and Northwest Ohio',
        'lead': 'Native gardens that look designed, not abandoned. Terramorph plans and installs native plant beds, pollinator habitat, meadows and rain gardens with plants that belong in Northwest Ohio and can handle our clay.',
        'problem': 'The yard is all lawn and shrubs that feed nothing, need constant mowing, and leave water standing after every rain.',
        'outcome': 'Clean, intentional native beds full of bees, butterflies and birds that need less mowing, watering and fertilizer once established.',
        'cta': 'Plan My Native Garden',
        'chapters': [
            {'eyebrow': 'Designed, not abandoned', 'h2': 'Native gardens that look designed, not abandoned',
             'paras': ['The biggest worry we hear about native plants is "will it look messy?" It does not have to. A native garden reads as intentional when it has clean bed edges, a mown border or path, plants grouped in drifts instead of scattered singles, and a plan for every season. That is the difference between a designed native landscape and a vacant lot, and it is the part we specialize in.']},
            {'eyebrow': 'Why it matters here', 'h2': 'Why native plants matter here',
             'paras': ["Native plants aren't just a look. They're the base of the local food web. North America has about 2.9 billion fewer birds than in 1970. A yard won't fix that alone, but a neighborhood of native yards adds real habitat back."],
             'cards': [('Caterpillars feed birds', 'Raising one brood of chickadees takes an estimated 6,000 to 9,000 caterpillars, and most caterpillars can only eat the native plants they evolved with.'),
                       ('A few plants do the heavy lifting', 'Native oaks support the caterpillars of 557 species of moths and butterflies, and black cherry 456. Non-native ginkgo and zelkova support none. Research shows just 14% of native plant groups support more than 90% of caterpillar species, so choosing the right "keystone" plants matters more than planting a lot.'),
                       ('Yards can make or break a bird population', 'In a study of suburban yards, chickadees sustained their population only where more than 70% of the plants were native.'),
                       ("Ohio's bees need ground", 'Ohio has an estimated 400 to 450 bee species. Most native bees live alone rather than in hives, and about 70% of them nest in bare, well-drained soil, so good habitat leaves some sunny ground open.')],
             'media': media('ref-monarch-milkweed', 'Monarch butterfly feeding on pink showy milkweed flowers, a host plant for monarch caterpillars', 'A monarch on milkweed, the only plant its caterpillars can eat.')},
            {'eyebrow': 'What we build', 'h2': 'What we design and install',
             'paras': ['Every project starts with how tidy you want it to look and what the site can support. Thinking about a larger property? Read <a href="native-prairie-landscaping-ohio.html">native prairie landscaping in Ohio</a> and <a href="native-plants-vs-lawn-ohio.html">native plants vs. lawn</a>.'],
             'cards': [('Native plant gardens', 'Front and backyard beds built from native perennials, grasses and shrubs, chosen for your sun, soil and how tidy you want it to look.'),
                       ('Pollinator habitat', 'Bloom from spring through fall, host plants like milkweed for monarchs, and sunny bare patches for ground-nesting bees.'),
                       ('Meadows and lawn conversions', 'Turn low-use lawn into a native meadow or prairie-style planting, with mown paths and clean edges.'),
                       ('Rain gardens', 'Shallow planted basins that catch roof and driveway runoff and soak it into the ground within a few days.'),
                       ('Invasive plant removal and replanting', "We clear bush honeysuckle, buckthorn, Callery (Bradford) pear and other invasives, then replant with natives so they don't come straight back.")],
             'media': media('ref-chipmunk-leaves', 'Eastern chipmunk foraging in fallen leaves among young seedlings', 'Leaf litter left under shrubs is habitat too: a chipmunk foraging among seedlings.')},
            {'eyebrow': 'Built for here', 'h2': 'Built for Northwest Ohio: Black Swamp clay, Oak Openings sand and zone 6b',
             'paras': ['Two very different native palettes live within a few miles of each other here. We plan for the soil you actually have and for zone 6b winters (USDA 2023 map). See <a href="best-plants-for-ohio-clay-soil.html">best plants for Ohio clay soil</a>.',
                       'Deep roots help on clay too: native prairie grasses like switchgrass can reach 8 to 11 feet deep and big bluestem 6 to 7 feet, opening paths for water that lawn grass never reaches.'],
             'cards': [('Clay country', 'Most of Wood and Lucas County, the old Great Black Swamp: plants that handle slow drainage and wet springs, like swamp milkweed ("a good plant for wet, even mucky, clay soil if there is sufficient sun," per OSU Extension) and switchgrass, which tolerates poorly drained soil and occasional flooding.'),
                       ('Oak Openings sand', "West of Toledo: fast-draining sand over clay, home to about a third of Ohio's state-listed rare plants and animals. Plants like wild lupine thrive there but hate clay.")]},
            {'id': 'rain-gardens', 'eyebrow': 'Rain gardens', 'h2': 'Rain gardens for wet yards and downspouts',
             'paras': ["A rain garden is a shallow, planted basin that catches runoff from a roof or driveway and lets it soak in, usually within a few days. It isn't a pond. Done right on clay, it means a few things.",
                       "Rain gardens are one drainage tool. When a yard needs regrading or a French drain instead, we'll tell you. See <a href=\"drainage-solutions.html\">drainage solutions</a>."],
             'cards': [('A percolation test first', 'We check how fast your soil actually absorbs water before sizing the basin.'),
                       ('A shallower basin on clay', 'With 2 to 6 inches of compost mixed into the soil so water soaks in.'),
                       ('Placed safely', 'At least 10 feet from the foundation, away from septic systems, and not on steep slopes.'),
                       ('The right plants', 'Plants that handle both standing water and summer drought.')],
             'media': media('ref-rain-garden-river-rock', 'Rain garden of native grasses and black-eyed Susans with a river-rock edge beside a path', 'A planted rain garden with a river-rock edge: runoff soaks in within days instead of standing on the lawn.')},
            {'eyebrow': 'Invasives', 'h2': 'Invasives: what to remove first',
             'paras': ["Ohio bans the sale and propagation of 63 invasive plants, including bush honeysuckle, common buckthorn, garlic mustard, autumn olive, tree-of-heaven and Callery pear (banned from sale since January 2023). Bush honeysuckle is the big one locally: it leafs out earlier and holds its leaves later than native shrubs, shading out wildflowers and young trees, and its berries lack the fat migrating birds need. It's best cut in early summer, and treated stumps need watching for at least a year. You're not required to remove existing plants, but replacing them with natives is one of the biggest habitat upgrades a yard can get."]},
            {'eyebrow': 'Cost', 'h2': 'Cost and what affects it',
             'paras': ['Cost depends on the size of the area, how much prep it needs (removing lawn or invasives, soil work, drainage), plant sizes (plugs establish fast and cost less, larger pots look finished sooner), and whether you want an establishment-care plan. We give a free estimate and can phase larger conversions over two or three seasons.']},
            {'eyebrow': 'Establishment', 'h2': 'The first three years',
             'paras': ['Native gardens are lower-maintenance, not no-maintenance. We offer establishment care so the investment survives those first seasons.'],
             'cards': [('Year one', 'Watering and weeding while roots establish, and the plants look small.'),
                       ('Year two', 'They fill in and bloom more.'),
                       ('Year three', 'The bed closes in and weeding drops.')]},
            {'eyebrow': 'Where we work', 'h2': 'Native landscaping across Wood and Lucas County',
             'paras': [f'Native landscaping, pollinator gardens and rain gardens across {AREA}. Free estimates: 419-873-6801. Planning a whole-property approach? See <a href="permaculture-design-toledo-ohio.html">permaculture design</a>.'],
             'links': [('permaculture-design-toledo-ohio.html', 'Permaculture design'),
                       ('food-forest-edible-landscaping-toledo-ohio.html', 'Food forests and edible landscaping'),
                       ('natural-swimming-pools-ponds-ohio.html', 'Natural swimming pools and ponds'),
                       ('native-prairie-landscaping-ohio.html', 'Native prairie landscaping in Ohio'),
                       ('native-plants-vs-lawn-ohio.html', 'Native plants vs. lawn'),
                       ('drainage-solutions.html', 'Drainage solutions'),
                       ('best-plants-for-ohio-clay-soil.html', 'Best plants for Ohio clay soil'),
                       ('landscape-design.html', 'Landscape design')]},
        ],
    },
    {
        'file': FOOD_FOREST,
        'title': 'Food Forests and Edible Landscaping',
        'service_name': 'Food Forest and Edible Landscape Design and Installation',
        'extra_services': ['Fruit and Nut Tree Planting', 'Raised Garden Bed Installation'],
        'seo_title': 'Food Forest &amp; Edible Landscaping Toledo, OH | Terramorph',
        'seo_desc': 'Food forests, fruit and nut trees, kitchen gardens and raised beds designed and installed in Toledo, Perrysburg and NW Ohio. Zone 6b picks. Free quote.',
        'crumb': 'Food Forests &amp; Edible Landscaping',
        'eyebrow': 'Food forests, orchards and kitchen gardens',
        'image': 'ref-agroforestry-rows.webp',
        'hero_alt': 'Rows of young fruit shrubs and trees with squash growing between them in an agroforestry planting',
        'hero_credit': hero_credit('ref-agroforestry-rows'),
        'headline': 'Food Forest &amp; Edible Garden Design and Installation in Northwest Ohio',
        'lead': "A yard that feeds you. Terramorph designs and installs food forests, fruit and nut trees, berry patches, kitchen gardens and raised beds, with varieties and pollination partners chosen for Northwest Ohio's zone 6b and clay.",
        'problem': 'The yard costs time and money every week and gives nothing back but grass clippings.',
        'outcome': 'A layered, good-looking edible landscape that produces fruit, nuts, berries and vegetables for years, planted right the first time.',
        'cta': 'Plan My Food Forest',
        'chapters': [
            {'eyebrow': 'A yard that feeds you', 'h2': 'A yard that feeds you',
             'paras': ['A food forest is a planting designed like a woodland edge, except most of what grows in it is edible: fruit and nut trees overhead, berry shrubs below, herbs and perennial vegetables underneath, and ground covers holding the soil. Once established, it keeps producing year after year with far less work than an annual vegetable garden. Not every yard needs a full forest. Many projects are a few fruit trees with companion plantings, a berry hedge, or a set of raised kitchen beds by the back door.']},
            {'eyebrow': 'What we build', 'h2': 'What we design and install',
             'paras': ['Each piece can stand alone or be part of a bigger <a href="permaculture-design-toledo-ohio.html">permaculture design</a>.'],
             'cards': [('Food forests', 'Layered plantings of fruit and nut trees, shrubs, perennials and ground covers, designed so each layer helps the others.'),
                       ('Fruit and nut trees and backyard orchards', 'Apples, pears, pawpaws, persimmons, hazelnuts, chestnuts and more, with the right pollination partners and spacing.'),
                       ('Kitchen gardens and raised beds', "Raised beds and vegetable gardens placed close to the house where you'll actually use them, sized and built to last."),
                       ('Berry patches and edible borders', 'Elderberry, blueberries, serviceberry and other berry shrubs used as hedges, borders and foundation plantings.')],
             'media': media('ref-vegetable-garden-hoops', 'Productive vegetable garden with raised beds and tall hoop frames on a sunny day', 'Raised beds with hoop frames: the kitchen-garden layer of an edible landscape.')},
            {'eyebrow': 'Trees that grow here', 'h2': 'Fruit and nut trees that grow in Northwest Ohio',
             'paras': ["Perrysburg and Toledo are in USDA zone 6b (2023 map). The biggest mistakes we see aren't the wrong tree, they're missing pollination partners and wet planting spots. Here is what we plan for."],
             'cards': [("Pawpaw (Ohio's official state native fruit since 2009)", 'Needs at least two genetically different trees to fruit. Grafted trees can fruit 3 to 4 years after planting. Pawpaws want deep, well-drained soil, so on our clay we plant them on raised or well-drained spots. Few pests or diseases.'),
                       ('American persimmon', 'Trees are male or female and only females fruit, so you usually plant one of each. Grafted trees can fruit in 3 to 6 years.'),
                       ('Elderberry', 'Ohio State Extension suggests Ohio growers start with American elderberry varieties. A light crop in year 2 and a full crop in years 3 to 4. Planting several varieties together improves the harvest.'),
                       ('Apples and pears', "Most varieties need a different variety blooming at the same time within about 50 feet. Some, like 'Jonagold' and 'Mutsu', have sterile pollen and can't pollinate others. Flowering crabapples can serve as pollinators."),
                       ('Chestnuts', 'Almost all need a second variety nearby for wind pollination. Chestnut blight wiped out the American chestnut as a forest tree, so we plant Chinese or blight-resistant hybrid chestnuts.'),
                       ('Hazelnuts', 'Wind-pollinated; plant at least two compatible plants close together.'),
                       ('Black walnut neighbors', 'Black walnut produces juglone, which can harm sensitive plants, mainly tomatoes, potatoes, peppers and eggplant. If you have a walnut, we keep the vegetable garden away from it.')],
             'media': media('ref-blueberries', 'Clusters of ripe blue and ripening red blueberries on a bush', 'Blueberries: a berry-shrub layer that also gives great fall color.')},
            {'eyebrow': 'The layers', 'h2': 'How a food forest is layered',
             'paras': ['Food forests are often described in seven layers, a model developed by English gardener Robert Hart when he turned a small apple and pear orchard into a layered edible landscape.',
                       'Around each tree we build a "guild" of companions that each do a job: nitrogen fixers like clover, flowers that bring in pollinators, bulbs that hold back grass, and mulch plants like comfrey.'],
             'cards': [('Canopy', 'Larger fruit and nut trees.'),
                       ('Low trees', 'Dwarf fruit trees and small nut trees.'),
                       ('Shrubs', 'Currants, elderberry, blueberries and other berries.'),
                       ('Herbaceous layer', 'Perennial herbs and vegetables.'),
                       ('Ground cover', 'Low plants that protect the soil.'),
                       ('Root layer', 'Root crops.'),
                       ('Vines', 'Climbing plants like grapes and hardy kiwi.')],
             'media': media('ref-mushroom-log', 'Edible mushroom growing from a cultivation log in a shaded wood-chip garden', 'Shade has a job too: an edible mushroom fruiting from a log over wood-chip mulch.')},
            {'eyebrow': 'Front yards', 'h2': 'Edible front yards that still look neat',
             'paras': ['An edible landscape can be the best-looking yard on the street. Blueberries have great fall color, serviceberry flowers early, and a fruit tree with a neat mulched guild looks intentional. In front yards we keep clean edges, a clear layout and plants that look good in winter too.']},
            {'eyebrow': 'Cost and harvest', 'h2': "Cost, timeline and when you'll harvest",
             'paras': ['Cost depends on the number and size of trees, how much soil prep and drainage work the site needs, and how many layers you want planted at once. Many clients start with trees and shrubs (the slow growers) and add the lower layers later. We give a free estimate with a phased plan. Harvest timing is honest.'],
             'cards': [('Raised beds and vegetables', 'The first season.'),
                       ('Berries such as elderberry', 'Light crop in year 2, full crop by years 3 to 4.'),
                       ('Grafted pawpaw and persimmon', 'Often 3 to 6 years.')],
             'media': media('ref-raised-bed-greens', 'Leafy greens growing in a wooden raised garden bed', 'Raised beds produce the first season while the trees and shrubs grow in.')},
            {'eyebrow': 'Care', 'h2': 'Planting and care plans',
             'paras': ['Fruit trees need establishment watering, mulch, protection from deer and rabbits, and pruning while they are young. We plant with tree guards where needed and offer care plans for watering, pruning and mulch.']},
            {'eyebrow': 'Where we work', 'h2': 'Food forests and kitchen gardens across Wood and Lucas County',
             'paras': [f'Food forests, fruit trees and kitchen gardens across {AREA}. Free estimates: 419-873-6801. Also see <a href="native-landscaping-toledo-ohio.html">native habitat</a> and <a href="natural-swimming-pools-ponds-ohio.html">natural ponds and pools</a>.'],
             'links': [('permaculture-design-toledo-ohio.html', 'Permaculture design'),
                       ('native-landscaping-toledo-ohio.html', 'Native habitat and pollinator gardens'),
                       ('natural-swimming-pools-ponds-ohio.html', 'Natural swimming pools and ponds'),
                       ('best-plants-for-ohio-clay-soil.html', 'Best plants for Ohio clay soil'),
                       ('landscape-design.html', 'Landscape design')]},
        ],
    },
    {
        'file': POOLS,
        'title': 'Natural Swimming Pools and Ponds',
        'service_name': 'Natural Swimming Pool Design and Construction',
        'extra_services': ['Pond and Water Feature Installation', 'Pondless Waterfall Installation', 'Wildlife Pond Design'],
        'seo_title': 'Natural Swimming Pools &amp; Ponds Toledo, Ohio | Terramorph',
        'seo_desc': 'Chemical-free natural swimming pools, swim ponds, wildlife ponds and pondless waterfalls with plant-based bog filters. Toledo, Perrysburg and NW Ohio.',
        'crumb': 'Natural Pools &amp; Ponds',
        'eyebrow': 'Natural pools, swim ponds and water features',
        'image': 'ref-wildlife-pond-lilies.webp',
        'hero_alt': 'Garden wildlife pond with water lilies, boulders and native-style plantings',
        'hero_credit': 'A garden wildlife pond with water lilies and planted margins. ' + hero_credit('ref-wildlife-pond-lilies'),
        'headline': 'Natural Swimming Pools, Swim Ponds &amp; Water Features in Northwest Ohio',
        'lead': 'Swim in living water. Terramorph has designed and built natural swimming pools, swim ponds, wildlife ponds and pondless waterfalls that use plants and gravel, not chlorine, to keep water clear, designed for Ohio winters and Northwest Ohio clay.',
        'problem': 'A chlorine pool means chemicals, a stark concrete look, and a backyard that ends at the pool fence.',
        'outcome': 'A pool or pond that looks like it belongs in the landscape, cleaned by plants, alive with dragonflies and birds, and built for local winters.',
        'cta': 'Plan My Natural Pool',
        'chapters': [
            {'eyebrow': 'Living water', 'h2': 'Swim in living water: what a natural pool is',
             'paras': ['A natural swimming pool has two parts: an open <b>swimming zone</b> and a shallow <b>regeneration zone</b> planted with water plants. Water circulates through the plants and gravel, where settling, microbes, plant roots and a natural biofilm clean it. No chlorine. The result looks like a garden pond you can swim in.',
                       "Natural pools aren't new. They're well established in Europe, and the design standard most builders follow is the German/Austrian FLL guideline. North America's first public natural swimming pool opened in Minneapolis in 2015, cleaned by about 7,000 aquatic plants rooted in gravel."],
             'media': media('ref-natural-swimming-pond', 'Natural swimming pond with a planted regeneration zone and wooden deck, no chlorine', 'A natural swimming pond (Germany): open swim zone on the left, planted regeneration zone along the far edge.')},
            {'eyebrow': 'What we build', 'h2': 'Options we build',
             'paras': ['From a full natural swimming pool to a small recirculating waterfall, each option fits a different yard and a different family.'],
             'cards': [('Natural swimming pools', 'A swimming zone with a separate or surrounding planted regeneration zone, often with a gentle pump and skimmer for circulation.'),
                       ('Swim ponds and recreation ponds', 'A larger, more natural-looking pond designed for swimming and wildlife, with planted margins and a beach or deck entry.'),
                       ('Wildlife ponds', 'Ponds built for frogs, dragonflies, birds and pollinators, with shallow shelves, native marginal plants and no swimming.'),
                       ('Pondless waterfalls and streams', 'The sound and look of moving water without an open pond, recirculating from a hidden underground basin. A good fit for small yards and homes with young children.'),
                       ('Bog filters for existing ponds', 'A planted gravel bog that cleans an existing pond with plants instead of chemicals.')]},
            {'eyebrow': 'How it works', 'h2': 'How natural filtration works',
             'paras': ['How big the planted zone needs to be depends on the design. In simpler, plant-driven pools it is often around half the surface area. Designs with more filtration equipment can use a smaller planted zone.'],
             'cards': [('Settling', 'Particles sink and are removed.'),
                       ('Microbes', 'Bacteria in the gravel break down organic matter.'),
                       ('Plants', 'Roots take up nutrients, especially phosphorus, that would otherwise feed algae.'),
                       ('Biofilm', 'A living film on gravel and roots filters fine pollutants.'),
                       ('Circulation', 'Many designs use a small pump to move water through the plant zone. At the Minneapolis public pool, the whole volume cycles through the plant filter about every 12 hours.')],
             'media': media('ref-river-wetlands-aerial', 'Aerial view of a river meandering through green and gold wetlands', 'Wetlands clean water the same way a regeneration zone does: settling, microbes and plant roots (Selawik refuge, Alaska).')},
            {'eyebrow': 'Built for here', 'h2': 'Built for Ohio winters and Northwest Ohio clay',
             'paras': ['Northwest Ohio ground and winters shape every natural pool and pond we build.'],
             'cards': [('Clay is good news', 'Ohio DNR says pond soils need at least 20% clay to hold water, because clay swells and seals when wet. Much of our area sits on heavy clay, which helps for wildlife ponds. Swimming pools are lined either way for a clean, controlled edge.'),
                       ('Winter', 'Natural pools and ponds freeze over in an Ohio winter. Plants go dormant, pumps are winterized or kept running depending on the design, and the system restarts in spring as the plants wake up.'),
                       ('Depth', "For fish to survive a northern Ohio winter, ODNR recommends 10 to 12 feet of depth in at least a quarter of a fish pond. Wildlife and swim ponds are designed for their own purpose and don't need to be that deep."),
                       ('Utility locates', 'Every dig starts with an OHIO811 call at least two working days ahead.')]},
            {'raw': True},  # comparison table, see COMPARE below
            {'eyebrow': 'Cost', 'h2': 'Cost and what drives it',
             'paras': ["We don't publish a price range because every natural pool is custom. Cost depends on size, the split between swim and regeneration zones, excavation and soil conditions, liner and edging materials (stone, decking, beach entry), pumps and skimmers, and how much planting you want. We give a free estimate and a clear scope. See <a href=\"financing.html\">financing</a> for larger projects."]},
            {'eyebrow': 'Conversions', 'h2': 'Converting an existing pool',
             'paras': ["Some chlorine pools can be converted to natural pools by adding a regeneration zone and changing the filtration. Whether it makes sense depends on the pool's shape, condition and the space around it. We'll assess yours honestly."]},
            {'eyebrow': 'Safety and permits', 'h2': 'Safety, permits and fencing',
             'paras': ["Ohio's public-pool rules don't apply to private home pools, and the state residential code leaves pool fences and barriers to each city or township. So the rules depend on where you live. We check your local zoning, fence and permit requirements and build to them. Many Ohio cities require a barrier at least 4 feet high around pools deeper than 24 inches."]},
            {'eyebrow': 'Maintenance', 'h2': 'Maintenance plans',
             'paras': ['Expect skimming leaves, trimming and thinning plants, checking the pump, regular water testing, and spring start-up and fall shutdown. We offer seasonal care plans so the system stays balanced.']},
            {'eyebrow': 'Where we work', 'h2': 'Natural pools and ponds across Wood and Lucas County',
             'paras': [f'Natural swimming pools, swim ponds, wildlife ponds and water features across {AREA}. Free estimates: 419-873-6801. Part of a bigger plan? See <a href="permaculture-design-toledo-ohio.html">permaculture design</a> and <a href="native-landscaping-toledo-ohio.html">native habitat</a>. Decks, stone edges and paths come from the same crew: <a href="paver-patios-hardscapes.html">paver patios and hardscapes</a>.'],
             'links': [('permaculture-design-toledo-ohio.html', 'Permaculture design'),
                       ('native-landscaping-toledo-ohio.html', 'Native habitat and pollinator gardens'),
                       ('food-forest-edible-landscaping-toledo-ohio.html', 'Food forests and edible landscaping'),
                       ('drainage-solutions.html', 'Drainage solutions'),
                       ('landscape-design.html', 'Landscape design'),
                       ('paver-patios-hardscapes.html', 'Paver patios and hardscapes')]},
        ],
    },
]

COMPARE = '''<section class="tm-sec-tight tm-paper tm-compare-sec"><div class="tm-wrap">
  <p class="tm-label">Side by side</p><h2 class="tm-h2">Natural pool vs. chlorine pool</h2>
  <table class="tm-compare"><thead><tr><th scope="col"></th><th scope="col">Natural pool</th><th scope="col">Chlorine pool</th></tr></thead><tbody>
    <tr><th scope="row">Water treatment</th><td>Plants, gravel, microbes; no chlorine</td><td>Chlorine or salt system</td></tr>
    <tr><th scope="row">Look</th><td>Blends into the landscape, planted edges</td><td>Hard edge, blue finish</td></tr>
    <tr><th scope="row">Wildlife</th><td>Dragonflies, frogs, birds</td><td>Kept out</td></tr>
    <tr><th scope="row">Upkeep</th><td>Skimming, plant care, regular water testing</td><td>Chemical balancing, filter care</td></tr>
    <tr><th scope="row">Winter</th><td>Freezes and restarts naturally in spring</td><td>Closed and covered</td></tr>
  </tbody></table>
  <p class="tm-compare-note">Chlorine-free doesn't mean test-free. A natural pool is a living system, and owners monitor it. The Minneapolis public pool is vacuumed daily and tested for bacteria up to three times a week. A home pool needs far less, but it still needs regular care.</p>
</div></section>'''


def chapter_media():
    """{page: {eyebrow: (src, alt, caption)}} for svc_v2 chapter figures."""
    out = {}
    for p in PAGES:
        out[p['file']] = {ch['eyebrow']: ch['media'] for ch in p['chapters'] if ch.get('media')}
    return out


def image_sitemap_entries():
    seen, out = set(), []
    for p in PAGES:
        src = 'assets/' + p['image']
        out.append((p['file'], src, p['hero_alt']))
        seen.add(src)
        for ch in p['chapters']:
            if ch.get('media') and ch['media'][0] not in seen:
                seen.add(ch['media'][0])
                out.append((p['file'], ch['media'][0], ch['media'][1]))
    return out


def build(g):
    """Write the four pages through build_pages.service_page()."""
    depth_section, service_page = g['_depth_section'], g['service_page']
    for p in PAGES:
        depth = ''
        for ch in p['chapters']:
            if ch.get('raw'):
                depth += COMPARE
                continue
            depth += depth_section(ch['eyebrow'], ch['h2'], ch['paras'], ch.get('cards', []), ch.get('links'), id=ch.get('id'))
        service_page(p['file'], p['title'], p['eyebrow'], p['image'], p['headline'], p['lead'], p['problem'], p['outcome'], p['cta'],
                     embed_jobber=True, depth=depth, seo_title=p['seo_title'], seo_desc=p['seo_desc'],
                     crumb_parent=('services.html', 'Services'), crumb=p['crumb'], hero_alt=p['hero_alt'], hero_credit=p['hero_credit'],
                     service_name=p['service_name'], extra_services=p['extra_services'], process=p.get('process'))

"""Search-gap pages (2026-11-24).

Seven pages built from the Google Ads search-term report
(~/projects/terramorph/04-marketing/search-terms-2026-11/summary.md):

  lawn-maintenance-toledo-ohio.html        lawn care toledo / toledo lawn mowing services
  lawn-maintenance-perrysburg-ohio.html    lawn care perrysburg ohio / lawn mowing perrysburg ohio
  lawn-maintenance-maumee-ohio.html        lawn care / mowing, Maumee
  leaf-removal-toledo-ohio.html            leaf removal toledo (added to LEAF_CITIES in seo_expansion.py)
  leaf-collection-toledo-perrysburg.html   perrysburg leaf collection / city of toledo leaf collection
  lawn-aeration-overseeding-northwest-ohio.html   lawn aeration near me / dethatching / aeration cost
  shrub-hedge-trimming-northwest-ohio.html        shrub, bush and hedge trimming

Rules these pages follow:
  * No prices, counts, certifications or guarantees beyond what the site already states.
  * No tree work. Terramorph does not do trees.
  * City leaf-pickup facts were read on each city's own website on 2026-11-24
    (URLs in CITY_LEAF_PAGES). Re-check them every fall before trusting the dates.
  * Photos are the existing real Terramorph library only. Captions and alt text
    say what the photo plainly shows and never name a town or a job.
"""

AERATION_FILE = 'lawn-aeration-overseeding-northwest-ohio.html'
SHRUB_FILE = 'shrub-hedge-trimming-northwest-ohio.html'
LEAF_GUIDE_FILE = 'leaf-collection-toledo-perrysburg.html'
AERATION_TITLE = 'Lawn Aeration and Overseeding'
SHRUB_TITLE = 'Shrub and Hedge Trimming'

# These carry their own answer card, local copy and FAQ schema, so the generic
# authority pass (city blurb + city FAQ injection) leaves them alone.
SKIP_AUTHORITY = [AERATION_FILE, SHRUB_FILE, LEAF_GUIDE_FILE]

# Official city pages, each opened and read on 2026-11-24.
CITY_LEAF_PAGES = {
    'Toledo': 'https://toledo.oh.gov/residents/neighborhoods/leaf-collection',
    'Perrysburg': 'https://www.perrysburgoh.gov/259/Yard-Waste-Program',
    'Maumee': 'https://www.maumee.org/348/Fall-Leaf-Collection',
}


def _ext(city, label):
    return f'<a href="{CITY_LEAF_PAGES[city]}" target="_blank" rel="noopener">{label}</a>'


def _light(html):
    """Inline links on light backgrounds inherit the body text colour with no underline,
    so they do not read as links. Mark them. (Dark sections already style links gold.)"""
    return html.replace('<a href=', '<a style="color:#173b27;font-weight:700;text-decoration:underline;text-underline-offset:3px" href=')


# ---------------------------------------------------------------------------
# Shrub photo set (added to SERVICE_PHOTOS['shrubs'] in build_pages.py)
# ---------------------------------------------------------------------------
SHRUB_PHOTOS = [
    ('Rounded boxwoods and shaped shrubs along a front walk', 'assets/real-boxwood-front-bed.webp'),
    ('Shaped shrubs in a curved front rock bed', 'assets/real-front-bed-curved-boxwood.webp'),
    ('Arborvitae row behind a split-rail fence', 'assets/real-fence-line-planting.webp'),
    ('Shaped shrubs in a foundation bed', 'assets/real-foundation-planting.webp'),
    ('Shrubs in a front bed with white rock', 'assets/real-estate-front-bed.webp'),
    ('Arborvitae row on a commercial lot', 'assets/real-arborvitae-row.webp'),
]

# ---------------------------------------------------------------------------
# FAQs for the two service pages (merged into SERVICE_FAQS)
# ---------------------------------------------------------------------------
FAQS = {
    AERATION_TITLE: [
        ('When is the best time to aerate and overseed a lawn in Northwest Ohio?', 'Late August through October. The soil is still warm, the nights are cool, and fall rain helps new grass root before winter. Earlier in that window is better, because seedlings need several weeks of growing weather before the ground gets cold. Spring aeration is possible, but spring seeding runs into summer heat and crabgrass.'),
        ('Is lawn aeration worth it on clay soil?', 'Clay is where it helps most. Much of Wood and Lucas County sits on heavy lakebed clay that packs down under foot traffic and mowers. Core aeration pulls plugs out of that packed layer so water, air, and seed can get into the soil instead of sitting on top of it.'),
        ('Should I dethatch or aerate my lawn?', 'Most lawns here need aeration, not dethatching. Thatch is the spongy layer of dead stems between the grass and the soil, and under about half an inch of it is normal. Dethatching is only worth doing when that layer is thicker. Compacted soil is the more common problem on local clay, and core aeration also helps thatch break down.'),
        ('What affects lawn aeration and overseeding cost?', 'Lawn size is the biggest factor. After that it is access for the machine, how thin or bare the lawn is, how much seed it needs and what kind, and whether the visit is combined with other work. Terramorph looks at the lawn and gives a free estimate. No prices are quoted sight unseen.'),
        ('How long does it take to see new grass after overseeding?', 'It depends on the seed. Perennial ryegrass can be up in about a week, tall and fine fescue in one to two weeks, and Kentucky bluegrass in two to four weeks. The seed has to stay damp the whole time, so light, frequent watering matters more than anything else in those first weeks.'),
        ('What should I do before the crew comes to aerate?', 'Mark sprinkler heads, invisible dog fence wire, and any shallow cable or lighting wire you know about. Mow the lawn at its normal height a day or two before. If the ground is very dry, watering the day before helps the tines pull deeper plugs.'),
        ('Can I aerate without overseeding?', 'Yes. A thick lawn that is only compacted can be aerated on its own. If the lawn is thin, patchy, or mostly older grass, seeding right after aeration is the better value because the seed falls into the holes and touches soil.'),
        ('Do you offer lawn aeration near me?', 'Terramorph aerates and overseeds lawns in Perrysburg, Toledo, Maumee, Sylvania, Rossford, Waterville, Whitehouse, Holland, Bowling Green, Oregon, and the rest of Wood and Lucas County, Ohio.'),
    ],
    SHRUB_TITLE: [
        ('Do you offer bush trimming and hedge trimming near me?', 'Terramorph trims shrubs, bushes, and hedges for homes and businesses in Perrysburg, Toledo, Maumee, Sylvania, Rossford, Waterville, Whitehouse, Holland, Bowling Green, Oregon, and the rest of Wood and Lucas County, Ohio.'),
        ('When is the best time to trim bushes in Ohio?', 'It depends on the plant. Shrubs that bloom in spring, like lilac, forsythia, and azalea, are trimmed right after they flower. Shrubs that bloom in summer on new growth, like panicle hydrangea and rose of Sharon, are cut in late winter or early spring. Evergreen shrubs and hedges are shaped after the spring flush of growth. Heavy cutting stops by late summer so new growth is not killed by frost.'),
        ('Can you cut back overgrown bushes?', 'Usually, yes. Many shrubs can be brought back down over one or two seasons, and multi-stem shrubs like lilac, forsythia, and spirea can be renewed by taking out the oldest stems at the ground. Some evergreens will not regrow from bare wood, so a shrub that has badly outgrown its spot is sometimes better replaced. We tell you which it is before anything is cut.'),
        ('Will trimming my hydrangea or lilac stop it from blooming?', 'Only if it is cut at the wrong time. Lilac, forsythia, azalea, and bigleaf hydrangea set next year\'s flower buds over the summer, so shearing them in fall or winter removes the flowers. Terramorph leaves those alone in fall and trims them after they bloom. Panicle and smooth hydrangea bloom on new growth and can be cut back in late winter.'),
        ('Can an overgrown arborvitae hedge be cut way back?', 'Not far. Arborvitae only grows new foliage from green wood. If it is cut back into the bare brown interior, that section stays bare. It can be shaped and kept in bounds, and the top can be brought down a modest amount, but a hedge that is several feet too tall or wide usually cannot be shrunk to half its size.'),
        ('Do you haul away the clippings?', 'Yes. Clippings and brush are raked out of the beds, blown off the walks and drive, and hauled away with the crew.'),
        ('Do you trim or remove trees?', 'No. Terramorph does not do tree removal, tree climbing, large-limb cutting, or stump grinding. This service covers shrubs, bushes, and hedges that can be trimmed safely from the ground. For tree work, call a tree service.'),
        ('What affects shrub and hedge trimming cost?', 'The number and size of the shrubs, how overgrown they are, the length and height of any hedge, access around the beds, and how much brush has to be hauled away. Terramorph looks at the property and gives a free estimate.'),
    ],
}

# Direct answers under each hero (svc_v2.ANSWERS) and in llms.txt.
ANSWERS = {
    AERATION_FILE: 'Terramorph provides core aeration and overseeding for lawns in Perrysburg, Toledo, Maumee, Sylvania, and across Wood and Lucas County, Ohio. A stand-on core aerator pulls plugs from compacted clay soil, and seed matched to the lawn\'s sun and shade goes down right after, so it lands in the holes. Late August through October is the best window in Northwest Ohio. Estimates are free.',
    SHRUB_FILE: 'Terramorph trims and shapes shrubs, bushes, and hedges for homes and businesses in Perrysburg, Toledo, Maumee, Sylvania, and across Wood and Lucas County, Ohio. Each plant is trimmed at the right time for its type so spring bloomers keep their flowers, overgrown shrubs are cut back in stages, and the clippings are hauled away. Terramorph does not do tree removal or large-tree work. Estimates are free.',
}


def build_service_pages(g):
    """Write the aeration and shrub-trimming service pages with build_pages.service_page().
    svc_v2 re-lays them out in the v2 design at the end of the build."""
    service_page, depth = g['service_page'], g['_depth_section']

    aeration_depth = ''.join([
        depth('Why lawns here need it', 'Clay soil packs down, and packed soil cannot grow thick grass.',
              ['Most of Wood and Lucas County sits on old lakebed clay, the same ground that was once the Great Black Swamp. Clay particles are tiny and flat. Foot traffic, mowers, kids, dogs, and construction equipment press them together until there is almost no space left for air or water.',
               'Grass roots stop where the soil gets tight. A compacted lawn has shallow roots, so it thins out, browns early in summer, and lets weeds move into the open spots. More fertilizer or seed spread on top does not fix it, because neither one gets into the soil.'],
              [('Water puddles or runs off', 'Rain sits on the surface or sheets toward the drive instead of soaking in.'),
               ('The screwdriver test fails', 'If a screwdriver will not push a few inches into damp soil by hand, the soil is compacted.'),
               ('Thin grass in the traffic lanes', 'The path to the gate, the dog run, and the play area wear out first.'),
               ('A newer home on a graded lot', 'Builder topsoil is often a thin layer over clay that was packed by equipment.'),
               ('The lawn browns out early', 'Shallow roots run out of water as soon as the heat arrives.')]),
        depth('What core aeration is', 'Core aeration pulls plugs out of the lawn. Spikes just poke it.',
              ['A core aerator drives hollow tines into the ground and pulls out plugs of soil a couple of inches long. Those holes give roots, water, and air a way down, and the soil around them loosens as it expands into the space.',
               'The plugs are left on the lawn on purpose. They break down over a couple of weeks of rain and mowing and put soil back on top of the thatch layer, which helps it decompose. Spike aerators and spiked shoes do not remove anything. They push soil sideways and can pack the sides of the hole tighter.'],
              [('Stand-on core aerator', 'A commercial machine that pulls consistent plugs across the whole lawn.'),
               ('Plugs stay on the lawn', 'They look rough for a week or two, then disappear. Do not rake them up.'),
               ('Damp soil works best', 'Tines pull deeper plugs when the ground is moist, not baked hard or saturated.'),
               ('Mark what is buried', 'Sprinkler heads, invisible dog fence wire, and shallow cables need flags before the machine runs.')]),
        depth('Overseeding', 'Overseeding right after aeration puts the seed where it can root.',
              ['Grass seed has to touch soil to grow. Seed thrown onto an established lawn mostly lands on thatch and dries out. Seed spread right after core aeration falls into the holes and onto loosened soil, where it stays damp and roots quickly.',
               'The seed is matched to the lawn. Kentucky bluegrass and perennial ryegrass suit open, sunny lawns. Tall fescue handles heat, wear, and clay. Fine fescue is the one that tolerates shade under mature trees. Bare ground left by grading or new construction is a different job, and that gets seeded or hydroseeded from scratch.'],
              [('Perennial ryegrass', 'Up in about a week. Quick cover while slower grasses fill in.'),
               ('Tall fescue', 'One to two weeks. Deep roots, good on clay and in summer heat.'),
               ('Fine fescue', 'One to two weeks. The best choice for shaded lawns.'),
               ('Kentucky bluegrass', 'Two to four weeks. Slow to start, then spreads to knit the lawn together.')]),
        depth('Timing', 'When to aerate and overseed in Northwest Ohio.',
              ['Late August through October is the best seeding window of the year here. The soil is still warm from summer, the nights are cool, fall rain does part of the watering, and summer weeds are fading instead of sprouting.',
               'Earlier in that window is better. New grass needs several weeks of growing weather before the ground turns cold, and the first frost at Toledo Express Airport arrives around October 24 in a typical year. Spring aeration can still help a compacted lawn, but seed put down in spring has to survive summer heat, and the crabgrass preventer many lawns get in spring stops grass seed from sprouting too.'],
              [('Late August and September', 'The best results. Warm soil and time to root before frost.'),
               ('October', 'Still workable most years, especially with faster-sprouting ryegrass and fescue.'),
               ('Spring', 'Aeration helps with compaction. Seeding is harder because of heat, weeds, and pre-emergent.'),
               ('Leaf season', 'Leaves have to come off new grass gently and often, or the seedlings are smothered.')],
              links=[('seasonal-cleanups.html', 'Leaf Removal &amp; Fall Cleanup'), ('lawn-maintenance.html', 'Lawn Maintenance')], id='timing'),
        depth('Aeration vs. dethatching', 'Dethatching or aeration: which one does the lawn need?',
              ['Thatch is the spongy brown layer of dead stems and roots between the green grass and the soil. A thin layer, under about half an inch, is normal and protects the soil. Dethatching, also called power raking, rips that layer out with spinning tines. It is hard on a lawn and only worth doing when the thatch is truly thick.',
               'On local clay, compaction is the more common problem, and the two get confused because both make a lawn feel hard and look thin. To check, cut a small wedge of turf a few inches deep and look at it from the side. If the brown spongy layer is thinner than your finger, the lawn needs aeration, not dethatching. Send a photo of that wedge with an estimate request and we will tell you what we see.'],
              [('Core aeration', 'Fixes compacted soil. Also helps thatch break down by mixing soil into it.'),
               ('Dethatching', 'Removes a thatch layer thicker than about half an inch. Stressful for the lawn.'),
               ('Overseeding', 'Thickens a thin lawn. Works best right after aeration.')], id='dethatching'),
        depth('What it costs', 'What goes into lawn aeration and overseeding cost.',
              ['Terramorph prices each lawn after looking at it, and the estimate is free. We do not post a flat price because two lawns the same size can be very different jobs.',
               'Lawn size is the biggest factor. Access matters next: gates, slopes, tight side yards, and obstacles slow the machine down. Then comes the seed, since a thin or half-bare lawn needs more of it than a decent lawn getting thickened, and shade blends cost differently than sun blends. Combining the visit with a fall cleanup or regular lawn maintenance can change the number too.'],
              [('Lawn size', 'Measured from the property, not guessed.'),
               ('Access', 'Gate width, slopes, and how much hand work is needed.'),
               ('Condition', 'How compacted, thin, or bare the lawn is.'),
               ('Seed', 'How much, and whether it is a sun, shade, or mixed blend.')],
              links=[('lawn-maintenance-cost-northwest-ohio.html', 'Lawn Maintenance Cost in Northwest Ohio')], id='cost'),
        depth('After the visit', 'What to do after aeration and overseeding.',
              ['The first three weeks decide how much of the seed becomes grass. The surface has to stay damp, which usually means light watering once or twice a day until the seed sprouts, then deeper watering less often as the roots go down.',
               'Stay off the new grass as much as you can. Mow again once the new grass reaches normal mowing height, with a sharp blade, and hold off on weed killers until the new grass has been mowed a few times. Keep fallen leaves from piling up on it.'],
              [('Weeks 1 to 3', 'Keep the surface damp. Light and frequent beats a heavy soak.'),
               ('First mow', 'When new grass reaches normal mowing height. Sharp blade, dry lawn.'),
               ('Weed control', 'Wait until the new grass has been mowed a few times.'),
               ('Leaves', 'Clear them gently and often so seedlings get light.')]),
        '<section class="section guide-index-section"><div class="container guide-grid">'
        + ''.join(f'<a class="guide-card" href="{h}"><span>Related</span><h3>{t}</h3><p>{d}</p><b>Open page &rarr;</b></a>' for h, t, d in [
            ('lawn-maintenance.html', 'Lawn Maintenance', 'Recurring mowing, edging, trimming, and bed upkeep on a set schedule.'),
            ('lawn-maintenance-toledo-ohio.html', 'Lawn Care in Toledo', 'Mowing and lawn care for older city lots, shade, and tight side yards.'),
            ('lawn-maintenance-perrysburg-ohio.html', 'Lawn Care in Perrysburg', 'Mowing and lawn care for flat clay lots and newer subdivisions.'),
            ('lawn-maintenance-maumee-ohio.html', 'Lawn Care in Maumee', 'Mowing and lawn care for shaded, established yards near the river.'),
            (SHRUB_FILE, 'Shrub and Hedge Trimming', 'Shrubs, bushes, and hedges shaped at the right time for each plant.'),
            ('seasonal-cleanups.html', 'Leaf Removal and Fall Cleanup', 'Leaves cleared and hauled away before the first snow.'),
        ]) + '</div></section>',
    ])
    service_page(
        AERATION_FILE, AERATION_TITLE, 'Core aeration and overseeding', 'real-stinger-aerator.webp',
        "Lawn aeration and overseeding for Northwest Ohio's compacted clay lawns.",
        'Core aeration pulls plugs out of compacted soil so air, water, and seed can get in. Overseeding right behind it fills thin and bare areas with new grass. Terramorph does both in one visit for lawns in Perrysburg, Toledo, Maumee, and across Wood and Lucas County. Free estimates.',
        'The lawn is thin, patchy, and hard as a brick by August. Water runs off instead of soaking in, and seed thrown on top never seems to take.',
        'Soil that takes in water and air again, new grass filling the thin spots, and a thicker lawn going into next spring.',
        'Request an Aeration Estimate', True, depth=aeration_depth,
        seo_title='Lawn Aeration & Overseeding in Toledo & Perrysburg | Terramorph',
        seo_desc='Lawn aeration and overseeding in Toledo, Perrysburg, Maumee, and Northwest Ohio. Core aeration for compacted clay, seed matched to sun and shade. Free estimates.',
        crumb_parent=('lawn-maintenance.html', 'Lawn Maintenance'), crumb='Aeration &amp; Overseeding',
        hero_alt='Stand-on core aerator on a striped lawn',
        service_name='Lawn Aeration', extra_services=['Overseeding'],
        service_desc='Core aeration and overseeding for residential and commercial lawns in Wood and Lucas County, Ohio: plugs pulled from compacted clay soil with a stand-on core aerator, then grass seed matched to sun and shade spread across the lawn.',
        process=('From a tired lawn to new grass.', 'Aeration and seeding happen in the same visit. What happens in the weeks after is mostly water and patience.',
                 [('Look at the lawn', 'Soil, thin areas, shade, and how the lawn has been cut and watered.'),
                  ('Aerate', 'Core aeration across the lawn, plugs left to break down and feed the soil.'),
                  ('Seed', 'Seed matched to your sun and shade, spread right after aeration so it lands in the holes.'),
                  ('Water and wait', 'Keep the seed damp until it sprouts. We tell you what to expect and when to mow again.')]))

    shrub_depth = ''.join([
        depth('What we trim', 'Bush trimming, hedge trimming, and shrub shaping in one visit.',
              ['Most properties have a mix: evergreen shrubs along the foundation, a hedge or privacy row on one side, and a few flowering shrubs that have gotten bigger than anyone planned. Terramorph trims all of it in one visit, cleans out the beds underneath, and hauls the brush away.',
               'The work is done from the ground with hand pruners, loppers, and hedge trimmers. The goal is a shrub that looks like itself, only smaller and tidier, not a row of identical green boxes unless a formal hedge is what you want.'],
              [('Foundation shrubs', 'Boxwood, yew, holly, spirea, and burning bush kept below the windows and off the siding.'),
               ('Hedges and privacy rows', 'Arborvitae, privet, and yew hedges kept straight, level, and inside their space.'),
               ('Flowering shrubs', 'Hydrangea, lilac, forsythia, viburnum, and rose of Sharon trimmed at the right time for each.'),
               ('Grasses and perennials', 'Ornamental grasses and spent perennials cut back as part of a spring or fall visit.'),
               ('Overgrowth', 'Branches cleared off walks, windows, downspouts, AC units, and house numbers.'),
               ('Cleanup', 'Clippings raked out of the beds and hauled away with the crew.')]),
        depth('Timing', 'When to trim bushes in Northwest Ohio depends on the plant.',
              ['There is no single best month. The right time depends on when the shrub blooms and whether it flowers on old wood or new growth. Getting it wrong does not usually kill the plant. It just costs a year of flowers or leaves it looking chopped.',
               'That is why a fall cleanup from Terramorph includes only light shaping, and why spring-flowering shrubs are left alone until they have bloomed.'],
              [('Spring bloomers: right after they flower', 'Lilac, forsythia, azalea, rhododendron, weigela, and bigleaf hydrangea set next year\'s buds in summer. Trim them in fall or winter and the flowers go with the clippings.'),
               ('Summer bloomers: late winter or early spring', 'Panicle and smooth hydrangea, rose of Sharon, butterfly bush, and summer spirea bloom on new growth, so they can be cut back before they leaf out.'),
               ('Evergreen shrubs and hedges: late spring into midsummer', 'Boxwood, yew, and arborvitae are shaped after the spring flush of growth, with a light touch-up later if needed.'),
               ('Late summer and fall: light shaping only', 'Heavy cutting late in the season pushes soft new growth that the first hard freeze kills.'),
               ('Dead or broken branches: any time', 'Dead, broken, and diseased wood comes out whenever it is found.')], id='timing'),
        depth('Hedges', 'Hedge trimming: straight lines, and wider at the bottom than the top.',
              ['A hedge that is sheared straight up and down, or wider at the top, shades its own lower branches. Over a few years the bottom thins out and goes bare. A hedge trimmed slightly narrower at the top lets light reach all the way down, and it stays green to the ground.',
               'Different hedge plants forgive different things. Yew and privet can take a hard cut and grow back. Boxwood does best with light shearing plus some thinning so air moves through it. Arborvitae only grows from green wood, so it is trimmed within the green and never cut back into the bare brown interior.'],
              [('Level tops and clean sides', 'Lines checked by eye from the street and from the house, not just up close.'),
               ('Tapered shape', 'Slightly narrower at the top so the bottom keeps its leaves.'),
               ('Arborvitae handled carefully', 'Shaped within the green growth. Cuts into bare wood do not fill back in.'),
               ('Height kept in reach', 'Regular trimming keeps a hedge at a size that can be maintained from the ground.')]),
        depth('Overgrown shrubs', 'Overgrown bushes: cut back, renew, or replace.',
              ['Shrubs covering the windows or crowding the front walk are the most common reason people call. There are three honest answers, and which one fits depends on the plant.',
               'Some shrubs can simply be reduced, taken down in size over one or two seasons so they are never stripped bare at once. Multi-stem shrubs like lilac, forsythia, spirea, and red twig dogwood can be renewed by removing the oldest, thickest stems at the ground so younger growth takes over. And some shrubs, usually evergreens planted too close to the house decades ago, are simply too big for the spot. Those are better removed and replaced with something that fits, which is a ' + _light('<a href="landscape-design.html">landscape design</a>') + ' conversation.'],
              [('Reduce', 'Bring the size down in stages so the shrub stays green and full.'),
               ('Renew', 'Take out the oldest stems at the base and let new growth replace them.'),
               ('Replace', 'Remove a shrub that has outgrown its spot and plant one that fits.')],
              links=[('landscape-design.html', 'Landscape Design'), ('mulch-installation-toledo-ohio.html', 'Mulch Installation'), ('seasonal-cleanups.html', 'Seasonal Cleanups')], id='overgrown'),
        depth('What this service is not', 'Shrubs, bushes, and hedges. Not tree work.',
              ['Terramorph does not do tree removal, tree climbing, large-limb cutting, or stump grinding. If the job needs a chainsaw overhead, a bucket truck, or a climber, it belongs with a tree service.',
               'What we do handle is everything in the beds that can be trimmed safely from the ground, along with the cleanup around it: bed edges, weeds, old mulch, and the brush pile at the end.'],
              [('We trim', 'Shrubs, bushes, hedges, ornamental grasses, and perennials.'),
               ('We do not do', 'Tree removal, climbing, large limbs, or stump grinding.'),
               ('Pairs well with', 'Spring and fall cleanups, bed edging, mulch, and recurring lawn maintenance.')]),
        depth('What it costs', 'What affects shrub and hedge trimming cost.',
              ['Terramorph looks at the property and gives a free estimate. Photos of the beds are usually enough to get started.',
               'The number comes down to how many shrubs there are and how big, how long it has been since they were last trimmed, the length and height of any hedge, how easy it is to get around the beds, and how much brush has to be loaded and hauled. Trimming that is part of regular maintenance takes less time per visit than a one-time rescue of beds that have been let go.'],
              [('Count and size', 'A few foundation shrubs is a different job than a full property.'),
               ('How overgrown', 'A light shaping is quicker than a hard cutback.'),
               ('Hedge length and height', 'Long or tall hedges take more time to keep level.'),
               ('Hauling', 'Brush volume and how far it has to be carried.')],
              links=[('lawn-maintenance.html', 'Lawn Maintenance'), ('spring-cleanup-northwest-ohio.html', 'Spring Cleanup Checklist'), (AERATION_FILE, 'Lawn Aeration and Overseeding')], id='cost'),
    ])
    service_page(
        SHRUB_FILE, SHRUB_TITLE, 'Shrub, bush, and hedge trimming', 'real-boxwood-front-bed.webp',
        "Shrub, bush, and hedge trimming that keeps the shape without costing next year's blooms.",
        'Terramorph trims and shapes shrubs, bushes, and hedges for homes and businesses in Perrysburg, Toledo, Maumee, Sylvania, and across Wood and Lucas County. Overgrown foundation plantings cut back, hedges squared up, and the clippings hauled away. Free estimates.',
        'The bushes have grown over the windows and the front walk, the hedge is bare at the bottom, and nobody is sure what can be cut back without killing it.',
        'Shrubs back in scale with the house, hedges with clean lines, beds cleaned up underneath, and every clipping hauled away.',
        'Request a Trimming Estimate', True, depth=shrub_depth,
        seo_title='Shrub, Bush & Hedge Trimming in Toledo & Perrysburg | Terramorph',
        seo_desc='Shrub, bush, and hedge trimming in Toledo, Perrysburg, Maumee, and Northwest Ohio. Overgrown bushes cut back, each plant trimmed at the right time. Free estimates.',
        crumb_parent=('services.html', 'Services'), crumb='Shrub &amp; Hedge Trimming',
        hero_alt='Rounded boxwoods and shaped shrubs along a front walk',
        service_name='Shrub and Hedge Trimming', extra_services=['Bush Trimming'],
        service_desc='Shrub, bush, and hedge trimming for homes and businesses in Wood and Lucas County, Ohio: shaping, overgrowth cut back, hedges leveled, and clippings hauled away. Does not include tree removal or large-tree work.',
        process=('From overgrown to back in shape.', 'A walk around the beds first, so you know what will be cut, how far, and what should wait for a better time of year.',
                 [('Walk the beds', 'We look at each shrub, what it is, and how far it can come back.'),
                  ('Agree on the plan', 'What gets shaped, what gets cut back hard, and what waits until after it blooms.'),
                  ('Trim', 'Hand pruners, loppers, and hedge trimmers, working from the ground.'),
                  ('Clean up', 'Beds raked out, walks blown off, and the brush hauled away.')]))


# ---------------------------------------------------------------------------
# Leaf removal in Toledo (one more LEAF_CITIES row for seo_expansion.py)
# ---------------------------------------------------------------------------
LEAF_TOLEDO = (
    'Toledo', 'toledo', 'real-fall-skidsteer-leaves.webp',
    "Leaf removal in Toledo, hauled away so you are not racing the city's curb week.",
    'Leaf removal and fall cleanup in Toledo, OH. Leaves cleared from lawns, beds, and fence lines and hauled away, whatever week the city truck comes. Free estimates.',
    "Toledo picks up leaves by ZIP code. Big trees do not always cooperate.",
    [f"The City of Toledo collects loose leaves at the curb every fall. The city says its 2026 program began Monday, November 2 and is scheduled to run about six weeks, moving through the city by ZIP code, with schedule updates posted on Fridays. Leaves are raked to the curb line no more than two days before the scheduled pickup. For your ZIP code's week, check the {_ext('Toledo', 'City of Toledo leaf collection page')}.",
     "That works well for a yard with a couple of trees and a free weekend at the right time. It is harder on the older, heavily treed streets in neighborhoods like Old Orchard, Westgate, the Old West End, and Beverly. Oaks hold their leaves late, often after the truck has already been through, and the city asks residents who miss collection not to put leaves in the street.",
     'Terramorph clears the lawn, the beds, the fence lines, and under the shrubs, loads the leaves, and hauls them away, so the timing is yours. Toledo lots are often narrow, with a fenced backyard, a detached garage, and tight side yards, and backpack blowers reach those spaces where leaves pile up and a rake is slowest.',
     'Many Toledo properties pair the fall cleanup with <a href="lawn-maintenance-toledo-ohio.html">lawn care in Toledo</a> through the season or a bed refresh from the <a href="landscaping-toledo-ohio.html">Toledo landscaping</a> page.'],
    [('When does the City of Toledo pick up leaves?', "The city says its 2026 leaf collection began Monday, November 2 and is scheduled to run about six weeks, moving through Toledo by ZIP code, with schedule updates posted on Fridays. Check the City of Toledo leaf collection page for your ZIP code's current week. Terramorph hauls leaves away on its own schedule, so nothing has to be raked to the curb."),
     ('What if I missed leaf pickup in Toledo?', 'The city asks residents who miss collection not to place leaves in the street. Its page lists composting or mulching, the trash container, and city drop-off sites as options. Terramorph can also clear the yard and haul everything away in one visit.'),
     ('Do you do leaf removal across Toledo?', 'Yes. Terramorph works in West Toledo, South Toledo, and the neighborhoods in between, along with Ottawa Hills, Sylvania, Maumee, and the rest of Lucas County.')],
)

# ---------------------------------------------------------------------------
# City leaf collection guide (one more GUIDES entry in build_pages.py)
# ---------------------------------------------------------------------------
LEAF_GUIDE = {
    'file': LEAF_GUIDE_FILE,
    'title': 'Toledo, Perrysburg, and Maumee Leaf Collection: When the City Picks Up Leaves and When to Hire a Crew',
    'short': 'How city leaf pickup works in Toledo, Perrysburg, and Maumee, where to find your pickup week, and when it makes more sense to have the leaves hauled away.',
    'category': 'Seasonal guide', 'service': 'Seasonal Cleanups', 'image': 'real-fall-leaf-crew.webp',
    'cta': 'Request a Leaf Removal Estimate',
    'sections': [
        ('The short answer',
         'The three cities handle leaves three different ways. Toledo collects loose leaves raked to the curb, working through the city by ZIP code. Perrysburg takes leaves through its yard-waste program, in paper bags or carts that each need a city tag. Maumee collects loose leaves by district, for owner-occupied homes only.'
         '</p><p>Pickup weeks change every year and can shift during the season, so this guide links to each city\'s own page instead of listing dates that will go stale. Everything below was checked against the city websites on November 24, 2026.'),
        ('City of Toledo leaf collection',
         f"Toledo runs a curbside leaf collection every fall. According to the {_ext('Toledo', 'City of Toledo leaf collection page')}, the 2026 program began Monday, November 2 and is scheduled to run about six weeks, with the schedule set by ZIP code and updates released on Fridays."
         '</p><p>The city asks residents to rake leaves to the curb line no more than two days before their scheduled pickup, keep storm drain inlets clear, and keep cars off the street when pickup is scheduled. If you miss collection, the city says not to place leaves in the street. Its page lists composting or mulching, your trash container, or a city drop-off site as the options, with drop-off open through January 8, 2027.'
         '</p><p>Your ZIP code\'s week is on the city page. Check it rather than a neighbor\'s memory of last year, because the order changes.'),
        ('Perrysburg leaf collection',
         f"Perrysburg handles leaves as yard waste. The {_ext('Perrysburg', 'City of Perrysburg yard waste page')} lists leaves among the materials collected in 30-gallon paper yard waste bags or in 64- and 96-gallon carts the resident buys, and says each bag or cart needs an official city yard waste tag for every collection. That page does not describe a loose-leaf curb pickup."
         '</p><p>From April 1 through November 30, the city says yard waste is collected on regular garbage days. From December 1 through March 31, collection is on Wednesdays only and has to be requested ahead of time by calling Modern Disposal at 419-874-2966. Tag locations and current tag fees are on the city page.'
         '</p><p>For a Perrysburg yard with one or two trees, that is a manageable number of bags. For a wooded lot, it is a lot of bagging and tagging, and the regular weekly route ends right around the time the last leaves come down.'),
        ('Maumee leaf collection',
         f"Maumee collects loose leaves by district. The {_ext('Maumee', 'City of Maumee fall leaf collection page')} says collection typically begins in October, the city is divided into four districts, and a schedule with pickup dates is posted each year. Leaves go behind the curb in front of your own property by the Sunday before your district's week, with no sticks, grass, or other debris mixed in, and not in the street or on storm drains."
         '</p><p>The service is for owner-occupied homes with two or fewer units. The city says rental properties, condominiums, apartment buildings, commercial properties, and mobile home parks are not included. It also says landscape contractors and anyone removing yard waste for hire may not place leaves at the curb for city collection.'
         '</p><p>That last rule matters if you hire help. A crew working in Maumee has to haul the leaves away, which is how Terramorph works everywhere.'),
        ('Sylvania, Rossford, Oregon, Bowling Green, and other towns',
         'Every city, village, and township in Wood and Lucas County sets its own leaf rules, and some change them from year to year. If you live outside the three cities above, check your city\'s leaf collection page or call the public service department before you rake anything to the street.'),
        ('When city leaf pickup is all you need',
         'City pickup is a good deal when the yard is small or lightly treed, you have the time and the back to rake, your trees drop before your scheduled week, and your property qualifies for the program. Plenty of homeowners in all three cities never need more than that.'
         '</p><p>If that is your yard, use the city program. A light layer of leaves can also be mulched into the lawn with a mower instead of being moved at all. Once leaves build up past about two inches, Ohio State University Extension recommends removing them so the grass underneath is not smothered.'),
        ('When hiring a leaf removal crew makes more sense',
         'The city truck takes what is at the curb on its week. It does not get leaves out of the beds, off the fence line, from under the shrubs, or out of the backyard. These are the situations where people call us instead.'
         '</p><p><b>The lot is heavily wooded.</b> A half acre of mature oak and maple is days of raking, and wet leaves are heavy.'
         '</p><p><b>The trees drop late.</b> Oaks hold leaves into late November and December, after many pickup weeks have passed.'
         '</p><p><b>You missed your week,</b> or you travel, or the weather did not cooperate.'
         '</p><p><b>The property does not qualify.</b> Rentals, condos, and commercial properties in Maumee are not covered by city collection.'
         '</p><p><b>Bagging is the bottleneck.</b> In Perrysburg, a big yard means a long row of tagged bags.'
         '</p><p><b>You want the beds done too.</b> Perennials cut back, bed edges cleaned up, and the lawn ready for winter in the same visit.'),
        ('What Terramorph leaf removal includes',
         'Terramorph clears leaves from the lawn, the beds, the fence lines, and under the shrubs with commercial walk-behind blowers and backpack crews, then loads and hauls them away. Spent perennials are cut back, sticks and debris go with the leaves, and nothing is left at the curb. The full list is on the <a href="seasonal-cleanups.html">leaf removal and fall cleanup</a> page, and the <a href="fall-cleanup-checklist-northwest-ohio.html">fall cleanup checklist</a> covers what to do yourself.'
         '</p><p>Town pages with local details: <a href="leaf-removal-toledo-ohio.html">leaf removal in Toledo</a>, <a href="leaf-removal-perrysburg-ohio.html">leaf removal in Perrysburg</a>, and <a href="leaf-removal-maumee-ohio.html">leaf removal in Maumee</a>. Estimates are free.'),
    ],
    'faqs': [
        ('When is leaf pickup in Toledo?', "The City of Toledo says its 2026 leaf collection began Monday, November 2 and is scheduled to run about six weeks, moving through the city by ZIP code, with schedule updates released on Fridays. Check the City of Toledo leaf collection page for your ZIP code's current week."),
        ('Does Perrysburg have curbside leaf collection?', "Perrysburg takes leaves through its yard-waste program. The city's yard waste page lists leaves among materials collected in paper yard waste bags or resident-purchased carts, each with an official city yard waste tag, on regular garbage days from April 1 through November 30 and by request on Wednesdays from December 1 through March 31. That page does not describe a loose-leaf curb pickup."),
        ('Who can use Maumee leaf collection?', "The City of Maumee says its fall leaf collection is for owner-occupied homes with two or fewer units. Rentals, condominiums, apartment buildings, commercial properties, and mobile home parks are not included, and contractors may not place leaves at the curb for city collection."),
        ('What if I miss my city leaf pickup?', 'Do not rake leaves into the street. Toledo lists composting or mulching, the trash container, and city drop-off sites as options after a missed collection. Other cities have their own rules, so check your city\'s leaf collection page. A leaf removal crew can also clear and haul everything in one visit.'),
        ('Does Terramorph leave leaves at the curb for the city?', 'No. Terramorph loads the leaves and hauls them away, so there is no pile at the curb and no city schedule to track.'),
        ('Can I just mulch the leaves with a mower?', 'A light layer, yes. Once leaves build up past about two inches, Ohio State University Extension recommends removing them, because a thick mat blocks light and can leave thin patches and snow mold by spring.'),
    ],
}
LEAF_GUIDE['sections'] = [(h, _light(body)) for h, body in LEAF_GUIDE['sections']]
LEAF_GUIDE_SEO_TITLE = 'Toledo & Perrysburg Leaf Collection vs. Hiring a Crew | Terramorph'
LEAF_GUIDE_CARD = (LEAF_GUIDE_FILE, 'Seasonal guide', 'City Leaf Collection vs. Hiring a Crew', 'How leaf pickup works in Toledo, Perrysburg, and Maumee, and when hauling makes more sense.')

# ---------------------------------------------------------------------------
# Lawn care town pages: Toledo, Perrysburg, Maumee
# ---------------------------------------------------------------------------
LAWN_TOWNS = [
    {
        'city': 'Toledo', 'slug': 'toledo', 'hero': 'real-brick-home-stripes.webp',
        'title': 'Lawn Care & Maintenance in Toledo, OH | Terramorph',
        'h1': 'Lawn care in Toledo for older lots, big shade trees, and tight side yards.',
        'desc': 'Lawn care and lawn mowing service in Toledo, OH: mowing, edging, trimming, and bed upkeep for city lots, shaded yards, and commercial frontage. Free estimates.',
        'lead': 'Toledo lawn mowing services from a local crew: mowing, edging, string trimming, and bed upkeep on a set schedule for homes and businesses across West Toledo, South Toledo, and the neighborhoods in between. Free estimates.',
        'answer_h2': 'Yes, Terramorph mows and maintains lawns in Toledo.',
        'answer_p': 'Recurring lawn maintenance covers mowing at the right height for the season, edging along walks and drives, trimming around fences, trees, and everything the mower cannot reach, and blowing the clippings off the hard surfaces before the crew leaves. Bed weeding and upkeep can be added so the whole front of the property stays kept, not only the grass.',
        'answer_items': [
            ('Homes, rentals, and businesses', 'Residential lawns and commercial frontage are both part of the route.'),
            ('Backyards and side yards planned ahead', 'Gates, fences, and narrow passes are looked at during the estimate, so the crew arrives knowing how each part of the lawn gets cut.'),
            ('One crew through the year', 'The same company handles fall aeration and overseeding, leaf removal, and snow.'),
            ('Free estimates', 'Send the address and a few photos, or call and talk it through.'),
        ],
        'local_h2': 'What makes Toledo lawns different from the suburbs around them.',
        'local_paras': [
            'Most Toledo lawns sit on older lots. In neighborhoods like the Old West End, Old Orchard, Westgate, Beverly, and Point Place, the houses are close together, the side yards are narrow, and a detached garage or a fenced backyard is common. That changes how a lawn gets cut. There is more trimming and edging for every square foot of grass, there are gates to plan around, and there is nowhere for sloppy work to hide.',
            'The trees are older too. Mature oaks and maples shade a lot of Toledo front yards, and grass in heavy shade grows thinner and slower than grass in full sun. Shaded lawns do better cut a little taller and overseeded with shade-tolerant fescue in the fall, and they need the leaves cleared before winter so the turf is not smothered.',
            'Soil is the third piece. Much of Toledo is built on old lakebed clay that packs tight and drains slowly, so lawns compact under foot traffic and stay soft after rain. Toward the west side of the city the ground turns sandier as it nears the Oak Openings region, and those lawns dry out faster in July and August. We look at which one you have before recommending anything beyond mowing.',
        ],
        'local_items': [
            ('Narrow side yards and gates', 'Trimmed by hand where a mower does not fit.'),
            ('Heavy shade', 'Cut taller, and overseeded with shade-tolerant seed in fall when it thins.'),
            ('Compacted clay', 'Fall core aeration opens it up so water and air reach the roots.'),
            ('Tree lawns and sidewalks', 'The strip between the sidewalk and the street is mowed and edged with the rest.'),
            ('Commercial frontage', 'Storefronts and offices along corridors like Secor Road, Reynolds Road, and Sylvania Avenue kept presentable through the season.'),
        ],
        'scope_h2': 'Lawn care in Toledo that connects to the rest of the property.',
        'scope_p': 'Mowing is the weekly part. Most Toledo properties need two or three other things over a year, and it is simpler when the crew that already knows the yard does them.',
        'scope_items': [
            ('Thin or compacted lawn', '<a href="lawn-aeration-overseeding-northwest-ohio.html">Core aeration and overseeding</a> in early fall.'),
            ('Bushes over the windows', '<a href="shrub-hedge-trimming-northwest-ohio.html">Shrub and hedge trimming</a>, timed for each plant.'),
            ('Leaves from the big trees', '<a href="leaf-removal-toledo-ohio.html">Leaf removal in Toledo</a>, hauled away.'),
            ('Tired front beds', 'New beds, plantings, and mulch start on the <a href="landscaping-toledo-ohio.html">Toledo landscaping</a> page.'),
            ('Winter', '<a href="snow-removal-toledo-ohio.html">Snow removal in Toledo</a> on a seasonal agreement.'),
        ],
        'faqs': [
            ('Do you offer lawn mowing service in Toledo?', 'Yes. Terramorph provides recurring lawn mowing, edging, and trimming for homes, rentals, and businesses in Toledo, with bed upkeep available on the same visit. Estimates are free.'),
            ('Can you mow a small city lot with a fenced backyard?', 'Yes. Compact lots, fenced backyards, and narrow side yards are common in Toledo. Mention gates, pets, and anything tight when you request the estimate so the crew plans for it.'),
            ('Why is the grass so thin under my trees?', 'Shade and tree roots. Grass under mature trees gets less light and competes with the roots for water. Cutting it taller, clearing leaves in fall, and overseeding with shade-tolerant fine fescue all help. In very deep shade, a mulched bed or groundcover is often a better answer than fighting for grass.'),
            ('How tall should a lawn in Toledo be cut?', 'The cool-season grasses grown in Northwest Ohio do best at about three to three and a half inches for most of the season, with no more than a third of the blade removed in one cut. Shaded lawns do better toward the taller end.'),
            ('Do you take care of commercial properties and rentals in Toledo?', 'Yes. Terramorph maintains commercial frontage and rental properties as well as owner-occupied homes, and can scope mowing together with bed maintenance, seasonal cleanups, and snow removal.'),
            ('Is lawn care year-round?', 'Mowing runs from spring into fall. Aeration and overseeding happen in early fall, leaf removal in November, and snow service through the winter, so the same company can cover the property all year.'),
        ],
    },
    {
        'city': 'Perrysburg', 'slug': 'perrysburg', 'hero': 'real-navy-home-stripes.webp',
        'title': 'Lawn Care & Maintenance in Perrysburg, OH | Terramorph',
        'h1': 'Lawn care in Perrysburg, Ohio, from the crew based here.',
        'desc': 'Lawn care and lawn mowing in Perrysburg, Ohio from a Perrysburg-based crew: mowing, edging, trimming, and bed upkeep for subdivision and larger lawns. Free estimates.',
        'lead': 'Lawn mowing in Perrysburg, Ohio, with edging, trimming, and bed upkeep on a set schedule. Terramorph is based on North Dixie Highway, and Perrysburg lawns are the ones our crews know best. Free estimates.',
        'answer_h2': 'Terramorph is a Perrysburg lawn care company, and mowing is where most properties start.',
        'answer_p': 'A maintenance visit covers the mowing, edging along the walk, drive, and curb, trimming around mailboxes, fences, trees, and beds, and blowing off the hard surfaces. Bed weeding and upkeep can be added, and the same crew can take the property through aeration, leaf season, and snow.',
        'answer_items': [
            ('Based in Perrysburg', 'The shop is at 23090 North Dixie Highway. This is home, not the edge of a service area.'),
            ('Edges that hold up to a close look', 'Walks, drives, curbs, and bed lines edged, because that is what the street sees.'),
            ('Subdivision lots and bigger lawns', 'From quarter-acre lots to wide-open lawns in the township.'),
            ('Free estimates', 'Send the address and a few photos, or call and talk it through.'),
        ],
        'local_h2': 'Perrysburg lawns are flat, open, and sitting on Black Swamp clay.',
        'local_paras': [
            'Perrysburg sits on the edge of the old Great Black Swamp. The ground is flat, and the soil underneath is heavy clay that holds water in spring and bakes hard in August. Almost everything about caring for a lawn here comes back to that.',
            'In the newer subdivisions near Levis Commons, Fort Meigs, Roachton Road, and Hull Prairie Road, the clay is often right under a thin layer of builder topsoil, and it was packed down by construction equipment before the sod or seed went on. Those lawns look fine for a year or two. Then they thin out, puddle after rain, and brown early in summer. Mowing at the right height helps. Fall core aeration and overseeding is usually what turns them around.',
            'Open lots also mean full sun and wind. Grass in full sun grows fast in May and June and needs a steady schedule so it is never cut too short in one pass. In July heat it slows down, and leaving it taller keeps the soil shaded and the roots cooler.',
            'Older Perrysburg is different. Near downtown, Front Street, and River Road, the lots have mature trees, deeper shade, and established beds, and the work is more about trimming, edges, and moving carefully around plantings.',
        ],
        'local_items': [
            ('New-construction lawns', 'Thin topsoil over compacted clay. Aeration and seed do more than extra fertilizer.'),
            ('Neighborhood standards', 'Crisp edges along the walk, drive, and curb, and clippings blown off before the crew leaves.'),
            ('Wet spots after rain', 'Flat clay lots hold water. Puddles that last are a <a href="drainage-solutions-perrysburg-ohio.html">drainage question</a>, and we look at those too.'),
            ('Full sun in summer', 'Cut taller in the heat so the lawn holds its color longer.'),
            ('Larger lawns', 'Open lots mowed with commercial stand-on mowers.'),
        ],
        'scope_h2': 'Perrysburg lawn care, plus the work that comes with the seasons.',
        'scope_p': 'Because the shop is in Perrysburg, the same crews are in these neighborhoods all year. Most lawn care clients add one or two of these as the seasons change.',
        'scope_items': [
            ('Thin lawn on a newer lot', '<a href="lawn-aeration-overseeding-northwest-ohio.html">Core aeration and overseeding</a> in early fall.'),
            ('Foundation shrubs and hedges', '<a href="shrub-hedge-trimming-northwest-ohio.html">Shrub and hedge trimming</a> so the beds match the lawn.'),
            ('Leaf season', '<a href="leaf-removal-perrysburg-ohio.html">Leaf removal in Perrysburg</a>, hauled away instead of bagged and tagged.'),
            ('New beds or a front-yard update', 'See <a href="landscaping-perrysburg-ohio.html">landscaping in Perrysburg</a>.'),
            ('Winter', '<a href="snow-removal-perrysburg-ohio.html">Snow removal in Perrysburg</a> on a seasonal agreement.'),
        ],
        'faqs': [
            ('Do you offer lawn mowing in Perrysburg, Ohio?', 'Yes. Terramorph is based in Perrysburg and provides recurring lawn mowing, edging, and trimming for homes and businesses here, with bed upkeep available on the same visit. Estimates are free.'),
            ('My lawn in a newer Perrysburg subdivision is thin and puddles after rain. Is that normal?', 'It is common. Newer lots often have a thin layer of topsoil over clay that was compacted during construction, so roots stay shallow and water sits on top. Core aeration and overseeding in early fall is the usual first step. If water stands for days, the grading or drainage should be looked at as well.'),
            ('Will the lawn meet my HOA standards?', 'Every association writes its own rules, so share them when you request the estimate. In practice those standards come down to regular mowing, clean edges along the walk, drive, and curb, and tidy beds, and all of that is part of the service.'),
            ('When does mowing season start and end in Perrysburg?', 'Mowing usually starts in April, once the grass is growing and the ground is firm enough to carry a mower, and runs into late October or November, when the last cuts overlap with leaf cleanup. The weather moves both ends a little each year.'),
            ('Can you handle the lawn and the landscape beds together?', 'Yes. Weeding, bed edging, shrub trimming, and mulch can be scoped with mowing so one crew is responsible for how the whole property looks.'),
            ('Do you also do snow removal in Perrysburg?', 'Yes. Seasonal snow removal for driveways, walks, and commercial lots is available, and many lawn care clients keep the same company through the winter.'),
        ],
    },
    {
        'city': 'Maumee', 'slug': 'maumee', 'hero': 'real-curved-beds-stripes.webp',
        'title': 'Lawn Care & Maintenance in Maumee, OH | Terramorph',
        'h1': 'Lawn care in Maumee for shaded yards and established neighborhoods near the river.',
        'desc': 'Lawn care and mowing in Maumee, OH: mowing, edging, trimming, and bed upkeep for shaded, established lots near Uptown, the river, and Side Cut. Free estimates.',
        'lead': 'Lawn mowing service in Maumee with edging, trimming, and bed upkeep on a set schedule, for homes near Uptown and the river and for business properties across town. Free estimates.',
        'answer_h2': 'Terramorph provides lawn care and mowing in Maumee, a few minutes from our Perrysburg shop.',
        'answer_p': 'Maumee is just across the river from where our trucks start the day. A maintenance visit covers mowing, edging along walks and drives, trimming around trees, fences, and beds, and blowing off the hard surfaces. Bed weeding and upkeep can be added to the same visit.',
        'answer_items': [
            ('Shaded lawns understood', 'Height and seed choices made for lawns that live under big trees.'),
            ('Careful around roots and trunks', 'Deck height adjusted over surface roots, and trunks trimmed around, not into.'),
            ('Homes and business properties', 'Established neighborhoods and office or retail frontage.'),
            ('Free estimates', 'Send the address and a few photos, or call and talk it through.'),
        ],
        'local_h2': 'Maumee lawns grow under old trees and close to the river.',
        'local_paras': [
            'Maumee is an older, settled town, and its lawns show it. Around Uptown, along River Road and Ford Street, and in the neighborhoods near Side Cut Metropark, the trees are tall, the lots are established, and many houses sit close enough together that only a trimmer fits down the side yard.',
            'Shade is the main thing. A lawn that gets fewer than about four hours of direct sun grows thin no matter how well it is mowed, and moss and bare patches follow. Cutting it shorter makes that worse. Shaded turf does better left a little taller, kept clear of leaves in fall, and overseeded with shade-tolerant fine fescue when it thins.',
            'Tree roots are the second thing. Big maples in particular send roots along the surface, so the lawn is bumpy, the soil under the canopy is dry, and a mower deck set too low will scalp the high spots. A crew that knows the yard raises the deck there and trims around the base of the tree by hand.',
            'Closer to the river, the ground can stay damp well into spring, and mowing soft clay leaves ruts that last all summer. Timing the first cuts for when the ground will carry a mower matters more than starting on a calendar date. Across town, the office and retail properties around Arrowhead Park and Monclova Road need the opposite: a steady schedule that keeps the frontage presentable every week.',
        ],
        'local_items': [
            ('Deep shade', 'Cut taller, kept clear of leaves, and overseeded with fine fescue when it thins.'),
            ('Surface roots', 'Deck height raised over high spots so they are not scalped.'),
            ('Soft ground in spring', 'First cuts timed to the ground, not the calendar, to avoid ruts.'),
            ('Tight side yards', 'Trimmed by hand where a mower does not fit between houses.'),
            ('Business frontage', 'Office and retail properties kept on a steady schedule.'),
        ],
        'scope_h2': 'Maumee lawn care, and what usually goes with it.',
        'scope_p': 'Shaded, established yards need a little more than mowing to look their best. These are the services Maumee lawn care clients add most.',
        'scope_items': [
            ('Thin, mossy, or compacted lawn', '<a href="lawn-aeration-overseeding-northwest-ohio.html">Core aeration and overseeding</a> with a shade blend in early fall.'),
            ('Overgrown foundation shrubs', '<a href="shrub-hedge-trimming-northwest-ohio.html">Shrub and hedge trimming</a> to bring them back in scale.'),
            ('Heavy leaf drop', '<a href="leaf-removal-maumee-ohio.html">Leaf removal in Maumee</a>, including the rentals and businesses the city program does not cover.'),
            ('Beds that need a refresh', 'See <a href="landscaping-maumee-ohio.html">landscaping in Maumee</a>.'),
            ('Winter', '<a href="snow-removal-maumee-ohio.html">Snow removal in Maumee</a> on a seasonal agreement.'),
        ],
        'faqs': [
            ('Do you offer lawn mowing service in Maumee?', 'Yes. Terramorph provides recurring lawn mowing, edging, and trimming for homes and businesses in Maumee, with bed upkeep available on the same visit. Estimates are free.'),
            ('Why does moss keep taking over my shaded lawn?', 'Moss fills in where grass is struggling, usually because of shade, compacted soil, or ground that stays damp. Raking it out is temporary. Aerating, overseeding with a shade-tolerant blend, and mowing taller improve the conditions. Where it is simply too dark for grass, a mulched bed or groundcover is the lasting fix.'),
            ('Can you mow around big tree roots without scalping the lawn?', 'Yes. The deck is raised over high spots and surface roots, and the area around the base of the tree is trimmed by hand so the trunk is not hit.'),
            ('When do you start mowing in spring?', 'Usually in April, once the grass is growing and the ground is firm. Lawns near the river can stay soft longer, and mowing them too early leaves ruts, so the first cut is timed to the ground.'),
            ('Do you maintain rental and commercial properties in Maumee?', 'Yes. Terramorph maintains rentals and commercial frontage as well as owner-occupied homes. Because the City of Maumee leaf collection does not include rentals or commercial properties, those owners often add leaf removal in the fall.'),
            ('What else can be handled along with lawn care?', 'Fall aeration and overseeding, shrub and hedge trimming, bed maintenance and mulch, leaf removal, and seasonal snow removal can all be scoped with mowing.'),
        ],
    },
]
LAWN_FILES = [f"lawn-maintenance-{t['slug']}-ohio.html" for t in LAWN_TOWNS]


def lawn_town_file(city):
    """Lawn care town page built here for this city, or None."""
    return next((f"lawn-maintenance-{t['slug']}-ohio.html" for t in LAWN_TOWNS if t['city'] == city), None)


def build_lawn_town_pages(ctx):
    """Write the three lawn care town pages. Returns {filename: (city, service, h1, desc)} for hub cards."""
    root, page, schema_for = ctx['root'], ctx['page'], ctx['schema_for']
    quote_form, trust_band, review_stack, faq_section = ctx['quote_form'], ctx['trust_band'], ctx['review_stack'], ctx['faq_section']
    PHONE, TEL = ctx['PHONE'], ctx['TEL']
    meta = {}

    def items(pairs):
        return ''.join(f'<div><b>{b}</b><span>{s}</span></div>' for b, s in pairs)

    for t in LAWN_TOWNS:
        city, filename = t['city'], f"lawn-maintenance-{t['slug']}-ohio.html"
        others = [(f"lawn-maintenance-{o['slug']}-ohio.html", f"{o['city']} lawn care", f"Lawn Care in {o['city']}", o['desc']) for o in LAWN_TOWNS if o['city'] != city]
        related = ''.join(f'<a class="guide-card" href="{h}"><span>{c}</span><h3>{h3}</h3><p>{d}</p><b>Open page &rarr;</b></a>' for h, c, h3, d in [
            ('lawn-maintenance.html', 'Service page', 'Lawn Maintenance', 'What recurring lawn maintenance from Terramorph covers across Wood and Lucas County.'),
            (AERATION_FILE, 'Lawn service', 'Lawn Aeration and Overseeding', 'Core aeration and seed for thin, compacted clay lawns. Best done in early fall.'),
            (SHRUB_FILE, 'Bed service', 'Shrub and Hedge Trimming', 'Shrubs, bushes, and hedges shaped at the right time for each plant.'),
            ('seasonal-cleanups.html', 'Seasonal', 'Leaf Removal and Fall Cleanup', 'Leaves cleared and hauled away, beds cut back, lawn ready for winter.'),
        ] + others)
        local_paras = ''.join(f'<p>{p}</p>' for p in t['local_paras'])
        body = f'''
<section class="page-hero premium-page-hero city-service-hero">
  <div class="page-hero-image"><img src="assets/{t['hero']}" alt="Striped lawn maintained by Terramorph, serving {city}, Ohio"></div><div class="hero-overlay"></div>
  <div class="container page-hero-content"><p class="crumb"><a href="index.html">Home</a> / <a href="lawn-maintenance.html">Lawn Maintenance</a> / {city}</p><p class="eyebrow light">Lawn care in {city}, Ohio</p><h1>{t['h1']}</h1><p>{t['lead']}</p><div class="cta-row"><a class="btn btn-gold" href="#quote">Request a {city} Lawn Care Estimate</a><a class="btn btn-outline-light" href="tel:{TEL}">Call {PHONE}</a></div></div>
</section>
{trust_band()}
<section class="section"><div class="container local-grid"><div><p class="eyebrow">Answer first</p><h2>{t['answer_h2']}</h2><p>{t['answer_p']}</p></div><div class="authority-list">{items(t['answer_items'])}</div></div></section>
<section class="section clay-section" id="local"><div class="container local-grid"><div><p class="eyebrow">{city} lawns</p><h2>{t['local_h2']}</h2>{local_paras}</div><div class="authority-list">{items(t['local_items'])}</div></div></section>
<section class="section" id="related-services"><div class="container local-grid"><div><p class="eyebrow">Beyond mowing</p><h2>{t['scope_h2']}</h2><p>{t['scope_p']}</p></div><div class="authority-list">{_light(items(t['scope_items']))}</div></div></section>
{faq_section(t['faqs'])}
<section class="section guide-index-section"><div class="container section-heading compact"><p class="eyebrow">Keep reading</p><h2>Lawn care and seasonal services nearby.</h2></div><div class="container guide-grid">{related}</div></section>
<section class="section quote-section"><div class="container quote-grid">{quote_form(f'Request a {city} Lawn Care Estimate', service='Lawn Maintenance')}<div class="cta-proof"><p class="eyebrow">Why homeowners reach out</p><h2>A crew that shows up on schedule and leaves the property sharp.</h2>{review_stack(2, 'Lawn Maintenance')}</div></div></section>
'''
        schema = schema_for(filename, t['title'], t['desc'], t['faqs'], 'Lawn Maintenance', extra_services=['Lawn Mowing'],
                            crumb_parent=('lawn-maintenance.html', 'Lawn Maintenance'), crumb_name=f'Lawn Care in {city}')
        (root / filename).write_text(page(t['title'], t['desc'], body, schema))
        meta[filename] = (city, 'Lawn Care', t['h1'], t['desc'])
    return meta


def town_cards(city):
    """Extra cards for a town's landscaping / drainage / patio pages: its lawn care and leaf removal pages."""
    slug = city.lower().replace(' ', '-')
    cards = []
    lawn = next((t for t in LAWN_TOWNS if t['city'] == city), None)
    if lawn:
        cards.append((f'lawn-maintenance-{slug}-ohio.html', f'{city} &middot; Lawn Care', lawn['h1'], lawn['desc']))
    if city == 'Toledo':
        cards.append(('leaf-removal-toledo-ohio.html', 'Toledo &middot; Leaf Removal', LEAF_TOLEDO[3], LEAF_TOLEDO[4]))
    elif city in ('Perrysburg', 'Maumee'):
        cards.append((f'leaf-removal-{slug}-ohio.html', f'{city} &middot; Leaf Removal', f'Leaf removal and fall cleanup in {city}.', 'Leaves cleared from the lawn, beds, and fence lines and hauled away. Free estimates.'))
    return ''.join(f'<a class="guide-card city-service-card" href="{h}"><span>{c}</span><h3>{h3}</h3><p>{d}</p><b>Open local page &rarr;</b></a>' for h, c, h3, d in cards)

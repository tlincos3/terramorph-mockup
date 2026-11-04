"""V3.45 SEO/ad expansion pages for Terramorph.

This module is called by build_pages.py after the base site generation. It keeps
high-volume local SEO/ad pages out of the core generator while still making the
build reproducible.
"""


def generate(ctx):
    root = ctx['root']
    page = ctx['page']
    schema_for = ctx['schema_for']
    quote_form = ctx['quote_form']
    trust_band = ctx['trust_band']
    review_stack = ctx['review_stack']
    faq_section = ctx['faq_section']
    meta_landing_page = ctx['meta_landing_page']
    PHONE = ctx['PHONE']
    TEL = ctx['TEL']
    BASE_URL = ctx['BASE_URL']
    DEFAULT_FAQS = ctx['DEFAULT_FAQS']

    cities = ['Sylvania', 'Bowling Green', 'Holland', 'Waterville', 'Whitehouse', 'Oregon', 'Rossford']
    notes = {
        'Sylvania': 'mature neighborhoods, shaded lawns, established beds, and curb appeal upgrades near Toledo-area homes',
        'Bowling Green': 'open lots, rental and owner-occupied properties, wind exposure, campus-area maintenance needs, and flat drainage conditions',
        'Holland': 'suburban yards, commercial frontage, bed refreshes, maintenance routes, and drainage patterns around drives and patios',
        'Waterville': 'river-area moisture patterns, wooded lots, established neighborhoods, and outdoor living upgrades that need careful water planning',
        'Whitehouse': 'larger yards, new construction edges, bed installation, lawn maintenance, and practical drainage planning',
        'Oregon': 'lake-effect weather, flat lots, commercial frontage, wet yards, and seasonal maintenance needs',
        'Rossford': 'older lots, compact yards, patio transitions, front-bed curb appeal, and runoff around drives or garages',
    }
    # Each service rotates through a pool of real project photos so nearby
    # city pages don't all repeat one image.
    service_defs = [
        ('Landscape Design', 'landscaping', 'landscaping', 'Landscape design, bed refreshes, plantings, mulch, rock, cleanup, lighting coordination, and curb appeal planning',
         ['real-mature-front-bed.webp', 'real-entry-columns-bed.webp', 'real-estate-front-bed.webp', 'real-entry.webp?v=3.14', 'real-arborvitae-row.webp', 'real-block-border-bed.webp', 'real-entry-paver-edge.webp']),
        ('Paver Patios and Hardscapes', 'paver-patios', 'paver patios', 'Paver patios, walkways, steps, seating areas, hardscape upgrades, fire pit areas, and outdoor living plans',
         ['real-modern-stone-wall.webp', 'real-retaining-block.webp', 'real-patio.webp?v=3.14', 'real-hardscape.webp?v=3.14', 'real-walkway.webp?v=3.14']),
        ('Drainage Solutions', 'drainage-solutions', 'drainage solutions', 'Standing water diagnosis, downspout routing, grading review, low-spot fixes, and drainage planning',
         ['real-drainage.webp', 'real-shoreline-riprap.webp', 'real-hydroseed.webp']),
        ('Lawn Maintenance', 'lawn-maintenance', 'lawn maintenance', 'Mowing, trimming, edging, bed upkeep, cleanup support, and recurring property presentation',
         ['real-striped-lawn-pool.webp', 'real-striped-lawn-lot.webp', 'real-mowing-service.webp', 'real-striped-lawn-deck.webp', 'real-estate-stone-wall.webp', 'real-lawn.webp', 'real-striped-lawn-front.webp']),
    ]

    # Per-service, per-city H1 + meta (2026-11-04). Every line uses only the
    # property facts already on the site (notes above / authority_pass CITY_CONTEXT).
    # Lawn pages deliberately do not sell mowing sign-ups: mowing is not being sold right now.
    CITY_SERVICE_COPY = {
        'Landscape Design': {
            'Sylvania': ("Landscape design for Sylvania's shaded, tree-lined lots.", 'Landscape design and bed refreshes in Sylvania, OH: shade-tolerant plantings, root-aware bed work, and clean curb appeal for established homes. Free estimates from Terramorph.'),
            'Bowling Green': ('Landscaping in Bowling Green for open, wind-exposed lots and rental properties.', 'Landscape design and bed installation in Bowling Green, OH for homes, rentals, and commercial frontage, planned around flat lots and wind exposure. Free estimates.'),
            'Holland': ('Landscaping in Holland: bed refreshes for homes and busy commercial frontage.', 'Landscape design, bed refreshes, and mulch for Holland and Springfield Township homes and businesses along Airport Highway and McCord Road. Free estimates.'),
            'Waterville': ("Landscape design for Waterville's wooded, river-side properties.", 'Landscape design in Waterville, OH planned around wooded lots, river-area moisture, and larger yards, from front beds to outdoor living. Free estimates from Terramorph.'),
            'Whitehouse': ('New-home landscaping in Whitehouse, from builder-grade lot to finished beds.', 'Landscape design and installation in Whitehouse, OH: front beds, plantings, mulch, and sod edges for new-construction and larger lots. Free estimates from Terramorph.'),
            'Oregon': ('Landscaping in Oregon, Ohio built for flat lots and open, wind-exposed yards.', 'Landscape design and bed installation in Oregon, OH for homes and commercial frontage along Navarre Avenue, with drainage checked first on flat lots. Free estimates.'),
            'Rossford': ("Landscaping for Rossford's compact yards and older front beds.", 'Landscape design and front-bed curb appeal in Rossford, OH, sized for compact lots and older homes near Dixie Highway and the Maumee River. Free estimates.'),
        },
        'Paver Patios and Hardscapes': {
            'Sylvania': ('Paver patios and walkways for Sylvania homes under mature trees.', 'Paver patios, walkways, and seat walls in Sylvania, OH, planned around mature trees, roots, and drainage on established lots. Free estimates from Terramorph.'),
            'Bowling Green': ('Paver patios in Bowling Green built on a base that handles flat, wet ground.', 'Paver patios and walkways in Bowling Green, OH with base prep and drainage planned for flat lots. Homes, rentals, and commercial properties. Free estimates.'),
            'Holland': ('Paver patios and walkways for Holland backyards.', 'Paver patios, walkways, and fire pit areas in Holland and Springfield Township, OH, with runoff around drives and patios handled first. Free estimates from Terramorph.'),
            'Waterville': ("Paver patios for Waterville's wooded lots and outdoor living upgrades.", 'Paver patios, seating areas, and walkways in Waterville, OH, planned around larger wooded yards, river-area moisture, and erosion. Free estimates from Terramorph.'),
            'Whitehouse': ("Paver patios for Whitehouse's new homes and large open lots.", 'Paver patios and walkways in Whitehouse, OH for new-construction and larger lots, with builder grading and drainage checked before the base goes in. Free estimates.'),
            'Oregon': ('Paver patios in Oregon, Ohio built for flat lots and winter exposure.', 'Paver patios and walkways in Oregon, OH with drainage and freeze-thaw planned for flat, wind-exposed lots. Homes and businesses. Free estimates from Terramorph.'),
            'Rossford': ("Paver walkways and patios that fit Rossford's compact yards.", 'Paver patios, walkways, and step transitions in Rossford, OH sized for compact lots and older homes, with driveway runoff handled. Free estimates from Terramorph.'),
        },
        'Drainage Solutions': {
            'Sylvania': ("Drainage solutions for Sylvania's shaded, mature lots.", 'Yard drainage in Sylvania, OH: standing water, downspout routing, and grading review around drives, patios, and mature trees. Free estimates from Terramorph.'),
            'Bowling Green': ("Drainage solutions for Bowling Green's flat lots and standing water.", 'Yard drainage in Bowling Green, OH for flat lots that hold water: diagnosis, grading, downspout routing, and low-spot fixes. Free estimates from Terramorph.'),
            'Holland': ("Drainage for Holland's wet lawn pockets and driveway runoff.", 'Yard drainage in Holland and Springfield Township, OH: wet lawn pockets, driveway runoff, and water around patios diagnosed and routed. Free estimates.'),
            'Waterville': ("Drainage and erosion fixes for Waterville's river-side and wooded lots.", 'Yard drainage in Waterville, OH planned for river-area moisture, wooded lots, and erosion on larger yards. Free estimates from Terramorph.'),
            'Whitehouse': ("Drainage for Whitehouse's new-construction lots and builder grading.", 'Yard drainage in Whitehouse, OH: builder-grade grading, standing water on larger lots, and downspout routing fixed before beds or patios go in. Free estimates.'),
            'Oregon': ("Drainage solutions for Oregon's flat lots and wet yards.", 'Yard drainage in Oregon, OH for flat lots and wet yards: diagnosis first, then grading, downspout routing, or drains. Homes and commercial frontage. Free estimates.'),
            'Rossford': ("Drainage fixes for Rossford's garages, driveways, and compact yards.", 'Yard drainage in Rossford, OH: runoff around drives and garages, older grades, and compact yards that hold water. Free estimates from Terramorph.'),
        },
        'Lawn Maintenance': {
            'Sylvania': ("Lawn and bed maintenance for Sylvania's shaded, established properties.", 'Lawn maintenance in Sylvania, OH: trimming, edging, and bed upkeep for shaded lawns and established beds. Free estimates from Terramorph.'),
            'Bowling Green': ('Lawn maintenance for Bowling Green rentals, homes, and commercial frontage.', 'Lawn maintenance in Bowling Green, OH for owner-occupied homes, rentals, campus-area properties, and commercial frontage. Free estimates from Terramorph.'),
            'Holland': ('Lawn maintenance for Holland homes and commercial corridors.', 'Lawn maintenance in Holland and Springfield Township, OH: trimming, edging, bed upkeep, and commercial frontage along Airport Highway. Free estimates.'),
            'Waterville': ("Lawn maintenance for Waterville's larger, wooded yards.", 'Lawn maintenance in Waterville, OH: trimming, edging, and bed upkeep for larger wooded lots and established neighborhoods. Free estimates from Terramorph.'),
            'Whitehouse': ("Lawn maintenance for Whitehouse's larger lots and new homes.", 'Lawn maintenance in Whitehouse, OH for larger lots and new-construction homes: trimming, edging, sod edges, and bed upkeep. Free estimates from Terramorph.'),
            'Oregon': ('Lawn maintenance for Oregon, Ohio homes and commercial frontage.', 'Lawn maintenance in Oregon, OH: trimming, edging, bed upkeep, and seasonal cleanup after wind and storms for homes and commercial frontage. Free estimates.'),
            'Rossford': ("Lawn maintenance for Rossford's compact yards and front beds.", 'Lawn maintenance in Rossford, OH: trimming, edging, and front-bed upkeep for compact yards and older lots. Free estimates from Terramorph.'),
        },
    }

    extra_city_pages = []
    city_page_meta = {}  # filename -> (city, service, headline, desc) for hub cards
    for city_index, city in enumerate(cities):
        city_slug = city.lower().replace(' ', '-')
        for service, service_slug, keyword_service, service_copy, image_pool in service_defs:
            image = image_pool[city_index % len(image_pool)]
            filename = f'{service_slug}-{city_slug}-ohio.html'
            headline, desc = CITY_SERVICE_COPY[service][city]
            lead = f'Terramorph helps {city} homeowners and property owners with {service_copy.lower()} backed by free estimates and phone-first follow-up.'
            angle = f'{city} projects often involve {notes[city]}. Terramorph reviews grade, access, water movement, materials, photos, and timeline before recommending a scope.'
            faqs = [
                (f'Does Terramorph offer {keyword_service} in {city}?', f'Yes. Terramorph serves {city} and nearby Northwest Ohio areas with {keyword_service} and related outdoor property work.'),
                ('Can I request a free estimate by phone?', f'Yes. Call Terramorph at {PHONE} with the service need, property details, photos if available, and timeline.'),
                ('Can photos be included with the request?', 'Yes. Photos are helpful because they show access, grade, existing conditions, water movement, beds, lawn areas, or hardscape details before follow-up.'),
            ]
            city_page_meta[filename] = (city, service, headline, desc)
            body = f'''
<section class="page-hero premium-page-hero city-service-hero">
  <div class="page-hero-image"><img src="assets/{image}" alt="Terramorph {service} in {city}, Ohio"></div><div class="hero-overlay"></div>
  <div class="container page-hero-content"><p class="crumb"><a href="index.html">Home</a> / <a href="service-areas.html">Service Areas</a> / {city} {service}</p><p class="eyebrow light">{keyword_service} in {city}, Ohio</p><h1>{headline}</h1><p>{lead}</p><div class="cta-row"><a class="btn btn-gold" href="#quote">Request a {city} Estimate</a><a class="btn btn-outline-light" href="tel:{TEL}">Call {PHONE}</a></div></div>
</section>
{trust_band()}
<section class="section"><div class="container local-grid"><div><p class="eyebrow">Local fit</p><h2>{city} outdoor work needs local judgment.</h2><p>{angle}</p><p>These local pages help homeowners understand the Terramorph services available in their city before requesting an estimate.</p></div><div class="authority-list"><div><b>Property review</b><span>Service need, city, address, photos, timeline, and visible site conditions.</span></div><div><b>Connected services</b><span>Drainage, patios, beds, lighting, cleanups, and maintenance can be scoped together when it makes sense.</span></div><div><b>Northwest Ohio conditions</b><span>Clay soil, flat lots, freeze-thaw, and heavy rain are considered before recommendations.</span></div><div><b>Fast follow-up</b><span>Quote requests include the details the team needs to respond with the right next step.</span></div></div></div></section>
{faq_section(faqs)}
<section class="section quote-section"><div class="container quote-grid">{quote_form('Request a ' + city + ' ' + service + ' Estimate')}<div class="cta-proof"><p class="eyebrow">Fast estimate path</p><h2>Call with photos, timeline, and service details ready.</h2>{review_stack(2, service)}</div></div></section>
'''
            short_title = f'{service.replace(" and Hardscapes", "")} in {city}, OH | Terramorph'
            (root / filename).write_text(page(short_title, desc, body, schema_for(filename, headline, desc, faqs, service)))
            extra_city_pages.append(filename)

    # ---- Leaf removal + snow removal city pages (2026-11-04) ----------------
    # Same template family as spring-fall-cleanups-toledo-ohio / snow-removal-toledo-ohio
    # (hero, answer-first block, local details, FAQ, related reading, quote), with a
    # real local section per town. Facts come only from this repo and
    # ~/projects/ads-research-2026-10/06-climate-calendar.md (NOAA Toledo Express
    # normals, city leaf-pickup programs). NO prices anywhere on a snow page.
    LEAF_WEATHER = [
        ('First frost: late October', 'Toledo Express Airport sees its first 32°F night around October 24 in a typical year. Annuals finish and perennials start going dormant.'),
        ('Hard freeze: early November', 'The first 28°F freeze typically lands November 4, with the first 24°F night around November 16. Hard freezes knock the last leaves down.'),
        ('Peak leaf drop: mid to late November', "Terramorph's own leaf jobs ramp up the last week of October and peak the third and fourth weeks of November, so that is when the main visit happens."),
        ('First snow: late November', 'The first measurable snow typically arrives around November 22. Wet leaves that freeze to the lawn under it stay there until spring.'),
        ('Leaves past two inches come off', 'Ohio State University Extension recommends removing leaves once they build up past about two inches, before they mat and smother the lawn.'),
    ]
    SNOW_WEATHER = [
        ('First plowable storm: mid-December', 'In 31 winters of Toledo Express Airport records, the first 2-inch snow day lands around December 12 in a typical year, and as early as November 11.'),
        ('Last plowable storm: early March', 'The last 2-inch day typically falls around March 7, and has come as late as late April.'),
        ('About four plowable storms a winter', 'The last ten winters averaged about four plowable storms. Big winters bring ten or more, which is why routes are built with room to run every storm.'),
        ('Storm systems, not lake effect', 'Northwest Ohio is not in the snowbelt. The lake-effect snow here is usually under an inch; the plowable storms come from large systems moving through.'),
        ('March is the worst for ice', 'March averages the most freeze-thaw days of any month (about 17), so walks and entries keep refreezing after the plowing is done.'),
    ]
    LEAF_CITIES = [
        # city, slug, hero photo, H1, meta, local heading, local paragraphs, city FAQ
        ('Perrysburg', 'perrysburg', 'real-fall-leaf-crew.webp',
         'Leaf removal in Perrysburg, hauled away instead of bagged at the curb.',
         'Leaf removal and fall cleanup in Perrysburg, OH. Leaves blown out of lawns, beds, and fence lines and hauled off, no bags or tags. Perrysburg-based crew. Free estimates.',
         'Perrysburg leaves go out as tagged bags, or they go with us.',
         ["Perrysburg's yard-waste program takes leaves as tagged bags or toters on the weekly route through November 30, then by request only on Wednesdays from December through March. Bagging a wooded Perrysburg lot is a weekend of work before the tags are even paid for.",
          'Terramorph is based in Perrysburg. Our crews blow the leaves out of the lawn, the beds, the fence lines, and from under the shrubs, load them, and haul them away. Nothing sits at the curb.',
          'Newer subdivisions near Levis Commons, Fort Meigs, River Road, and Roachton Road have flat lots and HOA curb-appeal expectations, so the cleanup also includes bed edges and a final mow when it is part of the plan.'],
         [('Does Perrysburg pick up leaves at the curb?', "Perrysburg's yard-waste program takes leaves as tagged bags or toters on the weekly route through November 30, then by request only on Wednesdays in December through March. Terramorph hauls leaves away instead, so there is no bagging or tagging."),
          ('When should a Perrysburg leaf cleanup be scheduled?', 'Book in September or October. The main visit happens in the second half of November, after the first hard freezes (typically November 4 and November 16) have brought down most of the leaves. Wooded lots often get one more pass.')]),
        ('Maumee', 'maumee', 'real-fall-windstorm-blower.webp',
         'Leaf removal in Maumee for shaded lots, rentals, and the properties the city truck skips.',
         'Leaf removal in Maumee, OH. City curbside pickup is owner-occupied homes only; Terramorph hauls leaves for any property, rentals and businesses included. Free estimates.',
         "Maumee's leaf truck only serves owner-occupied homes.",
         ["Maumee's fall leaf collection usually starts in October and runs by district, one set week each. It is for owner-occupied homes only, and anyone paid to remove yard waste is not allowed to use it. Rentals, condos, and commercial properties get no city pickup at all.",
          'Terramorph hauls everything it clears, so a Maumee rental, condo, or storefront is handled the same as a house, and an owner-occupied home does not have to wait for its district week.',
          'Uptown Maumee, River Road, and the neighborhoods near Side Cut Metropark are mature and heavily shaded, with tight access between houses. Backpack blowers reach the side yards and fence lines a walk-behind cannot.'],
         [('Does Maumee collect leaves at the curb?', "Maumee's fall leaf collection is for owner-occupied homes only, by district and set week, and contractors may not use it. Rentals, condos, and commercial properties need private removal, which is what Terramorph provides. Leaves are hauled away with the crew."),
          ('Can you do leaf removal for a Maumee rental or business?', 'Yes. Because Terramorph hauls the leaves, rentals, condos, and commercial properties in Maumee are handled the same way as owner-occupied homes.')]),
        ('Sylvania', 'sylvania', 'real-fall-cleanup-after.webp',
         "Leaf removal in Sylvania for big trees, shaded lawns, and established beds.",
         'Leaf removal and fall cleanup in Sylvania, OH. Mature-tree lots cleared, beds cut back, leaves hauled away. Downtown Sylvania, Olander Park, and nearby. Free estimates.',
         'Sylvania leaf loads come from mature trees, and they come late.',
         ['Sylvania properties have mature trees, shaded lawns, larger homes, and established beds with root competition. That means heavy leaf loads, and the last leaves often come down after the hard freezes in early and mid November.',
          'A thick layer left under the first snow blocks light and can leave matted, thin patches and snow mold by spring. Terramorph clears the lawn, the beds, and under the shrubs, and hauls the leaves away, so there is no city schedule to track.',
          'Crews work neighborhoods around Downtown Sylvania, Olander Park, Centennial Road, Main Street, and Sylvania Avenue.'],
         [('Do Sylvania leaf cleanups need a second visit?', 'Often, yes. Mature-tree lots drop the last leaves after the hard freezes in early and mid November, so heavily wooded Sylvania properties frequently book one more pass before the first lasting snow.'),
          ('Do you work around established beds and roots?', 'Yes. Leaves are blown out of the beds and from under shrubs, spent perennials are cut back, and spring-flowering shrubs are left alone so next year\'s buds stay on.')]),
        ('Bowling Green', 'bowling-green', 'real-fall-finished-lawn.webp',
         'Leaf removal in Bowling Green for open lots, rentals, and campus-area properties.',
         'Leaf removal and fall cleanup in Bowling Green, OH. Leaves cleared and hauled away for homes, rentals, and storefronts near BGSU, no waiting on city rounds. Free estimates.',
         "Bowling Green's city leaf rounds start late.",
         ["In 2025, Bowling Green's first round of curbside leaf collection began November 10 and the final round began December 8, with loose leaves set at the curb. On an open, wind-exposed lot, a pile at the curb does not stay a pile for long.",
          'Terramorph clears and hauls in one scheduled visit, so homes, rentals with tenant turnover, and commercial frontage near BGSU, Wooster Street, Poe Road, and downtown are done without raking to the street and waiting.',
          'Flat drainage is common here, so the cleanup also clears leaves out of the low spots and swales where they would otherwise hold water against the lawn.'],
         [('When does Bowling Green pick up leaves?', 'In 2025 the first round of curbside leaf collection began November 10 and the final round began December 8. Terramorph hauls leaves away on its own schedule, so there is nothing to rake to the curb.'),
          ('Do you handle rentals and commercial properties in Bowling Green?', 'Yes. Rental turnover, campus-area properties, and commercial frontage are common Bowling Green cleanups. Terramorph can scope a one-time cleanup or pair it with recurring maintenance.')]),
        ('Holland', 'holland', 'real-fall-skidsteer-leaves.webp',
         'Leaf removal in Holland and Springfield Township, homes and commercial frontage.',
         'Leaf removal and fall cleanup in Holland, OH. Suburban yards and commercial frontage along Airport Highway and McCord Road, leaves hauled away. Free estimates.',
         'Holland cleanups cover the yard and the frontage.',
         ['Holland and Springfield Township mix suburban yards with high-visibility commercial corridors along Airport Highway, McCord Road, and Angola Road. A storefront or office bed full of leaves reads as neglected fast.',
          'Terramorph clears lawns, beds, and fence lines and hauls the leaves off, for homes in Strawberry Acres and near Homecoming Park as well as business frontage that needs to look kept.',
          'Wet lawn pockets and driveway runoff are common here. Leaves left in those low spots hold water and mat down, so the cleanup gets them out before the ground freezes.'],
         [('Do you do leaf removal for Holland businesses?', 'Yes. Commercial frontage along Airport Highway and McCord Road can be scoped alongside residential cleanups, and the leaves are hauled away with the crew.'),
          ('Why clear leaves out of the wet spots?', 'Leaves that settle in wet lawn pockets hold water, mat down, and smother the grass under them. Clearing them before the ground freezes keeps those spots from coming back thin in spring.')]),
        ('Waterville', 'waterville', 'real-fall-haul-trailer.webp',
         'Leaf removal in Waterville for wooded, river-side lots.',
         'Leaf removal and fall cleanup in Waterville, OH. Wooded lots and larger yards near the Maumee River cleared with commercial blowers and hauled away. Free estimates.',
         'Waterville lots drop a lot of leaves, and the river keeps them wet.',
         ['Waterville properties are often wooded, with larger yards, established neighborhoods, and river-area moisture around Farnsworth Metropark, River Road, and the Anthony Wayne Trail. Wet leaves on a big lot are heavy, slow work by hand.',
          'Terramorph brings commercial walk-behind blowers, backpack crews, and the equipment to load and haul, so a full acre of leaves is cleared in one scheduled visit instead of a string of weekends.',
          'Erosion-prone slopes and drainage-sensitive areas are cleared without stripping the ground, and ornamental grasses or seed heads can stay standing for winter if you want them.'],
         [('Can you clear a large wooded lot in Waterville?', 'Yes. Commercial walk-behind blowers, backpack crews, and haul-off equipment are built for big leaf loads. Heavily wooded lots often book a main visit in the second half of November and one more pass after the last leaves fall.'),
          ('Do you haul the leaves away in Waterville?', 'Yes. Leaves and debris leave with the crew. Nothing is piled at the curb or along the river.')]),
        ('Rossford', 'rossford', 'real-fall-leaf-crew.webp',
         "Leaf removal in Rossford for compact yards and older front beds.",
         'Leaf removal and fall cleanup in Rossford, OH. Compact yards and front beds near Dixie Highway, Eagle Point Colony, and the river cleared and hauled away. Free estimates.',
         'Rossford yards are compact, so the cleanup is about the details.',
         ['Rossford lots are older and compact, with front-bed curb appeal and runoff around drives and garages. Leaves collect against the garage, in the side yard, and in the beds along the front walk.',
          'Terramorph clears the lawn, the beds, and the fence lines, cuts back spent perennials, and hauls everything away. Crews work neighborhoods near Dixie Highway, Eagle Point Colony, Lime City Road, and the Maumee River.',
          'A fall cleanup here often pairs with a bed edge cleanup and a mulch refresh so the front of the house looks finished through winter.'],
         [('Is a small Rossford yard worth a professional cleanup?', 'Yes. Compact yards collect leaves in the beds, side yards, and against the garage where they are slowest to clear by hand. One visit clears, cuts back, and hauls everything.'),
          ('Can the cleanup include the front beds?', 'Yes. Front-bed cleanouts, edge cleanup, and a mulch refresh are common Rossford add-ons so the house looks finished from the street.')]),
        ('Oregon', 'oregon', 'real-fall-windstorm-blower.webp',
         'Leaf removal in Oregon, Ohio after the wind has moved the leaves around.',
         'Leaf removal and fall cleanup in Oregon, OH. Flat, wind-exposed lots and Navarre Avenue frontage cleared and hauled away, storm debris included. Free estimates.',
         'Oregon lots are flat and open, and the wind does not respect property lines.',
         ['Oregon properties are flat, exposed to wind off the open ground and Maumee Bay, and prone to wet yards. Leaves pile against fences and buildings, and storm debris comes with them.',
          'Terramorph clears leaves, sticks, and wind-blown debris from lawns, beds, and fence lines and hauls it all away, for homes near Coy Road, Dustin Road, and Pearson Metropark and for commercial frontage along Navarre Avenue.',
          'On flat lots, leaves settle in the low spots that already hold water. Getting them out before the ground freezes keeps the lawn from going into winter matted and wet.'],
         [('Do you clear storm debris with the leaves in Oregon?', 'Yes. Sticks, fallen branches, and wind-blown debris are cleared and hauled with the leaves.'),
          ('Do you handle commercial frontage in Oregon, Ohio?', 'Yes. Commercial frontage along Navarre Avenue and other Oregon corridors can be scoped alongside residential cleanups.')]),
        ('Ottawa Hills', 'ottawa-hills', 'real-fall-cleanup-after.webp',
         'Leaf removal in Ottawa Hills, cleared and hauled in one visit.',
         'Leaf removal and fall cleanup in Ottawa Hills, OH. Lawns, beds, and fence lines cleared, perennials cut back, leaves hauled away. Free estimates from Terramorph.',
         'Ottawa Hills is inside our core Lucas County route.',
         ['Ottawa Hills borders West Toledo and sits inside the Lucas County area Terramorph covers every week in the fall, alongside Sylvania, Maumee, and Holland.',
          'Terramorph clears the lawn, the beds, the fence lines, and under the shrubs, cuts back spent perennials, leaves spring-flowering shrubs alone, and hauls everything away, so there is no curb schedule to track.',
          'The main visit happens in the second half of November, after the hard freezes in early and mid November bring down most of the leaves. Properties with a lot of trees often book one more pass before the first lasting snow.'],
         [('Does Terramorph serve Ottawa Hills?', 'Yes. Ottawa Hills is one of Terramorph\'s priority service areas in Lucas County, alongside Sylvania, Maumee, Holland, and Toledo.'),
          ('Do you haul the leaves away in Ottawa Hills?', 'Yes. Leaves and debris leave with the crew in the same visit.')]),
    ]
    SNOW_CITIES = [
        # city, slug, H1, meta, local heading, local paragraphs, city FAQ (no prices anywhere)
        ('Perrysburg', 'perrysburg',
         'Snow removal and snow plowing in Perrysburg, from the crew based here.',
         'Snow removal and plowing in Perrysburg, OH: driveways, walks, and commercial lots, plus salting. Perrysburg-based crew. Reserve before the first storm.',
         'Perrysburg is home base for the winter route.',
         ['Terramorph is based in Perrysburg, and Perrysburg driveways, walks, and lots are the core of the winter route, from the newer subdivisions near Levis Commons, Fort Meigs, and Roachton Road to River Road and Five Point Road.',
          'Seasonal snow service covers residential driveways, walkways, steps, and entries, and commercial parking lots, access lanes, and entrances. Salting can be included so walks and entries are safe, not just cleared.',
          'HOA neighborhoods expect a clean drive and walk after every qualifying snowfall. Service is triggered by the depth in your agreement, and routes run so the driveway is open when you need to leave.'],
         [('Do you plow residential driveways in Perrysburg?', 'Yes. Residential driveways, walks, steps, and entries across Perrysburg, plus commercial lots and entrances. One seasonal agreement runs all winter.'),
          ('When does the first plowable snow usually hit Perrysburg?', 'The first 2-inch snow day at Toledo Express Airport typically lands around December 12, and has come as early as November 11. Routes fill in the fall, so sign up before then.')]),
        ('Maumee', 'maumee',
         'Snow removal and snow plowing in Maumee for tight drives and mature neighborhoods.',
         'Snow removal and plowing in Maumee, OH: driveways, walks, and entries in Uptown and river-side neighborhoods, plus commercial lots and salting. Seasonal sign-up.',
         'Maumee driveways are tight, so the plow has to be careful.',
         ['Uptown Maumee, River Road, Ford Street, and the neighborhoods near Side Cut Metropark are mature, with tight access between houses and little room to push snow. The crew plans where the snow goes before the first storm.',
          'Residential service covers the driveway, walks, steps, and entry. Commercial service covers lots, access lanes, and entrances along Monclova Road and the Maumee corridors, with salting available for both.',
          'Service is triggered by the snowfall depth in your agreement, and routes run so driveways are open before work and lots are open before business.'],
         [('Can you plow a narrow Maumee driveway?', 'Yes. Tight access is common in Maumee\'s mature neighborhoods. The crew plans where snow is pushed before the season so drives, walks, and entries are cleared without piling snow where it blocks access.'),
          ('Do you salt walks and entries in Maumee?', 'Yes. Ice management and salting can be included in the seasonal agreement for walks, steps, entries, and commercial lots.')]),
        ('Sylvania', 'sylvania',
         'Snow removal and snow plowing in Sylvania for larger homes and long winters.',
         'Snow removal and plowing in Sylvania, OH: driveways, walks, and entries plus commercial lots and salting near Downtown Sylvania and Centennial Road. Seasonal sign-up.',
         'Sylvania winters run from the first December storm into March.',
         ['Sylvania properties include larger homes with mature trees around Downtown Sylvania, Olander Park, Centennial Road, Main Street, and Sylvania Avenue. A seasonal agreement covers every qualifying snowfall from the first storm to the last.',
          'The last 2-inch snow day at Toledo Express Airport typically falls around March 7, and March averages the most freeze-thaw days of any month, so walks and entries refreeze after the plowing is done. Salting can be part of the plan.',
          'Residential service covers driveways, walks, steps, and entries. Commercial service covers lots, access lanes, and entrances.'],
         [('How late into spring does Sylvania snow service run?', 'The seasonal agreement runs the full winter. The last 2-inch snow day typically falls around March 7 and has come as late as April, so service continues through the end of the season.'),
          ('Do you handle ice on Sylvania walks and drives?', 'Yes. March has the most freeze-thaw days of the year, so salting for walks, steps, entries, and lots can be included so surfaces are safe, not just cleared.')]),
        ('Bowling Green', 'bowling-green',
         'Snow removal and snow plowing in Bowling Green for open lots, rentals, and storefronts.',
         'Snow removal and plowing in Bowling Green, OH: driveways, rentals, campus-area lots, and storefronts near BGSU and downtown, plus salting. Seasonal sign-up.',
         'Bowling Green is flat and open, so the wind keeps working after the storm.',
         ['Bowling Green lots are open and wind-exposed, with flat drainage, rental turnover, campus-area properties, and commercial frontage along Wooster Street, Poe Road, and downtown. Wind moves snow back onto cleared drives and lots.',
          'Seasonal service covers residential driveways, walks, and entries, and commercial lots, access lanes, and entrances. Salting is available so walks and lots stay safe for tenants, customers, and staff.',
          'Service is triggered by the snowfall depth in your agreement, and routes run so lots are open before business and driveways before work.'],
         [('Do you plow rental properties in Bowling Green?', 'Yes. Rentals, campus-area properties, and commercial frontage near BGSU and downtown are common Bowling Green accounts. One seasonal agreement covers the property all winter.'),
          ('Does wind exposure change snow service in Bowling Green?', 'Open, flat lots let wind push snow back onto cleared areas. The crew plans where snow is piled before the season so it is less likely to drift back across the drive or lot.')]),
        ('Holland', 'holland',
         'Snow removal and snow plowing in Holland for homes and commercial corridors.',
         'Snow removal and plowing in Holland, OH: driveways and walks for homes, lots and entrances for businesses along Airport Highway and McCord Road. Seasonal sign-up.',
         'Holland frontage needs to be open before the customers arrive.',
         ['Holland and Springfield Township mix suburban neighborhoods like Strawberry Acres and Homecoming Park with busy commercial corridors along Airport Highway, McCord Road, and Angola Road. A storefront lot that is not open on time loses the morning.',
          'Commercial service covers lots, access lanes, entrances, and sidewalks, with salting. Residential service covers driveways, walks, steps, and entries.',
          'Service is triggered by the snowfall depth in your agreement. Routes run so lots are open before business and driveways before work.'],
         [('Do you plow commercial lots in Holland?', 'Yes. Lots, access lanes, entrances, and sidewalks along Airport Highway, McCord Road, and other Holland corridors, with salting available.'),
          ('Can a Holland home and business be on the same agreement?', 'Each property gets its own seasonal quote with its own trigger depth and scope. Call and the team will set up both.')]),
        ('Rossford', 'rossford',
         'Snow removal and snow plowing in Rossford for compact drives and garages.',
         'Snow removal and plowing in Rossford, OH: compact driveways, garage approaches, and walks near Dixie Highway, plus lots along Crossroads Parkway. Seasonal sign-up.',
         'Rossford drives are short, so the snow has to go somewhere smart.',
         ['Rossford lots are older and compact, with short drives, garage approaches, and little room between houses to pile snow. The crew plans where snow goes before the first storm so the drive, walk, and entry stay clear.',
          'Residential service covers driveways, walks, steps, and entries in neighborhoods near Dixie Highway, Eagle Point Colony, Lime City Road, and the Maumee River. Commercial service covers lots and entrances along Crossroads Parkway.',
          'Service is triggered by the snowfall depth in your agreement, and salting can be included for slick walks and drives.'],
         [('Can you plow a short Rossford driveway without blocking the garage?', 'Yes. Compact lots are common in Rossford. The crew plans where snow is pushed so the garage approach, walk, and entry stay open.'),
          ('Do you serve commercial properties along Crossroads Parkway?', 'Yes. Commercial lots, access lanes, and entrances in Rossford are covered under a seasonal agreement with salting available.')]),
        ('Oregon', 'oregon',
         'Snow removal and snow plowing in Oregon, Ohio for flat, exposed lots.',
         'Snow removal and plowing in Oregon, OH: driveways, walks, and entries for homes near Maumee Bay, plus commercial lots along Navarre Avenue with salting. Seasonal sign-up.',
         'Oregon lots are flat and exposed to winter weather off the bay.',
         ['Oregon properties sit on flat lots exposed to wind and winter weather near Maumee Bay, with commercial frontage along Navarre Avenue and neighborhoods around Coy Road, Dustin Road, and Pearson Metropark.',
          'Residential service covers driveways, walks, steps, and entries. Commercial service covers lots, access lanes, and entrances, with salting so surfaces are safe, not just cleared.',
          'Service is triggered by the snowfall depth in your agreement, and routes run so lots are open before business and driveways before work.'],
         [('Do you plow commercial lots along Navarre Avenue?', 'Yes. Commercial frontage in Oregon, Ohio is covered under a seasonal agreement for lots, access lanes, entrances, and sidewalks, with salting available.'),
          ('When should Oregon homeowners sign up for snow service?', 'Before the first storm. Routes fill in the fall, and the first 2-inch snow day typically lands around December 12, as early as November 11.')]),
    ]
    LEAF_WEATHER_HTML = ''.join(f'<div><b>{b}</b><span>{t}</span></div>' for b, t in LEAF_WEATHER)
    SNOW_WEATHER_HTML = ''.join(f'<div><b>{b}</b><span>{t}</span></div>' for b, t in SNOW_WEATHER)
    leaf_files = [f'leaf-removal-{slug}-ohio.html' for _, slug, *_ in LEAF_CITIES]
    snow_files = [f'snow-removal-{slug}-ohio.html' for _, slug, *_ in SNOW_CITIES]
    seasonal_city_meta = {}  # filename -> (city, kind, h1, desc)
    SEASONAL_FAQS = ctx['SERVICE_FAQS']

    def related_cards(items):
        return ''.join(f'<a class="guide-card" href="{href}"><span>{cat}</span><h3>{t}</h3><p>{d}</p><b>Open page &rarr;</b></a>' for href, cat, t, d in items)

    for city, slug, hero, h1, desc, local_h2, local_paras, city_faq in LEAF_CITIES:
        filename = f'leaf-removal-{slug}-ohio.html'
        title = f'Leaf Removal & Fall Cleanup in {city}, OH | Terramorph'
        faqs = city_faq + [SEASONAL_FAQS['Seasonal Cleanups'][0], SEASONAL_FAQS['Seasonal Cleanups'][3], SEASONAL_FAQS['Seasonal Cleanups'][4]]
        paras_html = ''.join(f'<p>{p}</p>' for p in local_paras)
        others = [(f'leaf-removal-{s}-ohio.html', f'{c} leaf removal', f'Leaf Removal & Fall Cleanup in {c}', d2) for c, s, _, _, d2, *_ in LEAF_CITIES if s != slug][:3]
        related = related_cards([
            ('seasonal-cleanups.html', 'Service page', 'Leaf Removal & Fall Cleanup', 'What a Terramorph fall cleanup includes, the Northwest Ohio timeline, and what a good cleanup leaves alone.'),
            ('fall-cleanup-checklist-northwest-ohio.html', 'Seasonal guide', 'Fall Cleanup Checklist for Northwest Ohio', 'What to clear, cut back, and leave standing before winter.'),
            (f'snow-removal-{slug}-ohio.html' if f'snow-removal-{slug}-ohio.html' in snow_files else 'snow-removal-signup.html', 'Winter service', f'Snow Removal in {city}' if f'snow-removal-{slug}-ohio.html' in snow_files else 'Seasonal Snow Removal Sign-Up', 'Book winter service at the same time so the property is covered from leaf season into snow.'),
        ] + others)
        body = f'''
<section class="page-hero premium-page-hero authority-page-hero"><div class="page-hero-image"><img src="assets/{hero}" alt="Terramorph fall leaf cleanup crew, serving {city}, Ohio"></div><div class="hero-overlay"></div><div class="container page-hero-content"><p class="crumb"><a href="index.html">Home</a> / <a href="seasonal-cleanups.html">Leaf Removal &amp; Fall Cleanup</a> / {city}</p><p class="eyebrow light">Leaf removal in {city}, Ohio</p><h1>{h1}</h1><p>Leaves blown out of the lawn, beds, fence lines, and from under the shrubs, then loaded and hauled away. Spent perennials cut back, debris gone, and the property ready for winter. Free estimates for {city} homes and businesses.</p><div class="cta-row"><a class="btn btn-gold" href="#quote">Request a {city} Leaf Removal Estimate</a><a class="btn btn-outline-light" href="tel:{TEL}">Call {PHONE}</a></div></div></section>
{trust_band()}
<section class="section"><div class="container local-grid"><div><p class="eyebrow">Answer first</p><h2>Terramorph does leaf removal and fall cleanup in {city}, and the leaves leave with the crew.</h2><p>A fall cleanup clears leaves from the lawn, the beds, the fence lines, and under the shrubs, cuts back spent perennials, lightly shapes shrubs, cleans up bed edges, and hauls all of it away. Commercial walk-behind blowers and backpack crews handle big wooded lots in one scheduled visit.</p></div><div class="authority-list"><div><b>Leaves hauled away</b><span>No bagging, no tagging, no waiting on a city truck. Leaves and debris leave with the crew.</span></div><div><b>Beds cut back the right way</b><span>Spent and diseased perennials come out. Lilac, forsythia, and azalea are left alone so next spring's buds stay on.</span></div><div><b>Whole property, one visit</b><span>Lawn, beds, fence lines, under shrubs, sticks and storm debris, and final mows when they are part of the plan.</span></div><div><b>Pairs with winter service</b><span>Many {city} properties book the cleanup and a seasonal snow agreement together.</span></div></div></div></section>
<section class="section clay-section" id="local"><div class="container local-grid"><div><p class="eyebrow">{city} details</p><h2>{local_h2}</h2>{paras_html}</div><div class="authority-list">{LEAF_WEATHER_HTML}</div></div></section>
{faq_section(faqs)}
<section class="section guide-index-section"><div class="container section-heading compact"><p class="eyebrow">Keep reading</p><h2>Leaf removal and winter service nearby.</h2></div><div class="container guide-grid">{related}</div></section>
<section class="section quote-section"><div class="container quote-grid">{quote_form(f'Request a {city} Leaf Removal Estimate', service='Seasonal Cleanups')}<div class="cta-proof"><p class="eyebrow">Why homeowners reach out</p><h2>Crews that show up, clean up, and haul it all away.</h2>{review_stack(2, 'Seasonal Cleanups')}</div></div></section>
'''
        schema = schema_for(filename, title, desc, faqs, 'Leaf Removal', extra_services=['Fall Cleanup'], crumb_parent=('seasonal-cleanups.html', 'Leaf Removal & Fall Cleanup'), crumb_name=f'Leaf Removal in {city}')
        (root / filename).write_text(page(title, desc, body, schema))
        seasonal_city_meta[filename] = (city, 'leaf', h1, desc)

    for city, slug, h1, desc, local_h2, local_paras, city_faq in SNOW_CITIES:
        filename = f'snow-removal-{slug}-ohio.html'
        title = f'Snow Removal & Plowing in {city}, OH | Terramorph'
        faqs = city_faq + [SEASONAL_FAQS['Snow Removal'][0], SEASONAL_FAQS['Snow Removal'][2], SEASONAL_FAQS['Snow Removal'][3]]
        paras_html = ''.join(f'<p>{p}</p>' for p in local_paras)
        others = [(f'snow-removal-{s}-ohio.html', f'{c} snow removal', f'Snow Removal & Plowing in {c}', d2) for c, s, _, d2, *_ in SNOW_CITIES if s != slug][:3]
        leaf_link = f'leaf-removal-{slug}-ohio.html' if f'leaf-removal-{slug}-ohio.html' in leaf_files else 'seasonal-cleanups.html'
        related = related_cards([
            ('snow-removal-signup.html', 'Winter sign-up', 'Seasonal Snow Removal Sign-Up', 'Residential driveways and commercial lots, one winter agreement. Reserve before the first storm.'),
            ('snow-removal.html', 'Service page', 'Snow Removal & Plowing', 'What seasonal snow service covers across Perrysburg, Toledo, Maumee, and Wood and Lucas County.'),
            (leaf_link, 'Fall cleanup', f'Leaf Removal in {city}', 'Book the fall cleanup and winter service together so the property is covered from leaf season into snow.'),
        ] + others)
        body = f'''
<section class="page-hero premium-page-hero authority-page-hero"><div class="page-hero-image"><img src="assets/snow-removal-truck.webp?v=3.17" alt="Terramorph plow truck after a storm, serving {city}, Ohio"></div><div class="hero-overlay"></div><div class="container page-hero-content"><p class="crumb"><a href="index.html">Home</a> / <a href="snow-removal.html">Snow Removal</a> / {city}</p><p class="eyebrow light">Snow removal in {city}, Ohio</p><h1>{h1}</h1><p>Seasonal snow plowing, sidewalk and walkway shoveling, snow blowing, salting, and de-icing for {city} driveways, walkways, entries, and commercial lots. One agreement runs all winter, service is triggered by the snowfall depth you agree to, and routes run so you can get out in the morning. Free estimates.</p><div class="cta-row"><a class="btn btn-gold" href="#quote">Reserve {city} Winter Service</a><a class="btn btn-outline-light" href="tel:{TEL}">Call {PHONE}</a></div></div></section>
{trust_band()}
<section class="section"><div class="container local-grid"><div><p class="eyebrow">Answer first</p><h2>Terramorph plows driveways, walks, and lots in {city} on a seasonal agreement.</h2><p>Residential service covers the driveway, with walkways, steps, and the entry shoveled or snow-blown clear. Commercial service covers parking lots, access lanes, entrances, and sidewalks. Salting and de-icing can be included for both. Winter routes fill in the fall, so reserve a spot before the first storm.</p></div><div class="authority-list"><div><b>Homes and businesses</b><span>Residential driveways and walks, commercial and industrial lots and entrances.</span></div><div><b>Triggered by depth</b><span>Service is triggered by the snowfall depth in your agreement, no call needed after each storm.</span></div><div><b>Ice management</b><span>Salting for walks, entries, drives, and lots so surfaces are safe, not just cleared.</span></div><div><b>Same local crew</b><span>The Terramorph team that handles patios, drainage, and cleanups runs the winter routes too.</span></div></div></div></section>
<section class="section clay-section" id="local"><div class="container local-grid"><div><p class="eyebrow">{city} details</p><h2>{local_h2}</h2>{paras_html}</div><div class="authority-list">{SNOW_WEATHER_HTML}</div></div></section>
{faq_section(faqs)}
<section class="section guide-index-section"><div class="container section-heading compact"><p class="eyebrow">Keep reading</p><h2>Winter service and fall cleanup nearby.</h2></div><div class="container guide-grid">{related}</div></section>
<section class="section quote-section"><div class="container quote-grid">{quote_form(f'Reserve {city} Winter Service', service='Snow Removal')}<div class="cta-proof"><p class="eyebrow">Why property owners reach out</p><h2>Reviews, proof, and a simple seasonal sign-up.</h2>{review_stack(2, 'Snow Removal')}</div></div></section>
'''
        schema = schema_for(filename, title, desc, faqs, 'Snow Removal', extra_services=['Snow Plowing'], crumb_parent=('snow-removal.html', 'Snow Removal'), crumb_name=f'Snow Removal in {city}', service_desc=ctx['SNOW_SERVICE_DESC'])
        (root / filename).write_text(page(title, desc, body, schema))
        seasonal_city_meta[filename] = (city, 'snow', h1, desc)

    case_studies = [
        ('perrysburg-paver-patio-case-study.html','Perrysburg','Paver Patios and Hardscapes','Perrysburg Paver Patio Planning Example','The backyard needed a better place to grill, sit, and connect the house to the lawn without creating drainage or freeze-thaw problems.','Terramorph reviews door transitions, base prep, water movement, access, seating layout, edge restraint, lighting options, and how the patio should tie into beds and lawn.','A clearer patio scope gives the homeowner a usable outdoor living area, cleaner flow, and fewer surprises before installation.','real-patio.webp?v=3.14'),
        ('maumee-yard-drainage-case-study.html','Maumee','Drainage Solutions','Maumee Yard Drainage Planning Example','Water was collecting after rain near low lawn areas, bed edges, and hardscape transitions where Northwest Ohio clay soil slowed drying.','Terramorph traces water sources, downspout paths, grade, discharge options, and whether grading, swales, buried lines, or bed changes make sense.','A practical drainage plan moves water intentionally instead of guessing at a single product.','real-shoreline-riprap.webp'),
        ('toledo-front-yard-curb-appeal-case-study.html','Toledo','Landscape Design','Toledo Front Yard Curb Appeal Planning Example','The front beds looked tired and disconnected from the entry, making the home feel less finished from the street.','Terramorph evaluates bed shape, plant selection, mulch or rock, edging, lighting, maintenance expectations, and how the front walk should feel.','A cleaner first impression with a landscape scope that is easier to maintain and better matched to the house.','real-entry-columns-bed.webp'),
        ('sylvania-landscape-bed-refresh-case-study.html','Sylvania','Landscape Design','Sylvania Landscape Bed Refresh Planning Example','Mature plantings and older bed edges needed a reset without making the property look overbuilt or hard to maintain.','Terramorph reviews sun and shade, soil, existing plant health, bed depth, mulch versus rock, pruning, and replacement planting options.','A cleaner bed design preserves what works and updates what looks dated.','real-mature-front-bed.webp'),
        ('bowling-green-lawn-maintenance-case-study.html','Bowling Green','Lawn Maintenance','Bowling Green Lawn Maintenance Planning Example','The property needed dependable mowing, trimming, and bed upkeep so the outside stayed clean during the growing season.','Terramorph defines route fit, frequency, access, trimming details, bed maintenance needs, and seasonal cleanup add-ons.','A simpler maintenance plan keeps curb appeal steady without the owner chasing one-off work.','real-striped-lawn-lot.webp'),
        ('holland-standing-water-case-study.html','Holland','Drainage Solutions','Holland Standing Water Planning Example','A flat area of lawn stayed wet after storms, limiting use and making maintenance harder.','Terramorph checks roof water, soil compaction, low spots, slope, discharge routes, and whether grading or drainage lines fit the property.','A clearer path to dry the usable lawn area and protect nearby beds or hardscape edges.','real-hydroseed.webp'),
        ('waterville-outdoor-living-case-study.html','Waterville','Paver Patios and Hardscapes','Waterville Outdoor Living Planning Example','The backyard needed a more intentional gathering area that connected patio use, walkways, and landscape beds.','Terramorph maps traffic flow, seating, grill placement, drainage, lighting, bed transitions, and base prep before pricing the project.','A backyard plan feels designed instead of pieced together.','real-hardscape.webp?v=3.14'),
        ('whitehouse-new-construction-landscape-case-study.html','Whitehouse','Landscape Design','Whitehouse New Construction Landscape Planning Example','The home needed front and backyard landscaping after construction so the property felt finished and easier to maintain.','Terramorph reviews grade, soil, builder drainage, bed layout, plant choices, mulch or rock, sod edges, and maintenance goals.','A phased landscape plan improves curb appeal while accounting for drainage and long-term upkeep.','real-estate-front-bed.webp'),
        ('oregon-seasonal-cleanup-case-study.html','Oregon','Seasonal Cleanups','Oregon Seasonal Cleanup Planning Example','Leaf buildup, debris, and overgrown beds made the property look neglected after seasonal weather.','Terramorph scopes cleanup, trimming, debris removal, bed reset, mulch, and recurring maintenance needs.','A cleaner property reset prepares the yard for the next season.','real-mulch.webp'),
        ('rossford-walkway-patio-case-study.html','Rossford','Paver Patios and Hardscapes','Rossford Walkway and Patio Planning Example','The homeowner needed safer movement from the house to outdoor areas with a cleaner hardscape transition.','Terramorph evaluates grade, steps, walkway width, drainage, base prep, edge restraint, and how the hardscape connects to beds and lawn.','A more usable outdoor path and patio area improves curb appeal and reduces guesswork.','real-entry-paver-edge.webp'),
    ]
    case_files = []
    for filename, city, service, title, problem, solution, outcome, image in case_studies:
        faqs = [(f'Does Terramorph handle {service.lower()} in {city}?', f'Yes. Terramorph serves {city} and surrounding Northwest Ohio communities with {service.lower()} and related outdoor property work.'), ('Can I send photos before an estimate?', 'Yes. Photos help Terramorph understand access, water movement, existing conditions, and project fit before follow-up.'), ('Is this an exact price example?', 'No. This is a planning example showing common local property problems and how Terramorph thinks through them. Final scope depends on the actual property.')]
        desc = f'{title}: local Terramorph project planning for {service.lower()} in {city}, Ohio.'
        body = f'''
<section class="page-hero premium-page-hero planning-example-hero"><div class="page-hero-image"><img src="assets/{image}" alt="{title}"></div><div class="hero-overlay"></div><div class="container page-hero-content"><p class="crumb"><a href="index.html">Home</a> / Project Planning Library / {city}</p><p class="eyebrow light">Hypothetical planning example</p><h1>{title}</h1><p>{desc} This is not presented as a completed customer project.</p><div class="cta-row"><a class="btn btn-gold" href="#quote">Request This Type of Work</a><a class="btn btn-outline-light" href="tel:{TEL}">Call {PHONE}</a></div></div></section>
{trust_band()}
<section class="section"><div class="container problem-grid"><div class="problem-card dark"><p class="eyebrow light">Problem</p><h2>{problem}</h2></div><div class="problem-card light-card"><p class="eyebrow">Terramorph approach</p><h2>{solution}</h2></div></div></section>
<section class="section clay-section"><div class="container local-grid"><div><p class="eyebrow">Expected outcome</p><h2>{outcome}</h2><p>This planning example shows the kind of details homeowners can have ready before a quote call: city, service need, photos, timeline, and the result they want.</p></div><div class="authority-list"><div><b>City</b><span>{city}, Ohio and nearby communities.</span></div><div><b>Service</b><span>{service}</span></div><div><b>Estimate path</b><span>Call {PHONE} with city, photos, timeline, and project notes.</span></div></div></div></section>
{faq_section(faqs)}
<section class="section quote-section"><div class="container quote-grid">{quote_form('Request Similar Terramorph Work')}<div class="cta-proof"><p class="eyebrow">Planning support</p><h2>Use this hypothetical scenario as a starting point for your own property.</h2>{review_stack(2, service)}</div></div></section>
'''
        (root / filename).write_text(page(title + ' | Terramorph', desc, body, schema_for(filename, title, desc, faqs, service)))
        case_files.append(filename)

    completed_projects = [
        (
            'completed-lawn-maintenance-project.html',
            'Completed Lawn Maintenance Work',
            'Lawn Maintenance',
            'real-lawn.webp',
            'A Terramorph field photo documenting a finished large-lot mowing visit with consistent striping and clean coverage.',
            [('Visible work', 'Uniform mowing pattern across a large residential lawn.'), ('Property context', 'Large open lawn with trees, fencing, and residential edges.'), ('Record source', 'Original Terramorph field photo preserved in the March 2026 project archive.')],
        ),
        (
            'completed-retaining-wall-project.html',
            'Completed Retaining Wall Work',
            'Retaining Walls',
            'real-retaining.webp?v=3.60',
            'A Terramorph field photo documenting a finished modular-block retaining wall beside an existing driveway and grade transition.',
            [('Visible work', 'Straight wall alignment, cap course, stepped end, and clean driveway transition.'), ('Property context', 'Residential grade change beside a garage and established landscape.'), ('Record source', 'Original Terramorph field photo preserved in the March 2026 project archive.')],
        ),
        (
            'completed-new-construction-landscape-project.html',
            'Completed New-Construction Landscape Work',
            'Landscape Design',
            'completed-new-construction-landscape.jpg',
            'A Terramorph field photo documenting finished foundation beds, dark mulch, and new plant installation around a Northwest Ohio home.',
            [('Visible work', 'Curved foundation beds, fresh mulch, and spaced new plantings.'), ('Property context', 'New-construction home with open lawn and a stone-and-siding exterior.'), ('Record source', 'Original Terramorph field photo preserved in the March 2026 project archive.')],
        ),
    ]
    completed_files = []
    for filename, title, service, image, summary, details in completed_projects:
        desc = f'{title} documented with an original Terramorph field photo from the Northwest Ohio service area.'
        detail_markup = ''.join(f'<div><b>{label}</b><span>{copy}</span></div>' for label, copy in details)
        body = f'''
<section class="page-hero premium-page-hero completed-work-hero"><div class="page-hero-image"><img src="assets/{image}" alt="{title} by Terramorph"></div><div class="hero-overlay"></div><div class="container page-hero-content"><p class="crumb"><a href="index.html">Home</a> / <a href="projects.html">Completed Work</a></p><p class="eyebrow light">Completed-work spotlight</p><h1>{title}</h1><p>{summary}</p><div class="cta-row"><a class="btn btn-gold" href="#quote">Request Similar Work</a><a class="btn btn-outline-light" href="tel:{TEL}">Call {PHONE}</a></div></div></section>
{trust_band()}
<section class="section"><div class="container local-grid"><div><p class="eyebrow">Documented field work</p><h2>What this Terramorph project photo shows.</h2><p>This record describes only details visible in the archived field photo. The exact customer address, price, schedule, and private project information are intentionally not published.</p></div><div class="authority-list">{detail_markup}</div></div></section>
<section class="section quote-section"><div class="container quote-grid">{quote_form('Request Similar ' + service + ' Work')}<div class="cta-proof"><p class="eyebrow">Project fit</p><h2>Send your city, property photos, service need, and timeline for a property-specific estimate.</h2>{review_stack(2, service)}</div></div></section>
'''
        (root / filename).write_text(page(title + ' | Terramorph', desc, body, schema_for(filename, title, desc, service=service)))
        completed_files.append(filename)

    review_desc = 'Leave a Google review for Terramorph LLC or request more landscape, patio, drainage, lighting, cleanup, or maintenance work in Northwest Ohio.'
    review_body = f'''
<section class="page-hero premium-page-hero compact-hero"><div class="hero-overlay"></div><div class="container page-hero-content"><p class="crumb"><a href="index.html">Home</a> / Reviews</p><p class="eyebrow light">Terramorph reviews</p><h1>Help more Northwest Ohio homeowners find Terramorph.</h1><p>If Terramorph did strong work for you, a Google review helps local homeowners choose a reliable landscaping, patio, drainage, lighting, cleanup, or maintenance crew.</p><div class="cta-row"><a class="btn btn-gold" href="https://www.google.com/search?q=Terramorph+LLC+Perrysburg+OH+reviews" rel="noopener">Leave a Google Review</a><a class="btn btn-outline-light" href="contact.html">Request More Work</a></div></div></section>
{trust_band()}
<section class="section"><div class="container local-grid"><div><p class="eyebrow">Share your experience</p><h2>Reviews help neighbors choose a crew they can trust.</h2><p>This page gives customers a simple place to leave feedback after completed work or request more help from Terramorph.</p></div><div class="authority-list"><div><b>What to mention</b><span>City, service, result, communication, cleanup, and whether you would recommend Terramorph.</span></div><div><b>Helpful examples</b><span>Paver patio in Perrysburg, drainage solution in Maumee, landscaping in Toledo, lawn maintenance in Sylvania.</span></div><div><b>Photos help</b><span>Before/after photos can make reviews more useful for future customers.</span></div></div></div></section>
<section class="section quote-section"><div class="container quote-grid">{quote_form('Request Terramorph Service')}<div class="cta-proof"><p class="eyebrow">Customer proof</p><h2>Real reviews support every service page.</h2>{review_stack(4)}</div></div></section>
'''
    (root / 'reviews.html').write_text(page('Terramorph Reviews | Leave a Google Review', review_desc, review_body, schema_for('reviews.html', 'Terramorph Reviews', review_desc, DEFAULT_FAQS)))

    meta_landing_page('lp-backyard-patio-estimate.html', 'Backyard Patio Estimate', 'Backyard patio estimate', 'real-patio.webp?v=3.14', 'Turn the backyard into a place people actually use.', 'Request a free backyard patio assessment for pavers, layout, seating, grill zones, walkways, drainage, and finished outdoor living.', ['The backyard has no useful gathering space or the existing patio/walkway feels disconnected from how you want to live outside.', 'Terramorph reviews layout, access, base conditions, drainage, materials, lighting, and the way the patio should connect to the home.', 'A patio should feel planned before it is priced.', 'The best backyard patio starts with layout, water movement, materials, budget, and how the space will actually be used.'], 'Paver Patios and Hardscapes', 'Request My Backyard Patio Estimate', 'Free Backyard Patio Layout + Cost Assessment', ['No clear grill or seating area', 'Backyard feels disconnected from the house', 'Old concrete or uneven walkway', 'Need patio drainage planned before installation'], [('Use', 'How people will grill, sit, host, walk, and move through the backyard.'), ('Site', 'Door transitions, grade, drainage, soil, access, and nearby beds.'), ('Scope', 'Pavers, walkways, steps, edge details, lighting, and realistic budget range.')])
    meta_landing_page('lp-standing-water-yard.html', 'Standing Water Drainage Estimate', 'Standing water drainage estimate', 'real-drainage.webp', 'Stop planning your yard around puddles.', 'Request a free drainage assessment for standing water, soggy grass, downspout runoff, grading issues, and low spots.', ['Rain leaves the yard soft, muddy, unusable, or pooling near the house, patio, driveway, beds, or garage.', 'Terramorph checks where water starts, how it moves, where it can safely discharge, and which practical drainage options fit the property.', 'Standing water needs diagnosis, not guessing.', 'Clay soil, flat lots, runoff, and freeze-thaw make Northwest Ohio drainage a local problem.'], 'Drainage Solutions', 'Request My Standing Water Assessment', 'Free Standing Water + Yard Drainage Assessment', ['Puddles after normal rain', 'Soggy low spots or mud', 'Water near foundation, garage, patio, or beds', 'Downspouts dumping into bad areas'], [('Source', 'Roof water, neighbor runoff, slope, soil, low spots, or hardscape runoff.'), ('Route', 'Safe paths for water that do not create a new problem.'), ('Fix', 'Grading, swales, drains, buried lines, dry creek details, or landscape-based solutions.')])
    meta_landing_page('lp-curb-appeal-upgrade.html', 'Front Yard Curb Appeal Estimate', 'Front yard curb appeal estimate', 'real-entry-columns-bed.webp', 'Make the front of the home look finished.', 'Request a free curb appeal assessment for landscape beds, plantings, mulch, rock, edging, lighting, and front-entry upgrades.', ['The front yard looks tired, builder-grade, overgrown, empty, or disconnected from the house.', 'Terramorph reviews bed shape, plant selection, soil, sun, mulch versus rock, edging, lighting, and maintenance expectations.', 'Curb appeal should be simple to understand.', 'A good front yard upgrade makes the home feel cleaner, more premium, and easier to maintain.'], 'Landscape Design', 'Request My Curb Appeal Estimate', 'Free Front Yard Curb Appeal Assessment', ['Front beds look empty or overgrown', 'Old shrubs or messy edges', 'Not sure what plants fit the house', 'Want a cleaner entry and better first impression'], [('Street view', 'What people notice from the road, driveway, sidewalk, and front door.'), ('Conditions', 'Sun, shade, soil, water, existing plants, and maintenance level.'), ('Plan', 'Bed shape, plant palette, mulch or rock, edging, lighting, and phased budget.')])
    meta_landing_page('lp-spring-cleanup.html', 'Spring Cleanup Estimate', 'Spring cleanup estimate', 'real-mature-front-bed.webp', 'Reset the property before the season gets away from you.', 'Request a free spring cleanup estimate for leaves, debris, pruning, bed reset, mulch, trimming, and property prep.', ['Winter left sticks, leaves, dead plant material, messy beds, weeds, and overgrown edges behind.', 'Terramorph reviews cleanup scope, bed condition, debris removal, pruning needs, mulch, and whether maintenance should continue after the reset.', 'A clean spring start makes the rest easier.', 'The right cleanup gets the property ready for mowing, mulch, planting, outdoor use, and better curb appeal.'], 'Seasonal Cleanups', 'Request My Spring Cleanup Estimate', 'Free Spring Cleanup + Bed Reset Estimate', ['Leaves and sticks everywhere', 'Messy beds or old mulch', 'Bushes and edges need trimming', 'Want mowing/maintenance set up after cleanup'], [('Cleanup', 'Leaves, sticks, debris, dead plant material, weeds, and edge reset.'), ('Refresh', 'Mulch, rock, pruning, trimming, plant replacement, and bed shaping.'), ('Maintain', 'Optional recurring lawn care and bed upkeep after the reset.')])

    faq_topics = [
        ('paver-patio-cost-toledo-ohio.html', 'How Much Does a Paver Patio Cost in Toledo, Ohio?', 'Paver patio cost depends on size, access, base prep, drainage, steps, patterns, borders, and whether the project includes seating, fire pits, lighting, or beds.', 'Paver Patios and Hardscapes', 'real-patio.webp?v=3.14', ['What affects patio pricing?', 'Size, excavation, base depth, drainage, paver style, edge restraint, steps, access, and finishing details all affect the final estimate.', 'Why is a site review important?', 'Northwest Ohio clay soil, grade, and water movement can change what base preparation and drainage planning are needed.', 'Can Terramorph give a free patio estimate?', 'Yes. Send city, approximate size, photos, and goals through the quote form for the best next step.']),
        ('yard-drainage-cost-northwest-ohio.html', 'How Much Does Yard Drainage Cost in Northwest Ohio?', 'Drainage cost depends on the water source, outlet route, grade, soil, distance, access, and whether the property needs drains, swales, grading, or downspout routing.', 'Drainage Solutions', 'real-shoreline-riprap.webp', ['Why is drainage pricing hard without seeing the yard?', 'A wet yard can come from roof water, neighbor runoff, low spots, clay soil, hardscape slope, or grade issues. The fix changes with the source.', 'Is every drainage fix a French drain?', 'No. Some properties need grading, swales, downspout extensions, catch basins, dry creek features, or a combination.', 'Can Terramorph inspect standing water?', 'Yes. Terramorph offers free drainage estimates for Wood and Lucas County properties.']),
        ('landscaping-cost-perrysburg-ohio.html', 'How Much Does Landscaping Cost in Perrysburg, Ohio?', 'Landscape pricing depends on bed size, plant selection, mulch or rock, edging, soil, existing removals, drainage, lighting, and whether the project is phased.', 'Landscape Design', 'real-mature-front-bed.webp', ['What changes a landscape estimate?', 'Plant count, plant size, bed depth, edging, removals, mulch or rock, drainage, soil, lighting, and access all affect scope.', 'Can landscaping be phased?', 'Yes. Many homeowners start with front curb appeal, then add patios, lighting, drainage, or backyard areas later.', 'Does Terramorph handle design and install?', 'Yes. Terramorph can plan and install beds, plants, mulch, rock, edging, sod, and related outdoor upgrades.']),
        ('best-plants-for-ohio-clay-soil.html', 'Best Landscape Plants for Ohio Clay Soil and Wet Yards', 'Ohio clay soil can hold water, compact easily, and stress the wrong plants. Better plant choices depend on sun, drainage, mature size, and maintenance expectations.', 'Landscape Design', 'real-planting.webp', ['Why does clay soil matter?', 'Clay can stay wet, compact, and drain slowly, so plant selection and bed preparation matter more than just picking what looks good.', 'Can wet-yard planting replace drainage?', 'Sometimes plants help, but persistent standing water usually needs grade, routing, or drainage review too.', 'Can Terramorph recommend plants?', 'Yes. Terramorph reviews sun, soil, water, house style, and maintenance goals before recommending plantings.']),
        ('spring-cleanup-cost-toledo-ohio.html', 'Spring Cleanup Cost in Toledo and Northwest Ohio', 'Spring cleanup pricing depends on debris volume, leaf removal, pruning, bed reset, mulch, edging, hauling, and whether maintenance continues after the cleanup.', 'Seasonal Cleanups', 'real-mulch.webp', ['What is included in spring cleanup?', 'Common cleanup work includes sticks, leaves, dead plant material, bed reset, trimming, edging, debris hauling, and optional mulch.', 'When should cleanup be scheduled?', 'Early spring is best once winter debris is visible and before weeds and growth get ahead of the property.', 'Can cleanup turn into ongoing maintenance?', 'Yes. Terramorph can pair cleanup with mowing, trimming, bed maintenance, and seasonal follow-up.']),
        ('lawn-maintenance-cost-northwest-ohio.html', 'Lawn Maintenance Cost in Northwest Ohio', 'Lawn maintenance cost depends on property size, mowing frequency, trimming, edging, obstacles, bed upkeep, commercial needs, and seasonal cleanup add-ons.', 'Lawn Maintenance', 'real-mowing-service.webp', ['What affects mowing price?', 'Lot size, route fit, mowing frequency, trimming, edging, slopes, gates, obstacles, and cleanup expectations affect pricing.', 'Do you maintain commercial properties?', 'Yes. Terramorph can help with residential, commercial, and property-owner maintenance needs.', 'Can lawn care include beds?', 'Yes. Bed maintenance, weeding, trimming, cleanup, mulch, and seasonal resets can be scoped with mowing.']),
        ('outdoor-lighting-cost-ohio.html', 'Outdoor Lighting Cost for Patios, Walkways, and Landscaping in Ohio', 'Outdoor lighting cost depends on fixture count, transformer size, wire runs, controls, path safety, accent areas, and whether lighting is added during a larger project.', 'Outdoor Lighting', 'real-lighting-night.webp', ['What affects outdoor lighting cost?', 'Fixture type, number of lights, wire runs, transformer placement, controls, trenching, and design complexity all matter.', 'Can lighting be added to patios or beds?', 'Yes. Lighting often works best when planned with patios, walkways, beds, retaining walls, or curb appeal upgrades.', 'Does Terramorph install landscape lighting?', 'Yes. Terramorph handles outdoor lighting for paths, patios, entries, beds, and nighttime curb appeal.']),
        ('how-to-choose-landscaper-toledo.html', 'How to Choose a Landscaper in Toledo, Perrysburg, Maumee, and Northwest Ohio', 'The best landscaper should understand local soil, drainage, maintenance, hardscapes, communication, cleanup, reviews, and how services connect across the whole property.', 'Landscape Design', 'real-estate-stone-wall.webp', ['What should homeowners look for?', 'Look for local proof, reviews, clear estimates, professional communication, drainage awareness, photos, and a team that thinks through the whole property.', 'Why does local experience matter?', 'Northwest Ohio clay soil, flat lots, freeze-thaw, rain, and seasonal maintenance needs affect outdoor work.', 'Can Terramorph handle multiple services?', 'Yes. Terramorph connects design, patios, drainage, lighting, cleanup, lawn maintenance, and other property services.']),
    ]
    faq_files = []
    for filename, title, intro, service, image, qa in faq_topics:
        q1, a1, q2, a2, q3, a3 = qa
        faqs = [(q1, a1), (q2, a2), (q3, a3)]
        desc = title + ' Terramorph explains local factors and offers free estimates in Northwest Ohio.'
        body = f'''
<section class="page-hero premium-page-hero faq-hero"><div class="page-hero-image"><img src="assets/{image}" alt="{title}"></div><div class="hero-overlay"></div><div class="container page-hero-content"><p class="crumb"><a href="index.html">Home</a> / <a href="guides.html">Guides</a></p><p class="eyebrow light">Local project guide</p><h1>{title}</h1><p>{intro}</p><div class="cta-row"><a class="btn btn-gold" href="#quote">Request a Free Estimate</a><a class="btn btn-outline-light" href="tel:{TEL}">Call {PHONE}</a></div></div></section>
{trust_band()}
<section class="section"><div class="container local-grid"><div><p class="eyebrow">Short answer</p><h2>{intro}</h2><p>Online ranges are usually too broad because local soil, access, grade, drainage, materials, and property condition matter. Terramorph uses a real property review to turn broad ranges into a practical next step.</p></div><div class="authority-list"><div><b>{q1}</b><span>{a1}</span></div><div><b>{q2}</b><span>{a2}</span></div><div><b>{q3}</b><span>{a3}</span></div></div></div></section>
{faq_section(faqs)}
<section class="section quote-section"><div class="container quote-grid">{quote_form('Request a Free Terramorph Estimate')}<div class="cta-proof"><p class="eyebrow">Why ask Terramorph</p><h2>Local estimates beat generic online ranges.</h2>{review_stack(2)}</div></div></section>
'''
        (root / filename).write_text(page(title + ' | Terramorph', desc, body, schema_for(filename, title, desc, faqs, service)))
        faq_files.append(filename)

    guide_links = ''.join(
        f'<a class="guide-card faq-expansion-card" href="{filename}"><span>Helpful local guide</span><h3>{title}</h3><p>{intro}</p><b>Read answer &rarr;</b></a>'
        for filename, title, intro, service, image, qa in faq_topics
    )
    guides_page = root / 'guides.html'
    guides_html = guides_page.read_text()
    if 'V3.45 FAQ expansion' not in guides_html:
        section = f'<section class="section guide-index-section v345-faq-expansion"><div class="container section-heading compact"><p class="eyebrow">Project planning answers</p><h2>Cost, comparison, and local property questions homeowners ask before they request a quote.</h2></div><div class="container guide-grid">{guide_links}</div></section>'
        guides_html = guides_html.replace('<section class="section quote-section">', section + '\n<section class="section quote-section">')
        guides_page.write_text(guides_html)

    city_cards = ''.join(
        f'<a class="guide-card city-service-card" href="{name}"><span>{city_page_meta[name][0]} &middot; {city_page_meta[name][1]}</span><h3>{city_page_meta[name][2]}</h3><p>{city_page_meta[name][3]}</p><b>Open local page &rarr;</b></a>'
        for name in extra_city_pages
    )
    # Leaf removal + snow removal by town, and the Toledo service pages that had no hub link (2026-11-04).
    TOLEDO_SERVICE_PAGES = [
        ('spring-fall-cleanups-toledo-ohio.html', 'Toledo &middot; Seasonal cleanups', 'Spring & Fall Cleanups in Toledo', 'Leaves, sticks, bed resets, pruning, debris removal, and mulch for Toledo properties.'),
        ('snow-removal-toledo-ohio.html', 'Toledo &middot; Snow removal', 'Snow Removal in Toledo', 'Winter plowing and access for Toledo homes, businesses, driveways, walkways, and commercial lots.'),
        ('tree-care-northwest-ohio.html', 'Northwest Ohio &middot; Tree and shrub care', 'Tree Trimming & Shrub Care', 'Tree and shrub trimming, pruning, overgrowth control, and bed cleanup across Northwest Ohio.'),
        ('mulch-installation-toledo-ohio.html', 'Toledo &middot; Mulch', 'Mulch Installation in Toledo', 'Mulch installation, bed edging, shrub trimming, cleanup, and rock conversion for Toledo beds.'),
        ('landscape-lighting-toledo-ohio.html', 'Toledo &middot; Lighting', 'Landscape Lighting in Toledo', 'Low-voltage lighting for Toledo patios, walkways, entries, beds, and nighttime curb appeal.'),
    ]
    seasonal_cards = ''.join(
        f'<a class="guide-card city-service-card" href="{name}"><span>{seasonal_city_meta[name][0]} &middot; {"Leaf removal" if seasonal_city_meta[name][1] == "leaf" else "Snow removal"}</span><h3>{seasonal_city_meta[name][2]}</h3><p>{seasonal_city_meta[name][3]}</p><b>Open local page &rarr;</b></a>'
        for name in leaf_files + snow_files
    )
    toledo_cards = ''.join(f'<a class="guide-card" href="{f}"><span>{cat}</span><h3>{t}</h3><p>{d}</p><b>Open page &rarr;</b></a>' for f, cat, t, d in TOLEDO_SERVICE_PAGES)
    seasonal_hub = (f'<section class="section guide-index-section v2026-seasonal-towns" id="seasonal-towns"><div class="container section-heading compact"><p class="eyebrow">Leaf removal and snow removal by town</p><h2>Fall cleanup and winter plowing pages for the towns we serve.</h2><p>Each page covers that town\'s leaf-pickup rules or winter conditions, what the visit includes, and how to book. Leaves are hauled away; snow service runs on one seasonal agreement.</p></div><div class="container guide-grid">{seasonal_cards}</div></section>'
                    f'<section class="section guide-index-section v2026-toledo-services"><div class="container section-heading compact"><p class="eyebrow">Toledo and Northwest Ohio service pages</p><h2>Cleanups, snow, tree care, mulch, and lighting.</h2></div><div class="container guide-grid">{toledo_cards}</div></section>')
    case_cards = ''.join(
        f'<a class="guide-card planning-example-card" href="{filename}"><span>Hypothetical &middot; {city} &middot; {service}</span><h3>{title}</h3><p>{problem}</p><b>View planning example &rarr;</b></a>'
        for filename, city, service, title, problem, solution, outcome, image in case_studies
    )
    completed_cards = ''.join(
        f'<a class="guide-card completed-project-card" href="{filename}"><span>Completed work &middot; {service}</span><h3>{title}</h3><p>{summary}</p><b>View documented work &rarr;</b></a>'
        for filename, title, service, image, summary, details in completed_projects
    )
    service_areas = root / 'service-areas.html'
    service_html = service_areas.read_text()
    if 'V3.45 expanded service area pages' not in service_html:
        section = f'<section class="section guide-index-section v345-expanded-service-pages"><div class="container section-heading compact"><p class="eyebrow">More service areas</p><h2>Local service information by city and project type.</h2><p>Homeowners in Sylvania, Bowling Green, Holland, Waterville, Whitehouse, Oregon, and Rossford can review the most relevant Terramorph services before requesting an estimate.</p></div><div class="container guide-grid">{city_cards}</div></section>'
        service_html = service_html.replace('<section class="section quote-section">', section + '\n' + seasonal_hub + '\n<section class="section quote-section">')
        service_areas.write_text(service_html)
    projects_page = root / 'projects.html'
    projects_html = projects_page.read_text()
    if 'V3.45 local case studies' not in projects_html:
        section = f'<section class="section guide-index-section completed-projects"><div class="container section-heading compact"><p class="eyebrow">Documented completed work</p><h2>Terramorph field-photo spotlights from the Northwest Ohio service area.</h2><p>These pages use original archived field photos and describe only visible, verifiable details. Private customer addresses and unsupported project claims are not published.</p></div><div class="container guide-grid">{completed_cards}</div></section><section class="section guide-index-section v345-case-studies"><div class="container section-heading compact"><p class="eyebrow">Separate project planning library</p><h2>Hypothetical outdoor project scenarios around Northwest Ohio.</h2><p>These are clearly labeled planning examples, not completed customer projects. Each one shows how Terramorph would think through a common scope before estimating the actual property.</p></div><div class="container guide-grid">{case_cards}</div></section>'
        projects_html = projects_html.replace('<section class="section transformation-section proof-gallery-section">', section + '\n<section class="section transformation-section proof-gallery-section">')
        projects_page.write_text(projects_html)

    support_pages = [
        ('faq.html', 'Terramorph FAQ Hub', 'Answers about landscaping, patios, drainage, lighting, cleanups, maintenance, estimates, service areas, and project planning in Northwest Ohio.', 'FAQ hub', 'The questions homeowners ask before hiring Terramorph.', 'Use this hub to compare services, understand the estimate process, and decide what details to send before requesting a free quote.', 'real-hero.webp', DEFAULT_FAQS + [
            ('What makes Terramorph different from a typical landscaper?', 'Terramorph connects design, drainage, hardscapes, lighting, maintenance, and cleanup so outdoor projects are planned around the whole property instead of one isolated task.'),
            ('Why does Northwest Ohio experience matter?', 'Clay soil, flat grading, freeze-thaw cycles, heavy rain, mature neighborhoods, and new-construction lots all change how landscapes, patios, and drainage should be planned.'),
            ('What should I include in a quote request?', 'Include city, address, service type, timeline, photos, budget range if known, and what outcome you want from the project.'),
            ('Does Terramorph serve Perrysburg?', 'Yes. Perrysburg is a core Terramorph service area along with Toledo, Maumee, Sylvania, Rossford, Oregon, Waterville, Whitehouse, Bowling Green, Wood County, and Lucas County.')
        ]),
        ('process.html', 'Terramorph Process', 'How Terramorph estimates, plans, schedules, builds, cleans up, and follows through on landscape, patio, drainage, lighting, and maintenance projects.', 'Process', 'A clear process removes the contractor guesswork.', 'Terramorph’s best projects start with visible site conditions, a clear outcome, smart sequencing, and honest communication before work begins.', 'real-entry.webp?v=3.14', [('How does the estimate process work?', 'Send the property details and photos, then Terramorph reviews fit, site conditions, schedule, and the best next step for a quote or walkthrough.'), ('Do you inspect drainage before installing patios or beds?', 'Yes. Water movement, grade, soil, and runoff are reviewed when they affect the long-term result.'), ('What happens after approval?', 'The team confirms scope, schedule, materials, access, and cleanup expectations before production.'), ('Do you clean up after the job?', 'Yes. Professional cleanup and a final walkthrough are part of the expected project experience.')]),
        ('warranty.html', 'Terramorph Warranty & Workmanship', 'Terramorph workmanship expectations, material considerations, maintenance responsibilities, and what homeowners should understand before outdoor work begins.', 'Warranty and workmanship', 'Premium work should come with clear expectations.', 'This page explains what Terramorph controls, what materials and weather can affect, and how homeowners can protect the finished result.', 'real-hardscape.webp?v=3.14', [('Does outdoor work require maintenance?', 'Yes. Plants, beds, lighting, patios, drainage features, and lawns all perform best when maintained correctly after installation.'), ('Are materials covered by manufacturer terms?', 'Some pavers, lighting fixtures, plants, and materials may carry manufacturer or supplier terms. Terramorph can explain what applies to the selected scope.'), ('Why are drainage outcomes property-specific?', 'Drainage depends on grade, soil, outlet options, rainfall, neighboring runoff, and future property changes. A site-specific plan is important.'), ('What should I do if I have a concern after work?', 'Contact Terramorph quickly with photos and a clear description so the team can review the issue and recommend the right next step.')]),
        ('materials.html', 'Landscape Materials Guide', 'Guide to mulch, rock, pavers, edging, plants, lighting fixtures, base prep, drainage materials, and Northwest Ohio outdoor material decisions.', 'Materials guide', 'The right material choice depends on the property, not a trend.', 'Compare common landscape and hardscape materials through the lens of durability, maintenance, drainage, curb appeal, and Northwest Ohio weather.', 'real-patio.webp?v=3.14', [('Is mulch or rock better?', 'Mulch often supports plant health and lower upfront cost; rock can reduce refresh frequency but needs fabric, edging, and plant/heat planning.'), ('What matters most for paver patios?', 'Base prep, compaction, drainage, edge restraint, paver selection, and freeze-thaw planning matter more than choosing by color alone.'), ('What plants work best in clay soil?', 'Plant choice depends on sun, drainage, mature size, maintenance level, and whether the bed needs soil improvement or drainage correction.'), ('Can outdoor lighting be added later?', 'Yes, but lighting is often cleaner and more efficient when planned with patios, walkways, retaining details, and landscape beds.')]),
        ('financing.html', 'Landscape Project Budgeting', 'How to budget and phase landscaping, patio, drainage, lighting, cleanup, and maintenance work with Terramorph in Northwest Ohio.', 'Budgeting and phasing', 'A premium outdoor plan can be built in smart phases.', 'This page helps homeowners think through must-fix issues, curb appeal wins, outdoor living upgrades, and maintenance before requesting an estimate.', 'real-lighting.webp?v=3.14', [('Can landscaping be phased?', 'Yes. Many homeowners start with drainage or front curb appeal, then phase patios, lighting, backyard work, and maintenance.'), ('What should be prioritized first?', 'Problems that can damage or limit use, such as drainage and grading, should usually be addressed before purely cosmetic upgrades.'), ('Does Terramorph publish fixed prices?', 'No. Site conditions change scope significantly, so Terramorph uses property-specific estimates instead of generic price menus.'), ('Can I share a target budget?', 'Yes. A target range helps Terramorph recommend the smartest scope, phasing, and materials for the property.')]),
        ('team.html', 'Terramorph Team & Standards', 'Meet the Terramorph standard for communication, jobsite care, reviews, local knowledge, and premium outdoor work in Northwest Ohio.', 'Team standards', 'Trust starts with who shows up and how the work is handled.', 'Terramorph’s service standard centers on communication, property respect, clean work, and practical local judgment.', 'real-lawn.webp', [('Who leads Terramorph projects?', 'Terramorph is a local Northwest Ohio outdoor services company led by Ty and the Terramorph crew.'), ('What standards matter on the job?', 'Communication, punctuality, property care, clean edges, correct materials, cleanup, and follow-through all matter.'), ('Why do team standards matter?', 'Homeowners need clear evidence of trust, process, service fit, and local reputation before choosing a contractor.'), ('How can customers help the team quote faster?', 'Send photos, city, access notes, desired outcome, and timeline in the request form.')]),
        ('community.html', 'Terramorph in Northwest Ohio', 'Terramorph service-area commitment, local property knowledge, neighborhoods served, and outdoor project priorities across Wood and Lucas County.', 'Community and service area', 'Built for Perrysburg, Toledo, Wood County, and Lucas County properties.', 'This page reinforces where Terramorph works, what local conditions matter, and why neighborhood-specific judgment improves outdoor results.', 'real-hero.webp', [('What communities does Terramorph serve?', 'Terramorph serves Perrysburg, Toledo, Maumee, Sylvania, Rossford, Oregon, Waterville, Whitehouse, Bowling Green, Wood County, Lucas County, and nearby Northwest Ohio areas.'), ('Why does local geography matter?', 'Flat lots, clay soil, mature trees, new construction grading, river-area moisture, and lake-effect weather can all affect outdoor work.'), ('Does Terramorph work on both homes and businesses?', 'Yes. Terramorph can review residential, commercial, and property-owner outdoor service needs.'), ('How should I choose a local landscaper?', 'Look for real reviews, project photos, clear services, local explanations, direct estimate paths, and evidence they understand the property conditions.')]),
        ('before-after-gallery.html', 'Terramorph Project Photo Gallery', 'Terramorph field-photo gallery for lawn maintenance, retaining walls, drainage, landscape installation, lighting, and outdoor property work in Northwest Ohio.', 'Project photo gallery', 'Field photos make completed work easier to evaluate.', 'Use this gallery as a visual proof hub for documented Terramorph field work, clearly separated from hypothetical project-planning examples.', 'real-hero.webp', [('Why does project proof matter?', 'Field photos show visible service fit, property context, and the type of outdoor work Terramorph handles.'), ('Can I request similar work?', 'Yes. Use the quote form and mention the photo or project type that matches your property goal.'), ('Should I send photos of my property?', 'Yes. Current property photos help Terramorph understand existing conditions and recommend a better next step.'), ('Are these before-and-after pairs?', 'No. This page is a field-photo gallery. Terramorph does not label photos as before-and-after pairs unless both stages are documented.')]),
        ('tree-care-northwest-ohio.html', 'Tree Trimming & Shrub Care in Northwest Ohio', 'Tree and shrub trimming, pruning, bed cleanup, overgrowth control, plant health observations, and seasonal landscape care considerations in Northwest Ohio.', 'Tree and shrub care', 'Clean pruning and trimming can change the whole property.', 'Terramorph can review trimming, pruning, overgrowth, bed resets, cleanup, and related landscape maintenance needs as part of a broader property plan.', 'real-mulch.webp', [('Does Terramorph trim shrubs and bushes?', 'Yes. Shrub trimming, spring pruning, overgrowth cleanup, and bed reset work can be scoped with seasonal cleanup or maintenance.'), ('Do you diagnose tree diseases?', 'Terramorph can observe visible issues and recommend next steps, but specialized arborist diagnosis may be needed for complex tree health problems.'), ('When should shrubs be trimmed?', 'Timing depends on plant type, bloom cycle, property goals, and whether the work is part of spring or fall cleanup.'), ('Can trimming be combined with mulch?', 'Yes. Trimming, bed edging, debris removal, and mulch often make sense together.')]),
        ('holiday-lighting.html', 'Holiday Lighting in Northwest Ohio', 'Holiday lighting planning, installation considerations, safety, property access, and seasonal outdoor service requests from Terramorph in Northwest Ohio.', 'Holiday lighting', 'Seasonal lighting should look clean and be handled safely.', 'Terramorph can review holiday lighting requests alongside outdoor lighting, cleanup, maintenance, and seasonal property needs.', 'real-lighting.webp?v=3.14', [('Does Terramorph offer holiday lighting?', 'Holiday lighting can be requested through Terramorph for review based on schedule, property fit, access, and service availability.'), ('What details should I send?', 'Send property photos, roofline or landscape areas, timeline, address, and whether removal/storage support is needed.'), ('Can holiday lighting pair with outdoor lighting?', 'Yes. Permanent outdoor lighting and seasonal holiday lighting can be discussed together when planning nighttime curb appeal.'), ('When should I request holiday lighting?', 'Request early before seasonal schedules fill, especially for larger homes or commercial properties.')]),
    ]
    support_files = []
    # Support pages that are really a service get a Service schema node (2026-11-04).
    support_service = {'tree-care-northwest-ohio.html': 'Tree and Shrub Trimming', 'holiday-lighting.html': 'Holiday Lighting'}
    for filename, title, desc, eyebrow, headline, intro, image, faqs in support_pages:
        detail_cards = ''.join(f'<div><b>{q}</b><span>{a}</span></div>' for q, a in faqs[:4])
        body = f'''\n<section class="page-hero premium-page-hero support-page-hero"><div class="page-hero-image"><img src="assets/{image}" alt="{title} by Terramorph"></div><div class="hero-overlay"></div><div class="container page-hero-content"><p class="crumb"><a href="index.html">Home</a> / {eyebrow}</p><p class="eyebrow light">{eyebrow}</p><h1>{headline}</h1><p>{intro}</p><div class="cta-row"><a class="btn btn-gold" href="#quote">Request a Free Estimate</a><a class="btn btn-outline-light" href="tel:{TEL}">Call {PHONE}</a></div></div></section>\n{trust_band()}\n<section class="section"><div class="container local-grid"><div><p class="eyebrow">Why this matters</p><h2>{desc}</h2><p>These details help homeowners compare outdoor service options and choose a clear next step near Perrysburg, Toledo, and Northwest Ohio.</p></div><div class="authority-list">{detail_cards}</div></div></section>\n{faq_section(faqs)}\n<section class="section quote-section"><div class="container quote-grid">{quote_form('Request a Free Terramorph Estimate')}<div class="cta-proof"><p class="eyebrow">Trust signal</p><h2>Clear information before the call helps homeowners choose with confidence.</h2>{review_stack(3)}</div></div></section>\n'''
        (root / filename).write_text(page(title + ' | Terramorph', desc, body, schema_for(filename, title, desc, faqs, service=support_service.get(filename))))
        support_files.append(filename)

    support_cards = ''.join(f'<a class="guide-card support-card" href="{filename}"><span>Trust resource</span><h3>{title}</h3><p>{desc}</p><b>Open resource &rarr;</b></a>' for filename, title, desc, eyebrow, headline, intro, image, faqs in support_pages)
    guides_page = root / 'guides.html'
    guides_html = guides_page.read_text()
    if 'v346-trust-resource-hub' not in guides_html:
        section = f'<section class="section guide-index-section v346-trust-resource-hub"><div class="container section-heading compact"><p class="eyebrow">Trust resources</p><h2>Process, warranty, materials, budgeting, FAQ, team standards, and local proof.</h2><p>These pages answer the questions homeowners ask before choosing Terramorph for outdoor work.</p></div><div class="container guide-grid">{support_cards}</div></section>'
        guides_html = guides_html.replace('<section class="section quote-section">', section + '\n<section class="section quote-section">')
        guides_page.write_text(guides_html)

    authority_pages = [
        ('services.html','Terramorph Services','Complete Terramorph service hub for landscape design, paver patios, drainage, lighting, lawn maintenance, cleanups, retaining walls, snow removal, sod, mulch, and commercial outdoor work.','Services hub','Outdoor services for Northwest Ohio properties.','Terramorph plans and installs outdoor upgrades around the whole property: curb appeal, water movement, hardscapes, maintenance, lighting, and seasonal needs.','real-hero.webp','Outdoor Services'),
        ('case-studies.html','Terramorph Project Planning Library','Hypothetical planning examples for Terramorph landscaping, patios, drainage, lawn maintenance, cleanups, and outdoor living projects in Northwest Ohio.','Planning library','Hypothetical project planning by city and service.','These examples explain how Terramorph would diagnose common property problems and scope possible work. They are not presented as completed customer projects.','real-patio.webp?v=3.14','Project Planning'),
        ('retaining-walls.html','Retaining Walls Northwest Ohio','Retaining wall planning, drainage, grading, steps, soil pressure, patio transitions, and landscape structure for Northwest Ohio homes.','Retaining walls','Retaining walls should solve grade problems, not create drainage problems.','Terramorph reviews slope, water, soil, wall purpose, access, and surrounding hardscape or landscape work before scoping retaining wall projects.','real-retaining.webp?v=3.60','Retaining Walls'),
        ('retaining-walls-toledo-ohio.html','Retaining Walls in Toledo, OH','Retaining wall planning and estimates for Toledo yards with slopes, grade changes, patios, beds, steps, drainage, and outdoor living transitions.','Toledo retaining walls','Retaining walls in Toledo need drainage and freeze-thaw planning.','Terramorph reviews grade, soil, runoff, access, wall height, nearby patios, and bed transitions before recommending a retaining wall scope.','real-retaining.webp?v=3.60','Retaining Walls'),
        ('retaining-walls-perrysburg-ohio.html','Retaining Walls in Perrysburg, OH','Retaining wall planning and estimates for Perrysburg properties needing grade control, outdoor living support, bed structure, steps, and drainage awareness.','Perrysburg retaining walls','A Perrysburg retaining wall should fit the property plan.','Terramorph scopes retaining walls around grade, drainage, soil, patio connections, lawn transitions, and long-term maintenance expectations.','real-retaining.webp?v=3.60','Retaining Walls'),
        ('outdoor-living.html','Outdoor Living Spaces Northwest Ohio','Outdoor living design for patios, fire pits, seating areas, outdoor kitchens, lighting, walkways, and landscape integration in Northwest Ohio.','Outdoor living','Outdoor living works best when layout, drainage, lighting, and materials are planned together.','Terramorph helps homeowners turn backyards into usable spaces with patio planning, hardscape details, lighting, beds, and water movement considered upfront.','real-hardscape.webp?v=3.14','Outdoor Living'),
        ('outdoor-kitchens-toledo-ohio.html','Outdoor Kitchens in Toledo, OH','Outdoor kitchen planning for Toledo patios, grill zones, seating, lighting, hardscape transitions, drainage, and backyard entertainment spaces.','Outdoor kitchens','An outdoor kitchen needs more than a grill location.','Terramorph reviews patio layout, access, utilities coordination, drainage, seating, lighting, and how the kitchen fits the full backyard plan.','real-hardscape.webp?v=3.14','Outdoor Kitchens'),
        ('fire-pit-installation-toledo-ohio.html','Fire Pit Installation in Toledo, OH','Fire pit area planning for Toledo backyards including paver patios, seating zones, walkways, drainage, lighting, and outdoor living flow.','Fire pits','A fire pit should feel built into the backyard, not dropped into it.','Terramorph scopes fire pit areas around seating, wind, safety clearances, patio layout, drainage, walkways, and lighting.','real-patio.webp?v=3.14','Fire Pits'),
        ('landscape-lighting-toledo-ohio.html','Landscape Lighting in Toledo, OH','Landscape lighting for Toledo homes, patios, walkways, entries, beds, security visibility, nighttime curb appeal, and outdoor living spaces.','Toledo landscape lighting','Lighting changes how the property feels after dark.','Terramorph plans low-voltage lighting around safety, curb appeal, patio use, path visibility, accent features, and future maintenance.','real-lighting.webp?v=3.14','Outdoor Lighting'),
        ('commercial-landscaping-toledo-ohio.html','Commercial Landscaping in Toledo, OH','Commercial landscaping, lawn maintenance, cleanups, bed upkeep, snow response, curb appeal, and exterior property care for Toledo businesses and property owners.','Commercial landscaping','Commercial properties need predictable exterior presentation.','Terramorph can review mowing, trimming, bed maintenance, seasonal cleanup, snow needs, access, route fit, and curb appeal priorities for Toledo properties.','real-maintenance.webp','Commercial Landscaping'),
        ('snow-removal-toledo-ohio.html','Snow Removal in Toledo, OH','Snow removal for Toledo homes and businesses: plowing, sidewalk and walkway shoveling, snow blowing, salting, and de-icing for driveways, walkways, and commercial lots.','Snow removal','Winter service is about safe access when weather hits.','Terramorph reviews driveway, walkway, parking, access, salting and de-icing needs, and winter risk areas before confirming snow service fit.','snow-removal-truck.webp?v=3.17','Snow Removal'),
        ('sod-installation-toledo-ohio.html','Sod Installation in Toledo, OH','Sod installation planning for Toledo yards including grading, soil prep, watering expectations, drainage, lawn edges, and landscape transitions.','Sod installation','Sod only works when soil prep and water are handled correctly.','Terramorph reviews grade, soil, access, drainage, sunlight, watering expectations, and lawn edges before sod installation.','real-lawn.webp','Sod Installation'),
        ('mulch-installation-toledo-ohio.html','Mulch Installation in Toledo, OH','Mulch installation, bed edging, shrub trimming, cleanup, rock conversion, plant refresh, and curb appeal upgrades for Toledo properties.','Mulch installation','Fresh mulch works best after beds are cleaned and shaped.','Terramorph scopes mulch around bed depth, edging, weeds, plant health, drainage, cleanup, and the look homeowners want from the street.','real-mulch.webp','Mulch Installation'),
        ('spring-fall-cleanups-toledo-ohio.html','Spring & Fall Cleanups Toledo, OH','Spring and fall cleanup estimates for Toledo properties including leaves, sticks, bed reset, pruning, trimming, debris removal, mulch, and maintenance setup.','Seasonal cleanups','Cleanups reset the property before the season gets away.','Terramorph reviews debris, leaf load, bed condition, trimming, hauling, mulch, and whether recurring maintenance should follow the cleanup.','real-mulch.webp','Seasonal Cleanups'),
        ('paver-patio-cost-northwest-ohio.html','Paver Patio Cost Northwest Ohio','Paver patio cost factors in Northwest Ohio including size, base prep, drainage, access, paver style, steps, fire pits, lighting, and outdoor living details.','Patio cost guide','Patio prices change when base prep and drainage change.','This guide explains why Northwest Ohio patio estimates depend on clay soil, freeze-thaw, excavation, water movement, access, layout, and finish details.','real-patio.webp?v=3.14','Paver Patios and Hardscapes'),
        ('retaining-wall-cost-toledo-ohio.html','Retaining Wall Cost Toledo, OH','Retaining wall cost factors for Toledo properties including wall height, access, drainage, soil, materials, steps, grading, and landscape transitions.','Retaining wall cost','Retaining wall pricing depends on what the wall is holding back.','This guide explains the cost drivers homeowners should understand before requesting a retaining wall estimate in Toledo or Northwest Ohio.','real-retaining.webp?v=3.60','Retaining Walls'),
        ('landscape-design-cost-northwest-ohio.html','Landscape Design Cost Northwest Ohio','Landscape design and installation cost factors in Northwest Ohio including beds, plants, mulch, rock, edging, drainage, lighting, removals, and phasing.','Landscape cost guide','Landscape pricing depends on scope, materials, site conditions, and phasing.','Terramorph explains how to think through budget, curb appeal, plant choices, maintenance expectations, and connected services before requesting a quote.','real-entry.webp?v=3.14','Landscape Design'),
        ('french-drain-cost-toledo-ohio.html','French Drain Cost Toledo, OH','French drain and yard drainage cost factors for Toledo properties including water source, outlet, trench distance, soil, grading, access, and alternatives.','French drain cost','A French drain is not always the right drainage fix.','This guide helps homeowners understand when a French drain makes sense, what affects cost, and why diagnosis comes before installation.','real-drainage.webp','Drainage Solutions'),
        ('best-drainage-solutions-for-clay-soil-ohio.html','Best Drainage for Ohio Clay Soil','Best drainage options for Ohio clay soil, flat yards, soggy grass, downspout runoff, low spots, grading problems, and Northwest Ohio storm patterns.','Clay soil drainage','Clay soil drainage needs water routing, not guesswork.','Terramorph explains practical options for Northwest Ohio yards: grading, swales, buried lines, drains, catch basins, dry creek features, and landscape-based solutions.','real-drainage.webp','Drainage Solutions'),
        ('new-construction-landscaping-northwest-ohio.html','New Construction Landscaping Northwest Ohio','New construction landscaping for Northwest Ohio homes including grading review, drainage, front beds, sod, plantings, mulch, rock, patios, and phased curb appeal.','New construction landscaping','Builder-grade yards often need a real outdoor plan.','Terramorph reviews grade, drainage, soil, bed layout, plant selection, sod edges, and future patio or lighting phases for new homes.','real-entry.webp?v=3.14','Landscape Design'),
        ('low-maintenance-landscaping-northwest-ohio.html','Low-Maintenance Landscaping Northwest Ohio','Low-maintenance landscaping ideas for Northwest Ohio including plant selection, mulch vs rock, bed edging, native plants, drainage-aware design, and maintenance planning.','Low-maintenance landscaping','Low-maintenance does not mean no planning.','Terramorph designs around mature plant size, soil, water, sun, edging, mulch or rock, and realistic upkeep for Northwest Ohio properties.','real-planting.webp','Landscape Design'),
        ('landscape-maintenance-packages-northwest-ohio.html','Landscape Maintenance Packages Northwest Ohio','Landscape maintenance package planning for Northwest Ohio properties including mowing, trimming, edging, bed upkeep, seasonal cleanups, mulch, and commercial maintenance.','Maintenance packages','Reliable maintenance keeps the property looking finished.','Terramorph can review route fit, service frequency, trimming, bed care, seasonal cleanup, mulch refresh, and commercial property presentation needs.','real-maintenance.webp','Lawn Maintenance'),
    ]
    authority_files = []
    for filename, title, desc, eyebrow, headline, intro, image, service in authority_pages:
        faqs = [('Does Terramorph offer this service in Northwest Ohio?', f'Yes. Terramorph can review {service.lower()} requests in Perrysburg, Toledo, Wood County, Lucas County, and nearby Northwest Ohio communities.'),('What details should I send for an estimate?', 'Send city, address, photos, timeline, access notes, the problem you want solved, and any budget or phasing preference.'),('Why does a site review matter?', 'Outdoor work depends on grade, water movement, soil, access, materials, existing conditions, and how the property should function long term.'),('Can this be combined with other services?', 'Yes. Terramorph can scope related needs such as drainage, patios, beds, lighting, cleanups, maintenance, mulch, rock, sod, and seasonal work together when it makes sense.')]
        cards = ''.join(f'<div><b>{q}</b><span>{a}</span></div>' for q,a in faqs)
        related = ''.join(f'<a class="guide-card" href="{f}"><span>Related</span><h3>{t}</h3><p>{d}</p><b>Open page &rarr;</b></a>' for f,t,d,ey,h,i,img,svc in authority_pages if f != filename and (svc == service or ey in ['Services hub','Case-study hub']))[:2500]
        body = f'''\n<section class="page-hero premium-page-hero authority-page-hero"><div class="page-hero-image"><img src="assets/{image}" alt="{title} by Terramorph"></div><div class="hero-overlay"></div><div class="container page-hero-content"><p class="crumb"><a href="index.html">Home</a> / {eyebrow}</p><p class="eyebrow light">{eyebrow}</p><h1>{headline}</h1><p>{intro}</p><div class="cta-row"><a class="btn btn-gold" href="#quote">Request a Free Estimate</a><a class="btn btn-outline-light" href="tel:{TEL}">Call {PHONE}</a></div></div></section>\n{trust_band()}\n<section class="section"><div class="container local-grid"><div><p class="eyebrow">Answer first</p><h2>{desc}</h2><p>Terramorph uses real property conditions, local Northwest Ohio experience, project photos, named customer reviews, and a clear quote path to help homeowners make a confident decision before work begins.</p></div><div class="authority-list">{cards}</div></div></section>\n{faq_section(faqs)}\n<section class="section guide-index-section"><div class="container section-heading compact"><p class="eyebrow">Related resources</p><h2>Keep planning the right scope.</h2></div><div class="container guide-grid">{related}</div></section>\n<section class="section quote-section"><div class="container quote-grid">{quote_form('Request a ' + service + ' Estimate')}<div class="cta-proof"><p class="eyebrow">Why Terramorph</p><h2>Local proof, clean process, and practical recommendations before the work starts.</h2>{review_stack(3)}</div></div></section>\n'''
        (root / filename).write_text(page(title + ' | Terramorph', desc, body, schema_for(filename, title, desc, faqs, service, service_desc=ctx['SNOW_SERVICE_DESC'] if filename == 'snow-removal-toledo-ohio.html' else None)))
        authority_files.append(filename)

    # services.html: the hub was generated with an empty "Related resources" grid.
    # Fill it with the seasonal pages, the Toledo service pages, and the snow/leaf town pages (2026-11-04).
    services_path = root / 'services.html'
    services_html = services_path.read_text()
    if 'v2026-seasonal-towns' not in services_html:
        core_cards = ''.join(f'<a class="guide-card" href="{f}"><span>{cat}</span><h3>{t}</h3><p>{d}</p><b>Open page &rarr;</b></a>' for f, cat, t, d in [
            ('seasonal-cleanups.html', 'Seasonal', 'Leaf Removal & Fall Cleanup', 'Leaves hauled away, beds cut back the right way, debris gone, and spring cleanups when the snow melts.'),
            ('snow-removal.html', 'Winter', 'Snow Removal & Plowing', 'Seasonal plowing and salting for driveways, walks, and commercial lots. Reserve before the first storm.'),
            ('snow-removal-signup.html', 'Winter', 'Snow Removal Sign-Up', 'Residential and commercial seasonal snow service, one winter agreement.'),
        ])
        services_html = services_html.replace('<section class="section guide-index-section"><div class="container section-heading compact"><p class="eyebrow">Related resources</p><h2>Keep planning the right scope.</h2></div><div class="container guide-grid"></div></section>',
                                              f'<section class="section guide-index-section"><div class="container section-heading compact"><p class="eyebrow">Seasonal and winter service</p><h2>Cleanups and snow, plus the Toledo service pages.</h2></div><div class="container guide-grid">{core_cards}{toledo_cards}</div></section>\n{seasonal_hub}', 1)
        services_path.write_text(services_html)

    # Link service and proof hubs into key discovery pages.
    for target, label in [('service-areas.html','v347-services-proof-links'),('projects.html','v347-services-proof-links'),('guides.html','v347-services-proof-links')]:
        path = root / target
        html = path.read_text()
        if label not in html:
            section = f'<section class="section guide-index-section {label}"><div class="container section-heading compact"><p class="eyebrow">Deeper planning</p><h2>Services, completed work, and project planning resources.</h2></div><div class="container guide-grid"><a class="guide-card" href="services.html"><span>Services</span><h3>All Terramorph Services</h3><p>Full service hub for landscaping, patios, drainage, lighting, walls, cleanups, sod, mulch, snow, and commercial work.</p><b>Open services &rarr;</b></a><a class="guide-card" href="projects.html"><span>Completed work</span><h3>Documented Project Photos</h3><p>Original Terramorph field photos and completed-work spotlights.</p><b>View completed work &rarr;</b></a><a class="guide-card" href="case-studies.html"><span>Planning</span><h3>Project Planning Library</h3><p>Clearly labeled hypothetical scenarios by city and service.</p><b>Open planning library &rarr;</b></a></div></section>'
            html = html.replace('<section class="section quote-section">', section + '\n<section class="section quote-section">')
            path.write_text(html)

    # Paid landing pages and hypothetical planning examples stay available to
    # direct visitors but out of organic search until they have unique campaign
    # or completed-project evidence.
    sitemap_path = root / 'sitemap.xml'
    sitemap = sitemap_path.read_text()
    organic_authority_files = [name for name in authority_files if name != 'case-studies.html']
    extra_pages = extra_city_pages + leaf_files + snow_files + faq_files + support_files + completed_files + organic_authority_files + ['reviews.html']
    additions = ''
    for name in extra_pages:
        loc = BASE_URL + '/' + name
        if loc not in sitemap:
            additions += f'  <url><loc>{loc}</loc><changefreq>monthly</changefreq><priority>0.7</priority></url>\n'
    sitemap = sitemap.replace('</urlset>\n', additions + '</urlset>\n')
    sitemap_path.write_text(sitemap)

    image_entries = [
        ('assets/real-hero.webp', 'Terramorph landscaping project in Northwest Ohio'),
        ('assets/real-patio.webp', 'Paver patio and outdoor living project by Terramorph'),
        ('assets/real-drainage.webp', 'Drainage solution and grading work by Terramorph'),
        ('assets/real-entry.webp', 'Front entry landscaping and curb appeal by Terramorph'),
        ('assets/real-hardscape.webp', 'Hardscape and outdoor living installation by Terramorph'),
        ('assets/real-lawn.webp', 'Lawn maintenance and property care by Terramorph'),
        ('assets/real-mulch.webp', 'Mulch and bed refresh project by Terramorph'),
        ('assets/real-lighting.webp', 'Outdoor landscape lighting by Terramorph'),
        ('assets/real-walkway.webp', 'Walkway and patio transition by Terramorph'),
        ('assets/real-planting.webp', 'Landscape planting and bed installation by Terramorph'),
        ('assets/completed-new-construction-landscape.jpg', 'Completed new-construction landscape installation by Terramorph'),
        ('assets/project-house.webp', 'Terramorph residential landscape project'),
        ('assets/project-lawn.webp', 'Terramorph lawn and landscape maintenance project'),
        ('assets/hero-landscape.webp', 'Terramorph landscape design hero image'),
        ('assets/patio.webp', 'Terramorph patio and hardscape service image'),
        ('assets/drainage.webp', 'Terramorph drainage solutions service image'),
        ('assets/lighting.webp', 'Terramorph outdoor lighting service image'),
        ('assets/outdoor-living.webp', 'Terramorph outdoor living service image'),
        ('assets/retaining.webp', 'Terramorph retaining wall service image'),
        ('assets/pond.webp', 'Terramorph pond and water feature service image'),
        ('assets/water-feature.webp', 'Terramorph water feature service image'),
    ]
    image_sitemap = '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9" xmlns:image="http://www.google.com/schemas/sitemap-image/1.1">\n'
    for image_path, caption in image_entries:
        image_sitemap += f'  <url><loc>{BASE_URL}/</loc><image:image><image:loc>{BASE_URL}/{image_path}</image:loc><image:caption>{caption}</image:caption></image:image></url>\n'
    for page_file, image_path, caption in ctx.get('EXTRA_IMAGE_SITEMAP', []):  # sustainable pages' credited reference photos
        image_sitemap += f'  <url><loc>{BASE_URL}/{page_file}</loc><image:image><image:loc>{BASE_URL}/{image_path}</image:loc><image:caption>{caption.replace("&", "&amp;").replace("<", "&lt;")}</image:caption></image:image></url>\n'
    image_sitemap += '</urlset>\n'
    (root / 'image-sitemap.xml').write_text(image_sitemap)

    robots = root / 'robots.txt'
    robots_text = robots.read_text() if robots.exists() else 'User-agent: *\nAllow: /\n'
    if f'Sitemap: {BASE_URL}/image-sitemap.xml' not in robots_text:
        robots_text = robots_text.rstrip() + f'\nSitemap: {BASE_URL}/image-sitemap.xml\n'
        robots.write_text(robots_text)

    readme = root / 'README.md'
    text = readme.read_text()
    text = text.replace('# Terramorph V3.45 Website', '# Terramorph V3.48 Website')
    text = text.replace('## V3.45 priorities implemented', '## V3.48 priorities implemented')
    if 'V3.45 SEO/ad expansion' not in text:
        text += '''\n## V3.49 local growth/ad expansion\n- Added 28 more city/service pages for Sylvania, Bowling Green, Holland, Waterville, Whitehouse, Oregon, and Rossford.\n- Added 10 clearly labeled hypothetical planning examples for common Northwest Ohio project scenarios.\n- Added three completed-work spotlights using original archived Terramorph field photos and verifiable visible details.\n- Added a review request page to support Google Business Profile review generation.\n- Added 4 dedicated Meta ad landing pages for backyard patios, standing water, curb appeal, and spring cleanup.\n- Updated sitemap with all new indexable service, guide, completed-work, and ad landing pages while keeping hypothetical planning examples out of organic search.\n- Added Google Business Profile, BBB, Facebook, and Instagram entity/proof links sitewide.\n- Added a website terms page and footer contact/proof links.\n'''
    text = text.replace(
        '- Updated sitemap with all new indexable service, guide, planning, and ad landing pages while keeping thank-you/review notes excluded.',
        '- Kept paid campaign pages and hypothetical planning examples out of the organic sitemap while leaving them available to direct visitors.'
    )
    readme.write_text(text)

    checklist = root / 'SEO_META_TRACKING_CHECKLIST.md'
    if checklist.exists():
        c = checklist.read_text()
        if 'V3.45 added landing pages' not in c:
            c += '''\n## V3.48 added landing pages\n\nRecommended Meta/Google campaign destinations added in this expansion:\n\n```text\nhttps://terramorphllc.com/lp-backyard-patio-estimate.html?utm_source=facebook&utm_medium=paid_social&utm_campaign=backyard_patio_estimate&utm_content={{ad.name}}\nhttps://terramorphllc.com/lp-standing-water-yard.html?utm_source=facebook&utm_medium=paid_social&utm_campaign=standing_water_drainage&utm_content={{ad.name}}\nhttps://terramorphllc.com/lp-curb-appeal-upgrade.html?utm_source=facebook&utm_medium=paid_social&utm_campaign=curb_appeal_upgrade&utm_content={{ad.name}}\nhttps://terramorphllc.com/lp-spring-cleanup.html?utm_source=facebook&utm_medium=paid_social&utm_campaign=spring_cleanup&utm_content={{ad.name}}\n```\n'''
            checklist.write_text(c)

    # Final metadata normalization keeps generated titles SERP-safe after all pages are written.
    import re, html
    title_overrides = {
        'services.html':'Landscaping Services: Cleanups, Snow, Patios & Drainage | Terramorph',
        'landscaping-toledo-ohio.html':'Landscaping in Toledo, OH | Terramorph',
        'landscaping-perrysburg-ohio.html':'Landscaping in Perrysburg, OH | Terramorph',
        'landscaping-maumee-ohio.html':'Landscaping in Maumee, OH | Terramorph',
        'drainage-solutions-toledo-ohio.html':'Drainage Solutions in Toledo, OH | Terramorph',
        'drainage-solutions-perrysburg-ohio.html':'Drainage Solutions in Perrysburg, OH | Terramorph',
        'drainage-solutions-maumee-ohio.html':'Drainage Solutions in Maumee, OH | Terramorph',
        'paver-patios-toledo-ohio.html':'Paver Patios in Toledo, OH | Terramorph',
        'paver-patios-perrysburg-ohio.html':'Paver Patios in Perrysburg, OH | Terramorph',
        'paver-patios-maumee-ohio.html':'Paver Patios in Maumee, OH | Terramorph',
        'best-plants-for-ohio-clay-soil.html':'Best Plants for Ohio Clay Soil | Terramorph',
        'french-drains-vs-pop-up-emitters.html':'French Drains vs Pop-Up Emitters | Terramorph',
        'how-to-choose-landscaper-toledo.html':'How to Choose a Toledo Landscaper | Terramorph',
        'move-water-away-from-house.html':'Move Water Away From Your House | Terramorph',
        'mulch-vs-rock-landscape-beds.html':'Mulch vs Rock Landscape Beds | Terramorph',
        'native-plants-vs-lawn-ohio.html':'Native Plants vs Lawn in Ohio | Terramorph',
        'native-prairie-landscaping-ohio.html':'Native Prairie Landscaping Ohio | Terramorph',
        'northwest-ohio-yard-drainage-problems.html':'Why Northwest Ohio Yards Hold Water | Terramorph',
        'outdoor-lighting-cost-ohio.html':'Outdoor Lighting Cost in Ohio | Terramorph',
        'paver-patio-northwest-ohio-weather.html':'Paver Patios for Ohio Weather | Terramorph',
        'spring-cleanup-northwest-ohio.html':'Spring Cleanup Northwest Ohio | Terramorph',
        'whitehouse-new-construction-landscape-case-study.html':'Whitehouse Landscape Planning Example | Terramorph',
    }
    desc_overrides = {
        'services.html':'Explore Terramorph landscaping, patios, drainage, lighting, maintenance, cleanups, walls, sod, mulch, snow, and commercial outdoor services in Northwest Ohio.'
    }
    for path in root.glob('*.html'):
        html_text = path.read_text()
        new_title = title_overrides.get(path.name)
        if new_title:
            html_text = re.sub(r'<title>.*?</title>', f'<title>{new_title}</title>', html_text, count=1, flags=re.S)
            escaped = html.escape(new_title, quote=True)
            html_text = re.sub(r'<meta property="og:title" content="[^"]*">', f'<meta property="og:title" content="{escaped}">', html_text)
            html_text = re.sub(r'<meta name="twitter:title" content="[^"]*">', f'<meta name="twitter:title" content="{escaped}">', html_text)
        if path.name in desc_overrides:
            escaped_desc = html.escape(desc_overrides[path.name], quote=True)
            html_text = re.sub(r'<meta name="description" content="[^"]*">', f'<meta name="description" content="{escaped_desc}">', html_text)
            html_text = re.sub(r'<meta property="og:description" content="[^"]*">', f'<meta property="og:description" content="{escaped_desc}">', html_text)
            html_text = re.sub(r'<meta name="twitter:description" content="[^"]*">', f'<meta name="twitter:description" content="{escaped_desc}">', html_text)
        html_text = html_text.replace('v=3.44', 'v=3.49').replace('v=3.48', 'v=3.49')
        path.write_text(html_text)

    return extra_pages

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
    service_defs = [
        ('Landscape Design', 'landscaping', 'landscaping', 'Landscape design, bed refreshes, plantings, mulch, rock, cleanup, lighting coordination, and curb appeal planning', 'real-entry.webp?v=3.14'),
        ('Paver Patios and Hardscapes', 'paver-patios', 'paver patios', 'Paver patios, walkways, steps, seating areas, hardscape upgrades, fire pit areas, and outdoor living plans', 'real-patio.webp?v=3.14'),
        ('Drainage Solutions', 'drainage-solutions', 'drainage solutions', 'Standing water diagnosis, downspout routing, grading review, low-spot fixes, and drainage planning', 'real-drainage.webp'),
        ('Lawn Maintenance', 'lawn-maintenance', 'lawn maintenance', 'Mowing, trimming, edging, bed upkeep, cleanup support, and recurring property presentation', 'real-lawn.webp'),
    ]

    extra_city_pages = []
    for city in cities:
        city_slug = city.lower().replace(' ', '-')
        for service, service_slug, keyword_service, service_copy, image in service_defs:
            filename = f'{service_slug}-{city_slug}-ohio.html'
            headline = f'{service} in {city}, Ohio for properties that need a clearer outdoor plan.'
            lead = f'Terramorph helps {city} homeowners and property owners with {service_copy.lower()} backed by free estimates and Jobber follow-up.'
            angle = f'{city} projects often involve {notes[city]}. Terramorph reviews grade, access, water movement, materials, photos, and timeline before recommending a scope.'
            faqs = [
                (f'Does Terramorph offer {keyword_service} in {city}?', f'Yes. Terramorph serves {city} and nearby Northwest Ohio areas with {keyword_service} and related outdoor property work.'),
                ('Can I request a free estimate online?', 'Yes. Use the secure quote form to send the service need, property details, photos, and timeline directly to Terramorph.'),
                ('Can photos be included with the request?', 'Yes. Photos are helpful because they show access, grade, existing conditions, water movement, beds, lawn areas, or hardscape details before follow-up.'),
            ]
            desc = f'Terramorph provides {keyword_service} in {city}, Ohio with free estimates for homeowners, businesses, and property owners.'
            body = f'''
<section class="page-hero premium-page-hero city-service-hero">
  <div class="page-hero-image"><img src="assets/{image}" alt="Terramorph {service} in {city}, Ohio"></div><div class="hero-overlay"></div>
  <div class="container page-hero-content"><p class="crumb"><a href="index.html">Home</a> / <a href="service-areas.html">Service Areas</a> / {city} {service}</p><p class="eyebrow light">{keyword_service} in {city}, Ohio</p><h1>{headline}</h1><p>{lead}</p><div class="cta-row"><a class="btn btn-gold" href="#quote">Request a {city} Estimate</a><a class="btn btn-outline-light" href="tel:{TEL}">Call {PHONE}</a></div></div>
</section>
{trust_band()}
<section class="section"><div class="container local-grid"><div><p class="eyebrow">Local fit</p><h2>{city} outdoor work needs local judgment.</h2><p>{angle}</p><p>These local pages help homeowners understand the Terramorph services available in their city before requesting an estimate.</p></div><div class="authority-list"><div><b>Property review</b><span>Service need, city, address, photos, timeline, and visible site conditions.</span></div><div><b>Connected services</b><span>Drainage, patios, beds, lighting, cleanups, and maintenance can be scoped together when it makes sense.</span></div><div><b>Northwest Ohio conditions</b><span>Clay soil, flat lots, freeze-thaw, and heavy rain are considered before recommendations.</span></div><div><b>Fast follow-up</b><span>Quote requests include the details the team needs to respond with the right next step.</span></div></div></div></section>
{faq_section(faqs)}
<section class="section quote-section"><div class="container quote-grid">{quote_form('Request a ' + city + ' ' + service + ' Estimate')}<div class="cta-proof"><p class="eyebrow">Fast estimate path</p><h2>Send photos, timeline, and service details in one secure request.</h2>{review_stack(2)}</div></div></section>
'''
            (root / filename).write_text(page(headline + ' | Terramorph', desc, body, schema_for(filename, headline, desc, faqs, service)))
            extra_city_pages.append(filename)

    case_studies = [
        ('perrysburg-paver-patio-case-study.html','Perrysburg','Paver Patios and Hardscapes','Perrysburg Paver Patio Planning Example','The backyard needed a better place to grill, sit, and connect the house to the lawn without creating drainage or freeze-thaw problems.','Terramorph reviews door transitions, base prep, water movement, access, seating layout, edge restraint, lighting options, and how the patio should tie into beds and lawn.','A clearer patio scope gives the homeowner a usable outdoor living area, cleaner flow, and fewer surprises before installation.','real-patio.webp?v=3.14'),
        ('maumee-yard-drainage-case-study.html','Maumee','Drainage Solutions','Maumee Yard Drainage Planning Example','Water was collecting after rain near low lawn areas, bed edges, and hardscape transitions where Northwest Ohio clay soil slowed drying.','Terramorph traces water sources, downspout paths, grade, discharge options, and whether grading, swales, buried lines, or bed changes make sense.','A practical drainage plan moves water intentionally instead of guessing at a single product.','real-drainage.webp'),
        ('toledo-front-yard-curb-appeal-case-study.html','Toledo','Landscape Design','Toledo Front Yard Curb Appeal Planning Example','The front beds looked tired and disconnected from the entry, making the home feel less finished from the street.','Terramorph evaluates bed shape, plant selection, mulch or rock, edging, lighting, maintenance expectations, and how the front walk should feel.','A cleaner first impression with a landscape scope that is easier to maintain and better matched to the house.','real-entry.webp?v=3.14'),
        ('sylvania-landscape-bed-refresh-case-study.html','Sylvania','Landscape Design','Sylvania Landscape Bed Refresh Planning Example','Mature plantings and older bed edges needed a reset without making the property look overbuilt or hard to maintain.','Terramorph reviews sun and shade, soil, existing plant health, bed depth, mulch versus rock, pruning, and replacement planting options.','A cleaner bed design preserves what works and updates what looks dated.','real-entry.webp?v=3.14'),
        ('bowling-green-lawn-maintenance-case-study.html','Bowling Green','Lawn Maintenance','Bowling Green Lawn Maintenance Planning Example','The property needed dependable mowing, trimming, and bed upkeep so the outside stayed clean during the growing season.','Terramorph defines route fit, frequency, access, trimming details, bed maintenance needs, and seasonal cleanup add-ons.','A simpler maintenance plan keeps curb appeal steady without the owner chasing one-off work.','real-lawn.webp'),
        ('holland-standing-water-case-study.html','Holland','Drainage Solutions','Holland Standing Water Planning Example','A flat area of lawn stayed wet after storms, limiting use and making maintenance harder.','Terramorph checks roof water, soil compaction, low spots, slope, discharge routes, and whether grading or drainage lines fit the property.','A clearer path to dry the usable lawn area and protect nearby beds or hardscape edges.','real-drainage.webp'),
        ('waterville-outdoor-living-case-study.html','Waterville','Paver Patios and Hardscapes','Waterville Outdoor Living Planning Example','The backyard needed a more intentional gathering area that connected patio use, walkways, and landscape beds.','Terramorph maps traffic flow, seating, grill placement, drainage, lighting, bed transitions, and base prep before pricing the project.','A backyard plan feels designed instead of pieced together.','real-hardscape.webp?v=3.14'),
        ('whitehouse-new-construction-landscape-case-study.html','Whitehouse','Landscape Design','Whitehouse New Construction Landscape Planning Example','The home needed front and backyard landscaping after construction so the property felt finished and easier to maintain.','Terramorph reviews grade, soil, builder drainage, bed layout, plant choices, mulch or rock, sod edges, and maintenance goals.','A phased landscape plan improves curb appeal while accounting for drainage and long-term upkeep.','real-entry.webp?v=3.14'),
        ('oregon-seasonal-cleanup-case-study.html','Oregon','Seasonal Cleanups','Oregon Seasonal Cleanup Planning Example','Leaf buildup, debris, and overgrown beds made the property look neglected after seasonal weather.','Terramorph scopes cleanup, trimming, debris removal, bed reset, mulch, and recurring maintenance needs.','A cleaner property reset prepares the yard for the next season.','real-mulch.webp'),
        ('rossford-walkway-patio-case-study.html','Rossford','Paver Patios and Hardscapes','Rossford Walkway and Patio Planning Example','The homeowner needed safer movement from the house to outdoor areas with a cleaner hardscape transition.','Terramorph evaluates grade, steps, walkway width, drainage, base prep, edge restraint, and how the hardscape connects to beds and lawn.','A more usable outdoor path and patio area improves curb appeal and reduces guesswork.','real-walkway.webp?v=3.14'),
    ]
    case_files = []
    for filename, city, service, title, problem, solution, outcome, image in case_studies:
        faqs = [(f'Does Terramorph handle {service.lower()} in {city}?', f'Yes. Terramorph serves {city} and surrounding Northwest Ohio communities with {service.lower()} and related outdoor property work.'), ('Can I send photos before an estimate?', 'Yes. Photos help Terramorph understand access, water movement, existing conditions, and project fit before follow-up.'), ('Is this an exact price example?', 'No. This is a planning example showing common local property problems and how Terramorph thinks through them. Final scope depends on the actual property.')]
        desc = f'{title}: local Terramorph project planning for {service.lower()} in {city}, Ohio.'
        body = f'''
<section class="page-hero premium-page-hero planning-example-hero"><div class="page-hero-image"><img src="assets/{image}" alt="{title}"></div><div class="hero-overlay"></div><div class="container page-hero-content"><p class="crumb"><a href="index.html">Home</a> / <a href="projects.html">Projects</a> / {city}</p><p class="eyebrow light">Local planning example</p><h1>{title}</h1><p>{desc}</p><div class="cta-row"><a class="btn btn-gold" href="#quote">Request Similar Work</a><a class="btn btn-outline-light" href="tel:{TEL}">Call {PHONE}</a></div></div></section>
{trust_band()}
<section class="section"><div class="container problem-grid"><div class="problem-card dark"><p class="eyebrow light">Problem</p><h2>{problem}</h2></div><div class="problem-card light-card"><p class="eyebrow">Terramorph approach</p><h2>{solution}</h2></div></div></section>
<section class="section clay-section"><div class="container local-grid"><div><p class="eyebrow">Expected outcome</p><h2>{outcome}</h2><p>This planning example shows the kind of details homeowners can send before a quote: city, service need, photos, timeline, and the result they want.</p></div><div class="authority-list"><div><b>City</b><span>{city}, Ohio and nearby communities.</span></div><div><b>Service</b><span>{service}</span></div><div><b>Estimate path</b><span>Request details through Jobber with city, photos, timeline, and project notes.</span></div></div></div></section>
{faq_section(faqs)}
<section class="section quote-section"><div class="container quote-grid">{quote_form('Request Similar Terramorph Work')}<div class="cta-proof"><p class="eyebrow">Local proof</p><h2>Use this as a starting point for your own property.</h2>{review_stack(2)}</div></div></section>
'''
        (root / filename).write_text(page(title + ' | Terramorph', desc, body, schema_for(filename, title, desc, faqs, service)))
        case_files.append(filename)

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
    meta_landing_page('lp-curb-appeal-upgrade.html', 'Front Yard Curb Appeal Estimate', 'Front yard curb appeal estimate', 'real-entry.webp?v=3.14', 'Make the front of the home look finished.', 'Request a free curb appeal assessment for landscape beds, plantings, mulch, rock, edging, lighting, and front-entry upgrades.', ['The front yard looks tired, builder-grade, overgrown, empty, or disconnected from the house.', 'Terramorph reviews bed shape, plant selection, soil, sun, mulch versus rock, edging, lighting, and maintenance expectations.', 'Curb appeal should be simple to understand.', 'A good front yard upgrade makes the home feel cleaner, more premium, and easier to maintain.'], 'Landscape Design', 'Request My Curb Appeal Estimate', 'Free Front Yard Curb Appeal Assessment', ['Front beds look empty or overgrown', 'Old shrubs or messy edges', 'Not sure what plants fit the house', 'Want a cleaner entry and better first impression'], [('Street view', 'What people notice from the road, driveway, sidewalk, and front door.'), ('Conditions', 'Sun, shade, soil, water, existing plants, and maintenance level.'), ('Plan', 'Bed shape, plant palette, mulch or rock, edging, lighting, and phased budget.')])
    meta_landing_page('lp-spring-cleanup.html', 'Spring Cleanup Estimate', 'Spring cleanup estimate', 'real-mulch.webp', 'Reset the property before the season gets away from you.', 'Request a free spring cleanup estimate for leaves, debris, pruning, bed reset, mulch, trimming, and property prep.', ['Winter left sticks, leaves, dead plant material, messy beds, weeds, and overgrown edges behind.', 'Terramorph reviews cleanup scope, bed condition, debris removal, pruning needs, mulch, and whether maintenance should continue after the reset.', 'A clean spring start makes the rest easier.', 'The right cleanup gets the property ready for mowing, mulch, planting, outdoor use, and better curb appeal.'], 'Seasonal Cleanups', 'Request My Spring Cleanup Estimate', 'Free Spring Cleanup + Bed Reset Estimate', ['Leaves and sticks everywhere', 'Messy beds or old mulch', 'Bushes and edges need trimming', 'Want mowing/maintenance set up after cleanup'], [('Cleanup', 'Leaves, sticks, debris, dead plant material, weeds, and edge reset.'), ('Refresh', 'Mulch, rock, pruning, trimming, plant replacement, and bed shaping.'), ('Maintain', 'Optional recurring lawn care and bed upkeep after the reset.')])

    faq_topics = [
        ('paver-patio-cost-toledo-ohio.html', 'How Much Does a Paver Patio Cost in Toledo, Ohio?', 'Paver patio cost depends on size, access, base prep, drainage, steps, patterns, borders, and whether the project includes seating, fire pits, lighting, or beds.', 'Paver Patios and Hardscapes', 'real-patio.webp?v=3.14', ['What affects patio pricing?', 'Size, excavation, base depth, drainage, paver style, edge restraint, steps, access, and finishing details all affect the final estimate.', 'Why is a site review important?', 'Northwest Ohio clay soil, grade, and water movement can change what base preparation and drainage planning are needed.', 'Can Terramorph give a free patio estimate?', 'Yes. Send city, approximate size, photos, and goals through the quote form for the best next step.']),
        ('yard-drainage-cost-northwest-ohio.html', 'How Much Does Yard Drainage Cost in Northwest Ohio?', 'Drainage cost depends on the water source, outlet route, grade, soil, distance, access, and whether the property needs drains, swales, grading, or downspout routing.', 'Drainage Solutions', 'real-drainage.webp', ['Why is drainage pricing hard without seeing the yard?', 'A wet yard can come from roof water, neighbor runoff, low spots, clay soil, hardscape slope, or grade issues. The fix changes with the source.', 'Is every drainage fix a French drain?', 'No. Some properties need grading, swales, downspout extensions, catch basins, dry creek features, or a combination.', 'Can Terramorph inspect standing water?', 'Yes. Terramorph offers free drainage estimates for Wood and Lucas County properties.']),
        ('landscaping-cost-perrysburg-ohio.html', 'How Much Does Landscaping Cost in Perrysburg, Ohio?', 'Landscape pricing depends on bed size, plant selection, mulch or rock, edging, soil, existing removals, drainage, lighting, and whether the project is phased.', 'Landscape Design', 'real-entry.webp?v=3.14', ['What changes a landscape estimate?', 'Plant count, plant size, bed depth, edging, removals, mulch or rock, drainage, soil, lighting, and access all affect scope.', 'Can landscaping be phased?', 'Yes. Many homeowners start with front curb appeal, then add patios, lighting, drainage, or backyard areas later.', 'Does Terramorph handle design and install?', 'Yes. Terramorph can plan and install beds, plants, mulch, rock, edging, sod, and related outdoor upgrades.']),
        ('best-plants-for-ohio-clay-soil.html', 'Best Landscape Plants for Ohio Clay Soil and Wet Yards', 'Ohio clay soil can hold water, compact easily, and stress the wrong plants. Better plant choices depend on sun, drainage, mature size, and maintenance expectations.', 'Landscape Design', 'real-planting.webp', ['Why does clay soil matter?', 'Clay can stay wet, compact, and drain slowly, so plant selection and bed preparation matter more than just picking what looks good.', 'Can wet-yard planting replace drainage?', 'Sometimes plants help, but persistent standing water usually needs grade, routing, or drainage review too.', 'Can Terramorph recommend plants?', 'Yes. Terramorph reviews sun, soil, water, house style, and maintenance goals before recommending plantings.']),
        ('spring-cleanup-cost-toledo-ohio.html', 'Spring Cleanup Cost in Toledo and Northwest Ohio', 'Spring cleanup pricing depends on debris volume, leaf removal, pruning, bed reset, mulch, edging, hauling, and whether maintenance continues after the cleanup.', 'Seasonal Cleanups', 'real-mulch.webp', ['What is included in spring cleanup?', 'Common cleanup work includes sticks, leaves, dead plant material, bed reset, trimming, edging, debris hauling, and optional mulch.', 'When should cleanup be scheduled?', 'Early spring is best once winter debris is visible and before weeds and growth get ahead of the property.', 'Can cleanup turn into ongoing maintenance?', 'Yes. Terramorph can pair cleanup with mowing, trimming, bed maintenance, and seasonal follow-up.']),
        ('lawn-maintenance-cost-northwest-ohio.html', 'Lawn Maintenance Cost in Northwest Ohio', 'Lawn maintenance cost depends on property size, mowing frequency, trimming, edging, obstacles, bed upkeep, commercial needs, and seasonal cleanup add-ons.', 'Lawn Maintenance', 'real-lawn.webp', ['What affects mowing price?', 'Lot size, route fit, mowing frequency, trimming, edging, slopes, gates, obstacles, and cleanup expectations affect pricing.', 'Do you maintain commercial properties?', 'Yes. Terramorph can help with residential, commercial, and property-owner maintenance needs.', 'Can lawn care include beds?', 'Yes. Bed maintenance, weeding, trimming, cleanup, mulch, and seasonal resets can be scoped with mowing.']),
        ('outdoor-lighting-cost-ohio.html', 'Outdoor Lighting Cost for Patios, Walkways, and Landscaping in Ohio', 'Outdoor lighting cost depends on fixture count, transformer size, wire runs, controls, path safety, accent areas, and whether lighting is added during a larger project.', 'Outdoor Lighting', 'real-lighting.webp?v=3.14', ['What affects outdoor lighting cost?', 'Fixture type, number of lights, wire runs, transformer placement, controls, trenching, and design complexity all matter.', 'Can lighting be added to patios or beds?', 'Yes. Lighting often works best when planned with patios, walkways, beds, retaining walls, or curb appeal upgrades.', 'Does Terramorph install landscape lighting?', 'Yes. Terramorph handles outdoor lighting for paths, patios, entries, beds, and nighttime curb appeal.']),
        ('how-to-choose-landscaper-toledo.html', 'How to Choose a Landscaper in Toledo, Perrysburg, Maumee, and Northwest Ohio', 'The best landscaper should understand local soil, drainage, maintenance, hardscapes, communication, cleanup, reviews, and how services connect across the whole property.', 'Landscape Design', 'real-hero.webp', ['What should homeowners look for?', 'Look for local proof, reviews, clear estimates, professional communication, drainage awareness, photos, and a team that thinks through the whole property.', 'Why does local experience matter?', 'Northwest Ohio clay soil, flat lots, freeze-thaw, rain, and seasonal maintenance needs affect outdoor work.', 'Can Terramorph handle multiple services?', 'Yes. Terramorph connects design, patios, drainage, lighting, cleanup, lawn maintenance, and other property services.']),
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
        f'<a class="guide-card city-service-card" href="{name}"><span>Local service area</span><h3>{name.replace("-", " ").replace(".html", "").title()}</h3><p>Terramorph service information for this city and outdoor project type.</p><b>Open local page &rarr;</b></a>'
        for name in extra_city_pages
    )
    case_cards = ''.join(
        f'<a class="guide-card planning-example-card" href="{filename}"><span>{city} &middot; {service}</span><h3>{title}</h3><p>{problem}</p><b>View case study &rarr;</b></a>'
        for filename, city, service, title, problem, solution, outcome, image in case_studies
    )
    service_areas = root / 'service-areas.html'
    service_html = service_areas.read_text()
    if 'V3.45 expanded service area pages' not in service_html:
        section = f'<section class="section guide-index-section v345-expanded-service-pages"><div class="container section-heading compact"><p class="eyebrow">More service areas</p><h2>Local service information by city and project type.</h2><p>Homeowners in Sylvania, Bowling Green, Holland, Waterville, Whitehouse, Oregon, and Rossford can review the most relevant Terramorph services before requesting an estimate.</p></div><div class="container guide-grid">{city_cards}</div></section>'
        service_html = service_html.replace('<section class="section quote-section">', section + '\n<section class="section quote-section">')
        service_areas.write_text(service_html)
    projects_page = root / 'projects.html'
    projects_html = projects_page.read_text()
    if 'V3.45 local case studies' not in projects_html:
        section = f'<section class="section guide-index-section v345-case-studies"><div class="container section-heading compact"><p class="eyebrow">Local planning examples</p><h2>Common outdoor project scenarios around Northwest Ohio.</h2><p>Each example shows a typical property problem, how Terramorph would think through the scope, and what to include when requesting an estimate.</p></div><div class="container guide-grid">{case_cards}</div></section>'
        projects_html = projects_html.replace('<section class="section transformation-section proof-gallery-section">', section + '\n<section class="section transformation-section proof-gallery-section">')
        projects_page.write_text(projects_html)

    # Add generated pages to sitemap without indexing thank-you/review-notes.
    sitemap_path = root / 'sitemap.xml'
    sitemap = sitemap_path.read_text()
    extra_pages = extra_city_pages + case_files + faq_files + ['reviews.html', 'lp-backyard-patio-estimate.html', 'lp-standing-water-yard.html', 'lp-curb-appeal-upgrade.html', 'lp-spring-cleanup.html']
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
    image_sitemap += '</urlset>\n'
    (root / 'image-sitemap.xml').write_text(image_sitemap)

    robots = root / 'robots.txt'
    robots_text = robots.read_text() if robots.exists() else 'User-agent: *\nAllow: /\n'
    if f'Sitemap: {BASE_URL}/image-sitemap.xml' not in robots_text:
        robots_text = robots_text.rstrip() + f'\nSitemap: {BASE_URL}/image-sitemap.xml\n'
        robots.write_text(robots_text)

    readme = root / 'README.md'
    text = readme.read_text()
    text = text.replace('# Terramorph V3.44 Website', '# Terramorph V3.45 Website')
    text = text.replace('## V3.44 priorities implemented', '## V3.45 priorities implemented')
    if 'V3.45 SEO/ad expansion' not in text:
        text += '''\n## V3.45 local growth/ad expansion\n- Added 28 more city/service pages for Sylvania, Bowling Green, Holland, Waterville, Whitehouse, Oregon, and Rossford.\n- Added 10 local planning example pages for common Northwest Ohio project scenarios.\n- Added a review request page to support Google Business Profile review generation.\n- Added 4 dedicated Meta ad landing pages for backyard patios, standing water, curb appeal, and spring cleanup.\n- Updated sitemap with all new indexable service, guide, planning, and ad landing pages while keeping thank-you/review notes excluded.\n'''
    readme.write_text(text)

    checklist = root / 'SEO_META_TRACKING_CHECKLIST.md'
    if checklist.exists():
        c = checklist.read_text()
        if 'V3.45 added landing pages' not in c:
            c += '''\n## V3.45 added landing pages\n\nRecommended Meta/Google campaign destinations added in this expansion:\n\n```text\nhttps://terramorphllc.com/lp-backyard-patio-estimate.html?utm_source=facebook&utm_medium=paid_social&utm_campaign=backyard_patio_estimate&utm_content={{ad.name}}\nhttps://terramorphllc.com/lp-standing-water-yard.html?utm_source=facebook&utm_medium=paid_social&utm_campaign=standing_water_drainage&utm_content={{ad.name}}\nhttps://terramorphllc.com/lp-curb-appeal-upgrade.html?utm_source=facebook&utm_medium=paid_social&utm_campaign=curb_appeal_upgrade&utm_content={{ad.name}}\nhttps://terramorphllc.com/lp-spring-cleanup.html?utm_source=facebook&utm_medium=paid_social&utm_campaign=spring_cleanup&utm_content={{ad.name}}\n```\n'''
            checklist.write_text(c)

    return extra_pages

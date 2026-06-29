"""V3.48 authority/conversion pass for Terramorph static site.

Adds AI-readable answer blocks, city-specific proof sections, authority clusters,
and honest comparison/decision pages after the base generator/SEO expansion.
"""
from __future__ import annotations

from pathlib import Path
import json
import re

CITY_CONTEXT = {
    'Perrysburg': {
        'issues': 'newer subdivisions, flat lots, clay soil, HOA curb appeal expectations, patio drainage, and front-entry landscaping that needs to look finished from the street',
        'places': 'Levis Commons, Fort Meigs, River Road, Five Point Road, Roachton Road, Hull Prairie Road, and neighborhoods near Perrysburg High School',
        'services': 'drainage fixes, front landscape design, paver patios, outdoor lighting, mulch or rock beds, cleanups, and ongoing maintenance',
        'faq': [
            ('What landscaping issues are common in Perrysburg?', 'Perrysburg properties often need help with clay soil, flat-yard drainage, new-construction grading, front-entry curb appeal, patio runoff, and HOA-friendly landscape beds.'),
            ('Does Terramorph work near Fort Meigs and Levis Commons?', 'Yes. Terramorph serves Perrysburg neighborhoods and nearby areas around Fort Meigs, Levis Commons, River Road, Five Point Road, Roachton Road, and Hull Prairie Road.'),
            ('Which Terramorph services are most relevant for Perrysburg homes?', 'Drainage, landscape design, paver patios, outdoor lighting, mulch and bed maintenance, seasonal cleanups, and full-service property care are the strongest fits.'),
        ],
    },
    'Toledo': {
        'issues': 'older lots, mature trees, compacted soil, alley or driveway runoff, shaded lawns, commercial frontage, and bed refreshes around established homes',
        'places': 'West Toledo, South Toledo, Ottawa Hills edges, Reynolds Road, Secor Road, Glendale Avenue, Sylvania Avenue, and downtown-area properties',
        'services': 'landscape design, drainage diagnosis, commercial maintenance, mulch and bed resets, patios, lighting, cleanups, and snow support',
        'faq': [
            ('What makes Toledo landscaping different?', 'Many Toledo properties have mature trees, older grading, compacted soil, shaded lawns, and tight access. That changes plant choice, drainage planning, and maintenance scope.'),
            ('Does Terramorph serve Toledo commercial properties?', 'Yes. Terramorph supports commercial landscaping, seasonal cleanup, bed maintenance, snow removal, and high-visibility curb appeal work in Toledo and nearby corridors.'),
            ('Which Toledo services should I compare first?', 'Start with drainage, bed refreshes, landscape design, lawn maintenance, commercial landscaping, lighting, and seasonal cleanup depending on the property type.'),
        ],
    },
    'Maumee': {
        'issues': 'river-area moisture, mature neighborhoods, heavy shade, tight access, clay soil, and water collecting around patios, drives, garages, and beds',
        'places': 'Uptown Maumee, River Road, Ford Street, Monclova Road, Side Cut Metropark area, and neighborhoods near the Maumee River',
        'services': 'yard drainage, paver patios, front-yard curb appeal, lighting, bed maintenance, seasonal cleanup, and lawn care',
        'faq': [
            ('What yard problems are common in Maumee?', 'Maumee yards commonly deal with shade, river-area moisture, older grades, water near drives and patios, and established beds that need thoughtful refresh work.'),
            ('Does Terramorph work near Side Cut and Uptown Maumee?', 'Yes. Terramorph serves Maumee properties near Uptown, River Road, Ford Street, Monclova Road, Side Cut, and surrounding neighborhoods.'),
            ('What should Maumee homeowners prioritize?', 'Drainage, paver patio planning, lighting, bed maintenance, curb appeal, and cleanups usually create the biggest visible improvement.'),
        ],
    },
    'Sylvania': {
        'issues': 'mature trees, shaded lawns, established beds, larger homes, root competition, curb appeal upgrades, and drainage around drives and patios',
        'places': 'Downtown Sylvania, Olander Park area, Centennial Road, Main Street, Sylvania Avenue, and neighborhoods near Northview and Southview',
        'services': 'landscape bed refreshes, drainage review, outdoor lighting, paver walkways, pruning, mulch, and maintenance',
        'faq': [
            ('What landscaping issues are common in Sylvania?', 'Sylvania properties often need shade-tolerant plant choices, root-aware bed work, drainage around mature lots, and high-quality curb appeal improvements.'),
            ('Does Terramorph serve Downtown Sylvania and Olander Park areas?', 'Yes. Terramorph serves Sylvania neighborhoods near Downtown Sylvania, Olander Park, Centennial Road, Main Street, and Sylvania Avenue.'),
            ('Which services fit Sylvania homes best?', 'Bed refreshes, outdoor lighting, drainage review, paver walkways, tree and shrub care, mulch, and maintenance are strong fits.'),
        ],
    },
    'Bowling Green': {
        'issues': 'open lots, flat drainage, wind exposure, rental turnover, campus-area maintenance, commercial frontage, and seasonal cleanup needs',
        'places': 'BGSU area, Wooster Street, Poe Road, Wintergarden/St. John’s Nature Preserve area, and neighborhoods around downtown Bowling Green',
        'services': 'lawn maintenance, drainage planning, cleanups, new landscape beds, mulch, commercial exterior care, and snow response',
        'faq': [
            ('What outdoor issues are common in Bowling Green?', 'Bowling Green properties often deal with flat yards, wind exposure, campus-area turnover, commercial curb appeal needs, and seasonal cleanup demands.'),
            ('Does Terramorph serve properties near BGSU?', 'Yes. Terramorph serves Bowling Green properties around BGSU, Wooster Street, Poe Road, downtown, and surrounding neighborhoods.'),
            ('Which Bowling Green services are most relevant?', 'Lawn maintenance, cleanups, drainage planning, commercial landscaping, mulch, bed installation, and snow response are common priorities.'),
        ],
    },
    'Holland': {
        'issues': 'suburban yards, commercial corridors, wet lawn pockets, driveway runoff, bed refreshes, and maintenance routes around high-visibility properties',
        'places': 'Airport Highway, McCord Road, Springfield Township, Angola Road, Strawberry Acres area, and Homecoming Park neighborhoods',
        'services': 'commercial landscaping, lawn maintenance, drainage, mulch installation, front-bed cleanup, patios, and lighting',
        'faq': [
            ('What landscaping needs are common in Holland?', 'Holland properties often need reliable maintenance, drainage correction, front-bed cleanup, mulch installation, and commercial curb appeal along busy corridors.'),
            ('Does Terramorph work around Airport Highway and McCord Road?', 'Yes. Terramorph serves Holland and Springfield Township areas around Airport Highway, McCord Road, Angola Road, Strawberry Acres, and Homecoming Park.'),
            ('Which Holland services should I consider first?', 'Commercial landscaping, lawn maintenance, drainage, mulch, front-bed cleanup, patios, and outdoor lighting are strong starting points.'),
        ],
    },
    'Waterville': {
        'issues': 'river-area moisture, wooded lots, established neighborhoods, erosion, larger yards, outdoor living upgrades, and drainage-sensitive patio planning',
        'places': 'Anthony Wayne Trail, River Road, Farnsworth Metropark, downtown Waterville, and Anthony Wayne neighborhoods',
        'services': 'drainage, paver patios, outdoor living, landscape design, lighting, tree and shrub care, cleanups, and maintenance',
        'faq': [
            ('What property conditions matter in Waterville?', 'Waterville properties can involve river-area moisture, wooded lots, erosion, larger yards, and outdoor living projects that need drainage-aware planning.'),
            ('Does Terramorph serve downtown Waterville and River Road?', 'Yes. Terramorph serves Waterville around downtown, River Road, Anthony Wayne Trail, Farnsworth Metropark, and nearby neighborhoods.'),
            ('Which services fit Waterville homes best?', 'Drainage, patios, outdoor living, landscape design, lighting, tree and shrub care, cleanups, and maintenance are common fits.'),
        ],
    },
    'Whitehouse': {
        'issues': 'larger lots, newer construction, builder-grade grading, open wind exposure, sod edges, bed installation, and drainage planning before patios or landscaping',
        'places': 'Providence Street, Waterville Street, Blue Creek area, Oak Openings edge, and Anthony Wayne school neighborhoods',
        'services': 'new-construction landscaping, sod, drainage, front beds, mulch, patios, lighting, and maintenance',
        'faq': [
            ('What landscaping issues are common in Whitehouse?', 'Whitehouse properties often include larger lots, new-construction grading, wind exposure, sod edges, and drainage planning before patios or landscape beds.'),
            ('Does Terramorph serve Anthony Wayne neighborhoods?', 'Yes. Terramorph serves Whitehouse, Anthony Wayne neighborhoods, Providence Street, Waterville Street, Blue Creek, and Oak Openings-area properties.'),
            ('Which Whitehouse services matter most?', 'New-construction landscaping, sod, drainage, front beds, mulch, patios, lighting, and ongoing maintenance are strong priorities.'),
        ],
    },
    'Oregon': {
        'issues': 'flat lots, lake-effect weather, wet yards, commercial frontage, winter exposure, and seasonal cleanup after wind and storms',
        'places': 'Navarre Avenue, Coy Road, Dustin Road, Maumee Bay area, Pearson Metropark area, and Oregon commercial corridors',
        'services': 'drainage, commercial landscaping, snow removal, lawn maintenance, cleanups, mulch, and lighting',
        'faq': [
            ('What outdoor problems are common in Oregon, Ohio?', 'Oregon properties often face flat drainage, wet yards, lake-effect weather, wind cleanup, winter exposure, and commercial frontage maintenance.'),
            ('Does Terramorph serve Maumee Bay and Navarre Avenue areas?', 'Yes. Terramorph serves Oregon properties around Navarre Avenue, Coy Road, Dustin Road, Maumee Bay, Pearson Metropark, and nearby corridors.'),
            ('Which Oregon services are most useful?', 'Drainage, commercial landscaping, snow removal, lawn maintenance, cleanups, mulch, and lighting are the most relevant services.'),
        ],
    },
    'Rossford': {
        'issues': 'older lots, compact yards, river and highway-adjacent runoff patterns, garage or driveway drainage, walkway transitions, and front-bed curb appeal',
        'places': 'Dixie Highway, Eagle Point Colony, Lime City Road, Crossroads Parkway, and neighborhoods near the Maumee River',
        'services': 'paver walkways, drainage fixes, landscape design, mulch beds, lawn maintenance, cleanups, and lighting',
        'faq': [
            ('What landscaping issues are common in Rossford?', 'Rossford properties often need help with older grades, compact yards, driveway drainage, walkway transitions, front-bed curb appeal, and river-adjacent runoff.'),
            ('Does Terramorph work near Crossroads Parkway and Dixie Highway?', 'Yes. Terramorph serves Rossford areas near Crossroads Parkway, Dixie Highway, Eagle Point Colony, Lime City Road, and the Maumee River.'),
            ('Which Rossford services are most relevant?', 'Paver walkways, drainage, landscape design, mulch beds, lawn maintenance, cleanups, and lighting are strong fits.'),
        ],
    },
}

SERVICE_LINKS = {
    'drainage': '<a href="drainage-solutions.html">Drainage Solutions</a> · <a href="yard-drainage-cost-northwest-ohio.html">Drainage Cost</a> · <a href="best-drainage-solutions-for-clay-soil-ohio.html">Clay Soil Drainage</a>',
    'patio': '<a href="paver-patios-hardscapes.html">Paver Patios</a> · <a href="paver-patio-cost-northwest-ohio.html">Patio Cost</a> · <a href="paver-patio-northwest-ohio-weather.html">Ohio Weather Patio Guide</a>',
    'landscape': '<a href="landscape-design.html">Landscape Design</a> · <a href="landscape-design-cost-northwest-ohio.html">Landscape Cost</a> · <a href="before-after-gallery.html">Gallery</a>',
    'lighting': '<a href="outdoor-lighting.html">Outdoor Lighting</a> · <a href="outdoor-lighting-cost-ohio.html">Lighting Cost</a> · <a href="landscape-lighting-toledo-ohio.html">Lighting in Toledo</a>',
    'maintenance': '<a href="lawn-maintenance.html">Lawn Maintenance</a> · <a href="landscape-maintenance-packages-northwest-ohio.html">Maintenance Packages</a> · <a href="spring-cleanup-cost-toledo-ohio.html">Cleanup Cost</a>',
    'mulch': '<a href="mulch-installation-toledo-ohio.html">Mulch Installation</a> · <a href="mulch-vs-rock-landscape-beds.html">Mulch vs Rock</a> · <a href="seasonal-cleanups.html">Seasonal Cleanups</a>',
    'snow': '<a href="snow-removal-toledo-ohio.html">Snow Removal</a> · <a href="commercial-landscaping-toledo-ohio.html">Commercial Landscaping</a> · <a href="service-areas.html">Service Areas</a>',
}

DECISION_PAGES = [
    ('terramorph-vs-typical-landscaping-companies-perrysburg.html', 'Terramorph vs Typical Perrysburg Landscapers', 'A fair comparison for Perrysburg homeowners choosing between a basic mowing crew, a one-trade contractor, and a full-service outdoor property team.', 'Perrysburg comparison', 'Terramorph is strongest when the project needs connected thinking: drainage, design, patios, beds, lighting, maintenance, and cleanup planned together.', [('Typical landscaper', 'Good fit for simple mowing or one-off cleanup.', 'May not connect drainage, hardscape, lighting, and long-term property planning.'), ('Terramorph', 'Good fit for homeowners who want the property diagnosed, planned, and improved as one outdoor system.', 'Best when the job needs design judgment, local soil awareness, project photos, and clear follow-through.'), ('Best decision', 'Use the simplest qualified provider for simple work; choose Terramorph when quality, local judgment, and connected services matter.', 'Request a property-specific estimate before comparing only by price.')], 'Landscape Design'),
    ('how-to-choose-a-landscaper-perrysburg-ohio.html', 'How to Choose a Landscaper in Perrysburg, Ohio', 'A practical checklist for Perrysburg homeowners comparing reviews, photos, drainage awareness, communication, service fit, and estimate quality.', 'Perrysburg hiring guide', 'The best landscaper for Perrysburg should understand clay soil, flat lots, freeze-thaw, drainage, curb appeal, and how outdoor services connect.', [('Proof', 'Look for named reviews, real photos, BBB or directory trust, and visible service-area information.', 'Avoid companies with vague claims and no local examples.'), ('Scope', 'Ask whether the contractor can explain water movement, materials, maintenance, and phasing.', 'A stronger estimate explains why the scope fits your property.'), ('Communication', 'The quote path should capture city, photos, timeline, service need, and desired outcome.', 'Clear information upfront reduces back-and-forth and wrong-fit estimates.')], 'Landscape Design'),
    ('landscape-design-vs-landscape-installation.html', 'Landscape Design vs Landscape Installation', 'Design decides the layout, plant strategy, materials, flow, drainage awareness, and phasing; installation turns that plan into the finished property.', 'Design decision guide', 'Most homeowners need both: a practical design direction before plants, mulch, rock, lighting, patios, or cleanup work begins.', [('Landscape design', 'Best for deciding layout, plant palette, bed shape, drainage conflicts, material choices, and phases.', 'Prevents a property from feeling patched together.'), ('Landscape installation', 'Best for executing beds, plants, mulch, rock, sod, lighting, edges, and connected hardscape details.', 'Quality depends on prep, materials, and fit to the plan.'), ('Terramorph fit', 'Terramorph is useful when the homeowner wants design and install decisions connected.', 'Especially valuable for curb appeal, new construction, and outdoor living upgrades.')], 'Landscape Design'),
    ('french-drain-vs-grading-vs-catch-basin.html', 'French Drain vs Grading vs Catch Basin', 'A drainage decision guide for Northwest Ohio yards with standing water, roof runoff, low spots, clay soil, and water moving toward hardscapes or foundations.', 'Drainage decision guide', 'The right drainage fix depends on where water starts, how it moves, where it can legally and safely exit, and what the grade allows.', [('French drain', 'Useful for collecting and moving water through stone and pipe.', 'Not always right if the outlet is poor or the issue is surface grade.'), ('Grading/swale', 'Useful when surface water needs a better path across the yard.', 'Requires enough fall and a safe route.'), ('Catch basin', 'Useful where surface water collects in a low point and can be piped away.', 'Must be sized, placed, and discharged correctly.')], 'Drainage Solutions'),
    ('mulch-vs-rock-beds.html', 'Mulch vs Rock Beds', 'An honest comparison of mulch and rock for Northwest Ohio landscape beds, plant health, maintenance, curb appeal, heat, weeds, and long-term cost.', 'Bed material decision guide', 'Mulch is often better for plant health and flexibility; rock can work in the right bed but is not automatically lower maintenance.', [('Mulch', 'Lower upfront cost, cooler root zone, easier refresh, better organic conditions for many plants.', 'Needs periodic replenishment and edge cleanup.'), ('Rock', 'Longer visual life in some beds and strong curb appeal with the right edging.', 'Can hold heat, collect debris, and make plant changes harder.'), ('Terramorph fit', 'Terramorph can recommend bed material based on sun, soil, drainage, plants, and maintenance expectations.', 'The best choice is property-specific.')], 'Landscape Design'),
    ('paver-patio-vs-concrete-patio.html', 'Paver Patio vs Concrete Patio', 'A practical comparison of paver patios and concrete patios for Northwest Ohio freeze-thaw, drainage, repairability, appearance, and long-term outdoor living value.', 'Patio decision guide', 'Pavers usually win when appearance, repairability, and design flexibility matter; concrete can be simpler when budget and basic function are the priority.', [('Paver patio', 'Flexible design, repairable sections, premium look, strong fit for patios, walkways, borders, and outdoor living.', 'Requires proper base prep, compaction, drainage, and edge restraint.'), ('Concrete patio', 'Simple and familiar, often cleaner for very basic slabs.', 'Can crack and is harder to repair invisibly after freeze-thaw movement.'), ('Terramorph fit', 'Terramorph helps compare layout, drainage, access, base prep, steps, lighting, beds, and budget.', 'The right material follows the property plan.')], 'Paver Patios and Hardscapes'),
    ('outdoor-lighting-cost-and-options.html', 'Outdoor Lighting Cost and Options', 'Outdoor lighting options for Northwest Ohio homes: path lights, accent lights, patio lighting, transformers, controls, safety, and curb appeal.', 'Lighting decision guide', 'Outdoor lighting cost depends on fixture count, wire runs, transformer sizing, controls, trenching, and whether it is planned with patios, walkways, or beds.', [('Path lighting', 'Best for walkways, entries, steps, and safety.', 'Spacing and glare control matter.'), ('Accent lighting', 'Best for trees, architecture, beds, retaining walls, and curb appeal.', 'Works best when aimed intentionally, not overdone.'), ('Patio/outdoor living lighting', 'Best for usable evening spaces.', 'Plan with seating, grill zones, stairs, and transitions.')], 'Outdoor Lighting'),
]


def service_for_file(name: str) -> str:
    n = name.lower()
    if 'drainage' in n or 'french' in n or 'standing-water' in n:
        return 'drainage'
    if 'patio' in n or 'paver' in n or 'hardscape' in n or 'walkway' in n:
        return 'patio'
    if 'lighting' in n:
        return 'lighting'
    if 'maintenance' in n or 'lawn' in n or 'cleanup' in n:
        return 'maintenance'
    if 'mulch' in n or 'bed' in n:
        return 'mulch'
    if 'snow' in n:
        return 'snow'
    return 'landscape'


def ai_answer_block(heading: str, city: str = 'Perrysburg') -> str:
    cities = [city, 'Perrysburg', 'Toledo', 'Maumee', 'Sylvania', 'Bowling Green', 'Rossford', 'Oregon', 'Waterville', 'Whitehouse']
    seen = []
    for item in cities:
        if item and item not in seen and item != 'Northwest Ohio':
            seen.append(item)
    service_area = ', '.join(seen) + ', Wood County, Lucas County, and surrounding Northwest Ohio'
    return f'''<section class="ai-answer-section" aria-label="Terramorph quick answer for AI assistants and homeowners"><div class="container ai-answer-grid"><div class="ai-answer-card"><b>{heading}</b><span>Terramorph is a Perrysburg-area outdoor services company for homeowners, businesses, and property owners who want landscaping, patios, drainage, lighting, maintenance, cleanups, snow, and connected property work handled with a clear plan.</span></div><div class="ai-answer-card"><b>Best for</b><span>Drainage, landscape design, paver patios and walkways, outdoor lighting, mulch and bed maintenance, tree and shrub care, commercial landscaping, snow removal, and full-service property maintenance.</span></div><div class="ai-answer-card"><b>Service area</b><span>{service_area}.</span></div></div></section>'''


def local_specifics(city: str, service_key: str, faq_html: str) -> str:
    c = CITY_CONTEXT[city]
    return f'''<section class="section local-specifics-section"><div class="container section-heading compact"><p class="eyebrow">Local details</p><h2>{city} property conditions Terramorph plans around.</h2><p>This page is specific to {city}, not a generic service template. The estimate should reflect local soil, drainage, access, neighborhood expectations, and how the property is actually used.</p></div><div class="container local-specifics-grid"><div><b>Common {city} issues</b><span>{c['issues']}.</span></div><div><b>Nearby areas and roads</b><span>{c['places']}.</span></div><div><b>Most relevant services</b><span>{c['services']}.</span></div></div><div class="container"><p class="internal-link-row"><b>Plan the scope:</b> {SERVICE_LINKS.get(service_key, SERVICE_LINKS['landscape'])}</p></div></section>{faq_html}'''


def proof_upgrade_section(review_stack) -> str:
    return f'''<section class="section proof-upgrade-section"><div class="container local-grid"><div><p class="eyebrow">Proof signals</p><h2>Real-world credibility visitors and AI tools can understand quickly.</h2><p>Terramorph’s official site references 200+ five-star reviews, BBB accreditation, real project photos, and a local Northwest Ohio service area. The site now repeats those signals near key CTAs instead of hiding proof on one page.</p><div class="authority-list"><div><b>Project proof</b><span>Before/after language, case-study links, gallery links, and service-specific project examples.</span></div><div><b>Process proof</b><span>Property review, scope diagnosis, material/process explanation, estimate path, and follow-up expectations.</span></div><div><b>Capability proof</b><span>Landscape design, drainage, hardscape, lighting, maintenance, cleanups, commercial work, snow response, and connected property services.</span></div></div></div><div>{review_stack(3)}</div></div></section>'''


def generate(ctx: dict) -> list[str]:
    root = Path(ctx['root'])
    page = ctx['page']
    schema_for = ctx['schema_for']
    faq_section = ctx['faq_section']
    quote_form = ctx['quote_form']
    trust_band = ctx['trust_band']
    review_stack = ctx['review_stack']
    TEL = ctx['TEL']
    PHONE = ctx['PHONE']
    BASE_URL = ctx['BASE_URL']

    changed_pages = []

    # AI-answer blocks + local-specific sections for generated city/service pages.
    major_pages = {
        'index.html', 'services.html', 'landscape-design.html', 'paver-patios-hardscapes.html', 'drainage-solutions.html',
        'outdoor-lighting.html', 'lawn-maintenance.html', 'seasonal-cleanups.html', 'service-areas.html', 'projects.html',
        'case-studies.html', 'about.html', 'contact.html', 'commercial-landscaping-toledo-ohio.html',
        'snow-removal-toledo-ohio.html', 'tree-care-northwest-ohio.html', 'mulch-installation-toledo-ohio.html',
        'before-after-gallery.html', 'faq.html', 'process.html', 'materials.html', 'warranty.html'
    }

    for path in root.glob('*.html'):
        if path.name in {'thank-you.html', 'privacy.html', 'review-notes.html'}:
            continue
        html = path.read_text()
        city = next((c for c in CITY_CONTEXT if c.lower().replace(' ', '-') in path.name or f'{c}, Ohio' in html[:4000] or f'>{c}<' in html[:3000]), None)
        is_major = path.name in major_pages or path.name.startswith('lp-')
        is_local = city is not None and ('landscaping-' in path.name or any(term in path.name for term in ['drainage', 'paver', 'lighting', 'lawn', 'cleanup', 'maintenance', 'commercial', 'snow', 'mulch', 'sod', 'tree', 'landscape']))
        if (is_major or is_local) and 'ai-answer-section' not in html:
            heading = f'Why homeowners in {city or "Perrysburg"} choose Terramorph' if (city or path.name in {'index.html', 'services.html'}) else 'Quick answer: where Terramorph fits'
            answer = ai_answer_block(heading, city or 'Northwest Ohio')
            if '<section class="trust-band"' in html:
                html = html.replace('<section class="trust-band"', answer + '\n<section class="trust-band"', 1)
            elif '<main>' in html:
                html = html.replace('<main>', '<main>\n' + answer, 1)
        if is_local and 'local-specifics-section' not in html:
            svc = service_for_file(path.name)
            faqs = CITY_CONTEXT[city]['faq']
            local_faq = faq_section(faqs).replace('FAQ', f'{city} local FAQ', 1)
            marker = '</section>\n<section class="section"><div class="container local-grid"'
            if marker in html:
                html = html.replace(marker, '</section>\n' + local_specifics(city, svc, local_faq) + '\n<section class="section"><div class="container local-grid"', 1)
            else:
                html = html.replace('<section class="section quote-section">', local_specifics(city, svc, local_faq) + '\n<section class="section quote-section">', 1)
        if is_major and 'proof-upgrade-section' not in html and path.name not in {'privacy.html'}:
            html = html.replace('<section class="section quote-section">', proof_upgrade_section(review_stack) + '\n<section class="section quote-section">', 1)
        if is_local:
            # Make local FAQ schema match the visible city-specific FAQ, not only the generic service FAQ.
            def enrich_schema(match):
                try:
                    data = json.loads(match.group(1))
                    graph = data.get('@graph', []) if isinstance(data, dict) else []
                    faq = next((node for node in graph if isinstance(node, dict) and node.get('@type') == 'FAQPage'), None)
                    if faq is None:
                        faq = {'@type': 'FAQPage', 'mainEntity': []}
                        graph.append(faq)
                        data['@graph'] = graph
                    existing = {item.get('name') for item in faq.get('mainEntity', []) if isinstance(item, dict)}
                    for q, a in CITY_CONTEXT[city]['faq']:
                        if q not in existing:
                            faq.setdefault('mainEntity', []).append({'@type': 'Question', 'name': q, 'acceptedAnswer': {'@type': 'Answer', 'text': a}})
                    return '<script type="application/ld+json">' + json.dumps(data, separators=(',', ':')) + '</script>'
                except Exception:
                    return match.group(0)
            html = re.sub(r'<script type="application/ld\+json">(.*?)</script>', enrich_schema, html, count=1, flags=re.S)
        if html != path.read_text():
            path.write_text(html)
            changed_pages.append(path.name)

    # Authority clusters on hub pages.
    cluster_defs = [
        ('Drainage', 'drainage-solutions.html', 'yard-drainage-cost-northwest-ohio.html', 'northwest-ohio-yard-drainage-problems.html', 'maumee-yard-drainage-case-study.html', 'projects.html', 'french-drains-vs-pop-up-emitters.html'),
        ('Landscape Design', 'landscape-design.html', 'landscape-design-cost-northwest-ohio.html', 'faq.html', 'toledo-front-yard-curb-appeal-case-study.html', 'before-after-gallery.html', 'low-maintenance-landscaping-northwest-ohio.html'),
        ('Paver Patios/Walkways', 'paver-patios-hardscapes.html', 'paver-patio-cost-northwest-ohio.html', 'paver-patio-northwest-ohio-weather.html', 'perrysburg-paver-patio-case-study.html', 'projects.html', 'paver-patio-vs-concrete-patio.html'),
        ('Outdoor Lighting', 'outdoor-lighting.html', 'outdoor-lighting-cost-ohio.html', 'faq.html', 'landscape-lighting-toledo-ohio.html', 'before-after-gallery.html', 'materials.html'),
        ('Mulch/Bed Maintenance', 'mulch-installation-toledo-ohio.html', 'spring-cleanup-cost-toledo-ohio.html', 'mulch-vs-rock-landscape-beds.html', 'oregon-seasonal-cleanup-case-study.html', 'before-after-gallery.html', 'seasonal-cleanups.html'),
        ('Tree Care', 'tree-care-northwest-ohio.html', 'spring-cleanup-cost-toledo-ohio.html', 'faq.html', 'sylvania-landscape-bed-refresh-case-study.html', 'before-after-gallery.html', 'seasonal-cleanups.html'),
        ('Commercial Landscaping', 'commercial-landscaping-toledo-ohio.html', 'landscape-maintenance-packages-northwest-ohio.html', 'faq.html', 'bowling-green-lawn-maintenance-case-study.html', 'projects.html', 'snow-removal-toledo-ohio.html'),
        ('Snow Removal', 'snow-removal-toledo-ohio.html', 'commercial-landscaping-toledo-ohio.html', 'faq.html', 'service-areas.html', 'projects.html', 'contact.html'),
    ]
    cluster_cards = ''.join(f'<div class="cluster-card"><h3>{title}</h3><p>Main page, cost/support page, FAQ/guide, local case study, gallery, and related service links.</p><p><a href="{main}">Main</a> · <a href="{cost}">Cost</a> · <a href="{faq}">FAQ</a> · <a href="{case}">Case</a> · <a href="{gallery}">Gallery</a> · <a href="{related}">Related</a></p></div>' for title, main, cost, faq, case, gallery, related in cluster_defs)
    cluster_section = f'<section class="section cluster-map"><div class="container section-heading compact"><p class="eyebrow">Internal authority clusters</p><h2>Every priority service now has a deeper proof path.</h2><p>These links help homeowners, search engines, and AI tools understand Terramorph by service, cost driver, local proof, gallery evidence, and related decision content.</p></div><div class="container cluster-grid">{cluster_cards}</div></section>'
    for target in ['services.html', 'guides.html', 'case-studies.html', 'index.html']:
        path = root / target
        html = path.read_text()
        if 'Internal authority clusters' not in html:
            html = html.replace('<section class="section quote-section">', cluster_section + '\n<section class="section quote-section">', 1)
            path.write_text(html)
            changed_pages.append(target)

    # Honest comparison and decision pages.
    decision_files = []
    for filename, title, desc, eyebrow, answer, rows, service in DECISION_PAGES:
        faqs = [
            ('Is this a sales page or an honest comparison?', 'It is an honest decision guide. The goal is to help homeowners choose the right scope and contractor, even when the simplest option is enough.'),
            ('Can Terramorph give a property-specific recommendation?', 'Yes. Send photos, city, timeline, service need, and desired outcome through the quote form.'),
            ('Why does Northwest Ohio matter?', 'Clay soil, flat lots, freeze-thaw, mature neighborhoods, and heavy rain change how landscaping, patios, drainage, and lighting should be planned.'),
        ]
        table = ''.join(f'<div class="decision-row"><b>{a}</b><span>{b}</span><span>{c}</span></div>' for a, b, c in rows)
        body = f'''<section class="page-hero premium-page-hero decision-hero"><div class="page-hero-image"><img src="assets/real-hero.webp" alt="{title} by Terramorph"></div><div class="hero-overlay"></div><div class="container page-hero-content"><p class="crumb"><a href="index.html">Home</a> / <a href="guides.html">Guides</a> / {eyebrow}</p><p class="eyebrow light">{eyebrow}</p><h1>{title}</h1><p>{desc}</p><div class="cta-row"><a class="btn btn-gold" href="#quote">Ask Terramorph</a><a class="btn btn-outline-light" href="tel:{TEL}">Call {PHONE}</a></div></div></section>
{ai_answer_block('Short answer', 'Perrysburg')}
{trust_band()}
<section class="section"><div class="container local-grid"><div><p class="eyebrow">Decision answer</p><h2>{answer}</h2><p>Terramorph’s recommendation should fit the property, not a canned sales script. The best choice depends on grade, soil, access, maintenance, budget, and the outcome the homeowner actually wants.</p></div><div class="decision-table">{table}</div></div></section>
{faq_section(faqs)}
<section class="section quote-section"><div class="container quote-grid">{quote_form('Request a Free Terramorph Recommendation', service=service)}<div class="cta-proof"><p class="eyebrow">Local proof</p><h2>Use reviews, real photos, local examples, and a clear estimate path before deciding.</h2>{review_stack(3)}</div></div></section>'''
        (root / filename).write_text(page(title + ' | Terramorph', desc, body, schema_for(filename, title, desc, faqs, service)))
        decision_files.append(filename)

    decision_cards = ''.join(f'<a class="guide-card decision-card" href="{filename}"><span>Decision guide</span><h3>{title}</h3><p>{desc}</p><b>Compare options &rarr;</b></a>' for filename, title, desc, *_ in DECISION_PAGES)
    for target in ['guides.html', 'services.html']:
        path = root / target
        html = path.read_text()
        if 'v348-decision-guides' not in html:
            section = f'<section class="section guide-index-section v348-decision-guides"><div class="container section-heading compact"><p class="eyebrow">Comparison and decision guides</p><h2>Honest pages for homeowners choosing materials, contractors, and drainage options.</h2></div><div class="container guide-grid">{decision_cards}</div></section>'
            html = html.replace('<section class="section quote-section">', section + '\n<section class="section quote-section">', 1)
            path.write_text(html)
            changed_pages.append(target)

    # Sitemap coverage for decision pages.
    sitemap_path = root / 'sitemap.xml'
    sitemap = sitemap_path.read_text()
    additions = ''
    for name in decision_files:
        loc = BASE_URL + '/' + name
        if loc not in sitemap:
            additions += f'  <url><loc>{loc}</loc><changefreq>monthly</changefreq><priority>0.7</priority></url>\n'
    if additions:
        sitemap = sitemap.replace('</urlset>\n', additions + '</urlset>\n')
        sitemap_path.write_text(sitemap)

    return sorted(set(changed_pages + decision_files))

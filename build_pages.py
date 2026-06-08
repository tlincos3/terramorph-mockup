from pathlib import Path

root = Path('/Users/Jarvis/Desktop/Terramorph-Mockup')
PHONE = '419-637-4498'
TEL = '4196374498'

NAV = f'''
<a class="skip-link" href="#main">Skip to content</a>
<div class="topbar" aria-label="Trust and contact bar">
  <div class="container topbar-inner">
    <div class="topbar-proof">
      <span>★★★★★ 200+ Google Reviews</span>
      <span>BBB Member</span>
      <span>Licensed And Insured</span>
      <span>Wood and Lucas County</span>
    </div>
    <a class="topbar-phone" href="tel:{TEL}">Call {PHONE}</a>
  </div>
</div>
<header class="site-header">
  <div class="container nav">
    <a class="brand" href="index.html" aria-label="Terramorph home">
      <img src="assets/logo.png" alt="Terramorph logo" width="56" height="56">
      <span><strong>Terramorph</strong><small>Outdoor Transformation Co.</small></span>
    </a>
    <nav class="links" aria-label="Primary navigation">
      <a href="landscape-design.html">Design</a>
      <a href="paver-patios-hardscapes.html">Patios</a>
      <a href="drainage-solutions.html">Drainage</a>
      <a href="projects.html">Projects</a>
      <a href="about.html">About</a>
      <a href="contact.html">Quote</a>
    </nav>
    <div class="nav-actions">
      <a class="btn btn-quiet" href="tel:{TEL}">Call Now</a>
      <a class="btn btn-primary" href="contact.html">Request Quote</a>
    </div>
    <button class="mobile-menu" type="button" aria-expanded="false" aria-controls="primary-links" onclick="toggleMenu(this)">Menu</button>
  </div>
</header>
'''

FOOT = f'''
<div class="sticky-mobile" aria-label="Mobile lead actions">
  <a class="btn btn-quiet" href="tel:{TEL}">Call</a>
  <a class="btn btn-primary" href="contact.html">Get quote</a>
</div>
<footer class="footer">
  <div class="container footer-grid">
    <div>
      <a class="brand footer-brand" href="index.html"><img src="assets/logo.png" alt="Terramorph logo" width="56" height="56"><span><strong>Terramorph</strong><small>Northwest Ohio Outdoor Transformation</small></span></a>
      <p>Premium landscape design, paver patios, drainage solutions, outdoor lighting, retaining walls, and outdoor living for Perrysburg, Toledo, Wood County, and Lucas County homeowners.</p>
      <p class="fine-print">Free estimates for design, patios, drainage, lighting, walls, seasonal cleanups, lawn maintenance, and bed maintenance programs.</p>
    </div>
    <div>
      <h2>Primary services</h2>
      <a href="landscape-design.html">Landscape design</a>
      <a href="paver-patios-hardscapes.html">Paver patios</a>
      <a href="drainage-solutions.html">Drainage Solutions</a>
      <a href="outdoor-lighting.html">Outdoor lighting</a>
      <a href="lawn-maintenance.html">Lawn maintenance</a>
      <a href="seasonal-cleanups.html">Seasonal cleanups</a>
      <a href="projects.html">Project photos</a>
      <a href="about.html">About</a>
    </div>
    <div>
      <h2>Service areas</h2>
      <a href="service-areas.html">Serving Wood and Lucas County</a>
      <a href="service-areas.html">Northwest Ohio expertise</a>
      <a href="service-areas.html">Drainage and soil conditions</a>
      <a href="service-areas.html">Local service approach</a>
    </div>
    <div>
      <h2>Start</h2>
      <a href="tel:{TEL}">Call {PHONE}</a>
      <a href="contact.html">Request a quote</a>
      <p>Free estimates, clear communication, dependable scheduling, and professional follow-through for Northwest Ohio homeowners.</p>
    </div>
  </div>
</footer>
<script src="app.js"></script>
'''

REVIEW_SNIPPETS = [
    ('CJ Miller', '“Amazing service every time and prompt to all appointments.”'),
    ('Richard Hansen', '“Great work at a fair price. They did what they said they were going to do, when they said they would do it. Fast, friendly. Will definitely use them again.”'),
    ('Derrick Fawley', '“Ty and his team put hydro mulch down in my front yard and they did an excellent job. The grass is looking awesome! Thanks guys.”'),
    ('Barb Flowers', '“I am so impressed with Ty and Terramorph. I called on a Monday and they did the landscaping on Friday. It looks fantastic. A great group of hard working young men. Would recommend to everyone.”'),
    ('Larry Calcamuggio', '“Fast and reliable. Ty did excellent work and very reasonable cost. I would not hesitate to suggest him to others. Thanks Ty!”'),
    ('Karen Chiaverini', '“Wonderful experience with the young men that worked on my waterfall. They did a good job.”'),
    ('Elliott Hudson', '“The crew came and did an amazing job!”'),
]

SERVICES = [
    ('Landscape Installation and Design', 'Plan My Landscape', 'Design planning, bed layouts, plant installation, sod, mulch, rock, edging, grading awareness, and full installation.', ['Plant installation', 'Mulch and rock beds', 'Sod installation', 'Bed shaping', 'Native habitat rehabilitation'], 'assets/real-entry.webp?v=3.14', 'landscape-design.html'),
    ('Paver Patios and Walkways', 'Plan My Patio', 'Paver patios, walkways, seating areas, retaining details, steps, fire pits, outdoor kitchens, and hardscape structure.', ['Patios', 'Walkways', 'Fire pits', 'Outdoor kitchens', 'Retaining walls', 'Concrete coordination'], 'assets/real-patio.webp?v=3.14', 'paver-patios-hardscapes.html'),
    ('Drainage Solutions', 'Fix My Drainage', 'Drainage diagnosis, grading, runoff routing, wet-yard solutions, soil-aware recommendations, and practical fixes for Northwest Ohio lots.', ['Standing water', 'Soggy lawns', 'Downspout routing', 'Grading', 'Erosion control', 'Dry creek features'], 'assets/real-drainage.webp', 'drainage-solutions.html'),
    ('Outdoor Lighting', 'Light My Property', 'Low-voltage lighting for paths, patios, entries, landscape features, safety, security, and nighttime curb appeal.', ['Path lights', 'Accent lighting', 'Patio lighting', 'Entry lighting', 'Security visibility'], 'assets/real-lighting.webp?v=3.14', 'outdoor-lighting.html'),
    ('Lawn Maintenance', 'Set Up Maintenance', 'Residential and commercial mowing, edging, trimming, bed upkeep, brush control, and recurring property presentation.', ['Mowing', 'Edging', 'Trimming', 'Weeding', 'Bed maintenance', 'Commercial maintenance'], 'assets/real-lawn.webp', 'lawn-maintenance.html'),
    ('Seasonal Cleanups', 'Schedule Cleanup', 'Spring and fall cleanups, pruning, leaf removal, debris removal, bed resets, overgrowth control, and property preparation.', ['Spring cleanup', 'Fall cleanup', 'Leaf removal', 'Spring pruning', 'Tree and bush trimming', 'Debris hauling'], 'assets/real-mulch.webp', 'seasonal-cleanups.html'),
    ('Snow Removal', 'Get Winter Service', 'Dependable winter service for homes, businesses, and properties that need safe access when Northwest Ohio weather hits.', ['Driveways', 'Walkways', 'Commercial lots', 'Ice management', 'Winter response'], 'assets/snow-removal-truck.webp?v=3.17', 'contact.html'),
]
SERVICE_GROUPS = [
    ('Landscape Installation and Design', ['Landscape design', 'Plant installation', 'Mulch and rock beds', 'Sod installation', 'Bed edging', 'Native habitat rehabilitation', 'Spring pruning']),
    ('Paver Patios and Walkways', ['Paver patios', 'Paver walkways', 'Retaining walls', 'Fire pits', 'Outdoor kitchens', 'Concrete services', 'Hardscape repairs and upgrades']),
    ('Drainage Solutions', ['Drainage diagnosis', 'Grading', 'Runoff routing', 'Standing water correction', 'Dry creek features', 'Erosion control', 'Downspout and low-spot planning']),
    ('Outdoor Lighting', ['Path lighting', 'Landscape accent lighting', 'Patio and entertainment lighting', 'Entry lighting', 'Security visibility', 'Night curb appeal']),
    ('Lawn Maintenance', ['Lawn care and mowing', 'Commercial maintenance', 'Residential maintenance', 'Trimming', 'Weeding', 'Bed maintenance', 'Brush clearing']),
    ('Seasonal Cleanups', ['Spring cleanups', 'Fall cleanups', 'Leaf removal', 'Debris cleanup', 'Tree and bush trimming', 'Bed resets', 'Junk removal and hauling']),
    ('Snow Removal', ['Residential snow removal', 'Commercial snow service', 'Industrial property access', 'Walkways', 'Ice management coordination', 'Winter response planning']),
    ('Additional Property Services', ['Power washing', 'Roof cleaning', 'Exterior services', 'Demolition and site prep', 'Moving and hauling', 'Holiday lighting'])
]
PROJECT_PHOTOS = [
    ('Paver patios and outdoor living', 'assets/real-patio.webp?v=3.14'),
    ('Walkways and hardscape detail', 'assets/real-walkway.webp?v=3.14'),
    ('Drainage and grading work', 'assets/real-drainage.webp'),
    ('Landscape beds and plant installation', 'assets/real-entry.webp?v=3.14'),
    ('Outdoor lighting', 'assets/real-lighting.webp?v=3.14'),
    ('Lawn maintenance and clean edging', 'assets/real-lawn.webp'),
]

def head(title, desc, schema=''):
    schema_block = f'\n  <script type="application/ld+json">{schema}</script>' if schema else ''
    return f'''<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{title}</title>
  <meta name="description" content="{desc}">
  <meta property="og:title" content="{title}">
  <meta property="og:description" content="{desc}">
  <meta property="og:type" content="website">
  <meta property="og:image" content="assets/real-hero.webp">
  <link rel="stylesheet" href="styles.css?v=3.19">{schema_block}
</head>
<body>{NAV}<main id="main">'''

def page(title, desc, body, schema=''):
    return head(title, desc, schema) + body + '</main>' + quote_popup() + FOOT + '</body></html>'

def quote_form(title='Request a Premium Project Quote'):
    return f'''
<section class="quote-panel" id="quote" aria-labelledby="quote-title">
  <p class="eyebrow light">Start with a fast quote</p>
  <h2 id="quote-title">{title}</h2>
  <p>Tell us what you want designed, built, fixed, cleaned up, or maintained. Free estimates are available for outdoor projects and ongoing maintenance programs.</p>
  <form class="quote-form" onsubmit="handleQuote(event)">
    <div class="field"><label for="name-{title[:4].replace(' ','')}">Name</label><input id="name-{title[:4].replace(' ','')}" name="name" autocomplete="name" required placeholder="Your name"></div>
    <div class="field"><label for="phone-{title[:4].replace(' ','')}">Phone</label><input id="phone-{title[:4].replace(' ','')}" name="phone" autocomplete="tel" inputmode="tel" required placeholder="(419) 000-0000"></div>
    <div class="field"><label for="city-{title[:4].replace(' ','')}">City</label><input id="city-{title[:4].replace(' ','')}" name="city" autocomplete="address-level2" placeholder="Perrysburg, Toledo, Maumee..."></div>
    <div class="field"><label for="service-{title[:4].replace(' ','')}">Primary service</label><select id="service-{title[:4].replace(' ','')}" name="service"><option>Landscape Installation and Design</option><option>Paver Patios and Walkways</option><option>Drainage Solutions</option><option>Outdoor Lighting</option><option>Lawn Maintenance</option><option>Seasonal Cleanups</option><option>Snow Removal</option><option>Mulch and Rock Beds</option><option>Plant Installation</option><option>Spring Pruning</option><option>Tree & Bush Trimming</option><option>Retaining Walls</option><option>Concrete Services</option><option>Fire Pit and Outdoor Kitchen</option><option>Power Washing and Roof Cleaning</option><option>Junk Removal and Hauling</option><option>Demolition and Site Prep</option><option>Holiday Lighting</option></select></div>
    <div class="field"><label for="timeline-{title[:4].replace(' ','')}">Timeline</label><select id="timeline-{title[:4].replace(' ','')}" name="timeline"><option>As soon as possible</option><option>This month</option><option>1–3 months</option><option>Planning for next season</option></select></div>
    <div class="field"><label for="budget-{title[:4].replace(' ','')}">Project range</label><select id="budget-{title[:4].replace(' ','')}" name="budget"><option>Not sure yet</option><option>$5k–$10k</option><option>$10k–$25k</option><option>$25k+</option></select></div>
    <div class="field full"><label for="notes-{title[:4].replace(' ','')}">What would you like changed?</label><textarea id="notes-{title[:4].replace(' ','')}" name="notes" placeholder="Standing water, patio, lighting, curb appeal, outdoor entertaining..."></textarea></div>
    <div class="field full"><label for="photo-{title[:4].replace(' ','')}">Optional photo</label><input id="photo-{title[:4].replace(' ','')}" type="file" name="photo" accept="image/*"></div>
    <div class="full form-actions"><button class="btn btn-gold" type="submit">Request My Quote</button><a class="btn btn-outline-light" href="tel:{TEL}">Call {PHONE}</a><div class="success" role="status" aria-live="polite"></div></div>
  </form>
</section>'''

def quote_popup():
    return f'''
<div class="quote-popup" id="quote-popup" role="dialog" aria-modal="true" aria-labelledby="quote-popup-title" aria-describedby="quote-popup-desc" hidden>
  <div class="quote-popup-backdrop" data-close-popup></div>
  <section class="quote-popup-card" tabindex="-1">
    <button class="quote-popup-close" type="button" aria-label="Close free quote popup" data-close-popup>×</button>
    <div class="quote-popup-copy">
      <p class="eyebrow">Free estimate</p>
      <h2 id="quote-popup-title">Get a free quote for your property.</h2>
      <p id="quote-popup-desc">Leave your contact info, property address, and what you are looking to have done so Terramorph can follow up with the right next step.</p>
      <div class="popup-trust"><span>★★★★★ 200+ Google Reviews</span><span>Licensed And Insured</span><span>Serving Wood and Lucas County</span></div>
    </div>
    <form class="quote-form popup-form" onsubmit="handleQuote(event)">
      <div class="field"><label for="popup-name">Full name</label><input id="popup-name" name="name" autocomplete="name" required placeholder="Full name"></div>
      <div class="field"><label for="popup-phone">Phone number</label><input id="popup-phone" name="phone" autocomplete="tel" inputmode="tel" required placeholder="(419) 000-0000"></div>
      <div class="field"><label for="popup-email">Email</label><input id="popup-email" name="email" autocomplete="email" inputmode="email" type="email" required placeholder="you@example.com"></div>
      <div class="field"><label for="popup-address">Property address</label><input id="popup-address" name="address" autocomplete="street-address" required placeholder="Street address"></div>
      <div class="field full"><label for="popup-notes">What are you looking to have done?</label><textarea id="popup-notes" name="notes" required placeholder="Landscape install, patio, drainage, lighting, lawn maintenance, cleanup, snow removal..."></textarea></div>
      <div class="full form-actions"><button class="btn btn-gold" type="submit">Get My Free Quote</button><a class="btn btn-primary" href="tel:{TEL}">Call {PHONE}</a><div class="success" role="status" aria-live="polite"></div></div>
    </form>
  </section>
</div>'''

def trust_band():
    return '''
<section class="trust-band" aria-label="Terramorph credibility">
  <div class="container trust-grid">
    <div class="trust-feature"><strong>200+</strong><span>Google Reviews</span><small>Consistent 5-star feedback from homeowners across the area.</small></div>
    <div class="trust-logo"><img src="assets/google-verified.png" alt="Google Verified badge"><span>Google Verified</span></div>
    <div class="trust-logo"><img src="assets/bbb-logo.svg" alt="BBB Better Business Bureau logo"><span>BBB Member</span></div>
    <div class="trust-feature"><strong>Regional</strong><span>Serving Wood and Lucas County</span><small>Northwest Ohio-specific expertise for outdoor projects, drainage, and property upkeep.</small></div>
    <div class="trust-feature"><strong>Insured</strong><span>Licensed And Insured</span><small>Professional protection before work starts.</small></div>
  </div>
</section>'''

def service_cards():
    cards = []
    for name, cta, summary, includes, img, href in SERVICES:
        cards.append(f'''
<a class="premium-service" href="{href}" aria-label="{name}">
  <img src="{img}" alt="{name} project photo" loading="lazy">
  <div class="service-body">
    <p class="eyebrow">Primary service</p>
    <h3>{name}</h3>
    <p>{summary}</p>
    <ul class="mini-list">{''.join(f'<li>{item}</li>' for item in includes)}</ul>
    <span class="card-cta">{cta} →</span>
  </div>
</a>''')
    return '<div class="service-matrix focused-services">' + ''.join(cards) + '</div>'


def full_service_directory():
    groups=[]
    for title, items in SERVICE_GROUPS:
        groups.append('<div class="service-group"><h3>'+title+'</h3><ul>' + ''.join(f'<li>{item}</li>' for item in items) + '</ul></div>')
    return '<section class="section service-directory"><div class="container section-heading compact"><p class="eyebrow">Full-service property work</p><h2>One crew for the work around the whole property.</h2><p>Start with the problem you want solved. Terramorph can handle the main project and the related work around it, from grading and beds to cleanup, hauling, lighting, and maintenance.</p></div><div class="container service-groups">' + ''.join(groups) + '</div></section>'

def photo_gallery():
    cards=[]
    for label, img in PROJECT_PHOTOS:
        cards.append(f'<figure class="work-photo"><img src="{img}" alt="Terramorph {label}" loading="lazy"><figcaption>{label}</figcaption></figure>')
    return '<div class="work-photo-grid">' + ''.join(cards) + '</div>'

def review_markup(name, quote, compact=False):
    cls = ' class="compact-review"' if compact else ''
    return f'<blockquote{cls}><div class="stars">★★★★★</div><p>{quote}</p><cite>— {name}</cite></blockquote>'

def review_stack(limit=None):
    reviews = REVIEW_SNIPPETS if limit is None else REVIEW_SNIPPETS[:limit]
    return '<div class="review-stack">' + ''.join(review_markup(name, quote, True) for name, quote in reviews) + '</div>'

def review_section():
    return '<section class="section reviews-section"><div class="container section-heading compact"><p class="eyebrow">5-Star Google Reviews</p><h2>Real names under real customer words.</h2><p>Strong review excerpts pulled from Terramorph’s current Google review presentation, now shown with reviewer names instead of anonymous quotes.</p></div><div class="container review-grid">' + ''.join(review_markup(name, quote) for name, quote in REVIEW_SNIPPETS[:6]) + '</div></section>'

def local_authority():
    return '''
<section class="section clay-section">
  <div class="container local-grid">
    <div>
      <p class="eyebrow">Local expertise</p>
      <h2>Locally owned, operated, licensed, insured, and trained for Northwest Ohio property problems.</h2>
      <p>Terramorph does not just send a mower and guess. The team includes licensed and insured professionals with certification-backed training, field experience, and the judgment to diagnose drainage, grading, plant health, hardscape base issues, maintenance needs, and seasonal property problems before recommending work.</p>
      <a class="btn btn-primary" href="service-areas.html">See Our Local Approach</a>
    </div>
    <div class="authority-list">
      <div><b>Diagnosis first</b><span>Crews look at grade, water movement, soil, sun exposure, access, plant health, and long-term maintenance before rushing into a scope.</span></div>
      <div><b>Licensed And Insured</b><span>Professional protection and accountability for residential, commercial, and industrial properties.</span></div>
      <div><b>Certified training</b><span>Team members bring training and practical field experience for safer recommendations, cleaner installs, and better problem-solving.</span></div>
      <div><b>Local conditions</b><span>Clay soil, flat lots, freeze-thaw cycles, drainage problems, and Northwest Ohio weather are accounted for in the work.</span></div>
    </div>
  </div>
</section>'''

def problem_picker():
    items = [
        ('Curb Appeal', 'Landscape Design, Plantings, Mulch, Rock, Edging', 'landscape-design.html'),
        ('Patio Or Walkway', 'Pavers, Walkways, Seating Areas, Outdoor Living', 'paver-patios-hardscapes.html'),
        ('Drainage Problem', 'Standing Water, Grading, Runoff, Wet Yard Fixes', 'drainage-solutions.html'),
        ('Property Upkeep', 'Mowing, Cleanups, Bed Maintenance, Snow Response', 'lawn-maintenance.html'),
    ]
    return """
<section class="section project-selector">
  <div class="container project-selector-inner">
    <div class="selector-copy">
      <p class="eyebrow">Start With The Project</p>
      <h2>What Do You Need Handled?</h2>
      <p>Pick the closest fit. Terramorph can scope related work together if the job crosses categories.</p>
    </div>
    <div class="selector-options">
      {options}
    </div>
  </div>
</section>""".format(options=''.join(
        f'<a class="selector-option" href="{href}"><span>{i+1:02d}</span><b>{title}</b><small>{copy}</small><em>Start Here →</em></a>'
        for i,(title,copy,href) in enumerate(items)
    ))

def transformation_home():
    return """
<section class="section signature-work-home" aria-label="Terramorph featured outdoor work">
  <div class="container signature-work-layout">
    <div class="signature-copy">
      <p class="eyebrow">Featured work</p>
      <h2>Outdoor projects that make the property feel finished.</h2>
      <p>From patios and walkways to entry landscaping, drainage, lighting, and upkeep, the work should look intentional from the street, the backyard, and every place people actually use the property.</p>
      <div class="signature-points">
        <span>Real project photos</span>
        <span>Design, build, drainage, and upkeep</span>
        <span>Serving Wood and Lucas County</span>
      </div>
      <a class="btn btn-primary" href="projects.html">View Project Photos</a>
    </div>
    <div class="signature-gallery">
      <a class="signature-card large" href="paver-patios-hardscapes.html">
        <img src="assets/real-patio.webp?v=3.19" alt="Terramorph paver patio and backyard hardscape project" loading="lazy">
        <span><b>Paver patios and walkways</b><small>Outdoor living spaces, hardscape structure, steps, and gathering areas.</small></span>
      </a>
      <a class="signature-card" href="landscape-design.html">
        <img src="assets/real-entry.webp?v=3.19" alt="Terramorph front entry landscape design and planting project" loading="lazy">
        <span><b>Landscape install and curb appeal</b><small>Beds, plantings, mulch, rock, edging, sod, and clean property presentation.</small></span>
      </a>
      <a class="signature-card" href="drainage-solutions.html">
        <img src="assets/real-drainage.webp?v=3.19" alt="Terramorph drainage and grading project" loading="lazy">
        <span><b>Drainage and grading</b><small>Water routing, grading awareness, low spots, and wet-yard improvements.</small></span>
      </a>
      <a class="signature-card" href="outdoor-lighting.html">
        <img src="assets/real-lighting.webp?v=3.19" alt="Terramorph outdoor lighting project at night" loading="lazy">
        <span><b>Lighting and finishing details</b><small>Path lighting, accent lighting, visibility, and nighttime curb appeal.</small></span>
      </a>
    </div>
  </div>
</section>"""

def process_home():
    return """
<section class="section process-section home-process">
  <div class="container process-feature">
    <div><p class="eyebrow">Property-First Planning</p><h2>A simpler path from property problem to estimate.</h2><p>Start with the property problem, review the right service options, see real work and named customer reviews, then request a clear estimate.</p></div>
    <div class="process-timeline large"><div><b>1. Pick the property problem</b><span>Design, patio, drainage, lighting, cleanup, maintenance, or snow.</span></div><div><b>2. See the outcome</b><span>Photos, service explanations, local proof, and named customer reviews.</span></div><div><b>3. Request the estimate</b><span>Send contact info, property address, and what needs done.</span></div></div>
  </div>
</section>"""

home = f'''
<section class="hero-v2">
  <div class="hero-media" aria-hidden="true"><img src="assets/real-hero.webp" alt=""></div>
  <div class="hero-overlay"></div>
  <div class="container hero-content">
    <div class="hero-copy">
      <p class="eyebrow light">Northwest Ohio outdoor transformation</p>
      <h1>Fix the yard. Finish the property. Make it worth coming home to.</h1>
      <p class="hero-lead">Landscape design, paver patios, drainage, lighting, cleanups, maintenance, and snow service for homeowners and properties that need outdoor work handled with real follow-through.</p>
      <div class="cta-row"><a class="btn btn-gold" href="contact.html">Get A Free Estimate</a><a class="btn btn-outline-light" href="#start-here">Choose My Project</a><a class="btn btn-outline-light" href="projects.html">See Work</a><a class="btn btn-call" href="tel:{TEL}">Call {PHONE}</a></div>
      <div class="above-fold-trust">
        <span>★★★★★ 200+ Google Reviews</span><span>Named Customer Reviews</span><span>BBB Member</span><span>Licensed And Insured</span><span>Serving Wood and Lucas County with Northwest Ohio-specific expertise</span>
      </div>
    </div>
  </div>
</section>
{trust_band()}
<div id="start-here">{problem_picker()}</div>
{transformation_home()}
<section class="section services-section homepage-services">
  <div class="container section-heading">
    <p class="eyebrow">Core Services</p>
    <h2>The major outdoor problems Terramorph can solve.</h2>
    <p>Start with the project you need handled. Terramorph can scope the main work and the related details around it so the whole property feels cleaner and more complete.</p>
  </div>
  <div class="container">{service_cards()}</div>
</section>
{local_authority()}
<section class="section work-section homepage-proof">
  <div class="container section-heading compact">
    <p class="eyebrow">Proof Of Work</p>
    <h2>Real Terramorph work, shown before the quote form.</h2>
    <p>Photos come before reviews and forms so visitors see actual output before being asked to take action.</p>
  </div>
  <div class="container">{photo_gallery()}</div>
</section>
{review_section()}
{process_home()}
<section class="section quote-section">
  <div class="container quote-grid">
    {quote_form('Request My Outdoor Transformation Quote')}
    <div class="cta-proof">
      <p class="eyebrow">Named Google Review Proof</p>
      <h2>Real words from homeowners who already trusted Terramorph.</h2>
      {review_stack(5)}
      <ul class="check-list">
        <li>Free estimates for projects, cleanups, and maintenance</li>
        <li>Fast phone call option on every device</li>
        <li>Google reviews, BBB Membership, and license/insurance proof nearby</li>
        <li>Project proof and named reviews before the request form</li>
      </ul>
    </div>
  </div>
</section>
'''


def faq_section(items):
    return '<section class="section faq-section"><div class="container section-heading compact"><p class="eyebrow">Questions homeowners ask</p><h2>Quick answers before you request an estimate.</h2></div><div class="container why-grid">' + ''.join(f'<div><b>{q}</b><span>{a}</span></div>' for q,a in items) + '</div></section>'

def schema_for(page_name, title, desc, faqs=None, service=None):
    import json
    base = {
      "@context":"https://schema.org",
      "@graph":[
        {"@type":"LocalBusiness","@id":"https://www.terramorph.example/#business","name":"Terramorph","telephone":"419-637-4498","areaServed":["Wood County OH","Lucas County OH","Northwest Ohio"],"description":"Landscape design, patios, drainage, lighting, lawn maintenance, cleanups, and outdoor property work in Wood and Lucas County."},
        {"@type":"WebPage","name":title,"description":desc,"url":"https://www.terramorph.example/"+page_name},
        {"@type":"BreadcrumbList","itemListElement":[{"@type":"ListItem","position":1,"name":"Home","item":"https://www.terramorph.example/"},{"@type":"ListItem","position":2,"name":title,"item":"https://www.terramorph.example/"+page_name}]}
      ]
    }
    if service:
        base["@graph"].append({"@type":"Service","name":service,"provider":{"@id":"https://www.terramorph.example/#business"},"areaServed":["Wood County OH","Lucas County OH","Northwest Ohio"]})
    if faqs:
        base["@graph"].append({"@type":"FAQPage","mainEntity":[{"@type":"Question","name":q,"acceptedAnswer":{"@type":"Answer","text":a}} for q,a in faqs]})
    return json.dumps(base, separators=(',',':'))

DEFAULT_FAQS = [
    ('Do you offer free estimates?', 'Yes. Terramorph offers free estimates for landscape design, patios, drainage, lighting, lawn maintenance, seasonal cleanups, and related outdoor property work.'),
    ('What areas do you serve?', 'Terramorph serves Wood and Lucas County with Northwest Ohio-specific expertise for soil, drainage, weather, maintenance, and outdoor projects.'),
    ('Can you handle multiple services together?', 'Yes. Many projects connect design, drainage, hardscaping, lighting, cleanup, and maintenance, so Terramorph can scope related work together.'),
    ('What happens after I request a quote?', 'Terramorph reviews your service need, property location, timeline, and photos if provided, then follows up with the right next step for an estimate or site review.')
]

SERVICE_FAQS = {
    'Landscape Design': [('Do you handle both design and installation?', 'Yes. Terramorph can plan and install landscape beds, plantings, mulch, rock, edging, sod, and related property improvements.'), ('Can landscape work include drainage or hardscape planning?', 'Yes. Terramorph looks at the whole property so drainage, patios, beds, lighting, and maintenance fit together instead of feeling patched together.')] + DEFAULT_FAQS[:2],
    'Paver Patios and Hardscapes': [('Do you build patios and walkways?', 'Yes. Terramorph handles paver patios, walkways, seating areas, steps, fire pits, outdoor kitchens, retaining details, and hardscape upgrades.'), ('Do you think about drainage before patios?', 'Yes. Drainage, grading, base conditions, and water movement should be considered before patio or walkway work begins.')] + DEFAULT_FAQS[:2],
    'Drainage Solutions': [('Can you fix standing water in the yard?', 'Terramorph evaluates grading, runoff, downspouts, soil, and low spots to recommend practical drainage solutions for Northwest Ohio yards.'), ('Why does local soil matter?', 'Flat lots, clay soil, freeze-thaw cycles, and heavy rain affect how drainage and landscape work should be planned in Wood and Lucas County.')] + DEFAULT_FAQS[:2],
    'Outdoor Lighting': [('Do you install outdoor lighting for patios and walkways?', 'Yes. Terramorph handles low-voltage lighting for paths, patios, entries, landscape features, safety, security, and nighttime curb appeal.'), ('Can lighting be added with a larger project?', 'Yes. Lighting often works best when planned with patios, walkways, beds, drainage, or a larger outdoor transformation.')] + DEFAULT_FAQS[:2],
    'Lawn Maintenance': [('Do you offer recurring lawn maintenance?', 'Yes. Terramorph offers mowing, edging, trimming, bed upkeep, weeding, brush control, and commercial or residential maintenance programs.'), ('Can maintenance include bed cleanup?', 'Yes. Lawn maintenance can be scoped with bed maintenance, mulch, trimming, seasonal cleanup, and other property upkeep.')] + DEFAULT_FAQS[:2],
    'Seasonal Cleanups': [('Do you handle spring and fall cleanups?', 'Yes. Terramorph handles spring cleanups, fall cleanups, leaf removal, debris removal, pruning, trimming, bed resets, and hauling.'), ('Can cleanups be paired with mulch or plant work?', 'Yes. Cleanups often pair well with mulch, rock beds, edging, pruning, plant installation, and lawn maintenance.')] + DEFAULT_FAQS[:2],
}

def service_page(filename, title, eyebrow, image, headline, lead, problem, outcome, cta):
    body = f'''
<section class="page-hero premium-page-hero">
  <div class="page-hero-image"><img src="assets/{image}" alt="{title} premium outdoor transformation"></div>
  <div class="hero-overlay"></div>
  <div class="container page-hero-content">
    <p class="crumb"><a href="index.html">Home</a> / {title}</p>
    <p class="eyebrow light">{eyebrow}</p>
    <h1>{headline}</h1>
    <p>{lead}</p>
    <div class="cta-row"><a class="btn btn-gold" href="contact.html">{cta}</a><a class="btn btn-outline-light" href="tel:{TEL}">Call {PHONE}</a></div>
  </div>
</section>
{trust_band()}
<section class="section">
  <div class="container problem-grid">
    <div class="problem-card dark"><p class="eyebrow light">Homeowner problem</p><h2>{problem}</h2></div>
    <div class="problem-card light-card"><p class="eyebrow">Expected outcome</p><h2>{outcome}</h2></div>
  </div>
</section>
<section class="section clay-section">
  <div class="container local-grid">
    <div><p class="eyebrow">How we work</p><h2>Clear estimates, professional work, and clean follow-through.</h2><p>Homeowners need to know what happens next: Terramorph reviews the property, talks through the goal, explains practical options, and gives a clear estimate before work begins.</p></div>
    <div class="authority-list">
      <div><b>Discovery</b><span>City, goal, frustration, timeline, range, and photos captured quickly.</span></div>
      <div><b>Site review</b><span>Grade, water flow, access, soil, sun, materials, and maintenance expectations.</span></div>
      <div><b>Scope</b><span>Clear options that connect budget to property improvement and long-term durability.</span></div>
      <div><b>Build</b><span>Professional install, cleanup, walkthrough, and follow-up.</span></div>
    </div>
  </div>
</section>
<section class="section work-section"><div class="container section-heading compact"><p class="eyebrow">Project photos</p><h2>Real work examples without staged pairings.</h2></div><div class="container">{photo_gallery()}</div></section>
{faq_section(SERVICE_FAQS.get(title, DEFAULT_FAQS))}
<section class="section quote-section"><div class="container quote-grid">{quote_form('Request a ' + title + ' Quote')}<div class="cta-proof"><p class="eyebrow">Why homeowners reach out</p><h2>Reviews, proof, and a simple free estimate request.</h2>{review_stack(2)}</div></div></section>
'''
    desc = f'{title} in Toledo, Wood County, Lucas County, and Northwest Ohio by Terramorph. Free estimates for homeowners and property owners.'
    schema = schema_for(filename, f'{title} | Terramorph', desc, SERVICE_FAQS.get(title, DEFAULT_FAQS), title)
    (root / filename).write_text(page(f'{title} in Wood and Lucas County | Terramorph', desc, body, schema))


def meta_landing_page(filename, title, eyebrow, image, headline, lead, bullets, service, form_title):
    faqs = SERVICE_FAQS.get(service, DEFAULT_FAQS)
    body = f'''
<section class="page-hero premium-page-hero meta-landing-hero">
  <div class="page-hero-image"><img src="assets/{image}" alt="{title} project photo"></div><div class="hero-overlay"></div>
  <div class="container page-hero-content"><p class="crumb"><a href="index.html">Home</a> / {title}</p><p class="eyebrow light">{eyebrow}</p><h1>{headline}</h1><p>{lead}</p><div class="cta-row"><a class="btn btn-gold" href="#quote">Get A Free Estimate</a><a class="btn btn-outline-light" href="tel:{TEL}">Call {PHONE}</a></div></div>
</section>
{trust_band()}
<section class="section"><div class="container problem-grid"><div class="problem-card dark"><p class="eyebrow light">Good fit if</p><h2>{bullets[0]}</h2></div><div class="problem-card light-card"><p class="eyebrow">What to expect</p><h2>{bullets[1]}</h2></div></div></section>
<section class="section clay-section"><div class="container local-grid"><div><p class="eyebrow">Why request now</p><h2>{bullets[2]}</h2><p>{bullets[3]}</p></div><div class="authority-list"><div><b>Fast next step</b><span>Submit the form or call and Terramorph can review the property, service need, timeline, and photos.</span></div><div><b>Real project proof</b><span>Project photos and named reviews stay close to the quote path so the page feels credible, not generic.</span></div><div><b>Local conditions</b><span>Wood and Lucas County soil, drainage, freeze-thaw, and weather are considered before recommending work.</span></div><div><b>Clear estimate</b><span>The goal is a practical scope, clean communication, and a path to getting the work handled.</span></div></div></div></section>
<section class="section work-section"><div class="container section-heading compact"><p class="eyebrow">Project photos</p><h2>See the kind of work this estimate can start.</h2></div><div class="container">{photo_gallery()}</div></section>
{review_section()}
{faq_section(faqs)}
<section class="section quote-section"><div class="container quote-grid">{quote_form(form_title)}<div class="cta-proof"><p class="eyebrow">Built for Facebook and mobile leads</p><h2>Simple page, real photos, reviews, call button, and free estimate form.</h2>{review_stack(3)}</div></div></section>
'''
    desc = f'{title} from Terramorph for Wood and Lucas County homeowners. Real photos, reviews, phone call, and free estimate request.'
    schema = schema_for(filename, title, desc, faqs, service)
    (root/filename).write_text(page(title + ' | Terramorph', desc, body, schema))

service_page('landscape-design.html', 'Landscape Design', 'Landscape design for Northwest Ohio homes', 'real-entry.webp?v=3.14', 'A landscape plan that makes the whole property feel finished.', 'Design-first landscaping for homeowners who want curb appeal, better outdoor living, and a property that feels intentionally built, not patched together.', 'The yard looks unfinished, builder-grade, or disconnected from how the family actually wants to live outside.', 'A cohesive design with better curb appeal, outdoor flow, plantings, hardscape structure, and pride of ownership.', 'Design My Property')
service_page('paver-patios-hardscapes.html', 'Paver Patios and Hardscapes', 'Premium patios and outdoor living', 'real-patio.webp?v=3.14', 'Build the backyard space people actually want to use.', 'Paver patios, walkways, hardscape structure, and outdoor living environments designed around entertaining, durability, and property value.', 'There is no comfortable place to grill, host, relax, or enjoy the backyard, especially after rain.', 'A durable patio or outdoor room that expands living space and makes the property feel more valuable.', 'Plan My Patio')
service_page('drainage-solutions.html', 'Drainage Solutions', 'Drainage expertise for clay soil and flat lots', 'real-drainage.webp', 'Stop fighting standing water and start using your yard again.', 'Practical drainage solutions for wet yards, pooling water, soggy lawns, and water moving toward patios or foundations in Northwest Ohio conditions.', 'Flat lots, clay soil, poor grading, or runoff make the yard frustrating and sometimes unusable.', 'A drier, more functional landscape with water routed intentionally and finished beautifully.', 'Fix My Drainage')
service_page('outdoor-lighting.html', 'Outdoor Lighting', 'Outdoor lighting for paths, patios, and entries', 'real-lighting.webp?v=3.14', 'Make the property safer, warmer, and better looking at night.', 'Low-voltage outdoor lighting for walkways, patios, entries, landscape beds, feature areas, safety, security, and nighttime curb appeal.', 'The property disappears after dark, paths feel unsafe, and the finished landscape or patio loses impact at night.', 'A cleaner nighttime look with better visibility, safer movement, and outdoor spaces that feel usable after sunset.', 'Light My Property')
service_page('lawn-maintenance.html', 'Lawn Maintenance', 'Recurring lawn and property upkeep', 'real-lawn.webp', 'Keep the property clean, edged, and professionally maintained.', 'Residential and commercial mowing, edging, trimming, weeding, bed upkeep, brush control, and recurring property presentation for Wood and Lucas County properties.', 'The property starts looking overgrown, uneven, or neglected because mowing, edging, beds, weeds, and trimming are not handled consistently.', 'A cleaner, better-maintained property with dependable upkeep and less weekend work for the owner.', 'Set Up Maintenance')
service_page('seasonal-cleanups.html', 'Seasonal Cleanups', 'Spring and fall cleanup service', 'real-mulch.webp', 'Reset the property before or after the season hits.', 'Spring and fall cleanups, leaf removal, pruning, trimming, debris removal, bed resets, mulch preparation, and hauling for Northwest Ohio properties.', 'Leaves, branches, overgrowth, dead material, and messy beds make the property look neglected and harder to maintain.', 'A cleaner property reset with debris removed, beds cleaned up, and the outdoor space ready for the next season.', 'Schedule Cleanup')

meta_landing_page('lp-patios.html', 'Paver Patio Estimate', 'Patio and outdoor living estimate', 'real-patio.webp?v=3.14', 'Turn the backyard into a patio, walkway, or outdoor living space people actually use.', 'Request a free estimate for paver patios, walkways, seating areas, fire pits, outdoor kitchens, and hardscape upgrades in Wood and Lucas County.', ['You want a better place to grill, host, relax, or connect the backyard to the home.', 'Terramorph reviews layout, base conditions, drainage, materials, access, and the finished look before scoping the project.', 'A better patio starts with a better plan.', 'Use this landing page when the goal is outdoor living, better backyard function, or a hardscape upgrade.'], 'Paver Patios and Hardscapes', 'Request My Patio Estimate')
meta_landing_page('lp-drainage.html', 'Drainage Solution Estimate', 'Wet yard and standing water estimate', 'real-drainage.webp', 'Stop fighting standing water after every rain.', 'Request a free estimate for drainage diagnosis, grading, runoff routing, soggy lawn fixes, downspout planning, and wet-yard solutions in Northwest Ohio.', ['Standing water, soggy grass, runoff, or drainage near patios and foundations is making the property frustrating.', 'Terramorph reviews grade, water movement, soil, low spots, downspouts, and practical ways to route water intentionally.', 'Drainage work needs local judgment.', 'Flat lots, clay soil, heavy rain, and freeze-thaw cycles make Northwest Ohio drainage different from a generic landscape job.'], 'Drainage Solutions', 'Request My Drainage Estimate')
meta_landing_page('lp-landscape-design.html', 'Landscape Design And Installation Estimate', 'Landscape design and install estimate', 'real-entry.webp?v=3.14', 'Make the front yard, beds, and outdoor space feel planned instead of patched together.', 'Request a free estimate for landscape design, plant installation, mulch, rock, edging, sod, bed shaping, and full-property outdoor improvements.', ['The property looks builder-grade, tired, disconnected, or hard to maintain.', 'Terramorph reviews curb appeal, beds, plantings, grading, access, drainage, maintenance, and how the whole property should feel finished.', 'Design and installation should work together.', 'The right plan connects plants, beds, edges, mulch, lighting, patios, drainage, and upkeep instead of treating them as separate guesses.'], 'Landscape Design', 'Request My Landscape Estimate')


projects = f'''
<section class="page-hero premium-page-hero">
  <div class="page-hero-image"><img src="assets/real-hardscape.webp?v=3.14" alt="Terramorph paver and hardscape project"></div><div class="hero-overlay"></div>
  <div class="container page-hero-content"><p class="crumb"><a href="index.html">Home</a> / Projects</p><p class="eyebrow light">Project photos</p><h1>Real Terramorph work across landscaping, patios, drainage, lighting, and maintenance.</h1><p>A simple photo hub for Terramorph work: no forced pairings, no confusing labels, just clean project photography and clear service direction.</p><div class="cta-row"><a class="btn btn-gold" href="contact.html">Start My Project</a><a class="btn btn-outline-light" href="tel:{TEL}">Call {PHONE}</a></div></div>
</section>
{trust_band()}
<section class="section work-section"><div class="container">{photo_gallery()}</div></section>
{full_service_directory()}
<section class="section transformation-section proof-gallery-section"><div class="container quote-grid">{quote_form('Ask About Similar Work')}<div class="cta-proof"><p class="eyebrow light">Want your property cleaned up or built out?</p><h2>Send a few details and get a free estimate.</h2><p>Tell Terramorph what service you need, what is frustrating you now, and what you want the property to look like when the work is finished.</p></div></div></section>
'''

projects_desc = 'Terramorph project photos for patios, walkways, drainage, landscape beds, lighting, and property work in Wood and Lucas County.'
(root/'projects.html').write_text(page('Project Photos in Wood and Lucas County | Terramorph', projects_desc, projects, schema_for('projects.html', 'Project Photos | Terramorph', projects_desc)))

about = f"""
<section class="page-hero premium-page-hero about-hero">
  <div class="page-hero-image"><img src="assets/real-entry.webp?v=3.14" alt="Terramorph finished landscape entry project"></div><div class="hero-overlay"></div>
  <div class="container page-hero-content"><p class="crumb"><a href="index.html">Home</a> / About</p><p class="eyebrow light">About Terramorph</p><h1>Outdoor work should feel planned, professional, and finished — not patched together.</h1><p>Terramorph is built for homeowners, businesses, and property owners who want one local crew that can diagnose the property, explain the options, and handle the work with clean follow-through.</p><div class="cta-row"><a class="btn btn-gold" href="contact.html">Get a Free Estimate</a><a class="btn btn-outline-light" href="projects.html">See Real Work</a><a class="btn btn-outline-light" href="tel:{TEL}">Call {PHONE}</a></div></div>
</section>
{trust_band()}
<section class="section about-intro-section">
  <div class="container about-split">
    <div>
      <p class="eyebrow">The difference</p>
      <h2>Terramorph looks at the whole property before recommending the work.</h2>
      <p>Most outdoor problems are connected. A patio fails when the base or drainage is wrong. Beds look messy when edging, grading, plant selection, and maintenance are disconnected. Lawns suffer when water, shade, soil, and upkeep are not considered together.</p>
      <p>That is why Terramorph’s approach starts with the property, not just a single service line. The goal is to make the outside of the home cleaner, more usable, easier to maintain, and better built for Northwest Ohio conditions.</p>
    </div>
    <aside class="about-proof-card">
      <span>Built for Northwest Ohio</span>
      <strong>Design • patios • drainage • lighting • maintenance • cleanup • snow</strong>
      <p>One practical team for the work around the whole property.</p>
    </aside>
  </div>
</section>
<section class="section clay-section">
  <div class="container section-heading compact"><p class="eyebrow">What you get</p><h2>Professional outdoor work with less guesswork.</h2><p>The page is not trying to overcomplicate it. Terramorph wins when the customer feels clear about the problem, the scope, the schedule, and the finished result.</p></div>
  <div class="container why-grid">
    <div><b>Diagnosis before selling</b><span>Grade, water movement, soil, access, plant health, use case, and maintenance needs are considered before rushing into a quote.</span></div>
    <div><b>Local property knowledge</b><span>Clay soil, flat lots, freeze-thaw cycles, heavy rain, and Northwest Ohio seasons shape the recommendation.</span></div>
    <div><b>Full-property thinking</b><span>Patios, drainage, beds, lighting, cleanup, maintenance, and snow all connect to how the property actually works.</span></div>
    <div><b>Clear communication</b><span>Free estimates, simple next steps, phone-first contact, and expectations that are easier for homeowners to understand.</span></div>
    <div><b>Clean job sites</b><span>Professional presentation matters: the goal is work that looks finished, cleaned up, and ready to use.</span></div>
    <div><b>Proof nearby</b><span>Real photos, 200+ Google reviews, BBB Membership, and licensed/insured credibility stay visible near the decision points.</span></div>
  </div>
</section>
<section class="section process-section">
  <div class="container process-feature">
    <div>
      <p class="eyebrow">Simple process</p>
      <h2>From messy yard problem to clear next step.</h2>
      <p>Whether someone needs a patio, drainage fix, lighting, bed refresh, cleanup, maintenance, or snow service, the flow should be easy: reach out, review the property, get a clear scope, then get the work done.</p>
    </div>
    <div class="process-timeline large">
      <div><b>1. Tell us what is wrong</b><span>Send the address, service need, photos if available, and what outcome you want.</span></div>
      <div><b>2. Walk the property</b><span>Review drainage, grade, materials, access, timeline, and service fit.</span></div>
      <div><b>3. Scope the solution</b><span>Get practical recommendations tied to budget, durability, and maintenance.</span></div>
      <div><b>4. Build it clean</b><span>Professional work, cleanup, walkthrough, and follow-through.</span></div>
    </div>
  </div>
</section>
<section class="section work-section"><div class="container section-heading compact"><p class="eyebrow">Proof Of Work</p><h2>Real Terramorph project photos.</h2><p>Instead of vague promises, the site should keep showing finished outdoor work and give people a clear path to request the same kind of result.</p></div><div class="container">{photo_gallery()}</div></section>
<section class="section quote-section"><div class="container quote-grid">{quote_form('Talk With Terramorph')}<div class="cta-proof"><p class="eyebrow">Best fit</p><h2>For property owners who want it handled right.</h2><ul class="check-list"><li>Homeowners who want better curb appeal or a more usable backyard</li><li>Properties with standing water, grading, or drainage problems</li><li>Businesses that need dependable landscape maintenance or snow response</li><li>Owners who want one crew to handle related outdoor work together</li></ul>{review_stack(3)}</div></div></section>
"""
about_desc = 'About Terramorph: landscape design, patios, drainage, lighting, maintenance, cleanups, and outdoor property work in Wood and Lucas County.'
(root/'about.html').write_text(page('About Terramorph | Wood and Lucas County Outdoor Work', about_desc, about, schema_for('about.html', 'About Terramorph', about_desc)))

areas = f'''
<section class="page-hero premium-page-hero">
  <div class="page-hero-image"><img src="assets/real-lawn-pool.webp" alt="Northwest Ohio lawn and landscape maintenance"></div><div class="hero-overlay"></div>
  <div class="container page-hero-content"><p class="crumb"><a href="index.html">Home</a> / Local Expertise</p><p class="eyebrow light">Northwest Ohio authority</p><h1>Licensed And Insured local expertise for Perrysburg, Toledo, Wood County, and Lucas County.</h1><p>Terramorph serves residential, commercial, and industrial properties with trained team members who understand drainage diagnosis, hardscape durability, plant health, snow response, and Northwest Ohio soil and weather conditions.</p><div class="cta-row"><a class="btn btn-gold" href="contact.html">Check My Property</a><a class="btn btn-outline-light" href="tel:{TEL}">Call {PHONE}</a></div></div>
</section>
{trust_band()}
{local_authority()}
<section class="section"><div class="container section-heading compact"><p class="eyebrow">Priority service areas</p><h2>Focused on Northwest Ohio.</h2></div><div class="container areas">{''.join(f'<a class="area" href="contact.html">{x}<span>Design • patios • drainage • lighting</span></a>' for x in ['Perrysburg','Toledo','Maumee','Sylvania','Rossford','Oregon','Waterville','Whitehouse','Monclova','Ottawa Hills','Bowling Green','Wood County','Lucas County','Northwest Ohio'])}</div></section>
<section class="section quote-section"><div class="container quote-grid">{quote_form('Get a Local Property Estimate')}<div class="cta-proof"><p class="eyebrow">Local estimates</p><h2>Tell us where you are and what you need done.</h2><p>Whether it is drainage, design, a patio, cleanup, mowing, mulch, trimming, or bed maintenance, Terramorph can point you toward the right next step.</p></div></div></section>
'''
areas_desc = 'Terramorph serves Wood and Lucas County with Northwest Ohio-specific expertise for landscaping, patios, drainage, lighting, cleanups, lawn maintenance, and property work.'
(root/'service-areas.html').write_text(page('Serving Wood and Lucas County | Terramorph Local Expertise', areas_desc, areas, schema_for('service-areas.html', 'Serving Wood and Lucas County', areas_desc)))

contact = f'''
<section class="page-hero premium-page-hero contact-hero">
  <div class="page-hero-image"><img src="assets/real-hero.webp" alt="Terramorph outdoor project for quote request"></div><div class="hero-overlay"></div>
  <div class="container page-hero-content"><p class="crumb"><a href="index.html">Home</a> / Quote</p><p class="eyebrow light">Fast project quote</p><h1>Tell Terramorph what you want built, fixed, or transformed.</h1><p>Use the form for lawn care, landscape maintenance, seasonal cleanup, pruning, mulch, plant installation, patios, retaining walls, drainage, lighting, concrete, power washing, hauling, snow removal, or other property work.</p><div class="cta-row"><a class="btn btn-gold" href="#quote">Start Quote</a><a class="btn btn-outline-light" href="tel:{TEL}">Call {PHONE}</a></div></div>
</section>
<section class="section quote-section"><div class="container quote-grid">{quote_form('Request My Terramorph Quote')}<div class="cta-proof"><p class="eyebrow">What happens next</p><h2>Simple free estimates for projects and maintenance.</h2><div class="process-timeline"><div><b>1. Request</b><span>Submit the short form or call directly.</span></div><div><b>2. Review</b><span>Terramorph reviews service, city, photos, and timeline.</span></div><div><b>3. Estimate</b><span>Book the site visit and prepare a clear scope.</span></div></div>{review_stack()}</div></div></section>
{trust_band()}
'''
contact_desc = 'Request a free estimate from Terramorph for landscape design, patios, drainage, outdoor lighting, lawn maintenance, seasonal cleanups, and property work.'
(root/'contact.html').write_text(page('Request a Free Outdoor Project Estimate | Terramorph', contact_desc, contact, schema_for('contact.html', 'Request a Free Estimate', contact_desc)))

review_notes = '''<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1"><title>V2.6 Review Notes | Terramorph</title><link rel="stylesheet" href="styles.css?v=3.19"></head><body><main class="section"><div class="container review-doc"><p class="eyebrow">V2.6 copy and polish summary</p><h1>Terramorph V2.6 copy, grammar, and punctuation pass</h1><h2>What changed</h2><ul><li>Expanded services to reflect the current Terramorph service mix: lawn care, mowing, landscape maintenance, seasonal cleanups, native habitat rehabilitation, fire pits, outdoor kitchens, concrete, drainage, lighting, plant installation, mulch, pruning, trimming, hauling, power washing, snow removal, holiday lighting, demolition, and site prep.</li><li>Replaced weak comparison imagery with stronger real Terramorph photos found on the Desktop.</li><li>Changed the middle-page typography from compressed decorative display styling to cleaner Inter/Manrope typography with better spacing and readability.</li><li>Reduced the heavy boxed/card feeling so service sections scan cleaner and feel more professional.</li><li>Kept trust, phone calls, free estimates, reviews, Google, BBB, licensed/insured, and local Northwest Ohio proof visible.</li></ul><p><a class="btn btn-primary" href="index.html">Open V2.6 Homepage</a></p></div></main></body></html>'''
(root/'review-notes.html').write_text(review_notes)

readme = '''# Terramorph V2.6 Website Mockup

Professional cleanup pass for Terramorph with cleaner typography, real Terramorph project photos, expanded services, corrected grammar and punctuation, consistent capitalization, and simpler homeowner-facing copy.

## Open
- `index.html` — homepage
- `landscape-design.html` — landscape design landing page
- `paver-patios-hardscapes.html` — patio/hardscape landing page
- `drainage-solutions.html` — drainage landing page
- `projects.html` — project proof hub
- `about.html` — About page
- `service-areas.html` — local authority / SEO page
- `contact.html` — free estimate form
- `review-notes.html` — summary of changes

## V2.6 priorities implemented
- Broader service coverage
- Real Terramorph images from Desktop files
- Cleaner mid-page typography
- Less compressed heading treatment
- Fewer heavy boxed/card sections
- Reviews, trust, Google reviews, BBB Membership, license/insurance, phone, and free estimate CTAs
- Sitewide grammar, punctuation, capitalization, and copy polish
- Accessibility improvements
- Added an About page explaining the local, diagnosis-first approach
'''
(root/'README.md').write_text(readme)
home_desc = 'Terramorph provides landscape design, paver patios, drainage, outdoor lighting, seasonal cleanups, lawn maintenance, and property work in Wood and Lucas County.'
(root/'index.html').write_text(page('Landscape Design, Patios, Drainage & Outdoor Work | Terramorph', home_desc, home, schema_for('index.html', 'Terramorph', home_desc, DEFAULT_FAQS)))
print('wrote V2 pages')

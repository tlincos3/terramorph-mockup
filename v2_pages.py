"""Phase 2 (2026-10): new header/footer on every page; new homepage and quote page.

Runs at the very end of build_pages.py, AFTER the legacy SEO passes, so the
legacy injectors never touch the v2 pages. Tracking tags come from head() in
build_pages.py untouched.
"""
import re, html as _html
import svc_v2

TOWNS = [  # name, lat, lon, page
    ('Perrysburg', 41.557, -83.627, 'landscaping-perrysburg-ohio.html'),
    ('Toledo', 41.654, -83.537, 'landscaping-toledo-ohio.html'),
    ('Maumee', 41.563, -83.654, 'landscaping-maumee-ohio.html'),
    ('Sylvania', 41.719, -83.713, 'landscaping-sylvania-ohio.html'),
    ('Bowling Green', 41.375, -83.651, 'landscaping-bowling-green-ohio.html'),
    ('Rossford', 41.610, -83.564, 'landscaping-rossford-ohio.html'),
    ('Oregon', 41.644, -83.487, 'landscaping-oregon-ohio.html'),
    ('Waterville', 41.501, -83.718, 'landscaping-waterville-ohio.html'),
    ('Whitehouse', 41.519, -83.804, 'landscaping-whitehouse-ohio.html'),
    ('Holland', 41.622, -83.712, 'landscaping-holland-ohio.html'),
    ('Ottawa Hills', 41.664, -83.643, 'service-areas.html'),
    ('Monclova', 41.566, -83.738, 'service-areas.html'),
]

def nav(c, home=False):
    q = '#request-form' if home else 'quote.html'
    return f'''<a class="skip-link" href="#main">Skip to content</a>
<header class="tm-header" data-tm-header>
  <div class="tm-header-inner">
    <a class="tm-brand" href="index.html" aria-label="Terramorph home"><img src="assets/tm-mark.png" alt="" width="40" height="40"><b>Terramorph</b></a>
    <nav class="tm-nav" id="tm-nav" aria-label="Primary navigation">
      <a href="landscape-design.html">Design</a>
      <a href="paver-patios-hardscapes.html">Patios</a>
      <a href="drainage-solutions.html">Drainage</a>
      <a href="seasonal-cleanups.html">Cleanups</a>
      <a href="snow-removal.html">Snow</a>
      <a href="projects.html">Projects</a>
      <a href="service-areas.html">Areas</a>
      <a href="about.html">About</a>
    </nav>
    <div class="tm-head-actions">
      <a class="tm-phone" href="tel:{c['TEL']}">{c['PHONE']}</a>
      <a class="tm-btn tm-btn-gold tm-btn-sm" href="{q}">Free quote</a>
      <button class="tm-menu-btn" type="button" aria-expanded="false" aria-controls="tm-nav" aria-label="Menu" data-tm-menu><span></span></button>
    </div>
  </div>
</header>
'''

def foot(c, home=False):
    q = '#request-form' if home else 'quote.html'
    return f'''
<div class="tm-bar" data-tm-bar aria-label="Call or get a quote">
  <a class="tm-btn tm-btn-line" href="tel:{c['TEL']}">Call</a>
  <a class="tm-btn tm-btn-gold" href="{q}">Free quote</a>
</div>
<footer class="tm-footer">
  <div class="tm-footer-inner">
    <div>
      <a class="tm-brand" href="index.html"><img src="assets/tm-mark.png" alt="" width="40" height="40"><b>Terramorph</b></a>
      <p>Landscape design, paver patios, drainage, and year-round property care for homeowners and businesses in Wood and Lucas County, Ohio.</p>
      <p>Terramorph LLC &middot; {c['BUSINESS_STREET']}, Perrysburg, OH 43551<br><a href="tel:{c['TEL']}" style="display:inline">{c['PHONE']}</a></p>
    </div>
    <div>
      <h2>Services</h2>
      <a href="landscape-design.html">Landscape design</a>
      <a href="paver-patios-hardscapes.html">Paver patios &amp; walls</a>
      <a href="drainage-solutions.html">Drainage solutions</a>
      <a href="outdoor-lighting.html">Outdoor lighting</a>
      <a href="lawn-maintenance.html">Lawn maintenance</a>
      <a href="seasonal-cleanups.html">Seasonal cleanups</a>
      <a href="snow-removal.html">Snow removal</a>
      <a href="snow-removal-signup.html">Snow removal sign-up</a>
    </div>
    <div>
      <h2>Learn</h2>
      <a href="projects.html">Project photos</a>
      <a href="guides.html">Guides</a>
      <a href="process.html">How we work</a>
      <a href="faq.html">FAQ</a>
      <a href="service-areas.html">Service areas</a>
      <a href="about.html">About</a>
    </div>
    <div>
      <h2>Contact</h2>
      <a href="{q}">Get a free quote</a>
      <a href="tel:{c['TEL']}">Call {c['PHONE']}</a>
      <a href="{c['GOOGLE_PROFILE_URL']}" target="_blank" rel="noopener">Google reviews</a>
      <a href="{c['BBB_PROFILE_URL']}" target="_blank" rel="noopener">BBB profile</a>
      <a href="{c['FACEBOOK_URL']}" target="_blank" rel="noopener">Facebook</a>
      <a href="{c['INSTAGRAM_URL']}" target="_blank" rel="noopener">Instagram</a>
    </div>
  </div>
  <div class="tm-footer-base">
    <span class="tm-promise">Every photo on this site is a real Terramorph project.</span>
    <span>&copy; Terramorph LLC &middot; <a href="privacy.html">Privacy</a> &middot; <a href="terms.html">Terms</a></span>
  </div>
</footer>
'''

def _project(lat, lon):
    x = (lon + 83.86) / 0.42 * 620 + 10
    y = (41.77 - lat) / 0.43 * 480 + 20
    return round(x), round(y)

def service_map(c):
    """Real, tappable map. app.js loads Leaflet + map tiles only when the section nears view."""
    import json
    towns = [{'n': n, 'la': la, 'lo': lo, 'p': p} for n, la, lo, p in TOWNS]
    hq = {'la': c['BUSINESS_GEO'][0], 'lo': c['BUSINESS_GEO'][1]}
    data = _html.escape(json.dumps({'towns': towns, 'hq': hq}), quote=True)
    return (f'<div class="tm-leaflet" data-leaflet="{data}" role="region" aria-label="Map of towns Terramorph serves in Wood and Lucas County, Ohio">'
            '<div class="tm-map-loading"><span></span>Loading map</div></div>')

def topo_svg(seed=3, w=1200, h=700, rings=9):
    """Slow-drifting contour lines, like a site plan. Pure SVG, decorative."""
    import math, random
    rnd = random.Random(seed)
    paths = []
    for cx, cy, base in [(w * .78, h * .3, 60), (w * .18, h * .82, 50)]:
        for k in range(rings):
            r = base + k * 46
            pts = []
            phase = rnd.random() * 6.28
            for a in range(0, 360, 12):
                t = math.radians(a)
                rr = r * (1 + .16 * math.sin(3 * t + phase) + .07 * math.sin(5 * t + phase * 1.7))
                pts.append(f'{cx + rr * math.cos(t):.0f},{cy + rr * .72 * math.sin(t):.0f}')
            paths.append(f'<polygon points="{" ".join(pts)}"/>')
    return (f'<svg class="tm-topo" viewBox="0 0 {w} {h}" preserveAspectRatio="xMidYMid slice" aria-hidden="true" focusable="false">'
            f'<g fill="none" stroke="currentColor" stroke-width="1.1">{"".join(paths)}</g></svg>')


def ba_card(before, after, label):
    """Before/after card that wipes from the before shot to the after shot.
    Real photo pairs only - never crops from ad graphics."""
    return (f'<figure class="tm-flip" data-flip aria-label="Before and after: {label}">'
            f'<div class="tm-flip-media"><img class="tm-flip-after" src="assets/{after}.webp" alt="After: {label}" loading="lazy">'
            f'<img class="tm-flip-before" src="assets/{before}.webp" alt="Before: {label}" loading="lazy"></div>'
            '<div class="tm-flip-toggle" role="group" aria-label="Show before or after">'
            '<button type="button" data-show="before">Before</button><button type="button" data-show="after" aria-pressed="true">After</button></div>'
            '</figure>')

PICKER = [
    ('drainage', 'Water sits after it rains', 'drainage-solutions.html', 'real-drainage.webp', 'Drainage solutions',
     'Standing water usually comes down to grading, downspouts, or clay soil that won&rsquo;t drain. We find where the water starts first, then route it away from the house and the lawn.'),
    ('patio', 'I want a patio or outdoor space', 'paver-patios-hardscapes.html', 'real-brick-patio-timber-edge.webp', 'Paver patios &amp; walkways',
     'We size the space around how you&rsquo;ll actually use it, then build the base right so it stays flat through Ohio freeze-thaw winters.'),
    ('beds', 'My beds look tired or bare', 'landscape-design.html', 'real-entry-columns-bed.webp', 'Landscape design &amp; beds',
     'Clean edging, fresh mulch or rock, and plants picked for clay soil and your sun. You see the plan before anything goes in the ground.'),
    ('lawn', 'The lawn needs regular care', 'lawn-maintenance.html', 'real-navy-home-stripes.webp', 'Lawn maintenance',
     'Mowing, edging, trimming, and bed upkeep on a set schedule, so the yard stays sharp without eating up your weekends.'),
    ('leaves', 'Leaves and fall mess', 'seasonal-cleanups.html', 'real-fall-leaf-crew.webp', 'Fall &amp; spring cleanups',
     'Leaves cleared and hauled away, beds cut back the right way, and the whole property left clean before winter.'),
    ('dark', 'The yard is dark at night', 'outdoor-lighting.html', 'real-lighting-night.webp', 'Outdoor lighting',
     'Low-voltage lights for paths, entries, and patios, so the property is safer and looks finished after dark.'),
    ('snow', 'Snow and ice', 'snow-removal.html', 'snow-removal-truck.webp', 'Snow removal',
     'Plowing, walks, and salting for homes and businesses, lined up before the first storm hits.'),
]

def yard_picker():
    btns = ''.join(f'<button type="button" class="tm-pick-opt" data-pick="{k}" aria-pressed="{"true" if i == 0 else "false"}"><span>{q}</span></button>' for i, (k, q, *_rest) in enumerate(PICKER))
    panes = ''.join(f'''<div class="tm-pick-pane{" is-on" if i == 0 else ""}" data-pane="{k}"{"" if i == 0 else " hidden"}>
      <div class="tm-pick-img"><img src="assets/{img}" alt="" loading="lazy"></div>
      <div class="tm-pick-copy"><p class="tm-label">What we&rsquo;d do</p><h3>{title}</h3><p>{body}</p>
        <div class="tm-cta-row"><a class="tm-btn tm-btn-gold tm-btn-sm" href="#request-form" data-pick-cta="{k}">Get a free quote</a><a class="tm-btn tm-btn-line tm-btn-sm" href="{href}">See how we do it</a></div></div>
    </div>''' for i, (k, q, href, img, title, body) in enumerate(PICKER))
    return f'''<section class="tm-sec tm-picker" id="yard-picker">
  <div class="tm-wrap">
    <div class="tm-head-row tm-reveal"><div><p class="tm-label">Start here</p><h2 class="tm-h2">What&rsquo;s going on with <span class="tm-foil">your yard?</span></h2></div><p class="tm-lead">Tap the one that sounds like you. We&rsquo;ll show you how we&rsquo;d handle it.</p></div>
    <div class="tm-pick" data-picker>
      <div class="tm-pick-opts" role="group" aria-label="Pick your yard problem">{btns}</div>
      <div class="tm-pick-stage" aria-live="polite">{panes}</div>
    </div>
  </div>
</section>'''

def faq_html(faqs):
    return ''.join(f'<details><summary>{q}</summary><p>{a}</p></details>' for q, a in faqs)

def form_panel(c, title, service, embed_id_suffix=''):
    return f'''<section class="quote-panel jobber-quote-panel quote-request-section tm-form-card" id="request-form" aria-label="Free quote request form" data-service="{service}">
  <h2 class="tm-visually-hidden" style="position:absolute;width:1px;height:1px;overflow:hidden;clip:rect(0 0 0 0)">{title}</h2>
  <div class="jobber-embed-wrap" aria-label="Terramorph Jobber quote request form">
    <div id="{c['JOBBER_CLIENTHUB_ID']}" data-jobber-lazy data-clienthub-id="{c['JOBBER_CLIENTHUB_ID']}" data-form-url="{c['JOBBER_FORM_URL']}">
      <button type="button" class="jobber-load-card" data-jobber-load><b>Tell us about your project</b><span>Takes about 2 minutes. Tap to open the secure request form.</span></button>
    </div>
    <noscript><a class="btn btn-gold" href="{c['JOBBER_DIRECT_URL']}" rel="noopener">Open the secure request form</a></noscript>
  </div>
  <div class="jobber-fallback">
    <p>Form not loading? Open it directly or call us.</p>
    <a class="btn btn-gold" href="{c['JOBBER_DIRECT_URL']}" target="_blank" rel="noopener">Open the request form</a>
    <a class="btn btn-outline-light" href="tel:{c['TEL']}">Call {c['PHONE']}</a>
  </div>
</section>'''

def _swap_head(html_text, home):
    css = '<link rel="stylesheet" href="tm.css?v={v}">'
    html_text = re.sub(r'<link rel="stylesheet" href="styles\.css\?v=[^"]+">',
                       '<link rel="preload" href="assets/tm-fraunces.woff2" as="font" type="font/woff2" crossorigin>\n  ' + css, html_text, count=1)
    return html_text

def marquee_html(c):
    REV = dict(c['REVIEW_SNIPPETS'])
    marquee_names = ['Richard Hansen', 'jon mercurio', 'Adam Raider', 'Teresa Thompson', 'Alejandro Urrea', 'Pete Detgen', 'Josh Johnson', 'Dominic Urquiola', 'Larry Calcamuggio', 'CJ Miller']
    def short(q):
        q = q.strip('“”')
        return q if len(q) < 120 else q[:q.rfind('.', 0, 118) + 1]
    items = ''.join(f'<span class="tm-marquee-item"><q>{short(REV[n])}</q><cite>{n}</cite></span>' for n in marquee_names if n in REV)
    return f'<div class="tm-marquee" aria-label="What customers say"><div class="tm-marquee-track">{items}{items.replace('class="tm-marquee-item"', 'class="tm-marquee-item" aria-hidden="true"')}</div></div>'

def render_home(c):
    REV = dict(c['REVIEW_SNIPPETS'])
    featured = ''.join(f'<article class="tm-review tm-reveal"><div class="tm-stars" aria-label="5 stars">★★★★★</div><blockquote>{REV[n]}</blockquote><cite>{n}</cite></article>' for n in ['Kate Vallerand', 'Jack Higgins', 'R.J. Rajner'] if n in REV)
    tiles = [
        ('paver-patios-hardscapes.html', 'real-brick-patio-timber-edge.webp', 'Patios &amp; hardscape', 'Paver patios, walkways, walls, and fire pit areas built on a base that survives Ohio winters.'),
        ('drainage-solutions.html', 'real-drainage.webp', 'Drainage', 'For yards that stay soggy for a day or more after rain, or water heading toward the house.'),
        ('landscape-design.html', 'real-entry-columns-bed.webp', 'Landscape design', 'A layout you can picture before anything is planted, then installed by the same crew.'),
        ('outdoor-lighting.html', 'real-lighting-night.webp', 'Outdoor lighting', 'Paths, patios, and entries lit for safety and curb appeal after dark.'),
        ('lawn-maintenance.html', 'real-navy-home-stripes.webp', 'Lawn care &amp; maintenance', 'Mowing, edging, and bed upkeep on a schedule, so the yard stays sharp all season.'),
        ('seasonal-cleanups.html', 'real-fall-leaf-crew.webp', 'Cleanups &amp; snow', 'Fall and spring cleanups with leaves hauled away, plus seasonal snow removal.'),
    ]
    tiles_html = ''.join(f'<a class="tm-tile tm-reveal" href="{href}"><img src="assets/{img}" alt="" loading="lazy"><div class="tm-tile-body"><h3>{t}</h3><p>{d}</p><span class="tm-tile-go">Learn more</span></div></a>' for href, img, t, d in tiles)
    icons = {
        'walk': '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M12 21s-6-5.6-6-10.5A6 6 0 0 1 18 10.5C18 15.4 12 21 12 21z"/><circle cx="12" cy="10.5" r="2.2"/></svg>',
        'quote': '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M7 3h7l4 4v14H7z"/><path d="M14 3v4h4M9.5 12h6M9.5 15.5h6M9.5 8.5h2.5"/></svg>',
        'build': '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M14.5 3.5l6 6-2 2-6-6zM12.5 5.5L4 14l2 6 6 2 8.5-8.5"/><path d="M8 16l3-3"/></svg>',
    }
    steps = [
        ('walk', 'Walk the yard', 'We come out, look at grade, drainage, soil, and access, and listen to how you want to use the space.', 'Free visit'),
        ('quote', 'Design + written quote', 'You get a plan you can picture and a quote that spells out the full scope before any work starts.', 'Price in writing first'),
        ('build', 'Build + final walkthrough', 'The same crew builds it, cleans up every day, and walks the finished work with you.', 'Same crew, start to finish'),
    ]
    steps_html = ''.join(f'<div class="tm-proc-step" role="listitem" style="--i:{i}"><div class="tm-proc-node"><span class="tm-proc-icon">{icons[ic]}</span></div><span class="tm-proc-num">0{i+1}</span><h3>{h}</h3><p>{p}</p><span class="tm-proc-tag">{tag}</span></div>' for i, (ic, h, p, tag) in enumerate(steps))
    town_links = ''.join(f'<a href="{p}">{n}</a>' for n, _, _, p in TOWNS)
    faqs = c['DEFAULT_FAQS']
    body = f'''
<section class="tm-hero">
  <div class="tm-hero-media"><img src="assets/real-hero.webp" alt="Striped lawn and stone wall at a Northwest Ohio home maintained by Terramorph" width="1280" height="960" fetchpriority="high" loading="eager"></div>
  <div class="tm-hero-shade"></div>
  <div class="tm-hero-inner">
    <p class="tm-label">Perrysburg · Toledo · Wood &amp; Lucas County</p>
    <h1 class="tm-h1"><span class="tm-word">Landscape design,</span> <span class="tm-word" style="animation-delay:.12s">patios &amp; drainage,</span> <span class="tm-word" style="animation-delay:.24s"><span class="tm-underline">built</span> for</span> <span class="tm-word" style="animation-delay:.36s">Northwest Ohio.</span></h1>
    <p class="tm-hero-sub">One local design/build team for the whole property, from a soggy backyard to a finished patio, with a clear written quote first.</p>
    <div class="tm-cta-row">
      <a class="tm-btn tm-btn-gold tm-btn-shine" href="#request-form">Get my free quote</a>
      <a class="tm-btn tm-btn-ghost" href="tel:{c['TEL']}">Call {c['PHONE']}</a>
    </div>
    <div class="tm-proof-row"><span><span class="tm-stars">★★★★★</span> <a href="{c['GOOGLE_PROFILE_URL']}" target="_blank" rel="noopener">4.9 from 220+ Google reviews</a></span><span>BBB Accredited</span><span>Free estimates</span></div>
  </div>
</section>
{marquee_html(c)}
{yard_picker()}

<section class="tm-sec" id="services">
  <div class="tm-wrap">
    <div class="tm-head-row"><div><p class="tm-label">What are you planning?</p><h2 class="tm-h2">Start with the <span class="tm-foil">project</span> on your mind.</h2></div><p class="tm-lead">Every tile is real Terramorph work. Pick the one closest to your project to see how we handle it.</p></div>
    <div class="tm-tiles">{tiles_html}</div>
  </div>
</section>

<section class="tm-sec tm-paper">
  <div class="tm-wrap tm-ba-grid">
    <div class="tm-reveal">
      <p class="tm-label">Before &amp; after</p>
      <h2 class="tm-h2">Drag to see the difference one visit makes.</h2>
      <p class="tm-lead">A wooded property near Toledo, buried in leaves, and the same yard after a Terramorph fall cleanup. Leaves cleared and hauled away, lawn finished.</p>
      <div class="tm-cta-row" style="margin-top:28px"><a class="tm-btn tm-btn-gold" href="#request-form">Want this for your yard? Get a free quote</a></div>
    </div>
    <div class="tm-ba tm-reveal" data-ba style="--pos:50%">
      <img src="assets/real-fall-cleanup-after.webp" alt="Same backyard after a Terramorph fall cleanup, clean striped lawn" loading="lazy">
      <img class="tm-ba-before" src="assets/real-fall-cleanup-before.webp" alt="Backyard covered in fall leaves before the cleanup" loading="lazy">
      <span class="tm-ba-tag l">Before</span><span class="tm-ba-tag r">After</span>
      <div class="tm-ba-handle"><div class="tm-ba-knob" aria-hidden="true">&#8596;</div></div>
      <input class="tm-ba-range" type="range" min="0" max="100" value="50" aria-label="Slide to compare before and after">
    </div>
  </div>
</section>

<section class="tm-sec-tight tm-work">
  <div class="tm-wrap"><div class="tm-head-row tm-reveal"><div><p class="tm-label">Recent work</p><h2 class="tm-h2">Real yards. Real <span class="tm-foil">Terramorph</span> crews.</h2></div><a class="tm-btn tm-btn-line" href="projects.html">See all project photos</a></div></div>
  <div class="tm-work-rail">{c['photo_gallery']()}</div>
</section>

<section class="tm-sec tm-process tm-dark">
  {topo_svg()}
  <div class="tm-wrap">
    <div class="tm-head-row tm-reveal"><div><p class="tm-label">How it works</p><h2 class="tm-h2">Three steps. <span class="tm-foil">No guesswork.</span></h2></div><p class="tm-lead">You always know what happens next, and what it costs, before any work begins.</p></div>
    <div class="tm-proc" data-proc role="list"><span class="tm-proc-line" aria-hidden="true"><i></i></span>{steps_html}</div>
  </div>
</section>

<section class="tm-sec tm-dark">
  <div class="tm-wrap">
    <div class="tm-head-row"><div><p class="tm-label">Reviews</p><h2 class="tm-h2">What Northwest Ohio homeowners say.</h2></div>
      <div class="tm-rating-big"><b>4.9</b><div><div class="tm-stars">★★★★★</div><a href="{c['GOOGLE_PROFILE_URL']}" target="_blank" rel="noopener" style="color:#fff">Read all 220+ on Google &rarr;</a></div></div></div>
    <div class="tm-reviews">{featured}</div>
  </div>
</section>

<section class="tm-sec tm-paper">
  <div class="tm-wrap tm-map-grid">
    <div class="tm-reveal">
      <p class="tm-label">Service area</p>
      <h2 class="tm-h2">Do we come to you?</h2>
      <p class="tm-lead">Tap a town on the map. Terramorph is based in Perrysburg and works across Wood and Lucas County.</p>
      <div class="tm-town-card" data-town-card aria-live="polite"><b>Pick a town on the map</b><p>We'll show you what we do there.</p></div>
      <div class="tm-town-list">{town_links}</div>
    </div>
    <div class="tm-map" data-map>{service_map(c)}</div>
  </div>
</section>

<section class="tm-sec-tight">
  <div class="tm-wrap">
    <div class="tm-facts tm-reveal">
      <div>
        <p class="tm-label">Terramorph at a glance</p>
        <h2 class="tm-h2" style="font-size:clamp(1.9rem,3.4vw,2.7rem)">The short version.</h2>
        <p>Terramorph LLC is a landscape design and build company based in Perrysburg, Ohio, founded by brothers Ty and Trent Lincoln. We design and install paver patios, retaining walls, drainage systems, landscape beds, and outdoor lighting, and we maintain lawns, handle seasonal cleanups, and plow snow for homes and businesses across Wood and Lucas County. We hold a 4.9-star rating from more than 220 Google reviews and are BBB accredited. Estimates are free.</p>
      </div>
      <dl class="tm-facts-grid">
        <div><dt>Based in</dt><dd>Perrysburg, OH</dd></div>
        <div><dt>Serving</dt><dd>Wood &amp; Lucas County</dd></div>
        <div><dt>Google rating</dt><dd>4.9 from 220+ reviews</dd></div>
        <div><dt>Accreditation</dt><dd>BBB Accredited</dd></div>
        <div><dt>Founders</dt><dd>Ty &amp; Trent Lincoln</dd></div>
        <div><dt>Phone</dt><dd><a href="tel:{c['TEL']}">{c['PHONE']}</a></dd></div>
      </dl>
    </div>
  </div>
</section>

<section class="tm-sec tm-paper">
  <div class="tm-wrap">
    <p class="tm-label">Questions</p>
    <h2 class="tm-h2" style="margin-bottom:26px">Before you reach out.</h2>
    <div class="tm-faq">{faq_html(faqs)}</div>
  </div>
</section>

<section class="tm-sec tm-quote tm-dark">
  <div class="tm-quote-bg"><img src="assets/real-lighting-night.webp" alt="" loading="lazy"></div>
  <div class="tm-wrap tm-quote-grid">
    <div>
      <p class="tm-label">Free quote</p>
      <h2 class="tm-h2">Let's walk your yard.</h2>
      <ul class="tm-quote-points"><li>Tell us what you want built, fixed, or cleaned up</li><li>Add photos if you have them, they help</li><li>We follow up to set up a visit and a written quote</li></ul>
      <a class="tm-btn tm-btn-ghost" href="tel:{c['TEL']}">Rather talk? Call {c['PHONE']}</a>
    </div>
    {form_panel(c, 'Request your free Terramorph quote', 'Outdoor Transformation')}
  </div>
</section>
'''
    return body

def render_quote(c):
    REV = dict(c['REVIEW_SNIPPETS'])
    revs = ''.join(f'<article class="tm-review"><div class="tm-stars">★★★★★</div><blockquote>{REV[n]}</blockquote><cite>{n}</cite></article>' for n in ['Richard Hansen', 'Barb Flowers'] if n in REV)
    return f'''
<section class="tm-qhero tm-dark">
  <div class="tm-wrap tm-q-grid">
    <div>
      <p class="tm-label">Free estimate</p>
      <h1 class="tm-h1">Get your free quote.</h1>
      <div class="tm-chips"><span>★ 4.9 from 220+ Google reviews</span><span>BBB Accredited</span><span>Wood &amp; Lucas County</span></div>
      {form_panel(c, 'Request your free Terramorph quote', 'Outdoor Transformation')}
    </div>
    <aside>
      <p class="tm-label" style="margin-top:6px">What happens next</p>
      <ol class="tm-next">
        <li><b>1</b><div><strong>We read your request</strong><span>Your project, address, timeline, and any photos come straight to our team.</span></div></li>
        <li><b>2</b><div><strong>We walk the yard</strong><span>We set a time to see the property and talk through what you want.</span></div></li>
        <li><b>3</b><div><strong>You get a written quote</strong><span>A clear scope and price before any work begins. No pressure.</span></div></li>
      </ol>
      <div style="margin-top:22px;display:grid;gap:14px">{revs}</div>
      <p style="margin-top:22px;color:#d6e2d4">Rather talk it through? <a href="tel:{c['TEL']}" style="color:var(--tm-gold-hi);font-weight:700">Call {c['PHONE']}</a></p>
    </aside>
  </div>
</section>
'''

NO_GALLERY = {'privacy.html', 'terms.html', 'thank-you.html', 'warranty.html', 'review-notes.html', 'projects.html', 'before-after-gallery.html'}
LEGACY_NAV = re.compile(r'<a class="skip-link" href="#main">Skip to content</a>\s*<div class="topbar".*?</header>\s*', re.S)
LEGACY_FOOT = re.compile(r'<div class="sticky-mobile".*?</footer>\s*', re.S)


def write_llms_txt(c):
    """Plain-text summary for AI assistants (llms.txt convention). Facts only."""
    import svc_v2
    B = c['BASE_URL']
    svc_lines = '\n'.join(f"- [{v['name']}]({B}/{k}): {svc_v2.ANSWERS.get(k, '')}" for k, v in svc_v2.SERVICES.items())
    towns = ', '.join(n for n, *_ in TOWNS)
    text = f"""# Terramorph LLC

> Landscape design and build company in Perrysburg, Ohio, serving homes and businesses across Wood and Lucas County (Greater Toledo): paver patios and hardscapes, drainage solutions, landscape design and installation, outdoor lighting, lawn maintenance, seasonal cleanups, and snow removal. Founded by brothers Ty and Trent Lincoln. 4.9 stars from more than 220 Google reviews. BBB accredited. Free estimates.

## Contact
- Phone: {c['PHONE']}
- Website: {B}/
- Free quote: {B}/quote.html
- Google Business Profile: {c['GOOGLE_PROFILE_URL']}
- Address: {c['BUSINESS_STREET']}, {c['BUSINESS_CITY']}, {c['BUSINESS_REGION']} {c['BUSINESS_POSTAL']}

## Service area
{towns}, and the rest of Wood County and Lucas County, Ohio.

## Services
{svc_lines}

## More
- [Project photos]({B}/projects.html): real Terramorph jobs.
- [Service areas]({B}/service-areas.html)
- [Reviews]({B}/reviews.html)
- [About]({B}/about.html)
"""
    (c['root'] / 'llms.txt').write_text(text)

def apply(c):
    root = c['root']
    head, schema_for = c['head'], c['schema_for']
    # 1) Homepage + quote page: full v2 pages.
    for name, title, desc, body_fn, body_cls in [
        ('index.html', 'Landscape Design, Patios & Drainage | Terramorph Perrysburg',
         'Paver patios, drainage, landscape design, and lawn care across Wood and Lucas County, Ohio. 4.9 stars from 220+ Google reviews. Free estimates.',
         render_home, 'tm tm-home'),
        ('quote.html', 'Get a Free Quote | Terramorph LLC',
         'Request a free Terramorph quote for landscape design, patios, drainage, lighting, cleanups, maintenance, or snow removal in Wood and Lucas County, Ohio.',
         render_quote, 'tm quote-page'),
    ]:
        home = name == 'index.html'
        faqs = c['DEFAULT_FAQS'] if home else None
        schema = schema_for(name, title, desc, faqs)
        h = head(title, desc, schema, name)
        h = re.sub(r'<body[^>]*>.*$', '', h, flags=re.S)  # drop legacy body/nav
        h = _swap_head(h, home).replace('{v}', c['TM_CSS_VERSION'])
        page = h + f'<body class="{body_cls}">' + nav(c, home) + '<main id="main">' + body_fn(c) + '</main>' + foot(c, home) + f'<script src="app.js?v={c["APP_JS_VERSION"]}"></script>\n</body></html>\n'
        (root / name).write_text(page)
    # 2) Every other page: new header, footer, and phone bar over the old body.
    sc = dict(c, topo_svg=topo_svg, ba_card=ba_card, form_panel=form_panel)
    write_llms_txt(c)
    for path in root.glob('*.html'):
        if path.name in ('index.html', 'quote.html'):
            continue
        t = path.read_text()
        if 'http-equiv="refresh"' in t[:600] or '<header class="site-header">' not in t:
            continue
        t = LEGACY_NAV.sub(nav(c), t, count=1)
        t = LEGACY_FOOT.sub(foot(c), t, count=1)
        if 'tm.css' not in t:
            t = re.sub(r'(<link rel="stylesheet" href="styles\.css\?v=[^"]+">)', r'\1\n  <link rel="preload" href="assets/tm-fraunces.woff2" as="font" type="font/woff2" crossorigin>\n  <link rel="stylesheet" href="tm.css?v=' + c['TM_CSS_VERSION'] + '">', t, count=1)
        # v2 skin: tm-skin body class + the review strip right under the page hero.
        if 'tm-skin' not in t:
            extra_cls = ' tm-lp' if path.name.startswith('lp-') else ''
            t = re.sub(r'<body(?: class="([^"]*)")?>', lambda m: f'<body class="{(m.group(1) + " ") if m.group(1) else ""}tm-skin{extra_cls}">', t, count=1)
        # Real-work gallery on every content page that has no project photos yet.
        if 'photo-carousel' not in t and path.name not in NO_GALLERY and len(c['photos_for_page'](path.name)) >= 3:
            gal = ('<section class="section work-section tm-added-work"><div class="container section-heading compact"><p class="eyebrow">Recent work</p>'
                   '<h2>' + c['gallery_heading_for_page'](path.name, 'Real Terramorph projects around Northwest Ohio.') + '</h2></div><div class="container">' + c['photo_gallery'](c['photos_for_page'](path.name)) + '</div></section>\n')
            for marker in ('<section class="section faq-section">', '<section class="section quote-section">'):
                if marker in t:
                    t = t.replace(marker, gal + marker, 1)
                    break
        if path.name in svc_v2.SERVICES:
            t = svc_v2.rebuild(sc, path.name, t)
        # Pages that carry the quote form: header + phone-bar quote buttons jump to it
        # instead of loading quote.html (one less page load for paid visitors).
        if 'id="request-form"' in t:
            t = t.replace('class="tm-btn tm-btn-gold" href="quote.html">Free quote</a>', 'class="tm-btn tm-btn-gold" href="#request-form">Free quote</a>')
            t = re.sub(r'(<div class="tm-head-actions">.*?)href="quote\.html"', r'\1href="#request-form"', t, count=1, flags=re.S)
        # Share previews (Facebook, ads, texts) show this page's own hero photo.
        hero_img = re.search(r'<div class="page-hero-image"><img src="(assets/[^"?]+)', t)
        if hero_img:
            img_url = c['BASE_URL'] + '/' + hero_img.group(1)
            t = re.sub(r'(<meta property="og:image" content=")[^"]+(")', lambda m: m.group(1) + img_url + m.group(2), t, count=1)
            t = re.sub(r'(<meta name="twitter:image" content=")[^"]+(")', lambda m: m.group(1) + img_url + m.group(2), t, count=1)
        if 'tm-marquee' not in t:
            t = re.sub(r'(<section class="page-hero[^"]*".*?</section>)', lambda m: m.group(1) + '\n' + marquee_html(c), t, count=1, flags=re.S)
        # Every snow page points at the seasonal sign-up page (2026-10-26).
        if path.name.startswith('snow-removal') and path.name != 'snow-removal-signup.html' and 'tm-snow-cta' not in t:
            strip = ('<section class="tm-snow-cta"><div class="tm-wrap"><p><b>Winter sign-up is open.</b> Residential and commercial seasonal snow service. Reserve before the first storm.</p>'
                     f'<div class="tm-cta-row"><a class="tm-btn tm-btn-gold" href="snow-removal-signup.html">Sign up for winter service</a><a class="tm-btn tm-btn-line" href="tel:{c["TEL"]}">Call {c["PHONE"]}</a></div></div></section>\n')
            t = re.sub(r'(<div class="tm-marquee[^>]*>.*?</div>\s*</div>\s*)', lambda m: m.group(1) + strip, t, count=1, flags=re.S) if '<div class="tm-marquee' in t else t.replace('<main id="main">', '<main id="main">' + strip, 1)
        path.write_text(t)

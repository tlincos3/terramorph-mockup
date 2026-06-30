from pathlib import Path
import re

root = Path(__file__).resolve().parent
PHONE = '419-873-6801'
TEL = '4198736801'
BASE_URL = 'https://terramorphllc.com'
GOOGLE_PROFILE_URL = 'https://maps.app.goo.gl/GTv5RfxQ2AV8GHug7'
BBB_PROFILE_URL = 'https://www.bbb.org/us/oh/perrysburg/profile/landscape-contractors/terramorph-llc-0422-211013048'
FACEBOOK_URL = 'https://facebook.com/p/Terramorph-100089790245208/'
INSTAGRAM_URL = 'https://instagram.com/terramorphllc/'
BUSINESS_NAME = 'Terramorph LLC'
BUSINESS_CITY = 'Perrysburg'
BUSINESS_REGION = 'OH'
BUSINESS_POSTAL = '43551'
BUSINESS_COUNTRY = 'US'
BUSINESS_CATEGORY = 'Landscaping, hardscaping, drainage, lawn care, and outdoor property services'
OFFICIAL_NAP_NOTE = 'Official citation info: Terramorph LLC, Perrysburg, OH 43551, 419-873-6801, https://terramorphllc.com/'
JOBBER_CLIENTHUB_ID = 'e644a784-b214-4a2b-93df-ace28dbb2a70-1578803'
JOBBER_FORM_URL = 'https://clienthub.getjobber.com/client_hubs/e644a784-b214-4a2b-93df-ace28dbb2a70/public/work_request/embedded_work_request_form?form_id=1578803'
JOBBER_DIRECT_URL = 'https://clienthub.getjobber.com/hubs/e644a784-b214-4a2b-93df-ace28dbb2a70/public/requests/1578803/new'
SAME_AS_URLS = [
    GOOGLE_PROFILE_URL,
    BBB_PROFILE_URL,
    FACEBOOK_URL,
    INSTAGRAM_URL,
    'https://www.yelp.com/biz/terramorph-perrysburg-2',
    'https://nextdoor.com/pages/terramorph-llc-perrysburg-oh/'
]

NAV = f'''
<a class="skip-link" href="#main">Skip to content</a>
<div class="topbar" aria-label="Trust and contact bar">
  <div class="container topbar-inner">
    <div class="topbar-proof">
      <a href="{GOOGLE_PROFILE_URL}" target="_blank" rel="noopener">★★★★★ 200+ Google Reviews</a>
      <a href="{BBB_PROFILE_URL}" target="_blank" rel="noopener">BBB Member</a>
      <span>Licensed and insured</span>
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
      <a href="guides.html">Guides</a>
      <a href="service-areas.html">Areas</a>
      <a href="projects.html">Projects</a>
      <a href="about.html">About</a>
      <a href="quote.html">Quote</a>
    </nav>
    <div class="nav-actions">
      <a class="btn btn-quiet" href="tel:{TEL}">Call Now</a>
      <a class="btn btn-primary" href="quote.html">Request Quote</a>
    </div>
    <button class="mobile-menu" type="button" aria-expanded="false" aria-controls="primary-links" onclick="toggleMenu(this)">Menu</button>
  </div>
</header>
'''

FOOT = f'''
<div class="sticky-mobile" aria-label="Mobile lead actions">
  <a class="btn btn-quiet" href="tel:{TEL}">Call</a>
  <a class="btn btn-primary" href="quote.html">Quote</a>
</div>
<footer class="footer">
  <div class="container footer-grid">
    <div>
      <a class="brand footer-brand" href="index.html"><img src="assets/logo.png" alt="Terramorph logo" width="56" height="56"><span><strong>Terramorph</strong><small>Northwest Ohio Outdoor Transformation</small></span></a>
      <p>Premium landscape design, paver patios, drainage solutions, outdoor lighting, retaining walls, and outdoor living for Perrysburg, Toledo, Wood County, and Lucas County homeowners.</p>
      <p class="fine-print">Free estimates for design, patios, drainage, lighting, walls, seasonal cleanups, lawn maintenance, and bed maintenance programs.</p>
      <p class="fine-print official-nap">{OFFICIAL_NAP_NOTE}</p>
    </div>
    <div>
      <h2>Primary services</h2>
      <a href="landscape-design.html">Landscape design</a>
      <a href="paver-patios-hardscapes.html">Paver patios</a>
      <a href="drainage-solutions.html">Drainage Solutions</a>
      <a href="outdoor-lighting.html">Outdoor lighting</a>
      <a href="lawn-maintenance.html">Lawn maintenance</a>
      <a href="seasonal-cleanups.html">Seasonal cleanups</a>
      <a href="guides.html">Outdoor project guides</a>
      <a href="faq.html">FAQ hub</a>
      <a href="process.html">Process</a>
      <a href="materials.html">Materials guide</a>
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
      <h2>Contact and proof</h2>
      <a href="tel:{TEL}">Call {PHONE}</a>
      <a href="{BASE_URL}/">terramorphllc.com</a>
      <a href="quote.html">Request a quote</a>
      <a href="service-areas.html#official-business-info">Official business info</a>
      <a href="{GOOGLE_PROFILE_URL}" target="_blank" rel="noopener">Google Business Profile</a>
      <a href="{BBB_PROFILE_URL}" target="_blank" rel="noopener">BBB profile</a>
      <a href="{FACEBOOK_URL}" target="_blank" rel="noopener">Facebook</a>
      <a href="{INSTAGRAM_URL}" target="_blank" rel="noopener">Instagram</a>
      <a href="privacy.html">Privacy Policy</a>
      <a href="terms.html">Terms</a>
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

def head(title, desc, schema='', page_name=''):
    canonical_url = BASE_URL + ('/' if page_name in ('', 'index.html') else '/' + page_name)
    body_class = 'quote-page' if page_name == 'quote.html' else ''
    body_attr = f' class="{body_class}"' if body_class else ''
    stylesheet_version = '3.54' if page_name == 'quote.html' else ('3.53' if page_name == 'index.html' else '3.49')
    schema_block = f'\n  <script type="application/ld+json">{schema}</script>' if schema else ''
    robots_block = '\n  <meta name="robots" content="noindex, nofollow">' if page_name in ('thank-you.html', 'review-notes.html') else ''
    ga4_tag = '''
  <!-- Google tag (gtag.js) -->
  <script async src="https://www.googletagmanager.com/gtag/js?id=G-QRTSH6WXYK"></script>
  <script>
    window.dataLayer = window.dataLayer || [];
    function gtag(){dataLayer.push(arguments);}
    gtag('js', new Date());
    gtag('config', 'G-QRTSH6WXYK');
    gtag('config', 'AW-17691366114');
  </script>'''
    meta_pixel = '''
  <!-- Meta Pixel Code -->
  <script>
  !function(f,b,e,v,n,t,s){if(f.fbq)return;n=f.fbq=function(){n.callMethod?
  n.callMethod.apply(n,arguments):n.queue.push(arguments)};if(!f._fbq)f._fbq=n;
  n.push=n;n.loaded=!0;n.version='2.0';n.queue=[];t=b.createElement(e);t.async=!0;
  t.src=v;s=b.getElementsByTagName(e)[0];s.parentNode.insertBefore(t,s)}(window, document,'script',
  'https://connect.facebook.net/en_US/fbevents.js');
  fbq('init', '1286455403443187');
  fbq('track', 'PageView');
  </script>
  <noscript><img height="1" width="1" style="display:none" alt="" src="https://www.facebook.com/tr?id=1286455403443187&ev=PageView&noscript=1" /></noscript>
  <!-- End Meta Pixel Code -->'''
    return f'''<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{title}</title>
  <meta name="description" content="{desc}">
  <link rel="canonical" href="{canonical_url}">
  <meta property="og:title" content="{title}">
  <meta property="og:description" content="{desc}">
  <meta property="og:type" content="website">
  <meta property="og:url" content="{canonical_url}">
  <meta property="og:site_name" content="Terramorph LLC">
  <meta property="og:image" content="{BASE_URL}/assets/real-hero.webp">
  <meta property="og:image:alt" content="Terramorph outdoor transformation project in Northwest Ohio">
  <meta name="twitter:card" content="summary_large_image">
  <meta name="twitter:title" content="{title}">
  <meta name="twitter:description" content="{desc}">
  <meta name="twitter:image" content="{BASE_URL}/assets/real-hero.webp">
  <meta name="format-detection" content="telephone=yes">
  <meta name="facebook-domain-verification" content="2s5mtnhpfztxtlwe85t8eflj8ubajd">
  <link rel="preconnect" href="https://www.googletagmanager.com">
  <link rel="preconnect" href="https://connect.facebook.net">
  <link rel="stylesheet" href="styles.css?v={stylesheet_version}">{robots_block}{schema_block}{ga4_tag}{meta_pixel}
</head>
<body{body_attr}>{NAV}<main id="main">'''

def optimize_markup(html):
    """Small performance/accessibility pass for generated static pages."""
    image_size_cache = {}
    def get_image_size(src):
        clean_src = src.split('?', 1)[0].split('#', 1)[0]
        if not clean_src.startswith('assets/'):
            return None
        if clean_src in image_size_cache:
            return image_size_cache[clean_src]
        path = root / clean_src
        size = None
        if path.exists() and path.suffix.lower() != '.svg':
            data = path.read_bytes()[:64]
            if data.startswith(b'RIFF') and data[8:12] == b'WEBP' and len(data) >= 30:
                if data[12:16] == b'VP8X' and len(data) >= 30:
                    width = 1 + int.from_bytes(data[24:27], 'little')
                    height = 1 + int.from_bytes(data[27:30], 'little')
                    size = (width, height)
                elif data[12:16] == b'VP8 ' and len(data) >= 30:
                    width = int.from_bytes(data[26:28], 'little') & 0x3fff
                    height = int.from_bytes(data[28:30], 'little') & 0x3fff
                    size = (width, height)
            elif data.startswith(b'\x89PNG\r\n\x1a\n') and len(data) >= 24:
                size = (int.from_bytes(data[16:20], 'big'), int.from_bytes(data[20:24], 'big'))
            elif data.startswith(b'\xff\xd8'):
                raw = path.read_bytes()
                idx = 2
                while idx < len(raw) - 9:
                    if raw[idx] != 0xff:
                        idx += 1
                        continue
                    marker = raw[idx + 1]
                    length = int.from_bytes(raw[idx + 2:idx + 4], 'big') if idx + 4 <= len(raw) else 0
                    if marker in {0xc0, 0xc1, 0xc2, 0xc3, 0xc5, 0xc6, 0xc7, 0xc9, 0xca, 0xcb, 0xcd, 0xce, 0xcf}:
                        size = (int.from_bytes(raw[idx + 7:idx + 9], 'big'), int.from_bytes(raw[idx + 5:idx + 7], 'big'))
                        break
                    idx += 2 + max(length, 1)
        image_size_cache[clean_src] = size
        return size

    def img_attrs(match):
        tag = match.group(0)
        src_match = re.search(r'\ssrc="([^"]+)"', tag)
        size = get_image_size(src_match.group(1)) if src_match else None

        def add_attr(current_tag, attr):
            if current_tag.endswith('/>'):
                return current_tag[:-2].rstrip() + f' {attr} />'
            return current_tag[:-1].rstrip() + f' {attr}>'

        if size and ' width=' not in tag.lower() and ' height=' not in tag.lower():
            tag = add_attr(tag, f'width="{size[0]}" height="{size[1]}"')
        if ' loading=' not in tag.lower() and ' fetchpriority=' not in tag.lower():
            tag = add_attr(tag, 'loading="lazy"')
        if ' decoding=' not in tag.lower():
            tag = add_attr(tag, 'decoding="async"')
        return tag
    return re.sub(r'<img\b[^>]*>', img_attrs, html)

def page(title, desc, body, schema=''):
    # Infer page name from schema where possible, otherwise callers can rely on index default.
    page_name = ''
    try:
        import json
        graph = json.loads(schema).get('@graph', []) if schema else []
        webpage = next((item for item in graph if item.get('@type') == 'WebPage'), {})
        url = webpage.get('url', '')
        if url and url.startswith(BASE_URL + '/'):
            page_name = url.replace(BASE_URL + '/', '') or 'index.html'
    except Exception:
        page_name = ''
    footer = FOOT
    if page_name in {'thank-you.html', 'privacy.html', 'terms.html', 'review-notes.html'}:
        footer = FOOT.replace('href="#quote"', 'href="contact.html#quote"')
    html = head(title, desc, schema, page_name) + body + '</main>' + quote_popup() + footer + '</body></html>'
    if page_name == 'index.html':
        html = html.replace('<a href="quote.html">Quote</a>', '<a href="#request-form">Quote</a>')
        html = html.replace('<a class="btn btn-primary" href="quote.html">Request Quote</a>', '<a class="btn btn-primary" href="#request-form">Request Quote</a>')
        html = html.replace('<a class="btn btn-primary" href="quote.html">Quote</a>', '<a class="btn btn-primary" href="#request-form">Quote</a>')
        html = html.replace('<a href="quote.html">Request a quote</a>', '<a href="#request-form">Request a quote</a>')
    return optimize_markup(html)

def quick_lead_form(service, offer):
    return f"""
<section class="quick-lead-card" aria-labelledby="quick-lead-title" data-service="{service}">
  <div class="quick-lead-copy">
    <p class="eyebrow light">Fast first step</p>
    <h2 id="quick-lead-title">Start the free assessment with a direct call.</h2>
    <p>{offer}. Send the basics first, then call Terramorph so the team can confirm the best next step.</p>
    <div class="quick-lead-proof"><span>★★★★★ 200+ Google Reviews</span><span>Licensed + insured</span><span>Wood + Lucas County</span></div>
  </div>
  <form class="quick-lead-form" data-quick-lead-form data-service="{service}" novalidate>
    <label>Name <input name="name" autocomplete="name" required></label>
    <label>Phone <input name="phone" type="tel" inputmode="tel" autocomplete="tel" required></label>
    <label>City <input name="city" autocomplete="address-level2" required></label>
    <label>Timeline
      <select name="timeline">
        <option value="">Choose one</option>
        <option>ASAP</option>
        <option>This month</option>
        <option>1-3 months</option>
        <option>Planning ahead</option>
      </select>
    </label>
    <label class="quick-lead-wide">What needs fixed or built?
      <textarea name="problem" rows="3" placeholder="Example: standing water near patio after rain, soggy backyard, downspout issue..." required></textarea>
    </label>
    <input type="hidden" name="service" value="{service}">
    <button class="btn btn-gold" type="submit">Call {PHONE}</button>
    <p class="quick-lead-status" data-quick-lead-status>Complete the basics, then call Terramorph at {PHONE}.</p>
  </form>
</section>"""

def quote_form(title='Request a Premium Project Quote', service='Outdoor Transformation', source='website', cta='Start Request', direct_only=False, same_tab=False):
    return f'''
<section class="quote-panel phone-quote-panel" id="quote" aria-labelledby="quote-title" data-service="{service}">
  <p class="eyebrow light">Fast free estimate</p>
  <h2 id="quote-title">{title}</h2>
  <p>Use the request form to send Terramorph the basics first, or call directly if the project is urgent.</p>
  <div class="quote-speed-row" aria-label="Fast estimate expectations">
    <span>✓ Free estimate</span><span>✓ Simple request form</span><span>✓ Wood + Lucas County</span>
  </div>
  <div class="phone-direct-card">
    <p class="eyebrow">Best next step</p>
    <h3>Send the project details, then Terramorph can follow up.</h3>
    <p>The quote page asks for name, phone, city, address, service type, timeline, and project notes so the crew has enough context before the first call.</p>
    <ul class="check-list">
      <li>Good for landscaping, patios, drainage, lighting, cleanups, maintenance, and snow service.</li>
      <li>Works on mobile so homeowners can text the request details directly.</li>
      <li>Call {PHONE} anytime for urgent property issues or scheduling questions.</li>
    </ul>
    <div class="phone-direct-actions"><a class="btn btn-gold" href="quote.html">Open Quote Form</a><a class="btn btn-outline-light" href="tel:{TEL}" data-quote-service="{service}">Call {PHONE}</a></div>
  </div>
</section>'''

def inline_jobber_quote_form(title='Request My Outdoor Transformation Quote'):
    return f'''
<section class="quote-panel jobber-quote-panel quote-request-section" id="request-form" aria-labelledby="home-request-title" data-service="Outdoor Transformation">
  <div class="quick-lead-card quote-request-card">
    <div class="quick-lead-copy">
      <p class="eyebrow light">Fast free estimate</p>
      <h2 id="home-request-title">{title}</h2>
      <p>Fill out the secure Terramorph Jobber form right here on the site. New requests go directly into the CRM so the team gets the service, city, photos, timeline, and project notes without sending visitors to another page first.</p>
      <div class="quick-lead-proof"><span>★★★★★ 200+ Google Reviews</span><span>Licensed + insured</span><span>Wood + Lucas County</span></div>
    </div>
    <div>
      <div class="jobber-embed-wrap" aria-label="Terramorph Jobber quote request form">
        <div id="{JOBBER_CLIENTHUB_ID}">
          <script src="https://d3ey4dbjkt2f6s.cloudfront.net/assets/static_link/work_request_embed_snippet.js" clienthub_id="{JOBBER_CLIENTHUB_ID}" form_url="{JOBBER_FORM_URL}"></script>
        </div>
      </div>
      <div class="jobber-fallback">
        <p>If the embedded form does not load, open the secure Jobber request form directly.</p>
        <a class="btn btn-gold" href="{JOBBER_DIRECT_URL}" target="_blank" rel="noopener">Open Jobber Quote Form</a>
        <a class="btn btn-outline-light" href="tel:{TEL}">Call {PHONE}</a>
      </div>
    </div>
  </div>
</section>'''

def quote_popup():
    return f'''
<div class="quote-popup" id="quote-popup" role="dialog" aria-modal="true" aria-labelledby="quote-popup-title" aria-describedby="quote-popup-desc" hidden>
  <div class="quote-popup-backdrop" data-close-popup></div>
  <section class="quote-popup-card quote-popup-simple" tabindex="-1">
    <button class="quote-popup-close" type="button" aria-label="Close free quote popup" data-close-popup>×</button>
    <div class="quote-popup-copy">
      <p class="eyebrow">Free estimate</p>
      <h2 id="quote-popup-title">Request a free Terramorph quote.</h2>
      <p id="quote-popup-desc">Send project details through the quote form, or call directly for urgent service questions and scheduling.</p>
      <div class="popup-trust"><a href="{GOOGLE_PROFILE_URL}" target="_blank" rel="noopener">★★★★★ 200+ Google Reviews</a><span>Licensed and insured</span><span>Serving Wood and Lucas County</span></div>
    </div>
    <div class="popup-direct-actions">
      <h3>Ready for an estimate?</h3>
      <p>Call now and Terramorph can confirm the right next step.</p>
      <a class="btn btn-gold" href="tel:{TEL}">Call {PHONE}</a>
      <a class="btn btn-primary" href="tel:{TEL}">Call {PHONE}</a>
    </div>
  </section>
</div>'''

def trust_band():
    return f'''
<section class="trust-band" aria-label="Terramorph credibility">
  <div class="container trust-grid">
    <a class="trust-feature trust-link" href="{GOOGLE_PROFILE_URL}" target="_blank" rel="noopener"><strong>200+</strong><span>Google Reviews</span><small>Consistent 5-star feedback from homeowners across the area.</small></a>
    <a class="trust-logo trust-link" href="{GOOGLE_PROFILE_URL}" target="_blank" rel="noopener"><img src="assets/google-verified.png" width="150" height="100" alt="Google Verified badge"><span>Google Verified</span></a>
    <a class="trust-logo trust-link" href="{BBB_PROFILE_URL}" target="_blank" rel="noopener"><img src="assets/bbb-logo.svg" width="240" height="84" alt="BBB Better Business Bureau logo"><span>BBB Member</span></a>
    <div class="trust-feature"><strong>Regional</strong><span>Serving Wood and Lucas County</span><small>Northwest Ohio-specific expertise for outdoor projects, drainage, and property upkeep.</small></div>
    <div class="trust-feature"><strong>Insured</strong><span>Licensed and insured</span><small>Professional protection before work starts.</small></div>
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
      <div><b>Licensed and insured</b><span>Professional protection and accountability for residential, commercial, and industrial properties.</span></div>
      <div><b>Certified training</b><span>Team members bring training and practical field experience for safer recommendations, cleaner installs, and better problem-solving.</span></div>
      <div><b>Local conditions</b><span>Clay soil, flat lots, freeze-thaw cycles, drainage problems, and Northwest Ohio weather are accounted for in the work.</span></div>
    </div>
  </div>
</section>'''

def official_business_info():
    return f'''
<section class="section official-business-section" id="official-business-info" aria-labelledby="official-business-title">
  <div class="container official-business-card">
    <div>
      <p class="eyebrow">Official business information</p>
      <h2 id="official-business-title">The citation data Google, Meta, and directories should match.</h2>
      <p>Local platforms should use one clean version of Terramorph's name, phone, website, service area, and category. This keeps Terramorph's name, phone, website, service area, and category consistent everywhere homeowners may find the business.</p>
    </div>
    <dl class="nap-grid">
      <div><dt>Business name</dt><dd>{BUSINESS_NAME}</dd></div>
      <div><dt>Phone</dt><dd><a href="tel:{TEL}">{PHONE}</a></dd></div>
      <div><dt>Website</dt><dd><a href="{BASE_URL}/">terramorphllc.com</a></dd></div>
      <div><dt>Primary area</dt><dd>{BUSINESS_CITY}, {BUSINESS_REGION} {BUSINESS_POSTAL}</dd></div>
      <div><dt>Service area</dt><dd>Wood County, Lucas County, Perrysburg, Toledo, Maumee, and Northwest Ohio</dd></div>
      <div><dt>Category</dt><dd>{BUSINESS_CATEGORY}</dd></div>
    </dl>
    <p class="fine-print">If a directory shows a different phone number, misspelled street variation, old business name, or incomplete category, it should be corrected to match this page.</p>
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
  <div class="hero-media"><img src="assets/real-hero.webp" alt="Terramorph landscaping, hardscape, and outdoor property transformation in Northwest Ohio"></div>
  <div class="hero-overlay"></div>
  <div class="container hero-content">
    <div class="hero-copy">
      <p class="eyebrow light">Northwest Ohio outdoor transformation</p>
      <h1>Fix the yard. Finish the property. Make it worth coming home to.</h1>
      <p class="hero-lead">Landscape design, paver patios, drainage, lighting, cleanups, maintenance, and snow service for homeowners and properties that need outdoor work handled with real follow-through.</p>
      <div class="cta-row"><a class="btn btn-gold" href="#request-form">Get A Free Estimate</a><a class="btn btn-outline-light" href="#start-here">Choose My Project</a><a class="btn btn-outline-light" href="projects.html">See Work</a><a class="btn btn-call" href="tel:{TEL}">Call {PHONE}</a></div>
      <div class="above-fold-trust">
        <span>★★★★★ 200+ Google Reviews</span><span>Named Customer Reviews</span><span>BBB Member</span><span>Licensed and insured</span><span>Serving Wood and Lucas County with Northwest Ohio-specific expertise</span>
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
{official_business_info()}
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
    {inline_jobber_quote_form('Request My Outdoor Transformation Quote')}
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
    page_url = BASE_URL + ('/' if page_name == 'index.html' else '/' + page_name)
    base = {
      "@context":"https://schema.org",
      "@graph":[
        {"@type":["LocalBusiness","LandscapingBusiness","HomeAndConstructionBusiness"],"@id":BASE_URL+"/#business","name":BUSINESS_NAME,"alternateName":["Terramorph","Terramorph Outdoor Transformation Co."],"url":BASE_URL+"/","image":BASE_URL+"/assets/real-hero.webp","logo":BASE_URL+"/assets/logo.png","telephone":PHONE,"priceRange":"Free estimates","aggregateRating":{"@type":"AggregateRating","ratingValue":"5","reviewCount":"200"},"address":{"@type":"PostalAddress","addressLocality":BUSINESS_CITY,"addressRegion":BUSINESS_REGION,"postalCode":BUSINESS_POSTAL,"addressCountry":BUSINESS_COUNTRY},"contactPoint":{"@type":"ContactPoint","telephone":PHONE,"contactType":"customer service","areaServed":["Wood County OH","Lucas County OH","Northwest Ohio"],"availableLanguage":"English"},"sameAs":SAME_AS_URLS,"knowsAbout":["Landscape design","Paver patios","Drainage solutions","Outdoor lighting","Lawn maintenance","Seasonal cleanups","Snow removal","Hardscaping","Retaining walls","Mulch and rock beds"],"areaServed":[{"@type":"AdministrativeArea","name":"Wood County, OH"},{"@type":"AdministrativeArea","name":"Lucas County, OH"},{"@type":"City","name":"Perrysburg, OH"},{"@type":"City","name":"Toledo, OH"},{"@type":"City","name":"Maumee, OH"},{"@type":"AdministrativeArea","name":"Northwest Ohio"}],"description":"Landscape design, patios, drainage, outdoor lighting, lawn maintenance, seasonal cleanups, snow removal, and outdoor property work in Wood and Lucas County."},
        {"@type":"WebSite","@id":BASE_URL+"/#website","url":BASE_URL+"/","name":"Terramorph LLC","publisher":{"@id":BASE_URL+"/#business"}},
        {"@type":"Organization","@id":BASE_URL+"/#organization","name":BUSINESS_NAME,"url":BASE_URL+"/","logo":BASE_URL+"/assets/logo.png","sameAs":SAME_AS_URLS},
        {"@type":"WebPage","name":title,"description":desc,"url":page_url,"isPartOf":{"@id":BASE_URL+"/#website"},"primaryImageOfPage":{"@id":page_url+"#primaryimage"}},
        {"@type":"ImageObject","@id":page_url+"#primaryimage","url":BASE_URL+"/assets/real-hero.webp","contentUrl":BASE_URL+"/assets/real-hero.webp","caption":"Terramorph outdoor transformation project in Northwest Ohio"},
        {"@type":"BreadcrumbList","itemListElement":[{"@type":"ListItem","position":1,"name":"Home","item":BASE_URL+"/"},{"@type":"ListItem","position":2,"name":title,"item":page_url}]}
      ]
    }
    for reviewer, quote in REVIEW_SNIPPETS[:3]:
        base["@graph"].append({"@type":"Review","itemReviewed":{"@id":BASE_URL+"/#business"},"author":{"@type":"Person","name":reviewer},"reviewBody":quote.strip('“”')})
    if service:
        base["@graph"].append({"@type":"Service","name":service,"provider":{"@id":BASE_URL+"/#business"},"areaServed":["Wood County OH","Lucas County OH","Northwest Ohio"],"url":page_url})
    if page_name == 'index.html':
        base["@graph"].append({"@type":"OfferCatalog","name":"Terramorph outdoor services","itemListElement":[{"@type":"Offer","itemOffered":{"@type":"Service","name":name,"url":BASE_URL+"/"+href}} for name,_,_,_,_,href in SERVICES if href.endswith('.html')]})
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
<section class="section quote-section"><div class="container quote-grid">{quote_form(('Request an Outdoor Lighting Quote' if title == 'Outdoor Lighting' else 'Request a ' + title + ' Quote'))}<div class="cta-proof"><p class="eyebrow">Why homeowners reach out</p><h2>Reviews, proof, and a simple free estimate request.</h2>{review_stack(2)}</div></div></section>
'''
    desc = f'{title} in Toledo, Wood County, Lucas County, and Northwest Ohio by Terramorph. Free estimates for homeowners and property owners.'
    schema = schema_for(filename, f'{title} | Terramorph', desc, SERVICE_FAQS.get(title, DEFAULT_FAQS), title)
    (root / filename).write_text(page(f'{title} in Wood and Lucas County | Terramorph', desc, body, schema))


def meta_landing_page(filename, title, eyebrow, image, headline, lead, bullets, service, form_title, offer, symptoms, next_steps):
    faqs = SERVICE_FAQS.get(service, DEFAULT_FAQS)
    body = f'''
<section class="page-hero premium-page-hero meta-landing-hero conversion-hero" data-funnel-service="{service}">
  <div class="page-hero-image"><img src="assets/{image}" alt="{title} project photo"></div><div class="hero-overlay"></div>
  <div class="container page-hero-content"><p class="eyebrow light">{eyebrow}</p><h1>{headline}</h1><p>{lead}</p><div class="offer-card"><b>{offer}</b><span>Send the problem, city, timeline, and photos if you have them. Terramorph follows up with the best next step.</span></div><div class="cta-row"><a class="btn btn-gold" href="#quote">Get My Free Assessment</a><a class="btn btn-outline-light" href="tel:{TEL}">Call {PHONE}</a></div><div class="above-fold-trust"><span>★★★★★ 200+ Google Reviews</span><span>BBB Member</span><span>Licensed + insured</span><span>Local crew</span></div></div>
</section>
<section class="conversion-trust-strip" aria-label="Terramorph credibility"><div class="container conversion-trust-grid"><span>★★★★★ 200+ Google Reviews</span><span>Google Verified</span><span>BBB Member</span><span>Licensed + insured</span><span>Serving Toledo, Perrysburg, Maumee, Wood County, Lucas County</span></div></section>
<section class="section quick-lead-section"><div class="container">{quick_lead_form(service, offer)}</div></section>
<section class="section pain-proof-section"><div class="container pain-proof-grid"><div class="pain-card"><p class="eyebrow light">This is for you if</p><h2>{bullets[0]}</h2><ul>{''.join(f'<li>{item}</li>' for item in symptoms)}</ul><a class="btn btn-gold" href="#quote">See What This Would Cost</a></div><div class="proof-card"><p class="eyebrow">What Terramorph checks</p><h2>{bullets[1]}</h2><div class="proof-steps">{''.join(f'<div><b>{i+1}. {title}</b><span>{copy}</span></div>' for i,(title,copy) in enumerate(next_steps))}</div></div></div></section>
<section class="section clay-section"><div class="container local-grid"><div><p class="eyebrow">Why request now</p><h2>{bullets[2]}</h2><p>{bullets[3]}</p><a class="btn btn-primary" href="#quote">Start My Free Assessment</a></div><div class="authority-list"><div><b>Fast next step</b><span>Submit the form or call and Terramorph can review the property, service need, timeline, and photos.</span></div><div><b>Real project proof</b><span>Project photos and named reviews stay close to the quote path so the page feels credible, not generic.</span></div><div><b>Local conditions</b><span>Wood and Lucas County soil, drainage, freeze-thaw, and weather are considered before recommending work.</span></div><div><b>Clear estimate</b><span>The goal is a practical scope, clean communication, and a path to getting the work handled.</span></div></div></div></section>
<section class="section work-section"><div class="container section-heading compact"><p class="eyebrow">Project photos</p><h2>See the kind of work this estimate can start.</h2></div><div class="container">{photo_gallery()}</div></section>
{review_section()}
{faq_section(faqs)}
<section class="section quote-section"><div class="container quote-grid">{quote_form(form_title, service=service, source='website', cta='Call for Estimate', direct_only=True, same_tab=True)}<div class="cta-proof"><p class="eyebrow">Built for fast homeowner decisions</p><h2>One clear offer, visible proof, a call button, and a short quote path.</h2>{review_stack(3)}<ul class="check-list"><li>See real project proof before requesting an estimate.</li><li>Call Terramorph and share the project details.</li><li>Help Terramorph respond with the right next step faster.</li></ul></div></div></section>
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

meta_landing_page('lp-patios.html', 'Paver Patio Estimate', 'Patio and outdoor living estimate', 'real-patio.webp?v=3.14', 'Build the patio without the guesswork.', 'Request a free patio assessment for pavers, walkways, seating areas, fire pits, and backyard hardscape upgrades.', ['You want a better place to grill, host, relax, or connect the backyard to the home — but need a real plan and estimate first.', 'Terramorph reviews layout, base conditions, drainage, materials, access, and the finished look before scoping the project.', 'A better patio starts with a better plan.', 'The right patio plan connects daily use, backyard flow, drainage, materials, and budget before work starts.'], 'Paver Patios and Hardscapes', 'Request My Patio Estimate', 'Free Patio Cost + Layout Assessment', ['No useful place to grill or host', 'Old concrete or uneven walkways', 'Backyard feels disconnected from the house', 'Need drainage considered before hardscape work'], [('Layout', 'How the patio connects to doors, grill zones, walkways, seating, and yard flow.'), ('Base + drainage', 'Soil, grade, water movement, and freeze-thaw risk before a patio is priced.'), ('Scope', 'Materials, access, timeline, and budget range for the finished outdoor living space.')])
meta_landing_page('lp-drainage.html', 'Drainage Solution Estimate', 'Wet yard and standing water estimate', 'real-drainage.webp', 'Stop standing water after every rain.', 'Request a free drainage assessment for standing water, soggy lawn, runoff, grading, and downspout issues.', ['Standing water, soggy grass, runoff, or drainage near patios and foundations is making the property frustrating after every heavy rain.', 'Terramorph reviews grade, water movement, soil, low spots, downspouts, and practical ways to route water intentionally.', 'Drainage work needs local judgment.', 'Flat lots, clay soil, heavy rain, and freeze-thaw cycles make Northwest Ohio drainage different from a generic landscape job.'], 'Drainage Solutions', 'Request My Drainage Estimate', 'Free Yard Drainage Assessment', ['Standing water after rain', 'Soggy lawn or soft low spots', 'Water near the house, garage, patio, or beds', 'Downspouts dumping into the wrong area'], [('Source', 'Where the water starts: roof, neighbor runoff, driveway, grade, clay soil, or low spots.'), ('Route', 'Where water can move safely without creating a new problem.'), ('Fix', 'Practical options such as grading, downspout routing, swales, drains, or finished landscape solutions.')])
meta_landing_page('lp-landscape-design.html', 'Landscape Design And Installation Estimate', 'Landscape design and install estimate', 'real-entry.webp?v=3.14', 'Make the yard look designed.', 'Request a free landscape review for front beds, curb appeal, plantings, mulch, rock, edging, and full-yard refreshes.', ['The property looks builder-grade, tired, disconnected, or hard to maintain — and you want a clear plan before spending money.', 'Terramorph reviews curb appeal, beds, plantings, grading, access, drainage, maintenance, and how the whole property should feel finished.', 'Design and installation should work together.', 'The right plan connects plants, beds, edges, mulch, lighting, patios, drainage, and upkeep instead of treating them as separate guesses.'], 'Landscape Design', 'Request My Landscape Estimate', 'Free Curb Appeal + Landscape Plan Review', ['Front beds look empty, overgrown, or outdated', 'Not sure what plants/materials fit the house', 'Need mulch, rock, edging, sod, or plant installation', 'Want design, install, and maintenance to connect'], [('Curb appeal', 'What people see from the street, entry, driveway, and outdoor living areas.'), ('Conditions', 'Sun, soil, grade, water movement, maintenance, and existing plant material.'), ('Plan', 'A practical design/install scope that connects budget to the finished look.')])


meta_landing_page('lp-outdoor-lighting.html', 'Outdoor Lighting Estimate', 'Outdoor lighting estimate', 'real-lighting.webp?v=3.14', 'Make the property look finished after dark.', 'Request a free outdoor lighting assessment for paths, patios, entries, landscape beds, and nighttime curb appeal.', ['The property looks good during the day but disappears at night — or paths, entries, patios, and steps feel darker than they should.', 'Terramorph reviews path safety, focal points, patios, entry visibility, wiring routes, transformer placement, and the finished nighttime look.', 'Good lighting sells safety and curb appeal fast.', 'The right lighting plan makes the home feel warmer, safer, more premium, and more usable after sunset.'], 'Outdoor Lighting', 'Request My Lighting Estimate', 'Free Outdoor Lighting Walkthrough', ['Dark walkways, entries, steps, or patio edges', 'Landscape or hardscape disappears after sunset', 'Want better curb appeal at night', 'Need safety/security visibility without harsh floodlights'], [('Safety', 'Where people walk, step, park, enter, host, and move after dark.'), ('Curb appeal', 'Which trees, beds, walls, architecture, and patio areas should become nighttime focal points.'), ('Install plan', 'Fixture type, wire routes, transformer location, controls, timeline, and budget range.')])


GUIDES = [
    {'file':'northwest-ohio-yard-drainage-problems.html','title':'Why Your Yard Holds Water After It Rains in Northwest Ohio','short':'Standing water, soggy grass, and soft spots usually come from grading, clay soil, downspouts, or runoff with nowhere smart to go.','category':'Drainage guide','service':'Drainage Solutions','image':'real-drainage.webp','cta':'Request a Drainage Assessment','sections':[('Why Northwest Ohio yards stay wet','Many Wood and Lucas County lots are flat, clay-heavy, and slow to drain. When downspouts, neighboring runoff, compacted soil, or low spots add more water than the yard can absorb, the result is standing water after normal rain.'),('Common causes Terramorph checks first','The first review should look at grade, where water enters the property, where roof water exits, low areas near patios or walkways, soil compaction, erosion paths, and whether water is moving toward structures.'),('When it becomes more than an annoyance','Persistent wet areas can damage lawns, make patios harder to use, create muddy access routes, wash mulch out of beds, stress plants, and push water toward foundations or garages if it is not routed intentionally.'),('What a practical fix can include','Depending on the property, the answer may involve grading, downspout routing, a swale, French drain, catch basin, dry creek feature, soil correction, or a finished landscape solution that moves water without making the yard look patched together.')],'faqs':[('Can Terramorph fix standing water in my yard?','Terramorph evaluates grading, runoff, downspouts, soil, and low spots to recommend practical drainage options for Northwest Ohio properties.'),('Is every wet yard a French drain job?','No. Some yards need grading, downspout routing, swales, soil correction, or a combination instead of one default drain.'),('Do you serve Toledo and Wood County for drainage?','Yes. Terramorph serves Wood and Lucas County with drainage and outdoor property work.')]},
    {'file':'french-drains-vs-pop-up-emitters.html','title':'French Drains vs. Pop-Up Emitters: Which Drainage Solution Do You Need?','short':'Both can move water, but they solve different problems. The right answer depends on where the water starts, where it can safely discharge, and how the property is graded.','category':'Drainage guide','service':'Drainage Solutions','image':'real-drainage.webp','cta':'Compare Drainage Options','sections':[('What a French drain is for','A French drain is generally used to collect subsurface or surface water along a trench and move it away through pipe and stone. It can help in consistently wet areas, but it must be placed and discharged correctly.'),('What a pop-up emitter is for','A pop-up emitter is often used at the end of a buried downspout or drainage line so water can discharge at a safer location. It is not a magic fix if the discharge area is still too low or saturated.'),('The real decision point','The question is not which product sounds better. The question is where water is coming from, whether it needs collection or just routing, and where it can exit without creating a new problem.'),('Why local review matters','Flat Northwest Ohio lots and clay soil make discharge planning important. If the outlet is wrong, the system may simply move the puddle to a different part of the yard.')],'faqs':[('Is a French drain better than a pop-up emitter?','Not always. A French drain collects and moves water; a pop-up emitter usually discharges water from a line. The right choice depends on the property.'),('Can downspouts be connected to buried drainage?','Often yes, if the route and outlet make sense for the property and local conditions.'),('Will Terramorph tell me which option fits?','Yes. Terramorph reviews grade, water movement, soil, and discharge options before recommending a drainage approach.')]},
    {'file':'move-water-away-from-house.html','title':'How to Move Water Away From Your House, Garage, Patio, or Building','short':'Water should be routed intentionally before it sits near foundations, washes out beds, undermines hardscapes, or creates muddy access areas.','category':'Drainage guide','service':'Drainage Solutions','image':'real-hardscape.webp?v=3.14','cta':'Fix Water Near Structures','sections':[('Start with where the water comes from','Roof water, driveway runoff, neighbor runoff, patio slope, compacted soil, and low lawn areas can all push water toward a structure. A good fix starts by identifying the source.'),('Grade matters before products','If the land slopes toward the house, a drain alone may not solve the issue. Grading, swales, downspout routing, or hardscape corrections may need to work together.'),('Patios and walkways need water planning too','Hard surfaces shed water quickly. If patios, walks, or drive areas do not move water correctly, runoff can pool at edges, soften base material, or create freeze-thaw issues.'),('The goal is controlled discharge','The best solution moves water to a safer area where it can drain, disperse, or exit without flooding a neighbor, damaging landscaping, or creating a new wet spot.')],'faqs':[('What if water is pooling near my foundation?','Have the grading, downspouts, soil, and runoff path reviewed so water can be routed away from the structure.'),('Can patios cause drainage problems?','Yes. Hardscapes can change water movement, so drainage should be reviewed before and after patio or walkway work.'),('Does Terramorph handle drainage and landscaping together?','Yes. Drainage can be scoped with landscape, patio, bed, and property improvement work.')]},
    {'file':'native-prairie-landscaping-ohio.html','title':'Native Prairie Landscaping in Ohio: Low-Maintenance, Wildlife-Friendly, and Built for Local Conditions','short':'Native prairie landscaping can reduce mowing, support pollinators, improve habitat, and give larger properties a more intentional low-maintenance look.','category':'Native landscaping guide','service':'Landscape Design','image':'real-entry.webp?v=3.14','cta':'Plan Native Landscaping','sections':[('Why native prairie landscaping is different','Native prairie-style areas use plants adapted to the region rather than treating every open area like a traditional lawn. The result can be more habitat value and less weekly mowing once established.'),('Good fits for Ohio properties','Prairie and native habitat areas can work well along property edges, open acreage, drainage transitions, commercial properties, retention areas, and homeowners who want a more natural but still intentional landscape.'),('Maintenance is lower, not zero','Native areas still need planning, establishment, weed control, edge definition, and seasonal management. The goal is not neglect; it is a designed landscape that matures into lower routine input.'),('Tax and incentive note','Some property types or conservation programs may offer potential incentives, but Terramorph does not provide tax advice. Ask a qualified tax professional or local program administrator before relying on any deduction, credit, or incentive.')],'faqs':[('Is native prairie landscaping maintenance-free?','No. It can become lower-maintenance than turf, but it still needs planning, establishment, weed control, and seasonal management.'),('Can native landscaping help pollinators?','Yes. Properly selected native plants can support pollinators, wildlife, and healthier habitat.'),('Can native prairie landscaping qualify for tax benefits?','It may depend on property type, use, and programs. Ask a tax professional; Terramorph does not promise tax benefits.')]},
    {'file':'native-plants-vs-lawn-ohio.html','title':'Native Plants vs. Traditional Lawn: What Works Better in Northwest Ohio?','short':'Traditional lawn is clean and usable. Native planting can lower mowing and improve habitat. The best properties often use both in the right places.','category':'Native landscaping guide','service':'Landscape Design','image':'real-lawn.webp','cta':'Design the Right Mix','sections':[('Where lawn still makes sense','Turf is useful for play areas, clean front presentation, pets, paths, and places where people actually walk or gather. A good property plan keeps lawn where lawn has a job.'),('Where native plants can outperform turf','Native beds, prairie edges, habitat zones, and low-use areas can reduce mowing demands, add seasonal interest, support pollinators, and make larger properties feel more intentional.'),('The best answer is usually a mix','For many Northwest Ohio properties, the strongest design combines clean lawn areas, defined bed edges, native planting zones, drainage-aware grading, and maintenance access.'),('Make it look intentional','Native landscaping needs clean borders, clear transitions, smart plant selection, and seasonal management so it reads as designed instead of overgrown.')],'faqs':[('Should I replace my whole lawn with native plants?','Usually not. Most properties work best with lawn where it is useful and native planting where it reduces maintenance or adds habitat value.'),('Will native plants look messy?','They can if poorly planned. Defined edges, plant selection, and seasonal management make the difference.'),('Can Terramorph design native and traditional landscaping together?','Yes. Terramorph can plan lawn, beds, native areas, drainage, and maintenance as one property strategy.')]},
    {'file':'paver-patio-northwest-ohio-weather.html','title':'What Makes a Paver Patio Last in Northwest Ohio Weather?','short':'Freeze-thaw cycles, drainage, base prep, edge restraint, and water movement matter more than the surface paver people notice first.','category':'Patio guide','service':'Paver Patios and Hardscapes','image':'real-patio.webp?v=3.14','cta':'Plan a Durable Patio','sections':[('The base does the heavy lifting','A patio is only as good as the preparation beneath it. Excavation, base depth, compaction, and leveling affect whether the surface stays clean and stable.'),('Drainage protects the patio','Water should move away from the house and off the patio surface. Poor drainage can soften edges, create pooling, and make freeze-thaw movement worse.'),('Edges and transitions matter','Steps, walkways, lawn edges, beds, walls, and door thresholds all affect how the patio performs and feels. These details should be planned before installation.'),('Northwest Ohio weather is the test','Heavy rain, clay soil, winter freezing, and spring thaw make planning more important than choosing a nice-looking paver alone.')],'faqs':[('Why do patios sink or shift?','Common causes include poor base preparation, drainage problems, weak edge restraint, soil movement, or freeze-thaw stress.'),('Should drainage be planned before a patio?','Yes. Drainage and grading should be reviewed before patio work starts.'),('Does Terramorph build patios and walkways?','Yes. Terramorph handles paver patios, walkways, outdoor living areas, and related hardscape planning.')]},
    {'file':'spring-cleanup-northwest-ohio.html','title':'Spring Cleanup Checklist for Northwest Ohio Properties','short':'A proper spring reset clears winter debris, refreshes beds, catches damage early, and gets the property ready for mowing, mulch, planting, and outdoor use.','category':'Seasonal guide','service':'Seasonal Cleanups','image':'real-mulch.webp','cta':'Schedule Spring Cleanup','sections':[('Clear winter debris first','Leaves, sticks, dead plant material, trash, and storm debris should be removed before beds and lawn areas are refreshed.'),('Reset beds and edges','Spring is a good time to define bed edges, clean old mulch, identify weeds, prune appropriate material, and prepare for mulch, rock, or plant installation.'),('Look for drainage and turf issues','Soft areas, washouts, standing water, dead spots, and compacted paths are easier to spot after winter and early spring rain.'),('Set up the maintenance season','A cleanup can pair with mowing, bed maintenance, mulch, plant work, trimming, or other property services so the yard starts the season under control.')],'faqs':[('When should I schedule spring cleanup?','Early spring is ideal once winter debris is visible and before the property gets too far into the growing season.'),('Can cleanup include mulch or trimming?','Yes. Cleanups can be paired with mulch, bed resets, pruning, trimming, and lawn maintenance.'),('Does Terramorph handle commercial cleanups?','Yes. Terramorph can help residential, commercial, and property-owner cleanup needs in Wood and Lucas County.')]},
    {'file':'mulch-vs-rock-landscape-beds.html','title':'Mulch vs. Rock Beds: Which Is Better for Low-Maintenance Landscaping?','short':'Mulch and rock both work, but they create different looks, costs, maintenance needs, and heat conditions around plants.','category':'Landscape guide','service':'Landscape Design','image':'real-entry.webp?v=3.14','cta':'Choose Better Beds','sections':[('Why homeowners choose mulch','Mulch gives beds a clean fresh look, helps retain soil moisture, can improve soil over time, and is easier to change as plants grow or designs evolve.'),('Why homeowners choose rock','Rock can last longer visually, reduce annual refreshing, and work well in certain foundation beds or commercial areas, but it may hold heat and collect debris.'),('Plant health matters','Some plants prefer cooler, more organic bed conditions. Others can tolerate rock. The right choice depends on sunlight, irrigation, drainage, and the plant palette.'),('Low-maintenance still needs upkeep','Neither mulch nor rock eliminates weeds forever. Clean edges, proper fabric decisions, bed depth, drainage, and regular maintenance all affect how beds age.')],'faqs':[('Is rock lower-maintenance than mulch?','Sometimes, but not always. Rock may need less refreshing but can collect debris, hold heat, and still allow weeds if the bed is not built well.'),('Is mulch better for plants?','Often mulch is more forgiving for plant health because it moderates soil temperature and moisture, but the right answer depends on the bed.'),('Can Terramorph install mulch and rock beds?','Yes. Terramorph handles mulch, rock, edging, bed shaping, plant installation, and maintenance planning.')]},
]

def guide_schema(g):
    import json
    url = BASE_URL + '/' + g['file']
    data = json.loads(schema_for(g['file'], g['title'] + ' | Terramorph', g['short'], g['faqs'], g['service']))
    data['@graph'].append({'@type':'Article','headline':g['title'],'description':g['short'],'author':{'@type':'Organization','name':'Terramorph LLC'},'publisher':{'@id':BASE_URL+'/#business'},'mainEntityOfPage':url,'image':BASE_URL + '/assets/' + g['image'].split('?')[0]})
    return json.dumps(data, separators=(',',':'))

def guide_card(g):
    return f'''<a class="guide-card" href="{g['file']}"><span>{g['category']}</span><h3>{g['title']}</h3><p>{g['short']}</p><b>Read guide &rarr;</b></a>'''

def guides_hub():
    featured = ''.join(guide_card(g) for g in GUIDES[:3])
    all_cards = ''.join(guide_card(g) for g in GUIDES[3:])
    body = f'''
<section class="page-hero premium-page-hero guides-hero">
  <div class="page-hero-image"><img src="assets/real-hero.webp" alt="Terramorph Northwest Ohio outdoor project guides"></div><div class="hero-overlay"></div>
  <div class="container page-hero-content"><p class="crumb"><a href="index.html">Home</a> / Outdoor Project Guides</p><p class="eyebrow light">Northwest Ohio property guides</p><h1>Clear answers for drainage, patios, native landscaping, cleanups, and low-maintenance beds.</h1><p>Helpful local guides built to rank organically and move homeowners toward the right Terramorph estimate.</p><div class="cta-row"><a class="btn btn-gold" href="contact.html">Request a Free Estimate</a><a class="btn btn-outline-light" href="tel:{TEL}">Call {PHONE}</a></div></div>
</section>
{trust_band()}
<section class="section guide-index-section"><div class="container section-heading compact"><p class="eyebrow">Start here</p><h2>High-intent outdoor project answers.</h2><p>These are written around the problems homeowners search when they are close to taking action: wet yards, drainage decisions, patio durability, native landscaping, seasonal cleanup, and bed material choices.</p></div><div class="container guide-grid featured-guides">{featured}</div></section>
<section class="section work-section"><div class="container section-heading compact"><p class="eyebrow">More guides</p><h2>Build confidence before the quote request.</h2></div><div class="container guide-grid">{all_cards}</div></section>
<section class="section quote-section"><div class="container quote-grid">{quote_form('Ask Terramorph What Fits Your Property')}<div class="cta-proof"><p class="eyebrow">Not sure where to start?</p><h2>Send the problem, city, photos, and timeline. Terramorph can point you toward the right next step.</h2>{review_stack(2)}</div></div></section>
'''
    desc = 'Outdoor project guides from Terramorph for drainage, patios, native landscaping, seasonal cleanups, mulch, rock, and Northwest Ohio property work.'
    (root/'guides.html').write_text(page('Outdoor Project Guides for Northwest Ohio | Terramorph', desc, body, schema_for('guides.html','Outdoor Project Guides',desc, DEFAULT_FAQS)))

def guide_page(g):
    section_html = ''.join(f'<section class="guide-content-block"><h2>{h}</h2><p>{txt}</p></section>' for h,txt in g['sections'])
    related_items = [x for x in GUIDES if x['file'] != g['file'] and (x['service'] == g['service'] or x['category'].split()[0] == g['category'].split()[0])][:3]
    related = ''.join(guide_card(x) for x in related_items)
    body = f'''
<section class="page-hero premium-page-hero guide-detail-hero">
  <div class="page-hero-image"><img src="assets/{g['image']}" alt="{g['title']}"></div><div class="hero-overlay"></div>
  <div class="container page-hero-content"><p class="crumb"><a href="index.html">Home</a> / <a href="guides.html">Guides</a> / {g['category']}</p><p class="eyebrow light">{g['category']}</p><h1>{g['title']}</h1><p>{g['short']}</p><div class="cta-row"><a class="btn btn-gold" href="contact.html">{g['cta']}</a><a class="btn btn-outline-light" href="tel:{TEL}">Call {PHONE}</a></div></div>
</section>
{trust_band()}
<section class="section guide-detail-section"><div class="container guide-layout"><article class="guide-article"><p class="guide-kicker">Serving Wood County, Lucas County, Toledo, Perrysburg, and Northwest Ohio.</p>{section_html}</article><aside class="guide-sidebar"><div class="guide-cta-card"><p class="eyebrow">Free estimate</p><h2>Want this looked at on your property?</h2><p>Send photos, city, timeline, and what is frustrating you. Terramorph can review the right next step.</p><a class="btn btn-primary" href="contact.html">Request Quote</a><a class="btn btn-quiet" href="tel:{TEL}">Call {PHONE}</a></div></aside></div></section>
{faq_section(g['faqs'])}
<section class="section work-section"><div class="container section-heading compact"><p class="eyebrow">Related guides</p><h2>Keep researching the right next step.</h2></div><div class="container guide-grid related-guides">{related}</div></section>
<section class="section quote-section"><div class="container quote-grid">{quote_form(g['cta'])}<div class="cta-proof"><p class="eyebrow">Why Terramorph</p><h2>Local drainage, landscape, patio, cleanup, and maintenance work built around Northwest Ohio conditions.</h2>{review_stack(2)}</div></div></section>
'''
    (root/g['file']).write_text(page(g['title'] + ' | Terramorph', g['short'], body, guide_schema(g)))

def write_guides():
    guides_hub()
    for g in GUIDES:
        guide_page(g)

write_guides()


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


CITY_SERVICE_PAGES = [
    {'file':'landscaping-toledo-ohio.html','city':'Toledo','service':'Landscape Design','keyword':'landscaping in Toledo, Ohio','headline':'Landscape design, beds, cleanups, and outdoor upgrades for Toledo properties.','lead':'Terramorph helps Toledo homeowners and property owners clean up curb appeal, rebuild tired beds, plan better outdoor spaces, and connect landscaping with drainage, patios, lighting, and maintenance.','image':'real-entry.webp?v=3.14','angle':'Toledo properties can vary block by block: mature trees, older drainage paths, compacted lawn areas, curb appeal needs, and tight access all affect the plan.','cta':'Request a Toledo Landscaping Estimate'},
    {'file':'drainage-solutions-toledo-ohio.html','city':'Toledo','service':'Drainage Solutions','keyword':'drainage solutions in Toledo, Ohio','headline':'Drainage solutions for wet yards, runoff, and standing water in Toledo.','lead':'For Toledo yards with soggy grass, low spots, roof runoff, or water moving toward hardscapes and foundations, Terramorph reviews the property and recommends practical ways to route water.','image':'real-drainage.webp','angle':'Older lots, clay soil, flat grading, alley/driveway runoff, and heavy Northwest Ohio rain make drainage diagnosis important before installing a one-size-fits-all drain.','cta':'Request a Toledo Drainage Estimate'},
    {'file':'paver-patios-toledo-ohio.html','city':'Toledo','service':'Paver Patios and Hardscapes','keyword':'paver patios in Toledo, Ohio','headline':'Paver patios, walkways, and outdoor living upgrades for Toledo homes.','lead':'Terramorph plans patio and walkway projects around base prep, drainage, transitions, access, and the way the backyard needs to work for hosting, grilling, and daily use.','image':'real-patio.webp?v=3.14','angle':'Toledo patio work needs to account for freeze-thaw movement, drainage, established yards, tight access, and how water leaves the house and hardscape.','cta':'Request a Toledo Patio Estimate'},
    {'file':'landscaping-perrysburg-ohio.html','city':'Perrysburg','service':'Landscape Design','keyword':'landscaping in Perrysburg, Ohio','headline':'Finished landscape design and installation for Perrysburg homes.','lead':'Terramorph helps Perrysburg homeowners upgrade curb appeal, beds, patios, lighting, drainage, and maintenance so the whole property feels planned instead of patched together.','image':'real-entry.webp?v=3.14','angle':'Perrysburg properties often need a cleaner full-property plan: front beds, backyard living, drainage awareness, mulch or rock decisions, plant selection, and ongoing upkeep.','cta':'Request a Perrysburg Landscaping Estimate'},
    {'file':'drainage-solutions-perrysburg-ohio.html','city':'Perrysburg','service':'Drainage Solutions','keyword':'drainage solutions in Perrysburg, Ohio','headline':'Perrysburg drainage solutions for standing water, clay soil, and runoff.','lead':'Terramorph reviews grading, low spots, downspouts, lawn saturation, patio runoff, and discharge options before recommending drainage work for Perrysburg properties.','image':'real-drainage.webp','angle':'Flat lots, clay-heavy soil, new construction grading, and heavy rain can leave Perrysburg yards wet longer than expected if water is not routed intentionally.','cta':'Request a Perrysburg Drainage Estimate'},
    {'file':'paver-patios-perrysburg-ohio.html','city':'Perrysburg','service':'Paver Patios and Hardscapes','keyword':'paver patios in Perrysburg, Ohio','headline':'Paver patios and outdoor living spaces for Perrysburg backyards.','lead':'Terramorph builds patio and hardscape plans around how the family will use the space, how water moves, and how the patio connects to lawn, beds, steps, lighting, and walkways.','image':'real-patio.webp?v=3.14','angle':'A patio in Perrysburg should be designed for Northwest Ohio weather, proper base prep, clean edges, drainage, and finished outdoor living rather than just a surface upgrade.','cta':'Request a Perrysburg Patio Estimate'},
    {'file':'landscaping-maumee-ohio.html','city':'Maumee','service':'Landscape Design','keyword':'landscaping in Maumee, Ohio','headline':'Landscape design, beds, and property upgrades for Maumee homes.','lead':'Terramorph helps Maumee properties look cleaner, drain better, and feel more intentional with landscape design, bed installation, mulch, rock, lighting, patios, cleanups, and maintenance.','image':'real-entry.webp?v=3.14','angle':'Maumee properties often benefit from practical upgrades that improve curb appeal while respecting mature neighborhoods, existing trees, soil conditions, and drainage paths.','cta':'Request a Maumee Landscaping Estimate'},
    {'file':'drainage-solutions-maumee-ohio.html','city':'Maumee','service':'Drainage Solutions','keyword':'drainage solutions in Maumee, Ohio','headline':'Drainage solutions for Maumee yards with standing water or runoff problems.','lead':'Terramorph can review wet areas, downspout routing, grading, discharge options, and surrounding landscape conditions before recommending drainage work.','image':'real-drainage.webp','angle':'Maumee drainage projects can involve mature lots, clay soil, roof runoff, older grading, and water paths around drives, patios, garages, and property lines.','cta':'Request a Maumee Drainage Estimate'},
    {'file':'paver-patios-maumee-ohio.html','city':'Maumee','service':'Paver Patios and Hardscapes','keyword':'paver patios in Maumee, Ohio','headline':'Paver patios, walkways, and hardscape upgrades for Maumee backyards.','lead':'Terramorph helps Maumee homeowners turn outdoor areas into usable patios, walkways, seating spaces, and finished backyards with drainage and base prep considered first.','image':'real-patio.webp?v=3.14','angle':'Patio work in Maumee should account for established yards, water movement, freeze-thaw cycles, access, transitions, and long-term maintenance around the hardscape.','cta':'Request a Maumee Patio Estimate'},
]
CITY_LINKS = {'Toledo':'landscaping-toledo-ohio.html','Perrysburg':'landscaping-perrysburg-ohio.html','Maumee':'landscaping-maumee-ohio.html'}

def city_service_card(item):
    return f'''<a class="guide-card city-service-card" href="{item['file']}"><span>{item['city']} &middot; {item['service']}</span><h3>{item['headline']}</h3><p>{item['lead']}</p><b>Open local page &rarr;</b></a>'''

def city_service_schema(item):
    faqs = [(f'Does Terramorph offer {item["service"].lower()} in {item["city"]}?', f'Yes. Terramorph serves {item["city"]} and nearby Wood and Lucas County areas with {item["service"].lower()} and related outdoor property work.'),('Can I request a free estimate by phone?', f'Yes. Call Terramorph at {PHONE} with the service need, property details, photos if available, and timeline.'),('What other services can be included?', 'Terramorph can review related needs such as drainage, patios, beds, lighting, cleanups, maintenance, mulch, rock, trimming, and property improvements.')]
    desc = f"Terramorph provides {item['keyword']} for homeowners and property owners, with phone-first free estimates."
    return schema_for(item['file'], item['headline'] + ' | Terramorph', desc, faqs, item['service'])

def city_service_page(item):
    related = ''.join(city_service_card(x) for x in CITY_SERVICE_PAGES if x['city'] == item['city'] and x['file'] != item['file'])
    service_related = ''.join(city_service_card(x) for x in CITY_SERVICE_PAGES if x['service'] == item['service'] and x['file'] != item['file'])
    faqs = [(f'Does Terramorph serve {item["city"]}?', f'Yes. Terramorph serves {item["city"]}, Wood County, Lucas County, and surrounding Northwest Ohio communities.'),(f'Can I get a free {item["service"].lower()} estimate in {item["city"]}?', f'Yes. Call Terramorph at {PHONE} to request a free estimate and confirm the best next step.'),('Can photos be included with the request?', 'Yes. Photos are helpful for drainage, patios, beds, cleanups, and landscape projects because they help the team understand the property before follow-up.')]
    body = f'''
<section class="page-hero premium-page-hero city-service-hero">
  <div class="page-hero-image"><img src="assets/{item['image']}" alt="Terramorph {item['service']} in {item['city']}, Ohio"></div><div class="hero-overlay"></div>
  <div class="container page-hero-content"><p class="crumb"><a href="index.html">Home</a> / <a href="service-areas.html">Service Areas</a> / {item['city']} {item['service']}</p><p class="eyebrow light">{item['keyword']}</p><h1>{item['headline']}</h1><p>{item['lead']}</p><div class="cta-row"><a class="btn btn-gold" href="#quote">{item['cta']}</a><a class="btn btn-outline-light" href="tel:{TEL}">Call {PHONE}</a></div></div>
</section>
{trust_band()}
<section class="section"><div class="container local-grid"><div><p class="eyebrow">Local fit</p><h2>{item['city']} outdoor work needs local judgment.</h2><p>{item['angle']}</p><p>Terramorph positions the estimate around the actual property: grade, water movement, access, materials, maintenance expectations, budget, and the outcome the owner wants.</p></div><div class="authority-list"><div><b>Property review</b><span>Service need, city, address, photos, timeline, and visible site conditions.</span></div><div><b>Connected services</b><span>Drainage, patios, beds, lighting, cleanups, and maintenance can be scoped together when it makes sense.</span></div><div><b>Northwest Ohio conditions</b><span>Clay soil, flat lots, freeze-thaw, and heavy rain are considered before recommendations.</span></div><div><b>Fast follow-up</b><span>Quote requests include the details the team needs to respond with the right next step.</span></div></div></div></section>
<section class="section work-section"><div class="container section-heading compact"><p class="eyebrow">Related {item['city']} services</p><h2>Other outdoor work Terramorph can review nearby.</h2></div><div class="container guide-grid">{related}</div></section>
{faq_section(faqs)}
<section class="section quote-section"><div class="container quote-grid">{quote_form(item['cta'])}<div class="cta-proof"><p class="eyebrow">Fast estimate path</p><h2>Send photos, timeline, and service details in one secure request.</h2>{review_stack(2)}</div></div></section>
<section class="section guide-index-section"><div class="container section-heading compact"><p class="eyebrow">More local pages</p><h2>Compare by service area and project type.</h2></div><div class="container guide-grid related-guides">{service_related}</div></section>
'''
    desc = f"{item['headline']} Phone-first free estimates from Terramorph for {item['city']} and Northwest Ohio properties."
    (root/item['file']).write_text(page(item['headline'] + ' | Terramorph', desc, body, city_service_schema(item)))

def write_city_service_pages():
    for item in CITY_SERVICE_PAGES:
        city_service_page(item)

write_city_service_pages()

areas = f'''
<section class="page-hero premium-page-hero">
  <div class="page-hero-image"><img src="assets/real-lawn-pool.webp" alt="Northwest Ohio lawn and landscape maintenance"></div><div class="hero-overlay"></div>
  <div class="container page-hero-content"><p class="crumb"><a href="index.html">Home</a> / Local Expertise</p><p class="eyebrow light">Northwest Ohio authority</p><h1>Licensed and insured local expertise for Perrysburg, Toledo, Wood County, and Lucas County.</h1><p>Terramorph serves residential, commercial, and industrial properties with trained team members who understand drainage diagnosis, hardscape durability, plant health, snow response, and Northwest Ohio soil and weather conditions.</p><div class="cta-row"><a class="btn btn-gold" href="contact.html">Check My Property</a><a class="btn btn-outline-light" href="tel:{TEL}">Call {PHONE}</a></div></div>
</section>
{trust_band()}
{local_authority()}
{official_business_info()}
<section class="section guide-index-section"><div class="container section-heading compact"><p class="eyebrow">Local service pages</p><h2>Estimate information by city and project type.</h2><p>Use these pages to review the most relevant Terramorph services for your city, then call Terramorph for a free estimate.</p></div><div class="container guide-grid">{''.join(city_service_card(x) for x in CITY_SERVICE_PAGES)}</div></section>
<section class="section"><div class="container section-heading compact"><p class="eyebrow">Priority service areas</p><h2>Focused on Northwest Ohio.</h2></div><div class="container areas">{''.join(f'<a class="area" href="{CITY_LINKS.get(x, "contact.html")}">{x}<span>Design • patios • drainage • lighting</span></a>' for x in ['Perrysburg','Toledo','Maumee','Sylvania','Rossford','Oregon','Waterville','Whitehouse','Monclova','Ottawa Hills','Bowling Green','Wood County','Lucas County','Northwest Ohio'])}</div></section>
<section class="section quote-section"><div class="container quote-grid">{quote_form('Get a Local Property Estimate')}<div class="cta-proof"><p class="eyebrow">Local estimates</p><h2>Tell us where you are and what you need done.</h2><p>Whether it is drainage, design, a patio, cleanup, mowing, mulch, trimming, or bed maintenance, Terramorph can point you toward the right next step.</p></div></div></section>
'''
areas_desc = 'Terramorph serves Wood and Lucas County with Northwest Ohio-specific expertise for landscaping, patios, drainage, lighting, cleanups, lawn maintenance, and property work.'
(root/'service-areas.html').write_text(page('Serving Wood and Lucas County | Terramorph Local Expertise', areas_desc, areas, schema_for('service-areas.html', 'Serving Wood and Lucas County', areas_desc)))

contact = f'''
<section class="page-hero premium-page-hero contact-hero">
  <div class="page-hero-image"><img src="assets/real-hero.webp" alt="Terramorph outdoor project for quote request"></div><div class="hero-overlay"></div>
  <div class="container page-hero-content"><p class="crumb"><a href="index.html">Home</a> / Quote</p><p class="eyebrow light">Fast project quote</p><h1>Tell Terramorph what you want built, fixed, or transformed.</h1><p>Call for lawn care, landscape maintenance, seasonal cleanup, pruning, mulch, plant installation, patios, retaining walls, drainage, lighting, concrete, power washing, hauling, snow removal, or other property work.</p><div class="cta-row"><a class="btn btn-gold" href="#quote">Start Quote</a><a class="btn btn-outline-light" href="tel:{TEL}">Call {PHONE}</a></div></div>
</section>
<section class="section quote-section"><div class="container quote-grid">{quote_form('Request My Terramorph Quote')}<div class="cta-proof"><p class="eyebrow">What happens next</p><h2>Simple free estimates for projects and maintenance.</h2><div class="process-timeline"><div><b>1. Request</b><span>Submit the short form or call directly.</span></div><div><b>2. Review</b><span>Terramorph reviews service, city, photos, and timeline.</span></div><div><b>3. Estimate</b><span>Book the site visit and prepare a clear scope.</span></div></div>{review_stack()}</div></div></section>
{trust_band()}
'''
contact_desc = 'Request a free estimate from Terramorph for landscape design, patios, drainage, outdoor lighting, lawn maintenance, seasonal cleanups, and property work.'
(root/'contact.html').write_text(page('Request a Free Outdoor Project Estimate | Terramorph', contact_desc, contact, schema_for('contact.html', 'Request a Free Estimate', contact_desc)))

quote_desc = 'Request a free Terramorph quote online for landscaping, patios, drainage, outdoor lighting, cleanups, lawn maintenance, snow removal, and outdoor property work in Northwest Ohio.'
quote_page = f'''
<section class="page-hero premium-page-hero compact-hero quote-request-hero">
  <div class="hero-overlay"></div>
  <div class="container page-hero-content">
    <p class="crumb"><a href="index.html">Home</a> / Request Quote</p>
    <p class="eyebrow light">Free estimate request</p>
    <h1>Tell Terramorph what needs built, fixed, or cleaned up.</h1>
    <p>Submit the secure Jobber request form so the project details go straight into Terramorph's CRM for follow-up.</p>
    <div class="cta-row"><a class="btn btn-gold" href="#request-form">Start Request</a><a class="btn btn-outline-light" href="tel:{TEL}">Call {PHONE}</a></div>
  </div>
</section>
<section class="section quote-panel jobber-quote-panel quote-request-section" id="request-form" aria-labelledby="quote-title">
  <div class="container quote-request-layout">
    <div class="quick-lead-card quote-request-card">
      <div class="quick-lead-copy">
        <p class="eyebrow light">Project details</p>
        <h2 id="quote-title">Request a free outdoor project estimate.</h2>
        <p>Use the secure Terramorph Jobber request form below. New requests go directly into the CRM so the team can follow up with the right service, city, photos, and timeline.</p>
        <div class="quick-lead-proof"><span>★★★★★ 200+ Google Reviews</span><span>Licensed + insured</span><span>Wood + Lucas County</span></div>
      </div>
      <div class="jobber-embed-wrap" aria-label="Terramorph Jobber quote request form">
        <div id="{JOBBER_CLIENTHUB_ID}">
          <script src="https://d3ey4dbjkt2f6s.cloudfront.net/assets/static_link/work_request_embed_snippet.js" clienthub_id="{JOBBER_CLIENTHUB_ID}" form_url="{JOBBER_FORM_URL}"></script>
        </div>
      </div>
      <div class="jobber-fallback">
        <p>If the embedded form does not load, open the secure Jobber request form directly.</p>
        <a class="btn btn-gold" href="{JOBBER_DIRECT_URL}" target="_blank" rel="noopener">Open Jobber Quote Form</a>
        <a class="btn btn-outline-light" href="tel:{TEL}">Call {PHONE}</a>
      </div>
    </div>
    <div class="quote-request-copy">
      <p class="eyebrow">Before Terramorph follows up</p>
      <h2>Photos, measurements, and access notes help speed up the estimate.</h2>
      <div class="authority-list">
        <div><b>1. Describe the problem</b><span>What you want fixed, built, cleaned, maintained, or priced.</span></div>
        <div><b>2. Share location</b><span>City, address, or nearest cross street for service-area planning.</span></div>
        <div><b>3. Add timeline</b><span>ASAP, this month, 1-3 months, or planning ahead.</span></div>
        <div><b>4. Add photos in Jobber</b><span>The CRM request keeps photos and project notes organized for follow-up.</span></div>
      </div>
    </div>
  </div>
</section>
{trust_band()}
'''
(root/'quote.html').write_text(page('Request a Free Quote | Terramorph LLC', quote_desc, quote_page, schema_for('quote.html', 'Request a Free Quote', quote_desc)))

privacy = f'''
<section class="page-hero premium-page-hero compact-hero">
  <div class="hero-overlay"></div>
  <div class="container page-hero-content">
    <p class="crumb"><a href="index.html">Home</a> / Privacy Policy</p>
    <p class="eyebrow light">Privacy Policy</p>
    <h1>Terramorph Privacy Policy</h1>
    <p>How Terramorph LLC collects, uses, and protects information submitted through this website, phone calls, and quote requests.</p>
  </div>
</section>
<section class="section legal-page">
  <div class="container narrow-copy">
    <p><strong>Last updated:</strong> June 9, 2026</p>
    <h2>Information we collect</h2>
    <p>Terramorph may collect information you choose to provide when requesting an estimate, calling, emailing, or using our online quote form. This can include your name, phone number, email address, property address, project details, service needs, preferred timeline, photos, and any notes you submit.</p>
    <h2>How we use information</h2>
    <p>We use submitted information to respond to quote requests, schedule site visits, prepare estimates, communicate about projects, improve our services, and keep accurate customer and project records.</p>
    <h2>Quote forms and third-party tools</h2>
    <p>Terramorph may use business tools to manage scheduling, customer communication, and project follow-up. Information you provide by phone or through future website features may be processed by service providers so Terramorph can respond and manage the request.</p>
    <h2>Website analytics and advertising</h2>
    <p>This website may use standard analytics, advertising, pixels, cookies, or tracking links to understand website traffic, measure marketing performance, and improve future advertising. These tools may collect browser, device, page visit, referral, and interaction information.</p>
    <h2>Information sharing</h2>
    <p>Terramorph does not sell your personal information. We may share information with service providers that help operate the website, process quote requests, manage customer communication, provide advertising analytics, or perform business operations. We may also share information when required by law or to protect our business, customers, or property.</p>
    <h2>Data security</h2>
    <p>We use reasonable administrative and technical safeguards to protect information. No website, email, or online form can guarantee perfect security, so avoid submitting highly sensitive information through website forms.</p>
    <h2>Your choices</h2>
    <p>You can request updates, corrections, or removal of your contact information from active marketing lists by contacting Terramorph. Some records may be retained when needed for business, legal, accounting, or project-history purposes.</p>
    <h2>Contact</h2>
    <p>For privacy questions, call <a href="tel:{TEL}">{PHONE}</a>.</p>
  </div>
</section>
'''
privacy_desc = 'Privacy Policy for Terramorph LLC website visitors, quote requests, analytics, advertising, and customer communication.'
(root/'privacy.html').write_text(page('Privacy Policy | Terramorph LLC', privacy_desc, privacy, schema_for('privacy.html', 'Privacy Policy', privacy_desc)))



terms = f'''
<section class="page-hero premium-page-hero compact-hero">
  <div class="hero-overlay"></div>
  <div class="container page-hero-content">
    <p class="crumb"><a href="index.html">Home</a> / Terms</p>
    <p class="eyebrow light">Website terms</p>
    <h1>Terramorph website terms</h1>
    <p>Plain-language terms for using this website, requesting estimates, and following links to third-party tools.</p>
  </div>
</section>
<section class="section legal-page">
  <div class="container narrow-copy">
    <p><strong>Last updated:</strong> June 29, 2026</p>
    <h2>Website use</h2>
    <p>This website is provided by Terramorph LLC to help property owners learn about services, view project information, and request estimates.</p>
    <h2>Estimates and service requests</h2>
    <p>Submitting a quote request does not create a service agreement. Project scope, timing, pricing, access, materials, and availability are confirmed directly by Terramorph before work begins.</p>
    <h2>Project information</h2>
    <p>Service descriptions, photos, guides, and project examples are general information. Outdoor work depends on site conditions including grade, drainage, soil, access, weather, existing materials, and customer goals.</p>
    <h2>Third-party tools and links</h2>
    <p>The website may link to Google, BBB, Facebook, Instagram, Yelp, Nextdoor, and other third-party platforms. Those platforms operate under their own terms and privacy practices.</p>
    <h2>No guarantee from website content alone</h2>
    <p>Terramorph aims to keep the website accurate, but final recommendations require property-specific review and direct communication with the team.</p>
    <h2>Contact</h2>
    <p>Questions about these terms can be handled by phone at <a href="tel:{TEL}">{PHONE}</a> or through the <a href="contact.html">Terramorph quote request page</a>.</p>
  </div>
</section>
'''
terms_desc = 'Website terms for Terramorph LLC visitors, quote requests, third-party links, and service information.'
(root/'terms.html').write_text(page('Terms | Terramorph LLC', terms_desc, terms, schema_for('terms.html', 'Terms', terms_desc)))

review_notes_body = '''<section class="section"><div class="container review-doc"><p class="eyebrow">V3.49 final optimization summary</p><h1>Terramorph local SEO, citation, and conversion response</h1><h2>What changed</h2><ul><li>Added official business information blocks so Google, Meta, and directories have one consistent NAP/entity source.</li><li>Strengthened LocalBusiness/LandscapingBusiness/HomeAndConstructionBusiness schema, sameAs links, contact point, service areas, categories, and service offer catalog.</li><li>Added canonical, Open Graph, Twitter card, and absolute social image metadata across generated pages.</li><li>Kept high-intent quote CTAs, phone-click tracking, city/service pages, proof, reviews, and local service-area copy visible near conversion points.</li></ul><p><a class="btn btn-primary" href="index.html">Open homepage</a></p></div></section>'''
review_notes_desc = 'Summary of Terramorph V3.49 local SEO, AI visibility, local authority, conversion, and technical optimization improvements.'
(root/'review-notes.html').write_text(page('V3.49 Final Optimization Notes | Terramorph', review_notes_desc, review_notes_body, schema_for('review-notes.html', 'V3.49 Final Optimization Notes', review_notes_desc)))

readme = '''# Terramorph V3.49 Website

Audit-response build focused on local SEO, Google/Meta entity clarity, NAP consistency, citation cleanup support, high-intent service-area landing pages, and phone-first conversion tracking.

## Open
- `index.html` — homepage
- `landscape-design.html` — landscape design landing page
- `paver-patios-hardscapes.html` — patio/hardscape landing page
- `drainage-solutions.html` — drainage landing page
- `guides.html` — Outdoor Project Guides SEO hub
- eight long-form guide pages for drainage, native landscaping, patios, cleanups, and landscape beds
- `projects.html` — project proof hub
- `about.html` — About page
- `service-areas.html` — local service area hub
- nine city/service pages for Toledo, Perrysburg, and Maumee landscaping, drainage, and patios
- `contact.html` — phone-first quote request page
- `privacy.html` — privacy policy
- `review-notes.html` — summary of changes

## V3.49 priorities implemented
- Official NAP/entity block for citation tools and directory cleanup
- Stronger LocalBusiness, LandscapingBusiness, HomeAndConstructionBusiness, service, FAQ, breadcrumb, and offer catalog schema
- Canonical URLs, Open Graph, Twitter cards, and absolute social preview images across generated pages
- SameAs signals for BBB, Yelp, and Nextdoor where public profiles are visible
- Fewer heavy boxed/card sections
- Reviews, trust, Google reviews, BBB Membership, license/insurance, phone, and free estimate CTAs
- Sitewide NAP consistency note in footer and official business information section
- Accessibility improvements
- Added an About page explaining the local, diagnosis-first approach
- Added Outdoor Project Guides hub and eight SEO guide pages with FAQ/article schema and quote CTAs
- Connected quote requests to phone-first call CTAs
- Added city/service pages for Toledo, Perrysburg, and Maumee core services
'''
(root/'README.md').write_text(readme)
home_desc = 'Terramorph provides landscape design, paver patios, drainage, outdoor lighting, seasonal cleanups, lawn maintenance, and property work in Wood and Lucas County.'
(root/'index.html').write_text(page('Landscape Design, Patios, Drainage & Outdoor Work | Terramorph', home_desc, home, schema_for('index.html', 'Terramorph', home_desc, DEFAULT_FAQS)))

thank_you = f"""
<section class="page-hero premium-page-hero compact-hero"><div class="hero-overlay"></div><div class="container page-hero-content"><p class="eyebrow light">Quote request received</p><h1>Thanks — Terramorph has your request.</h1><p>If the project is urgent, call now so the next step can be handled faster.</p><div class="cta-row"><a class="btn btn-gold" href="tel:{TEL}">Call {PHONE}</a><a class="btn btn-outline-light" href="index.html">Back to Home</a></div></div></section>
<section class="section"><div class="container local-grid"><div><p class="eyebrow">What happens next</p><h2>Terramorph reviews your property details, service need, timeline, and photos if provided.</h2><p>You can speed up the estimate by having photos, property address, and a clear description ready.</p></div><div class="authority-list"><div><b>1. Review</b><span>Project type, location, access, timeline, and visible property conditions.</span></div><div><b>2. Follow-up</b><span>Terramorph confirms the best next step by phone.</span></div><div><b>3. Estimate</b><span>A site review or quote path is scheduled based on the project.</span></div></div></div></section>
"""
(root/'thank-you.html').write_text(page('Quote Request Received | Terramorph', 'Thank-you page for Terramorph quote requests in Wood and Lucas County.', thank_you, schema_for('thank-you.html', 'Quote Request Received', 'Thank-you page for Terramorph quote requests.')))

def write_static_seo_files():
    pages = ['index.html','quote.html','landscape-design.html','paver-patios-hardscapes.html','drainage-solutions.html','outdoor-lighting.html','lawn-maintenance.html','seasonal-cleanups.html','guides.html'] + [g['file'] for g in GUIDES] + [p['file'] for p in CITY_SERVICE_PAGES] + ['projects.html','about.html','service-areas.html','contact.html','privacy.html','terms.html','lp-patios.html','lp-drainage.html','lp-landscape-design.html','lp-outdoor-lighting.html']
    sitemap = '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
    priorities = {'index.html':'1.0','quote.html':'0.95','contact.html':'0.9','drainage-solutions.html':'0.9','paver-patios-hardscapes.html':'0.9','landscape-design.html':'0.9'}
    for page_name in pages:
        loc = BASE_URL + ('/' if page_name == 'index.html' else '/' + page_name)
        sitemap += f'  <url><loc>{loc}</loc><changefreq>monthly</changefreq><priority>{priorities.get(page_name, "0.7")}</priority></url>\n'
    sitemap += '</urlset>\n'
    (root/'sitemap.xml').write_text(sitemap)
    (root/'robots.txt').write_text(f'User-agent: *\nAllow: /\nSitemap: {BASE_URL}/sitemap.xml\n')

def post_process_html():
    for path in root.glob('*.html'):
        html = path.read_text()
        url = BASE_URL + ('/' if path.name == 'index.html' else '/' + path.name)
        html = html.replace('<meta property="og:image" content="assets/real-hero.webp">', f'<meta property="og:image" content="{BASE_URL}/assets/real-hero.webp">\n  <meta property="og:url" content="{url}">\n  <meta name="twitter:card" content="summary_large_image">\n  <link rel="canonical" href="{url}">')
        html = html.replace('Request a Outdoor Lighting Quote', 'Request an Outdoor Lighting Quote')
        html = html.replace('href="contact.html#quote"', 'href="quote.html"')
        if path.name != 'contact.html':
            html = html.replace('href="contact.html"', 'href="quote.html"')
        html = html.replace('href="#quote"', 'href="quote.html"')
        html = html.replace('<script src="app.js"></script>', '<script src="app.js?v=3.51"></script>')
        html = html.replace('<script src="app.js?v=3.50"></script>', '<script src="app.js?v=3.51"></script>')
        path.write_text(html)

write_static_seo_files()
post_process_html()
try:
    import seo_expansion
    seo_expansion.generate(globals())
    import authority_pass
    authority_changed = authority_pass.generate(globals())
    post_process_html()
    print(f'wrote V3.49 local SEO/ad authority expansion pages ({len(authority_changed)} authority updates)')
except Exception as exc:
    raise RuntimeError('seo expansion generation failed') from exc

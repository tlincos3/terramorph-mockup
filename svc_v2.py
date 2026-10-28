"""Phase 2b (2026-10): rebuilt layouts for the 7 main service pages.

The legacy generators still write each service page first (title, meta, schema,
tracking tags, and every heading/paragraph Google already indexes). This module
then re-lays out the <main> content in the v2 design without dropping any of
that copy: hero, quick answers, problem -> outcome, photo-led chapters, the
process timeline, real-work gallery, reviews, FAQ, related reading, local
pages, and an embedded quote form. Sections it does not recognise are kept
as-is (they still get the tm-skin styling).
"""
import re
from pathlib import Path

SERVICES = {
    # 'photos' key = the SERVICE_PHOTOS set in build_pages.py (one source of truth, 2026-10-26).
    'landscape-design.html': {'name': 'Landscape Design', 'city_prefix': 'landscaping-', 'photos': 'design'},
    'paver-patios-hardscapes.html': {'name': 'Paver Patios and Hardscapes', 'city_prefix': 'paver-patios-', 'photos': 'patios'},
    'drainage-solutions.html': {'name': 'Drainage Solutions', 'city_prefix': 'drainage-solutions-', 'photos': 'drainage'},
    'outdoor-lighting.html': {'name': 'Outdoor Lighting', 'city_prefix': None, 'photos': 'lighting'},
    'lawn-maintenance.html': {'name': 'Lawn Maintenance', 'city_prefix': 'lawn-maintenance-', 'photos': 'lawn'},
    'seasonal-cleanups.html': {'name': 'Seasonal Cleanups', 'city_prefix': 'spring-fall-cleanups-', 'photos': 'fall-cleanup'},
    'snow-removal.html': {'name': 'Snow Removal', 'city_prefix': 'snow-removal-', 'photos': 'snow'},
    # Sustainable-landscape pages (2026-10-27). Empty photo sets: no Terramorph job
    # photos yet, so no "our crews built" gallery. Chapter photos are credited
    # reference photos from sustainable.py (CHAPTER_MEDIA), never shown as our work.
    'permaculture-design-toledo-ohio.html': {'name': 'Permaculture Design', 'city_prefix': None, 'photos': 'permaculture'},
    'native-landscaping-toledo-ohio.html': {'name': 'Native Landscaping', 'city_prefix': None, 'photos': 'native'},
    'food-forest-edible-landscaping-toledo-ohio.html': {'name': 'Food Forests and Edible Landscaping', 'city_prefix': None, 'photos': 'edible'},
    'natural-swimming-pools-ponds-ohio.html': {'name': 'Natural Swimming Pools and Ponds', 'city_prefix': None, 'photos': 'water'},
}


# Extra chapters for pages whose legacy copy has no detail sections. Only
# services already listed on the site (SERVICE_GROUPS) - no prices, no promises.
EXTRA = {
    'outdoor-lighting.html': [
        {'eyebrow': 'What we light', 'h2': 'Paths, entries, patios, and the trees that frame the house.',
         'paras': '<p>Low-voltage lighting is planned around how you move through the property at night and what you want people to notice from the street.</p>',
         'items': [('Path lighting', 'Walkways and steps lit so family and guests can see where they are going.'),
                   ('Accent lighting', 'Trees, stone, and plantings lit to give the house depth after dark.'),
                   ('Patio and entertaining areas', 'Light for the outdoor spaces you actually use at night.'),
                   ('Entry lighting', 'Front doors and drives that look welcoming and are easy to find.'),
                   ('Security visibility', 'Fewer dark corners around the house, garage, and side yards.')]},
        {'eyebrow': 'Planned with the yard', 'h2': 'Lighting works best when it is planned with the patio and beds.',
         'paras': '<p>When lighting is part of a bigger project, wire runs go in before pavers and plants, so nothing gets torn up later. It can also be added to an existing yard.</p>',
         'checks': ['Fixtures placed for the view from the street and from inside', 'Wire runs planned around patios, beds, and walkways', 'Added to new projects or existing landscapes']},
    ],
    'lawn-maintenance.html': [
        {'eyebrow': 'What a visit covers', 'h2': 'Mowing, edging, trimming, and the details that make a yard look kept.',
         'paras': '<p>Recurring service for homes and businesses across Wood and Lucas County, on a set schedule.</p>',
         'items': [('Mowing', 'Cut at the right height for the season, with clean striping.'),
                   ('Edging', 'Sharp lines along walks, drives, and beds.'),
                   ('Trimming', 'Around fences, trees, and everything the mower cannot reach.'),
                   ('Weeding and bed upkeep', 'Beds kept clean between bigger projects.'),
                   ('Commercial maintenance', 'Recurring service for business properties too.')]},
        {'eyebrow': 'Through the year', 'h2': 'One crew for the lawn in every season.',
         'paras': '<p>The same team that mows can handle the seasonal work, so the property is looked after from spring to snow.</p>',
         'checks': ['Fall core aeration and overseeding for thin lawns', 'Spring and fall cleanups', 'Mulch and bed refreshes', 'Snow removal once winter hits']},
    ],
    'snow-removal.html': [
        {'eyebrow': 'What we cover', 'h2': 'Driveways, walks, and lots cleared so you can get where you need to go.',
         'paras': '<p>Winter service for homes, businesses, and properties that need safe access when Northwest Ohio weather hits.</p>',
         'items': [('Residential driveways', 'Plowed so you can get out in the morning.'),
                   ('Walkways', 'Sidewalks, steps, and entries cleared.'),
                   ('Commercial lots', 'Parking lots and access lanes for businesses.'),
                   ('Ice management', 'Salting for slick walks and drives.'),
                   ('Winter response planning', 'A plan for your property before the storms start.')]},
        {'eyebrow': 'Plan ahead', 'h2': 'Get on the schedule before the first storm.',
         'paras': '<p>Booking in the fall means the property is already covered when the first snow comes, instead of scrambling for a plow that morning. Residential and commercial seasonal sign-up is open now.</p>',
         'checks': ['Homes and businesses', 'Driveways, walks, and lots', 'Wood and Lucas County'],
         'ctas': ['<a class="btn btn-gold" href="snow-removal-signup.html">Sign up for winter service</a>']},
    ],
}

# Direct answer under each service page's hero (what AI assistants and Google
# quote first). Only facts the site already states.
ANSWERS = {
    'landscape-design.html': 'Terramorph designs and installs landscapes for homes and businesses in Perrysburg, Toledo, Maumee, Sylvania, and across Wood and Lucas County, Ohio. You see the plan first: beds, plants picked for clay soil and your sun, edging, rock or mulch, and drainage checked before anything is planted. The same crew then installs it. Estimates are free.',
    'paver-patios-hardscapes.html': 'Terramorph builds paver patios, walkways, fire pit areas, steps, and retaining walls across Wood and Lucas County, Ohio. Every patio starts below the surface with excavation, a compacted base, drainage planning, and solid edge restraint, so the pavers stay flat through Northwest Ohio freeze-thaw winters. The layout is planned around how you will use the space. Estimates are free.',
    'drainage-solutions.html': 'Terramorph fixes standing water, soggy lawns, and runoff for homes in Perrysburg, Toledo, Maumee, and across Wood and Lucas County, Ohio. We find where the water comes from first, then move it with grading, buried downspouts, French drains, catch basins, or dry creek beds, depending on the yard. Clay soil and flat lots are the usual causes here. Estimates are free.',
    'outdoor-lighting.html': 'Terramorph designs and installs low-voltage outdoor lighting for paths, entries, patios, driveways, and trees across Wood and Lucas County, Ohio. Lighting is planned around how you move through the yard at night and what you want seen from the street. It can be added to an existing landscape or built into a new patio or bed. Estimates are free.',
    'lawn-maintenance.html': 'Terramorph provides recurring lawn maintenance for homes and businesses in Perrysburg, Toledo, and across Wood and Lucas County, Ohio: mowing, edging, trimming, weeding, and bed upkeep on a set schedule. The same crew can handle fall core aeration and overseeding, spring and fall cleanups, mulch refreshes, and snow removal. Estimates are free.',
    'seasonal-cleanups.html': 'Terramorph does fall and spring cleanups across Wood and Lucas County, Ohio. A fall cleanup clears leaves from the lawn, beds, and fence lines and hauls them away, cuts back perennials, shapes shrubs, cleans up bed edges, and finishes the lawn before winter. Commercial blowers and full crews handle big wooded lots. Estimates are free.',
    'snow-removal.html': 'Terramorph provides snow removal for homes and businesses in Perrysburg, Toledo, and across Wood and Lucas County, Ohio: plowed driveways, cleared walkways and entries, commercial lots, and salting for ice. Booking before the first storm gets the property covered for the season. Estimates are free.',
}
import sustainable as _sus
ANSWERS.update(_sus.ANSWERS)

ICONS = {
    'walk': '<path d="M12 21s-6-5.6-6-10.5A6 6 0 0 1 18 10.5C18 15.4 12 21 12 21z"/><circle cx="12" cy="10.5" r="2.2"/>',
    'eye': '<path d="M2.5 12S6 5.5 12 5.5 21.5 12 21.5 12 18 18.5 12 18.5 2.5 12 2.5 12z"/><circle cx="12" cy="12" r="3"/>',
    'quote': '<path d="M7 3h7l4 4v14H7z"/><path d="M14 3v4h4M9.5 12h6M9.5 15.5h6M9.5 8.5h2.5"/>',
    'build': '<path d="M14.5 3.5l6 6-2 2-6-6zM12.5 5.5L4 14l2 6 6 2 8.5-8.5"/><path d="M8 16l3-3"/>',
    'check': '<circle cx="12" cy="12" r="9"/><path d="M7.5 12.5l3 3 6-6.5"/>',
}
STEP_ICONS = ['walk', 'eye', 'quote', 'build', 'check', 'check']


def _txt(s):
    return re.sub(r'\s+', ' ', re.sub(r'<[^>]+>', '', s or '')).strip()


def _first(pat, s, flags=re.S):
    m = re.search(pat, s, flags)
    return m.group(1) if m else ''


def _items(block):
    """<div><b>Title</b><span>Body</span></div> pairs inside a list block."""
    return re.findall(r'<div>\s*<b>(.*?)</b>\s*<span>(.*?)</span>', block, re.S)


def _sections(main):
    """Split <main> into top-level <section> blocks (sections never nest here,
    except the quote-panel inside quote-section, which we handle by depth)."""
    out, i = [], 0
    for m in re.finditer(r'<section\b[^>]*>', main):
        pass
    pos = 0
    while True:
        m = re.search(r'<section\b([^>]*)>', main[pos:])
        if not m:
            break
        start = pos + m.start()
        depth, j = 0, start
        for t in re.finditer(r'<(/?)section\b[^>]*>', main[start:]):
            depth += -1 if t.group(1) else 1
            if depth == 0:
                end = start + t.end()
                break
        else:
            end = len(main)
        cls = _first(r'class="([^"]*)"', m.group(1))
        out.append((cls, main[start:end]))
        pos = end
    return out


def _photo(c, name):
    root = c['root']
    for ext in ('webp', 'jpg'):
        if (root / 'assets' / f'{name}.{ext}').exists():
            return f'assets/{name}.{ext}'
    return None


def rebuild(c, name, t):
    cfg = SERVICES[name]
    svc = cfg['name']
    m_open = t.find('<main id="main">')
    m_close = t.find('</main>', m_open)
    if m_open < 0 or m_close < 0:
        return t
    main = t[m_open + len('<main id="main">'):m_close]
    secs = _sections(main)
    photo_set = c['SERVICE_PHOTOS'][cfg['photos']]
    # Chapters never repeat the hero photo (it is still in the gallery).
    hero_src = _first(r'<div class="page-hero-image"><img src="assets/([^"?]+)', main)
    hero_stem = re.sub(r'(-m|-w\d+)?\.(webp|jpg)$', '', hero_src or '')
    photos = [p for _, p in photo_set if (c['root'] / p).exists() and re.sub(r'\.(webp|jpg)$', '', p.split('/')[-1]) != hero_stem]
    pi = 0
    # Credited reference photos keyed by chapter eyebrow (sustainable pages only).
    ch_media = c.get('CHAPTER_MEDIA', {}).get(name, {})

    def next_photo():
        # One service photo per chapter, never repeated. When the set runs out
        # the chapter renders copy-only instead of showing an unrelated photo.
        nonlocal pi
        if pi >= len(photos):
            return None
        p = photos[pi]
        pi += 1
        return p

    hero = glance = trust = chips = problem = outcome = process = faq = reviews = quote_title = ''
    chapters, raw_after, links = [], [], []
    for cls, html in secs:
        sec_id = _first(r'^<section\b[^>]*\bid="([^"]*)"', html)
        if 'page-hero' in cls:
            hero = html
        elif 'ai-answer-section' in cls:
            cards = re.findall(r'<div class="ai-answer-card"><b>(.*?)</b><span>(.*?)</span></div>', html, re.S)
            cards = [(b, s_) for b, s_ in cards if 'where Terramorph fits' not in b]
            glance = ''.join(f'<div class="tm-glance-card tm-reveal"><b>{b}</b><span>{s_}</span></div>' for b, s_ in cards)
        elif 'trust-band' in cls:
            trust = html
        elif 'conversion-trust-strip' in cls:
            chips = ''.join(f'<span>{x}</span>' for x in re.findall(r'<span>(.*?)</span>', html, re.S) if len(_txt(x)) < 60)
        elif 'quote-section' in cls:
            quote_title = quote_title or _txt(_first(r'<h2[^>]*>(.*?)</h2>', html))
            for href, label in re.findall(r'<a [^>]*href="([^"]+)"[^>]*>(.*?)</a>', html, re.S):
                pass
        elif 'jobber-quote-panel' in cls or 'quote-panel' in cls:
            quote_title = _txt(_first(r'<h2[^>]*>(.*?)</h2>', html)) or quote_title
        elif 'proof-upgrade-section' in cls or 'work-section' in cls:
            continue  # generic proof copy + old gallery: replaced by reviews + service gallery
        elif 'faq-section' in cls:
            qa = _items(html)
            faq = ''.join(f'<details><summary>{q}</summary><p>{a}</p></details>' for q, a in qa)
        elif 'guide-index-section' in cls:
            for href, h3, desc in re.findall(r'<a class="guide-card[^"]*" href="([^"]+)"[^>]*>.*?<h3>(.*?)</h3>(?:\s*<p>(.*?)</p>)?', html, re.S):
                links.insert(0, (href, _txt(h3), _txt(desc)))
        elif 'problem-grid' in html and not problem:
            problem = _first(r'problem-card dark">.*?<h2>(.*?)</h2>', html)
            outcome = _first(r'light-card">.*?<h2>(.*?)</h2>', html)
        elif 'clay-section' in cls and ('Clear estimates' in html or 'data-process' in html) and not process:
            steps = _items(html)
            lead = _first(r'<h2>.*?</h2>\s*<p>(.*?)</p>', html)
            h2 = _first(r'<h2>(.*?)</h2>', html)
            nodes = ''.join(f'<div class="tm-proc-step" role="listitem" style="--i:{i}"><div class="tm-proc-node"><span class="tm-proc-icon"><svg viewBox="0 0 24 24" aria-hidden="true">{ICONS[STEP_ICONS[i]]}</svg></span></div><span class="tm-proc-num">0{i+1}</span><h3>{b}</h3><p>{s}</p></div>' for i, (b, s) in enumerate(steps))
            process = (f'<section class="tm-sec tm-process tm-dark">{c["topo_svg"](seed=len(name))}<div class="tm-wrap">'
                       f'<div class="tm-head-row tm-reveal"><div><p class="tm-label">How we work</p><h2 class="tm-h2">{h2}</h2></div><p class="tm-lead">{lead}</p></div>'
                       f'<div class="tm-proc tm-proc-{len(steps)}" data-proc role="list"><span class="tm-proc-line" aria-hidden="true"><i></i></span>{nodes}</div></div></section>')
        elif 'local-grid' in html and not re.search(r'season-timeline|cleanup-grid|ba-pair|process-timeline|<table', html):
            eyebrow = _first(r'<p class="eyebrow[^"]*">(.*?)</p>', html)
            h2 = _first(r'<h2>(.*?)</h2>', html)
            first_col = _first(r'<div class="container local-grid">\s*<div>(.*?)</div>\s*(?:<div class="authority-list|<ul class="check-list|<div class="mini|</div>\s*</section>)', html) or html
            paras = ''.join(f'<p>{p}</p>' for p in re.findall(r'<p>(.*?)</p>', first_col, re.S))
            depth = _first(r'(<p class="depth-links">.*?</p>)', html)
            for href, label in re.findall(r'<a href="([^"]+)">(.*?)</a>', depth):
                links.append((href, _txt(label)))
            items = _items(_first(r'<div class="authority-list">(.*?)</div>\s*</div>', html) or '')
            checks = re.findall(r'<li>(.*?)</li>', _first(r'<ul class="check-list">(.*?)</ul>', html))
            ctas = re.findall(r'(<a class="btn[^"]*" href="[^"]+">.*?</a>)', html, re.S)
            chapters.append({'eyebrow': eyebrow, 'h2': h2, 'paras': paras, 'items': items, 'checks': checks,
                             'dark': 'clay-section' in cls, 'ctas': ctas, 'id': sec_id})
        else:
            # unknown block (timeline, comparison table, cleanup before/after...): keep it, in order
            chapters.append({'raw': html})
            for href, label in re.findall(r'<p class="internal-link-row">.*?</p>', html, re.S):
                pass

    if sum(1 for ch in chapters if 'raw' not in ch) < 2:
        for ex in EXTRA.get(name, []):
            chapters.append({'eyebrow': ex['eyebrow'], 'h2': ex['h2'], 'paras': ex['paras'], 'items': ex.get('items', []),
                             'checks': ex.get('checks', []), 'dark': False, 'ctas': ex.get('ctas', [])})

    # reviews: every compact review on the page, de-duplicated, up to 3
    revs, rseen = [], set()
    for q, n in re.findall(r'<blockquote class="compact-review">.*?<p>(.*?)</p>\s*<cite>(.*?)</cite>', main, re.S):
        if q not in rseen:
            rseen.add(q); revs.append((q, n))
    for n_, q_ in c['REVIEW_SNIPPETS']:
        if len(revs) >= 3:
            break
        if q_ not in rseen and len(q_) > 60:
            rseen.add(q_); revs.append((q_, n_))
    reviews = ''.join(f'<article class="tm-review tm-reveal"><div class="tm-stars" aria-label="5 stars">★★★★★</div><blockquote>{q}</blockquote><cite>{_txt(n).lstrip("— ").strip()}</cite></article>' for q, n in revs[:max(3, min(6, len(revs)) // 3 * 3)])

    # internal link rows anywhere in main
    for row in re.findall(r'<p class="internal-link-row">(.*?)</p>', main, re.S):
        for href, label in re.findall(r'<a href="([^"]+)">(.*?)</a>', row):
            links.append((href, _txt(label)))

    # ---- hero: keep the original markup (H1, copy, CTAs, image) and add chips + rating card
    hero = hero.replace('class="page-hero premium-page-hero', 'class="page-hero premium-page-hero tm-svc-hero', 1)
    extra = ''
    if chips:
        extra += f'<div class="tm-hero-chips">{chips}</div>'
    extra += (f'<a class="tm-hero-rating" href="{c["GOOGLE_PROFILE_URL"]}" target="_blank" rel="noopener">'
              '<b>4.9</b><span><span class="tm-stars">★★★★★</span><small>220+ Google reviews</small></span></a>')
    hero = re.sub(r'(<div class="cta-row">.*?</div>)', lambda m: m.group(1) + extra, hero, count=1, flags=re.S)

    out = [hero]
    if name in ANSWERS:
        glance = (f'<div class="tm-glance-card tm-answer tm-reveal"><b>{svc} in Northwest Ohio: the short answer</b><span>{ANSWERS[name]}</span>'
                  '<small class="tm-updated">Reviewed October 2026 &middot; Terramorph LLC, Perrysburg, Ohio</small></div>') + glance
    if glance:
        out.append(f'<section class="tm-sec-tight tm-glance-sec"><div class="tm-wrap"><div class="tm-glance">{glance}</div></div></section>')
    if trust:
        out.append(trust)
    if problem:
        out.append(f'''<section class="tm-sec tm-ps-sec"><div class="tm-wrap tm-ps" data-inview>
  <div class="tm-ps-card tm-ps-problem"><p class="tm-label">Sound familiar?</p><h2 class="tm-ps-h">{problem}</h2></div>
  <div class="tm-ps-arrow" aria-hidden="true"><svg viewBox="0 0 48 24"><path d="M2 12h40M34 4l8 8-8 8"/></svg></div>
  <div class="tm-ps-card tm-ps-fix"><p class="tm-label">What you get</p><h2 class="tm-ps-h">{outcome}</h2><a class="tm-btn tm-btn-gold tm-btn-sm" href="#request-form">Get a free quote</a></div>
</div></section>''')

    n = 0
    for k, ch in enumerate(chapters):
        if 'raw' in ch:
            out.append(ch['raw'])
            continue
        n += 1
        ref = ch_media.get(_txt(ch['eyebrow']))
        img = None if ref else next_photo()
        lst = ''
        if ch['items']:
            lst = '<ol class="tm-ch-list">' + ''.join(f'<li class="tm-reveal"><b>{b}</b><span>{s}</span></li>' for b, s in ch['items']) + '</ol>'
        if ch['checks']:
            lst += '<ul class="tm-ch-checks">' + ''.join(f'<li>{x}</li>' for x in ch['checks']) + '</ul>'
        cta = ''.join(x.replace('class="btn btn-primary"', 'class="tm-btn tm-btn-gold tm-btn-sm"').replace('class="btn btn-gold"', 'class="tm-btn tm-btn-gold tm-btn-sm"') for x in ch['ctas'][:1])
        flip = ' tm-ch-flip' if n % 2 == 0 else ''
        dark = ' tm-ch-dark' if ch['dark'] else ''
        if ref:
            r_src, r_alt, r_cap = ref
            media = f'<figure class="tm-ch-media tm-reveal"><img src="{r_src}" alt="{r_alt}" loading="lazy"><span class="tm-ch-num">0{n}</span><figcaption class="tm-photo-credit">{r_cap}</figcaption></figure>'
        else:
            media = f'<figure class="tm-ch-media tm-reveal"><img src="{img}" alt="Terramorph {svc.lower()} work in Northwest Ohio" loading="lazy"><span class="tm-ch-num">0{n}</span></figure>' if img else f'<div class="tm-ch-num tm-ch-num-solo" aria-hidden="true">0{n}</div>'
        solo = '' if (img or ref) else ' tm-ch-solo'
        id_attr = f' id="{ch["id"]}"' if ch.get('id') else ''
        out.append(f'''<section class="tm-sec tm-ch{flip}{dark}"{id_attr}><div class="tm-wrap tm-ch-grid{solo}">
  {media}
  <div class="tm-ch-copy">{f'<p class="tm-label">{ch["eyebrow"]}</p>' if ch['eyebrow'] else ''}<h2 class="tm-h2">{ch['h2']}</h2>{ch['paras']}{lst}{f'<div class="tm-cta-row">{cta}</div>' if cta else ''}</div>
</div></section>''')
        if n == 1 and cfg.get('ba'):
            cards = ''.join(c['ba_card'](b, a, label) for b, a, label in cfg['ba'])
            out.append(f'<section class="tm-sec-tight tm-paper"><div class="tm-wrap"><div class="tm-head-row tm-reveal"><div><p class="tm-label">Before &amp; after</p><h2 class="tm-h2">Same yard, one visit apart.</h2></div><a class="tm-btn tm-btn-line" href="before-after-gallery.html">More before &amp; afters</a></div><div class="tm-ba-row">{cards}</div></div></section>')

    if process:
        out.append(process)
    gal = c['photo_gallery'](photo_set) if len(photo_set) >= 3 else ''
    if gal:
        out.append(f'<section class="tm-sec-tight tm-work"><div class="tm-wrap"><div class="tm-head-row tm-reveal"><div><p class="tm-label">Recent work</p><h2 class="tm-h2">Real {svc.lower()} work by our crews.</h2></div><a class="tm-btn tm-btn-line" href="projects.html">All project photos</a></div></div><div class="tm-work-rail">{gal}</div></section>')
    if reviews:
        out.append(f'''<section class="tm-sec tm-dark tm-svc-reviews"><div class="tm-wrap"><div class="tm-head-row tm-reveal"><div><p class="tm-label">Reviews</p><h2 class="tm-h2">Homeowners who hired us.</h2></div>
  <div class="tm-rating-big"><b>4.9</b><div><div class="tm-stars">★★★★★</div><a href="{c['GOOGLE_PROFILE_URL']}" target="_blank" rel="noopener" style="color:#fff">Read all 220+ on Google &rarr;</a></div></div></div><div class="tm-reviews">{reviews}</div></div></section>''')
    if faq:
        out.append(f'<section class="tm-sec tm-paper"><div class="tm-wrap tm-faq-grid"><div class="tm-reveal"><p class="tm-label">Questions homeowners ask</p><h2 class="tm-h2">Quick answers before you request an estimate.</h2><p class="tm-lead">Still wondering about something? Call <a href="tel:{c["TEL"]}">{c["PHONE"]}</a>, 7 a.m. to 8 p.m.</p></div><div class="tm-faq">{faq}</div></div></section>')

    out.append(f'''<section class="tm-sec-tight"><div class="tm-wrap"><div class="tm-facts tm-reveal">
  <div><p class="tm-label">Terramorph at a glance</p><h2 class="tm-h2" style="font-size:clamp(1.9rem,3.4vw,2.7rem)">The short version.</h2>
  <p>Terramorph LLC is a landscape design and build company based in Perrysburg, Ohio, founded by brothers Ty and Trent Lincoln. We handle {svc.lower()} along with patios, drainage, landscape beds, lighting, lawn care, cleanups, and snow removal for homes and businesses across Wood and Lucas County. 4.9 stars from more than 220 Google reviews, BBB accredited, and estimates are free.</p></div>
  <dl class="tm-facts-grid"><div><dt>Based in</dt><dd>Perrysburg, OH</dd></div><div><dt>Serving</dt><dd>Wood &amp; Lucas County</dd></div><div><dt>Google rating</dt><dd>4.9 from 220+ reviews</dd></div><div><dt>Accreditation</dt><dd>BBB Accredited</dd></div><div><dt>Founders</dt><dd>Ty &amp; Trent Lincoln</dd></div><div><dt>Phone</dt><dd><a href="tel:{c['TEL']}">{c['PHONE']}</a></dd></div></dl>
</div></div></section>''')

    seen, link_cards = set(), []
    for entry in links:
        href, label, desc = (entry + ('',))[:3]
        if href in seen or href == name or href.startswith(('tel:', 'quote', 'http', '#')) or not label:
            continue
        seen.add(href)
        link_cards.append(f'<a class="tm-read tm-reveal" href="{href}"><span>{label}{f"<small>{desc}</small>" if desc else ""}</span><i aria-hidden="true">&rarr;</i></a>')
    if link_cards:
        out.append(f'<section class="tm-sec-tight"><div class="tm-wrap"><p class="tm-label">Keep reading</p><h2 class="tm-h2" style="margin-bottom:26px">Plan your {svc.lower()} project.</h2><div class="tm-reads">{"".join(link_cards[:12])}</div></div></section>')

    if cfg['city_prefix']:
        towns = sorted(p.name for p in c['root'].glob(cfg['city_prefix'] + '*-ohio.html'))
        if towns:
            def town(fn):
                return fn[len(cfg['city_prefix']):-len('-ohio.html')].replace('-', ' ').title()
            chips_html = ''.join(f'<a href="{fn}">{town(fn)}</a>' for fn in towns)
            out.append(f'<section class="tm-sec-tight tm-paper tm-svc-towns"><div class="tm-wrap"><p class="tm-label">Near you</p><h2 class="tm-h2" style="margin-bottom:22px">{svc} by town.</h2><div class="tm-town-list">{chips_html}</div></div></section>')

    if name in c.get('SAVINGS_PAGES', set()):
        out.append(c['project_savings_block']('#request-form'))

    out.append(f'''<section class="tm-sec tm-quote tm-dark">
  <div class="tm-quote-bg"><img src="{photos[0] if photos else 'assets/real-hero.webp'}" alt="" loading="lazy"></div>
  <div class="tm-wrap tm-quote-grid">
    <div>
      <p class="tm-label">Free estimate</p>
      <h2 class="tm-h2">{quote_title or f'Request a {svc} quote'}</h2>
      <ul class="tm-quote-points"><li>Tell us what you want built, fixed, or cleaned up</li><li>Add photos if you have them, they help</li><li>We follow up to set up a visit and a written quote</li></ul>
      <a class="tm-btn tm-btn-ghost" href="tel:{c['TEL']}">Rather talk? Call {c['PHONE']}</a>
    </div>
    {c['form_panel'](c, quote_title or f'Request a {svc} quote', svc)}
  </div>
</section>''')

    new_main = '\n'.join(out)
    t = t[:m_open + len('<main id="main">')] + '\n' + new_main + '\n' + t[m_close:]
    t = t.replace('class="tm-skin"', 'class="tm-skin tm-svc"', 1)
    return t

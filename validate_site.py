from __future__ import annotations
import json, re, sys
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urldefrag, urlparse

ROOT = Path(__file__).resolve().parent
BASE = 'https://terramorphllc.com'
HTML_FILES = sorted(ROOT.glob('*.html'))
EXTERNAL_PREFIXES = ('http://', 'https://', 'tel:', 'mailto:', 'sms:', 'javascript:')
NOINDEX = {'thank-you.html', 'review-notes.html'}

class Parser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.links=[]; self.imgs=[]; self.scripts=[]; self.titles=[]; self.metas=[]; self.h1=[]; self.labels=[]; self.inputs=[]
        self._title=False; self._h1=False
    def handle_starttag(self, tag, attrs):
        attrs=dict(attrs)
        if tag=='a' and attrs.get('href'): self.links.append(attrs['href'])
        if tag=='img': self.imgs.append(attrs)
        if tag=='script' and attrs.get('type')=='application/ld+json': self._script=True; self._buf=''
        if tag=='title': self._title=True; self._buf=''
        if tag=='h1': self._h1=True; self._buf=''
        if tag=='meta': self.metas.append(attrs)
        if tag=='label': self.labels.append(attrs)
        if tag in ('input','select','textarea'): self.inputs.append(attrs)
    def handle_data(self, data):
        if getattr(self,'_script',False) or self._title or self._h1: self._buf += data
    def handle_endtag(self, tag):
        if tag=='script' and getattr(self,'_script',False): self.scripts.append(self._buf.strip()); self._script=False
        if tag=='title' and self._title: self.titles.append(self._buf.strip()); self._title=False
        if tag=='h1' and self._h1: self.h1.append(re.sub(r'\s+',' ',self._buf.strip())); self._h1=False

def meta_content(p, key, value):
    for m in p.metas:
        if m.get(key)==value:
            return m.get('content','')
    return ''

errors=[]; warnings=[]
all_names={p.name for p in HTML_FILES}
for path in HTML_FILES:
    html=path.read_text(errors='replace')
    p=Parser(); p.feed(html)
    if not p.titles: errors.append(f'{path.name}: missing title')
    elif len(p.titles[0])>68: warnings.append(f'{path.name}: long title {len(p.titles[0])}: {p.titles[0]}')
    desc=meta_content(p,'name','description')
    if not desc: errors.append(f'{path.name}: missing meta description')
    elif len(desc)>180: warnings.append(f'{path.name}: long meta description {len(desc)}')
    m_can = re.search(r'<link[^>]+rel="canonical"[^>]+href="([^"]+)"', html)
    canonical = m_can.group(1) if m_can else None
    if not canonical: errors.append(f'{path.name}: missing canonical')
    expected = BASE + ('/' if path.name=='index.html' else '/' + path.name)
    if canonical and canonical != expected: errors.append(f'{path.name}: canonical mismatch {canonical} != {expected}')
    if len(p.h1)!=1: errors.append(f'{path.name}: expected 1 h1, found {len(p.h1)}')
    # JSON-LD parse
    for i,s in enumerate(p.scripts,1):
        try: json.loads(s)
        except Exception as e: errors.append(f'{path.name}: invalid json-ld #{i}: {e}')
    # image checks
    for img in p.imgs:
        src=img.get('src','')
        if not img.get('alt') and img.get('alt')!='': errors.append(f'{path.name}: img missing alt {src}')
        if src and not src.startswith(EXTERNAL_PREFIXES):
            clean=src.split('?')[0]
            if clean.startswith('/'): clean=clean.lstrip('/')
            if not (ROOT/clean).exists(): errors.append(f'{path.name}: missing image {src}')
    # internal links
    for href in p.links:
        href,_=urldefrag(href)
        if not href or href.startswith(EXTERNAL_PREFIXES): continue
        if href.startswith('/'): target=href.lstrip('/') or 'index.html'
        else: target=href
        target=target.split('?')[0]
        if target.endswith('/'): target += 'index.html'
        if target not in all_names and not (ROOT/target).exists(): errors.append(f'{path.name}: broken internal link {href}')
    if path.name not in NOINDEX and 'noindex' in html.lower(): errors.append(f'{path.name}: unexpected noindex')

# sitemap coverage
sitemap=(ROOT/'sitemap.xml').read_text() if (ROOT/'sitemap.xml').exists() else ''
if not sitemap: errors.append('missing sitemap.xml')
for path in HTML_FILES:
    if path.name in NOINDEX or path.name=='privacy.html':
        continue
    loc=BASE + ('/' if path.name=='index.html' else '/' + path.name)
    if loc not in sitemap: errors.append(f'sitemap missing {path.name}')
for name in NOINDEX:
    if BASE+'/'+name in sitemap: errors.append(f'sitemap includes noindex {name}')
robots=(ROOT/'robots.txt').read_text() if (ROOT/'robots.txt').exists() else ''
if f'Sitemap: {BASE}/sitemap.xml' not in robots: errors.append('robots missing sitemap')
if f'Sitemap: {BASE}/image-sitemap.xml' not in robots: warnings.append('robots missing image sitemap')

print(f'HTML files: {len(HTML_FILES)}')
print(f'Errors: {len(errors)}')
for e in errors[:200]: print('ERROR:', e)
print(f'Warnings: {len(warnings)}')
for w in warnings[:200]: print('WARN:', w)
sys.exit(1 if errors else 0)

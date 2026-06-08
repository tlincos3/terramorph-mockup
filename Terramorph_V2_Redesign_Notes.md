# TerraMorph V2 Redesign Pass

## Objective
Move the TerraMorph mockup from a good prototype into a premium outdoor transformation brand that can support higher-ticket landscape design, patio, drainage, lighting, retaining wall, and outdoor living leads.

## Positioning implemented
**Northwest Ohio’s Premium Outdoor Transformation Company**

The V2 homepage no longer leads like a lawn care company. Maintenance is deemphasized. The primary conversion paths now lead with:
- Landscape Design
- Paver Patios
- Drainage Solutions
- Outdoor Lighting
- Retaining Walls
- Outdoor Living

## Major V2 changes

### 1. Hero redesign
- Rebuilt the hero around dusk outdoor lighting / premium outdoor living imagery.
- Added stronger emotional headline: “Turn your yard into the place everyone wants to gather.”
- Added above-the-fold trust: 200+ Google Reviews, BBB Member, Licensed & Insured, Local Perrysburg Company.
- Added premium quote, transformation, and phone CTAs.

### 2. Emotional selling
The copy now sells outcomes instead of service tasks:
- Pride of ownership
- Hosting family and friends
- Increased property confidence/value
- Better curb appeal
- Fixing drainage frustration
- Making outdoor space usable

### 3. Transformation section
Added a photo section showing:
- Before: standing water, builder-grade landscaping, poor curb appeal, unusable backyard
- After: outdoor living, premium patios, improved drainage, curb appeal, property confidence

### 4. Trust upgrade
Trust is now present above the fold and throughout the site:
- 200+ Google Reviews
- Google Verified badge
- BBB badge/member language
- Licensed & Insured
- Local Perrysburg company
- Wood & Lucas County service-area proof

### 5. Gallery converted into project photos
Projects are now framed as sales stories with:
- City
- Customer problem
- Scope / solution
- Transformation result
- Before image
- After image
- CTA: “I Want Something Similar”

### 6. Premium service cards
Each service card includes:
- Best for
- Homeowner problem
- Expected outcome
- Specific CTA

Examples:
- Landscape Design → Design My Property
- Drainage Solutions → Fix My Drainage
- Paver Patios → Plan My Patio
- Outdoor Lighting → Light My Property
- Retaining Walls → Build My Wall

### 7. Local authority layer
Added Northwest Ohio-specific credibility around:
- Clay soil
- Flat lots
- Drainage issues
- Freeze/thaw cycles
- Perrysburg neighborhoods
- Toledo-area property challenges
- Wood & Lucas Counties

### 8. Conversion optimization
- Sticky mobile Call / Get Quote bar
- Shorter quote flow with proper lead fields
- Service-specific CTAs
- Review snippets near forms
- Project-photo proof near CTAs
- Project range field including $25k+
- Phone CTA visible throughout

### 9. Accessibility upgrade
Verified Lighthouse accessibility score: **100** on the V2 homepage.

Implemented:
- Semantic `main`, header, nav, footer
- Skip link
- Proper labels for form fields
- Autocomplete / inputmode where relevant
- Alt text
- Keyboard focus states
- ARIA live success message
- High-contrast CTA/focus treatment
- Reduced-motion media query

## Verification results
Local server: `http://localhost:8777/index.html`

Lighthouse V2 homepage:
- Performance: 84
- Accessibility: 100
- Best Practices: 96
- SEO: 100
- Agentic Browsing: 99

Crawl verification:
- HTML files checked: 8
- Internal links checked: 235
- Images checked: 75
- Missing links/assets: 0

Browser verification:
- Homepage opened successfully
- Contact page opened successfully
- Browser console showed 0 JS errors
- Quote form success state verified through DOM submit

Screenshots generated:
- `screenshots/home-v2-desktop.png`
- `screenshots/home-v2-mobile.png`
- `screenshots/contact-v2-desktop.png`

## Remaining production notes
This is still a static mockup. Production should connect:
- CRM form submission
- Call tracking
- Google Ads conversion tracking
- Meta Pixel + CAPI
- Review widgets / verified review snippets
- LocalBusiness, Service, FAQ, Breadcrumb schema
- Real project project-photo photography and final copy approvals

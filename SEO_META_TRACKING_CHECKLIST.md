# Terramorph SEO + Meta Tracking Checklist

## Implemented in this branch

- Meta Pixel remains installed sitewide: `1286455403443187`.
- Added stronger attribution context capture for:
  - `utm_source`
  - `utm_medium`
  - `utm_campaign`
  - `utm_content`
  - `utm_term`
  - `fbclid`
  - `gclid`
  - `wbraid`
  - `gbraid`
  - `msclkid`
  - Meta browser/click IDs: `_fbp`, `_fbc`
- Added normalized `dataLayer` events and GA4 `gtag` events so Google Ads / GA4 can read clean website activity:
  - `terramorph_page_view`
  - `quote_intent`
  - `phone_click`
  - `quote_thank_you_attributed` on an attributed thank-you visit for diagnostics only
- Hardened Meta lead tracking:
  - Phone clicks fire `Contact` and `PhoneClick`, not a premature `Lead`.
  - Quote-link clicks fire `Contact` and `QuoteIntent`.
  - Paid landing pages use the secure Jobber request form instead of browser-only quick forms.
  - Jobber's native `form_submit` is the only source mapped to GA4 `generate_lead`.
  - An attributed thank-you visit fires GA4 diagnostic `quote_thank_you_attributed` and Meta `Lead`, with a session guard against reload duplicates.
  - Internal quote and direct Jobber links preserve UTMs plus `gclid`, `wbraid`, and `gbraid`.
- SEO cleanup:
  - Removed `thank-you.html` and `review-notes.html` from sitemap.
  - Added `noindex, nofollow` to `thank-you.html` and `review-notes.html`.
  - Added `noindex, follow` to eight paid landing pages and eleven hypothetical planning pages.
  - Removed all noindex pages from the organic sitemap.
  - Bumped the application cache version to `3.57`.

## Google Ads launch package

- Added `google-ads-launch-2026-06-30/` with Search campaign build files for drainage, paver patios, landscape design, maintenance, and cleanups.
- Campaign files are intentionally set to `Paused` so the account can be reviewed before spend starts.
- Primary optimization should use duration-qualified calls, verified quote submissions, and qualified CRM outcomes. Keep simple clicks secondary.

## Still needed outside the repo

These require Google/Meta/account access and should be verified in the ad platforms. Give access to `jarvisthebeast369@gmail.com` or send the relevant IDs and I can finish the account-side setup:

1. Google Search Console
   - Verify `https://terramorphllc.com/` property.
   - Submit `https://terramorphllc.com/sitemap.xml`.

2. Google Analytics / Tag Manager
   - Confirm GA4 measurement ID `G-QRTSH6WXYK` is connected to the right property.
   - Link GA4 to Google Ads.
   - Keep `phone_click` and `quote_intent` as secondary intent signals.
   - Import `generate_lead` as the single primary website-form conversion after the repaired Jobber event is available in Google Ads.

3. Meta Events Manager
   - Confirm domain verification for `terramorphllc.com`.
   - Confirm Pixel `1286455403443187` is assigned to the right Business Manager/ad account.
   - Mark `Lead`, `Contact`, and quote-related custom events as visible/tested.

4. Google Ads call tracking
   - Enable call reporting.
   - Add call asset `419-873-6801`.
   - Count calls after a useful duration threshold, starting at 60 seconds.
   - Add website-call conversion tracking if Google forwarding numbers are approved for the site.

5. Google Business Profile
   - Add/confirm website URL, service categories, service areas, photos, hours, and appointment/contact URL.
   - Use `https://terramorphllc.com/reviews.html` as the crew/customer review-request destination.
   - Add fresh project photos regularly with city/service captions.

6. Meta Ads setup
   - Use the dedicated landing pages below by offer instead of sending paid traffic to the homepage.
   - Build separate ad sets for patios, drainage/standing water, curb appeal, and spring cleanup.
   - Test Pixel events in Meta Events Manager after deployment: PageView, Lead, Contact, and custom quote intent events.

7. Search Console
   - Submit both `https://terramorphllc.com/sitemap.xml` and `https://terramorphllc.com/image-sitemap.xml`.
   - Do not request indexing for `lp-*` paid pages. Inspect and request indexing for the highest-priority service and guide pages instead.

8. Conversion QA after deploy
   - Click phone CTA from a tagged URL.
   - Do not create another QA request merely to force reporting; use the completed acceptance test and normal linked-account processing.
   - Confirm intent/diagnostic events remain secondary and each genuine completed request produces one GA4 `generate_lead`.

## Recommended Meta campaign URLs

Use UTMs on every ad destination, for example:

```text
https://terramorphllc.com/lp-patios.html?utm_source=facebook&utm_medium=paid_social&utm_campaign=patios_leads&utm_content={{ad.name}}
https://terramorphllc.com/lp-drainage.html?utm_source=facebook&utm_medium=paid_social&utm_campaign=drainage_leads&utm_content={{ad.name}}
https://terramorphllc.com/lp-landscape-design.html?utm_source=facebook&utm_medium=paid_social&utm_campaign=landscape_design_leads&utm_content={{ad.name}}
https://terramorphllc.com/lp-outdoor-lighting.html?utm_source=facebook&utm_medium=paid_social&utm_campaign=outdoor_lighting_leads&utm_content={{ad.name}}
```

## V3.45 added landing pages

Recommended Meta/Google campaign destinations added in this expansion:

```text
https://terramorphllc.com/lp-backyard-patio-estimate.html?utm_source=facebook&utm_medium=paid_social&utm_campaign=backyard_patio_estimate&utm_content={{ad.name}}
https://terramorphllc.com/lp-standing-water-yard.html?utm_source=facebook&utm_medium=paid_social&utm_campaign=standing_water_drainage&utm_content={{ad.name}}
https://terramorphllc.com/lp-curb-appeal-upgrade.html?utm_source=facebook&utm_medium=paid_social&utm_campaign=curb_appeal_upgrade&utm_content={{ad.name}}
https://terramorphllc.com/lp-spring-cleanup.html?utm_source=facebook&utm_medium=paid_social&utm_campaign=spring_cleanup&utm_content={{ad.name}}
```

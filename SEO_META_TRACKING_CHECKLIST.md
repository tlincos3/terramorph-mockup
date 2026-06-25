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
  - `msclkid`
  - Meta browser/click IDs: `_fbp`, `_fbc`
- Added normalized `dataLayer` events so Google Tag Manager / GA4 can read clean website activity later. This is GTM-ready, but Google tracking is not live until a GTM container or GA4 tag is installed:
  - `terramorph_page_view`
  - `quote_intent`
  - `phone_click`
  - `quick_lead_continue`
  - `quote_submit`
  - `quote_submit_fallback`
- Hardened Meta lead tracking:
  - Phone clicks fire `Lead` + `Contact`.
  - Quick lead forms fire `Lead` before sending users to Jobber.
  - Jobber quote-clicks preserve attribution parameters.
  - Thank-you page now has attribution-guarded fallback tracking so completed quote returns are less likely to be missed without counting random direct thank-you visits as primary Meta Lead conversions.
- SEO cleanup:
  - Removed `thank-you.html` and `review-notes.html` from sitemap.
  - Added `noindex, nofollow` to `thank-you.html` and `review-notes.html`.
  - Bumped static asset cache versions to `3.44`.

## Still needed outside the repo

These require Google/Meta/Jobber account access and should be verified in the ad platforms. Give access to `jarvisthebeast369@gmail.com` or send the relevant IDs and I can finish the account-side setup:

1. Google Search Console
   - Verify `https://terramorphllc.com/` property.
   - Submit `https://terramorphllc.com/sitemap.xml`.

2. Google Analytics / Tag Manager
   - Current repo state is `dataLayer`-ready only; Google tracking is not live until a GTM container or GA4 tag is installed.
   - If GA4 exists: send the GA4 Measurement ID or GTM container ID.
   - If not, create one and wire the existing `dataLayer` events to GA4 conversions.

3. Meta Events Manager
   - Confirm domain verification for `terramorphllc.com`.
   - Confirm Pixel `1286455403443187` is assigned to the right Business Manager/ad account.
   - Mark `Lead`, `Contact`, and quote-related custom events as visible/tested.

4. Jobber
   - Confirm the Jobber form redirect/confirmation behavior returns users to `https://terramorphllc.com/thank-you.html` when possible.
   - If Jobber cannot redirect, rely on quick-form and outbound quote intent tracking, but true form-submit tracking will be limited.

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
   - Inspect the new landing pages after deploy and request indexing for the highest-priority pages first.

8. Conversion QA after deploy
   - Click phone CTA from a tagged URL.
   - Submit the quick lead form from a tagged URL.
   - Click through to Jobber from a tagged URL.
   - Confirm attribution parameters remain attached and events show in Meta/GTM debugging.

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

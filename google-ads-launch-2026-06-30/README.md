# Terramorph Google Ads Search Launch - 2026-06-30

This package is built for a $3,000/month Google Search launch for Terramorph LLC.

It is designed to put Terramorph in front of high-intent Northwest Ohio homeowners searching for landscape design, landscape installation, maintenance, cleanups, drainage, and paver patios. Landscape design/install and maintenance/cleanup leads are prioritized over drainage and patio leads. Campaigns are set to `Paused` in the build files so the account can be reviewed before spend starts.

## Current Constraints

- Chrome/account control is not available in this Codex session, so the Google Ads account cannot be edited directly yet.
- The live website is currently phone-first and uses `419-873-6801`.
- The live paid landing pages have GA4, Meta Pixel, phone-click tracking, and quick-lead tracking.
- Google Ads, GA4, call reporting, Google Business Profile, and conversion import still need account access verification.

## Files

- `campaigns.csv` - campaign-level settings and budgets.
- `keywords.csv` - exact and phrase keywords by campaign/ad group.
- `responsive-search-ads.csv` - RSA copy by campaign/ad group.
- `negative-keyword-list.csv` - shared negatives to apply to all Search campaigns.
- `assets.csv` - sitelinks, callouts, snippets, and call asset plan.
- `conversion-and-launch-checklist.md` - required account-side setup before enabling spend.

## Launch Budget

- Search | Landscape Design + Installation | NW Ohio: $40/day
- Search | Maintenance + Cleanups | NW Ohio: $30/day
- Search | Drainage | NW Ohio: $15/day
- Search | Paver Patios | NW Ohio: $15/day

Total: $100/day, about $3,000/month.

## Required Location Target

Target people in or regularly in:

Perrysburg, Toledo, Maumee, Sylvania, Bowling Green, Rossford, Oregon, Waterville, Whitehouse, Wood County, and Lucas County, Ohio.

Use presence targeting. Do not use broad "interested in" location targeting.

## Recommended Initial Settings

- Campaign type: Search only.
- Status: Paused until tracking is verified.
- Search partners: Off for the first 30 days unless volume is too low.
- Display expansion: Off.
- Bidding: Start with Maximize Clicks with a CPC cap if conversion tracking is not verified. Switch to Maximize Conversions after reliable call/form conversions are flowing.
- Ad schedule: 7:00 AM to 8:00 PM, Monday through Saturday, unless calls are answered outside those hours.
- Final URL suffix: `utm_source=google&utm_medium=cpc&utm_campaign={campaignid}&utm_content={creative}&utm_term={keyword}`

## Account Access Needed

To actually launch, grant account access or use a logged-in browser session for:

- Google Ads
- GA4 property with measurement ID `G-QRTSH6WXYK`
- Google Business Profile
- Website/tag management if conversion snippets need changes

Do not send passwords. Use Google account access.

# Conversion And Launch Checklist

Use this before enabling any Terramorph Google Ads campaign.

## 1. Account Access

- Confirm Google Ads access.
- Confirm GA4 access for measurement ID `G-QRTSH6WXYK`.
- Confirm Google Business Profile access.
- Confirm billing is valid, but do not change billing without owner approval.

## 2. Conversion Actions

Primary conversions:

- Calls from ads using call asset `419-873-6801`.
- Calls from website using Google forwarding number/call reporting if available.
- GA4 event import: `phone_click`.

Secondary conversions:

- GA4 event import: `quick_lead_continue`.
- GA4 event import: `quote_intent`.
- GA4 event import: `quote_submit_fallback` only if thank-you return behavior is confirmed.

Do not optimize to page views, scrolls, or all clicks.

## 3. GA4 And Google Ads Linking

- Link GA4 property to Google Ads.
- Import relevant GA4 events into Google Ads conversions.
- Mark `phone_click` as primary only after confirming it fires once per actual phone CTA click.
- Keep `quick_lead_continue` secondary until lead quality is proven.
- Confirm the live site sends `gclid` and UTM context into page events.

## 4. Call Tracking

- Enable call reporting.
- Use call asset with `419-873-6801`.
- Count calls as conversions only after a useful duration threshold, starting at 60 seconds.
- If call volume is high but quality is weak, raise the threshold to 90 or 120 seconds.

## 5. Location Settings

- Target only Perrysburg, Toledo, Maumee, Sylvania, Bowling Green, Rossford, Oregon, Waterville, Whitehouse, Wood County, and Lucas County.
- Use presence targeting.
- Exclude people only "interested in" the area.

## 6. Pre-Launch QA

- Open each final URL on desktop and mobile.
- Click phone CTA from a URL containing `?gclid=test&utm_source=google&utm_medium=cpc`.
- Submit the quick-lead form from a tagged URL and verify `quick_lead_continue`.
- Verify `phone_click` appears in GA4 DebugView or Realtime.
- Confirm Meta Pixel still fires PageView/Lead/Contact as expected.
- Confirm no campaign has Display expansion enabled.
- Confirm all campaigns are still paused before final review.

## 7. First 30 Days

Daily for first week:

- Review search terms.
- Add negatives for jobs, DIY, supplies, low-intent research, and out-of-area searches.
- Watch calls by campaign and ad group.
- Pause spenders with no call or lead intent.

Weekly:

- Move budget toward the highest-value qualified calls, with landscape design/install and maintenance/cleanup lead quality reviewed first.
- Check Auction Insights for Perrysburg and Toledo competitors.
- Review phone-call quality, not just click volume.
- Raise budget only after qualified calls are visible.

Initial success targets:

- Calls and quick-lead events should appear within the first few days.
- Landscape design/install and maintenance/cleanup should get first budget protection if lead quality is acceptable.
- Drainage and patios should remain capped unless they produce clearly higher-value qualified calls.

## 8. Activation Rule

Do not enable campaigns until:

- Conversion tracking is verified.
- Location targeting is confirmed.
- Negative list is applied.
- Call asset is active.
- Owner gives explicit approval to turn on spend.

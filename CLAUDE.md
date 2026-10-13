# terramorphllc.com — the site

136 static HTML pages on GitHub Pages. Repo `tlincos3/terramorph-mockup`.
Owner agent: `terramorph-web`.

## The tracking contract — verify after EVERY change

This has broken silently before and it costs real leads. Curl the live site and check all
four:

1. Homepage has gtag config for `AW-17691366114` AND `G-QRTSH6WXYK`, and
   **G-QRTSH6WXYK must come AFTER the AW configs.** The Jobber form embed reads the LAST
   config. Wrong order kills form tracking with no error.
2. Homepage carries `phone_conversion_number '419-873-6801'` and label
   `QJLGCNu6wtscEOKl8_NB`.
3. `app.js` carries `AW_QUOTE_REQUEST_LABEL = 'obvlCJaFougcEOKl8_NB'`.
4. `/thank-you.html` returns 200 — the hosted Jobber form redirects there.

If any fail, that is the headline of your report, above everything else.

## Publishing (since 2026-10-13, Phase 0)

GitHub Pages serves the **docs/** folder, not the repo root. `build_pages.py` regenerates the
pages and then copies ONLY public files into docs/ (pages, app.js, styles.css, sitemaps,
robots, CNAME, favicon, top-level assets). Internal notes, code, screenshots, ad creatives
(assets/ads) and review-notes.html never reach the live site. Always run build_pages.py
then validate_site.py and commit docs/ with your change. validate_site.py now blocks on:
broken tracking on ANY page, "hypothetical" content, internal files in docs/, or a stale docs/.

The 10 invented "planning example" case-study pages are now redirect pages to projects.html
(RETIRED_REDIRECTS in build_pages.py). Do not bring invented jobs back. The June ad-launch
spreadsheets moved out of this public repo to ~/projects/terramorph/04-marketing/.

## Pages are generated

Many pages come from `build_pages.py`. Edit the generator, not the output — check which
before editing. `authority_pass.py` handles the SEO content passes.

## Voice

Design/build hardscape: landscape design, paver patios, drainage. Service area is
Perrysburg, Toledo, Maumee, Sylvania, Bowling Green, Rossford, Oregon, Waterville,
Whitehouse, Wood and Lucas County. 220+ five-star reviews, BBB accredited, 419-873-6801.

**Never write in the old "lawncare, landscaping and odd jobs" voice.** That is the previous
version of the business and the Desktop material still uses it.

## Shipping

Commit author email must be `261499129+tlincos3@users.noreply.github.com`.
After pushing, verify the Pages build succeeded and the change is actually live — then
re-check the tracking contract.

## Rejected: call-back mini-form

A two-field "Rather have us call you?" form ran 2026-09-14 to 2026-09-17 and was removed
at Trent's request — he tried it and did not like it. Do not re-add it or any similar
secondary mini-form without asking him. Its Supabase table
`public.terramorph_backup_leads` (project `bnmqhtlaptwmwkdajabh`) was left in place;
the scheduled task `terramorph-callback-lead-alert` is paused.

## Known gap

There is no first-party lead capture on this site. Leads go to a phone number or into a
cross-origin Jobber iframe, so a missed call or abandoned form leaves no record Trent
controls. `quick_lead_form()` exists in the generator but no deployed page renders it, and
it only writes to localStorage anyway. See `terramorph-leads`.

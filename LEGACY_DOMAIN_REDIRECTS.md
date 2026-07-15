# Legacy terra419.com Redirect Plan

## Current state

As of July 14, 2026, GoDaddy's forwarding product sends only the apex and
`www` homepages to `https://terramorphllc.com`. Requests for indexed legacy
paths such as `/about-us` and `/landscape-installation-landscape-design` return
a 404 from GoDaddy before reaching the new website.

A dedicated redirect project is deployed at:

```text
https://terra419-redirect.vercel.app
```

The Vercel project is named `terra419-redirect`. Both `terra419.com` and
`www.terra419.com` are assigned to it and are waiting for DNS activation.

## Required DNS activation

GoDaddy's forwarding product currently owns four locked A records. Remove the
apex and `www` forwarding entries before adding these records:

```text
Type  Name  Data
A     @     76.76.21.21
A     www   76.76.21.21
```

Keep GoDaddy's existing nameservers and all TXT verification records. Do not
change the nameservers or remove Google Search Console verification records.

## Redirect behavior

Mappings live in `legacy-redirect/vercel.json`. The project sends indexed old
service and location URLs directly to their closest equivalents on
`terramorphllc.com`, preserves query strings, and sends unknown legacy paths to
the new homepage instead of returning an old-domain 404.

Vercel returns `308 Permanent Redirect`, which Google treats as a permanent
redirect for site moves in the same way as a 301.

## Verification

After the DNS change, run:

```bash
curl -sS -D - -o /dev/null https://terra419.com/
curl -sS -D - -o /dev/null https://terra419.com/about-us
curl -sS -D - -o /dev/null https://terra419.com/landscape-installation-landscape-design
curl -sS -D - -o /dev/null https://www.terra419.com/snow-removal
```

Expected behavior:

- The first response is a `308` with a `Location` on `terramorphllc.com`.
- The redirected destination returns `200`.
- There is no intermediate redirect to another `terra419.com` URL.
- Query strings such as Google Ads UTM parameters remain intact.

Keep this redirect project active for at least 12 months after Google finishes
processing the Search Console change of address. Longer is preferable while
old backlinks and directory listings still exist.

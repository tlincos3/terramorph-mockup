# terra419.com legacy redirect

This Vercel project exists only to redirect the former `terra419.com` URLs to
their closest equivalents on `terramorphllc.com`. It prevents indexed legacy
pages from returning 404 errors during the Google Search Console change of
address period.

The explicit mappings in `vercel.json` must remain above the catch-all rule.
Vercel preserves query strings on these redirects, including Google Ads UTM
parameters.

## Deployment

```bash
vercel deploy --prod --yes
```

After deployment, assign both `terra419.com` and `www.terra419.com` to the
project, apply the DNS records Vercel provides, and verify representative URLs:

```bash
curl -sS -D - -o /dev/null https://terra419.com/about-us
curl -sS -D - -o /dev/null https://terra419.com/landscape-installation-landscape-design
curl -sS -D - -o /dev/null https://www.terra419.com/snow-removal
```

Each legacy URL should return one permanent redirect directly to the matching
`https://terramorphllc.com/` page.

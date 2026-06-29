# Legacy terra419.com Redirect Plan

Current live test result on 2026-06-29: `terra419.com` redirects only to `www.terra419.com`, and `www.terra419.com` still serves the old site. This must be changed in the legacy domain host/DNS/edge layer, not inside the `terramorphllc.com` GitHub Pages repo.

## Required behavior

- One-hop 301 from both `terra419.com` and `www.terra419.com` to `https://terramorphllc.com`.
- Preserve equivalent paths where a strong equivalent exists.
- Do not redirect old domain traffic to another old-domain URL first.
- Keep query strings for ad/campaign attribution.

## Preferred edge rule

If using Cloudflare, create a bulk redirect or redirect rule:

```text
Source hostname: terra419.com OR www.terra419.com
Status: 301
Preserve query string: yes
```

Use these path mappings before the catch-all:

```text
https://terra419.com/                         -> https://terramorphllc.com/
https://www.terra419.com/                     -> https://terramorphllc.com/
https://terra419.com/drainage                 -> https://terramorphllc.com/drainage-solutions.html
https://www.terra419.com/drainage             -> https://terramorphllc.com/drainage-solutions.html
https://terra419.com/paver-patios             -> https://terramorphllc.com/paver-patios-hardscapes.html
https://www.terra419.com/paver-patios         -> https://terramorphllc.com/paver-patios-hardscapes.html
https://terra419.com/landscape-design         -> https://terramorphllc.com/landscape-design.html
https://www.terra419.com/landscape-design     -> https://terramorphllc.com/landscape-design.html
https://terra419.com/outdoor-lighting         -> https://terramorphllc.com/outdoor-lighting.html
https://www.terra419.com/outdoor-lighting     -> https://terramorphllc.com/outdoor-lighting.html
https://terra419.com/lawn-maintenance         -> https://terramorphllc.com/lawn-maintenance.html
https://www.terra419.com/lawn-maintenance     -> https://terramorphllc.com/lawn-maintenance.html
https://terra419.com/contact                  -> https://terramorphllc.com/contact.html
https://www.terra419.com/contact              -> https://terramorphllc.com/contact.html
https://terra419.com/about                    -> https://terramorphllc.com/about.html
https://www.terra419.com/about                -> https://terramorphllc.com/about.html
https://terra419.com/*                        -> https://terramorphllc.com/$1
https://www.terra419.com/*                    -> https://terramorphllc.com/$1
```

## Nginx equivalent

```nginx
server {
    listen 443 ssl http2;
    server_name terra419.com www.terra419.com;

    location = / { return 301 https://terramorphllc.com/$is_args$args; }
    location = /drainage { return 301 https://terramorphllc.com/drainage-solutions.html$is_args$args; }
    location = /paver-patios { return 301 https://terramorphllc.com/paver-patios-hardscapes.html$is_args$args; }
    location = /landscape-design { return 301 https://terramorphllc.com/landscape-design.html$is_args$args; }
    location = /outdoor-lighting { return 301 https://terramorphllc.com/outdoor-lighting.html$is_args$args; }
    location = /lawn-maintenance { return 301 https://terramorphllc.com/lawn-maintenance.html$is_args$args; }
    location = /contact { return 301 https://terramorphllc.com/contact.html$is_args$args; }
    location = /about { return 301 https://terramorphllc.com/about.html$is_args$args; }

    location / { return 301 https://terramorphllc.com$request_uri; }
}
```

## Verification commands

```bash
curl -sSIL https://terra419.com/drainage | sed -n '1,12p'
curl -sSIL https://www.terra419.com/drainage | sed -n '1,12p'
curl -sSIL https://terra419.com/paver-patios | sed -n '1,12p'
curl -sSIL https://www.terra419.com/paver-patios | sed -n '1,12p'
```

Expected: first response is `HTTP/2 301` or `HTTP/1.1 301` with `location: https://terramorphllc.com/...`; final response is `200`; no intermediate old-domain hop.

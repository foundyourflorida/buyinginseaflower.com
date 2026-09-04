# Moving production hosting to Cloudflare Pages

Goal: Cloudflare Pages serves `docs/` from the GitHub repo `foundyourflorida/buyinginseaflower.com`; Cloudflare manages DNS and SSL for `buyinginseaflower.com` and `www`; canonical URL is `https://buyinginseaflower.com`; all http and www traffic 301s to it with path, query, UTM and gclid preserved. GitHub Pages stays configured as the rollback host until the cutover is verified.

## What is already in the repo

- `docs/` is the complete static site (no build step needed on Cloudflare).
- `docs/_headers`: security headers and noindex for `/admin/` and `/thank-you/`.
- `docs/_redirects`: minor path redirects. (Cloudflare Pages `_redirects` cannot match hostnames, so the www redirect is a zone rule, below.)
- Canonical tags, sitemap, feed and `llms.txt` already use `https://buyinginseaflower.com`.

## Steps that need the Cloudflare account (owner)

1. Create the account at dash.cloudflare.com (free plan) with trenton@foundyourflorida.com.
2. **Workers & Pages → Create → Pages → Connect to Git** → authorize the `foundyourflorida` GitHub account → select `buyinginseaflower.com`.
   Build settings: Framework preset **None**, Build command **(empty)**, Build output directory **`docs`**, production branch **`main`**. Save and Deploy. This produces `https://<project>.pages.dev`, which is a full preview of production (verify it before touching DNS).
3. **Add the site to Cloudflare**: Dashboard → Add a site → `buyinginseaflower.com` → Free. Cloudflare imports the existing records (it will show the four GitHub A records and the www CNAME; leave them for now).
4. **Custom domains on the Pages project**: Pages project → Custom domains → add `buyinginseaflower.com` and `www.buyinginseaflower.com`. Cloudflare will offer to replace the DNS records with CNAMEs to the Pages project; accept for both. (Rollback = put the GitHub A records/CNAME back.)
5. **SSL/TLS**: SSL/TLS → Overview → **Full (strict)**; Edge Certificates → **Always Use HTTPS: On**, **Automatic HTTPS Rewrites: On**. Do not enable HSTS until https has been verified for a day.
6. **www → apex redirect**: Rules → Redirect Rules → Create → "www to apex":
   - When incoming requests match: Hostname equals `www.buyinginseaflower.com`
   - Then: Dynamic redirect, expression `concat("https://buyinginseaflower.com", http.request.uri.path, if(len(http.request.uri.query) > 0, concat("?", http.request.uri.query), ""))`, status **301**, preserve query string **on**.
7. **Nameservers (the irreversible-feeling step; it is reversible)**: in Squarespace Domains → buyinginseaflower.com → Nameservers → Use custom nameservers → enter the two nameservers Cloudflare shows on the site overview. Propagation is minutes to a few hours.

## Verification after cutover

- `https://buyinginseaflower.com/`, `/buyers-guide/`, `/book/`, `/thank-you/` return 200 with a valid certificate.
- `http://buyinginseaflower.com/costs/?gclid=abc&utm_source=x` → 301 → `https://buyinginseaflower.com/costs/?gclid=abc&utm_source=x`
- `https://www.buyinginseaflower.com/costs/?gclid=abc` → 301 → `https://buyinginseaflower.com/costs/?gclid=abc`
- Google tag: one loader, `G-N1PEN4WMZ7` and `AW-18430676225` configured; form and Calendly conversions unchanged (same `main.js`).

## Rollback

Switch the nameservers at Squarespace back to `nsa1..nsa4.squarespacedns.com`; the GitHub Pages A records and www CNAME there are untouched, and the GitHub Pages site remains enabled and building from `main`. Nothing on GitHub needs to change to roll back.

## Optional: let Claude do steps 2 to 6 by API

Create an API token (My Profile → API Tokens → Create Token) with: Account → Cloudflare Pages: Edit; Zone → DNS: Edit; Zone → Zone Settings: Edit; Zone → Zone: Read; and Zone → Dynamic Redirect: Edit, scoped to the account and zone. Save it to `~/.config/cloudflare/token` on this Mac (never paste it into chat) and the deployment, DNS records, SSL settings and redirect rule can be applied by script.

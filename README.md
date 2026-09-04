# buyinginseaflower.com

Static, dependency-free website for **Buying in SeaFlower**, Trenton Miller's independent buyer's guide to SeaFlower in Bradenton, FL (Found Your Florida / LPT Realty, LLC).

- **Build:** `python3 build.py` (Python 3.9+, Pillow for the brand images; no Node, no npm). Output goes to `docs/`, which is what gets deployed.
- **Preview:** `python3 -m http.server 8765 --directory docs` then open http://localhost:8765/
- **Deploy:** see `DEPLOY.md` (GitHub Pages + Squarespace DNS).

## Where things live

| Path | What |
|---|---|
| `gen/config.py` | Site settings: contact details, booking URL, form endpoint, analytics ID, brokerage/licence text, nav, legal texts |
| `gen/content/facts.py` | Community facts, HOA/CDD tables, timeline, schools, drive times (with the as-of date) |
| `gen/content/builder_*.py` | One data module per builder: collections, plans, prices, quick move-ins, models, incentives, sources |
| `gen/content/faqs.py` | The FAQ (grouped by topic; tag `insider` marks Trenton's perspective) |
| `gen/content/posts.py` | Blog articles (site-markdown bodies) |
| `gen/content/videos.py` | YouTube catalog used on the site (embedded via a privacy-enhanced facade; nothing downloaded) |
| `gen/content/testimonials.py` | Reviews quoted verbatim from foundyourflorida.com |
| `gen/pages/*.py` | One module per page or page family; each exposes `pages()` returning page dicts |
| `gen/layout.py`, `gen/components.py`, `gen/html.py` | Page shell (SEO head, JSON-LD, header/footer), reusable components, the small markdown converter |
| `static/` | CSS, JS, images (copied to `docs/assets/`) |
| `tools/make_images.py` | Generates the Open Graph image, favicons and touch icon at build time |

## Updating content

1. Edit the data module (prices in `builder_*.py`, fees in `facts.py`, questions in `faqs.py`, posts in `posts.py`).
2. Bump `SITE["updated"]`/`updated_iso` in `gen/config.py` and `AS_OF` in `facts.py` when facts are re-verified. Pages show "Updated …" badges from these.
3. Run `python3 build.py`, check the QA output, commit and push (GitHub Pages redeploys automatically).

Markdown subset supported in content: `##`/`###` headings, paragraphs, `-` and `1.` lists, `>` quotes, `| tables |`, `---`, `:::trent … :::` callouts (also `:::note`, `:::info`, `:::warn`), raw HTML lines, and inline `**bold**`, `*italic*`, `[text](url)`.

## Lead capture

Forms post JSON to `SITE["form_endpoint"]`, currently FormSubmit (`https://formsubmit.co/ajax/trenton@foundyourflorida.com`), which emails every submission to trenton@foundyourflorida.com. If the endpoint is empty the form falls back to a pre-filled email. The JS also supports the Found Your Florida lead API shape if you point the endpoint at `https://foundyourflorida.com/api/leads`.

Booking uses the Calendly inline widget on `/book/` (`SITE["booking_url"]`). Analytics: GA4 via `SITE["ga_id"]` (events: `generate_lead`, `click_call`, `click_text`, `cta_click`, `video_play`, `faq_open`, `faq_search`, `filter`).

## Generated files

`sitemap.xml`, `robots.txt` (AI crawlers allowed), `llms.txt` and `llms-full.txt` (plain-text mirror for AI search), `feed.xml` (blog RSS), `404.html`, `CNAME`, `site.webmanifest`, favicons and the OG image are all produced by `build.py`.

## Conversion tracking (GA4 → Google Ads)

GA4 measurement ID `G-N1PEN4WMZ7` is installed once per page in `gen/layout.py` (`gtag.js` + one `config`). Add `?ga_debug=1` to any URL to send events to GA4 DebugView.

Two conversion events are emitted from `static/js/main.js`, with non-personal parameters only:

| Event | Fires when | Parameters |
|---|---|---|
| `generate_lead` | FormSubmit returns `{"success":"true"}` for a lead form (never on click, validation error, network error, or on `/thank-you/`) | `method=website_form`, `form_id`, `form_name`, `page_path` |
| `book_appointment` | A `message` from origin `https://calendly.com` with `event: "calendly.event_scheduled"` on `/book/` | `method=calendly`, `event_type=30min_strategy_call`, `page_path` |

Deduplication: a form is marked `data-sent` after one confirmed success and further submits are ignored; the event is sent with `transport_type: beacon` and the redirect to `/thank-you/` happens on `event_callback` (1.2 s fallback). Calendly bookings are keyed by invitee URI in `sessionStorage`, so one booking counts once. No name, email, phone or message text is ever passed to `gtag`.

To import into Google Ads: GA4 Admin → Events → mark `generate_lead` and `book_appointment` as key events; then Google Ads → Goals → Conversions → New → Import → Google Analytics 4 → select both. Do not use a URL-based (`/thank-you/`) conversion; the event import is the reliable path.

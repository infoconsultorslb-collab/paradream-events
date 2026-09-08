# Paradream Events — Website

An exact self-hosted copy of [paradreamlb.com](https://www.paradreamlb.com), migrated
off Strikingly. This uses the **real scraped HTML/CSS from the live site** — same
layout, same theme, same photos — rather than a redesign, so it looks and matches
identically. No build step, no server, no framework: plain static files that can be
hosted anywhere for free (Netlify, Vercel, GitHub Pages, Cloudflare Pages, S3, ...).

## How this was built

1. The live site was mirrored (`wget --mirror`) to capture the real server-rendered
   HTML for every page — same structure, same Strikingly theme CSS (loaded from
   Strikingly's CDN, which stays live independent of hosting), same photos (loaded
   from Strikingly's image CDN directly).
2. One thing doesn't carry over cleanly: Strikingly's booking forms are rendered
   entirely client-side against Strikingly's own backend, so a raw copy would show
   broken, empty form widgets once hosted elsewhere. `tools/build_exact.py` finds
   each page's form container and swaps in a real, working form — same fields, same
   options as the original — wired up as a **Netlify Form** (`data-netlify="true"`),
   so submissions land in the Netlify dashboard / forwarded email with zero backend
   code.
3. Strikingly's own app JavaScript (the bundles that rendered those forms, and would
   otherwise error out trying to reach Strikingly's backend from a different domain)
   is stripped. Everything else — text, images, layout, the theme's own CSS — is
   untouched.

To regenerate the site (e.g. after re-scraping an updated live site, or editing a
form's fields in `tools/build.py`):

```bash
python3 tools/build_exact.py
```

This reads from the raw mirrored HTML (not included in this repo — see below) and
(re)writes every page at the repo root. `tools/build.py` isn't run directly for the
final pages anymore, but `build_exact.py` imports its form field definitions
(`EVENT_FORMS`, `CONTACT_FIELDS`, `JOIN_US_FIELDS`) and rendering helpers, so edit
those there to change a form's fields.

**Note:** `build_exact.py` expects the original mirrored HTML at a local path (see
`MIRROR_DIR` at the top of the script) — it isn't part of this repo since it's just
scraped source material, not a maintained asset. To regenerate from scratch, re-run
the `wget --mirror` capture against the live site and point `MIRROR_DIR` at the
result.

## Preview locally

```bash
python3 -m http.server 8000
```
then open `http://localhost:8000`.

## Deploying (Netlify)

1. Push this repo to GitHub (already done if you're reading this on the deployed branch).
2. On [netlify.com](https://netlify.com), "Add new site" → "Import an existing project" →
   pick this repo. Build command: none. Publish directory: `.` (repo root). Netlify
   auto-detects `netlify.toml`.
3. Once live on its `*.netlify.app` URL, add the custom domain (`paradreamlb.com`)
   under Site settings → Domain management, and update DNS to point at Netlify.
   Netlify issues a free HTTPS certificate automatically.
4. Cancel/downgrade the Strikingly plan once DNS has fully cut over and the new site
   is confirmed working.

## Site structure

Matches the original site's URLs exactly: `/`, `/why-paradream.html`,
`/our-services.html`, `/gallery.html`, `/contact-us.html`, `/join-us.html`,
`/pages/cookie-policy.html`, one page per occasion (`/proposal.html`,
`/engagement.html`, `/bachelor.html`, `/your-big-day.html`,
`/holy-first-communion.html`, `/baptism.html`, `/gender-reveal.html`,
`/birthday-1.html`, `/christmas.html`), and `/portfolio/items/*.html` for each
service category's photo gallery.

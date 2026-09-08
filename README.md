# Paradream Events — Website

A self-hosted rebuild of [paradreamlb.com](https://www.paradreamlb.com), migrated off
Strikingly. Plain static HTML/CSS/JS — no build step, no server, no framework — so it
can be hosted anywhere for free (Netlify, Vercel, GitHub Pages, Cloudflare Pages, S3, ...).

## What's here

- Real content pulled from the live Strikingly site (page text, testimonials, FAQ,
  event booking-form fields, and 200+ photos) and rebuilt as a clean, fast, mobile-friendly
  static site.
- `tools/build.py` — the generator. All page content lives in this one file as plain
  Python data (nav links, testimonials, event form fields, image lists, etc). Edit the
  data at the top, then regenerate:

  ```bash
  python3 tools/build.py
  ```

  This overwrites every `.html` file in the repo (not `assets/`) from the data in the
  script, so it's safe to re-run any time content changes.
- `assets/img/` — photos carried over from the old site.
- `assets/css/style.css`, `assets/js/main.js`, `assets/js/lightbox.js` — shared styling
  and behavior (mobile nav, cookie banner, gallery lightbox).
- Booking forms (`/events/*.html`, `/join-us.html`, `/contact-us.html`) are wired up as
  **Netlify Forms** (`data-netlify="true"`) — submissions land in the Netlify dashboard
  and can be forwarded to email with zero backend code. If you deploy elsewhere, swap
  the form `action`/attributes for that host's form-handling equivalent (e.g. Formspree).

## Preview locally

```bash
python3 -m http.server 8000
```

then open `http://localhost:8000`.

## Deploying (Netlify)

1. Push this repo to GitHub (already done if you're reading this on the deployed branch).
2. On [netlify.com](https://netlify.com), "Add new site" → "Import an existing project" →
   pick this repo. Build command: none. Publish directory: `.` (repo root). Netlify
   auto-detects `netlify.toml` in this repo, which also sets cache headers and 301
   redirects from the old Strikingly URLs (`/bachelor`, `/pages/cookie-policy`, etc.) to
   their new paths, so old links/SEO keep working.
3. Once the site is live on its `*.netlify.app` URL, add the custom domain
   (`paradreamlb.com`) under Site settings → Domain management, and update the domain's
   DNS to point at Netlify (Netlify's UI gives you the exact records to add). Netlify
   issues a free HTTPS certificate automatically.
4. Cancel/downgrade the Strikingly plan once DNS has fully cut over and the new site is
   confirmed working.

Vercel, Cloudflare Pages, and GitHub Pages all work the same way for a static site like
this — just without the `netlify.toml` redirects/forms (those are Netlify-specific;
GitHub Pages needs a plain `_redirects`-free setup and a third-party form service).

## Site structure

- `/`, `/why-paradream.html`, `/our-services.html`, `/gallery.html`, `/contact-us.html`,
  `/join-us.html`, `/cookie-policy.html`
- `/events/*.html` — one booking-request page per occasion (proposal, engagement,
  bachelor, your-big-day, holy-first-communion, baptism, gender-reveal, birthday,
  christmas), each with the real field set from the original site's forms.
- `/portfolio/*.html` — photo galleries per service category (oriental zaffah, circus
  show, inflatable games, table decoration, catering, characters & mascots, photo booth,
  christmas mascots).

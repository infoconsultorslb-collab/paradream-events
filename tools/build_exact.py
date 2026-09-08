#!/usr/bin/env python3
"""
Builds an *exact* copy of the live paradreamlb.com pages, using the real
scraped Strikingly HTML/CSS as-is (same layout, same theme CSS, same
photos loaded straight from Strikingly's CDN) instead of a redesign.

The only thing swapped out is the booking-form widgets: Strikingly renders
those entirely client-side against its own backend, so a plain rehost of
the scraped HTML would show broken, non-functional form skeletons. Those
get replaced with working Netlify Forms using the exact same fields.

Run with: python3 tools/build_exact.py
Requires the raw mirrored HTML in MIRROR_DIR (see README for how it was
produced — this script is not meant to be re-run without that mirror).
"""
import os
import re
from bs4 import BeautifulSoup

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MIRROR_DIR = "/tmp/claude-0/-home-user-paradream-events/ffd02ae3-71df-58be-90df-1451eac3b701/scratchpad/mirror/paradream-mirror/www.paradreamlb.com"

import sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from build import (
    render_form, CONTACT_FIELDS, JOIN_US_FIELDS, EVENT_FORMS, PHONE, PHONE_HREF, BASE,
)

# (mirror filename, output filename, form kind, form key)
# form kind: None (no form), "email" (contact-us simple form), "custom" (event/join forms)
PAGES = [
    ("index.html", "index.html", None, None),
    ("why-paradream.html", "why-paradream.html", None, None),
    ("our-services.html", "our-services.html", None, None),
    ("gallery.html", "gallery.html", None, None),
    ("contact-us.html", "contact-us.html", "email", "contact"),
    ("join-us.html", "join-us.html", "custom", "join-us"),
    ("proposal.html", "proposal.html", "custom", "proposal"),
    ("engagement.html", "engagement.html", "custom", "engagement"),
    ("bachelor.html", "bachelor.html", "custom", "bachelor"),
    ("your-big-day.html", "your-big-day.html", "custom", "your-big-day"),
    ("holy-first-communion.html", "holy-first-communion.html", "custom", "holy-first-communion"),
    ("baptism.html", "baptism.html", "custom", "baptism"),
    ("christmas.html", "christmas.html", "custom", "christmas"),
    ("birthday-1.html", "birthday-1.html", "custom", "birthday"),
    ("gender-reveal.html", "gender-reveal.html", "custom", "gender-reveal"),
    ("pages/cookie-policy.html", "pages/cookie-policy.html", None, None),
    ("portfolio/items/catering-services.html", "portfolio/items/catering-services.html", None, None),
    ("portfolio/items/characters-mascots.html", "portfolio/items/characters-mascots.html", None, None),
    ("portfolio/items/christmas-mascots.html", "portfolio/items/christmas-mascots.html", None, None),
    ("portfolio/items/circus-show.html", "portfolio/items/circus-show.html", None, None),
    ("portfolio/items/inflatable-games.html", "portfolio/items/inflatable-games.html", None, None),
    ("portfolio/items/oriental-zaffah.html", "portfolio/items/oriental-zaffah.html", None, None),
    ("portfolio/items/orientalzaffah.html", "portfolio/items/orientalzaffah.html", None, None),
    ("portfolio/items/photo-booth-entertainment.html", "portfolio/items/photo-booth-entertainment.html", None, None),
    ("portfolio/items/table-decoration-set-up.html", "portfolio/items/table-decoration-set-up.html", None, None),
]

STRIKINGLY_JS_HOST = "static-assets.strikinglycdn.com"


def strip_strikingly_scripts(soup):
    for tag in soup.find_all("script"):
        src = tag.get("src", "")
        if STRIKINGLY_JS_HOST in src:
            tag.decompose()
    # the giant inline $S config blob is only useful to the JS we just removed
    for tag in soup.find_all("script"):
        if not tag.get("src") and tag.string and "window.$S=" in (tag.string or ""):
            tag.decompose()


def inject_my_js_and_css(soup):
    if soup.head:
        link = soup.new_tag("link", rel="stylesheet", href=f"{BASE}/assets/css/site-extra.css")
        soup.head.append(link)
    if soup.body:
        script = soup.new_tag("script", src=f"{BASE}/assets/js/main.js")
        soup.body.append(script)


def replace_form(soup, kind, key):
    if kind == "email":
        node = soup.select_one(".s-component.s-form.s-email-form") or soup.select_one(".s-email-form")
        fields = CONTACT_FIELDS
        form_name = "contact"
        submit_label = "Submit"
    else:
        node = soup.select_one(".s-custom-form-container")
        if key == "join-us":
            fields = JOIN_US_FIELDS
            form_name = "join-us"
            submit_label = "Submit Application"
        else:
            fields = EVENT_FORMS[key]
            form_name = key
            submit_label = "Submit Booking Request"

    if node is None:
        print(f"  WARNING: form container not found for {key}")
        return

    replacement_html = f"""<div class="pf-scope" style="padding:3rem 1rem;max-width:700px;margin:0 auto;">
{render_form(form_name, fields, submit_label)}
</div>"""
    replacement = BeautifulSoup(replacement_html, "html.parser")
    node.replace_with(replacement)


def process(mirror_name, out_name, form_kind, form_key):
    src_path = os.path.join(MIRROR_DIR, mirror_name)
    html = open(src_path, encoding="utf-8", errors="replace").read()
    soup = BeautifulSoup(html, "html.parser")

    strip_strikingly_scripts(soup)
    inject_my_js_and_css(soup)
    if form_kind:
        replace_form(soup, form_kind, form_key)

    out_path = os.path.join(ROOT, out_name)
    os.makedirs(os.path.dirname(out_path) or ".", exist_ok=True)
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(str(soup))
    print("wrote", out_name)


if __name__ == "__main__":
    for mirror_name, out_name, form_kind, form_key in PAGES:
        process(mirror_name, out_name, form_kind, form_key)
    print("\nDone.")

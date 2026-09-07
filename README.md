# Paradream Events — Website

Migration of [paradreamlb.com](https://www.paradreamlb.com) off Strikingly to a
self-hosted static site, deployed on Netlify/Vercel.

## Status

Waiting on a mirrored copy of the live site's content/assets (see below) before
the actual site code lands here.

## How to get me the mirrored site

Strikingly doesn't offer a native "export my code" button, so the plan is to
mirror the live, published site from your own machine (this sandbox's network
access is locked down and can't reach paradreamlb.com directly).

1. Install `wget` if you don't have it (macOS: `brew install wget`, most Linux
   distros already have it, Windows: use WSL or a `wget` build).
2. Run a full mirror of the live site:

   ```bash
   wget --mirror \
        --convert-links \
        --adjust-extension \
        --page-requisites \
        --no-parent \
        -P paradream-mirror \
        https://www.paradreamlb.com
   ```

   This walks every linked page (home, `/join-us`, `/bachelor`, `/baptism`,
   etc.), rewrites links to work locally, and pulls down images/CSS/JS into
   `paradream-mirror/`.

3. Zip the result: `zip -r paradream-mirror.zip paradream-mirror`
4. Hand it off one of two ways:
   - Attach/drop the zip in the chat with Claude, and mention its path — Claude
     will unzip it into this repo and clean it up into a real static site.
   - Or push the raw mirrored files yourself to this repo's
     `claude/paradream-migration-rady2m` branch under a `mirror/` folder, and
     tell Claude it's there.

## Plan once content is in hand

1. Turn the raw mirror into clean, de-duplicated static HTML/CSS/JS (Strikingly
   markup tends to be heavy — this gets trimmed to something maintainable).
2. Re-host images/fonts locally instead of pointing at Strikingly's CDN.
3. Add a `netlify.toml` (or `vercel.json`) for one-click deploys.
4. Wire up the custom domain (`paradreamlb.com`) to point at Netlify/Vercel
   instead of Strikingly once the new site is verified working.

# app-legal

Public legal pages for Seng2HS Android apps (GitHub Pages).

## Enable Pages

1. Repo **Settings → Pages**
2. Source: **Deploy from a branch**
3. Branch: `main` · Folder: `/docs`
4. Save

## URLs

Base: `https://seng2hs.github.io/app-legal/`

| App | Privacy |
|---|---|
| ChalkBoard | https://seng2hs.github.io/app-legal/chalkboard/privacy.html |
| CapitalNest | https://seng2hs.github.io/app-legal/capital-nest/privacy.html |
| KnoSpar | https://seng2hs.github.io/app-legal/knospar/privacy.html |
| PaperShelf | https://seng2hs.github.io/app-legal/paper-shelf/privacy.html |
| UniversalKit | https://seng2hs.github.io/app-legal/universal-kit/privacy.html |

Same folder for `terms.html`, `support.html`, `deletion.html`.

## Add a new app later

Create `docs/your-app-slug/` with:

- `index.html`
- `privacy.html`
- `terms.html`
- `support.html`
- `deletion.html`

Then link it from `docs/index.html` (or re-run `python tool/generate_site.py` after editing the script).

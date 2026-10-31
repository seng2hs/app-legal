# app-legal

CapitalNest-style product + legal sites for all Seng2HS Android apps (GitHub Pages).

## Enable Pages

1. Repo **Settings → Pages**
2. Source: **Deploy from a branch**
3. Branch: `main` · Folder: `/docs`
4. Save

## Generate / refresh sites

Template CSS/JS: `D:\Work\Senthil\capitalnest-policy`

```powershell
python tool/generate_site.py
```

Writes each app under `docs/<slug>/` (home, privacy, terms, support, deletion, themed css/js/assets).

## URLs

Hub: https://seng2hs.github.io/app-legal/

| App | Home | Privacy |
|---|---|---|
| ChalkBoard | [/chalkboard/](https://seng2hs.github.io/app-legal/chalkboard/) | [privacy](https://seng2hs.github.io/app-legal/chalkboard/privacy.html) |
| CapitalNest | [/capital-nest/](https://seng2hs.github.io/app-legal/capital-nest/) | [privacy](https://seng2hs.github.io/app-legal/capital-nest/privacy.html) |
| KnoSpar | [/knospar/](https://seng2hs.github.io/app-legal/knospar/) | [privacy](https://seng2hs.github.io/app-legal/knospar/privacy.html) |
| PaperShelf | [/paper-shelf/](https://seng2hs.github.io/app-legal/paper-shelf/) | [privacy](https://seng2hs.github.io/app-legal/paper-shelf/privacy.html) |
| UniversalKit | [/universal-kit/](https://seng2hs.github.io/app-legal/universal-kit/) | [privacy](https://seng2hs.github.io/app-legal/universal-kit/privacy.html) |

Same folder also has `terms.html`, `support.html`, `deletion.html`.

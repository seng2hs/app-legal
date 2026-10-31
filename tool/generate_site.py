from pathlib import Path

ROOT = Path(__file__).resolve().parents[1] / "docs"
ROOT.mkdir(parents=True, exist_ok=True)

APPS = [
    {
        "slug": "chalkboard",
        "name": "ChalkBoard",
        "tagline": "Teacher whiteboard for live screen-share lessons",
        "about": (
            "ChalkBoard is a digital whiteboard for teachers — write, graph, "
            "import media, and present while students watch over Meet or Teams."
        ),
        "data": (
            "Board documents, pages, drawings, imported images/PDFs, and "
            "settings are stored locally on your device."
        ),
        "permissions": [
            "Camera / photos — only when you capture or import images onto the board.",
            "Storage / files — only when you import or export a PDF.",
            "Internet — ads (when enabled) and optional Play Store update checks.",
        ],
        "ads": True,
    },
    {
        "slug": "capital-nest",
        "name": "CapitalNest",
        "tagline": "Personal finance and capital tracking",
        "about": (
            "CapitalNest helps you track and organize personal finance "
            "information on your device."
        ),
        "data": (
            "Finance-related entries and app settings you enter are stored "
            "locally on your device unless a feature explicitly syncs elsewhere."
        ),
        "permissions": [
            "Internet — if the app uses online features, ads, or updates.",
            "Storage — only when you import/export files you choose.",
        ],
        "ads": True,
    },
    {
        "slug": "knospar",
        "name": "KnoSpar",
        "tagline": "Knowledge and learning tools",
        "about": (
            "KnoSpar provides learning and knowledge tools for personal use "
            "on your device."
        ),
        "data": (
            "Content and settings you create in the app are stored locally "
            "on your device unless a feature explicitly syncs elsewhere."
        ),
        "permissions": [
            "Internet — if the app uses online features, ads, or updates.",
            "Storage / media — only when you choose to import or share files.",
        ],
        "ads": True,
    },
    {
        "slug": "paper-shelf",
        "name": "PaperShelf",
        "tagline": "Documents and reading shelf",
        "about": (
            "PaperShelf helps you keep and organize documents and reading "
            "material on your device."
        ),
        "data": (
            "Documents, library metadata, and settings are stored locally "
            "on your device unless a feature explicitly syncs elsewhere."
        ),
        "permissions": [
            "Storage / files — when you import, open, or export documents.",
            "Internet — if the app uses online features, ads, or updates.",
        ],
        "ads": True,
    },
    {
        "slug": "universal-kit",
        "name": "UniversalKit",
        "tagline": "Everyday utility toolkit",
        "about": (
            "UniversalKit is a collection of everyday utility tools that run "
            "on your device."
        ),
        "data": (
            "Tool preferences and content you create are stored locally on "
            "your device unless a feature explicitly syncs elsewhere."
        ),
        "permissions": [
            "Internet — if the app uses online features, ads, or updates.",
            (
                "Device features — only when a tool you open needs them "
                "(for example camera or files), and only after you use that tool."
            ),
        ],
        "ads": True,
    },
]

UPDATED = "31 October 2026"

CSS = """
:root {
  --ink: #1c1c1c;
  --accent: #0f766e;
  --accent-tint: #e6f4f2;
  --slate: #334155;
  --muted: #6b7280;
  --line: #e7e2dc;
  --paper: #ffffff;
  --bg: #f7f5f2;
}
* { box-sizing: border-box; }
body {
  margin: 0;
  font-family: "Segoe UI", system-ui, -apple-system, sans-serif;
  background: var(--bg);
  color: var(--ink);
  line-height: 1.6;
}
a { color: var(--accent); text-decoration: none; }
a:hover { text-decoration: underline; }
.wrap { max-width: 760px; margin: 0 auto; padding: 28px 20px 64px; }
.nav {
  display: flex; flex-wrap: wrap; gap: 8px 16px;
  align-items: center; justify-content: space-between;
  margin-bottom: 24px; padding-bottom: 14px; border-bottom: 1px solid var(--line);
}
.brand { font-weight: 800; letter-spacing: -0.03em; color: var(--ink); text-decoration: none; }
.brand small { color: var(--accent); font-weight: 600; margin-left: 8px; }
.nav-links { display: flex; flex-wrap: wrap; gap: 12px; font-size: 0.9rem; font-weight: 600; }
.card {
  background: var(--paper); border: 1px solid var(--line); border-radius: 16px;
  padding: 28px 24px; box-shadow: 0 10px 28px rgba(28,28,28,.06);
}
h1 { margin: 0 0 8px; font-size: 1.7rem; letter-spacing: -0.03em; }
h2 { margin: 1.5em 0 .45em; font-size: 1.05rem; }
.meta { color: var(--muted); font-size: .9rem; margin-bottom: 18px; }
p, li { color: var(--slate); font-size: .97rem; }
ul { padding-left: 1.15em; }
li { margin: .35em 0; }
.grid { display: grid; gap: 12px; }
@media (min-width: 640px) { .grid { grid-template-columns: 1fr 1fr; } }
.app-card {
  display: block; background: var(--paper); border: 1px solid var(--line);
  border-radius: 14px; padding: 18px 16px; text-decoration: none; color: inherit;
}
.app-card:hover { border-color: var(--accent); text-decoration: none; }
.app-card strong { display: block; font-size: 1.05rem; margin-bottom: 4px; }
.app-card span { color: var(--muted); font-size: .88rem; }
.hero { text-align: center; padding: 12px 8px 4px; }
.hero p { max-width: 36em; margin: 10px auto 18px; }
.footer { margin-top: 26px; text-align: center; color: var(--muted); font-size: .85rem; }
.badge {
  display: inline-block; background: var(--accent-tint); color: var(--accent);
  font-size: .75rem; font-weight: 700; padding: 3px 8px; border-radius: 99px; margin-bottom: 10px;
}
"""


def nav(app=None):
    if app:
        brand_href = "../index.html"
        brand = (
            f'<a class="brand" href="{brand_href}">app-legal'
            f'<small>{app["name"]}</small></a>'
        )
        links = """
        <div class="nav-links">
          <a href="index.html">About</a>
          <a href="privacy.html">Privacy</a>
          <a href="terms.html">Terms</a>
          <a href="support.html">Support</a>
          <a href="deletion.html">Deletion</a>
        </div>"""
    else:
        brand = '<a class="brand" href="index.html">app-legal</a>'
        links = '<div class="nav-links"><a href="#apps">Apps</a></div>'
    return f'<nav class="nav">{brand}{links}</nav>'


def page(title, body, app=None):
    css = "../styles.css" if app else "styles.css"
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1" />
  <title>{title}</title>
  <meta name="description" content="{title}" />
  <link rel="stylesheet" href="{css}" />
</head>
<body>
  <div class="wrap">
    {nav(app)}
    {body}
    <p class="footer">Hosted for Google Play / AdMob · Last updated {UPDATED}</p>
  </div>
</body>
</html>
"""


def privacy_body(app):
    perms = "\n".join(f"<li>{p}</li>" for p in app["permissions"])
    ads = ""
    if app["ads"]:
        ads = f"""
        <h2>3. Advertising</h2>
        <ul>
          <li>Store builds of {app["name"]} may show ads through Google AdMob.</li>
          <li>AdMob/Google may collect device identifiers and usage data under Google’s policies.</li>
          <li>Google Privacy Policy: <a href="https://policies.google.com/privacy" rel="noopener">https://policies.google.com/privacy</a></li>
        </ul>"""
    return f"""
    <article class="card">
      <div class="badge">{app["name"]}</div>
      <h1>Privacy Policy</h1>
      <p class="meta">Last updated: {UPDATED}</p>
      <p>{app["about"]}</p>
      <h2>1. Information we store</h2>
      <ul>
        <li>{app["data"]}</li>
        <li>We do not require an account to use the core app experience described here.</li>
        <li>We do not sell your personal information.</li>
      </ul>
      <h2>2. Permissions</h2>
      <ul>
        {perms}
      </ul>
      {ads}
      <h2>4. Children’s privacy</h2>
      <ul>
        <li>{app["name"]} is intended for general users / educators as described in the store listing.</li>
        <li>Do not enter sensitive personal data about children beyond what a feature clearly needs.</li>
      </ul>
      <h2>5. Sharing</h2>
      <ul>
        <li>Your content stays on your device unless you export, share, or use an online feature that sends data.</li>
      </ul>
      <h2>6. Contact</h2>
      <ul>
        <li>Questions: use <a href="support.html">Support</a> or the contact details on the Google Play listing.</li>
        <li>Data deletion: see <a href="deletion.html">Account / Data Deletion</a>.</li>
      </ul>
      <p>We may update this policy when the app changes. Continued use means you accept the updated policy.</p>
    </article>"""


def terms_body(app):
    return f"""
    <article class="card">
      <div class="badge">{app["name"]}</div>
      <h1>Terms of Use</h1>
      <p class="meta">Last updated: {UPDATED}</p>
      <p>By using {app["name"]} (“the App”), you agree to these Terms.</p>
      <h2>1. The App</h2>
      <ul>
        <li>{app["about"]}</li>
        <li>Features may change as we improve the App.</li>
      </ul>
      <h2>2. Your content</h2>
      <ul>
        <li>You own content you create.</li>
        <li>You are responsible for what you enter, import, export, or share.</li>
        <li>Do not use the App for unlawful, harmful, or infringing content.</li>
      </ul>
      <h2>3. Acceptable use</h2>
      <ul>
        <li>Use the App for personal / intended educational or productivity purposes.</li>
        <li>Do not reverse engineer, abuse ads, or disrupt the App.</li>
      </ul>
      <h2>4. Ads and updates</h2>
      <ul>
        <li>Store builds may show advertisements.</li>
        <li>Updates may be delivered through Google Play.</li>
      </ul>
      <h2>5. Disclaimer</h2>
      <ul>
        <li>The App is provided “as is” without warranties of any kind.</li>
        <li>We are not liable for lost data, device issues, or third-party services (including ads or Play Store).</li>
        <li>Export or back up important work if you need a copy outside the device.</li>
      </ul>
      <h2>6. Changes</h2>
      <ul>
        <li>We may update these Terms. Continued use after an update means you accept them.</li>
      </ul>
      <h2>7. Contact</h2>
      <ul>
        <li>See <a href="support.html">Support</a> or the Play Store listing.</li>
      </ul>
    </article>"""


def support_body(app):
    return f"""
    <article class="card">
      <div class="badge">{app["name"]}</div>
      <h1>Support</h1>
      <p class="meta">How to get help with {app["name"]}</p>
      <p>{app["about"]}</p>
      <h2>Contact</h2>
      <ul>
        <li>Use the support email published on the Google Play listing for {app["name"]}.</li>
        <li>Include your device model, Android version, and a short description of the issue.</li>
      </ul>
      <h2>Common topics</h2>
      <ul>
        <li>App not opening / crash — update from Play Store, then reinstall if needed.</li>
        <li>Permissions — enable Camera / Files only if you use those features.</li>
        <li>Ads — store builds may show ads; special builds may hide them.</li>
      </ul>
      <h2>Legal</h2>
      <ul>
        <li><a href="privacy.html">Privacy Policy</a></li>
        <li><a href="terms.html">Terms of Use</a></li>
        <li><a href="deletion.html">Account / Data Deletion</a></li>
      </ul>
    </article>"""


def deletion_body(app):
    return f"""
    <article class="card">
      <div class="badge">{app["name"]}</div>
      <h1>Account / Data Deletion</h1>
      <p class="meta">Last updated: {UPDATED}</p>
      <p>
        {app["name"]} primarily stores data on your device. This page explains how to remove that data
        and how to request deletion of any data held by us (if applicable).
      </p>
      <h2>1. Delete data on your device</h2>
      <ul>
        <li>Open Android <strong>Settings → Apps → {app["name"]} → Storage → Clear data</strong> (wording may vary by device).</li>
        <li>Or uninstall {app["name"]} to remove the app and its local app data from that device.</li>
      </ul>
      <h2>2. If you shared content</h2>
      <ul>
        <li>Files you exported (for example PDF or shared documents) live where you saved/shared them — delete those copies separately.</li>
      </ul>
      <h2>3. Request deletion from the developer</h2>
      <ul>
        <li>If you believe we hold personal data about you outside the device (for example support email correspondence), contact us via the Play Store listing or <a href="support.html">Support</a>.</li>
        <li>Include the app name (<strong>{app["name"]}</strong>), your contact email, and what you want deleted.</li>
        <li>We will respond within a reasonable time and delete or anonymize developer-held personal data when required, except where we must retain it for legal reasons.</li>
      </ul>
      <h2>4. Advertising partners</h2>
      <ul>
        <li>Ad networks such as Google AdMob may process device identifiers under their own policies. See Google’s tools and privacy policy for ad-related choices.</li>
      </ul>
    </article>"""


def app_index_body(app):
    return f"""
    <div class="card hero">
      <div class="badge">App legal pages</div>
      <h1>{app["name"]}</h1>
      <p>{app["tagline"]}</p>
      <p>{app["about"]}</p>
      <p>
        <a href="privacy.html">Privacy Policy</a> ·
        <a href="terms.html">Terms of Use</a> ·
        <a href="support.html">Support</a> ·
        <a href="deletion.html">Data Deletion</a>
      </p>
    </div>"""


def main():
    (ROOT / "styles.css").write_text(CSS.strip() + "\n", encoding="utf-8")

    cards = "\n".join(
        f"""<a class="app-card" href="{a["slug"]}/index.html">
  <strong>{a["name"]}</strong>
  <span>{a["tagline"]}</span>
</a>"""
        for a in APPS
    )
    root_body = f"""
<div class="card hero">
  <h1>App legal hub</h1>
  <p>
    Public Privacy Policy, Terms, Support, and Data Deletion pages for Seng2HS apps.
    Use these URLs in Google Play Console and AdMob.
  </p>
</div>
<h2 id="apps" style="margin-top:22px">Apps</h2>
<div class="grid">
{cards}
</div>
"""
    (ROOT / "index.html").write_text(
        page("App legal hub — Seng2HS", root_body), encoding="utf-8"
    )

    for app in APPS:
        d = ROOT / app["slug"]
        d.mkdir(parents=True, exist_ok=True)
        pages = {
            "index.html": (f"{app['name']} — Legal", app_index_body(app)),
            "privacy.html": (f"Privacy Policy — {app['name']}", privacy_body(app)),
            "terms.html": (f"Terms of Use — {app['name']}", terms_body(app)),
            "support.html": (f"Support — {app['name']}", support_body(app)),
            "deletion.html": (f"Data Deletion — {app['name']}", deletion_body(app)),
        }
        for fname, (title, body) in pages.items():
            (d / fname).write_text(page(title, body, app), encoding="utf-8")

    readme = """# app-legal

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
"""
    (ROOT.parent / "README.md").write_text(readme, encoding="utf-8")
    print("OK", ROOT)
    print("html files:", len(list(ROOT.rglob("*.html"))))


if __name__ == "__main__":
    main()

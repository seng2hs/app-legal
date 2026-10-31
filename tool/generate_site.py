"""
Build CapitalNest-style marketing + legal sites for all apps
inside D:/Work/Senthil/app-legal/docs/<slug>/.

Template CSS/JS come from D:/Work/Senthil/capitalnest-policy.
Publish via GitHub Pages on app-legal (branch main, /docs).
"""

from __future__ import annotations

import re
import shutil
from pathlib import Path

from PIL import Image

SRC = Path(r"D:\Work\Senthil\capitalnest-policy")
ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
BASE = "https://seng2hs.github.io/app-legal"

APPS = [
    {
        "slug": "chalkboard",
        "name": "ChalkBoard",
        "tag": "Teach. Draw. Share.",
        "domain": f"{BASE}/chalkboard",
        "email": "support@chalkboard.app",
        "logo": Path(r"D:\Work\Senthil\ChalkBoard\design\brand\chalkboard_logo_icon.png"),
        "theme": "#0F766E",
        "theme_dark": "#115E59",
        "theme_light": "#0D9488",
        "accent": "#14B8A6",
        "accent_soft": "#E6F4F2",
        "bg": "#F7F5F2",
        "bg_muted": "#F1EEE9",
        "border": "#E7E2DC",
        "shadow_rgb": "15, 118, 110",
        "hero_badge": "Live Lessons · Screen Share Ready",
        "hero_title_html": 'Teach.<br>Draw.<br><span class="accent">Share.</span>',
        "hero_sub": "The teacher whiteboard built for live classes.",
        "hero_desc": (
            "Write, annotate, graph, import camera/PDF pages, and present while "
            "students watch over Google Meet or Teams — clean boards for clear teaching."
        ),
        "keywords": "teacher whiteboard, digital chalkboard, live teaching, screen share, graph, latex, pdf import, ChalkBoard",
        "category": "EducationalApplication",
        "trust": [
            "Offline Boards",
            "Private on Device",
            "PDF Import/Export",
            "STEM Graphs",
            "Presenter Mode",
            "Multi-page Lessons",
        ],
        "features": [
            ("Write & Annotate", "Pens, markers, shapes and text on a calm teaching canvas."),
            ("STEM Graphs", "Plot functions and explore parameters during live explanation."),
            ("LaTeX", "Add math notation without leaving the board."),
            ("Camera & Gallery", "Snap or import photos as lesson pages."),
            ("PDF Pages", "Import PDF pages onto the board for annotation."),
            ("Export PDF", "Share the lesson board as a PDF after class."),
            ("Presenter Mode", "Hide chrome for clean Meet / Teams screen share."),
            ("Multi Documents", "Switch named lessons and keep editing context clear."),
        ],
        "benefits_title": "Built for Teachers. Designed for Clarity.",
        "benefits_desc": (
            "Whether you teach tuition, school, or coaching classes, ChalkBoard keeps "
            "the focus on the board — not on complicated menus."
        ),
        "benefits": [
            ("Privacy First", "Lesson boards stay on your device unless you export them."),
            ("Offline Ready", "Teach without depending on a cloud account."),
            ("Live Class Fit", "Presenter mode keeps screen share tidy for students."),
            ("Simple Flow", "Pick up the pen and teach — tools stay out of the way."),
        ],
        "data_items": [
            "Board documents and pages",
            "Ink strokes, shapes, text, graphs and LaTeX",
            "Imported images and PDF page renders",
            "App settings and preferences",
        ],
        "permissions": [
            ("Camera / photos", "Only when you capture or import images."),
            ("Storage / files", "Only when you import or export PDF."),
            ("Internet", "Ads (free/store builds) and optional Play update checks."),
        ],
        "faqs": [
            (
                "Is my lesson data stored in the cloud?",
                "No. Boards are stored locally on your device unless you export or share a PDF yourself.",
            ),
            (
                "How do I delete my data?",
                "Clear app storage in Android Settings, or uninstall ChalkBoard. See the Data Deletion page for steps.",
            ),
            (
                "Does ChalkBoard show ads?",
                "Store builds may show Google AdMob ads. Special offline builds can hide ads.",
            ),
            (
                "How do I contact support?",
                "Use the Contact page. Include your device model and a short description of the issue.",
            ),
        ],
        "deletion_steps": [
            "Open Android <strong>Settings → Apps → ChalkBoard → Storage → Clear data</strong>.",
            "Or uninstall <strong>ChalkBoard</strong> to remove the app and local lesson data from that device.",
            "Delete any PDF exports you shared separately (they live where you saved them).",
        ],
    },
    {
        "slug": "capital-nest",
        "name": "CapitalNest",
        "tag": "Your Personal Wealth Companion",
        "domain": f"{BASE}/capital-nest",
        "email": "support@capitalnest.app",
        "logo": Path(r"D:\Work\Senthil\CapitalNestApp\capitalnestapp\assets\branding\app_icon.png"),
        "theme": "#0F5D31",
        "theme_dark": "#0A3F22",
        "theme_light": "#147A40",
        "accent": "#24A148",
        "accent_soft": "#E8F8EE",
        "bg": "#F8FAF9",
        "bg_muted": "#F1F5F3",
        "border": "#E2EBE5",
        "shadow_rgb": "15, 93, 49",
        "hero_badge": "Offline Finance · Privacy First",
        "hero_title_html": 'Track.<br>Grow.<br><span class="accent">Wealth.</span>',
        "hero_sub": "Offline personal finance and wealth manager.",
        "hero_desc": (
            "Track fixed deposits, RD, loans, lending, cash flow, income, expenses "
            "and portfolio — private money manager that stays on your device."
        ),
        "keywords": "fixed deposit, fd tracker, rd tracker, wealth manager, finance tracker, money manager, CapitalNest",
        "category": "FinanceApplication",
        "trust": [
            "Offline First",
            "Private on Device",
            "FD & RD Tracking",
            "Loan Tracker",
            "Cash Flow",
            "Portfolio View",
        ],
        "features": [
            ("FD Tracker", "Track fixed deposits, maturity and interest clearly."),
            ("RD Tracker", "Follow recurring deposits and projected returns."),
            ("Loans & Lending", "Keep borrow and lend records organized."),
            ("Cash Flow", "See income and expense movement in one place."),
            ("Portfolio", "Understand distribution across your wealth buckets."),
            ("Calculators", "FD/RD interest helpers when you need a quick check."),
            ("Local Storage", "Records stay on-device by default."),
            ("Clean Reports", "Simple insights without a noisy dashboard."),
        ],
        "benefits_title": "Built for Everyone. Designed for You.",
        "benefits_desc": (
            "Whether you need an FD tracker, RD tracker, loan tracker or a full "
            "personal finance wealth manager, CapitalNest keeps everything organized."
        ),
        "benefits": [
            ("Privacy First", "Financial records stay on your device. We don’t sell your data."),
            ("Offline Storage", "Works without forcing a cloud account for core use."),
            ("Smart Insights", "Clear reports help you act before maturities and dues."),
            ("Simple Interface", "Calm UI so reviewing wealth feels effortless."),
        ],
        "data_items": [
            "FD, RD, loan, lending and cash-flow records you enter",
            "Portfolio and report preferences",
            "Optional imported/exported files",
            "App settings",
        ],
        "permissions": [
            ("Storage / files", "Only when you import or export files."),
            ("Internet", "Ads (if enabled), updates, and optional online features."),
            ("Notifications", "Only if you enable maturity or due reminders."),
        ],
        "faqs": [
            (
                "Is my finance data stored in the cloud?",
                "Core records are designed to stay on your device. See the Privacy Policy for details.",
            ),
            (
                "How do I delete my data?",
                "Clear app storage or uninstall CapitalNest. See the Data Deletion page.",
            ),
            (
                "Does CapitalNest show ads?",
                "Store builds may show ads. Details are in the Privacy Policy.",
            ),
            (
                "How do I contact support?",
                "Use the Contact page with your device model and a short description of the issue.",
            ),
        ],
        "deletion_steps": [
            "Open Android <strong>Settings → Apps → CapitalNest → Storage → Clear data</strong>.",
            "Or uninstall <strong>CapitalNest</strong> to remove local finance data from that device.",
            "Delete any exports you saved outside the app separately.",
        ],
    },
    {
        "slug": "knospar",
        "name": "KnoSpar",
        "tag": "Learn. Practice. Grow.",
        "domain": f"{BASE}/knospar",
        "email": "support@knospar.app",
        "logo": Path(r"D:\Work\Senthil\KnoSpar\assets\brand\play_store_icon_512.png"),
        "theme": "#4F46E5",
        "theme_dark": "#3730A3",
        "theme_light": "#6366F1",
        "accent": "#818CF8",
        "accent_soft": "#EEF2FF",
        "bg": "#F8F9FC",
        "bg_muted": "#F1F3F9",
        "border": "#E2E5F0",
        "shadow_rgb": "79, 70, 229",
        "hero_badge": "Knowledge Tools · Private Learning",
        "hero_title_html": 'Learn.<br>Practice.<br><span class="accent">Grow.</span>',
        "hero_sub": "Knowledge tools that stay on your device.",
        "hero_desc": (
            "KnoSpar helps you organize learning, practice concepts, and keep study "
            "materials handy — without forcing a cloud account for core use."
        ),
        "keywords": "learning app, knowledge tools, study, practice, education, KnoSpar",
        "category": "EducationalApplication",
        "trust": [
            "On-device Focus",
            "Private by Default",
            "Simple Study Flow",
            "Fast Access",
            "Local Content",
            "Play Updates",
        ],
        "features": [
            ("Study Content", "Keep learning material organized for quick revision."),
            ("Practice Flow", "Work through concepts at your own pace."),
            ("Local Storage", "Your progress and notes stay on the device."),
            ("Clean UI", "A calm interface so studying stays focused."),
            ("Reminders", "Optional nudges when you enable notifications."),
            ("Import / Share", "Bring files in or share outputs when you choose."),
            ("Offline Friendly", "Core learning continues without constant internet."),
            ("Updates", "Improvements delivered through Google Play."),
        ],
        "benefits_title": "Built for Learners. Designed for Focus.",
        "benefits_desc": (
            "KnoSpar keeps learning practical and private — so you spend time on "
            "understanding, not on account setup."
        ),
        "benefits": [
            ("Privacy First", "Learning content stays local unless you share it."),
            ("Less Friction", "Open the app and continue where you left off."),
            ("Your Pace", "Practice without pressure from social feeds."),
            ("Clear Support", "Contact us when something blocks your progress."),
        ],
        "data_items": [
            "Study notes and learning content you create",
            "Progress and preferences",
            "Optional imported files",
            "App settings",
        ],
        "permissions": [
            ("Notifications", "Only if you enable reminders."),
            ("Storage / files", "Only when you import or export files."),
            ("Internet", "Ads (if enabled), updates, and optional online features."),
        ],
        "faqs": [
            (
                "Does KnoSpar require an account?",
                "Core use is designed to work on-device. Any future account features will be optional and clearly disclosed.",
            ),
            (
                "How do I delete my data?",
                "Clear app storage or uninstall KnoSpar. See the Data Deletion page.",
            ),
            (
                "Are there ads?",
                "Store builds may show ads. Details are in the Privacy Policy.",
            ),
            (
                "How do I get support?",
                "Use the Contact page with your device details and issue description.",
            ),
        ],
        "deletion_steps": [
            "Open Android <strong>Settings → Apps → KnoSpar → Storage → Clear data</strong>.",
            "Or uninstall <strong>KnoSpar</strong> to remove local app data.",
            "Remove any files you exported/shared outside the app separately.",
        ],
    },
    {
        "slug": "paper-shelf",
        "name": "PaperShelf",
        "tag": "Your documents. Your shelf.",
        "domain": f"{BASE}/paper-shelf",
        "email": "support@papershelf.app",
        "logo": Path(r"D:\Work\Senthil\PaperShelf\assets\branding\logo.png"),
        "theme": "#B45309",
        "theme_dark": "#92400E",
        "theme_light": "#D97706",
        "accent": "#F59E0B",
        "accent_soft": "#FFFBEB",
        "bg": "#FFFCF7",
        "bg_muted": "#F7F1E8",
        "border": "#EDE4D5",
        "shadow_rgb": "180, 83, 9",
        "hero_badge": "Documents · Private Shelf",
        "hero_title_html": 'Keep.<br>Organize.<br><span class="accent">Read.</span>',
        "hero_sub": "A calm shelf for the papers that matter.",
        "hero_desc": (
            "PaperShelf helps you keep documents and reading material organized on "
            "your device — find what you need without clutter."
        ),
        "keywords": "documents, pdf organizer, reading, paper shelf, file library, PaperShelf",
        "category": "ProductivityApplication",
        "trust": [
            "Local Library",
            "Private Files",
            "Quick Find",
            "Import Friendly",
            "Clean Layout",
            "Play Updates",
        ],
        "features": [
            ("Document Shelf", "Keep PDFs and papers in one organized place."),
            ("Quick Browse", "Find documents without digging through folders."),
            ("Import Files", "Add documents when you choose to import them."),
            ("Reading Focus", "A simple layout for less distraction."),
            ("Local First", "Your library stays on the device by default."),
            ("Share Out", "Export or share files only when you decide."),
            ("Search Ready", "Locate items faster as your shelf grows."),
            ("Lightweight", "Built to feel quick on everyday Android phones."),
        ],
        "benefits_title": "Built for Documents. Designed for Calm.",
        "benefits_desc": (
            "PaperShelf is for people who want a private, tidy place for reading "
            "and reference material — without a complicated DMS."
        ),
        "benefits": [
            ("Privacy First", "Documents stay local unless you share them."),
            ("Less Clutter", "A shelf metaphor keeps things understandable."),
            ("Your Library", "Import what you need; leave the rest out."),
            ("Support Path", "Contact us if import or reading flow breaks."),
        ],
        "data_items": [
            "Document library metadata",
            "Files you import into the app",
            "Reading preferences",
            "App settings",
        ],
        "permissions": [
            ("Storage / files", "When you import, open, or export documents."),
            ("Internet", "Ads (if enabled), updates, and optional online features."),
        ],
        "faqs": [
            (
                "Where are my documents stored?",
                "Primarily on your device. Shared/exported copies live wherever you saved them.",
            ),
            (
                "How do I delete my library?",
                "Clear app storage or uninstall PaperShelf. See Data Deletion for steps.",
            ),
            (
                "Does PaperShelf upload my PDFs?",
                "Core library use is local-first. Online features, if added, will be disclosed in Privacy Policy updates.",
            ),
            (
                "How do I contact support?",
                "Use the Contact page with device details and what went wrong.",
            ),
        ],
        "deletion_steps": [
            "Open Android <strong>Settings → Apps → PaperShelf → Storage → Clear data</strong>.",
            "Or uninstall <strong>PaperShelf</strong> to remove local library data.",
            "Delete any copies you exported outside the app separately.",
        ],
    },
    {
        "slug": "universal-kit",
        "name": "UniversalKit",
        "tag": "Everyday tools. One kit.",
        "domain": f"{BASE}/universal-kit",
        "email": "support@universalkit.app",
        "logo": Path(r"D:\Work\Senthil\UniversalKit\assets\brand\logo_b_1024.png"),
        "theme": "#1D4ED8",
        "theme_dark": "#1E3A8A",
        "theme_light": "#2563EB",
        "accent": "#3B82F6",
        "accent_soft": "#EFF6FF",
        "bg": "#F8FAFC",
        "bg_muted": "#F1F5F9",
        "border": "#E2E8F0",
        "shadow_rgb": "29, 78, 216",
        "hero_badge": "Utilities · Offline Friendly",
        "hero_title_html": 'Tools.<br>Ready.<br><span class="accent">Anywhere.</span>',
        "hero_sub": "A practical kit of everyday utilities.",
        "hero_desc": (
            "UniversalKit bundles useful day-to-day tools in one Android app — "
            "open what you need, get it done, and keep preferences on your device."
        ),
        "keywords": "utilities, toolkit, tools app, everyday utilities, UniversalKit",
        "category": "UtilitiesApplication",
        "trust": [
            "Multi Tools",
            "On-device Prefs",
            "Fast Launch",
            "Simple UI",
            "Optional Ads",
            "Play Updates",
        ],
        "features": [
            ("Utility Bundle", "Multiple everyday tools in one install."),
            ("Quick Access", "Jump to the tool you need without hunting."),
            ("Local Preferences", "Your settings stay on the device."),
            ("Offline Friendly", "Many tools work without constant connectivity."),
            ("Permission Light", "Sensitive permissions only when a tool needs them."),
            ("Clean Design", "A consistent UI across the kit."),
            ("Share Outputs", "Export or share results when a tool supports it."),
            ("Regular Updates", "Improvements via Google Play."),
        ],
        "benefits_title": "Built for Daily Tasks. Designed to Stay Light.",
        "benefits_desc": (
            "UniversalKit is for people who want handy tools without installing "
            "ten separate apps."
        ),
        "benefits": [
            ("Privacy Aware", "Data stays local unless a tool explicitly shares."),
            ("Less App Clutter", "One kit instead of many one-purpose installs."),
            ("Clear Permissions", "Camera/files only when you open tools that need them."),
            ("Support Ready", "Contact us if a tool misbehaves."),
        ],
        "data_items": [
            "Tool preferences and settings",
            "Content you create inside tools",
            "Optional imported/exported files",
            "App configuration",
        ],
        "permissions": [
            ("Camera / files", "Only when you open a tool that needs them."),
            ("Internet", "Ads (if enabled), updates, and optional online tools."),
        ],
        "faqs": [
            (
                "Do all tools need internet?",
                "No. Many utilities are offline friendly. Internet is used for ads/updates or online-specific tools.",
            ),
            (
                "How do I delete my data?",
                "Clear app storage or uninstall UniversalKit. See Data Deletion.",
            ),
            (
                "Why does a tool ask for permission?",
                "Only tools that need camera or files will request those permissions when you use them.",
            ),
            (
                "How do I contact support?",
                "Use the Contact page and mention which tool had the issue.",
            ),
        ],
        "deletion_steps": [
            "Open Android <strong>Settings → Apps → UniversalKit → Storage → Clear data</strong>.",
            "Or uninstall <strong>UniversalKit</strong> to remove local preferences and tool data.",
            "Delete any exported files outside the app separately.",
        ],
    },
]


def patch_css(css: str, app: dict) -> str:
    css = css.replace("#0F5D31", app["theme"])
    css = css.replace("#0A3F22", app["theme_dark"])
    css = css.replace("#147A40", app["theme_light"])
    css = css.replace("#24A148", app["accent"])
    css = css.replace("#E8F8EE", app["accent_soft"])
    css = css.replace("#F8FAF9", app["bg"])
    css = css.replace("#F1F5F3", app["bg_muted"])
    css = css.replace("#E2EBE5", app["border"])
    css = re.sub(
        r"rgba\(15, 93, 49, ([0-9.]+)\)",
        rf"rgba({app['shadow_rgb']}, \1)",
        css,
    )
    css = re.sub(
        r"rgba\(36, 161, 72, ([0-9.]+)\)",
        rf"rgba({app['shadow_rgb']}, \1)",
        css,
    )
    return css


def make_logo(dest_assets: Path, app: dict) -> None:
    """Copy each app's real brand logo into the site assets folder."""
    dest_assets.mkdir(parents=True, exist_ok=True)
    src: Path | None = app.get("logo")
    if src is None or not src.exists():
        raise FileNotFoundError(f"Logo missing for {app['name']}: {src}")

    img = Image.open(src).convert("RGBA")
    # Normalize to a square canvas so header/favicon crops stay clean.
    w, h = img.size
    side = max(w, h)
    canvas = Image.new("RGBA", (side, side), (0, 0, 0, 0))
    canvas.paste(img, ((side - w) // 2, (side - h) // 2), img)

    logo = canvas.resize((512, 512), Image.Resampling.LANCZOS)
    favicon = canvas.resize((64, 64), Image.Resampling.LANCZOS)
    logo.save(dest_assets / "logo.png", optimize=True)
    favicon.save(dest_assets / "favicon.png", optimize=True)


def svg_icon(kind: str) -> str:
    icons = {
        "shield": '<path d="M12 3l8 4v5c0 5-3.5 8.5-8 10-4.5-1.5-8-5-8-10V7l8-4z"/><path d="M9 12l2 2 4-4"/>',
        "lock": '<rect x="5" y="11" width="14" height="10" rx="2"/><path d="M8 11V8a4 4 0 018 0v3"/>',
        "bolt": '<path d="M13 2L4 14h7l-1 8 10-14h-7l1-6z"/>',
        "spark": '<path d="M12 3v4M12 17v4M3 12h4M17 12h4M5.5 5.5l2.5 2.5M16 16l2.5 2.5M18.5 5.5L16 8M8 16l-2.5 2.5"/>',
        "grid": '<rect x="4" y="4" width="6" height="6" rx="1"/><rect x="14" y="4" width="6" height="6" rx="1"/><rect x="4" y="14" width="6" height="6" rx="1"/><rect x="14" y="14" width="6" height="6" rx="1"/>',
        "cloud": '<path d="M7 18a4 4 0 01.5-7.9A5 5 0 0117 9a3.5 3.5 0 01.5 7H7z"/>',
        "chart": '<path d="M4 19V9l4 2 4-5 4 4 4-3"/><path d="M4 19h16"/>',
        "pen": '<path d="M4 20l4.5-1L19 8.5 15.5 5 5 15.5 4 20z"/><path d="M13.5 6.5l4 4"/>',
    }
    d = icons.get(kind, icons["grid"])
    return f'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round">{d}</svg>'


def header(app: dict, active: str = "home") -> str:
    def cls(key: str) -> str:
        return ' class="active"' if active == key else ""

    return f"""  <header class="site-header">
    <div class="container nav">
      <a class="brand" href="index.html" aria-label="{app['name']} home">
        <img src="assets/logo.png" alt="" width="44" height="44">
        <span class="brand-text">
          <span class="brand-name">{app['name']}</span>
          <span class="brand-tag">{app['tag']}</span>
        </span>
      </a>
      <nav class="nav-links" aria-label="Primary">
        <a href="index.html"{cls('home')}>Home</a>
        <a href="index.html#features"{cls('features')}>Features</a>
        <a href="index.html#benefits"{cls('benefits')}>Benefits</a>
        <a href="index.html#faq"{cls('faq')}>FAQ</a>
        <a href="support.html"{cls('contact')}>Contact</a>
      </nav>
      <a class="btn btn-primary nav-cta btn-coming" href="index.html#download">Coming Soon</a>
      <button class="nav-toggle" id="nav-toggle" type="button" aria-label="Open menu" aria-expanded="false" aria-controls="mobile-drawer">
        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" aria-hidden="true"><path d="M4 7h16M4 12h16M4 17h16"/></svg>
      </button>
    </div>
  </header>

  <div class="drawer-overlay" id="drawer-overlay" hidden></div>
  <aside class="drawer" id="mobile-drawer" aria-label="Mobile navigation" aria-hidden="true">
    <div class="drawer-header">
      <div class="drawer-brand">
        <img src="assets/logo.png" alt="" width="36" height="36">
        {app['name']}
      </div>
      <button class="drawer-close" id="drawer-close" type="button" aria-label="Close menu">
        <svg viewBox="0 0 24 24" width="20" height="20" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" aria-hidden="true"><path d="M6 6l12 12M18 6L6 18"/></svg>
      </button>
    </div>
    <nav class="drawer-links">
      <a href="index.html">Home</a>
      <a href="index.html#features">Features</a>
      <a href="index.html#benefits">Benefits</a>
      <a href="index.html#faq">FAQ</a>
      <a href="support.html">Contact</a>
      <a href="privacy.html">Privacy Policy</a>
      <a href="terms.html">Terms &amp; Conditions</a>
      <a href="deletion.html">Data Deletion</a>
    </nav>
    <a class="btn btn-primary btn-block btn-coming" href="index.html#download">Coming Soon</a>
  </aside>"""


def footer(app: dict) -> str:
    return f"""  <footer class="site-footer">
    <div class="container footer-grid">
      <div>
        <div class="footer-brand">
          <img src="assets/logo.png" alt="" width="36" height="36">
          <strong>{app['name']}</strong>
        </div>
        <p>{app['hero_sub']}</p>
      </div>
      <div>
        <h4>Product</h4>
        <a href="index.html#features">Features</a>
        <a href="index.html#benefits">Benefits</a>
        <a href="index.html#faq">FAQ</a>
      </div>
      <div>
        <h4>Legal</h4>
        <a href="privacy.html">Privacy Policy</a>
        <a href="terms.html">Terms &amp; Conditions</a>
        <a href="deletion.html">Data Deletion</a>
        <a href="support.html">Contact</a>
      </div>
    </div>
    <div class="container footer-bottom">
      <p>&copy; 2026 {app['name']}. All rights reserved.</p>
      <div class="footer-bottom-links">
        <a href="privacy.html">Privacy</a>
        <a href="terms.html">Terms</a>
        <a href="support.html">Contact</a>
      </div>
    </div>
  </footer>
  <script src="js/main.js" defer></script>"""


def inner_footer(app: dict) -> str:
    return f"""  <footer class="page-inner-footer">
    <div class="container footer-bottom">
      <p>&copy; 2026 {app['name']}. All rights reserved.</p>
      <div class="footer-bottom-links">
        <a href="privacy.html">Privacy Policy</a>
        <a href="terms.html">Terms</a>
        <a href="support.html">Contact</a>
        <a href="deletion.html">Data Deletion</a>
      </div>
    </div>
  </footer>
  <script src="js/main.js" defer></script>"""


def write_index(dest: Path, app: dict) -> None:
    trust_html = []
    icons = ["shield", "lock", "cloud", "spark", "chart", "bolt"]
    for i, label in enumerate(app["trust"]):
        delay = f' reveal-delay-{(i % 3) + 1}' if i else ""
        trust_html.append(
            f"""        <div class="trust-item reveal{delay}">
          <div class="trust-icon">{svg_icon(icons[i % len(icons)])}</div>
          <span>{label}</span>
        </div>"""
        )

    features_html = []
    for i, (title, desc) in enumerate(app["features"]):
        delay = f" reveal-delay-{(i % 3) + 1}" if i % 3 else ""
        features_html.append(
            f"""          <article class="feature-card reveal{delay}">
            <div class="feature-icon">{svg_icon('grid')}</div>
            <h3>{title}</h3>
            <p>{desc}</p>
          </article>"""
        )

    benefits_html = []
    for i, (title, desc) in enumerate(app["benefits"]):
        delay = f" reveal-delay-{i}" if i else ""
        benefits_html.append(
            f"""          <article class="benefit-card reveal{delay}">
            <h3>{title}</h3>
            <p>{desc}</p>
          </article>"""
        )

    faq_html = []
    for q, a in app["faqs"]:
        faq_html.append(
            f"""          <div class="faq-item">
            <button class="faq-question" type="button" aria-expanded="false">{q}</button>
            <div class="faq-answer"><p>{a}</p></div>
          </div>"""
        )

    faq_ld = ",\n".join(
        f"""          {{
            "@type": "Question",
            "name": {q!r},
            "acceptedAnswer": {{ "@type": "Answer", "text": {a!r} }}
          }}"""
        for q, a in app["faqs"]
    )

    html = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{app['name']} — {app['tag']}</title>
  <meta name="description" content="{app['hero_desc']}">
  <meta name="keywords" content="{app['keywords']}">
  <meta name="author" content="{app['name']}">
  <meta name="theme-color" content="{app['theme']}">
  <link rel="canonical" href="{app['domain']}/">
  <link rel="icon" type="image/png" href="assets/favicon.png">
  <link rel="apple-touch-icon" href="assets/logo.png">
  <meta property="og:type" content="website">
  <meta property="og:url" content="{app['domain']}/">
  <meta property="og:title" content="{app['name']} — {app['tag']}">
  <meta property="og:description" content="{app['hero_desc']}">
  <meta property="og:image" content="{app['domain']}/assets/logo.png">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Poppins:wght@400;500;600;700&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="css/main.css">
  <script type="application/ld+json">
  {{
    "@context": "https://schema.org",
    "@graph": [
      {{
        "@type": "Organization",
        "name": "{app['name']}",
        "url": "{app['domain']}/",
        "logo": "{app['domain']}/assets/logo.png",
        "email": "{app['email']}"
      }},
      {{
        "@type": "SoftwareApplication",
        "name": "{app['name']}",
        "applicationCategory": "{app['category']}",
        "operatingSystem": "Android",
        "offers": {{ "@type": "Offer", "price": "0", "priceCurrency": "INR" }},
        "description": {app['hero_desc']!r}
      }},
      {{
        "@type": "FAQPage",
        "mainEntity": [
{faq_ld}
        ]
      }}
    ]
  }}
  </script>
</head>
<body>
{header(app, 'home')}

  <main>
    <section class="hero" id="home">
      <div class="hero-bg" aria-hidden="true">
        <div class="hero-glow"></div>
        <div class="hero-glow-2"></div>
      </div>
      <div class="container hero-grid">
        <div class="hero-content reveal">
          <div class="hero-badge">{app['hero_badge']}</div>
          <h1 class="hero-title">{app['hero_title_html']}</h1>
          <p class="hero-sub">{app['hero_sub']}</p>
          <p class="hero-desc">{app['hero_desc']}</p>
          <div class="hero-actions">
            <a class="btn btn-primary btn-coming" href="#download" id="download">Coming Soon</a>
            <a class="btn btn-secondary" href="#features">Explore Features</a>
          </div>
        </div>
        <div class="hero-visual reveal reveal-delay-2">
          <div class="phone">
            <div class="phone-screen" style="display:flex;align-items:center;justify-content:center;background:linear-gradient(160deg,{app['theme']},{app['theme_dark']});color:#fff;min-height:420px;padding:2rem;text-align:center;">
              <div>
                <img src="assets/logo.png" alt="" width="72" height="72" style="margin:0 auto 1rem;border-radius:16px;">
                <h2 style="font-size:1.4rem;margin-bottom:.5rem;">{app['name']}</h2>
                <p style="opacity:.9;">{app['tag']}</p>
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>

    <section class="trust" aria-label="Trust indicators">
      <div class="container trust-grid">
{chr(10).join(trust_html)}
      </div>
    </section>

    <section class="section" id="features">
      <div class="container">
        <div class="section-header reveal">
          <span class="eyebrow">Features</span>
          <h2 class="section-title">Everything You Need</h2>
          <p class="section-desc">{app['hero_desc']}</p>
        </div>
        <div class="features-grid">
{chr(10).join(features_html)}
        </div>
      </div>
    </section>

    <section class="section section-muted" id="benefits">
      <div class="container">
        <div class="section-header reveal">
          <span class="eyebrow">Why {app['name']}</span>
          <h2 class="section-title">{app['benefits_title']}</h2>
          <p class="section-desc">{app['benefits_desc']}</p>
        </div>
        <div class="benefit-cards">
{chr(10).join(benefits_html)}
        </div>
      </div>
    </section>

    <section class="section" id="faq">
      <div class="container">
        <div class="section-header reveal">
          <span class="eyebrow">FAQ</span>
          <h2 class="section-title">Frequently Asked Questions</h2>
          <p class="section-desc">Answers based on our Privacy Policy, Terms, Support and Data Deletion guidance.</p>
        </div>
        <div class="faq-list reveal">
{chr(10).join(faq_html)}
        </div>
      </div>
    </section>

    <section class="cta-banner" id="download">
      <div class="container">
        <div class="cta-inner reveal">
          <div class="cta-copy">
            <div class="cta-icon" aria-hidden="true">
              <svg viewBox="0 0 24 24" fill="currentColor"><path d="M12 2l2.4 4.9 5.4.8-3.9 3.8.9 5.4L12 14.9 7.2 17l.9-5.4L4.2 7.7l5.4-.8L12 2z"/></svg>
            </div>
            <div>
              <h3>Get {app['name']}</h3>
              <p>Coming soon on Google Play. Privacy Policy and Terms are already available for store listing.</p>
            </div>
          </div>
          <div class="cta-action">
            <a class="btn btn-primary btn-coming" href="support.html">Contact Support</a>
            <small>Coming soon on Google Play</small>
          </div>
        </div>
      </div>
    </section>
  </main>

{footer(app)}
</body>
</html>
"""
    (dest / "index.html").write_text(html, encoding="utf-8")


def write_legal_page(dest: Path, app: dict, kind: str) -> None:
    if kind == "privacy":
        title = "Privacy Policy"
        active = "home"
        items = "\n".join(f"          <li>{x}</li>" for x in app["data_items"])
        perms = "\n".join(
            f"          <li><strong>{k}:</strong> {v}</li>" for k, v in app["permissions"]
        )
        body = f"""        <h1>Privacy Policy</h1>
        <p class="page-meta"><strong>Effective Date:</strong> October 2026</p>
        <p>{app['name']} ("we", "our", or "us") respects your privacy. {app['name']} is designed with a Privacy First approach. Your information stays under your control on your device whenever possible.</p>
        <h2>Information We Collect</h2>
        <h3>Information You Enter</h3>
        <p>This information is stored on your device:</p>
        <ul>
{items}
        </ul>
        <h2>Permissions</h2>
        <ul>
{perms}
        </ul>
        <h2>Advertising</h2>
        <p>Store / free builds may display Google AdMob advertisements. Google may collect advertising ID, device information, and ad performance metrics. See Google's Privacy Policy for details.</p>
        <h2>Purchases</h2>
        <p>If paid upgrades are offered, payments are processed by Google Play Billing. We do not store raw payment card details.</p>
        <h2>Data Storage</h2>
        <p>Core app data is stored locally on your device. We do not operate a required cloud account for basic use described here.</p>
        <h2>Data Sharing</h2>
        <p>We do not sell your personal information. Content leaves your device only when you export/share it or use a feature that clearly needs internet.</p>
        <h2>Children's Privacy</h2>
        <p>{app['name']} is intended for general users as described on the store listing. Do not enter sensitive children's data beyond what a feature needs.</p>
        <h2>Changes</h2>
        <p>This Privacy Policy may be updated over time. Continued use after updates means you accept the revised policy.</p>
        <h2>Contact</h2>
        <p>Email <strong>{app['email']}</strong> or visit our <a href="support.html">Contact</a> page.</p>"""
    elif kind == "terms":
        title = "Terms & Conditions"
        active = "home"
        body = f"""        <h1>Terms &amp; Conditions</h1>
        <p class="page-meta"><strong>Effective Date:</strong> October 2026</p>
        <p>By using {app['name']} ("the App"), you agree to these Terms.</p>
        <h2>1. The App</h2>
        <p>{app['hero_desc']}</p>
        <h2>2. Your Content</h2>
        <p>You own content you create. You are responsible for what you enter, import, export, or share. Do not use the App for unlawful or infringing material.</p>
        <h2>3. Acceptable Use</h2>
        <p>Use the App for its intended personal / educational / productivity purpose. Do not reverse engineer, abuse ads, or disrupt the service.</p>
        <h2>4. Ads &amp; Updates</h2>
        <p>Store builds may show advertisements. Updates may be delivered through Google Play.</p>
        <h2>5. Disclaimer</h2>
        <p>The App is provided "as is" without warranties. We are not liable for lost data, device issues, or third-party services including ad networks and Play Store.</p>
        <h2>6. Changes</h2>
        <p>We may update these Terms. Continued use after an update means you accept the new Terms.</p>
        <h2>7. Contact</h2>
        <p>Email <strong>{app['email']}</strong> or use the <a href="support.html">Contact</a> page.</p>"""
    elif kind == "support":
        title = "Contact"
        active = "contact"
        body = f"""        <h1>Contact</h1>
        <p class="page-meta">Support for {app['name']}</p>
        <p>{app['hero_desc']}</p>
        <h2>Email</h2>
        <p><strong>{app['email']}</strong></p>
        <p>Include your device model, Android version, and a short description of the issue. Typical response time is 24–48 hours.</p>
        <h2>Common Topics</h2>
        <ul>
          <li>App crash / not opening — update from Play Store, then reinstall if needed.</li>
          <li>Permissions — grant Camera/Files only if you use those features.</li>
          <li>Ads — store builds may show AdMob ads.</li>
        </ul>
        <h2>Legal</h2>
        <ul>
          <li><a href="privacy.html">Privacy Policy</a></li>
          <li><a href="terms.html">Terms &amp; Conditions</a></li>
          <li><a href="deletion.html">Data Deletion</a></li>
        </ul>"""
    else:
        title = "Data Deletion"
        active = "home"
        steps = "\n".join(f"            <li>{s}</li>" for s in app["deletion_steps"])
        body = f"""        <h1>Delete Your Data</h1>
        <p>{app['name']} primarily stores information on your device. Use the steps below to permanently remove local app data.</p>
        <div class="page-steps">
          <h2>To permanently remove application data:</h2>
          <ol>
{steps}
          </ol>
        </div>
        <p>If you contacted support by email and want that correspondence deleted, email <strong>{app['email']}</strong> with the app name and your request.</p>
        <p><em>If cloud sync is added in a future release, this page will be updated with remote deletion instructions.</em></p>"""

    html = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{title} — {app['name']}</title>
  <meta name="description" content="{title} for {app['name']}.">
  <meta name="theme-color" content="{app['theme']}">
  <link rel="canonical" href="{app['domain']}/{kind if kind != 'support' else 'support'}.html">
  <link rel="icon" type="image/png" href="assets/favicon.png">
  <link rel="apple-touch-icon" href="assets/logo.png">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Poppins:wght@400;500;600;700&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="css/main.css">
</head>
<body class="page-inner">
{header(app, active)}
  <main class="page-inner-main">
    <div class="container">
      <article class="page-panel">
{body}
      </article>
    </div>
  </main>
{inner_footer(app)}
</body>
</html>
"""
    fname = "support.html" if kind == "support" else f"{kind}.html"
    if kind == "terms":
        fname = "terms.html"
    (dest / fname).write_text(html, encoding="utf-8")


def write_robots_sitemap(dest: Path, app: dict) -> None:
    (dest / "robots.txt").write_text(
        f"User-agent: *\nAllow: /\n\nSitemap: {app['domain']}/sitemap.xml\n",
        encoding="utf-8",
    )
    urls = ["", "privacy.html", "terms.html", "support.html", "deletion.html"]
    parts = [
        '<?xml version="1.0" encoding="UTF-8"?>',
        '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">',
    ]
    for u in urls:
        loc = f"{app['domain']}/" if u == "" else f"{app['domain']}/{u}"
        pri = "1.0" if u == "" else "0.6"
        parts.append(
            f"  <url><loc>{loc}</loc><changefreq>monthly</changefreq><priority>{pri}</priority></url>"
        )
    parts.append("</urlset>\n")
    (dest / "sitemap.xml").write_text("\n".join(parts), encoding="utf-8")


def build_app(app: dict) -> Path:
    dest = DOCS / app["slug"]
    if dest.exists():
        shutil.rmtree(dest)
    dest.mkdir(parents=True)
    (dest / "css").mkdir()
    (dest / "js").mkdir()
    (dest / "assets").mkdir()

    css = (SRC / "css" / "main.css").read_text(encoding="utf-8")
    (dest / "css" / "main.css").write_text(patch_css(css, app), encoding="utf-8")
    shutil.copy2(SRC / "js" / "main.js", dest / "js" / "main.js")
    make_logo(dest / "assets", app)
    write_index(dest, app)
    for kind in ("privacy", "terms", "support", "deletion"):
        write_legal_page(dest, app, kind)
    write_robots_sitemap(dest, app)
    return dest


def write_hub() -> None:
    cards = []
    for app in APPS:
        cards.append(
            f"""      <a class="hub-card" href="{app['slug']}/">
        <img src="{app['slug']}/assets/logo.png" alt="" width="56" height="56">
        <div>
          <strong>{app['name']}</strong>
          <span>{app['tag']}</span>
        </div>
      </a>"""
        )
    html = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>App Legal — Seng2HS</title>
  <meta name="description" content="Privacy, Terms, Support and product pages for Seng2HS Android apps.">
  <meta name="theme-color" content="#0F5D31">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Poppins:wght@400;500;600;700&display=swap" rel="stylesheet">
  <style>
    :root {{
      --ink: #14201a;
      --muted: #5b6b62;
      --line: #e2ebe5;
      --bg: #f8faf9;
      --card: #ffffff;
      --brand: #0f5d31;
    }}
    * {{ box-sizing: border-box; }}
    body {{
      margin: 0;
      font-family: Poppins, system-ui, sans-serif;
      color: var(--ink);
      background:
        radial-gradient(900px 420px at 10% -10%, rgba(15,93,49,.12), transparent 60%),
        radial-gradient(700px 360px at 100% 0%, rgba(36,161,72,.10), transparent 55%),
        var(--bg);
      min-height: 100vh;
    }}
    .wrap {{ max-width: 960px; margin: 0 auto; padding: 48px 20px 72px; }}
    h1 {{ font-size: clamp(1.8rem, 4vw, 2.6rem); margin: 0 0 8px; letter-spacing: -0.03em; }}
    .lead {{ color: var(--muted); margin: 0 0 36px; max-width: 42rem; line-height: 1.6; }}
    .grid {{
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(240px, 1fr));
      gap: 16px;
    }}
    .hub-card {{
      display: flex;
      gap: 14px;
      align-items: center;
      padding: 18px;
      background: var(--card);
      border: 1px solid var(--line);
      border-radius: 18px;
      text-decoration: none;
      color: inherit;
      transition: transform .18s ease, box-shadow .18s ease;
    }}
    .hub-card:hover {{
      transform: translateY(-2px);
      box-shadow: 0 14px 30px rgba(15, 93, 49, .10);
    }}
    .hub-card img {{ border-radius: 12px; }}
    .hub-card strong {{ display: block; font-size: 1.05rem; }}
    .hub-card span {{ color: var(--muted); font-size: .88rem; }}
    footer {{ margin-top: 40px; color: var(--muted); font-size: .85rem; }}
    footer a {{ color: var(--brand); }}
  </style>
</head>
<body>
  <main class="wrap">
    <h1>App Legal</h1>
    <p class="lead">CapitalNest-style product and legal pages for every Seng2HS Android app — Privacy, Terms, Support and Data Deletion.</p>
    <div class="grid">
{chr(10).join(cards)}
    </div>
    <footer>
      <p>Base URL: <a href="{BASE}/">{BASE}/</a></p>
    </footer>
  </main>
</body>
</html>
"""
    (DOCS / "index.html").write_text(html, encoding="utf-8")
    # drop old shared styles if present
    old = DOCS / "styles.css"
    if old.exists():
        old.unlink()


def main() -> None:
    if not (SRC / "css" / "main.css").exists():
        raise SystemExit(f"Template missing: {SRC}")
    DOCS.mkdir(parents=True, exist_ok=True)
    for app in APPS:
        path = build_app(app)
        print("built", path)
    write_hub()
    print("hub", DOCS / "index.html")


if __name__ == "__main__":
    main()

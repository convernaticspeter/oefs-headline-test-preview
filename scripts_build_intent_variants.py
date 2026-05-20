from pathlib import Path
from html import escape

root = Path(__file__).parent

# ── Service-area SVG maps ──────────────────────────────────────────
# Simplified topographic district maps for each city variant

LINZ_MAP_SVG = '''<svg viewBox="0 0 600 520" xmlns="http://www.w3.org/2000/svg" aria-label="Einzugsgebiet Linz und Umgebung">
  <defs>
    <linearGradient id="d" x1="0" y1="0" x2="0" y2="1"><stop offset="0%" stop-color="#e8f0f8"/><stop offset="100%" stop-color="#d4e2f0"/></linearGradient>
  </defs>
  <rect width="600" height="520" fill="#f4f7fa" rx="20"/>
  <!-- Donau -->
  <path d="M0,228 Q150,218 300,232 Q450,246 600,228" fill="none" stroke="#b0cfe0" stroke-width="28" stroke-linecap="round" opacity="0.7"/>
  <path d="M0,228 Q150,218 300,232 Q450,246 600,228" fill="none" stroke="#c8dff0" stroke-width="14" stroke-linecap="round" opacity="0.5"/>
  <!-- Stadt Linz Kern -->
  <ellipse cx="300" cy="210" rx="90" ry="55" fill="#0056a7" opacity="0.18" stroke="#0056a7" stroke-width="2.5"/>
  <text x="300" y="213" text-anchor="middle" font-size="14" font-weight="700" fill="#003d7a" font-family="system-ui,sans-serif">Linz Stadt</text>
  <!-- Nördliche Stadtteile -->
  <rect x="230" y="100" width="140" height="50" rx="12" fill="url(#d)" stroke="#b8cfe0" stroke-width="2"/>
  <text x="300" y="120" text-anchor="middle" font-size="11" font-weight="600" fill="#33495d" font-family="system-ui,sans-serif">Urfahr · Pöstlingberg</text>
  <text x="300" y="137" text-anchor="middle" font-size="10" fill="#5d7182" font-family="system-ui,sans-serif">St. Magdalena · Dornach-Auhof</text>
  <!-- Südliche Stadtteile -->
  <rect x="220" y="305" width="160" height="50" rx="12" fill="url(#d)" stroke="#b8cfe0" stroke-width="2"/>
  <text x="300" y="325" text-anchor="middle" font-size="11" font-weight="600" fill="#33495d" font-family="system-ui,sans-serif">Ebelsberg · Pichling</text>
  <text x="300" y="342" text-anchor="middle" font-size="10" fill="#5d7182" font-family="system-ui,sans-serif">Kleinmünchen · Neue Heimat</text>
  <!-- West -->
  <rect x="40" y="260" width="120" height="42" rx="12" fill="url(#d)" stroke="#b8cfe0" stroke-width="2"/>
  <text x="100" y="278" text-anchor="middle" font-size="11" font-weight="600" fill="#33495d" font-family="system-ui,sans-serif">Leonding</text>
  <text x="100" y="293" text-anchor="middle" font-size="10" fill="#5d7182" font-family="system-ui,sans-serif">Pasching · Wilhering</text>
  <!-- Ost -->
  <rect x="425" y="190" width="140" height="55" rx="12" fill="url(#d)" stroke="#b8cfe0" stroke-width="2"/>
  <text x="495" y="210" text-anchor="middle" font-size="11" font-weight="600" fill="#33495d" font-family="system-ui,sans-serif">Industriegebiet-Hafen</text>
  <text x="495" y="227" text-anchor="middle" font-size="10" fill="#5d7182" font-family="system-ui,sans-serif">Kaplanhof · Franckviertel</text>
  <!-- Süd -->
  <rect x="370" y="370" width="170" height="55" rx="12" fill="url(#d)" stroke="#b8cfe0" stroke-width="2"/>
  <text x="455" y="392" text-anchor="middle" font-size="11" font-weight="600" fill="#33495d" font-family="system-ui,sans-serif">Traun · Ansfelden</text>
  <text x="455" y="409" text-anchor="middle" font-size="10" fill="#5d7182" font-family="system-ui,sans-serif">Hörsching · St. Florian</text>
  <!-- Nordwest -->
  <rect x="30" y="130" width="130" height="42" rx="12" fill="url(#d)" stroke="#b8cfe0" stroke-width="2"/>
  <text x="95" y="148" text-anchor="middle" font-size="11" font-weight="600" fill="#33495d" font-family="system-ui,sans-serif">Ottensheim</text>
  <text x="95" y="163" text-anchor="middle" font-size="10" fill="#5d7182" font-family="system-ui,sans-serif">Walding · Gramastetten</text>
  <!-- Legende -->
  <rect x="440" y="440" width="130" height="50" rx="8" fill="#fff" stroke="#d0dce6" stroke-width="1.5"/>
  <rect x="450" y="450" width="12" height="12" rx="3" fill="#0056a7" opacity="0.2" stroke="#0056a7" stroke-width="2"/>
  <text x="468" y="461" font-size="10" fill="#3d4f5f" font-family="system-ui,sans-serif">ÖFS betreut</text>
  <text x="450" y="480" font-size="9" fill="#6a7d8c" font-family="system-ui,sans-serif">Linz Stadt + Umland</text>
</svg>'''

WIEN_MAP_SVG = '''<svg viewBox="0 0 600 520" xmlns="http://www.w3.org/2000/svg" aria-label="Einzugsgebiet Wien alle Bezirke">
  <defs>
    <linearGradient id="wd" x1="0" y1="0" x2="0" y2="1"><stop offset="0%" stop-color="#e8f0f8"/><stop offset="100%" stop-color="#d4e2f0"/></linearGradient>
  </defs>
  <rect width="600" height="520" fill="#f4f7fa" rx="20"/>
  <!-- Donau -->
  <path d="M0,200 Q300,190 600,210" fill="none" stroke="#b0cfe0" stroke-width="24" stroke-linecap="round" opacity="0.6"/>
  <path d="M0,310 Q300,300 600,315" fill="none" stroke="#b0cfe0" stroke-width="20" stroke-linecap="round" opacity="0.5"/>
  <!-- Zentrum -->
  <ellipse cx="300" cy="250" rx="55" ry="48" fill="#0056a7" opacity="0.2" stroke="#0056a7" stroke-width="2.5"/>
  <text x="300" y="254" text-anchor="middle" font-size="12" font-weight="700" fill="#003d7a" font-family="system-ui,sans-serif">1.–9. Bezirk</text>
  <!-- Innere Bezirke Ring -->
  <ellipse cx="300" cy="255" rx="120" ry="100" fill="none" stroke="#b8cfe0" stroke-width="1.5" stroke-dasharray="8,4"/>
  <text x="300" y="145" text-anchor="middle" font-size="10" fill="#5d7182" font-family="system-ui,sans-serif">10.–19. Bezirk</text>
  <!-- Äußere Bezirke Ring -->
  <ellipse cx="300" cy="260" rx="230" ry="150" fill="none" stroke="#b8cfe0" stroke-width="1.5" stroke-dasharray="8,4"/>
  <text x="300" y="95" text-anchor="middle" font-size="10" fill="#5d7182" font-family="system-ui,sans-serif">20.–23. Bezirk</text>
  <!-- Bezirkslabels außen -->
  <g font-size="9" fill="#4d616f" font-family="system-ui,sans-serif">
    <text x="300" y="75">Floridsdorf · Donaustadt</text>
    <text x="520" y="210">Simmering</text>
    <text x="520" y="320">Favoriten · Liesing</text>
    <text x="80" y="310">Hietzing · Penzing</text>
    <text x="80" y="160">Hernals · Währing · Döbling</text>
  </g>
  <!-- Legende -->
  <rect x="440" y="440" width="130" height="50" rx="8" fill="#fff" stroke="#d0dce6" stroke-width="1.5"/>
  <rect x="450" y="450" width="12" height="12" rx="3" fill="#0056a7" opacity="0.2" stroke="#0056a7" stroke-width="2"/>
  <text x="468" y="461" font-size="10" fill="#3d4f5f" font-family="system-ui,sans-serif">ÖFS betreut</text>
  <text x="450" y="480" font-size="9" fill="#6a7d8c" font-family="system-ui,sans-serif">Alle 23 Bezirke</text>
</svg>'''

GRAZ_MAP_SVG = '''<svg viewBox="0 0 600 520" xmlns="http://www.w3.org/2000/svg" aria-label="Einzugsgebiet Graz und Umgebung">
  <defs>
    <linearGradient id="gd" x1="0" y1="0" x2="0" y2="1"><stop offset="0%" stop-color="#e8f0f8"/><stop offset="100%" stop-color="#d4e2f0"/></linearGradient>
  </defs>
  <rect width="600" height="520" fill="#f4f7fa" rx="20"/>
  <!-- Mur -->
  <path d="M300,0 Q290,130 310,260 Q295,390 300,520" fill="none" stroke="#b0cfe0" stroke-width="20" stroke-linecap="round" opacity="0.6"/>
  <path d="M300,0 Q290,130 310,260 Q295,390 300,520" fill="none" stroke="#c8dff0" stroke-width="8" stroke-linecap="round" opacity="0.5"/>
  <!-- Zentrum -->
  <ellipse cx="300" cy="200" rx="70" ry="50" fill="#0056a7" opacity="0.2" stroke="#0056a7" stroke-width="2.5"/>
  <text x="300" y="204" text-anchor="middle" font-size="13" font-weight="700" fill="#003d7a" font-family="system-ui,sans-serif">Graz Stadt</text>
  <!-- Stadtteile -->
  <rect x="210" y="270" width="180" height="42" rx="12" fill="url(#gd)" stroke="#b8cfe0" stroke-width="2"/>
  <text x="300" y="288" text-anchor="middle" font-size="10" fill="#33495d" font-family="system-ui,sans-serif">Liebenau · St. Peter · Waltendorf · Ries</text>
  <text x="300" y="303" text-anchor="middle" font-size="9" fill="#5d7182" font-family="system-ui,sans-serif">Jakomini · Gries · Lend · Geidorf</text>
  <!-- Nord -->
  <rect x="210" y="80" width="180" height="42" rx="12" fill="url(#gd)" stroke="#b8cfe0" stroke-width="2"/>
  <text x="300" y="97" text-anchor="middle" font-size="10" fill="#33495d" font-family="system-ui,sans-serif">Andritz · Gösting · Eggenberg</text>
  <text x="300" y="113" text-anchor="middle" font-size="9" fill="#5d7182" font-family="system-ui,sans-serif">Wetzelsdorf · Straßgang · Puntigam</text>
  <!-- Umland -->
  <rect x="50" y="160" width="130" height="55" rx="12" fill="url(#gd)" stroke="#b8cfe0" stroke-width="2"/>
  <text x="115" y="178" text-anchor="middle" font-size="10" fill="#33495d" font-family="system-ui,sans-serif">Gratkorn · Gratwein</text>
  <text x="115" y="194" text-anchor="middle" font-size="9" fill="#5d7182" font-family="system-ui,sans-serif">Thal · Judendorf</text>
  <text x="115" y="209" text-anchor="middle" font-size="9" fill="#5d7182" font-family="system-ui,sans-serif">Sankt Radegund</text>
  <rect x="420" y="160" width="140" height="55" rx="12" fill="url(#gd)" stroke="#b8cfe0" stroke-width="2"/>
  <text x="490" y="178" text-anchor="middle" font-size="10" fill="#33495d" font-family="system-ui,sans-serif">Hart bei Graz · Raaba</text>
  <text x="490" y="194" text-anchor="middle" font-size="9" fill="#5d7182" font-family="system-ui,sans-serif">Gössendorf · Hausmannstätten</text>
  <text x="490" y="209" text-anchor="middle" font-size="9" fill="#5d7182" font-family="system-ui,sans-serif">Laßnitzhöhe · Nestelbach</text>
  <rect x="420" y="370" width="150" height="55" rx="12" fill="url(#gd)" stroke="#b8cfe0" stroke-width="2"/>
  <text x="495" y="388" text-anchor="middle" font-size="10" fill="#33495d" font-family="system-ui,sans-serif">Feldkirchen · Seiersberg</text>
  <text x="495" y="404" text-anchor="middle" font-size="9" fill="#5d7182" font-family="system-ui,sans-serif">Pirka · Premstätten</text>
  <text x="495" y="419" text-anchor="middle" font-size="9" fill="#5d7182" font-family="system-ui,sans-serif">Unterpremstätten · Wundschuh</text>
  <!-- Legende -->
  <rect x="440" y="440" width="130" height="50" rx="8" fill="#fff" stroke="#d0dce6" stroke-width="1.5"/>
  <rect x="450" y="450" width="12" height="12" rx="3" fill="#0056a7" opacity="0.2" stroke="#0056a7" stroke-width="2"/>
  <text x="468" y="461" font-size="10" fill="#3d4f5f" font-family="system-ui,sans-serif">ÖFS betreut</text>
  <text x="450" y="480" font-size="9" fill="#6a7d8c" font-family="system-ui,sans-serif">Graz Stadt + GU</text>
</svg>'''

MAPS = {
    'unterhaltsreinigung-linz': LINZ_MAP_SVG,
    'bueroreinigung-linz': LINZ_MAP_SVG,
    'reinigungsfirma-linz': LINZ_MAP_SVG,
}

# ── CSS ───────────────────────────────────────────────────────────
css = r'''
:root{--blue:#0056a7;--blue2:#003d7a;--line:rgba(16,24,32,.09);--muted:#5d6f7f;--shadow:0 8px 30px rgba(16,24,32,.07);--pad:clamp(16px,5vw,38px)}
*,*:before,*:after{box-sizing:border-box;margin:0}
html{scroll-behavior:smooth;-webkit-text-size-adjust:100%}
body{font-family:-apple-system,BlinkMacSystemFont,'Segoe UI',system-ui,sans-serif;color:#1a2330;background:#fff;line-height:1.52;font-size:17px;-webkit-font-smoothing:antialiased}
img{display:block;max-width:100%}
a{color:var(--blue);text-decoration:underline;text-underline-offset:4px;text-decoration-thickness:1px}
a.btn{text-decoration:none}
.shell{width:min(1280px,calc(100% - var(--pad)*2));margin:0 auto}

/* nav */
.nav{position:sticky;top:0;z-index:100;background:rgba(255,255,255,.96);border-bottom:1px solid var(--line);backdrop-filter:blur(12px);-webkit-backdrop-filter:blur(12px)}
.nav .shell{display:flex;align-items:center;justify-content:space-between;height:68px}
.logo{height:38px;width:auto;flex-shrink:0}
.navlinks{display:flex;gap:28px;align-items:center;list-style:none;padding:0}
.navlinks a{text-decoration:none;color:#1a2330;font-weight:650;font-size:15px;letter-spacing:-.01em;transition:color .15s;white-space:nowrap}
.navlinks a:hover{color:var(--blue)}
.nav-cta{background:var(--blue);color:#fff!important;border-radius:999px;padding:8px 20px;font-weight:700!important;font-size:14px!important;transition:background .2s}
.nav-cta:hover{background:var(--blue2)!important}
.navlinks .sep{display:none}

/* hero */
.hero{background:#f6f9fc;overflow:hidden}
.hero-grid{display:grid;grid-template-columns:minmax(0,1.05fr) minmax(440px,.95fr);align-items:center;gap:clamp(32px,7vw,80px);padding:clamp(40px,8vw,90px) 0}
.hero-copy{display:flex;flex-direction:column;gap:22px}
.hero-label{display:inline-flex;align-items:center;gap:9px;border:1px solid rgba(0,86,167,.18);background:#fff;border-radius:999px;padding:7px 14px;font-size:12px;font-weight:700;color:var(--blue2);letter-spacing:.04em;text-transform:uppercase;width:fit-content}
.hero-label img{width:18px;height:12px;object-fit:cover;border-radius:2px}
.hero h1{font-size:clamp(42px,6.2vw,82px);line-height:.96;letter-spacing:-.06em;color:#0d1b2a;font-weight:800}
.hero .sub{font-size:clamp(17px,2vw,21px);line-height:1.5;color:#3d4f5f;max-width:580px}
.hero .actions{display:flex;gap:14px;flex-wrap:wrap;align-items:center}
.btn{display:inline-flex;align-items:center;justify-content:center;min-height:54px;border-radius:999px;padding:0 24px;font-weight:700;font-size:16px;cursor:pointer;border:1px solid transparent;letter-spacing:-.01em;white-space:nowrap}
.btn.primary{background:var(--blue);color:#fff;box-shadow:0 8px 24px rgba(0,86,167,.22)}
.btn.primary:hover{background:var(--blue2)}
.btn.secondary{background:#fff;color:var(--blue);border-color:rgba(0,86,167,.22)}
.btn.secondary:hover{background:#f4f8fc}
.hero .micro{font-size:13px;color:#6a7d8c;line-height:1.4}
.hero-media img{width:100%;height:520px;object-fit:cover;border-radius:20px;box-shadow:0 14px 44px rgba(16,24,32,.1)}

/* proof bar */
.proof{background:#fff;border-bottom:1px solid var(--line)}
.proof .shell{padding:24px 0;display:flex;align-items:center;justify-content:space-between;gap:20px;flex-wrap:wrap}
.proof-label{font-weight:650;color:#3d4f5f;font-size:14px;white-space:nowrap}
.proof-logos{display:flex;gap:clamp(12px,4vw,30px);align-items:center;flex-wrap:wrap}
.proof-logos img{height:clamp(26px,3.5vw,38px);width:auto;object-fit:contain;filter:grayscale(1);opacity:.64}

/* section */
.sec{padding:clamp(60px,10vw,110px) 0}
.sec.alt{background:#f6f9fc}
.sec-header{margin-bottom:48px;max-width:860px}
.sec-kicker{text-transform:uppercase;letter-spacing:.14em;color:var(--blue);font-size:12px;font-weight:700;margin-bottom:10px}
.sec h2{font-size:clamp(32px,4.6vw,60px);line-height:1.02;letter-spacing:-.05em;color:#0d1b2a;font-weight:800;margin-bottom:18px}
.sec-header p{font-size:18px;line-height:1.55;color:#4d5f6f}

/* service grid */
.svc-grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(300px,1fr));gap:22px}
.svc-card{background:#fff;border:1px solid var(--line);border-radius:20px;padding:28px;box-shadow:var(--shadow)}
.svc-card h3{font-size:22px;font-weight:700;color:#0d1b2a;margin-bottom:8px}
.svc-card p{color:#4d5f6f;line-height:1.5;font-size:16px}
.svc-icon{width:46px;height:46px;border-radius:14px;background:rgba(0,86,167,.08);display:grid;place-items:center;margin-bottom:16px;color:var(--blue);font-size:20px}

/* map section */
.map-layout{display:grid;grid-template-columns:minmax(0,1fr) minmax(400px,1.2fr);gap:clamp(28px,6vw,60px);align-items:center}
.map-layout svg{width:100%;height:auto;border-radius:18px;box-shadow:var(--shadow)}
.map-copy h2{font-size:clamp(28px,4vw,52px);line-height:1.04;letter-spacing:-.04em;font-weight:800;color:#0d1b2a;margin-bottom:16px}
.map-copy p{font-size:17px;line-height:1.55;color:#4d5f6f;margin-bottom:20px}
.map-badges{display:flex;flex-wrap:wrap;gap:8px}
.map-badge{background:rgba(0,86,167,.07);color:var(--blue2);border-radius:999px;padding:6px 14px;font-size:13px;font-weight:650}

/* about */
.about-grid{display:grid;grid-template-columns:1fr 1fr;gap:36px}
.about-card{border-radius:20px;padding:30px;border:1px solid var(--line)}
.about-card.good{background:rgba(34,197,94,.04);border-color:rgba(34,197,94,.16)}
.about-card.bad{background:rgba(239,68,68,.03)}
.about-card h3{font-size:22px;font-weight:700;margin-bottom:14px;color:#0d1b2a}
.about-card ul{list-style:none;padding:0;display:grid;gap:10px}
.about-card li{position:relative;padding-left:32px;line-height:1.42;color:#3d4f5f;font-size:16px}
.about-card li:before{position:absolute;left:0;top:0;width:22px;height:22px;border-radius:50%;display:grid;place-items:center;color:#fff;font-weight:700;font-size:12px}
.about-card.good li:before{content:'✓';background:#22c55e}
.about-card.bad li:before{content:'×';background:#ef4444}

/* process */
.steps-grid{display:grid;grid-template-columns:repeat(4,minmax(0,1fr));gap:16px}
.step-card{background:#fff;border:1px solid var(--line);border-radius:20px;padding:24px}
.step-card .num{display:inline-grid;place-items:center;width:38px;height:38px;border-radius:50%;background:var(--blue);color:#fff;font-weight:800;font-size:16px;margin-bottom:16px}
.step-card h3{font-size:19px;font-weight:700;color:#0d1b2a;margin-bottom:6px}
.step-card p{font-size:15px;color:#4d5f6f;line-height:1.45}

/* references */
.ref-grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(280px,1fr));gap:16px}
.ref-card{background:#fff;border:1px solid var(--line);border-radius:16px;padding:22px}
.ref-card blockquote{font-size:16px;line-height:1.52;color:#1a2330;margin:0 0 12px;font-style:italic}
.ref-card footer{font-size:13px;color:#6a7d8c;font-weight:650}

/* contact */
.contact-box{display:grid;grid-template-columns:1fr 1fr;gap:32px;background:#0d1b2a;color:#fff;border-radius:24px;padding:clamp(28px,5vw,44px);box-shadow:0 16px 50px rgba(16,24,32,.14)}
.contact-box h2{color:#fff;font-size:clamp(26px,4vw,44px)}
.contact-box p{color:rgba(255,255,255,.74);line-height:1.55}
.form{display:grid;gap:12px}
.form input,.form select,.form textarea{width:100%;border:1px solid rgba(255,255,255,.16);background:rgba(255,255,255,.07);color:#fff;border-radius:14px;min-height:50px;padding:12px 15px;font:inherit;font-size:16px}
.form textarea{min-height:100px}
.form ::placeholder{color:rgba(255,255,255,.46)}
.form button{min-height:54px;border:0;border-radius:999px;background:#fff;color:var(--blue2);font-weight:700;font-size:16px;cursor:pointer}
.form .privacy{font-size:12px!important;color:rgba(255,255,255,.5)!important;margin:0;line-height:1.4}

/* footer */
.footer{padding:36px 0;border-top:1px solid var(--line);color:#6a7d8c;font-size:14px}
.footer .shell{display:flex;justify-content:space-between;align-items:center;gap:20px;flex-wrap:wrap}
.footer a{color:#6a7d8c}

/* mobile */
@media(max-width:920px){
  .nav .shell{height:60px}
  .navlinks{gap:14px}
  .navlinks a:not(.nav-cta){display:none}
  .nav-cta{font-size:12px!important;padding:7px 14px}
  .logo{height:30px}
  .hero-grid{grid-template-columns:1fr;gap:26px;padding:28px 0 46px}
  .hero-copy{order:2;gap:16px}
  .hero-media{order:1}
  .hero-media img{height:260px;border-radius:14px}
  .hero h1{font-size:clamp(34px,10vw,52px);line-height:.94;letter-spacing:-.05em}
  .hero .sub{font-size:16px}
  .hero .actions .btn{width:100%}
  .proof .shell{justify-content:center}
  .proof-logos{justify-content:center}
  .svc-grid{grid-template-columns:1fr}
  .map-layout{grid-template-columns:1fr;gap:28px}
  .map-layout svg{max-height:340px}
  .about-grid{grid-template-columns:1fr}
  .steps-grid{grid-template-columns:1fr}
  .contact-box{grid-template-columns:1fr}
  .sec{padding:50px 0}
  .sec-header{margin-bottom:30px}
}

/* Linz-specific accent colors for map badges */
[data-map="linz"] .map-badge{background:rgba(0,86,167,.07);color:var(--blue2)}
'''

# ── Variant data ──────────────────────────────────────────────────
variants = {
    'unterhaltsreinigung-linz': {
        'title': 'Unterhaltsreinigung Linz | ÖFS Meisterbetrieb',
        'description': 'Unterhaltsreinigung in Linz für Büros, Praxen und Gewerbeflächen: fixes Team, klarer Reinigungsplan, Objektleiter und Probereinigung.',
        'hero_label': 'Unterhaltsreinigung · für Unternehmen',
        'h1': 'Unterhaltsreinigung Linz.',
        'sub': 'Für Büros, Praxen und Gewerbeflächen, die laufend sauber bleiben müssen — mit fixem Reinigungsteam, geregelter Vertretung und einem Objektleiter, der erreichbar ist, wenn etwas nicht passt.',
        'services': [
            ('Regelmäßige Bereiche', 'Arbeitsplätze, Besprechungsräume, Empfang, Teeküchen, Sanitärbereiche, Böden und Müll — sauber nach Plan, nicht nach Zufall.'),
            ('Ablauf im Objekt', 'Reinigungsplan, Uhrzeiten, Schlüssel, sensible Zonen und Prioritäten werden vor dem Start geklärt.'),
            ('Vertretung & Rückmeldung', 'Wenn jemand ausfällt oder etwas nicht passt, gibt es eine zuständige Person und keine Suche nach der richtigen Nummer.'),
        ],
        'bad_list': [
            'jede Woche neu erklären, was wichtig ist',
            'interne Nachkontrolle nach jeder Meldung',
            'wechselnde Personen ohne Objektwissen',
        ],
        'good_list': [
            'fixer Plan je Objekt',
            'Objektleiter mit Verantwortung',
            'Probereinigung vor laufender Betreuung',
        ],
        'map_intro': 'ÖFS betreut Unternehmen in Linz Stadt und im gesamten Linzer Umland — von Urfahr über die Innenstadt bis nach Traun, Leonding, Ansfelden und das Mühlviertel.',
        'map_badges': ['Linz Stadt', 'Urfahr', 'Dornach', 'Ebelsberg', 'Traun', 'Leonding', 'Ansfelden', 'Pasching', 'Hörsching', 'Pichling', 'Kleinmünchen', 'St. Magdalena'],
        'cta_form_head': 'Probereinigung für Ihr Objekt in Linz anfragen.',
        'cta_form_sub': 'Schicken Sie die Eckdaten zum Objekt. ÖFS meldet sich persönlich und klärt den passenden nächsten Schritt.',
        'proof_line': 'Meisterbetrieb seit 2006 · 90+ eigene Mitarbeiter · 200+ Firmenkunden',
    },
    'bueroreinigung-linz': {
        'title': 'Büroreinigung Linz für Unternehmen | ÖFS',
        'description': 'Büroreinigung in Linz für Unternehmen: verlässliche Reinigung mit fixem Team, Objektleiter und klarem Reinigungsplan. Probereinigung vor Vertragsstart.',
        'hero_label': 'Büroreinigung · für Unternehmen',
        'h1': 'Büroreinigung in Linz ohne Nachlaufen.',
        'sub': 'Ein Büro ist dann sauber, wenn niemand extra nachtelefonieren muss. ÖFS stellt ein fixes Team, einen verantwortlichen Objektleiter und einen Reinigungsplan, der vor dem ersten Einsatz steht.',
        'services': [
            ('Arbeitsbereiche & Böden', 'Schreibtische, Besprechungsräume, Empfang, Böden, Teeküchen, Sanitär — alle Flächen nach Plan.'),
            ('Fixe Ansprechperson', 'Ein Objektleiter kennt Ihr Objekt, reagiert auf Rückmeldungen und sorgt für Vertretung bei Ausfall.'),
            ('Außerhalb der Arbeitszeit', 'Reinigung vor oder nach Bürozeiten, abgestimmt auf Ihren Betrieb. Keine Störung im Tagesgeschäft.'),
        ],
        'bad_list': [
            'ständig wechselndes Reinigungspersonal',
            'kein Ansprechpartner bei Rückfragen',
            'Reinigungsqualität schwankt ohne Kontrolle',
        ],
        'good_list': [
            'fixes Team mit Objektkenntnis',
            'Objektleiter als direkter Ansprechpartner',
            'regelmäßige Qualitätskontrollen vor Ort',
        ],
        'map_intro': 'ÖFS reinigt Büros in ganz Linz und Umgebung — von der Innenstadt über den Hafen bis nach Leonding, Traun und Ansfelden.',
        'map_badges': ['Linz Stadt', 'Innenstadt', 'Hafen', 'Urfahr', 'Leonding', 'Traun', 'Ansfelden', 'Pasching', 'Ebelsberg', 'Dornach'],
        'cta_form_head': 'Probereinigung für Ihr Büro in Linz anfragen.',
        'cta_form_sub': 'Schicken Sie die Eckdaten zu Ihrem Büro. ÖFS meldet sich persönlich und klärt den passenden nächsten Schritt.',
        'proof_line': 'Meisterbetrieb seit 2006 · 90+ eigene Mitarbeiter · 200+ Firmenkunden',
    },
    'reinigungsfirma-linz': {
        'title': 'Reinigungsfirma Linz für Unternehmen | ÖFS',
        'description': 'Reinigungsfirma in Linz für gewerbliche Kunden: Büroreinigung, Unterhaltsreinigung und Objektbetreuung mit fixem Team und Objektleiter.',
        'hero_label': 'Reinigungsfirma · für Betriebe',
        'h1': 'Reinigungsfirma in Linz für Betriebe.',
        'sub': 'Wer eine Reinigungsfirma sucht, will nicht nur Sauberkeit — sondern einen Partner, der den Ablauf verlässlich hält. ÖFS arbeitet mit fixen Teams, klaren Plänen und einem Objektleiter pro Kunde.',
        'services': [
            ('Gewerbliche Reinigung', 'Büros, Praxen, Ordinationen, Gewerbeflächen — alles aus einer Hand mit einem verantwortlichen Team.'),
            ('Objektbetreuung', 'Jedes Objekt bekommt einen Objektleiter. Der kennt die Räume, die Prioritäten und ist bei Rückfragen direkt erreichbar.'),
            ('Flexible Intervalle', 'Täglich, wöchentlich oder nach Vereinbarung — Intervalle, die zu Ihrem Betrieb passen, nicht umgekehrt.'),
        ],
        'bad_list': [
            'anonyme Reinigungstrupps ohne feste Zuständigkeit',
            'Qualität hängt vom Tagespersonal ab',
            'keine persönliche Betreuung vor Ort',
        ],
        'good_list': [
            'fester Objektleiter als Ansprechpartner',
            'fixes Team pro Objekt',
            'Probereinigung vor laufender Betreuung',
        ],
        'map_intro': 'Als Reinigungsfirma mit Sitz in Oberösterreich betreut ÖFS gewerbliche Kunden in Linz Stadt und im gesamten Zentralraum.',
        'map_badges': ['Linz Stadt', 'Urfahr', 'Leonding', 'Traun', 'Ansfelden', 'Pasching', 'Hörsching', 'Ebelsberg', 'Pichling', 'Dornach', 'Wels'],
        'cta_form_head': 'Probereinigung für Ihr Objekt in Linz anfragen.',
        'cta_form_sub': 'Schicken Sie die Eckdaten zum Objekt. ÖFS meldet sich persönlich und klärt den passenden nächsten Schritt.',
        'proof_line': 'Meisterbetrieb seit 2006 · 90+ eigene Mitarbeiter · 200+ Firmenkunden',
    },
}

# ── Render ────────────────────────────────────────────────────────
def render(slug, v):
    map_svg = MAPS.get(slug, LINZ_MAP_SVG)
    badges = ''.join(f'<span class="map-badge">{escape(b)}</span>' for b in v['map_badges'])
    svc_rows = ''.join(
        f'<article class="svc-card"><div class="svc-icon">●</div><h3>{escape(t)}</h3><p>{escape(p)}</p></article>'
        for t, p in v['services']
    )
    bad_items = ''.join(f'<li>{escape(item)}</li>' for item in v['bad_list'])
    good_items = ''.join(f'<li>{escape(item)}</li>' for item in v['good_list'])

    return f'''<!doctype html>
<html lang="de">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <meta name="robots" content="noindex,nofollow">
  <title>{escape(v['title'])}</title>
  <meta name="description" content="{escape(v['description'])}">
  <style>{css}</style>
</head>
<body>
  <header class="nav">
    <div class="shell">
      <a href="/" aria-label="ÖFS Startseite"><img class="logo" src="../assets/logo-oefs-dark.webp" alt="ÖFS Logo"></a>
      <nav class="navlinks">
        <a href="#leistungen">Leistungen</a>
        <a href="#einzugsgebiet">Einzugsgebiet</a>
        <a href="#warum">Warum ÖFS</a>
        <a href="#anfrage" class="nav-cta">Probereinigung anfragen</a>
      </nav>
    </div>
  </header>

  <section class="hero">
    <div class="shell hero-grid">
      <div class="hero-copy">
        <div class="hero-label"><img src="../assets/at-flag.webp" alt="" aria-hidden="true">{escape(v['hero_label'])}</div>
        <h1>{v['h1']}</h1>
        <p class="sub">{escape(v['sub'])}</p>
        <div class="actions">
          <a class="btn primary" href="#anfrage">Probereinigung anfragen</a>
          <a class="btn secondary" href="#leistungen">Leistungsumfang</a>
        </div>
        <p class="micro">Unverbindlich · nur gewerbliche Objekte · ÖFS meldet sich persönlich</p>
      </div>
      <div class="hero-media">
        <img src="../assets/hero-office-cleaning.webp" alt="ÖFS Reinigungskraft in einem hellen, modernen Büro">
      </div>
    </div>
  </section>

  <section class="proof">
    <div class="shell">
      <span class="proof-label">{escape(v['proof_line'])}</span>
      <div class="proof-logos">
        <img src="../assets/logo-tabakfabrik-live.webp" alt="Tabakfabrik">
        <img src="../assets/logo-haribo-live.webp" alt="Haribo">
        <img src="../assets/logo-viadonau-live.webp" alt="via donau">
        <img src="../assets/logo-nike-live.webp" alt="Nike">
        <img src="../assets/logo-barmherzige.webp" alt="Barmherzige">
      </div>
    </div>
  </section>

  <main>
    <section class="sec" id="leistungen">
      <div class="shell">
        <div class="sec-header">
          <div class="sec-kicker">Leistungen</div>
          <h2>Was die laufende Reinigung wirklich ausmacht.</h2>
          <p>Bei gewerblicher Reinigung geht es nicht um den einzelnen Putztermin — sondern um einen Ablauf, der wiederholbar funktioniert.</p>
        </div>
        <div class="svc-grid">{svc_rows}</div>
      </div>
    </section>

    <section class="sec alt" id="einzugsgebiet">
      <div class="shell map-layout" data-map="linz">
        <div class="map-copy">
          <div class="sec-kicker">Einzugsgebiet</div>
          <h2>ÖFS ist in Linz und Umgebung für Sie vor Ort.</h2>
          <p>{escape(v['map_intro'])}</p>
          <div class="map-badges">{badges}</div>
        </div>
        {map_svg}
      </div>
    </section>

    <section class="sec" id="warum">
      <div class="shell">
        <div class="sec-header">
          <div class="sec-kicker">Der Unterschied</div>
          <h2>Sauberkeit ist das Ergebnis. Entscheidend ist, wer den Ablauf hält.</h2>
        </div>
        <div class="about-grid">
          <div class="about-card bad">
            <h3>Wenn Reinigung intern hängen bleibt</h3>
            <ul>{bad_items}</ul>
          </div>
          <div class="about-card good">
            <h3>Wenn ÖFS vorher sauber klärt</h3>
            <ul>{good_items}</ul>
          </div>
        </div>
      </div>
    </section>

    <section class="sec alt">
      <div class="shell">
        <div class="sec-header">
          <div class="sec-kicker">Ablauf</div>
          <h2>Erst das Objekt verstehen, dann laufend reinigen.</h2>
          <p>Die Probereinigung ist der sichere Einstieg: ÖFS sieht das Objekt, Sie sehen die Arbeitsweise — und danach wird entschieden.</p>
        </div>
        <div class="steps-grid">
          <article class="step-card"><div class="num">1</div><h3>Objekt beschreiben</h3><p>Fläche, Nutzung, aktuelle Probleme und gewünschte Intervalle.</p></article>
          <article class="step-card"><div class="num">2</div><h3>Zuständigkeit klären</h3><p>Wer reagiert, wer koordiniert, was bei Ausfall passiert.</p></article>
          <article class="step-card"><div class="num">3</div><h3>Probereinigung starten</h3><p>Sie sehen nicht nur ein Angebot, sondern die Arbeitsweise.</p></article>
          <article class="step-card"><div class="num">4</div><h3>Betreuung entscheiden</h3><p>Wenn Objekt und Ablauf passen, wird daraus eine geregelte Betreuung.</p></article>
        </div>
      </div>
    </section>

    <section class="sec alt" id="anfrage">
      <div class="shell contact-box">
        <div>
          <div class="sec-kicker" style="color:rgba(255,255,255,.6)">Anfrage</div>
          <h2>{escape(v['cta_form_head'])}</h2>
          <p>{escape(v['cta_form_sub'])}</p>
        </div>
        <form class="form">
          <input placeholder="Unternehmen" autocomplete="organization">
          <input placeholder="Ansprechpartner" autocomplete="name">
          <input placeholder="Telefon oder E-Mail" autocomplete="email">
          <select>
            <option>Büro</option><option>Praxis / Ordination</option><option>Gewerbefläche</option><option>Sonstiges Objekt</option>
          </select>
          <textarea placeholder="Was soll ÖFS über das Objekt wissen?"></textarea>
          <button type="button">Anfrage senden</button>
          <p class="privacy">Ihre Angaben werden zur Kontaktaufnahme und Bearbeitung Ihrer Anfrage verarbeitet.</p>
        </form>
      </div>
    </section>
  </main>

  <footer class="footer">
    <div class="shell">
      <span>ÖFS Reinigungsservice · Meisterbetrieb seit 2006</span>
      <span><a href="https://oefs-reinigungsprofis.at/impressum">Impressum</a> · <a href="https://oefs-reinigungsprofis.at/datenschutz">Datenschutz</a></span>
    </div>
  </footer>
</body>
</html>'''

# ── Build ─────────────────────────────────────────────────────────
for slug, v in variants.items():
    outdir = root / slug
    outdir.mkdir(exist_ok=True)
    (outdir / 'index.html').write_text(render(slug, v))

# Overview page
links = ''.join(
    f'<li><a href="{slug}/">{escape(v["title"])}</a><span>{escape(v["description"])}</span></li>'
    for slug, v in variants.items()
)
overview = f'''<!doctype html><html lang="de"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1"><meta name="robots" content="noindex,nofollow"><title>ÖFS Intent-Previews Linz</title><style>{css} main{{padding:70px 0}} .overview-list{{list-style:none;margin:34px 0 0;padding:0;display:grid;gap:14px}} .overview-list li{{background:#fff;border:1px solid var(--line);border-radius:20px;padding:22px;box-shadow:var(--shadow)}} .overview-list a{{display:block;color:var(--blue2);font-weight:800;font-size:22px;text-decoration:none;margin-bottom:7px}} .overview-list span{{color:var(--muted);line-height:1.45}}</style></head><body><main><div class="shell"><div class="sec-kicker">ÖFS Google Ads Message Match</div><h1>Intent-Previews Linz.</h1><p class="sub">Drei Sub-URLs für bessere Übereinstimmung zwischen Suchbegriff, Anzeige und Landingpage. Noindex, keine Live-Ads.</p><ul class="overview-list">{links}</ul></div></main></body></html>'''
(root / 'intent-previews.html').write_text(overview)

print('created', ', '.join(variants.keys()), 'and intent-previews.html')

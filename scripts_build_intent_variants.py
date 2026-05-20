from pathlib import Path
from html import escape

root = Path(__file__).parent

variants = {
    'unterhaltsreinigung-linz': {
        'intent': 'unterhaltsreinigung',
        'title': 'Unterhaltsreinigung Linz | ÖFS Meisterbetrieb',
        'description': 'Unterhaltsreinigung in Linz für Büros, Praxen und Gewerbeflächen: fixes Team, klarer Reinigungsplan, Objektleiter und Probereinigung.',
        'eyebrow': 'Unterhaltsreinigung Linz · für Unternehmen',
        'h1': 'Unterhalts­reinigung Linz.',
        'lead': 'Für Büros, Praxen und Gewerbeflächen, die laufend sauber bleiben müssen — mit fixem Reinigungsteam, geregelter Vertretung und einem Objektleiter, der erreichbar ist, wenn etwas nicht passt.',
        'field_note': 'Objektmappe: Intervalle · Räume · Vertretung · Reklamation',
        'proof_line': 'Meisterbetrieb seit 2006 · 90+ eigene Mitarbeiter · 200+ Firmenkunden',
        'pain_h2': 'Wenn laufende Reinigung im Büro wieder Thema wird, fehlt meistens kein Putzmittel. Es fehlt ein Ablauf.',
        'pain_body': 'Jemand meldet eine Kleinigkeit, dann fragt jemand nach, dann weiß die Vertretung von nichts. Genau dort kostet Reinigung plötzlich interne Zeit. ÖFS legt vor dem Start fest, wer zuständig ist, welche Räume Priorität haben und wie Rückmeldungen behandelt werden.',
        'service_h2': 'Was bei der Unterhaltsreinigung geregelt wird',
        'service_intro': 'Bei laufender Betreuung zählt nicht nur, dass gereinigt wird. Entscheidend ist, dass Räume, Intervalle und Zuständigkeit so klar sind, dass im Büro niemand hinterherorganisieren muss.',
        'rows': [
            ('Regelmäßige Bereiche', 'Arbeitsplätze, Besprechungsräume, Empfang, Teeküchen, Sanitärbereiche, Böden und Müll — sauber nach Plan, nicht nach Zufall.'),
            ('Ablauf im Objekt', 'Reinigungsplan, Uhrzeiten, Schlüssel, sensible Zonen und Prioritäten werden vor dem Start geklärt.'),
            ('Vertretung & Rückmeldung', 'Wenn jemand ausfällt oder etwas nicht passt, gibt es eine zuständige Person und keine Suche nach der richtigen Nummer.'),
        ],
        'compare_bad': ['jede Woche neu erklären, was wichtig ist', 'interne Nachkontrolle nach jeder Meldung', 'wechselnde Personen ohne Objektwissen'],
        'compare_good': ['fixer Plan je Objekt', 'Objektleiter mit Verantwortung', 'Probereinigung vor laufender Betreuung'],
        'route': 'Unterhaltsreinigung',
    },
    'reinigungsfirma-linz': {
        'intent': 'reinigungsfirma',
        'title': 'Reinigungsfirma Linz für Unternehmen | ÖFS',
        'description': 'Reinigungsfirma in Linz für Betriebe, Büros und Praxen: eigenes Personal, fixer Ansprechpartner, Objektbetreuung und Probereinigung.',
        'eyebrow': 'Reinigungsfirma Linz · Büros, Praxen, Betriebe',
        'h1': 'Reinigungsfirma in Linz für Betriebe.',
        'lead': 'Für Unternehmen, die eine Reinigungsfirma suchen, aber keine wechselnden Aushilfen, keine Hotline-Schleifen und kein Nachlaufen wegen Kleinigkeiten wollen.',
        'field_note': 'Objektmappe: Ansprechpartner · eigenes Team · laufende Betreuung',
        'proof_line': 'Gewerbliche Objekte · eigenes Personal · Probereinigung vor Bindung',
        'pain_h2': 'Eine Reinigungsfirma entlastet erst dann, wenn jemand wirklich zuständig ist.',
        'pain_body': 'Viele Anbieter können reinigen. Im Alltag entscheidet aber, ob Ihr Objekt bekannt ist, ob Rückmeldungen ankommen und ob bei Ausfall jemand organisiert. Genau diese Verantwortung muss vor dem ersten laufenden Termin geklärt sein.',
        'service_h2': 'Welche Betreuung ÖFS für Betriebe in Linz übernimmt',
        'service_intro': 'Für Betriebe zählt nicht der einzelne Putztermin, sondern eine Betreuung, die wiederholbar funktioniert: gleiches Objektwissen, klare Rückmeldung und eine verantwortliche Person.',
        'rows': [
            ('Büros & Betriebe', 'Büroflächen, Besprechungsräume, Empfang, Allgemeinflächen, Küchen und Sanitärbereiche.'),
            ('Organisation', 'Fixer Ansprechpartner, eigenes geschultes Personal, Vertretung bei Krankheit oder Urlaub.'),
            ('Start mit wenig Risiko', 'Objekt kurz beschreiben, passende Betreuung abstimmen, Probereinigung vereinbaren und danach entscheiden.'),
        ],
        'compare_bad': ['Anbieter kennt das Objekt kaum', 'Reklamationen verschwinden zwischen Team und Büro', 'jeder Termin fühlt sich wie ein Neustart an'],
        'compare_good': ['eine verantwortliche Person', 'eigenes Team mit Vertretung', 'klare Rückmeldung nach der Probereinigung'],
        'route': 'Reinigungsfirma',
    },
    'bueroreinigung-linz': {
        'intent': 'bueroreinigung',
        'title': 'Büroreinigung Linz für Unternehmen | ÖFS',
        'description': 'Büroreinigung in Linz für Unternehmen: fixes Team, eigener Ansprechpartner, klare Abläufe und Probereinigung vor laufender Betreuung.',
        'eyebrow': 'Büroreinigung Linz · für Unternehmen',
        'h1': 'Büroreinigung in Linz ohne Nachlaufen.',
        'lead': 'Für Büros, Praxen und Betriebe, die saubere Arbeitsplätze brauchen — ohne dauernde Rückfragen, wechselnde Zuständigkeiten und interne Nachkontrolle nach jeder Reklamation.',
        'field_note': 'Objektmappe: Arbeitsplätze · Nebenräume · Ansprechpartner',
        'proof_line': 'Büros · Praxen · gewerbliche Flächen · Probereinigung',
        'pain_h2': 'Büroreinigung stört dann, wenn sie im Büro ständig wieder Thema wird.',
        'pain_body': 'Die Küche ist nicht sauber, im Besprechungsraum sieht man Spuren, jemand muss wieder schreiben oder anrufen. Gute Büroreinigung reduziert genau diese internen Schleifen, weil Räume, Zuständigkeit und Rückmeldung vorher sauber geregelt sind.',
        'service_h2': 'Welche Bereiche in der Büroreinigung sauber geregelt werden',
        'service_intro': 'Büroreinigung wird dann entlastend, wenn Arbeitsbereiche, Nebenräume und Rückmeldungen vor dem Start sauber geregelt sind.',
        'rows': [
            ('Arbeitsbereiche', 'Schreibtische, Oberflächen, Besprechungsräume, Empfang, Verkehrsflächen und Müll.'),
            ('Nebenräume', 'Teeküchen, Aufenthaltsräume, Sanitärbereiche, Böden und sensible Zonen nach Abstimmung.'),
            ('Betreuung', 'Fixer Objektleiter, eigenes Reinigungsteam, Vertretung bei Ausfall und Probereinigung vor laufender Betreuung.'),
        ],
        'compare_bad': ['Sauberkeit hängt an Einzelpersonen', 'Office muss nachtelefonieren', 'Kleinigkeiten werden zu Dauerthemen'],
        'compare_good': ['fixer Ansprechpartner', 'klarer Ablauf je Raum', 'Rückmeldung und Nachbesserung geregelt'],
        'route': 'Büroreinigung',
    },
}

css = r'''
:root{--blue:#0571d3;--blue2:#0a58a8;--ink:#101820;--muted:#5d6874;--paper:#fbfcfb;--line:#d9e1e8;--soft:#eef6ff;--green:#16a15a;--red:#d63c32;--pad:clamp(22px,4vw,48px);--max:1180px;--radius:28px;--shadow:0 22px 70px rgba(16,24,32,.12)}
*{box-sizing:border-box}html{scroll-behavior:smooth}body{margin:0;background:#f3f6f8;color:var(--ink);font-family:Aptos,"Segoe UI",Tahoma,sans-serif;-webkit-font-smoothing:antialiased}a{color:inherit}.shell{width:min(var(--max),calc(100% - var(--pad)*2));margin:0 auto}.nav{position:sticky;top:0;z-index:50;background:rgba(251,252,251,.92);backdrop-filter:blur(14px);border-bottom:1px solid rgba(16,24,32,.08)}.nav .shell{height:78px;display:flex;align-items:center;justify-content:space-between;gap:24px}.logo{height:38px;width:auto}.navlinks{display:flex;align-items:center;gap:22px;font-size:14px;font-weight:800;color:#2b3844}.navlinks a{text-decoration:none}.nav-cta{background:var(--blue);color:#fff;text-decoration:none;border-radius:999px;padding:13px 18px;font-weight:950;box-shadow:0 8px 20px rgba(5,113,211,.2)}
.hero{position:relative;overflow:hidden;background:linear-gradient(90deg,#f7fafc 0%,#f7fafc 58%,#dfefff 58%,#dfefff 100%)}.hero:before{content:"";position:absolute;inset:0;background:linear-gradient(rgba(5,113,211,.045) 1px,transparent 1px),linear-gradient(90deg,rgba(5,113,211,.045) 1px,transparent 1px);background-size:42px 42px;mask-image:linear-gradient(90deg,rgba(0,0,0,.8),transparent 72%);pointer-events:none}.hero-grid{position:relative;display:grid;grid-template-columns:minmax(0,1.02fr) minmax(410px,.98fr);align-items:center;gap:42px;min-height:660px;padding:54px 0 62px}.hero-copy{padding:34px 0}.eyebrow{display:inline-flex;gap:9px;align-items:center;border:1px solid rgba(5,113,211,.22);background:#fff;border-radius:999px;padding:8px 12px;font-size:13px;font-weight:950;color:var(--blue2);margin-bottom:22px}.eyebrow img{width:19px;height:13px;object-fit:cover;border-radius:2px}.hero h1{font-family:Georgia,"Times New Roman",serif;font-size:clamp(48px,6.5vw,88px);line-height:.9;letter-spacing:-.06em;margin:0 0 24px;max-width:780px}.lead{font-size:clamp(18px,2.1vw,22px);line-height:1.48;color:#33414f;max-width:670px;margin:0 0 30px}.actions{display:flex;gap:13px;flex-wrap:wrap;align-items:center}.btn{display:inline-flex;align-items:center;justify-content:center;min-height:54px;border-radius:999px;padding:0 22px;font-weight:950;text-decoration:none;border:1px solid transparent;font-size:16px}.btn.primary{background:var(--blue);color:#fff;box-shadow:0 12px 26px rgba(5,113,211,.24)}.btn.secondary{background:#fff;color:var(--blue2);border-color:rgba(5,113,211,.24)}.micro{font-size:13px;color:#6a7480;margin-top:13px;line-height:1.4}.hero-media{position:relative}.photo-card{position:relative;border-radius:34px;overflow:hidden;background:#fff;box-shadow:var(--shadow);border:1px solid rgba(16,24,32,.08);transform:rotate(.65deg)}.photo-card img.hero-img{display:block;width:100%;height:560px;object-fit:cover;object-position:center}.protocol{position:absolute;left:-22px;bottom:26px;width:min(350px,80%);background:rgba(255,255,255,.94);border:1px solid rgba(16,24,32,.12);border-left:7px solid var(--blue);box-shadow:0 18px 50px rgba(16,24,32,.16);padding:18px 18px 16px;border-radius:18px}.protocol small{display:block;text-transform:uppercase;letter-spacing:.14em;color:var(--blue2);font-weight:950;font-size:10px;margin-bottom:7px}.protocol strong{display:block;font-size:18px;line-height:1.18}.stamp{position:absolute;right:20px;top:20px;background:#fff;border-radius:50%;width:86px;height:86px;display:grid;place-items:center;box-shadow:0 12px 32px rgba(16,24,32,.14)}.stamp img{width:66px;height:66px;object-fit:contain}.proofstrip{background:#fff;border-block:1px solid rgba(16,24,32,.08)}.proofstrip .shell{display:grid;grid-template-columns:260px 1fr;gap:26px;align-items:center;padding-top:24px;padding-bottom:24px}.prooftext{font-weight:950;color:#24313d;line-height:1.32}.logos{display:grid;grid-template-columns:repeat(5,minmax(0,1fr));gap:18px;align-items:center}.logos img{max-width:100%;max-height:42px;object-fit:contain;filter:grayscale(1);opacity:.7}.intent-nav{background:#e9f4ff;border-bottom:1px solid rgba(5,113,211,.16)}.intent-nav .shell{display:flex;gap:10px;flex-wrap:wrap;padding-top:13px;padding-bottom:13px}.intent-chip{border:1px solid rgba(5,113,211,.26);background:#fff;color:#0a58a8;border-radius:999px;padding:10px 14px;text-decoration:none;font-size:13px;font-weight:950}.intent-chip.active{background:var(--blue);color:#fff}.section{padding:82px 0}.section.white{background:#fff}.section.blueprint{background:#f6fbff}.kicker{text-transform:uppercase;letter-spacing:.15em;color:var(--blue2);font-size:12px;font-weight:950;margin-bottom:10px}.section-title{max-width:800px;margin-bottom:34px}.section h2{font-family:Georgia,"Times New Roman",serif;font-size:clamp(34px,4.8vw,62px);line-height:.98;letter-spacing:-.045em;margin:0 0 18px}.section p{font-size:18px;line-height:1.58;color:#53606d}.pain-layout{display:grid;grid-template-columns:minmax(0,.95fr) minmax(360px,.75fr);gap:46px;align-items:start}.field-card{background:#fff;border:1px solid var(--line);border-radius:30px;padding:26px;box-shadow:0 14px 42px rgba(16,24,32,.08);position:relative}.field-card:before{content:"ÖFS OBJEKTPROTOKOLL";position:absolute;right:22px;top:18px;color:rgba(5,113,211,.16);font-size:11px;font-weight:950;letter-spacing:.16em}.field-row{display:grid;grid-template-columns:124px 1fr;gap:14px;padding:15px 0;border-bottom:1px solid #e8edf2}.field-row:last-child{border-bottom:0}.field-row b{font-size:12px;text-transform:uppercase;letter-spacing:.11em;color:#71808d}.field-row span{font-size:16px;line-height:1.38;color:#263440}.service-list{display:grid;gap:14px}.service-row{display:grid;grid-template-columns:230px 1fr;gap:28px;background:#fff;border:1px solid var(--line);border-radius:24px;padding:24px;box-shadow:0 10px 30px rgba(16,24,32,.055)}.service-row h3{font-size:23px;line-height:1.1;margin:0;color:#13202b}.service-row p{margin:0;color:#4b5966}.compare{display:grid;grid-template-columns:1fr 1fr;gap:18px}.compare-card{border-radius:28px;padding:26px;border:1px solid var(--line);background:#fff}.compare-card.good{border-color:rgba(22,161,90,.28);box-shadow:0 14px 38px rgba(22,161,90,.08)}.compare-card.bad{background:#fff9f8}.compare-card h3{margin:0 0 15px;font-size:24px}.compare-card ul{list-style:none;margin:0;padding:0;display:grid;gap:12px}.compare-card li{position:relative;padding-left:34px;line-height:1.42;color:#3d4852}.compare-card li:before{position:absolute;left:0;top:-2px;width:24px;height:24px;border-radius:50%;display:grid;place-items:center;color:#fff;font-weight:950;font-size:14px}.compare-card.good li:before{content:"✓";background:var(--green)}.compare-card.bad li:before{content:"×";background:var(--red)}.steps{display:grid;grid-template-columns:repeat(4,minmax(0,1fr));gap:16px}.step{background:#fff;border:1px solid var(--line);border-radius:24px;padding:22px;min-height:190px}.step b{display:inline-grid;place-items:center;width:34px;height:34px;border-radius:50%;background:var(--blue);color:#fff;margin-bottom:18px}.step h3{margin:0 0 10px;font-size:22px}.step p{font-size:16px;margin:0}.formbox{display:grid;grid-template-columns:.85fr 1fr;gap:30px;background:#10202d;color:#fff;border-radius:36px;padding:34px;box-shadow:var(--shadow)}.formbox h2{color:#fff}.formbox p{color:rgba(255,255,255,.78)}.form{display:grid;gap:13px}.form input,.form select,.form textarea{width:100%;border:1px solid rgba(255,255,255,.18);background:rgba(255,255,255,.08);color:#fff;border-radius:16px;min-height:52px;padding:13px 15px;font:inherit}.form textarea{min-height:112px}.form input::placeholder,.form textarea::placeholder{color:rgba(255,255,255,.54)}.form button{min-height:56px;border:0;border-radius:999px;background:#fff;color:var(--blue2);font-weight:950;font-size:16px}.privacy{font-size:12px!important;color:rgba(255,255,255,.62)!important;margin:0}.footer{padding:30px 0;color:#71808d;font-size:13px}.footer .shell{display:flex;justify-content:space-between;gap:18px;flex-wrap:wrap}
@media (max-width:920px){.nav .shell{height:70px}.navlinks a:not(.nav-cta){display:none}.hero{background:#f7fafc}.hero-grid{display:flex;flex-direction:column;gap:26px;min-height:0;padding:18px 0 42px}.hero-media{order:1;width:100%}.hero-copy{order:2;padding:0}.photo-card{transform:none;border-radius:24px}.photo-card img.hero-img{height:270px}.protocol{left:14px;right:14px;bottom:14px;width:auto;padding:14px;border-radius:16px}.protocol strong{font-size:15px}.stamp{width:66px;height:66px;right:14px;top:14px}.stamp img{width:50px;height:50px}.eyebrow{font-size:12px;margin-bottom:16px}.hero h1{font-size:clamp(38px,12vw,52px);line-height:.92;letter-spacing:-.055em;margin-bottom:18px}.lead{font-size:17px}.actions .btn{width:100%}.proofstrip .shell{grid-template-columns:1fr;gap:16px}.logos{grid-template-columns:repeat(2,1fr)}.pain-layout,.compare,.formbox{grid-template-columns:1fr}.service-row{grid-template-columns:1fr;gap:10px}.steps{grid-template-columns:1fr}.section{padding:58px 0}.field-row{grid-template-columns:1fr}.footer .shell{display:block}.intent-chip{flex:1 1 100%;text-align:center}.nav-cta{padding:11px 13px;font-size:13px}.logo{height:32px}}
'''

def render_list(items):
    return ''.join(f'<li>{escape(item)}</li>' for item in items)

def render_rows(rows):
    return ''.join(f'<article class="service-row"><h3>{escape(t)}</h3><p>{escape(p)}</p></article>' for t,p in rows)

def render(slug, v):
    chips = ''.join(
        f'<a class="intent-chip {"active" if k==slug else ""}" href="../{k}/">{variants[k]["route"]} Linz</a>'
        for k in ['bueroreinigung-linz','unterhaltsreinigung-linz','reinigungsfirma-linz']
    )
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
<body data-intent="{escape(v['intent'])}">
  <header class="nav"><div class="shell"><a href="../intent-previews.html" aria-label="ÖFS Preview Übersicht"><img class="logo" src="../assets/logo-oefs-dark.webp" alt="ÖFS Logo"></a><nav class="navlinks"><a href="#ablauf">Ablauf</a><a href="#vergleich">Warum ÖFS</a><a class="nav-cta" href="#anfrage">Probereinigung anfragen</a></nav></div></header>

  <section class="hero">
    <div class="shell hero-grid">
      <div class="hero-copy">
        <div class="eyebrow"><img src="../assets/at-flag.webp" alt="Österreich Flagge">{escape(v['eyebrow'])}</div>
        <h1>{v['h1']}</h1>
        <p class="lead">{escape(v['lead'])}</p>
        <div class="actions"><a class="btn primary" href="#anfrage">Probereinigung anfragen</a><a class="btn secondary" href="#leistungen">Leistungsumfang ansehen</a></div>
        <p class="micro">Unverbindlich starten · nur gewerbliche Objekte · ÖFS meldet sich persönlich</p>
      </div>
      <div class="hero-media">
        <figure class="photo-card"><img class="hero-img" src="../assets/hero-office-cleaning.webp" alt="ÖFS Reinigungskraft in einem hellen Büro"><div class="stamp"><img src="../assets/meisterbetrieb.webp" alt="Meisterbetrieb"></div><figcaption class="protocol"><small>ÖFS Einsatzlogik</small><strong>{escape(v['field_note'])}</strong></figcaption></figure>
      </div>
    </div>
  </section>

  <section class="proofstrip"><div class="shell"><div class="prooftext">{escape(v['proof_line'])}</div><div class="logos"><img src="../assets/logo-tabakfabrik-live.webp" alt="Tabakfabrik"><img src="../assets/logo-haribo-live.webp" alt="Haribo"><img src="../assets/logo-viadonau-live.webp" alt="via donau"><img src="../assets/logo-nike-live.webp" alt="Nike"><img src="../assets/logo-barmherzige.webp" alt="Barmherzige"></div></div></section>
  <div class="intent-nav"><div class="shell">{chips}</div></div>

  <main>
    <section class="section white">
      <div class="shell pain-layout">
        <div><div class="kicker">Worum es wirklich geht</div><h2>{escape(v['pain_h2'])}</h2><p>{escape(v['pain_body'])}</p></div>
        <aside class="field-card" aria-label="Objektprotokoll">
          <div class="field-row"><b>Objekt</b><span>Büro, Praxis oder gewerbliche Fläche in Linz</span></div>
          <div class="field-row"><b>Problem</b><span>Nachtelefonieren, wechselnde Zuständigkeit, unklare Vertretung</span></div>
          <div class="field-row"><b>Start</b><span>Probereinigung, bevor die laufende Betreuung entschieden wird</span></div>
          <div class="field-row"><b>Verantwortung</b><span>Objektleiter, eigenes Team, klare Reklamationsabwicklung</span></div>
        </aside>
      </div>
    </section>

    <section class="section blueprint" id="leistungen">
      <div class="shell"><div class="section-title"><div class="kicker">{escape(v['route'])} Linz</div><h2>{escape(v['service_h2'])}</h2><p>{escape(v['service_intro'])}</p></div><div class="service-list">{render_rows(v['rows'])}</div></div>
    </section>

    <section class="section white" id="vergleich">
      <div class="shell"><div class="section-title"><div class="kicker">Der Unterschied im Alltag</div><h2>Sauberkeit ist das Ergebnis. Entscheidend ist, wer den Ablauf hält.</h2></div><div class="compare"><article class="compare-card bad"><h3>Wenn Reinigung intern hängen bleibt</h3><ul>{render_list(v['compare_bad'])}</ul></article><article class="compare-card good"><h3>Wenn ÖFS vorher sauber klärt</h3><ul>{render_list(v['compare_good'])}</ul></article></div></div>
    </section>

    <section class="section blueprint" id="ablauf">
      <div class="shell"><div class="section-title"><div class="kicker">Ablauf</div><h2>Erst Objekt verstehen, dann laufend reinigen.</h2><p>Die Probereinigung ist der sichere Einstieg: ÖFS sieht das Objekt, Sie sehen die Arbeitsweise, und danach wird entschieden, ob die laufende Betreuung passt.</p></div><div class="steps"><article class="step"><b>1</b><h3>Objekt kurz beschreiben</h3><p>Fläche, Nutzung, aktuelle Probleme und gewünschte Intervalle.</p></article><article class="step"><b>2</b><h3>Zuständigkeit klären</h3><p>Wer reagiert, wer koordiniert, was bei Ausfall passiert.</p></article><article class="step"><b>3</b><h3>Probereinigung starten</h3><p>Sie sehen nicht nur ein Angebot, sondern die Arbeitsweise.</p></article><article class="step"><b>4</b><h3>Laufende Betreuung entscheiden</h3><p>Wenn Objekt und Ablauf passen, wird daraus eine geregelte Betreuung.</p></article></div></div>
    </section>

    <section class="section white" id="anfrage"><div class="shell formbox"><div><div class="kicker">Anfrage</div><h2>Probereinigung für Ihr Objekt in Linz anfragen.</h2><p>Schicken Sie die Eckdaten zum Objekt. ÖFS meldet sich persönlich und klärt den passenden nächsten Schritt.</p></div><form class="form"><input placeholder="Unternehmen" autocomplete="organization"><input placeholder="Ansprechpartner" autocomplete="name"><input placeholder="Telefon oder E-Mail" autocomplete="email"><select><option>Büro</option><option>Praxis / Ordination</option><option>Gewerbefläche</option><option>Sonstiges Objekt</option></select><textarea placeholder="Was soll ÖFS über das Objekt wissen?"></textarea><button type="button">Anfrage senden</button><p class="privacy">Ihre Angaben werden zur Kontaktaufnahme und Bearbeitung Ihrer Anfrage verarbeitet.</p></form></div></section>
  </main>
  <footer class="footer"><div class="shell"><span>ÖFS Reinigungsservice</span><span>{escape(v['title'])}</span></div></footer>
</body>
</html>'''

for slug, v in variants.items():
    outdir = root / slug
    outdir.mkdir(exist_ok=True)
    (outdir / 'index.html').write_text(render(slug, v))

links = ''.join(f'<li><a href="{slug}/">{escape(v["title"])}</a><span>{escape(v["description"])}</span></li>' for slug,v in variants.items())
overview = f'''<!doctype html><html lang="de"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1"><meta name="robots" content="noindex,nofollow"><title>ÖFS Intent-Previews Linz</title><style>{css}main{{padding:70px 0}}.overview-list{{list-style:none;margin:34px 0 0;padding:0;display:grid;gap:14px}}.overview-list li{{background:#fff;border:1px solid var(--line);border-radius:24px;padding:22px;box-shadow:0 10px 30px rgba(16,24,32,.06)}}.overview-list a{{display:block;color:var(--blue2);font-weight:950;font-size:22px;text-decoration:none;margin-bottom:7px}}.overview-list span{{color:var(--muted);line-height:1.45}}</style></head><body><main><div class="shell"><div class="kicker">ÖFS Google Ads Message Match</div><h1>Intent-Previews Linz.</h1><p class="lead">Drei Sub-URLs für bessere Übereinstimmung zwischen Suchbegriff, Anzeige und Landingpage. Noindex, keine Live-Ads.</p><ul class="overview-list">{links}</ul></div></main></body></html>'''
(root / 'intent-previews.html').write_text(overview)
print('created', ', '.join(variants.keys()), 'and intent-previews.html')

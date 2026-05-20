from pathlib import Path

root = Path(__file__).parent
base = (root / 'index.html').read_text()
base = base.replace('  </style>', '    @media (max-width:900px){body[data-intent] .hero-grid{padding:10px var(--pad) 46px}body[data-intent] h1{font-size:clamp(27px,7.1vw,29px);line-height:1.08;letter-spacing:-.04em;max-width:100%}body[data-intent] .hero-copy{max-width:100%}body[data-intent] .actions .btn{width:100%}}\n  </style>')

extra_css = '''
    .intent-nav{background:#edf6ff;border-bottom:1px solid rgba(55,154,254,.18)}body[data-intent] .hero-grid{grid-template-columns:minmax(0,1.16fr) minmax(380px,.84fr)}body[data-intent] h1{font-size:clamp(43px,5.7vw,72px);max-width:760px;overflow-wrap:break-word;hyphens:auto}.intent-nav .shell{display:flex;gap:10px;flex-wrap:wrap;padding-top:14px;padding-bottom:14px}.intent-chip{display:inline-flex;align-items:center;justify-content:center;border:1px solid rgba(55,154,254,.32);background:#fff;color:#075cae;border-radius:999px;padding:10px 14px;font-size:13px;font-weight:950;text-decoration:none}.intent-chip.active{background:var(--blue);color:#fff;border-color:var(--blue)}
    .service-grid{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:18px;margin-top:34px}.service-card{background:#fff;border:1px solid var(--line);border-radius:var(--radius);padding:27px;box-shadow:0 12px 34px rgba(1,1,1,.055)}.service-card h3{font-size:22px;line-height:1.12;margin:0 0 12px;color:var(--ink)}.service-card ul{margin:0;padding:0;list-style:none;display:grid;gap:9px;color:var(--muted);line-height:1.42}.service-card li{position:relative;padding-left:22px}.service-card li:before{content:"✓";position:absolute;left:0;top:0;color:#10a94d;font-weight:950}.local-line{margin-top:24px;background:#f7fbff;border:1px solid rgba(55,154,254,.22);border-radius:22px;padding:18px 20px;color:var(--muted);line-height:1.48}.local-line strong{color:var(--ink)}
'''
base = base.replace('    .form{display:grid;', extra_css + '    .form{display:grid;')
base = base.replace('.pain-grid,.guarantee-grid,.testbar,.form{grid-template-columns:1fr}', '.pain-grid,.guarantee-grid,.service-grid,.testbar,.form{grid-template-columns:1fr}')
base = base.replace('<section class="strip">', '<div class="intent-nav"><div class="shell"><a class="intent-chip" data-intent="bueroreinigung" href="../bueroreinigung-linz/">Büroreinigung Linz</a><a class="intent-chip" data-intent="unterhaltsreinigung" href="../unterhaltsreinigung-linz/">Unterhaltsreinigung Linz</a><a class="intent-chip" data-intent="reinigungsfirma" href="../reinigungsfirma-linz/">Reinigungsfirma Linz</a></div></div>\n  <section class="strip">')
base = base.replace('</section>\n  <main>', '</section>\n  <main>\n    __SERVICE_SECTION__')
base = base.replace("document.querySelectorAll('.angle').forEach", "document.querySelectorAll('.intent-chip').forEach(a=>{if(a.dataset.intent===document.body.dataset.intent)a.classList.add('active')});\n    document.querySelectorAll('.angle').forEach")
base = base.replace('<body>', '<body data-intent="__INTENT__">')

variants = {
    'unterhaltsreinigung-linz': {
        'intent': 'unterhaltsreinigung',
        'title': 'Unterhaltsreinigung Linz | ÖFS Meisterbetrieb',
        'description': 'Unterhaltsreinigung in Linz für Büros, Praxen und Gewerbeflächen: fixes Team, klarer Reinigungsplan, Objektleiter und Probereinigung.',
        'eyebrow': 'Unterhaltsreinigung Linz · für Unternehmen',
        'h1': 'Unterhalts&shy;reinigung Linz.',
        'hero': 'Für Büros, Praxen und Gewerbeflächen, die laufend sauber bleiben müssen — mit <strong>fixem Reinigungsteam</strong>, geregelter Vertretung und erreichbarem Objektleiter.',
        'problem_h2': 'Laufende Reinigung wird teuer, wenn der Ablauf jedes Mal neu erklärt werden muss.',
        'problem_lead': 'Unterhaltsreinigung soll im Alltag verschwinden: Räume sind sauber, Zuständigkeiten sind klar, Ausfälle sind geregelt. Wenn das nicht passiert, landet die Arbeit wieder intern.',
        'service_kicker': 'Leistungsumfang',
        'service_h2': 'Was bei der Unterhaltsreinigung in Linz geregelt wird.',
        'service_lead': 'Nicht nur reinigen, sondern den laufenden Ablauf sauber organisieren: Intervalle, Räume, Prioritäten, Vertretung und Rückmeldung.',
        'cards': [
            ('Regelmäßige Bürobereiche', ['Arbeitsplätze und Besprechungsräume', 'Empfang und Verkehrsflächen', 'Teeküchen und Sanitärbereiche', 'Böden, Oberflächen und Müll']),
            ('Ablauf und Zuständigkeit', ['fixer Reinigungsplan je Objekt', 'zuständiger Objektleiter', 'geregelte Vertretung bei Ausfall', 'klare Reklamationsabwicklung']),
            ('Geeignete Objekte', ['Büros und Kanzleien', 'Ordinationen und Praxen', 'Gewerbeflächen', 'laufende Objektbetreuung in Linz und Umgebung'])
        ],
        'local': 'Für Unternehmen in Linz und Umgebung, wenn die Reinigung regelmäßig funktionieren muss — nicht nur als Einzelputz.',
        'angle1': ('Unterhaltsreinigung, bei der der Ablauf steht.', 'Klare Intervalle', 'Wenn Räume, Zeiten und Zuständigkeiten definiert sind, muss niemand jede Woche neu erklären, was zu tun ist.'),
        'angle2': ('Ein Objektleiter für Ihre laufende Reinigung in Linz.', 'Fixe Zuständigkeit', 'Eine verantwortliche Person kennt Objekt, Prioritäten und Rückmeldungen — damit Themen nicht zwischen Team und Hotline verschwinden.'),
        'angle3': ('Unterhaltsreinigung, die nicht wieder im Office landet.', 'Intern entlasten', 'Wenn Reinigung ständig intern nachbesprochen wird, fehlt ein Ablauf, der Verantwortung klar bei ÖFS hält.')
    },
    'reinigungsfirma-linz': {
        'intent': 'reinigungsfirma',
        'title': 'Reinigungsfirma Linz für Unternehmen | ÖFS',
        'description': 'Reinigungsfirma in Linz für Betriebe, Büros und Praxen: eigenes Personal, fixer Ansprechpartner, Objektbetreuung und Probereinigung.',
        'eyebrow': 'Reinigungsfirma Linz · Büros, Praxen, Betriebe',
        'h1': 'Reinigungsfirma in Linz für Betriebe.',
        'hero': 'Für Unternehmen, die keine wechselnden Aushilfen und keine unklare Zuständigkeit wollen. ÖFS betreut gewerbliche Objekte mit <strong>eigenem Team</strong>, Objektleiter und Probereinigung.',
        'problem_h2': 'Eine Reinigungsfirma ist nur dann entlastend, wenn jemand wirklich zuständig ist.',
        'problem_lead': 'Viele Anbieter versprechen Sauberkeit. Im Alltag zählt aber, wer reagiert, wer das Objekt kennt und was passiert, wenn etwas nicht passt.',
        'service_kicker': 'Für gewerbliche Objekte',
        'service_h2': 'Büroreinigung, Unterhaltsreinigung und Objektbetreuung aus einer Hand.',
        'service_lead': 'Die Seite ist für Unternehmen gedacht, die eine verlässliche Reinigungsfirma in Linz suchen — nicht für Privathaushalte oder einzelne Putztermine.',
        'cards': [
            ('Büros und Betriebe', ['Büroflächen und Besprechungsräume', 'Empfangs- und Allgemeinflächen', 'Küchen und Sanitärbereiche', 'regelmäßige Betreuung statt Einzelputz']),
            ('Organisation', ['fixer Ansprechpartner', 'eigenes geschultes Personal', 'Vertretung bei Krankheit oder Urlaub', 'Rückmeldung bei Reklamationen']),
            ('Start mit wenig Risiko', ['Objekt kurz beschreiben', 'passende Betreuung abstimmen', 'Probereinigung vereinbaren', 'danach laufende Betreuung entscheiden'])
        ],
        'local': 'Für Linz, Leonding, Traun, Pasching und Umgebung nur verwenden, wenn diese regionale Betreuung operativ sauber zugesagt werden kann.',
        'angle1': ('Eine Reinigungsfirma, der Sie nicht nachlaufen müssen.', 'Weniger Nachtelefonieren', 'Wenn jede Meldung eine zweite Nachfrage braucht, ist nicht die einzelne Reinigung das Problem, sondern die Zuständigkeit.'),
        'angle2': ('Ein fixer Ansprechpartner für Ihr Objekt in Linz.', 'Klare Zuständigkeit', 'Ein Name, eine Nummer, eine verantwortliche Person — damit Themen nicht jedes Mal neu erklärt werden müssen.'),
        'angle3': ('Reinigungsfirma für Betriebe, nicht für einmaliges Durchwischen.', 'B2B passend', 'ÖFS richtet sich an gewerbliche Objekte, bei denen laufende Sauberkeit und verlässliche Betreuung wichtiger sind als ein Einzeltermin.')
    },
    'bueroreinigung-linz': {
        'intent': 'bueroreinigung',
        'title': 'Büroreinigung Linz für Unternehmen | ÖFS',
        'description': 'Büroreinigung in Linz für Unternehmen: fixes Team, eigener Ansprechpartner, klare Abläufe und Probereinigung vor laufender Betreuung.',
        'eyebrow': 'Büroreinigung Linz · für Unternehmen',
        'h1': 'Büroreinigung in Linz ohne Nachlaufen.',
        'hero': 'Für Büros, Praxen und Betriebe, die saubere Arbeitsplätze brauchen — ohne wechselnde Zuständigkeiten, ohne dauernde Rückfragen und mit <strong>Probereinigung</strong> vor der laufenden Betreuung.',
        'problem_h2': 'Büroreinigung stört dann, wenn sie im Büro ständig Thema bleibt.',
        'problem_lead': 'Wenn Küche, Sanitärbereich oder Besprechungsraum nicht passen, muss intern jemand reagieren. Gute Büroreinigung reduziert diese Rückfragen statt neue Arbeit zu erzeugen.',
        'service_kicker': 'Büroreinigung Linz',
        'service_h2': 'Welche Bereiche in der Büroreinigung sauber geregelt werden.',
        'service_lead': 'ÖFS legt vor dem Start fest, welche Flächen, Intervalle und Zuständigkeiten für Ihr Büro wichtig sind.',
        'cards': [
            ('Arbeitsbereiche', ['Schreibtische und Oberflächen', 'Besprechungsräume', 'Empfang und Verkehrsflächen', 'Müll und Verbrauchsmaterialien']),
            ('Nebenräume', ['Teeküchen und Aufenthaltsräume', 'Sanitärbereiche', 'Böden und sensible Zonen', 'Ordinationen/Praxen nach Abstimmung']),
            ('Betreuung', ['fixer Objektleiter', 'eigenes Reinigungsteam', 'Vertretung bei Ausfall', 'Probereinigung vor laufender Betreuung'])
        ],
        'local': 'Für Büroflächen und gewerbliche Objekte in Linz, bei denen laufende Sauberkeit verlässlich organisiert sein muss.',
        'angle1': ('Büroreinigung, bei der Sie nicht nachtelefonieren müssen.', 'Weniger Nachtelefonieren', 'Wenn jede Meldung eine zweite und dritte Nachfrage braucht, ist die Reinigung nicht entlastend genug organisiert.'),
        'angle2': ('Ein fester Ansprechpartner für Ihr Büro in Linz.', 'Klare Zuständigkeit', 'Ein fester Ansprechpartner ist oft der Unterschied zwischen gemeldeter Beschwerde und gelöstem Thema.'),
        'angle3': ('Büroreinigung, die nicht wieder im Office hängen bleibt.', 'Intern entlasten', 'Wenn Reinigung ständig im Team besprochen wird, braucht es einen Ablauf, bei dem ÖFS die Verantwortung übernimmt.')
    }
}

service_tpl = '''<section class="section" id="leistungen">
      <div class="shell"><div class="section-title"><div class="kicker">{service_kicker}</div><h2>{service_h2}</h2><p class="lead">{service_lead}</p></div>
      <div class="service-grid">{cards}</div><p class="local-line"><strong>Lokaler Bezug:</strong> {local}</p></div>
    </section>'''
card_tpl = '<article class="service-card"><h3>{title}</h3><ul>{lis}</ul></article>'

for slug, v in variants.items():
    html = base
    html = html.replace('__INTENT__', v['intent'])
    html = html.replace('<title>ÖFS Büroreinigung Wien</title>', f'<title>{v["title"]}</title>')
    html = html.replace('content="ÖFS Büroreinigung für Unternehmen in Wien mit fixem Team, fixer Zuständigkeit und Probereinigung."', f'content="{v["description"]}"')
    html = html.replace('Büroreinigung Wien · für Unternehmen', v['eyebrow'])
    html = html.replace('Verlässliche Büroreinigung für Firmen in Wien.', v['h1'])
    html = html.replace('Für Büros, Praxen und Betriebe, die <strong>nicht ständig nachtelefonieren</strong> wollen. Mit fixem Ansprechpartner, geregelter Vertretung und Probereinigung vor der laufenden Betreuung.', v['hero'])
    html = html.replace('Büroreinigung Wien · Linz · Graz', f'{v["title"]}')
    html = html.replace('Erst ist es nur eine Meldung. Dann telefoniert jemand wieder hinterher.', v['problem_h2'])
    html = html.replace('Die Küche ist nicht sauber, der Ansprechpartner wechselt, die Vertretung weiß von nichts. Genau dann wird Reinigung zur internen Aufgabe.', v['problem_lead'])
    html = html.replace('Vor der Zusammenarbeit wird festgelegt, wer Ihr Objekt betreut, wie Vertretung bei Ausfall funktioniert und was bei einer Reklamation passiert. Danach starten Sie mit einer Probereinigung.', 'Vor der Zusammenarbeit wird festgelegt, wer Ihr Objekt betreut, wie Vertretung bei Ausfall funktioniert und was bei einer Reklamation passiert. Danach starten Sie mit einer Probereinigung.')
    cards = ''
    for title, items in v['cards']:
        lis = ''.join(f'<li>{item}</li>' for item in items)
        cards += card_tpl.format(title=title, lis=lis)
    ctx = dict(v)
    ctx.pop('cards', None)
    service = service_tpl.format(cards=cards, **ctx)
    html = html.replace('__SERVICE_SECTION__', service)
    a1,a2,a3 = v['angle1'], v['angle2'], v['angle3']
    html = html.replace('data-h="Büroreinigung, bei der Sie nicht nachtelefonieren müssen." data-t="Weniger Nachtelefonieren" data-c="Wenn jede Meldung eine zweite und dritte Nachfrage braucht, ist die Reinigung nicht entlastend genug organisiert."', f'data-h="{a1[0]}" data-t="{a1[1]}" data-c="{a1[2]}"')
    html = html.replace('>Weniger Nachtelefonieren</button>', f'>{a1[1]}</button>')
    html = html.replace('data-h="Ein fester Ansprechpartner für Ihr Büro in Wien." data-t="Klare Zuständigkeit" data-c="Ein fester Ansprechpartner ist oft der Unterschied zwischen gemeldeter Beschwerde und gelöstem Thema."', f'data-h="{a2[0]}" data-t="{a2[1]}" data-c="{a2[2]}"')
    html = html.replace('>Fixe Zuständigkeit</button>', f'>{a2[1]}</button>')
    html = html.replace('data-h="Büroreinigung, die nicht wieder im Office hängen bleibt." data-t="Intern entlasten" data-c="Wenn Reinigung ständig im Team besprochen wird, braucht es einen Ablauf, bei dem ÖFS die Verantwortung übernimmt."', f'data-h="{a3[0]}" data-t="{a3[1]}" data-c="{a3[2]}"')
    html = html.replace('>Intern entlasten</button>', f'>{a3[1]}</button>')
    html = html.replace('Weniger Nachtelefonieren</h2><p id="angle-copy">Wenn jede Meldung eine zweite und dritte Nachfrage braucht, ist die Reinigung nicht entlastend genug organisiert.', f'{a1[1]}</h2><p id="angle-copy">{a1[2]}')
    # replace remaining city specifics from Wien in labels
    html = html.replace('in Wien', 'in Linz').replace('Wien.', 'Linz.').replace('Wien?', 'Linz?')
    html = html.replace('src="assets/', 'src="../assets/')
    outdir = root / slug
    outdir.mkdir(exist_ok=True)
    (outdir / 'index.html').write_text(html)

# Variant overview page
links = '\n'.join(f'<li><a href="{slug}/">{v["title"]}</a><span>{v["description"]}</span></li>' for slug,v in variants.items())
overview = f'''<!doctype html><html lang="de"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1"><meta name="robots" content="noindex,nofollow"><title>ÖFS Intent-Previews Linz</title><style>body{{font-family:-apple-system,BlinkMacSystemFont,"Segoe UI",sans-serif;margin:0;background:#f4f8ff;color:#111}}main{{max-width:900px;margin:0 auto;padding:56px 24px}}h1{{font-size:clamp(34px,7vw,64px);line-height:.96;letter-spacing:-.05em;margin:0 0 14px}}p{{color:#5d6470;font-size:18px;line-height:1.5}}ul{{list-style:none;margin:34px 0 0;padding:0;display:grid;gap:14px}}li{{background:#fff;border:1px solid rgba(0,0,0,.08);border-radius:22px;padding:20px;box-shadow:0 10px 28px rgba(0,0,0,.06)}}a{{display:block;color:#0878df;font-weight:950;font-size:21px;text-decoration:none;margin-bottom:6px}}span{{color:#555;line-height:1.45}}</style></head><body><main><h1>ÖFS Linz Intent-Previews</h1><p>Drei saubere Sub-URLs für Message-Match-Tests. Keine Live-Ads, noindex, nur Preview.</p><ul>{links}</ul></main></body></html>'''
(root / 'intent-previews.html').write_text(overview)
print('created', ', '.join(variants.keys()), 'and intent-previews.html')

import os, json, time, requests
from pathlib import Path
from datetime import datetime
from PIL import Image
from io import BytesIO

ROOT = Path(__file__).resolve().parent
ASSETS = ROOT / 'assets'
OUTDIR = ROOT / 'generated-hero-logical-carpet-2026-05-20'
OUTDIR.mkdir(exist_ok=True)

API_KEY = os.environ.get('KIE_API_KEY')
if not API_KEY:
    raise SystemExit('Missing KIE_API_KEY')

UPLOAD_URL = 'https://kieai.redpandaai.co/api/file-stream-upload'
CREATE_URL = 'https://api.kie.ai/api/v1/jobs/createTask'
STATUS_URL = 'https://api.kie.ai/api/v1/jobs/recordInfo'
HEADERS = {'Authorization': f'Bearer {API_KEY}'}

logo_path = ASSETS / 'logo-oefs-dark.webp'
with logo_path.open('rb') as fh:
    r = requests.post(
        UPLOAD_URL,
        headers=HEADERS,
        data={'uploadPath': 'images'},
        files={'file': ('logo-oefs-dark.webp', fh, 'image/webp')},
        timeout=180,
    )
r.raise_for_status()
logo_url = r.json()['data']['downloadUrl']

BASE = '''Generate a photorealistic documentary photo for an Austrian B2B office-cleaning landing page.
Use the supplied image only as the exact ÖFS logo reference if a small logo patch is visible. The logo must be subtle embroidered silvery-gray on dark navy workwear, never bright, never large.

PHYSICAL LOGIC / HARD CONSTRAINTS:
- The office floor is CARPET or carpet tiles. Therefore: absolutely no mop, no wet mop, no mop bucket, no wet floor sign, no floor scrubber with water, no puddles, no glossy wet floor.
- Cleaning action must make sense for carpeted offices: commercial vacuum cleaner, cable-managed vacuuming, dusting/wiping desks, emptying bins, restocking supplies.
- Keep the scene credible for a B2B office: used desks, ergonomic chairs, bins, cables, meeting room glass, evening/early morning light.
- No smiling model, no face looking into camera, no heroic pose, no staged handshake, no tablet presentation.
- Documentary service-photo look, ordinary European office, slightly imperfect composition, not a sterile showroom, not a stock-photo ad.
- Composition must work as right-side hero crop: main action center/right; left side can be calmer negative space for split hero layout.
- No fake readable signs, no extra logos, no distorted hands, no impossible reflections.
'''.strip()

jobs = [
    (
        'oefs-hero-logical-carpet-vacuum-openoffice.webp',
        'After-hours open-plan office in Vienna with dark gray carpet tiles. One ÖFS cleaner in dark navy workwear is vacuuming between desks using a compact commercial canister vacuum with hose and cable. Cleaning cart is partly visible in background with cloths and bin liners only, no mop equipment. Chairs slightly pulled out, bins under desks, realistic fluorescent and evening window light. Candid side/back view, face not prominent.'
    ),
    (
        'oefs-hero-logical-carpet-bin-desk-reset.webp',
        'Quiet carpeted office corridor opening into a desk area after work. One ÖFS cleaner in dark navy workwear empties desk-side paper bins into a service cart and wipes a desk edge with a microfiber cloth. Carpet tiles clearly visible, no wet cleaning tools. Used office details: monitor arms, cables, chairs, glass meeting room wall. Natural documentary angle from hallway, not posed.'
    ),
    (
        'oefs-hero-logical-carpet-detail-vacuum.webp',
        'Documentary low-to-mid angle in a carpeted office: commercial vacuum head moving along gray carpet tiles beside chair legs and desk pedestals, cleaner visible from torso/back in dark navy ÖFS workwear, service cart softly in background. Practical office-cleaning moment, realistic scale, no water, no mop, no bucket, no showroom gloss.'
    ),
]

manifest = {'created_at': datetime.now().isoformat(), 'model': 'nano-banana-2', 'logo_url': logo_url, 'jobs': []}

for name, scene in jobs:
    body = {
        'model': 'nano-banana-2',
        'input': {
            'prompt': BASE + '\n\nSCENE:\n' + scene,
            'image_input': [logo_url],
            'aspect_ratio': '16:9',
            'resolution': '2K',
            'output_format': 'png',
        },
    }
    print('submit', name, flush=True)
    rr = requests.post(CREATE_URL, headers={**HEADERS, 'Content-Type': 'application/json'}, json=body, timeout=180)
    rr.raise_for_status()
    task_id = rr.json().get('data', {}).get('taskId') or rr.json().get('taskId')
    print('task', task_id, flush=True)
    info = {}; state = None
    for i in range(90):
        time.sleep(8)
        sr = requests.get(STATUS_URL, headers=HEADERS, params={'taskId': task_id}, timeout=90)
        sr.raise_for_status()
        info = sr.json().get('data') or sr.json()
        state = info.get('state') or info.get('status')
        print(i, state, flush=True)
        if state in ('success', 'failed'):
            break
    rec = {'file': name, 'prompt': scene, 'task_id': task_id, 'state': state}
    if state == 'success':
        result = info.get('resultJson') or info.get('result') or '{}'
        if isinstance(result, str):
            result = json.loads(result)
        url = (result.get('resultUrls') or result.get('urls') or result.get('images') or [None])[0]
        data = requests.get(url, timeout=180).content
        png = OUTDIR / name.replace('.webp', '.png')
        webp = OUTDIR / name
        png.write_bytes(data)
        im = Image.open(BytesIO(data)).convert('RGB')
        im.save(webp, 'WEBP', quality=90, method=6)
        rec.update({'result_url': url, 'png': str(png), 'webp': str(webp), 'size': im.size})
        print('saved', webp, im.size, flush=True)
    else:
        rec['raw'] = info
    manifest['jobs'].append(rec)
    (OUTDIR / 'manifest.json').write_text(json.dumps(manifest, ensure_ascii=False, indent=2))
print('DONE', OUTDIR)

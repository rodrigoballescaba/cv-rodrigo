import json, subprocess, hashlib, gzip, os, sys, tempfile

PROJECT = 'cv-rodrigo-b28a1'
SITE = 'cv-rodrigo-b28a1'
HOSTING_DIR = '/home/hatch/workspace/cv/public'
TMP = tempfile.mkdtemp(prefix='hdeploy-')

def get_token():
    d = json.load(open(os.path.expanduser('~/.config/configstore/firebase-tools.json')))
    return d['tokens']['access_token']

TOKEN = get_token()

def api(method, url, data=None, timeout=60):
    cmd = ['curl', '-s', '--max-time', str(timeout), '-X', method,
           '-H', f'Authorization: Bearer {TOKEN}',
           '-H', 'Content-Type: application/json']
    if data is not None:
        cmd += ['-d', json.dumps(data)]
    cmd.append(url)
    r = subprocess.run(cmd, capture_output=True, text=True, timeout=timeout + 10)
    try:
        return json.loads(r.stdout) if r.stdout.strip() else {}
    except Exception:
        print('API RAW:', r.stdout[:500], r.stderr[:500], flush=True)
        return {}

CONFIG = {
    "cleanUrls": True,
    "redirects": [
        {"glob": "/images/CV-Rodrigo.pdf", "location": "/cv/rodrigo-ballesteros-cv.pdf", "statusCode": 301}
    ],
    "headers": [
        {"glob": "**/*.html", "headers": {"Cache-Control": "no-cache"}},
        {"glob": "**/*.@(jpg|png|svg|webp|ico|pdf)", "headers": {"Cache-Control": "public, max-age=604800"}},
        {"glob": "**/*.@(css|js)", "headers": {"Cache-Control": "public, max-age=3600"}},
    ],
}

# 1. Create version
v = api('POST',
        f'https://firebasehosting.googleapis.com/v1beta1/projects/{PROJECT}/sites/{SITE}/versions',
        {'config': CONFIG})
VERSION = v.get('name', '')
if not VERSION:
    print('VERSION CREATE FAILED:', v, flush=True)
    sys.exit(1)
print('version:', VERSION, flush=True)

# 2. Hash gzipped contents
files = {}
gzipped = {}
for root, dirs, filenames in os.walk(HOSTING_DIR):
    dirs[:] = [d for d in dirs if not d.startswith('.')]
    for fn in filenames:
        if fn.startswith('.'):
            continue
        full = os.path.join(root, fn)
        rel = '/' + os.path.relpath(full, HOSTING_DIR)
        with open(full, 'rb') as fh:
            gz = gzip.compress(fh.read(), compresslevel=9)
        h = hashlib.sha256(gz).hexdigest()
        files[rel] = h
        gzipped[h] = gz
print('files:', len(files), flush=True)

# 3. populateFiles
pop = api('POST', f'https://firebasehosting.googleapis.com/v1beta1/{VERSION}:populateFiles',
          {'files': files})
upload_url = pop.get('uploadUrl', '')
need = pop.get('uploadRequiredHashes', [])
if not upload_url:
    print('POPULATE FAILED:', pop, flush=True)
    sys.exit(1)
print('to upload:', len(need), flush=True)

# 4. Upload each required hash with curl --data-binary (urllib dies on the proxy)
for h in need:
    p = os.path.join(TMP, h + '.gz')
    with open(p, 'wb') as fh:
        fh.write(gzipped[h])
    for attempt in range(4):
        r = subprocess.run(['curl', '-s', '--max-time', '120', '-X', 'POST',
                            '-H', f'Authorization: Bearer {TOKEN}',
                            '-H', 'Content-Type: application/octet-stream',
                            '--data-binary', '@' + p,
                            upload_url + '/' + h],
                           capture_output=True, text=True, timeout=140)
        if r.returncode == 0:
            break
        print(f'retry {attempt+1} for {h[:12]}', flush=True)
    else:
        print('UPLOAD FAILED:', h, r.stdout[:200], r.stderr[:200], flush=True)
        sys.exit(1)
print('uploads done', flush=True)

# 5. Finalize version
fin = api('PATCH', f'https://firebasehosting.googleapis.com/v1beta1/{VERSION}?updateMask=status',
          {'status': 'FINALIZED'})
print('finalize:', fin.get('status'), flush=True)

# 6. Create release (versionName as full resource name in query param, empty json body)
rel = api('POST',
          f'https://firebasehosting.googleapis.com/v1beta1/projects/{PROJECT}/sites/{SITE}/releases?versionName={VERSION}',
          {})
print('release:', rel.get('name', rel), flush=True)
print('DEPLOY OK')

"""Verify and unpack this portable multipart snapshot with Python 3 stdlib."""
import hashlib,json,pathlib,zipfile
root=pathlib.Path(__file__).resolve().parent
info=json.loads((root/'parts.json').read_text(encoding='utf-8'))
target=root/info['archive_name']
whole=hashlib.sha256()
if not target.exists():
    temporary=target.with_suffix('.partial.zip')
    with temporary.open('wb') as out:
        for part in info['parts']:
            path=root/part['name']; data=path.read_bytes()
            if len(data)!=part['bytes'] or hashlib.sha256(data).hexdigest()!=part['sha256']:
                raise SystemExit('Missing/corrupt part: '+part['name'])
            whole.update(data);out.write(data)
    if whole.hexdigest()!=info['archive_sha256']:
        raise SystemExit('Archive hash mismatch')
    temporary.replace(target)
else:
    with target.open('rb') as stream:
        for block in iter(lambda:stream.read(1024*1024),b''):whole.update(block)
    if whole.hexdigest()!=info['archive_sha256']:raise SystemExit('Existing archive hash mismatch')
destination=root/'reading'
if destination.exists():
    raise SystemExit('reading/ already exists; preserve its outputs. Choose a new extraction directory.')
with zipfile.ZipFile(target) as z:
    for member in z.namelist():
        p=pathlib.PurePosixPath(member)
        if p.is_absolute() or '..' in p.parts or ':' in p.parts[0]:raise SystemExit('Unsafe archive path')
    z.extractall(destination)
print('Ready:',destination, 'Books:', info['selected_books'])

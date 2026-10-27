#!/usr/bin/env python3
"""Verify retained FM/music descriptors and physical references. Offline only."""
from pathlib import Path
import hashlib
import json
from firmware_disassembly import disassemble_arm

ROOT = Path(__file__).resolve().parents[1]
sha = lambda b: hashlib.sha256(b).hexdigest()
source = ROOT / 'nokia-ta1278-research/firmware/original/system-20261025T054301+0800/user.bin'
b = source.read_bytes()
expected = '8f0db2dc82f9e763cb700c2e5781b7ca7125a4d250f4c075dbec793eb549c1ca'
assert sha(b) == expected
wanted = {'FM_OPTION_WIN_ID': '0x88591653', 'MMIMP3_LOAD_WAIT_WIN_ID': '0x88ad6ea5'}
windows = [r for r in json.loads((ROOT / 'nokia-ta1278-research/analysis/ui/window-semantics.json').read_text())['windows'] if r.get('name') in wanted]
assert len(windows) == len(wanted)
for r in windows:
    off = int(r['offset'], 16)
    assert sha(b[off:off + r['size']]) == r['sha256']
    assert r['handler_thumb'] == wanted[r['name']]
fm = next(r for r in windows if r['name'] == 'FM_OPTION_WIN_ID')
keys = next(a for a in fm['attributes'] if a.get('framework_opcode') == 'MMK_CREATE_SOFTKEY')
assert keys['named_arguments']['_LEFT_SOFT_ID_'] == '0x0'
assert keys['named_arguments']['_MID_SOFT_ID_'] == '0x40000a1f'
folder = ROOT / 'docs/handset-samples/20261025'
index = json.loads((folder / 'index.json').read_text())
names = ['radio-options', 'radio-close-option', 'music-root-empty-selection', 'music-options', 'music-refresh', 'stopwatch-root', 'stopwatch-running', 'stopwatch-lap', 'stopwatch-stopped', 'stopwatch-reset', 'contacts-options', 'test-contact-options', 'calendar-options', 'system-settings', 'personalization']
samples = [s for s in index['samples'] if s['name'] in names]
assert len(samples) == len(names)
for s in samples:
    assert sha((folder / s['png']).read_bytes()) == s['png_sha256']
ranges = [(0x88591652, 0x88591700), (0x88ad6ea4, 0x88ad6fe8)]
out = ROOT / 'docs/evidence'
(out / 'app-page-handlers-thumb.txt').write_text(disassemble_arm(b, 0x88000000, ranges))
report = {'source': str(source.relative_to(ROOT)), 'source_sha256': expected, 'windows': windows,
          'samples': samples, 'ranges': [{'start': hex(a), 'end': hex(z), 'sha256': sha(b[a-0x88000000:z-0x88000000])} for a,z in ranges],
          'confirmed': ['Separate FM option and music load-wait windows, descriptor bytes and handler addresses.', 'FM menu left softkey is empty and center is Select.', 'Retained screenshots show dimmed parent pages under FM/music options; music refresh has a waiting caption instead of the library.'],
          'limits': ['Descriptor presence is not a full handler reconstruction.', 'The FM speaker row is grey in these captures; the native hardware predicate is not recovered. Replica has no FM backend and leaves it disabled.', 'Music scan input gating, background completion and the generated dot animation are local implementation policies.', 'Stopwatch screenshots cover one lap only; no maximum, multiple-lap ordering or scrolling claim is made.']}
(out / 'app-page-evidence.json').write_text(json.dumps(report, indent=2, ensure_ascii=False)+'\n')
print('Verified two native window descriptors and 15 retained screenshot hashes; no device access.')

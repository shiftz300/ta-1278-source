#!/usr/bin/env python3
"""Verify the recovered binary percentage operator; no native execution."""
from pathlib import Path
import hashlib, json, struct
from firmware_disassembly import disassemble_arm
root=Path(__file__).resolve().parents[1]
source=root/'nokia-ta1278-research/firmware/original/system-20261025T054301+0800/user.bin'
b=source.read_bytes(); sha=lambda x:hashlib.sha256(x).hexdigest()
assert sha(b)=='8f0db2dc82f9e763cb700c2e5781b7ca7125a4d250f4c075dbec793eb549c1ca'
assert struct.unpack_from('<d',b,0xb90bf4)[0]==100.
checks={0xb911c0:'2520',0xb909f4:'2528',0xb909f6:'3cd0',0xb90a98:'29ee011b',0xb90a9c:'81ee008b'}
for offset,raw in checks.items(): assert b[offset:offset+len(raw)//2].hex()==raw
ranges=[(0x88b90932,0x88b90aba),(0x88b90be4,0x88b90c1c),(0x88b91134,0x88b911d4)]
(root/'docs/evidence/calculator-percent-thumb.txt').write_text(disassemble_arm(b,0x88000000,ranges))
r={'source':str(source.relative_to(root)),'source_sha256':sha(b),'operator':'%','operator_assignment':'0x88b911c0','dispatch':'0x88b909f4 -> 0x88b90a72','multiplier_address':'0x88b90bf4','multiplier':100.,'formula':'lhs * 100.0 / rhs','instructions':['0x88b90a98 vmul.f64 d1,d9,d1','0x88b90a9c vdiv.f64 d8,d1,d0'],'checked_bytes':{hex(k+0x88000000):v for k,v in checks.items()},'ranges':[{'start':hex(a),'end':hex(z),'sha256':sha(b[a-0x88000000:z-0x88000000])} for a,z in ranges],'limits':['Static arithmetic/operator recovery, not a physical percentage test.','Full calculator state-machine, repeated equals, formatting and tiny-denominator thresholds are not reconstructed.']}
(root/'docs/evidence/calculator-percent.json').write_text(json.dumps(r,indent=2)+'\n')
print('Percent operator and multiplication/division instructions verified.')

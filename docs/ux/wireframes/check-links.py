#!/usr/bin/env python3
"""Validate local wireframe links and reject links to the current screen."""
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urldefrag
import sys

ROOT = Path(__file__).parent
class Links(HTMLParser):
    def __init__(self): super().__init__(); self.hrefs=[]; self.screen=None; self.nav=False
    def handle_starttag(self, tag, attrs):
        a=dict(attrs)
        if tag=='article' and 'screen' in a.get('class','').split(): self.screen=a.get('id')
        if tag in ('div','nav') and 'nav' in a.get('class','').split(): self.nav=True
        if tag=='a' and 'href' in a: self.hrefs.append((a['href'],self.screen,self.nav))
    def handle_endtag(self, tag):
        if tag in ('div','nav') and self.nav: self.nav=False
        if tag=='article': self.screen=None
errors=[]
for source in sorted(ROOT.glob('*.html')):
    parser=Links(); parser.feed(source.read_text())
    for href,screen,in_nav in parser.hrefs:
        if href.startswith(('http:','https:','mailto:')): continue
        filepart,anchor=urldefrag(href)
        target=ROOT/filepart if filepart else source
        if not target.is_file(): errors.append(f'{source.name}: missing file {href}'); continue
        if anchor:
            ids=set(__import__('re').findall(r'id="([^"]+)"',target.read_text()))
            if anchor not in ids: errors.append(f'{source.name}: missing anchor {href}')
            if target==source and anchor==screen and not in_nav: errors.append(f'{source.name}: self-link {href}')
if errors:
    print('\n'.join(errors)); sys.exit(1)
print(f'OK: checked {sum(1 for _ in ROOT.glob("*.html"))} HTML files; all local links and anchors are valid.')

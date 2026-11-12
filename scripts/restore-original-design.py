from pathlib import Path
import re,json,hashlib,html,urllib.parse,sys
mobile="--mobile" in sys.argv
root=Path(__file__).resolve().parent.parent;out=root/('public/original-mobile' if mobile else 'public/original');out.mkdir(exist_ok=True);styles=root/'public/original/styles';styles.mkdir(exist_ok=True)
assets=json.loads((root/'public/asset-map.json').read_text());downloads={p.name:'/downloads/'+p.name for p in (root/'public/downloads').iterdir()};routes={}
def attrs(tag):return dict(re.findall(r'([\w:-]+)=["\']([^"\']*)["\']',tag))
for f in (root/('research-mobile' if mobile else 'research')).glob('*.html'):
 source=f.read_text();canonical=re.search(r'<link[^>]*rel="canonical"[^>]*href="([^"]+)"',source)
 if not canonical:continue
 path=urllib.parse.urlparse(html.unescape(canonical[1])).path.rstrip('/') or '/'
 if path in routes:continue
 # Keep the original presentation, remove Wix executable code, telemetry and runtime data.
 source=re.sub(r'<script\b[^>]*>.*?</script>','',source,flags=re.S|re.I)
 source=re.sub(r'<!--.*?-->','',source,flags=re.S)
 source=re.sub(r'<link\b[^>]*(?:rel="(?:prefetch|preload|alternate|canonical)"|as="fetch")[^>]*>','',source)
 def css(m):
  content=m[2];name=hashlib.sha256(content.encode()).hexdigest()[:20]+'.css';(styles/name).write_text(content)
  return '<link rel="stylesheet" href="/original/styles/'+name+'">'
 source=re.sub(r'<style([^>]*)>(.*?)</style>',css,source,flags=re.S|re.I)
 def image(m):
  tag=m[0];a=attrs(tag);u=html.unescape(a.get('src',''));base=u.split('/v1/')[0];local=assets.get(base)
  if local and local.startswith('/'):
   tag=re.sub(r'\bsrc="[^"]*"','src="'+local+'"',tag);tag=re.sub(r'\s+(?:srcset|sizes)="[^"]*"','',tag)
  elif '/v1/' in u and 'static.wixstatic.com/media/' in u:
   tag=re.sub(r'\bsrc="[^"]*"','src="'+html.escape(base,quote=True)+'"',tag);tag=re.sub(r'\s+(?:srcset|sizes)="[^"]*"','',tag)
  return tag
 source=re.sub(r'<img\b[^>]*>',image,source)
 def anchor(m):
  tag=m[0];a=attrs(tag);href=html.unescape(a.get('href',''))
  if href.startswith('https://www.pi-education.com') or href.startswith('https://pi-education.com'):
   p=urllib.parse.urlparse(href);href=p.path or '/'
   if '/_files/' in href:href=downloads.get(href.rsplit('/',1)[-1],href)
   href+=('#'+p.fragment if p.fragment else '')
  if href.startswith('./#'):href=href[2:]
  tag=re.sub(r'\bhref="[^"]*"','href="'+html.escape(href,quote=True)+'"',tag)
  if href.startswith('/'):tag=re.sub(r'\s+target="[^"]*"','',tag)
  return tag
 source=re.sub(r'<a\b[^>]*>',anchor,source)
 source=re.sub(r'\s+on(?:click|load|error|submit)=["\'][^"\']*["\']','',source,flags=re.I)
 source=source.replace('</head>','<link rel="stylesheet" href="/original-adapter.css"><script defer src="/original-adapter.js"></script></head>')
 source=re.sub(r'\n\s*\n','\n',source)
 name=hashlib.sha256(path.encode()).hexdigest()[:20]+'.html';(out/name).write_text(source);routes[path]=('/original-mobile/' if mobile else '/original/')+name
(root/('app/original-mobile-routes.json' if mobile else 'app/original-routes.json')).write_text(json.dumps(routes,indent=2));print('Restored',len(routes),'original page layouts;',len(list(styles.iterdir())),'deduplicated stylesheets')

from pathlib import Path
import re,json
r=Path(__file__).resolve().parent.parent
import sys
mobile='--mobile' in sys.argv
source=(r/'public'/('original-mobile' if mobile else 'original')/Path(json.loads((r/('app/original-mobile-routes.json' if mobile else 'app/original-routes.json')).read_text())['/']).name).read_text()
old=(r/'shell.html').read_text();body=re.search(r'<body[^>]*>(.*)</body>',old,re.S)[1]
source=re.sub(r'<main\b[^>]*>.*?</main>','<main id="PAGES_CONTAINER"><div class="pi-native">'+body+'</div></main>',source,flags=re.S,count=1)
source=source.replace('</head>','<link rel="stylesheet" href="/native-style.css"><link rel="stylesheet" href="/member-experience.css"><script defer src="/member-experience.js"></script><script defer src="/app.js"></script><script defer src="/features.js"></script></head>')
source=source.replace('id="SITE_FOOTER"','id="SITE_FOOTER"')
(r/('app/shell-mobile.ts' if mobile else 'app/shell.ts')).write_text('export default '+json.dumps(source)+';\n')
css=(r/'public/style.css').read_text();css=re.sub(r'@import[^;]+;','',css)
(r/'public/native-style.css').write_text('@scope (.pi-native){'+css+'}\n.pi-native{--green:#00ad69;--dark:#333;--cream:#fff;--muted:#555;--yellow:#ddd}.pi-native>.topbar,.pi-native>header,.pi-native>footer,.pi-native>.chat{display:none!important}.pi-native{max-width:1100px;padding:25px 30px;box-sizing:border-box}.pi-native .pagehead{background:white;padding:30px 0}.pi-native h1,.pi-native h2{color:#00ad69;font-weight:400;letter-spacing:0}.pi-native .button,.pi-native .native-form,.pi-native .sidebox,.pi-native input,.pi-native textarea,.pi-native select{border-radius:0}.pi-native .native-form,.pi-native .sidebox{background:white}.pi-native .wrap{padding:25px 0}.pi-native .breadcrumb{display:none}.pi-native #search{display:none}')

import sys, os, re, glob, statistics
from html.parser import HTMLParser
import tiktoken, markdown
enc = tiktoken.get_encoding("o200k_base")
T = lambda s: len(enc.encode(s))

class Split(HTMLParser):
    def __init__(s):
        super().__init__(convert_charrefs=True); s.stack=[]; s.text=[]; s.md=[]
    def handle_starttag(s, tag, a):
        s.stack.append(tag)
        if tag in ("h1","h2","h3","h4","h5","h6"): s.md.append("\n"+"#"*int(tag[1])+" ")
        elif tag=="li": s.md.append("\n- ")
        elif tag in ("p","div","section","tr","br","pre"): s.md.append("\n")
        elif tag in ("td","th"): s.md.append(" | ")
        elif tag=="code": s.md.append("`")
    def handle_endtag(s, tag):
        if tag=="code": s.md.append("`")
        while s.stack and s.stack.pop()!=tag: pass
    def handle_data(s, d):
        if any(t in ("script","style","svg") for t in s.stack): return
        s.text.append(d); s.md.append(d)

def blocks(html, tag):
    return "".join(re.findall(rf"<{tag}\b.*?</{tag}>", html, flags=re.S|re.I))

def analyze(path):
    h = open(path, encoding="utf-8", errors="replace").read()
    p = Split(); p.feed(h)
    text = re.sub(r"[ \t]+"," ", "".join(p.text)); text = re.sub(r"\n\s*\n+","\n\n", text).strip()
    md = re.sub(r"[ \t]+"," ", "".join(p.md)); md = re.sub(r"\n\s*\n+","\n\n", md).strip()
    return dict(name=os.path.basename(path), html=T(h), style=T(blocks(h,"style")), script=T(blocks(h,"script")), svg=T(blocks(h,"svg")), text=T(text), mdish=T(md))

rows=[analyze(f) for f in sorted(glob.glob(os.path.join(sys.argv[1],"*.html"))) if not f.endswith("index.html")]
def show(rs, label):
    print(f"\n== {label} (n={len(rs)}) ==")
    print(f"{'file':42} {'html':>6} {'style':>6} {'script':>6} {'svg':>6} {'text':>6} {'md~':>6} {'html/md~':>8}")
    for r in rs:
        print(f"{r['name'][:42]:42} {r['html']:6} {r['style']:6} {r['script']:6} {r['svg']:6} {r['text']:6} {r['mdish']:6} {r['html']/r['mdish']:8.2f}")
    ratios=[r['html']/r['mdish'] for r in rs]
    tot=lambda k: sum(r[k] for r in rs)
    print(f"median html/md~ = {statistics.median(ratios):.2f}, min {min(ratios):.2f}, max {max(ratios):.2f}")
    print(f"share of html tokens: style {tot('style')/tot('html'):.0%}, script {tot('script')/tot('html'):.0%}, svg {tot('svg')/tot('html'):.0%}, visible text {tot('text')/tot('html'):.0%}")
main=[r for r in rows if not r['name'].startswith('unknowns')]
unk=[r for r in rows if r['name'].startswith('unknowns')]
show(main,"main examples 01-20"); show(unk,"unknowns examples")

# our guideline: md vs bare html conversion
g=open(sys.argv[2],encoding="utf-8").read()
bare=markdown.markdown(g, extensions=["tables"])
print(f"\n== guideline file ==\nmd {T(g)} tokens, bare HTML (python-markdown, no CSS) {T(bare)} tokens, ratio {T(bare)/T(g):.2f}")

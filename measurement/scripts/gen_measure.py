import sys, os, re, glob
import tiktoken
enc = tiktoken.get_encoding("o200k_base"); T=lambda s: len(enc.encode(s))
d=sys.argv[1]
def blocks(h,tag): return "".join(re.findall(rf"<{tag}\b.*?</{tag}>", h, flags=re.S|re.I))
for f in sorted(glob.glob(os.path.join(d,"*_*.*"))):
    s=open(f,encoding="utf-8").read()
    extra=""
    if f.endswith(".html"):
        st,sc=T(blocks(s,"style")),T(blocks(s,"script"))
        stripped=re.sub(r"<(style|script)\b.*?</\1>","",s,flags=re.S|re.I)
        extra=f" style {st} script {sc} stripped {T(stripped)}"
    print(f"{os.path.basename(f):14} chars {len(s):6} o200k {T(s):6}{extra}")

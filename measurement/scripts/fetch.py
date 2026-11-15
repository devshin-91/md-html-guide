import json, sys, urllib.request, os
out = sys.argv[1]
def get(u):
    req = urllib.request.Request(u, headers={"User-Agent": "token-measure-script"})
    return urllib.request.urlopen(req, timeout=30).read()
tree = json.loads(get("https://api.github.com/repos/thariqs/html-effectiveness/git/trees/HEAD?recursive=1"))
files = [t["path"] for t in tree["tree"] if t["type"]=="blob" and t["path"].endswith(".html")]
print(len(files), "html files")
for p in files:
    data = get("https://raw.githubusercontent.com/thariqs/html-effectiveness/HEAD/" + p)
    name = p.replace("/", "__")
    open(os.path.join(out, name), "wb").write(data)
    print(p, len(data))

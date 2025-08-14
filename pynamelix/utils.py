# app.py
import uuid, random
from flask import Flask, request, jsonify, Response
from namelix_wrapper import try_namelix  # ім'я файлу з кодом вище

app = Flask(__name__)

def local_generate(keyword: str, n: int = 20):
    base = (keyword or "").strip()
    if not base: return []
    prefixes = ["neo","meta","uni","omni","hyper","alpha","brand","bright","nova","prime","quant","zen"]
    suffixes = ["ly","ify","io","ster","scape","verse","labs","works","hub","forge","pilot","spark"]
    ideas=set()
    while len(ideas)<n:
        mode=random.choice(["prefix","suffix","mix"])
        if mode=="prefix": ideas.add((random.choice(prefixes)+base).title())
        elif mode=="suffix": ideas.add((base+random.choice(suffixes)).title())
        else:
            half=max(2,len(base)//2); ideas.add((base[:half]+random.choice(suffixes)).title())
    return sorted(ideas)

HTML = """<!doctype html>
<meta charset="utf-8"><title>Namelix</title>
<form id="f"><input id="kw" placeholder="Enter keywords" required>
<button>Generate</button></form><div id="out"></div>
<script>
document.getElementById("f").addEventListener("submit", async (e)=>{
  e.preventDefault();
  const kw=document.getElementById("kw").value.trim();
  const r=await fetch("/generate",{method:"POST",headers:{"Content-Type":"application/json"},
    body:JSON.stringify({keywords:kw})});
  const data=await r.json();
  const list=data.items||[];
  document.getElementById("out").innerHTML = list.length
    ? "<ul>"+list.map(n=>`<li>${n}</li>`).join("")+"</ul>"
    : `<span style="color:#c00">${data.error||'No results'}</span>`;
});
</script>
"""

@app.get("/")
def home():
    return Response(HTML, mimetype="text/html")

@app.post("/generate")
def generate():
    body = request.get_json(silent=True) or {}
    kw = (body.get("keywords") or "").strip()
    if not kw:
        return jsonify({"error":"No keywords provided"}), 400

    # 1: згенеруємо request_id як у фронті
    req_id = str(uuid.uuid4())

    # 2: виклик Namelix з полями з вашого дампу
    names, err = try_namelix(
        keyword=kw,
        request_id=req_id,
        description="",
        blacklist="",
        max_length=25,
        style="default",
        random_level="low",
        extensions=["com"],
        require_domains=True,
        prev_names="",
        saved="",
        premium_index=0,
        page=0,
        num=5,
        seed=123407637,
    )

    if names:
        return jsonify({"items": names})
    # fallback
    app.logger.warning("[namelix] %s", err)
    return jsonify({"items": local_generate(kw), "error": err or "fallback"}), 200

if __name__ == "__main__":
    # Переконайтеся, що NAMELIX_COOKIE передано в середовищі, інакше може бути 'error'
    # NAMELIX_COOKIE="_ga=...; _gid=...; _ga_8FEY..." python app.py
    app.run(host="127.0.0.1", port=5000, debug=True)

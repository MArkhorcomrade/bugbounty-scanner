import requests, yaml, json
from datetime import datetime

with open("programs.yaml") as f:
    programs = yaml.safe_load(f)["programs"]

results = []
for p in programs:
    try:
        r = requests.get(p["url"], timeout=10)
        results.append({
            "name": p["name"],
            "url": p["url"],
            "status": r.status_code,
            "content_snippet": r.text[:200]  # first 200 chars
        })
    except Exception as e:
        results.append({
            "name": p["name"],
            "url": p["url"],
            "error": str(e)
        })

with open("results.json", "w") as f:
    json.dump({
        "last_run": datetime.utcnow().isoformat(),
        "results": results
    }, f, indent=2)

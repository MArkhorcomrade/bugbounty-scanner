import requests, yaml, json
from datetime import datetime

with open("programs.yaml") as f:
    data = yaml.safe_load(f)

programs = data.get("programs", [])
dorks = data.get("dorks", [])

results = []

# Scan program URLs
for p in programs:
    try:
        r = requests.get(p["url"], timeout=10)
        results.append({
            "name": p["name"],
            "url": p["url"],
            "status": r.status_code,
            "content_snippet": r.text[:200]
        })
    except Exception as e:
        results.append({
            "name": p["name"],
            "url": p["url"],
            "error": str(e)
        })

# Save results (with dorks included for reference)
with open("results.json", "w") as f:
    json.dump({
        "last_run": datetime.utcnow().isoformat(),
        "results": results,
        "dorks": dorks
    }, f, indent=2)

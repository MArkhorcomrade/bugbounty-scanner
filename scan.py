import yaml
import requests

with open("programs.yaml", "r") as f:
    config = yaml.safe_load(f)

programs = config["programs"]
dorks = config["dorks"]

results = []

# Scan URLs from programs
for p in programs:
    try:
        r = requests.get(p["url"], timeout=10)
        results.append({"program": p["name"], "url": p["url"], "status": r.status_code})
    except Exception as e:
        results.append({"program": p["name"], "url": p["url"], "status": str(e)})

# Add dorks to results (not executed, just listed for now)
for d in dorks:
    results.append({"program": "DORK", "url": d, "status": "SEARCH_ONLY"})

# Save results
with open("output.md", "w") as f:
    f.write("# Bug Bounty Scanner Results\n\n")
    for r in results:
        f.write(f"- **{r['program']}** → {r['url']} → `{r['status']}`\n")

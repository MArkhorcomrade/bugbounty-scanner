import yaml
import requests

# Load YAML config
with open("programs.yaml", "r") as f:
    config = yaml.safe_load(f)

# Only get dorks now
dorks = config.get("dorks", [])

results = []

# Add dorks to results (SEARCH_ONLY for now)
for d in dorks:
    results.append({"program": "DORK", "url": d, "status": "SEARCH_ONLY"})

# Save results
with open("output.md", "w") as f:
    f.write("# Bug Bounty Scanner Results\n\n")
    for r in results:
        f.write(f"- **{r['program']}** → {r['url']} → `{r['status']}`\n")

from googlesearch import search

# Input and output files
input_file = "output.md"
output_file = "dork_results.txt"

# Read the file and extract lines with SEARCH_ONLY
with open(input_file, "r", encoding="utf-8") as f:
    lines = f.readlines()

dorks = []
for line in lines:
    if "`SEARCH_ONLY`" in line:
        # Extract the dork between → and `SEARCH_ONLY`
        parts = line.split("→")
        if len(parts) >= 2:
            dork = parts[1].replace("`SEARCH_ONLY`", "").strip()
            dorks.append(dork)

# Open the output file
with open(output_file, "w", encoding="utf-8") as out:
    for dork in dorks:
        out.write(f"Dork: {dork}\n")
        try:
            # Search Google for each dork, limit to first 5 results
            for url in search(dork, num_results=5):
                out.write(f"  {url}\n")
        except Exception as e:
            out.write(f"  Error: {e}\n")
        out.write("\n")

print(f"Finished! Results saved in {output_file}")

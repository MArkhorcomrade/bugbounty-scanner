from googlesearch import search

# List of your dorks (example subset, you can paste all)
dorks = [
    'inurl:/bug-bounty site:.com',
    'inurl:/responsible-disclosure site:.com',
    'inurl:/vulnerability-disclosure site:.com',
    'filetype:txt "security contact" site:.com',
    '"bug bounty" site:.gov',
    '"vulnerability disclosure" intitle:security site:.org'
]

# Number of results per dork
num_results = 5

output_file = 'dork_results.txt'

with open(output_file, 'w') as f:
    for dork in dorks:
        f.write(f"\nDORK: {dork}\n")
        f.write("="*50 + "\n")
        try:
            results = search(dork, num_results=num_results, lang='en')
            for url in results:
                f.write(url + "\n")
        except Exception as e:
            f.write(f"Error searching {dork}: {e}\n")
        f.write("\n")

print(f"Search complete! Results saved in {output_file}")

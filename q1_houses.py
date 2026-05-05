import requests

BASE_URL = "https://anapioficeandfire.com/api/houses"
all_houses = []

# Paginate through ALL pages
url = f"{BASE_URL}?pageSize=50"
while url:
    response = requests.get(url)
    data = response.json()
    all_houses.extend(data)
    
    # Get next page from Link header
    link_header = response.headers.get("Link", "")
    next_url = None
    for part in link_header.split(","):
        if 'rel="next"' in part:
            next_url = part.split(";")[0].strip().strip("<>")
    url = next_url

# Sort alphabetically by house name
all_houses.sort(key=lambda x: x["name"])

# Write to text file
with open("houses.txt", "w", encoding="utf-8") as f:
    f.write(f"{'House Name':<60} {'Region'}\n")
    f.write("-" * 100 + "\n")
    for house in all_houses:
        name = house.get("name", "Unknown")
        region = house.get("region", "Unknown")
        f.write(f"{name:<60} {region}\n")

print(f" Done! {len(all_houses)} houses saved to houses.txt")
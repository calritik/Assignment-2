# q3_characters.py
import requests
import openpyxl 

BASE_URL = "https://anapioficeandfire.com/api/characters"
all_characters = []

url = f"{BASE_URL}?pageSize=50"
page = 1
while url:
    print(f"Fetching page {page}...")
    response = requests.get(url)
    data = response.json()
    all_characters.extend(data)
    page += 1
    
    link_header = response.headers.get("Link", "")
    url = None
    for part in link_header.split(","):
        if 'rel="next"' in part:
            url = part.split(";")[0].strip().strip("<>")

# Count seasons per character
processed = []
for char in all_characters:
    name = char.get("name") or ", ".join(char.get("aliases", ["Unknown"]))
    tv_series = char.get("tvSeries", [])
    # Filter out empty strings
    seasons = [s for s in tv_series if s.strip()]
    season_count = len(seasons)
    seasons_list = ", ".join(seasons) if seasons else "None"
    processed.append({
        "name": name,
        "season_count": season_count,
        "seasons": seasons_list,
        "gender": char.get("gender", ""),
        "culture": char.get("culture", "")
    })

# Sort by number of season appearances (descending)
processed.sort(key=lambda x: x["season_count"], reverse=True)

#Save to Excel
wb = openpyxl.Workbook()
ws = wb.active
ws.title = "Characters"

# Header row
headers = ["Name", "Season Count", "Seasons Appeared", "Gender", "Culture"]
ws.append(headers)

# Bold the header
from openpyxl.styles import Font
for cell in ws[1]:
    cell.font = Font(bold=True)

# Data rows
for char in processed:
    ws.append([
        char["name"],
        char["season_count"],
        char["seasons"],
        char["gender"],
        char["culture"]
    ])

# Auto-size columns
for col in ws.columns:
    max_len = max(len(str(cell.value or "")) for cell in col)
    ws.column_dimensions[col[0].column_letter].width = min(max_len + 2, 50)

wb.save("characters.xlsx")
print(f" Done! {len(processed)} characters saved to characters.xlsx")
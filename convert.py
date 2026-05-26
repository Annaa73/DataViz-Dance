import openpyxl
import json

# Load your Excel file
wb = openpyxl.load_workbook("data/dance_data.xlsx", read_only=True)
ws = wb.active
rows = list(ws.iter_rows(values_only=True))
headers = rows[0]

dances = []
for row in rows[1:]:
    d = dict(zip(headers, row))
    
    # Skip rows with no dance name or bad coordinates
    if not d.get("Dance style"):
        continue
    try:
        lat = float(str(d["Latitude"]).replace("−", "-").replace("\u2212", "-"))
        lon = float(str(d["Longitude"]).replace("−", "-").replace("\u2212", "-"))
    except:
        continue

    dances.append({
        "name":            str(d.get("Dance style") or "").strip(),
        "type":            str(d.get("Dance Type") or "").strip(),
        "active":          str(d.get("Active") or "").strip().lower() == "yes",
        "lat":             round(lat, 4),
        "lon":             round(lon, 4),
        "origin":          str(d.get("Origin") or "").strip(),
        "era":             str(d.get("Time -origin") or "").strip(),
        "cultural":        str(d.get("Cultural Significance") or "").strip(),
        "characteristics": str(d.get("Notable Characteristics") or "").strip(),
        "instruments":     str(d.get("Instrumental") or "").strip(),
        "hardness"    : str(d.get("Hardness Ratio") or "").strip(),
        "formation":       str(d.get("Dance Formation") or "").strip(),
        "tempo":           str(d.get("Tempo (BPM)") or "").strip(),
        "practitioners":   str(d.get("Famous Practitioners") or "").strip(),
        "festivals":       str(d.get("Events and Festivals") or "").strip(),
        "modern":       str(d.get("Modern Adaptations") or "").strip(),
        "genre":           str(d.get("Associated Music Genre") or "").strip(),
        "difficulty":      str(d.get("Learning Difficulty") or "").strip(),
        "health":          str(d.get("Health Benefits") or "").strip(),
        "ageGroup":        str(d.get("Age Group") or "").strip(),
        "flourishUrl":     "",   # ← you'll fill this in later per dance
    })

# Write output
output = "const DANCES = " + json.dumps(dances, indent=2, ensure_ascii=False) + ";\n"

with open("data/dances.js", "w", encoding="utf-8") as f:
    f.write(output)

print(f"✓ Done — {len(dances)} dances written to data/dances.js")
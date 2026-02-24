import json
from pathlib import Path

DATA = Path('gares-et-stations-du-reseau-ferre-dile-de-france-par-ligne.json')

def load_stations():
    with DATA.open('r', encoding='utf-8') as f:
        stations = json.load(f)
    metroList = {}
    for s in stations:
        if s.get('mode') != 'METRO':
            continue
        name, line = s["nom_gares"], s["indice_lig"]
        metroList.setdefault(name, { "lines": [],"visited": False})
        if line not in metroList[name]["lines"]:
            metroList[name]["lines"].append(line)
    return metroList

metro = load_stations()
print(metro)
print(f"Found {len(metro)} metro stations.")
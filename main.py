import json
with open('gares-et-stations-du-reseau-ferre-dile-de-france-par-ligne.json', 'r', encoding='utf-8') as f:
    stations = json.load(f)

numEntries = 0
metroList = {}

for s in stations:
    name = s["nom_gares"]
    line = s["indice_lig"]
    if s.get('mode') == 'METRO':
        if name not in metroList:
            metroList[name] = {
                "lines": [],
                "visited": False
            }
        if line not in metroList[name]["lines"]:
            metroList[name]["lines"].append(line)
    numEntries+=1

print(metroList)
print(f"Found {len(metroList)} metros in {numEntries}")
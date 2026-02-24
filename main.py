import json
with open('gares-et-stations-du-reseau-ferre-dile-de-france-par-ligne.json', 'r', encoding='utf-8') as f:
    stations = json.load(f)

numEntries = 0
metroList = {}

for s in stations:
    numEntries+=1
    if s.get('mode') != 'METRO':
        continue
    name, line = s["nom_gares"], s["indice_lig"]
    metroList.setdefault(name, { "lines": [],"visited": False})
    if line not in metroList[name]["lines"]:
        metroList[name]["lines"].append(line)

print(metroList)
print(f"Found {len(metroList)} metros in {numEntries}")
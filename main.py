import json
with open('gares-et-stations-du-reseau-ferre-dile-de-france-par-ligne.json', 'r', encoding='utf-8') as f:
    stations = json.load(f)

numMetro = 0
numEntries = 0

for s in stations:
    if s.get('mode') == 'METRO':
        name = s.get('nom_gares')
        line = s.get('indice_lig')
        print(f"{name} is on  line {line}")
        numMetro+=1
    numEntries+=1


print(f"Found {numMetro} metros in {numEntries}")
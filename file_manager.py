import json
from pathlib import Path

DATA = Path('gares-et-stations-du-reseau-ferre-dile-de-france-par-ligne.json')
STATES = Path('visited_stations.json')

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

def load_states():
    if STATES.exists():
        with STATES.open() as f:
            return json.load(f)
    return {}

def save_state(state):
    with STATES.open('w') as f:
        json.dump(state, f, indent=2)
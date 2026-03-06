import json
from pathlib import Path
import re

DATA = Path('gares-et-stations-du-reseau-ferre-dile-de-france-par-ligne.json')
DEFAULT_STATES = Path('visited_stations.json')

def load_metro_lines():
    with DATA.open('r', encoding='utf-8') as f:
        stations = json.load(f)
    metroList = {}
    for s in stations:
        if s.get('mode') != 'METRO':
            continue
        name, line = s["nom_gares"], s["indice_lig"]
        metroList.setdefault(name, { "lines": []})
        if line not in metroList[name]["lines"]:
            metroList[name]["lines"].append(line)
    
    orderedList = {}
    for name, data in metroList.items():
        for line in data['lines']:
            orderedList .setdefault(line, []).append(name)
            
    return dict(sorted(orderedList.items(), key=line_sort_key))

def line_sort_key(x):
    match = re.match(r'(\d+)(.*)', x[0])
    return (int(match.group(1)), match.group(2)) if match else (999, x[0])

def load_states(filePath=DEFAULT_STATES):
    if filePath.exists():
        with filePath.open() as f:
            content = f.read().strip()
            if not content:
                return {}
            return json.loads(content)
    return {}

def save_state(state, filePath=DEFAULT_STATES):
    with filePath.open('w') as f:
        json.dump(state, f, indent=2)
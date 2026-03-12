#service_manager.py

from file_manager import load_metro_lines, load_states, save_state
from pathlib import Path

class MetroService:
    def __init__(self, stateFile=Path("visited_stations.json")):
        self.stateFile = stateFile
        self.lines = load_metro_lines()
        self.visited = load_states(stateFile)

    def get_lines(self):
        return self.lines
    
    def visited_states(self, name):
        return self.visited.get(name, False)
    
    def toggle_visited(self, name):
        self.visited[name] = not self.visited.get(name, False)
        save_state(self.visited, self.stateFile)

    def get_line_percentages(self):
        percentages = {}
        for line, stations in self.lines.items():
            total = len(stations)
            visited_count = sum(1 for s in stations if self.visited.get(s, False))
            percentages[line] = round((visited_count / total * 100) if total > 0 else 0, 1)
        return percentages
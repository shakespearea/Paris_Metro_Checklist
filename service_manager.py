from file_manager import load_metro_lines, load_states, save_state
from pathlib import Path

class MetroService:
    def __init__(self, stateFile=Path("visited_stations.json")):
        self.stateFile = stateFile
        self.lines = load_metro_lines()
        self.visited = load_states(stateFile)

    def get_lines(self):
        return self.lines
    
    def visited_States(self, name):
        return self.visited.get(name, False)
    
    def toggle_visited(self, name):
        self.visited[name] = not self.visited.get(name, False)
        save_state(self.visited, self.stateFile)
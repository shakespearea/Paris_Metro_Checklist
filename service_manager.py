from file_manager import load_stations, load_states, save_state
from pathlib import Path

class MetroService:
    def __init__(self, stateFile=Path("visited_stations.json")):
        self.stateFile = stateFile
        self.stations = load_stations()
        try:
            states = load_states(stateFile)
            self.stations.update(states)
        except FileNotFoundError:
            pass

    def get_all(self):
        return self.stations
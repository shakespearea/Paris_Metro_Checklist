import pytest
from file_manager import load_stations, load_states, save_state

# Initialisation
@pytest.fixture
def visited():
    return {}

def test_set_sation_visited(visited):
    assert visited.get("Pasteur", False) is False
    visited["Pasteur"] = True
    assert visited["Pasteur"] is True

def test_save_and_reload(visited, tmp_path):
    temp_states = tmp_path / "temp_states.json"
    visited["Pasteur"] = True
    save_state(visited, temp_states)
    states = load_states(temp_states)
    assert states["Pasteur"] is True

def test_unsaved_change_does_not_affect_saved_state(visited, tmp_path):
    temp_states = tmp_path / "temp_states.json"
    visited["Pasteur"] = True
    save_state(visited, temp_states)
    visited["Pasteur"] = False
    states = load_states(temp_states)
    assert visited["Pasteur"] is True
    assert states["Pasteur"] is True

def test_station_appears_in_correct_lines():
    stations = load_stations()
    assert "Pasteur" in stations["6"]
    assert "Pasteur" in stations["12"]

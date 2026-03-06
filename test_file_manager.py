import pytest
from file_manager import load_metro_lines, load_states, save_state

# Initialisation
@pytest.fixture
def metroLines():
    return load_metro_lines()

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
    assert visited["Pasteur"] is False
    assert states["Pasteur"] is True

def test_load_states_missing_file(tmp_path):
    assert load_states(tmp_path / "nonexistent.json") == {}

def test_load_states_empty_file(tmp_path):
    empty = tmp_path / "empty.json"
    empty.write_text("")
    assert load_states(empty) == {}

def test_station_appears_in_correct_lines(metroLines):
    assert all("République" in metroLines[line] for line in ["3", "5", "8", "9", "11"])
    assert all("Châtelet" in metroLines[line] for line in ["1", "4", "11", "14"])
    assert all("Jaurès" in metroLines[line] for line in ["2", "5", "7b"])
    assert all("Pasteur" in metroLines[line] for line in ["6", "12"])
    assert "La Fourche" in metroLines["13"]

def test_stations_sorted(metroLines):
    keys = list(metroLines.keys())
    assert keys.index("1") < keys.index("2") < keys.index("3") < keys.index("3bis")
    assert keys.index("3bis") < keys.index("4") < keys.index("5") < keys.index("6")
    assert keys.index("6") < keys.index("7") < keys.index("7b") < keys.index("8")
    assert keys.index("8") < keys.index("9") < keys.index("10") < keys.index("11")
    assert keys.index("11") < keys.index("12") < keys.index("13") < keys.index("14")
import pytest
from file_manager import load_stations, load_states, save_state

# Initialisation
@pytest.fixture
def metro():
    return load_stations()

def test_set_sation_visited(metro):
    assert metro["Pasteur"]["visited"] is False
    metro["Pasteur"]["visited"] = True
    assert metro["Pasteur"]["visited"] is True

def test_save_and_reload(metro, tmp_path):
    temp_states = tmp_path / "temp_states.json"
    metro["Pasteur"]["visited"] = True
    save_state(metro, temp_states)
    states = load_states(temp_states)
    assert states["Pasteur"]["visited"] is True

def test_unsaved_change_does_not_affect_saved_state(metro, tmp_path):
    temp_states = tmp_path / "temp_states.json"
    metro["Pasteur"]["visited"] = True
    save_state(metro, temp_states)
    metro["Pasteur"]["visited"] = False
    states = load_states(temp_states)
    assert metro["Pasteur"]["visited"] is False
    assert states["Pasteur"]["visited"] is True

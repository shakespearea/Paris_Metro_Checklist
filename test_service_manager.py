import pytest
from unittest.mock import patch

from service_manager import MetroService
from file_manager import load_states

@pytest.fixture
def metro(tmp_path):
    stateFile = tmp_path / "visited.json"
    with patch("service_manager.load_metro_lines", return_value={"1": ["Nation", "Bastille"]}):
        return MetroService(stateFile=stateFile)
    
def test_toggle_visited_false_to_true(metro):
    assert metro.visited_states("Nation") is False
    metro.toggle_visited("Nation")
    assert metro.visited_states("Nation") is True

def test_toggle_visited_true_to_false(metro):
    metro.toggle_visited("Nation")
    metro.toggle_visited("Nation")
    assert metro.visited_states("Nation") is False
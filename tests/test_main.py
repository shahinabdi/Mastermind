import pytest
from unittest.mock import patch
from src.main import get_player_choice, play_game


@pytest.fixture
def test_get_player_choice_valid():
    """Test get_player_choice with valid input."""
    with patch('builtins.input', return_value='1'):
        choice = get_player_choice()
        assert choice == 1


def test_get_player_choice_invalid_then_valid():
    """Test get_player_choice with invalid then valid input."""
    with patch('builtins.input', side_effect=['3', 'a', '1']):
        choice = get_player_choice()
        assert choice == 1


@patch('src.game.game_controller.GameController.play', return_value=True)
@patch('builtins.input', side_effect=['1', 'n'])
def test_play_game_human(mock_input, mock_play):
    """Test playing game as human."""
    play_game()
    assert mock_play.called


@patch('src.game.game_controller.GameController.play', return_value=True)
@patch('builtins.input', side_effect=['2', 'n'])
def test_play_game_computer(mock_input, mock_play):
    """Test playing game with computer."""
    play_game()
    assert mock_play.called


@patch('src.game.game_controller.GameController.play', return_value=True)
@patch('builtins.input', side_effect=['1', 'y', '2', 'n'])
def test_play_game_multiple_rounds(mock_input, mock_play):
    """Test playing multiple rounds."""
    play_game()
    assert mock_play.call_count == 2

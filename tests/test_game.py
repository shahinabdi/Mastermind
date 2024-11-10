from src.utils.constants import GameRules
from src.game.config import GameConfig
from src.game.mastermind import MastermindGame
import pytest
import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


@pytest.fixture
def game():
    config = GameConfig()
    return MastermindGame(config)


def test_secret_code_generation(game):
    """Test if secret code is generated with correct length and valid colors."""
    assert len(game.secret_code) == GameRules.CODE_LENGTH
    assert all(color in GameRules.DEFAULT_COLORS for color in game.secret_code)


def test_validate_guess(game):
    """Test guess validation."""
    valid_guess = GameRules.DEFAULT_COLORS[:GameRules.CODE_LENGTH]
    invalid_guess = ['INVALID'] * GameRules.CODE_LENGTH

    assert game.validate_guess(valid_guess) is True
    assert game.validate_guess(invalid_guess) is False


def test_check_guess(game):
    """Test guess checking logic."""
    # Set a known secret code
    game.secret_code = ['R', 'G', 'B', 'Y']

    # Test exact match
    exact_match = game.check_guess(['R', 'G', 'B', 'Y'])
    assert exact_match == (4, 0)

    # Test partial match
    partial_match = game.check_guess(['Y', 'R', 'G', 'B'])
    assert partial_match[0] + partial_match[1] == 4  # All colors correct


def test_game_over_conditions(game):
    """Test game over conditions."""
    # Game should not be over initially
    assert game.is_game_over() is False

    # Game should be over after max attempts
    for _ in range(GameRules.MAX_ATTEMPTS):
        game.check_guess(GameRules.DEFAULT_COLORS[:GameRules.CODE_LENGTH])
    assert game.is_game_over() is True

import pytest
import sys
import os
from src.game.config import GameConfig
from src.utils.constants import GameRules

# Add src directory to Python path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


@pytest.fixture
def default_config():
    """Fixture providing default GameConfig instance."""
    return GameConfig()


def test_valid_config(default_config):
    """Test valid configuration."""
    assert default_config.code_length == GameRules.CODE_LENGTH
    assert default_config.max_attempts == GameRules.MAX_ATTEMPTS
    assert default_config.available_colors == GameRules.DEFAULT_COLORS
    assert default_config.validate() is True


def test_invalid_code_length():
    """Test configuration with invalid code length."""
    invalid_config = GameConfig(code_length=0)
    assert invalid_config.validate() is False
    assert invalid_config.code_length == 0
    assert invalid_config.max_attempts == GameRules.MAX_ATTEMPTS
    assert invalid_config.available_colors == GameRules.DEFAULT_COLORS


def test_invalid_max_attempts():
    """Test configuration with invalid max attempts."""
    invalid_config = GameConfig(max_attempts=0)
    assert invalid_config.validate() is False
    assert invalid_config.code_length == GameRules.CODE_LENGTH
    assert invalid_config.max_attempts == 0
    assert invalid_config.available_colors == GameRules.DEFAULT_COLORS


def test_invalid_colors():
    """Test configuration with invalid colors list."""
    invalid_config = GameConfig(available_colors=[])
    assert invalid_config.validate() is False
    assert invalid_config.code_length == GameRules.CODE_LENGTH
    assert invalid_config.max_attempts == GameRules.MAX_ATTEMPTS
    assert invalid_config.available_colors == []


def test_custom_valid_config():
    """Test configuration with custom valid values."""
    custom_config = GameConfig(
        code_length=6,
        max_attempts=15,
        available_colors=GameRules.DEFAULT_COLORS +
        ['P']  # Adding one more color
    )
    assert custom_config.validate() is True
    assert custom_config.code_length == 6
    assert custom_config.max_attempts == 15
    assert len(custom_config.available_colors) == len(
        GameRules.DEFAULT_COLORS) + 1

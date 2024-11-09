from enum import Enum
from typing import List


class Color(Enum):
    """Available colors for the game."""
    RED = 'R'
    GREEN = 'G'
    BLUE = 'B'
    YELLOW = 'Y'
    WHITE = 'W'
    BLACK = 'K'


class GameRules:
    """Game rules and configurations."""
    DEFAULT_COLORS: List[str] = [color.value for color in Color]
    CODE_LENGTH: int = 4
    MAX_ATTEMPTS: int = 10

    # Feedback symbols
    CORRECT_POSITION = '●'  # Black peg
    CORRECT_COLOR = '○'     # White peg

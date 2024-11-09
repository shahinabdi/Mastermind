from dataclasses import dataclass
from typing import List
from ..utils.constants import GameRules


@dataclass
class GameConfig:
    """Game configuration settings."""
    code_length: int = GameRules.CODE_LENGTH
    max_attempts: int = GameRules.MAX_ATTEMPTS
    available_colors: List[str] = GameRules.DEFAULT_COLORS

    def validate(self) -> bool:
        """Validate configuration settings."""
        return (self.code_length > 0 and
                self.max_attempts > 0 and
                len(self.available_colors) >= self.code_length)

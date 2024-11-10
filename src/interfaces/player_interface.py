from abc import ABC, abstractmethod
from typing import List


class IPlayer(ABC):
    """Base interface for game players (human or computer)."""

    @abstractmethod
    def make_guess(self) -> List[str]:
        """Make a guess for the secret code."""
        pass

    @abstractmethod
    def get_feedback(self, correct_position: int, correct_color: int) -> None:
        """Receive feedback for the last guess."""
        pass

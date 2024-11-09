from abc import ABC, abstractmethod
from typing import List, Tuple


class IGame(ABC):
    """Base interface for the Mastermind game."""

    @abstractmethod
    def generate_secret_code(self) -> List[str]:
        """Generate a secret code for game."""
        pass

    @abstractmethod
    def validate_guess(self, guess: List[str]) -> bool:
        """Validate if the guess is in correct format."""
        pass

    @abstractmethod
    def check_guess(self, guess: List[str]) -> tuple[int, int]:
        """
        Check the guess against the secret code.
        Returns:
            Tuple[int, int]: (correct_position, correct_color_wrong_position)
        """
        pass

    @abstractmethod
    def is_game_over(self) -> bool:
        """Check if the game is over."""
        pass

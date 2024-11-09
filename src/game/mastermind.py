import random
from typing import List, Tuple
from ..interfaces.game_interface import IGame
from ..game.config import GameConfig


class MastermindGame(IGame):
    def __init__(self, config: GameConfig):
        if not config.validate():
            raise ValueError("Invalid game configuration")

        self.config = config
        self.secret_code: List[str] = []
        self.attempts: int = 0
        self.is_won: bool = False
        self.generate_secret_code()

    def generate_secret_code(self) -> List[str]:
        """Generate a random secret code."""
        self.secret_code = random.choices(
            self.config.available_colors,
            k=self.config.code_length
        )
        return self.secret_code

    def validate_guess(self, guess: List[str]) -> bool:
        """Validate if the guess is in correct format."""
        if len(guess) != self.config.code_length:
            return False
        return all(color in self.config.available_colors for color in guess)

    def check_guess(self, guess: List[str]) -> Tuple[int, int]:
        """Check the guess against the secret code."""
        if not self.validate_guess(guess):
            raise ValueError("Invalid guess")

        self.attempts += 1

        # Count exact matches
        correct_position = sum(1 for i in range(len(guess))
                               if guess[i] == self.secret_code[i])

        # Count color matches (including exact matches)
        guess_colors = guess.copy()
        secret_colors = self.secret_code.copy()

        total_matches = 0
        for color in self.config.available_colors:
            total_matches += min(
                guess_colors.count(color),
                secret_colors.count(color)
            )

        # Calculate colors in wrong position
        correct_color = total_matches - correct_position

        # Check if game is won
        self.is_won = correct_position == self.config.code_length

        return (correct_position, correct_color)

    def is_game_over(self) -> bool:
        """Check if the game is over."""
        return self.is_won or self.attempts >= self.config.max_attempts

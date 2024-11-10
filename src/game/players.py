# Standard library imports
import random
from typing import List, Dict

# Local application imports
from src.interfaces.player_interface import IPlayer
from src.utils.constants import GameRules, Color


class HumanPlayer(IPlayer):
    def make_guess(self) -> List[str]:
        """Get guess from human player."""
        available_colors = [color.value for color in Color]
        while True:
            guess = input(
                f"Enter your guess ({GameRules.CODE_LENGTH} colors"
                f" from {', '.join(available_colors)}): "
            ).upper().split()

            if (len(guess) == GameRules.CODE_LENGTH and
                    all(color in available_colors for color in guess)):
                return guess

            print("Invalid guess. Please try again.")

    def get_feedback(self, correct_position: int, correct_color: int) -> None:
        """Display feedback to human player."""
        print(
            f"Correct position: {GameRules.CORRECT_POSITION * correct_position}")
        print(f"Correct color: {GameRules.CORRECT_COLOR * correct_color}")


class ComputerPlayer(IPlayer):
    def __init__(self):
        self.possible_colors = [color.value for color in Color]
        self.last_guess: List[str] = []
        self.feedback_history: List[Dict] = []

    def make_guess(self) -> List[str]:
        """
        Make a guess based on simple strategy:
        - First guess: Random colors
        - Subsequent guesses: Use feedback to make more informed guesses
        """
        if not self.feedback_history:
            # First guess is random
            self.last_guess = random.choices(
                self.possible_colors,
                k=GameRules.CODE_LENGTH
            )
        else:
            # Use previous feedback to make a more informed guess
            good_colors = set()
            for feedback in self.feedback_history:
                if feedback['correct_position'] + feedback['correct_color'] > 0:
                    good_colors.update(feedback['guess'])

            # If we have good colors, prefer them
            colors_to_use = list(
                good_colors) if good_colors else self.possible_colors
            self.last_guess = random.choices(
                colors_to_use,
                k=GameRules.CODE_LENGTH
            )

        return self.last_guess

    def get_feedback(self, correct_position: int, correct_color: int) -> None:
        """Store feedback for future guesses."""
        self.feedback_history.append({
            'guess': self.last_guess,
            'correct_position': correct_position,
            'correct_color': correct_color
        })

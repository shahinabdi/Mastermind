from typing import List
from ..interfaces.player_interface import IPlayer
from ..utils.constants import GameRules


class HumanPlayer(IPlayer):
    def make_guess(self) -> List[str]:
        """Get guess from human player."""
        while True:
            guess = input(f"Enter your guess ({GameRules.CODE_LENGTH} colors"
                          f" from {', '.join(GameRules.DEFAULT_COLORS)}): "
                          ).upper().split()

            if len(guess) == GameRules.CODE_LENGTH and all(
                color in GameRules.DEFAULT_COLORS for color in guess
            ):
                return guess
            print("Invalid guess. Please try again.")

    def get_feedback(self, correct_position: int, correct_color: int) -> None:
        """Display feedback to human player."""
        print(
            f"Correct position: {GameRules.CORRECT_POSITION * correct_position}")
        print(f"Correct color: {GameRules.CORRECT_COLOR * correct_color}")

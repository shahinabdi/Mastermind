from typing import Optional
from .mastermind import MastermindGame
from .config import GameConfig
from .players import HumanPlayer, ComputerPlayer
from ..interfaces.player_interface import IPlayer


class GameController:
    def __init__(self, player: Optional[IPlayer] = None):
        self.config = GameConfig()
        self.game = MastermindGame(self.config)
        self.player = player or HumanPlayer()

    def display_game_state(self, attempts: int, max_attempts: int):
        """Display current game state."""
        print(f"\nAttempt {attempts}/{max_attempts}")
        print("-" * 20)

    def play(self) -> bool:
        """
        Main game loop.
        Returns:
            bool: True if player won, False otherwise
        """
        print("\nWelcome to Mastermind!")
        print(f"Try to guess the {self.config.code_length} color code.")
        print(f"Available colors: {', '.join(self.config.available_colors)}")

        while not self.game.is_game_over():
            self.display_game_state(
                self.game.attempts + 1,
                self.config.max_attempts
            )

            # Get player's guess
            guess = self.player.make_guess()

            # Check guess and provide feedback
            correct_position, correct_color = self.game.check_guess(guess)
            self.player.get_feedback(correct_position, correct_color)

            # Check if won
            if self.game.is_won:
                print("\nCongratulations! You've won!")
                return True

        if not self.game.is_won:
            print("\nGame Over! You've run out of attempts.")
            print(f"The secret code was: {' '.join(self.game.secret_code)}")
            return False

        return True

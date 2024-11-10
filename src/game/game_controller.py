# Standard library imports
from typing import Optional

# Local application imports
from src.game.mastermind import MastermindGame
from src.game.config import GameConfig
from src.game.players import HumanPlayer, ComputerPlayer
from src.interfaces.player_interface import IPlayer


class GameController:
    def __init__(self, player: Optional[IPlayer] = None):
        self.config = GameConfig()
        self.game = MastermindGame(self.config)
        self.player = player or HumanPlayer()
        self.is_computer = isinstance(self.player, ComputerPlayer)

    def display_game_state(self, attempts: int, max_attempts: int):
        """Display current game state."""
        print(f"\nAttempt {attempts}/{max_attempts}")
        print("-" * 20)

    def display_welcome_message(self):
        """Display welcome message and game instructions."""
        print("\nWelcome to Mastermind!")
        print(f"Try to guess the {self.config.code_length} color code.")
        print(f"Available colors: {', '.join(self.config.available_colors)}")
        if self.is_computer:
            print("Computer is playing...")
            print("Press Enter after each move to continue...")

    def play(self) -> bool:
        """
        Main game loop.
        Returns:
            bool: True if player won, False otherwise
        """
        self.display_welcome_message()

        while not self.game.is_game_over():
            self.display_game_state(
                self.game.attempts + 1,
                self.config.max_attempts
            )

            # Get player's guess
            guess = self.player.make_guess()

            # If computer is playing, show its guess and wait for user input
            if self.is_computer:
                print(f"Computer's guess: {' '.join(guess)}")
                input("Press Enter to continue...")

            # Check guess and provide feedback
            correct_position, correct_color = self.game.check_guess(guess)
            self.player.get_feedback(correct_position, correct_color)

            # Display result for computer player
            if self.is_computer:
                print(f"Results: {correct_position} correct positions, "
                      f"{correct_color} correct colors")

            # Check if won
            if self.game.is_won:
                winner = "Computer" if self.is_computer else "Congratulations! You"
                print(f"\n{winner}'ve won!")
                print(f"Solved in {self.game.attempts} attempts!")
                return True

        if not self.game.is_won:
            loser = "Computer" if self.is_computer else "You"
            print(f"\nGame Over! {loser}'ve run out of attempts.")
            print(f"The secret code was: {' '.join(self.game.secret_code)}")
            return False

        return True

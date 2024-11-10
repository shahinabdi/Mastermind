# Local application imports
from src.game.game_controller import GameController
from src.game.players import HumanPlayer, ComputerPlayer


def get_player_choice() -> int:
    """Get valid player choice from user."""
    while True:
        print("\nWelcome to Mastermind!")
        print("1. Play as Human")
        print("2. Watch Computer Play")
        try:
            choice = int(input("Choose mode (1-2): "))
            if choice in (1, 2):
                return choice
            print("Please enter 1 or 2")
        except ValueError:
            print("Please enter a valid number")


def play_game() -> None:
    """Main game function."""
    choice = get_player_choice()
    player = HumanPlayer() if choice == 1 else ComputerPlayer()

    game = GameController(player)
    game.play()

    if input("\nPlay again? (y/n): ").lower().startswith('y'):
        play_game()


if __name__ == "__main__":
    play_game()

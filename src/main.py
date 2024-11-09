from game.game_controller import GameController
from game.players import HumanPlayer, ComputerPlayer


def main():
    # Get game mode
    print("Welcome to Mastermind!")
    print("1. Play as Human")
    print("2. Watch Computer Play")

    while True:
        try:
            choice = int(input("Choose mode (1-2): "))
            if choice in (1, 2):
                break
            print("Please enter 1 or 2")
        except ValueError:
            print("Please enter a valid number")

    # Create appropriate player
    player = HumanPlayer() if choice == 1 else ComputerPlayer()

    # Start game
    game = GameController(player)
    game.play()

    # Ask to play again
    if input("\nPlay again? (y/n): ").lower().startswith('y'):
        main()


if __name__ == "__main__":
    main()

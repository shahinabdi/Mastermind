import pytest
from unittest.mock import patch, MagicMock
from src.game.game_controller import GameController
from src.game.players import HumanPlayer, ComputerPlayer
from src.utils.constants import GameRules


@pytest.fixture
def controller():
    return GameController()


@pytest.fixture
def controller_with_computer():
    return GameController(ComputerPlayer())


@pytest.fixture
def mock_player():
    """Create a mock player for testing."""
    player = MagicMock()
    player.make_guess.return_value = ['R', 'G', 'B', 'Y']
    return player


def test_game_controller_initialization(controller):
    """Test GameController initialization."""
    assert controller.player is not None
    assert isinstance(controller.player, HumanPlayer)
    assert controller.config is not None
    assert controller.game is not None


def test_game_controller_with_computer_player(controller_with_computer):
    """Test GameController with computer player."""
    assert isinstance(controller_with_computer.player, ComputerPlayer)


def test_game_controller_with_mock_player():
    """Test GameController with mock player."""
    mock_player = MagicMock()
    controller = GameController(mock_player)

    mock_player.make_guess.return_value = ['R', 'G', 'B', 'Y']
    controller.game.secret_code = ['R', 'G', 'B', 'Y']

    controller.play()

    # Verify interactions
    assert mock_player.make_guess.called
    assert mock_player.get_feedback.called
    mock_player.get_feedback.assert_called_with(4, 0)


def test_display_game_state(controller, capsys):
    """Test display_game_state method."""
    controller.display_game_state(1, 10)
    captured = capsys.readouterr()
    assert "Attempt 1/10" in captured.out


def test_play_game_loss(mock_player):
    """Test playing game until loss."""
    controller = GameController(mock_player)
    controller.game.secret_code = ['W', 'W', 'W', 'W']

    # Set up mock behavior
    mock_player.make_guess.return_value = ['R', 'G', 'B', 'Y']

    result = controller.play()

    # Verify interactions
    assert mock_player.make_guess.call_count == GameRules.MAX_ATTEMPTS
    assert result is False


def test_play_game_win(mock_player):
    """Test playing game until win."""
    controller = GameController(mock_player)
    controller.game.secret_code = ['R', 'G', 'B', 'Y']

    # Set up mock behavior
    mock_player.make_guess.return_value = ['R', 'G', 'B', 'Y']

    result = controller.play()

    # Verify interactions
    assert mock_player.make_guess.call_count == 1
    mock_player.get_feedback.assert_called_once_with(4, 0)
    assert result is True


def test_play_computer_game(mock_player):
    """Test playing game with computer player."""
    with patch('builtins.input', side_effect=[''] * 10) as mock_input:
        controller = GameController(mock_player)
        controller.is_computer = True  # Set computer player flag
        mock_player.make_guess.side_effect = [['R', 'G', 'B', 'Y']] * 10

        result = controller.play()

        # Verify interactions
        assert isinstance(result, bool)
        assert mock_player.make_guess.called
        # For computer player, input should be called for "Press Enter to continue"
        assert mock_input.call_count > 0


def test_game_feedback(mock_player, capsys):
    """Test game feedback messages."""
    controller = GameController(mock_player)
    controller.game.secret_code = ['R', 'G', 'B', 'Y']
    mock_player.make_guess.return_value = ['R', 'G', 'B', 'Y']

    controller.play()

    captured = capsys.readouterr()
    assert "Welcome to Mastermind!" in captured.out
    assert f"Try to guess the {GameRules.CODE_LENGTH} color code" in captured.out
    assert "Congratulations" in captured.out
    assert mock_player.get_feedback.called


def test_game_over_message(mock_player, capsys):
    """Test game over message."""
    controller = GameController(mock_player)
    controller.game.secret_code = ['W', 'W', 'W', 'W']
    mock_player.make_guess.return_value = ['R', 'G', 'B', 'Y']

    controller.play()

    captured = capsys.readouterr()
    assert "Game Over" in captured.out
    assert "The secret code was" in captured.out
    assert mock_player.get_feedback.call_count == GameRules.MAX_ATTEMPTS


def test_player_interaction_sequence(mock_player):
    """Test the sequence of interactions with the player."""
    from unittest.mock import call

    controller = GameController(mock_player)
    controller.game.secret_code = ['R', 'G', 'B', 'Y']

    # Set up a sequence of guesses
    mock_player.make_guess.side_effect = [
        ['R', 'B', 'Y', 'G'],  # First guess: 1 correct position, 3 correct colors
        ['R', 'G', 'B', 'Y']   # Second guess: All correct
    ]

    controller.play()

    # Verify the sequence of interactions
    assert mock_player.make_guess.call_count == 2
    mock_player.get_feedback.assert_has_calls([
        call(1, 3),  # First feedback
        call(4, 0)   # Second feedback
    ])

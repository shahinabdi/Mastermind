import pytest
from unittest.mock import patch
from src.game.players import HumanPlayer, ComputerPlayer
from src.utils.constants import GameRules, Color


@pytest.fixture
def human_player():
    return HumanPlayer()


@pytest.fixture
def computer_player():
    return ComputerPlayer()


def test_human_player_valid_guess(human_player):
    """Test human player with valid input."""
    with patch('builtins.input', return_value='R G B Y'):
        guess = human_player.make_guess()
        assert len(guess) == GameRules.CODE_LENGTH
        assert all(color in [c.value for c in Color] for color in guess)


def test_human_player_invalid_then_valid_guess(human_player):
    """Test human player with invalid input followed by valid input."""
    with patch('builtins.input', side_effect=['X X X X', 'R G B Y']):
        guess = human_player.make_guess()
        assert len(guess) == GameRules.CODE_LENGTH
        assert all(color in [c.value for c in Color] for color in guess)


def test_human_player_feedback(human_player, capsys):
    """Test human player feedback display."""
    human_player.get_feedback(2, 1)
    captured = capsys.readouterr()
    assert "Correct position: ●●" in captured.out
    assert "Correct color: ○" in captured.out


def test_computer_player_initial_guess(computer_player):
    """Test computer player's first guess."""
    guess = computer_player.make_guess()
    assert len(guess) == GameRules.CODE_LENGTH
    assert all(color in [c.value for c in Color] for color in guess)


def test_computer_player_with_feedback(computer_player):
    """Test computer player's guess after receiving feedback."""
    first_guess = computer_player.make_guess()
    computer_player.get_feedback(2, 1)
    second_guess = computer_player.make_guess()

    assert len(second_guess) == GameRules.CODE_LENGTH
    assert all(color in [c.value for c in Color] for color in second_guess)
    assert second_guess != first_guess


def test_computer_player_guesses_differ():
    """Test that computer player makes different guesses."""
    computer = ComputerPlayer()
    guesses = set()
    for _ in range(5):
        guess = computer.make_guess()
        guesses.add(tuple(guess))
        computer.get_feedback(1, 1)

        assert len(guess) == GameRules.CODE_LENGTH
        assert all(color in [c.value for c in Color] for color in guess)

    assert len(guesses) > 1


def test_computer_player_feedback_storage(computer_player):
    """Test computer player stores feedback correctly."""
    guess = computer_player.make_guess()
    computer_player.get_feedback(2, 1)

    assert len(computer_player.feedback_history) == 1
    feedback = computer_player.feedback_history[0]
    assert feedback['correct_position'] == 2
    assert feedback['correct_color'] == 1
    assert feedback['guess'] == guess

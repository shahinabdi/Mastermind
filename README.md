# Mastermind Game

A command-line implementation of the classic Mastermind game in Python. This project was originally created as a university assignment and has been rebuilt with modern Python practices, comprehensive testing, and proper software architecture.

## Author

**Shahin ABDI**

- GitHub: [shahinabdi](https://github.com/shahinabdi)

## Project Overview

Mastermind is a code-breaking game where one player creates a secret code and another player tries to guess it within a limited number of attempts. After each guess, the code-maker provides feedback about how many colors are correct and in the correct position.

### Features

- Command-line interface
- Single player mode against computer
- Computer player mode with basic AI strategy
- Configurable game rules (code length, available colors, attempts)
- Comprehensive feedback after each guess
- Score tracking

## Technical Details

### Project Structure

```
mastermind/
├── conftest.py               # Pytest configuration for all tests
├── LICENSE                   # MIT License file
├── README.md                # Project documentation
├── requirements.txt         # Project dependencies
├── pytest.ini              # Pytest settings
├── setup.py                # Package installation configuration
├── src/                    # Source code root
│   ├── __init__.py        # Makes src a Python package
│   ├── game/              # Game logic package
│   │   ├── __init__.py
│   │   ├── config.py      # Game configuration settings
│   │   ├── game_controller.py  # Main game controller
│   │   ├── mastermind.py      # Core game mechanics
│   │   └── players.py         # Player implementations
│   ├── interfaces/        # Abstract base classes
│   │   ├── __init__.py
│   │   ├── game_interface.py  # Game interface definitions
│   │   └── player_interface.py # Player interface definitions
│   ├── main.py           # Application entry point
│   ├── models/           # Data models (if needed)
│   │   └── __init__.py
│   └── utils/            # Utility functions and constants
│       ├── __init__.py
│       └── constants.py  # Game constants and enums
├── tests/               # Test suite directory
│   ├── __init__.py     # Makes tests a package
│   ├── test_config.py          # Tests for game configuration
│   ├── test_game_controller.py # Tests for game controller
│   ├── test_game.py           # Tests for core game mechanics
│   ├── test_main.py           # Tests for main entry point
│   └── test_players.py        # Tests for player implementations
```

### Technologies Used

- Python 3.11.5
- pytest for testing
- mypy for type checking
- Coverage.py for test coverage

## Setup and Installation

1. Ensure you have Python 3.11 or later installed:

```bash
python --version
```

2. Create and activate a virtual environment:

```bash
# Create virtual environment
python -m venv venv

# Activate on Unix/macOS
source venv/bin/activate

# Activate on Windows
venv\Scripts\activate
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

## Running the Game

```bash
python src/main.py
```

## Playing the Game

1. Choose game mode:

   - Play as Human
   - Watch Computer Play

2. If playing as human:

   - Enter colors as space-separated values (e.g., "R G B Y")
   - Available colors: R (Red), G (Green), B (Blue), Y (Yellow), W (White), K (Black)
   - Get fedback after each guess:
     - Black dot (●): Correct color and position
     - White dot (○): Correct color, wrong position

## Playing the Game

### Running Tests

```bash
# Run all tests
pytest

# Run tests with coverage
pytest --cov=src

# Run specific test file
pytest tests/test_game_controller.py
```

### Code Quality

```bash
# Type checking
mypy src/

# Code formatting
black src/

# Sort imports
isort src/
```

## Project Architecture

### Design Patterns

- Interface-based design with abstract base classes
- MVC-inspired architecture
- Strategy pattern for player implementations
- Factory pattern for game configuration

### Key Components

- `GameController`: Manages game flow and player interaction
- `MastermindGame`: Implements core game logic
- `Player Interface`: Defines player behavior contract
- `Game Interface`: Defines game behavior contract

### Testing Strategy

- Unit tests for all components
- Mock objects for player interaction
- Parametrized tests for game rules
- Integration tests for game flow
- 90%+ test coverage

## License

MIT License

## Contributing

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request

# Version History

- 1.0.0
  - Complete rebuild of university project
  - Added comprehensive test suite
  - Implemented proper architecture
  - Added computer player

# 📘 Assignment: Hangman Game

## 🎯 Objective

Build a console-based Hangman game in Python to practice string manipulation, control flow, and user input handling. Students will implement the core game loop, word selection, guess validation, and win/lose conditions.

## 📝 Tasks

### 🛠️ Game Implementation

#### Description
Implement a playable Hangman game that picks a secret word and allows a player to guess letters until they either reveal the word or run out of attempts. A starter file `starter-code.py` is provided to help you get started.

#### Requirements
Completed program should:

- Randomly select a secret word from a predefined list (in-script or loaded from a file).
- Accept single-letter guesses (case-insensitive) and display current progress using underscores for unrevealed letters (e.g., `_ a _ _ m a n`).
- Prevent repeated guesses from decrementing the remaining attempts.
- Track and display remaining incorrect attempts (suggested: 6 attempts).
- End the game when the player guesses the word or exhausts attempts, and display an appropriate win/lose message including the secret word.
- Provide clear prompts and validate input (only single alphabetic characters accepted).

Example gameplay (simplified):

```
Secret: _ a _ _ m a n
Guess a letter: g
Incorrect! Attempts left: 5
Guess a letter: h
Correct! Secret: h a n g m a n
You win! 🎉
```

### 🛠️ Optional Enhancements

#### Description
Add one or more quality-of-life or gameplay improvements to make the assignment more engaging.

#### Requirements

- Add ASCII-art hangman stages that update with each incorrect guess.
- Load words from a separate `words.txt` file and support multiple difficulty levels.
- Track score across multiple rounds or implement a hint system.


# game_logic.py
import random
from ascii_art import STAGES

# List of secret words
WORDS = ["python", "git", "github", "snowman", "meltdown"]


def get_random_word():
    """Selects a random word from the list."""
    return random.choice(WORDS)


def display_game_state(mistakes, secret_word, guessed_letters):
    """Displays the snowman stage and the current word state."""
    print(STAGES[mistakes])
    display_word = ""
    for letter in secret_word:
        if letter in guessed_letters:
            display_word += letter + " "
        else:
            display_word += "_ "
    print("Word:", display_word)
    print("\n")


def play_game():
    secret_word = get_random_word()
    guessed_letters = []
    mistakes = 0
    max_mistakes = len(STAGES) - 1

    print("Welcome to Snowman Meltdown!")

    while True:
        display_game_state(mistakes, secret_word, guessed_letters)

        # Check for win
        if all(letter in guessed_letters for letter in secret_word):
            print("🎉 Congratulations! You saved the snowman! 🧊")
            break

        # Check for loss
        if mistakes >= max_mistakes:
            print(STAGES[-1])
            print(f"💀 The snowman melted! The word was: {secret_word}")
            break

        # Ask user for input
        guess = input("Guess a letter: ").lower()

        # Skip invalid inputs or already guessed letters
        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single valid letter.\n")
            continue
        if guess in guessed_letters:
            print("You already guessed that letter!\n")
            continue

        # Add to guessed letters and update mistakes if wrong
        guessed_letters.append(guess)
        if guess not in secret_word:
            mistakes += 1
            print("Incorrect guess!\n")
        else:
            print("Good guess!\n")

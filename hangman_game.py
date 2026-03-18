# Hangman Game
# CodeAlpha Python Programming Tasks

# We need the random module to pick a random word
import random

# --- STEP 1: List of words to guess from ---
words = ["python", "apple", "mango", "football", "laptop"]

# Pick a random word from the list
secret_word = random.choice(words)

# --- STEP 2: Set up the game ---

# This will store the letters the player has guessed
guessed_letters = []

# The player gets 6 wrong guesses before they lose
wrong_guesses = 0
max_wrong = 6

print("Welcome to Hangman!")
print("Try to guess the word letter by letter.")
print("You have 6 incorrect guesses allowed.")
print("")

# --- STEP 3: Game Loop - keeps running until win or lose ---
while wrong_guesses < max_wrong:

    # --- Build the word to display ---
    display_word = ""
    all_guessed = True  # We assume all letters are guessed

    for letter in secret_word:
        if letter in guessed_letters:
            display_word = display_word + letter + " "  # add the letter
        else:
            display_word = display_word + "_ "          # add a blank
            all_guessed = False  # Not all letters guessed yet

    print("Word: " + display_word)

    # Show how many wrong guesses are left
    print("Wrong guesses so far:", wrong_guesses, "out of", max_wrong)
    print("Letters you guessed:", guessed_letters)
    print("")

    # --- STEP 4: Check if player won ---
    if all_guessed:
        print("🎉 You won! The word was:", secret_word)
        break  # Stop the game

    # --- STEP 5: Ask the player to guess a letter ---
    guess = input("Guess a letter: ")

    # Make the letter lowercase so capital letters still work
    guess = guess.lower()

    # Check if they already guessed this letter
    if guess in guessed_letters:
        print("You already guessed that letter! Try another one.")
        print("")

    # Check if the guess is correct
    elif guess in secret_word:
        print("✅ Correct!")
        guessed_letters.append(guess)  # Add to guessed list
        print("")

    # If the guess is wrong
    else:
        print("❌ Wrong!")
        wrong_guesses = wrong_guesses + 1  # Add 1 to wrong guesses
        guessed_letters.append(guess)      # Add to guessed list
        print("")

# --- STEP 6: If player runs out of guesses ---
if wrong_guesses == max_wrong:
    print("💀 Game over! The word was:", secret_word)
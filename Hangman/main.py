import random

import hangman_art
import hangman_words


# Display the Hangman logo
print(hangman_art.logo)

# Randomly select a word
chosen_word = random.choice(hangman_words.word_list)


# Game variables
lives = 6
gameover = False
words_guessed = []
display = ""


# Create the blank word display
for i in range(len(chosen_word)):
    display += "_"

print(display)


# Main game loop
while not gameover:

    # Reset the display for each round
    display = ""

    # Display the current Hangman stage
    print(hangman_art.stages[lives])

    # Get the player's guess
    guess = input("Guess a letter: ").lower()

    # Check if the guessed letter is in the word
    if guess not in chosen_word:
        lives -= 1
        print(f"You guessed {guess}, that's not in the word. You lose a life.")

    # End the game if the player runs out of lives
    if lives == 0:
        gameover = True
        print(hangman_art.stages[0])
        print(f"IT WAS {chosen_word}! YOU LOSE.")

    # Notify the player if they already guessed the letter
    if guess in words_guessed:
        print(f"You've already guessed {guess}")

    # Build the current display word
    for char in chosen_word:
        if guess == char:
            display += char
            words_guessed.append(guess)
        elif char in words_guessed:
            display += char
        else:
            display += "_"

    # Check if the player has guessed the entire word
    if display == chosen_word:
        gameover = True
        print("You Win!")

    # Show the current progress and remaining lives
    print(display)
    print(f"****************************{lives}/6 LIVES LEFT****************************")
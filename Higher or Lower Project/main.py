import game_data
import art
import random
import os


# Selects and returns a random account from the game_data list
def random_account():
    return random.choice(game_data.data)


# Checks whether the user's guess is correct
# Returns True if the user selected the account with more followers
# Returns False if the user's guess is incorrect
def check_answer(guess, a, b):
    if a['follower_count'] > b['follower_count'] and guess == "a":
        return True
    elif a['follower_count'] < b['follower_count'] and guess == "b":
        return True
    else:
        return False


# Runs the Higher or Lower game
def game():
    # Keeps track of the player's score
    score = 0

    # Selects two random accounts to compare
    account_a = random_account()
    account_b = random_account()

    # Displays the game logo and introduction
    print(art.logo)
    print("Welcome to the Higher or Lower Game!")
    print("The goal is to guess who has more followers on Instagram.")

    # Continues running the game until the player gives an incorrect answer
    while True:

        # Displays the information for the first account
        # The follower count is not shown because that is what the player is trying to guess
        print(
            f"Compare A: {account_a['name']}, "
            f"a {account_a['description']}, "
            f"from {account_a['country']}"
        )

        # Displays the "VS" logo between the two accounts
        print(art.vs)

        # Displays the information for the second account
        print(
            f"Against B: {account_b['name']}, "
            f"a {account_b['description']}, "
            f"from {account_b['country']}."
        )

        # Asks the player to choose which account has more followers
        # .lower() converts the answer to lowercase so "A" and "a" are treated the same
        answer = input(
            "Who has more followers? Type 'A' or 'B': "
        ).lower()

        # Checks if the player's answer is correct
        if check_answer(answer, account_a, account_b):
            # Increase the score by 1 if the answer is correct
            score += 1

            # Tell the player their answer was correct and display their score
            print(f"You're right! Current score: {score}.")

        else:
            # Clear the terminal when the player gets the answer wrong
            os.system("clear")

            # Display the game logo again
            print(art.logo)

            # Display the player's final score
            print(f"Sorry, that's wrong. Final score: {score}.")

            # End the game loop
            break

        # The previous Account B becomes the new Account A
        # This allows the player to continue comparing from the previous round
        account_a = account_b

        # Select a new random account to become Account B
        account_b = random_account()

        # Clear the terminal before displaying the next round
        os.system("clear")

        # Display the logo at the top of the new round
        print(art.logo)

    # Display the final score after the game loop ends
    print(f"Game over! Final score: {score}.")


# Starts the game
game()
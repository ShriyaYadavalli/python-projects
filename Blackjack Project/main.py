import random
import art


deck = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]


# FUNCTIONS

def deal_cards(hand):
    hand.append(random.choice(deck))


def calculate_score(cards):
    score = sum(cards)

    # Change Ace from 11 to 1 if needed
    for index, card in enumerate(cards):
        if score > 21 and card == 11:
            cards[index] = 1
            score = sum(cards)

    return score


def is_blackjack(cards):
    return len(cards) == 2 and sum(cards) == 21


def check_game_over(player_hand, dealer_hand):
    player_score = calculate_score(player_hand)
    dealer_score = calculate_score(dealer_hand)

    if is_blackjack(player_hand) or is_blackjack(dealer_hand):
        return True

    if player_score > 21 or dealer_score > 21:
        return True

    return False


def player_turn(player_hand):

    player_turn_over = False

    while not player_turn_over:

        choice = input(
            "Type 'y' to get another card, type 'n' to pass: "
        )

        if choice == "y":

            deal_cards(player_hand)

            player_score = calculate_score(player_hand)

            print(f"Your cards: {player_hand}")
            print(f"Your score: {player_score}")

            if player_score > 21:
                return True   # game is over because player lost

        else:
            player_turn_over = True

    return False   # player finished, but game continues


def dealer_turn(dealer_hand):

    dealer_score = calculate_score(dealer_hand)

    while dealer_score < 17:

        deal_cards(dealer_hand)

        dealer_score = calculate_score(dealer_hand)


def end_game(player_hand, dealer_hand):

    player_score = calculate_score(player_hand)
    dealer_score = calculate_score(dealer_hand)

    print("\n---------- FINAL RESULTS ----------")

    print(f"Your cards: {player_hand}")
    print(f"Your score: {player_score}")

    print(f"Computer cards: {dealer_hand}")
    print(f"Computer score: {dealer_score}")


    if is_blackjack(dealer_hand) and is_blackjack(player_hand):
        print("Draw 🙃")

    elif is_blackjack(dealer_hand):
        print("Lose, opponent has Blackjack 😱")

    elif is_blackjack(player_hand):
        print("Win with a Blackjack 😎")

    elif player_score > 21:
        print("You went over. You lose 😭")

    elif dealer_score > 21:
        print("Opponent went over. You win 😁")

    elif player_score > dealer_score:
        print("You win 😎")

    elif dealer_score > player_score:
        print("You lose 😭")

    else:
        print("Draw 🙃")



def game():

    print(art.logo)


    player_hand = []
    dealer_hand = []


    # Deal starting cards
    for i in range(2):
        deal_cards(player_hand)
        deal_cards(dealer_hand)


    player_score = calculate_score(player_hand)
    dealer_score = calculate_score(dealer_hand)


    print(f"Your cards: {player_hand}")
    print(f"Your score: {player_score}")
    print(f"Computer's first card: {dealer_hand[0]}")


    is_game_over = check_game_over(player_hand, dealer_hand)


    # Player and dealer turns
    if not is_game_over:

        is_game_over = player_turn(player_hand)


    if not is_game_over:

        dealer_turn(dealer_hand)


    end_game(player_hand, dealer_hand)



# MAIN

while True:

    play_game = input(
        "Do you want to play a game of Blackjack? Type 'y' or 'n': "
    )

    if play_game == "y":
        game()

    else:
        print("Goodbye!")
        break
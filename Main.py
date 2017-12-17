from Cards import Card
from Rules import Rule
from User import Player


def main():

    # Creating strings to identify computer and user
    user_name = raw_input("Please enter your name: ")

    # Print welcoming message
    print("Hello {}".format(user_name) + ", let's play a game...... called Black Jack!")

    # Initialization for classes
    card_init = Card()
    rule_init = Rule(user_name, card_init.users_cards, card_init.computer_cards)
    player_init = Player(card_init, rule_init, user_name)

    # Calling functions in 'Card'
    card_init.shuffle_deck()

    while True:

        # Check user's actions
        player_init.keyboard_input()

        # If user's deck breaks the rules, end game
        if not rule_init.review_cards(user_name):
            break

        # Let computer withdraw card
        card_init.computer_draw()

        # If computer's deck breaks the rules, end game
        if not rule_init.review_cards("Computer"):
            break


main()

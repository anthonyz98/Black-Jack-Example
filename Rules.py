class Rule:

    def __init__(self, user_name, users_deck, computers_deck):
        self.user_name = user_name
        self.users_deck = users_deck
        self.computers_deck = computers_deck
        self.total_deck_value = 0

    def computer_review(self, element_counter, continue_game):
        """ This function checks whether or not the computer's deck exceeds 21 """
        while element_counter < len(self.computers_deck):
            self.total_deck_value += self.computers_deck[element_counter]

            if self.total_deck_value > 21:
                continue_game = False
                print("Computer loss the game!")
                print("Computer's deck: {}".format(self.computers_deck) + "")
                print("Computer's deck value: {}".format(self.total_deck_value) + "\n")
            elif self.total_deck_value == 21:
                continue_game = False
                print("Computer won the game!")
                print("Computer's deck value: {}".format(self.total_deck_value) + "\n")
            else:
                continue_game = True

            element_counter += 1

        self.total_deck_value = 0

        return continue_game

    def player_review(self, element_counter, continue_game):
        while element_counter < len(self.users_deck):
            self.total_deck_value += self.users_deck[element_counter]

            if self.total_deck_value > 21:
                continue_game = False
                print("{}".format(self.user_name) + ", loss the game!")
            elif self.total_deck_value == 21:
                continue_game = False
                print("{}".format(self.user_name) + ", won the game!")
            else:
                continue_game = True

            element_counter += 1

        print("{}".format(self.user_name) + "'s deck: {}".format(self.users_deck))
        print("Total Value: {}".format(self.total_deck_value) + "\n")

        self.total_deck_value = 0

        return continue_game

    def review_cards(self, reviewer_name):
        """ This function checks whether or not the user's deck exceeds 21 """
        element_counter = 0
        continue_game = False

        if reviewer_name == "Computer":
            return self.computer_review(element_counter, continue_game)
        else:
            return self.player_review(element_counter, continue_game)

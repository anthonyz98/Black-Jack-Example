class Player:

    def __init__(self, card_init, rule_init, user_name):
        self.card_init = card_init
        self.rule_init = rule_init
        self.user_name = user_name

    def keyboard_input(self):

        # Ask for user's input
        user_input = raw_input("\n" + "{}".format(self.user_name) +
                               ", would you like to draw another card? "
                               "Or, stay? Y/n ")

        # First check user's action
        if user_input == "Y":
            self.card_init.draw_cards()
        elif user_input == "n":
            pass
        else:
            print("You entered the wrong input.\n")

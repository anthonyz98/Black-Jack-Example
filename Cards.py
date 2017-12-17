import random

class Card:

    def __init__(self):
        self.suits = ["Hearts", "Spades", "Diamonds", "Clubs"]
        self.deck = {}
        self.users_cards = []
        self.computer_cards = []

    def randomize_values(self):
        """ This function randomizes the order of values when it is called.
            This would be used for every suit.
        """
        values = [0]
        values[0] = random.randint(1, 11)

        while len(values) < 11:
            rand = random.randint(1, 11)

            for iterator in values:
                if rand not in values:
                    values.insert(iterator, rand)
                else:
                    iterator += 1

        return values

    def shuffle_deck(self):
        """ This function assigns a 'value' for each 'key'.
            The 'key' are the elements in 'suits'.
            The 'value' would be assigned by 'randomize_values'
        """
        for i in self.suits:
            self.deck[i] = self.randomize_values()

    def draw_cards(self):
        """ This function generates a random number and associates it to a suit.
            Afterwards, the first element in the 'deck' array would be removed.
        """
        random_suit = random.randint(1, 4)  # 1-4 represents each element in 'suit' array.

        if random_suit == 1:
            suit_name = "Hearts"  # The number 1 is associated to 'Hearts'
            final_name = self.deck[suit_name]  # Locate the 'suit_name' in 'deck' dictionary
            first_value = final_name[0]  # Of the 'key' get the first element
            self.users_cards.append(first_value)  # Add the first element to the 'user's deck'
            del final_name[0]  # Delete the first element of key.

        elif random_suit == 2:
            suit_name = "Clubs"
            final_name = self.deck[suit_name]
            first_value = final_name[0]
            self.users_cards.append(first_value)
            del final_name[0]

        elif random_suit == 3:
            suit_name = "Spades"
            final_name = self.deck[suit_name]
            first_value = final_name[0]
            self.users_cards.append(first_value)
            del final_name[0]

        else:
            suit_name = "Diamonds"
            final_name = self.deck[suit_name]
            first_value = final_name[0]
            self.users_cards.append(first_value)
            del final_name[0]

    def computer_draw(self):
        """ This function generates a random number and associates it to a suit.
            Afterwards, the first element in the 'deck' array would be removed.
        """
        random_suit = random.randint(1, 4)  # 1-4 represents each element in 'suit' array.

        if random_suit == 1:
            suit_name = "Hearts"  # The number 1 is associated to 'Hearts'
            final_name = self.deck[suit_name]  # Locate the 'suit_name' in 'deck' dictionary
            first_value = final_name[0]  # Of the 'key' get the first element
            self.computer_cards.append(first_value)  # Add the first element to the 'user's deck'
            del final_name[0]  # Delete the first element of key.

        elif random_suit == 2:
            suit_name = "Clubs"
            final_name = self.deck[suit_name]
            first_value = final_name[0]
            self.computer_cards.append(first_value)
            del final_name[0]

        elif random_suit == 3:
            suit_name = "Spades"
            final_name = self.deck[suit_name]
            first_value = final_name[0]
            self.computer_cards.append(first_value)
            del final_name[0]

        else:
            suit_name = "Diamonds"
            final_name = self.deck[suit_name]
            first_value = final_name[0]
            self.computer_cards.append(first_value)
            del final_name[0]

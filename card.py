class Card():

    def __init__(self, suit, value, suit_weight):
        self.suit = suit
        self.value = value
        self.suit_weight = suit_weight

    def get_card_value(self):
        return self.value

    def get_card_suit(self):
        return self.suit

    def get_suit_weight(self):
        return self.suit_weight

    def __str__(self):
        return (str(self.get_card_value()) + " of " + str(self.get_card_suit()))

    def __repr__(self):
        return (str(self.get_card_value()) + " of " + str(self.get_card_suit()))

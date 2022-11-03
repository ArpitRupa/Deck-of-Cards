class Card():

    def __init__(self, suit, value, suit_weight):
        self.suit = str(suit)
        self.value = str(value)
        self.suit_weight: int = suit_weight

    def get_card_value(self) -> str:
        return self.value

    def get_card_suit(self) -> str:
        return self.suit

    def get_suit_weight(self) -> int:
        return self.suit_weight

    def __str__(self) -> str:
        return (str(self.get_card_value()) + " of " + str(self.get_card_suit()))

    def __repr__(self) -> str:
        return (str(self.get_card_value()) + " of " + str(self.get_card_suit()))

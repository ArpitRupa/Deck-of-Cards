
class Hand():

    def __init__(self):
        self.cards: list = []

    def get_cards(self):
        return self.cards

    def get_top_card(self):
        return self.cards.pop()

    def add_cards(self, card) -> None:
        self.cards[:0] = card

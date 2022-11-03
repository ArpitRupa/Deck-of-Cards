from core.card import Card


class Hand():

    def __init__(self):
        self.cards: list[Card] = []

    def get_cards(self) -> list[Card]:
        return self.cards

    def get_top_card(self) -> Card:
        return self.cards.pop()

    def add_cards(self, card: Card) -> None:
        self.cards[:0] = card

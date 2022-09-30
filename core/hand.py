
class Hand():

    def __init__(self):
        self.cards = []

    def get_cards(self):
        return self.cards
        
    def get_top_card(self):
        return self.cards.pop()
    
    def add_cards(self, card):
        self.cards[:0] = card
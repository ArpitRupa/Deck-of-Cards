from player import Player
from deck import Deck
from card import Card
from hand import Hand

class Blackjack():

    def __init__(self):
        self.players = []

    def hit_me(self,player):

        return

    def stand(self,player):
        return
    
    def start_game(self):

        blackjack_deck = Deck()

        for player in self.players:
            player.hand.cards.append(blackjack_deck.deal_card())



from player import Player
from deck import Deck
from card import Card
from hand import Hand
import inquirer
import re

class Blackjack():

    def __init__(self):
        self.players = [Player("Dealer", dealer=True)]
        self.activeplayers = []
        self.cardvalues = {"J":10, "Q":10, "K":10, "A":11}
        self.dealercall = False

    def hit_me(self,player, deck):

        #deal card and show player hand
        player.hand.cards.append(deck.deal_card())
        self.show_hand(player)

        #if player hand value > 21, the player is bust and removed from play
        if self.get_hand_value(player.hand.get_cards()) > 21:
            player.bust = True
            self.activeplayers.remove(player)
        return

    def stand(self,player):
        self.activeplayers.remove(player)
    
        #if no more active players, the dealer calls
        if len(self.activeplayers) < 1:
            self.dealercall = True

        return

    def show_hand(self, player):
        player_hand = player.hand.get_cards()

        #dealer always hides one card until the end
        if player.isDealer:
            print(player.name + " is showing " + str(player_hand[1:]) + " for a total value of " + str (self.get_hand_value(player_hand[1:])) )
        else:
            #normal players always show all of their cards
            print(player.name + " is showing " + str(player_hand) + " for a total value of " + str (self.get_hand_value(player_hand) ) )     
        return

    def get_hand_value(self, hand):

        total_val = 0
        #track # of aces to optimize 1 vs 11 value for card
        ace_counter = 0

        for card in hand:
            
            card_value = card.get_card_value()

            if card_value == "A":
                ace_counter += 1

            #if the card is face card or an A, we need to get the value from the class dictionary
            if card_value in self.cardvalues:
                card_value = self.cardvalues.get(card_value)
            
            total_val += card_value

        #check how many aces we have, and if we are in bust territory
        while ace_counter > 0 and total_val > 21:
            ace_counter -= 1
            total_val -= 10

        return total_val

    def check_winner(self):
        return
    
    def start_game(self):

        blackjack_deck = Deck()

        #deal 2 cards to all of the players
        for n in range(2):
            for player in self.players:
                player.hand.cards.append(blackjack_deck.deal_card())

        #all players show their hands
        for player in self.players:
            self.show_hand(player)
            if player.isDealer == False:
                    self.activeplayers.append(player)

        #while there are still players not busted or standed
        while (self.dealercall==False):

            #go through players and determine their actions
            for player in self.activeplayers:
                player_hand = player.hand.get_cards()
                questions = [
                    inquirer.List('action',
                    message="What would " + player.name + " like to do? Current value: " + str (self.get_hand_value(player_hand) ),
                    choices=['Hit Me', 'Stand'],
                        ),
                    ]
                action = inquirer.prompt(questions)['action']
                
                print(player.name + " selected " + str( action ) )

                #perform one of the two actions
                if action == "Hit Me":
                    self.hit_me(player, blackjack_deck)
                else:
                    self.stand(player)
                    



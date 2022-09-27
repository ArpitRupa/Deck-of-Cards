from player import Player
from deck import Deck
import inquirer
import re


class Blackjack():

    def __init__(self):
        self.players = [Player("Dealer", dealer=True)]
        self.activeplayers = []
        self.cardvalues = {"J": 10, "Q": 10, "K": 10, "A": 11}
        self.dealercall = False

    def hit_me(self, player, deck):

        # deal card and show player hand
        card = deck.deal_card()
        print(player.name + " receives a " + str(card))
        player.hand.cards.append(card)
        self.show_hand(player)

        # if player hand value > 21, the player is bust and removed from play
        if self.get_hand_value(player.hand.get_cards()) > 21:
            player.bust = True
            self.activeplayers.remove(player)
        return

    def stand(self, player):
        self.activeplayers.remove(player)

        # if no more active players, the dealer calls
        if len(self.activeplayers) < 1:
            self.dealercall = True

        return

    # runs after all players are standing or busted
    def dealers_turn(self, deck):

        for player in self.players:
            if player.isDealer:
                dealerIndex = self.players.index(player)
                break

        dealer = self.players[dealerIndex]
        dealer_hand = dealer.hand.get_cards()
        print(dealer.name + " shows hidden card. The card was a " +
              str(dealer_hand[0]))
        print("Dealer's current hand: " + str(dealer_hand))

        dealer_active = True
        while dealer_active:
            dealer_value = self.get_hand_value(dealer_hand)
            print(dealer.name + "'s current value: " + str(dealer_value))

            # dealer must stand if hand value is greater than 16
            if dealer_value > 16 and dealer_value < 22:
                print(
                    "Dealer's total is greater than or equal to 17, Dealer must stand.")
                dealer_active = False
            elif dealer_value < 16:
                card = deck.deal_card()
                dealer.hand.cards.append(card)
                print("Dealer receives a " + str(card))
                print("Dealer's current hand: " + str(dealer_hand))
            else:
                print("The dealer busts.")
                dealer.bust = True
                return

        print("Dealer's turn has concluded. Dealer's value is " +
              str(self.get_hand_value(dealer_hand)))

        if self.get_hand_value(dealer_hand) > 21:
            print("The dealer busts.")
            dealer.bust = True
        return

    def show_hand(self, player):
        player_hand = player.hand.get_cards()

        # dealer always hides one card until the end
        if player.isDealer:
            print(player.name + " is showing " +
                  str(player_hand[1:]) + " for a total value of " + str(self.get_hand_value(player_hand[1:])))
        else:
            # normal players always show all of their cards
            print(player.name + " is showing " + str(player_hand) +
                  " for a total value of " + str(self.get_hand_value(player_hand)))
        return

    def get_hand_value(self, hand):

        total_val = 0
        # track # of aces to optimize 1 vs 11 value for card
        ace_counter = 0

        for card in hand:

            card_value = card.get_card_value()

            if card_value == "A":
                ace_counter += 1

            # if the card is face card or an A, we need to get the value from the class dictionary
            if card_value in self.cardvalues:
                card_value = self.cardvalues.get(card_value)

            total_val += card_value

        # check how many aces we have, and if we are in bust territory
        while ace_counter > 0 and total_val > 21:
            ace_counter -= 1
            total_val -= 10

        return total_val

    def check_winner(self):

        winning_players = []
        tie_players = []
        losing_players = []

        players = []

        for player in self.players:
            if player.isDealer:

                dealer_index = self.players.index(player)
                dealer_hand = player.hand.get_cards()
                dealer_value = self.get_hand_value(dealer_hand)
            elif player.bust == False:
                players.append(player)

        # if dealer is bust, remaining active players win
        if self.players[dealer_index].bust:
            print("Dealer has bust, remaining players win!")
            print("Winners: " + str(players))

            return

        for player in players:

            hand = player.hand.get_cards()
            value = self.get_hand_value(hand)
            print(player.name + " " + str(value))

            if value > dealer_value:
                winning_players.append(player)
            elif value == dealer_value:
                tie_players.append(player)

        for player in self.players:
            if player not in winning_players and player not in tie_players:
                losing_players.append(player)

        print("Game has concluded.")

        if len(winning_players) == 0 and len(tie_players) == 0:
            print("All players lose.")
            return

        if len(winning_players) > 0:
            print("Winners: " + str(winning_players))

        if len(tie_players) > 0:
            print("Dealer ties with:" + str(tie_players))

        if len(losing_players) > 0:
            print("Losers: " + str(losing_players))

        return

    def start_game(self):

        blackjack_deck = Deck()

        # deal 2 cards to all of the players
        for n in range(2):
            for player in self.players:
                player.hand.cards.append(blackjack_deck.deal_card())

        # all players show their hands
        for player in self.players:
            self.show_hand(player)
            if player.isDealer == False:
                self.activeplayers.append(player)

        # while there are still players not busted or standed
        while (self.dealercall == False):

            # go through players and determine their actions
            for player in self.activeplayers[:]:
                player_hand = player.hand.get_cards()
                questions = [
                    inquirer.List('action',
                                  message="What would " + player.name + " like to do? Current value: " +
                                  str(self.get_hand_value(player_hand)),
                                  choices=['Hit Me', 'Stand'],
                                  ),
                ]
                action = inquirer.prompt(questions)['action']

                print(player.name + " selected " + str(action))

                # perform one of the two actions
                if action == "Hit Me":
                    self.hit_me(player, blackjack_deck)
                    if player.bust:
                        print("Oops! " + player.name +
                              " has gotten too greedy and busts!")
                else:
                    self.stand(player)

                # dealer call if no active players remaining
                if len(self.activeplayers) < 1:
                    self.dealercall = True

        print("All players are standing or busted...")
        print("Dealer's turn has started...")
        self.dealers_turn(blackjack_deck)

        self.check_winner()

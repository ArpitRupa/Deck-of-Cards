from core.hand import Hand
from core.player import Player
from core.deck import Deck
from games.game import Game
from ui.components.logwindow import LogWindow
from ui.components.blackjackactionbox import BlackjackActionBox


class Blackjack(Game):

    def __init__(self, log_window: LogWindow) -> None:
        super().__init__(log_window)
        self.cardvalues: dict = {"J": 10, "Q": 10, "K": 10, "A": 11}
        self.dealercall: bool = False
        self.deck: Deck = None
        self.ties: list[Player] = []
        self.action_box: BlackjackActionBox = BlackjackActionBox()

    def hit_me(self, player: Player) -> None:

        deck = self.deck

        # deal card and show player hand
        card = deck.deal_card()
        action = player.name + " receives a " + str(card)
        print(action)
        self.log_window.append_to_log(action)
        player.hand.cards.append(card)

        print(player.name + " current value:" +
              str(self.get_hand_value(player.hand.get_cards())))

        # if player hand value > 21, the player is bust and removed from play
        if self.get_hand_value(player.hand.get_cards()) > 21:
            action = player.name + " has bust."
            print(action)
            self.log_window.append_to_log(action)
            player.bust = True
            self.activeplayers.remove(player)
            self.losers.append(player)
        return

    def stand(self, player: Player) -> None:
        self.activeplayers.remove(player)
        player.didStand = True
        action = player.name + " chose to stand."
        print(action)
        self.log_window.append_to_log(action)
        # if no more active players, the dealer calls
        if len(self.activeplayers) < 1:
            self.dealercall = True

        return

    # runs after all players are standing or busted
    def dealers_turn(self, deck: Deck) -> None:

        for player in self.players:
            if player.isDealer:
                dealerIndex = self.players.index(player)
                break

        dealer = self.players[dealerIndex]
        dealer_hand = dealer.hand.get_cards()
        action = (dealer.name + " shows hidden card. The card was a " +
                  str(dealer_hand[0]))
        print(action)
        self.log_window.append_to_log(action)

        print("Dealer's current hand: " + str(dealer_hand))

        dealer_active = True
        while dealer_active:
            dealer_value = self.get_hand_value(dealer_hand)
            print(dealer.name + "'s current value: " + str(dealer_value))
            self.log_window.append_to_log(
                dealer.name + "'s current value: " + str(dealer_value))

            # dealer must stand if hand value is greater than 16
            if dealer_value > 16 and dealer_value < 22:
                print(
                    "Dealer's total is greater than or equal to 17, Dealer must stand.")
                dealer_active = False
                self.log_window.append_to_log("Dealer selected to stand.")
            elif dealer_value <= 16:
                card = deck.deal_card()
                dealer.hand.cards.append(card)
                action = "Dealer receives a " + str(card)
                print(action)
                self.log_window.append_to_log(action)
                print("Dealer's current hand: " + str(dealer_hand))
            else:
                action = "The dealer busts."
                print(action)
                self.log_window.append_to_log(action)
                dealer.bust = True
                return

        action = ("Dealer's turn has concluded. Dealer's value is " +
                  str(self.get_hand_value(dealer_hand)))
        print(action)
        self.log_window.append_to_log(action)

        if self.get_hand_value(dealer_hand) > 21:
            print("The dealer busts.")
            self.log_window.append_to_log("The dealer busts.")
            dealer.bust = True
        return

    def show_hand(self, player: Player) -> None:
        player_hand = player.hand.get_cards()

        # dealer always hides one card until the end
        if player.isDealer:
            action = (player.name + " is showing " +
                      str(player_hand[1:]) + " for a total value of " + str(self.get_hand_value(player_hand[1:])))
        else:
            # normal players always show all of their cards
            action = (player.name + " is showing " + str(player_hand) +
                      " for a total value of " + str(self.get_hand_value(player_hand)))
        print(action)
        self.log_window.append_to_log(action)
        return

    def get_hand_value(self, hand: list) -> int:

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

            total_val += int(card_value)

        # check how many aces we have, and if we are in bust territory
        while ace_counter > 0 and total_val > 21:
            ace_counter -= 1
            total_val -= 10

        return total_val

    def check_winner(self) -> None:

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
            dealer_hand = str(self.players[dealer_index].hand.get_cards())
            print("Dealer cards:" + dealer_hand)
            print("Dealer has bust, remaining players win!")
            self.log_window.append_to_log(
                "Dealer has bust, remaining players win!")
            print("Winners: " + str(players))
            self.log_window.append_to_log("Winners: " + str(players))
            self.winners = str(players)

            return

        for player in players:

            hand = player.hand.get_cards()
            value = self.get_hand_value(hand)
            print(player.name + " " + str(value))

            if value > dealer_value:
                self.winners.append(player)
            elif value == dealer_value:
                self.ties.append(player)
            else:
                self.losers.append(player)

        print("Game has concluded.")

        if len(self.winners) == 0 and len(self.ties) == 0:
            print("All players lose.")
            return

        if len(self.winners) > 0:
            print("Winners: " + str(self.winners))

        if len(self.ties) > 0:
            print("Dealer ties with:" + str(self.ties))

        if len(self.losers) > 0:
            print("Losers: " + str(self.losers))

        return

    def start_game(self):

        blackjack_deck = Deck()
        self.deck = blackjack_deck

        # deal 2 cards to all of the players
        for n in range(2):
            for player in self.players:
                player.hand.cards.append(blackjack_deck.deal_card())

        # all players show their hands
        for player in self.players:
            self.show_hand(player)
            if player.isDealer == False:
                self.activeplayers.append(player)

    def dealer_call(self) -> None:
        print("All players are standing or busted...")
        print("Dealer's turn has started...")
        self.dealers_turn(self.deck)

        self.check_winner()

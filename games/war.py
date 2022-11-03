import copy
from games.game import Game
from core.deck import Deck
from ui.components.UICard import UICard
from ui.components.logwindow import LogWindow
from core.player import Player
from ui.components.buttons.warbutton import WarButton
from ui.components.textbox import Textbox


class War(Game):

    def __init__(self, log_window: LogWindow) -> None:
        super().__init__(log_window)
        # dict of list of cards(value) player(key) played
        self.total_round: dict[Player:list[UICard]] = {}
        # winner of current round
        self.round_winner: Player
        # values for face cards
        self.card_values: dict[str:int] = {"J": 11, "Q": 12, "K": 13, "A": 14}
        self.action_button: WarButton = WarButton(
            "Draw", text_size=50, center=(600, 450))
        self.state = "Draw"
        self.round_count: int = 0
        self.round_limit: int = 0
        self.round_limit_input: Textbox

    # updates the current state of the game and changes button text
    def update_state(self, state: str) -> None:
        self.state = state
        self.action_button = WarButton(
            state, text_size=50, center=(600, 450))

    # returns winner of round
    def battle(self, players: list[Player]) -> Player:
        current_round = []
        winner_index = 0
        self.state = "Battle"

        # shallow copy of players list to parse over
        current_players = copy.copy(players)

        if len(current_players) == 1:
            return current_players[0]

        for player in current_players:

            # check if player is in the current round [used for tie recursion]
            if player not in self.total_round:
                self.total_round[player] = []

            card = player.hand.get_top_card()
            card_value = card.get_card_value()

            if card_value in self.card_values:
                card_value = self.card_values.get(card_value)
            self.total_round[player].append(card)
            current_round.append((player.name, int(card_value)))

        # max from the cards in the list of tuples
        winning_card = max(current_round, key=lambda item: item[1])[1]

        # indicies of players with current highest card
        win_card_indicies = []

        print(current_round)
        # loop through the current round and find players who played highest card
        for card in current_round:
            if card[1] == winning_card:
                win_card_indicies.append(current_round.index(card))

        # check if there are any ties
        if len(win_card_indicies) > 1:

            tie_players = []

            for index in win_card_indicies[:]:

                # all tie players need to put down 4 cards in the event of a tie

                player = current_players[index]
                # check if players have more than 5 cards remaining (4 + 1 playable)
                if (len(player.hand.get_cards()) < 5):

                    # if not the player loses
                    print(player.name + " does not have enough cards for the tie.\n" +
                          player.name + " has been removed from the game!")

                    self.log_window.append_to_log(
                        player.name + " does not have enough cards for the tie.")

                    # all of the player's card to the pile
                    self.total_round[player].extend(
                        player.hand.get_cards())

                    # remove player from active players
                    self.remove_player(player)
                    player.bust = True
                else:
                    # pop 4 cards into the current round
                    for c in range(3):
                        self.total_round[player].append(
                            player.hand.get_top_card())

                    # add player to the "tie round"
                    tie_players.append(player)

            # run battle again with tie players
            return self.battle(tie_players)

        else:
            winner_index = win_card_indicies[0]
            self.round_winner = current_players[winner_index]

            self.log_window.append_to_log(
                str(self.round_winner) + " wins the round!")

            print(str(self.round_winner) + " wins the round!")
            return self.round_winner

    # remove players who have 0 cards remaining in their hands
    def remove_players(self) -> None:

        for player in self.active_players[:]:

            if len(player.hand.get_cards()) < 1:

                print(player.name + " does not have any cards remaining." +
                      player.name + " has been removed from the game!")

                self.log_window.append_to_log(
                    player.name + " does not have any cards remaining.")
                self.remove_player(player)
                player.bust = True

        return

    # collect all the cards and add them to the "hand" of the winner at the index

    def collect(self) -> None:

        winner = self.round_winner
        # convert from dict to total round
        total = [card for player in self.total_round.values()
                 for card in player]

        print("Cards to collect: " + str(total))

        self.log_window.append_to_log("Cards to collect: " + str(total))

        # add cards to winners hand
        winner.hand.add_cards(total)

        # remove players with 0 cards remaining from the game
        self.remove_players()

        # reset the cards in the pile to prep for new round
        self.total_round.clear()

        self.round_count += 1

        # end game after 500 rounds; winner has most cards
        if self.round_count > self.round_limit:
            winner = max(self.active_players,
                         key=lambda item: len(item.hand.get_cards()))
            for player in self.active_players:
                if player is not winner:
                    self.remove_player(player)

        return

    def start_game(self):
        print("Started war with players: " + str(self.players))

        war_deck = Deck()

        # split the deck into X close to equal as possible groups; X=# of players
        while (war_deck.count > 0):

            for player in self.players:

                if war_deck.count < 1:
                    break
                card = war_deck.deal_card()
                player.hand.cards.append(card)
        self.active_players = self.players

    def remove_player(self, player: Player):
        self.losers.append(player.name)
        self.log_window.append_to_log(
            player.name + " has been removed from the game!")
        self.active_players.remove(player)

        return

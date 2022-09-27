from gc import collect
import copy
from deck import Deck
class War():

    def __init__(self):
        #active players
        self.players = []
        #cards in the current "winnable" round
        self.total_round = []
        #values for face cards
        self.card_values = {"J": 11, "Q":12, "K":13, "A":14}


    #returns winner of round
    def battle (self, players):
        current_round = []
        winner_index = 0
        #shallow copy of players list to parse over
        current_players = copy.copy(players)

        if len (current_players) == 1:
            return current_players[0]


        for player in current_players:

            card =player.hand.get_top_card()
            card_value = card.get_card_value()

            if card_value in self.card_values:
                card_value = self.card_values.get(card_value)
            self.total_round.append(card)
            current_round.append((player.name, card_value))
        
        #max from the cards in the list of tuples
        winning_card = max(current_round, key=lambda item:item[1])[1]

        #indicies of players with current highest card
        win_card_indicies = []

        print(current_round)
        #loop through the current round and find players who played highest card
        for card in current_round:
            if card[1] == winning_card:
                win_card_indicies.append(current_round.index(card))

        #check if there are any ties
        if len (win_card_indicies) > 1:
            
            tie_players = []

            for index in win_card_indicies[:]:
                
                #all tie players need to put down 4 cards in the event of a tie

                player = current_players[index]
                #check if players have more than 5 cards remaining
                if ( len(player.hand.get_cards()) < 5 ) :
                    
                    #if not the player loses
                    print(player.name + " does not have enough cards for the tie.\n" + player.name + " has been removed from the game!")

                    #all of the player's card to the pile
                    self.total_round.extend(player.hand.get_cards())

                    #remove player from active players
                    self.players.remove(player)
                else:
                    #pop 4 cards into the current round
                    for c in range(4):
                        self.total_round.append(player.hand.get_top_card())

                    #add player to the "tie round"
                    tie_players.append(player)

            #run battle again with tie players
            return self.battle(tie_players)

        else:
            winner_index = win_card_indicies[0]
            return current_players[winner_index]
        

    #remove players who have 0 cards remaining in their hands
    def remove_players(self) : 

        for player in self.players[:]:

            if len(player.hand.get_cards()) < 1:
                
                print(player.name + " does not have any cards remaining.\n" + player.name + " has been removed from the game!")
                self.players.remove(player)


    #collect all the cards and add them to the "hand" of the winner at the index
    def collect (self, winner):

        print(str(winner) + " wins the round!\n" + "Cards to collect: " +  str(self.total_round) )

        #add cards to winners hand
        winner.hand.add_cards(self.total_round)

        #remove players with 0 cards remaining from the game
        self.remove_players()

        #reset the cards in the pile to prep for new round
        self.total_round.clear()

        return


    def start_game(self):
        print("Started war with players: " + str(self.players))

        war_deck = Deck()

        #split the deck into X equal groups, X=# of players
        while (war_deck.count > 0):

            for player in self.players:

                if war_deck.count < 1:
                    break
                card = war_deck.deal_card()
                player.hand.cards.append(card)


        while len(self.players) > 1:
            #battle each round to find winner
            winner = self.battle(self.players)
            #winner collects the cards
            self.collect(winner)
            print("CURRENT CARD COUNTS: ")

            for player in self.players:
                print( player.name + ": " + str(len(player.hand.get_cards())) )
        
        print("Game Over\n" + "Winner is: " + str(self.players[0]) )

        return
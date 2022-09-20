from card import Card

class Deck():
    def __init__(self):
        self.suits = ["clubs", "hearts", "spades", "diamonds"]
        self.count = 52
        self.deck = self.create_deck()
        
        


    def create_deck(self):

        deck = []

        #13 cards per a suit
        for i in range(1, 14):
            
            #card value is not int if > 10
            match i:
                case 11:
                    value = "J"
                
                case 12:
                    value = "Q"

                case 13:
                    value = "K"

                case defaut:
                    value = i

            #each suit has one card per a value
            for suit in self.suits:
                deck.append(Card(suit,value))
    
        return deck

    
from turtle import rt
from card import Card
import random

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

    def shuffle(self) :


        midpoint = self.count//2

        #maybe a better way to do shuffle count
        shuffle_count = self.count

        for i in range(shuffle_count):
            
            front_half = random.randint(0,midpoint)
            back_half = random.randint(midpoint+1, self.count-1)

            temp = self.deck[front_half]

            self.deck[front_half] = self.deck[back_half]
            self.deck[back_half] = temp

        return

    def deal_card(self):

        card = self.deck.pop()
        #count of cards in deck reduced by 1 when card is dealt
        self.count -= 1

        print("Dealer deals a " + card.__str__() )

        # print(self.count)

        #just pop from the top of the list to deal
        return card

    def deal_one_card(self):

        #maybe add a try and exception here later
        if self.count < 1:
            print ("No more cards to deal")
            return

        return self.deal_card()
    
    def sort_deck():
        return
    
    def __str__(self):

        deck = []
        for i in self.deck:
            deck.append(i.__str__())
        
        return  ("\n".join(deck))

deck1 = Deck()

# print(deck1.deck)

# for i in range (53):
#     deck1.deal_one_card()

deck1.shuffle()

print(deck1)
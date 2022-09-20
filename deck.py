from turtle import rt
from card import Card
import random

class Deck():
    def __init__(self):
        self.suits = [("diamonds",1), ("clubs",3), ("hearts",2), ("spades",4)]
        self.count = 52
        self.deck = self.create_deck()

    def create_deck(self):

        deck = []

        #13 cards per a suit
        for i in range(1, 14):
            
            #card value is not int if > 10 or is equal to 1
            match i:
                case 1:
                    value ="A"

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
                deck.append(Card(suit[0],value,suit[1]))
    
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


    def merge(self, A, B):
    
        sorted = []
        
        while (len (A) > 0 and len(B) > 0):
            
            valA = A[0].get_card_value()
            valB = B[0].get_card_value()

            match valA:
                case "A":
                    valA = 1
                case "J":
                    valA = 11
                case "Q":
                    valA = 12
                case "K":
                    valA = 13
            
            match valB:
                case "A":
                    valB = 1
                case "J":
                    valB = 11
                case "Q":
                    valB = 12
                case "K":
                    valB = 13


            if valA > valB:
                sorted.append(B[0])
                B.pop(0)

            # elif valA == valB:
            #     if A[0].get_suit_weight() > B[0].get_suit_weight():
            #         sorted.append(B[0])
            #         B.pop(0)
            else:
                sorted.append(A[0])
                A.pop(0)
                
        while len(A) > 0:
            sorted.append(A[0])
            A.pop(0)
        
        while len(B) > 0:
            sorted.append(B[0])
            B.pop(0)
    
        return sorted


    def mergesort(self, cards):
        
        if len(cards) == 1:
            return cards
        
        half = int(len(cards)/2)
        arrayA = cards[:half]
        arrayB = cards[half:]
        
        arrayA = self.mergesort( list (arrayA) )
        arrayB = self.mergesort( list (arrayB) )
        
        return self.merge( arrayA, arrayB)

    
    #order should be number value followed by spade, clubs, hearts, diamond
    def sort_deck(self):

        print ("Starting Sort......")
        self.deck = self.mergesort(self.deck)

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
# print(deck1.deck[0])
# print(deck1.deck[0].get_suit_weight())

# deck1.sort_deck()

# print(deck1)
from hand import Hand

class Player():

    def __init__(self, name, dealer=False):
        self.name = name
        self.hand = Hand()
        self.bust = False
        self.isDealer = dealer
        self.didStand = False
    
    def __repr__(self):
        return ( self.name )



    

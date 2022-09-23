class Card():

  def __init__(self, suit, value, suitweight):
    self.suit = suit
    self.value = value
    self.suitWeight = suitweight

  def get_card_value(self):
    return self.value
  
  def get_card_suit(self):
    return self.suit

  def get_suit_weight(self):
    return self.suitWeight

  def __str__(self):
    return ( str(self.get_card_value()) + " of " + str(self.get_card_suit()) )

  def __repr__(self):
    return ( str(self.get_card_value()) + " of " + str(self.get_card_suit()) )
    
# card1= Card("club", "queen")

# print(card1.suit)
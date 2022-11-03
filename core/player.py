from core.hand import Hand


class Player():

    def __init__(self, name, dealer=False):
        self.name: str = name
        self.hand: Hand = Hand()
        self.bust: bool = False
        self.isDealer: bool = dealer
        self.didStand: bool = False

    def __repr__(self) -> str:
        return (self.name)

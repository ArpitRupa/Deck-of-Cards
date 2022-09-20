# Deck-of-Cards
A set of classes that represent a deck of poker-style playing cards. (Fifty-two playing cards in four suits: hearts, spades, clubs, diamonds, with face values of Ace, 2-10, Jack,
Queen, and King.)

Within one of the classes I provide two operations:
1. shuffle() Shuffle returns no value, but results in the cards in the deck being randomly permuted.

2. dealOneCard (This function returns one card from the deck to the caller. Specifically, a call to shuffle followed by 52 calls to dealOneCard results in the caller being provided all 52 cards of the deck in a random order. If the caller then makes a 53rd call dealOneCard(), no card is dealt.

# Deck-of-Cards
A set of classes that represent a deck of poker-style playing cards. (Fifty-two playing cards in four suits: hearts, spades, clubs, diamonds, with face values of Ace, 2-10, Jack, Queen, and King.)

I created two classes to represent my deck, a `Card` class and a `Deck` Class.

The **`Card`** class has class variables: 
- `value` stores the value of the card: [A, 2, 3...Q, K]
- `suit` stores the suit of the card [Spade, clubs, hearts, diamond]
- `suit_weight` stores the weight value of the suit [1,2,3,4]


The **`Deck`** class has class variables:
- `suits` holds a list of suit tuples [("diamonds",1), ("clubs",3), ("hearts",2), ("spades",4)]
- `count` a count of the current number of cards in the deck
- `deck` a list of cards (objects) in the deck

Within the deck class I provide the following operations:
1. **shuffle()** 
    Shuffle returns no value, but results in the cards in the deck being randomly permuted. Shuffle is called in the intialization of the deck class.

2. **deal_card()**
    This function returns one card from the deck to the caller and removes the card from the deck.

3. **sort_deck()**
    This function will utilize merge sort to sort the cards in ascending order by suits and value such that:
```
(A of spades, A of clubs, A of hearts, A of diamonds ... K of Diamonds)
```

## Games

Inside of the program is the option to play games. Simply run `start.py` and the console will guide you through the process. Currently I have supported 2-8 players for each game, and the ability of players to provide a input to provide their names.

Currently I have implemented Blackjack.

### Blackjack

Blackjack is implemented by using a `Blackjack` class to represent an active game. In addition, I created a `Player` class to represent the players and a `Hands` class to represent their hands.

The **`Blackjack`** class has class variables:

- `players` which contains all players and is initalized with a Dealer player

- `activeplayers` varible to identify current players in the game that have not bust or standed

- `cardvalues` a dictionary to reference face card values

- `dealercall` a boolean that is used to check the if there are any active players

The **``Player``** class has the class variables:

- `name` which contains the name of the player

- `hand` contains a `Hand` object for the player

- `bust` boolean that stores the status of if the player has bust

- `isDealer` boolean that stores if the player is a Dealer [default is False]

- `didStand` boolean that checks if the player has decided to stand yet

The **``Hand``** class has the class variables:

- `cards` a list of the cards in the hand


In addition, the `Blackjack` class has several methods to help with the game.

- `hit_me` will deal a card to a player, show the card, and print the player's current hand value
- `stand` removes the player from the `activeplayers` list and checks to see if `dealercall` should be made active
- `dealers_turn` runs after all players are removes from the `activeplayers` list. Shows the dealer's "hidden" card and continues to give the dealer cards until their value is greater than or equal to 17 OR they bust.
- `show_hand` shows 1 all cards but the "hidden card" if the player is a dealer. Shows all of the player's cards otherwise.
- `get_hand_value` returns the numerical value of the hand
- `check_winner` runs at the end of the game. Checks values of players and dealer and returns a list of winners, losers, and players who tied with the dealer.
- `start_game` main method of the class. Starts the game, and asks players for their action (hit or stand). Runs `dealers_turn` and `check_winner` at the end.



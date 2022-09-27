from blackjack import Blackjack
from player import Player
from war import War
import inquirer

def main():
    
    game = ""
    questions = [
                    inquirer.List('game',
                    message="What game would you like to play?",
                    choices=['Blackjack', 'War'],
                        ),
                    ]
    game = inquirer.prompt(questions)['game']

    match game:
        case "Blackjack":
            game = Blackjack()
        case "War":
            game = War()

    number_of_players = int(input("How many players are playing? \n"))

    if type(number_of_players) != type(5) or number_of_players < 2 or number_of_players > 8:
        print ("error...the input value must be an integer between 2-8 \n")
        return

    for i in range(number_of_players) :

        name = input( "Enter name for Player " + str(i+1) +" \n")
        game.players.append(Player(name))

    game.start_game()




if __name__ == "__main__":
    main()
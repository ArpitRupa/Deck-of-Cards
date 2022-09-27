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

    # get number of players

    is_valid = False

    while is_valid is False:
        number_of_players = input("How many players are playing? \n")

        if number_of_players.strip().isdigit() and int(number_of_players) < 9:
            is_valid = True
        else:
            print("error...the input value must be an integer between 2-8 \n")

    # get names of players
    for i in range(int(number_of_players)):

        valid_name = False

        while valid_name == False:

            name = input("Enter name for Player " + str(i+1) + " \n")

            if len(name) > 0:
                valid_name = True

        game.players.append(Player(name))

    game.start_game()


if __name__ == "__main__":
    main()

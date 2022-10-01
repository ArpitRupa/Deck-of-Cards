from ui.splashscreen import Splashscreen
from ui.startwindow import start_window
from ui.gamewindow import Window
from ui.uiconfig import WIDTH, HEIGHT, scale, scale_aspect, GREY, create_text_surface
from games.blackjack import Blackjack
from textbox import Textbox
import pygame
import os


class DeckOfCards:

    def __init__(self) -> None:

        # stores name of selcted game
        self.game_title = ""

        self.FPS = 60
        self.game_clock = pygame.time.Clock()

        # window background 1920 x 1080
        self.table = scale_aspect(pygame.image.load(os.path.join(
            "Assets", "items", "table_top.png")).convert_alpha(), scale)
        self.table_rect = self.table.get_rect(center=(WIDTH/2, HEIGHT/2))

        # states for game intialization
        self.get_num_players = True

        # how many players
        self.num_players = 0
        # names of players
        self.players = []

        self.events = None

    # render the background

    def render_background(self, window):
        window.window.fill(GREY)
        window.window.blit(self.table, self.table_rect)

    def start_blackjack(self, window, game):

        self.render_background(window)
        # num_players.render_textbox(window.window)

        # create textbox to get num of players
        if self.num_players == 0:
            print("is none")
            num_players = Textbox(520, 450, 300, 100, input_type="int")
            # run it once
            self.num_players = num_players

        for event in game.events:
            self.num_players.handle_event(event)

        self.num_players.update()
        self.num_players.draw(window.window)
        game_title = create_text_surface(
            self.game_title, 100)
        ask_num_players = create_text_surface(
            "How many players are playing?", 75)
        window.window.blit(game_title, (435, (50/600)*HEIGHT))
        window.window.blit(
            ask_num_players, (225, (180/600)*HEIGHT))

        pygame.display.flip()

        return

    def start_war(self, window):
        self.render_background(window)
        # window.window.blit(war_text, ((200/800)*WIDTH, (400/600)*HEIGHT))
        return


def main():
    pygame.init()

    window = Window("Deck of Cards")
    splash_screen = Splashscreen()
    game = DeckOfCards()
    num_players = Textbox(520, 450, 300, 100)

    RUN = True

    # game loop
    while RUN:
        game.game_clock.tick(game.FPS)

        game.events = pygame.event.get()
        for event in game.events:
            if event.type == pygame.QUIT:
                RUN = False

        # continue displaying splash screen if no game is selected
        if game.game_title == "":
            start_window(window, splash_screen, game)
        # else start the game that has a the value "True" in the dictionary
        elif game.game_title == "Blackjack":
            game.start_blackjack(window, game)
        elif game.game_title == "War":
            game.start_war(window)

    pygame.quit()


if __name__ == "__main__":
    main()

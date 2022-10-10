from multiprocessing import Event
import os
import pygame
from textbox import Textbox
from ui.splashscreen import Splashscreen
from ui.startwindow import start_window
from ui.gamewindow import Window
from ui.uiconfig import WIDTH, HEIGHT, scale, scale_aspect, GREY, create_text_surface
from UIPlayer import UIPlayer


class DeckOfCards:

    def __init__(self) -> None:

        # stores name of selcted game
        self.game_title: str = ""

        self.FPS: int = 60
        self.game_clock = pygame.time.Clock()

        # window background 1920 x 1080
        self.table = scale_aspect(pygame.image.load(os.path.join(
            "Assets", "items", "table_top.png")).convert_alpha(), scale)
        self.table_rect = self.table.get_rect(center=(WIDTH/2, HEIGHT/2))

        # states for game intialization
        self.num_players_text: bool = None
        self.got_count: bool = False

        # how many players
        self.player_count: int = 0
        # dict of players
        self.player_dict = {}
        # track active player's text box
        self.active_player: int = 1

        # store events of game
        self.events = None
        # state to help know when we're done getting inputs
        self.got_all_input: bool = False
        # state to only set coords for players once
        self.coords_set: bool = False

    # render the background

    def render_background(self, window):
        window.window.fill(GREY)
        window.window.blit(self.table, self.table_rect)

    def render_title(self, window):
        game_title = create_text_surface(
            self.game_title, 100)
        title_rect = game_title.get_rect()
        title_rect.midbottom = (WIDTH/2, HEIGHT*.17)
        window.window.blit(game_title, title_rect)

    def initalize_game(self, window):

        self.render_background(window)
        self.render_title(window)

        if not self.got_all_input:
            active_player = self.active_player
            # create textbox to get num of players
            if self.num_players_text is None:
                num_players = Textbox(520, 450, 300, 100, input_type="int")
                # run it once
                self.num_players_text = num_players

            #####
            #####
            # need to add player count boundss
            #####
            #####
            if self.num_players_text.valid_input() and not self.got_count:
                self.player_count = int(self.num_players_text.text)
                self.got_count = True
                for i in range(self.player_count):
                    self.player_dict[i+1] = UIPlayer()

            # only ask for num of players and render text box if we have not got the count
            if not self.got_count:
                for event in self.events:
                    self.num_players_text.handle_event(event)
                ask_num_players = create_text_surface(
                    "How many players are playing?", 75)
                self.num_players_text.update()
                self.num_players_text.draw(window.window)
                window.window.blit(
                    ask_num_players, (225, (180/600)*HEIGHT))

            # output error text if input was not numerical int
            if not self.num_players_text.valid_enter:
                error_text = create_text_surface(
                    "Please prvoide an integer value.", 50, "firebrick2")
                window.window.blit(error_text, (350, 575))

            # no empty inputs
            if self.num_players_text.text_was_empty:
                error_text = create_text_surface(
                    "Input cannot be empty.", 50, "firebrick2")
                window.window.blit(error_text, (390, 525))

            # render text box for each player input
            if self.player_count > 0 and self.active_player <= self.player_count:
                current_player = self.player_dict[active_player]

                # only make textbox if th UIPlayer object does not have a textbox
                if current_player.input_text is None:
                    player_text = Textbox(500, 450, 300, 100)
                    current_player.input_text = player_text

                # only run while we have not got the name of the current player
                if not current_player.got_name and self.got_count:
                    for event in self.events:
                        current_player.input_text.handle_event(event)
                    ask_player_name = create_text_surface(
                        "Enter Name of Player " + str(active_player), 75)
                    current_player.input_text.update()
                    current_player.input_text.draw(window.window)
                    window.window.blit(
                        ask_player_name, (300, (180/600)*HEIGHT))
                    current_player.set_player_number(int(active_player))

                if current_player.input_text.valid_input():
                    current_player.gotname = True
                    self.player_dict[active_player].name = current_player.input_text.text
                    self.active_player += 1

                    if self.active_player > self.player_count:
                        self.got_all_input = True
        else:
            if self.got_all_input:
                if not self.coords_set:
                    for i in self.player_dict:
                        self.player_dict[i].update_name_surface()
                        self.player_dict[i].set_ui_coordinates()
                    self.coords_set = True
                if self.game_title == "Blackjack":
                    self.run_blackjack(window)
                elif self.game_title == "War":
                    self.run_war(window)

        pygame.display.flip()

        return

    def run_blackjack(self, window):
        self.render_background(window)
        self.render_title(window)
        for i in self.player_dict:
            self.player_dict[i].display_name(window)
        return

    def run_war(self, window):
        self.render_background(window)
        self.render_title(window)
        return


def main():
    pygame.init()

    window = Window("Deck of Cards")
    splash_screen = Splashscreen()
    game = DeckOfCards()

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
        # else initalize the game (get some inputs)
        else:
            game.initalize_game(window)

    pygame.quit()


if __name__ == "__main__":
    main()

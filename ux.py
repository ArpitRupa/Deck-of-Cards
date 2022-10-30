import os
import pygame
from playagainbutton import PlayAgainButton
from games.blackjack import Blackjack
from textbox import Textbox
from blackjackactionbox import BlackjackActionBox
from ui.splashscreen import Splashscreen
from ui.startwindow import start_window
from ui.gamewindow import Window
from ui.uiconfig import WIDTH, HEIGHT, scale, scale_aspect, GREY, create_text_surface
from UIPlayer import UIPlayer
from logbutton import LogButton
from gameoverwindow import GameOverWindow


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
        self.player_dict: dict = {}
        # track active player's text box
        self.active_player: int = 1

        self.current_player: UIPlayer
        self.prev_player: UIPlayer

        # store events of game
        self.events: pygame.event = None
        # state to help know when we're done getting inputs
        self.got_all_input: bool = False
        # state to only set coords for players once
        self.coords_set: bool = False
        self.action_box = None

        self.log_button: LogButton = LogButton(
            name="Logs", text_size=60, center=(90, 850))

        self.play_again_button: PlayAgainButton = PlayAgainButton(
            "Play Again", text_size=75, center=(600, 800))

        self.game = None
        self.game_started: bool = False
        self.game_over: bool = False

        self.game_over_window: GameOverWindow = GameOverWindow()

        self.rerender: bool = True

        self.play_again: bool = False

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

        if not self.got_all_input:
            self.render_background(window)
            self.render_title(window)
            active_player = self.active_player
            # create textbox to get num of players
            if self.num_players_text is None:
                num_players = Textbox(520, 450, 300, 100, input_type="int")
                # run it once
                self.num_players_text = num_players

            # check if the input is num and valid
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
                    "Please prvoide an integer value between 2-8.", 50, "firebrick2")
                window.window.blit(error_text, (250, 575))

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

                # check if the player name is valid
                if current_player.input_text.valid_input():
                    current_player.gotname = True
                    self.player_dict[active_player].name = current_player.input_text.text
                    self.active_player += 1

                    if self.active_player > self.player_count:
                        self.got_all_input = True
        else:
            if self.got_all_input:
                if self.game_title == "Blackjack":
                    self.run_blackjack(window)
                elif self.game_title == "War":
                    self.run_war(window)

        pygame.display.flip()

        return

    # set coords for UIPlayers
    def init_table(self) -> None:
        if not self.coords_set:
            for i in self.player_dict:
                self.player_dict[i].update_name_surface()
                self.player_dict[i].set_ui_coordinates()
            self.coords_set = True

    def run_blackjack(self, window) -> None:
        # run once when game hasn't started
        if not self.game:
            self.render_background(window)
            self.render_title(window)
            self.game = Blackjack(self.log_button.log_window)

            # create and add dealer to the list of players
            self.player_dict[0] = UIPlayer("Dealer", dealer=True)
            self.game.players.append(self.player_dict[0])

            # set coords for UIplayers
            self.init_table()

            # append all players to game list of players
            for i in self.player_dict:
                self.player_dict[i].display_name(window)
                if i > 0:
                    self.game.players.append(self.player_dict[i])

            # start the game
            self.game.start_game()

            self.current_player = self.game.activeplayers[0]
            self.prev_player = self.game.activeplayers[1]
            player = self.current_player
            self.action_box = BlackjackActionBox(player.name)
            self.action_box.update_value(
                self.game.get_hand_value(player.hand.get_cards()))

        # re-render only if UI changes [new card/log window]
        if self.rerender:
            self.render_background(window)
            self.render_title(window)

            for player in self.game.players:

                # display all player names
                player.display_name(window)

                # render the cards of the players
                player.create_UI_cards(self.game.dealercall)
                for card in player.ui_cards:
                    card.display_cards(window)
            self.rerender = False

        game = self.game

        # draw action box
        self.action_box.draw(window)
        # draw log button for game
        self.log_button.draw(window, events=self.events)

        # run if there are players active outside of the dealer

        if not game.dealercall:
            if self.current_player == self.prev_player:
                # update the index of current player
                current_index = self.active_player + 1
                if current_index >= len(game.activeplayers):
                    self.current_player = game.activeplayers[0]
                else:
                    self.current_player = game.activeplayers[current_index]

                player = self.current_player
                # update UI elements in action box
                self.action_box.update_player(
                    player.name)
                self.action_box.update_value(
                    self.game.get_hand_value(player.hand.get_cards()))

            self.active_player = game.activeplayers.index(self.current_player)
            # get the player action
            for event in self.events:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    # check if mouse is currently over the hit button
                    if self.action_box.hit_button.hover:
                        game.hit_me(self.current_player)
                        # update the screen if the player busts
                        self.current_player.display_name(window)
                        self.prev_player = self.current_player

                        # True to re-render cards next loop
                        self.rerender = True

                    # check if mouse is currently over the stand button
                    elif self.action_box.stand_button.hover:
                        game.stand(self.current_player)
                        # update the screen when player stands
                        self.current_player.display_name(window)
                        self.prev_player = self.current_player

            if len(game.activeplayers) < 1:
                self.rerender = True
                game.dealercall = True

        elif not self.game_over:
            self.game.dealer_call()
            self.rerender = True
            self.game_over = True

        # game over

        if self.game_over:
            winners_text = "Winners: " + "".join(str(game.winners))
            tie_text = "Tie with Dealer: " + "".join(str(game.ties))
            loser_text = "Losers: " + "".join(str(game.losers))

            self.game_over_window.set_winner_text(winners_text)
            self.game_over_window.set_tie_text(tie_text)
            self.game_over_window.set_loser_text(loser_text)

            self.game_over_window.draw(window)
            for event in self.events:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if self.play_again_button.hover:
                        self.play_again = self.play_again_button.handle_click(
                            self.play_again_button)

            self.play_again_button.draw(window)

        for event in self.events:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if self.log_button.hover:
                    self.log_button.handle_click()
                    self.rerender = True

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

        if game.play_again:
            game = DeckOfCards()

        pygame.display.update()

    pygame.quit()


if __name__ == "__main__":
    main()

from ui.splashscreen import Splashscreen
from ui.gamewindow import Window
from ui.uiconfig import WIDTH, HEIGHT, scale, scale_aspect, GREY
from games.blackjack import Blackjack
from textbox import Textbox
import pygame
import os


class DeckOfCards:

    def __init__(self) -> None:

        self.FPS = 60
        self.game_clock = pygame.time.Clock()

        # window background 1920 x 1080
        self.table = scale_aspect(pygame.image.load(os.path.join(
            "Assets", "items", "table_top.png")).convert_alpha(), scale)
        self.table_rect = self.table.get_rect(center=(WIDTH/2, HEIGHT/2))

        # dictionary to store game state
        self.games_selected = {"Blackjack": False, "War": False}

        # check if input-box is clicked
        self.input_box = False

    # render the background

    def render_background(self, window):
        window.window.fill(GREY)
        window.window.blit(self.table, self.table_rect)

    def start_blackjack(self, window, num_players):
        blackjack = Blackjack()

        # num_players.render_textbox(window.window)

        for event in pygame.event.get():
            num_players.handle_event(event)

        # num_players.update()
        self.render_background(window)
        # num_players.draw(window.window)
        pygame.display.flip()
        # window.window.blit(blackjack_text, ((200/800)*WIDTH, (400/600)*HEIGHT))
        # pygame.display.update()
        return

    def start_war(self, window):
        self.render_background(window)
        # window.window.blit(war_text, ((200/800)*WIDTH, (400/600)*HEIGHT))
        return

    def start_window(self, window, splash_screen):
        window.window.fill(GREY)

        # get variables from splashscreen to make it easier to reference
        blackjack_surf, blackjack_rect = splash_screen.blackjack_surf, splash_screen.blackjack_rect
        war_surf, war_rect = splash_screen.war_surf, splash_screen.war_rect

        title_text, instruction_text, blackjack_text, war_text = splash_screen.text[
            "Title"], splash_screen.text["Instruction"], splash_screen.text["Blackjack"], splash_screen.text["War"]

        # LOCATION OF RENDER
        self.render_background(window)
        window.window.blit(
            blackjack_surf, (blackjack_rect[0]-17, blackjack_rect[1]))
        window.window.blit(war_surf, (war_rect[0]-33, war_rect[1]))
        window.window.blit(title_text, ((225/800)*WIDTH, (50/600)*HEIGHT))
        window.window.blit(
            instruction_text, ((300/800)*WIDTH, (180/600)*HEIGHT))
        window.window.blit(blackjack_text, ((200/800)*WIDTH, (400/600)*HEIGHT))
        window.window.blit(war_text, ((530/800)*WIDTH, (400/600)*HEIGHT))

        # hover effect for blackjack icon
        if splash_screen.blackjack_rect.collidepoint(pygame.mouse.get_pos()):
            blackjack_surf.set_alpha(180)
            blackjack_text.set_alpha(140)
        else:
            blackjack_surf.set_alpha(255)
            blackjack_text.set_alpha(255)

        # hover effect for war icon
        if war_rect.collidepoint(pygame.mouse.get_pos()):
            war_surf.set_alpha(180)
            war_text.set_alpha(140)
        else:
            war_surf.set_alpha(255)
            war_text.set_alpha(255)

        # check which game the player clicks on
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                # change state based on which icon is clicked
                if blackjack_rect.collidepoint(pygame.mouse.get_pos()):
                    self.games_selected["Blackjack"] = True
                elif war_rect.collidepoint(pygame.mouse.get_pos()):
                    self.games_selected["War"] = True

        # update the splash-screen
        pygame.display.update()


def main():
    pygame.init()

    window = Window("Deck of Cards")
    splash_screen = Splashscreen()
    game = DeckOfCards()
    num_players = Textbox(450, 450, 300, 100)

    RUN = True

    # game loop
    while RUN:
        # game.game_clock.tick(game.FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                RUN = False

        # continue displaying splash screen if no game is selected
        if all(value == False for value in game.games_selected.values()):
            game.start_window(window, splash_screen)
        # else start the game that has a the value "True" in the dictionary
        elif game.games_selected["Blackjack"]:
            game.start_blackjack(window, num_players)
        elif game.games_selected["War"]:
            game.start_war(window)

    pygame.quit()


if __name__ == "__main__":
    main()

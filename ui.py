from pickle import FALSE
from tkinter import CENTER
from splashscreen import Splashscreen
from gamewindow import Window
from uiconfig import WIDTH, HEIGHT, scale, font_big, font_med, font_small, CARD_HEIGHT, CARD_WIDTH, GREEN, GREY, BLACK, WHITE, LIGHT_GREEN, RED, LIGHT_RED
import pygame
import os


pygame.init()


class DeckOfCards:

    def __init__(self) -> None:
        self.FPS = 60
        self.game_clock = pygame.time.Clock()

        # dictionary to store game state
        self.games_selected = {"Blackjack": False, "War": False}
        # tuple with active as 2nd value in tuple
        self.players = []


# def scale_aspect(image, scale):
#     # https://www.delftstack.com/howto/python-pygame/scale-images-in-pygame/

#     # returns the width and height
#     ext = image.get_rect()[2:4]

#     # multiplier to scale image
#     size = scale

#     image = pygame.transform.scale(
#         image,
#         (int(ext[0]*size), int(ext[1]*size))
#     )

#     return image


def scale_text(size):
    return round((size/480000)*(WIDTH*HEIGHT))


# render the background
def render_table(window):
    window.window.fill(GREY)
    window.window.blit(TABLE, TABLE_RECT)


# title_font = pygame.font.Font(None, scale_text(50))
# instruction_font = pygame.font.Font(None, scale_text(25))
# game_font = pygame.font.Font(None, scale_text(20))


# WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
# pygame.display.set_caption("Deck of Cards")

# icon = pygame.image.load(os.path.join(
#     "Assets", "icon.png")).convert()
# pygame.display.set_icon(icon)

# # used for scaling table and cards
# scale = round((WIDTH/1920 + HEIGHT/1080)/2, 4)

# surfaces
# blackjack = pygame.image.load(os.path.join(
#     "Assets", "games", "blackjack.png")).convert_alpha()
# blackjack = scale_aspect(blackjack, .75)

# war = pygame.image.load(os.path.join(
#     "Assets", "games", "war.png")).convert_alpha()
# war = scale_aspect(war, .75)


# texts
# title_text = title_font.render("Deck of Cards", True, 'Black')
# instruction_text = instruction_font.render("Select a game:", True, "Black")
# blackjack_text = game_font.render("BlackJack", True, "Black")
# war_text = game_font.render("War", True, "Black")


# # rects
# blackjack_rect = blackjack.get_bounding_rect()
# blackjack_rect.midbottom = (WIDTH/3.2, HEIGHT/1.5)


# war_rect = war.get_bounding_rect()
# war_rect.midbottom = (WIDTH/1.46, HEIGHT/1.47)


def start_window(games_selected, window, splash_screen):
    window.window.fill(GREY)

    # get variables from splashscreen to make it easier to reference
    blackjack_surf, blackjack_rect = splash_screen.blackjack_surf, splash_screen.blackjack_rect
    war_surf, war_rect = splash_screen.war_surf, splash_screen.war_rect

    title_text, instruction_text, blackjack_text, war_text = splash_screen.text[
        "Title"], splash_screen.text["Instruction"], splash_screen.text["Blackjack"], splash_screen.text["War"]

    # LOCATION OF RENDER
    render_table(window)
    window.window.blit(
        blackjack_surf, (blackjack_rect[0]-17, blackjack_rect[1]))
    window.window.blit(war_surf, (war_rect[0]-33, war_rect[1]))
    window.window.blit(title_text, ((225/800)*WIDTH, (50/600)*HEIGHT))
    window.window.blit(instruction_text, ((300/800)*WIDTH, (180/600)*HEIGHT))
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
                games_selected["Blackjack"] = True
            elif war_rect.collidepoint(pygame.mouse.get_pos()):
                games_selected["War"] = True

    # update the splash-screen
    pygame.display.update()


def start_blackjack(window):
    render_table(window)
    # window.window.blit(blackjack_text, ((200/800)*WIDTH, (400/600)*HEIGHT))
    pygame.display.update()
    return


def start_war(window):
    render_table(window)
    # window.window.blit(war_text, ((200/800)*WIDTH, (400/600)*HEIGHT))
    pygame.display.update()
    return


def setup_splash():

    return


def main():

    game = DeckOfCards()

    window = Window("Deck of Cards")

    # 1920 x 1080
    TABLE = pygame.image.load(os.path.join(
        "Assets", "items", "table_top.png")).convert_alpha()
    TABLE = scale_aspect(TABLE, scale)

    TABLE_RECT = TABLE.get_rect(center=(WIDTH/2, HEIGHT/2))

    splash_screen = Splashscreen()

    RUN = True

    setup_splash()

    game_clock = pygame.time.Clock()

    # game loop
    while RUN:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                RUN = False

        # continue displaying splash screen if no game is selected
        if all(value == False for value in game.games_selected.values()):
            start_window(game.games_selected, window, splash_screen)
        # else start the game that has a the value "True" in the dictionary
        elif game.games_selected["Blackjack"]:
            start_blackjack(window)
        elif game.games_selected["War"]:
            start_war(window)
        # game_clock.tick(FPS)

    pygame.quit()


if __name__ == "__main__":
    main()

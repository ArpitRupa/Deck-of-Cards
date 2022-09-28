from pickle import FALSE
from tkinter import CENTER
import pygame
import os

pygame.init()

# Margins
MARGIN_LEFT = 230
MARGIN_TOP = 150

# WINDOW SIZE
WIDTH = 1200
HEIGHT = 900

# COLORS
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREY = (110, 110, 110)
GREEN = (0, 255, 0)
LIGHT_GREEN = (0, 120, 0)
RED = (255, 0, 0)
LIGHT_RED = (120, 0, 0)

CARD_HEIGHT, CARD_WIDTH = 185, 131


def scale_aspect(image, scale):
    # https://www.delftstack.com/howto/python-pygame/scale-images-in-pygame/

    # returns the width and height
    ext = image.get_rect()[2:4]

    # multiplier to scale image
    size = scale

    image = pygame.transform.scale(
        image,
        (int(ext[0]*size), int(ext[1]*size))
    )

    return image


def scale_text(size):
    return round((size/480000)*(WIDTH*HEIGHT))


title_font = pygame.font.Font(None, scale_text(50))
instruction_font = pygame.font.Font(None, scale_text(25))
game_font = pygame.font.Font(None, scale_text(20))


WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Deck of Cards")

icon = pygame.image.load(os.path.join(
    "Assets", "icon.png")).convert()
pygame.display.set_icon(icon)

# used for scaling table and cards
scale = round((WIDTH/1920 + HEIGHT/1080)/2, 4)

# surfaces
blackjack = pygame.image.load(os.path.join(
    "Assets", "games", "blackjack.png")).convert_alpha()
blackjack = scale_aspect(blackjack, .75)

war = pygame.image.load(os.path.join(
    "Assets", "games", "war.png")).convert_alpha()
war = scale_aspect(war, .75)


# 1920 x 1080
TABLE = pygame.image.load(os.path.join(
    "Assets", "items", "table_top.png")).convert_alpha()
TABLE = scale_aspect(TABLE, scale)

# texts
title_text = title_font.render("Deck of Cards", True, 'Black')
instruction_text = instruction_font.render("Select a game:", True, "Black")
blackjack_text = game_font.render("BlackJack", True, "Black")
war_text = game_font.render("War", True, "Black")


# rects
blackjack_rect = blackjack.get_bounding_rect()
blackjack_rect.midbottom = (WIDTH/3.2, HEIGHT/1.5)


war_rect = war.get_bounding_rect()
war_rect.midbottom = (WIDTH/1.46, HEIGHT/1.47)

TABLE_RECT = TABLE.get_rect(center=(WIDTH/2, HEIGHT/2))


def start_window(BLACKJACK, WAR):
    WINDOW.fill(GREY)

    # LOCATION OF RENDER
    WINDOW.blit(TABLE, TABLE_RECT)
    # pygame.draw.rect(WINDOW, RED, blackjack_rect)
    # pygame.draw.rect(WINDOW, RED, war_rect)
    WINDOW.blit(blackjack, (blackjack_rect[0]-17, blackjack_rect[1]))
    WINDOW.blit(war, (war_rect[0]-33, war_rect[1]))
    WINDOW.blit(title_text, ((225/800)*WIDTH, (50/600)*HEIGHT))
    WINDOW.blit(instruction_text, ((300/800)*WIDTH, (180/600)*HEIGHT))
    WINDOW.blit(blackjack_text, ((200/800)*WIDTH, (400/600)*HEIGHT))
    WINDOW.blit(war_text, ((530/800)*WIDTH, (400/600)*HEIGHT))

    if blackjack_rect.collidepoint(pygame.mouse.get_pos()):
        blackjack.set_alpha(180)
        blackjack_text.set_alpha(140)
    else:
        blackjack.set_alpha(255)
        blackjack_text.set_alpha(255)

    if war_rect.collidepoint(pygame.mouse.get_pos()):
        war.set_alpha(180)
        war_text.set_alpha(140)
    else:
        war.set_alpha(255)
        war_text.set_alpha(255)

    for event in pygame.event.get():
        # print(pygame.mouse.get_pos())
        if event.type == pygame.MOUSEBUTTONDOWN:
            print("player clicked")
            if blackjack_rect.collidepoint(pygame.mouse.get_pos()):
                print("Player clicked Blackjack")
            elif war_rect.collidepoint(pygame.mouse.get_pos()):
                print("Player clicked War")

    pygame.display.update()


def start_blackjack():
    return


def start_war():
    return


def main():

    # FPS
    FPS = 120

    # game states
    BLACKJACK = False
    WAR = False
    RUN = True

    game_clock = pygame.time.Clock()

    while RUN:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                RUN = False

        if not BLACKJACK and not WAR:
            start_window(BLACKJACK, WAR)
        elif BLACKJACK:
            start_blackjack()
        elif WAR:
            start_war()
        # game_clock.tick(FPS)

    pygame.quit()


if __name__ == "__main__":
    main()

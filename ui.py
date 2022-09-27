import pygame
import os


# Margins
MARGIN_LEFT = 230
MARGIN_TOP = 150

# WINDOW SIZE
WIDTH = 800
HEIGHT = 600

# COLORS
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREY = (110, 110, 110)
GREEN = (0, 255, 0)
LIGHT_GREEN = (0, 120, 0)
RED = (255, 0, 0)
LIGHT_RED = (120, 0, 0)

FPS = 60
CARD_HEIGHT, CARD_WIDTH = 72, 47

A_of_spades = pygame.image.load(os.path.join(
    "Assets", "Cards", "card-spades-1.png"))
card = pygame.transform.scale(A_of_spades, (CARD_WIDTH, CARD_HEIGHT))

WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Deck of Cards")

icon = pygame.image.load('icon.png')
pygame.display.set_icon(icon)


def update_window():
    WINDOW.fill(GREY)

    # LOCATION OF RENDER
    WINDOW.blit(card, (400, 300))
    pygame.display.update()


def main():

    run = True

    game_clock = pygame.time.Clock()

    while run:
        game_clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        update_window()

    pygame.quit()


if __name__ == "__main__":
    main()

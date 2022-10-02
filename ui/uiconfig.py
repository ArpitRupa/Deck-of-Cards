import pygame
import os

# helper methods


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


def create_text_surface(text, size, color="Black"):
    font = pygame.font.Font(None, size)
    return font.render(text, True, color)


def scale_text(size):
    return round((size/480000)*(WIDTH*HEIGHT))


pygame.init()

# WINDOW SIZE
WIDTH = 1200
HEIGHT = 900

scale = round((WIDTH/1920 + HEIGHT/1080)/2, 4)

# COLORS
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREY = (110, 110, 110)
GREEN = (0, 255, 0)
LIGHT_GREEN = (0, 120, 0)
RED = (255, 0, 0)
LIGHT_RED = (120, 0, 0)

CARD_HEIGHT, CARD_WIDTH = 185, 131

# text constants for game
font_big = pygame.font.Font(None, scale_text(50))
font_med = pygame.font.Font(None, scale_text(25))
font_small = pygame.font.Font(None, scale_text(20))

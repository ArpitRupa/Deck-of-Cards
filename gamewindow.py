import pygame
import os
from uiconfig import WIDTH, HEIGHT


class Window:

    def __init__(self, name) -> None:
        self.width = WIDTH
        self.height = HEIGHT
        self.window = pygame.display.set_mode((self.width, self.height))
        self.window_icon = pygame.image.load(os.path.join(
            "Assets", "icon.png")).convert()

        self.setup_window(name)

    def setup_window(self, name):
        pygame.display.set_caption("Deck of Cards")
        pygame.display.set_icon(self.window_icon)
        return

    def set_variables(self):
        return

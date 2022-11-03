import pygame
import os
from ui.uiconfig import WIDTH, HEIGHT


class Window:

    def __init__(self, name: str) -> None:
        self.width = WIDTH
        self.height = HEIGHT
        self.window = pygame.display.set_mode((self.width, self.height))
        self.window_icon = pygame.image.load(os.path.join(
            "Assets", "icon.png")).convert()

        self.setup_window(name)

    def setup_window(self, name: str) -> None:
        pygame.display.set_caption(name)
        pygame.display.set_icon(self.window_icon)
        return

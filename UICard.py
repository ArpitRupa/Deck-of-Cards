import pygame
import os


class UICard():

    def __init__(self) -> None:
        self.value: str
        self.suit: str
        self.image: pygame.surface

    def set_card_image(self) -> None:
        self.image = pygame.image.load(os.path.join(
            "Assets", "Cards", self.suit+"_"+self.value".png")).convert_alpha()

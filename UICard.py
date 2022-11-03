import pygame
import os
from ui.uiconfig import scale_aspect


class UICard():

    def __init__(self, value=0, suit="none") -> None:
        self.value: str = value
        self.suit: str = suit
        self.image: pygame.Surface = self.set_card_image()
        self.rect: pygame.Rect = self.set_pixel_rect()

    def set_card_image(self) -> pygame.Surface:
        if self.value == 0:
            return scale_aspect(pygame.image.load(os.path.join(
                "Assets", "Cards", "BackgroundRed.png")).convert_alpha(), .50)
        else:
            return scale_aspect(pygame.image.load(os.path.join(
                "Assets", "Cards", self.suit+"_"+str(self.value)+".png")).convert_alpha(), .50)

    def set_pixel_rect(self) -> pygame.Surface:
        return self.image.get_bounding_rect()

    def set_card_rect(self) -> pygame.Rect:
        return self.image.get_rect()

    def display_cards(self, window) -> None:
        window.window.blit(self.image, self.rect)

import pygame
import os
from ui.uiconfig import scale_aspect


class UICard():

    def __init__(self, value, suit) -> None:
        self.value: str = value
        self.suit: str = suit
        self.image: pygame.Surface = self.set_card_image()
        self.rect: pygame.Rect = self.set_pixel_rect()
        # self.pixel_rect: pygame.Rect = self.set_pixel_rect()
        # self.trimmed_surface: pygame.Surface = self.set_trimmed_surface()

    def set_card_image(self) -> pygame.Surface:
        return scale_aspect(pygame.image.load(os.path.join(
            "Assets", "Cards", self.suit+"_"+str(self.value)+".png")).convert_alpha(), .50)

    def set_pixel_rect(self) -> pygame.Surface:
        return self.image.get_bounding_rect()

    # def set_trimmed_surface(self) -> pygame.Rect:
    #     return pygame.Surface(self.pixel_rect.size)

    def set_card_rect(self) -> pygame.Rect:
        return self.image.get_rect()

    def display_cards(self, window) -> None:
        window.window.blit(self.image, self.rect)

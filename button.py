import pygame
from ui.uiconfig import GREY, create_text_surface
from ui.gamewindow import Window


class Button():
    def __init__(self, name: str = "Button", fill: tuple = (230, 227, 80), text_size: int = 40, center=(0, 0)) -> None:
        self.name = name
        self.surf: pygame.Surface = self.get_surface(name=name, size=text_size)
        self.rect: pygame.Rect = self.get_rect(center)
        self.fill: tuple = fill
        self.hover: bool = False
        pass

    def get_surface(self, name, size) -> pygame.Surface:
        surf = create_text_surface(name, size)
        return surf

    def get_rect(self, coords: tuple) -> pygame.Rect:
        return self.surf.get_rect(center=coords)

    # creates a border rect for a rect

    def create_outer_rect(self, rect: pygame.Rect, scale: int = 10) -> pygame.Rect:
        outer_rect = rect.copy()

        outer_rect.width = outer_rect.width+scale
        outer_rect.height = outer_rect.height+scale
        outer_rect.x = outer_rect.x - scale/2
        outer_rect.y = outer_rect.y - scale/2

        return outer_rect

    def handle_hover(self) -> None:

        if self.rect.collidepoint(pygame.mouse.get_pos()):
            fill_to_change = GREY
            hover = True
        else:
            fill_to_change = (230, 227, 80)
            hover = False
        self.hover = hover
        self.fill = fill_to_change

        return

    def draw(self, window: Window) -> None:
        outer_rect = self.create_outer_rect(self.rect, scale=12)
        self.handle_hover()

        # draw button border
        pygame.draw.rect(window.window, "Black", outer_rect)

        # fill the button
        pygame.draw.rect(window.window, self.fill, self.rect)

        # display button text
        window.window.blit(self.surf, self.rect)

        return

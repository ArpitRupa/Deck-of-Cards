import pygame
from ui.uiconfig import create_text_surface
from button import Button


class LogButton(Button):

    def __init__(self, name: str = "Button", fill: tuple = (230, 227, 80), text_size: int = 40, center=(0, 0)) -> None:
        super().__init__(name, fill, text_size, center)
        self.render_log: bool = False
        self.log: list[str] = []

    def hand_click(self) -> None:
        self.render_log = not self.render_log

    def draw(self, window) -> None:
        outer_rect = self.create_outer_rect(self.rect, scale=12)
        self.handle_hover()

        # draw button border
        pygame.draw.rect(window.window, "Black", outer_rect)

        # fill the button
        pygame.draw.rect(window.window, self.fill, self.rect)

        # display button text
        window.window.blit(self.surf, self.rect)

import pygame
from ui.uiconfig import create_text_surface
from ui.components.buttons.button import Button
from ui.screens.gamewindow import Window
from ui.components.logwindow import LogWindow


class LogButton(Button):

    def __init__(self, name: str = "Button", fill: tuple = (230, 227, 80), text_size: int = 40, center=(0, 0)) -> None:
        super().__init__(name, fill, text_size, center)
        self.render_log: bool = False
        self.log_window: LogWindow = LogWindow()

    def handle_click(self) -> None:
        self.render_log = not self.render_log

    def draw(self, window: Window, events: list) -> None:
        outer_rect = self.create_outer_rect(self.rect, scale=12)
        self.handle_hover()

        # draw button border
        pygame.draw.rect(window.window, "Black", outer_rect)

        # fill the button
        pygame.draw.rect(window.window, self.fill, self.rect)

        # display button text
        window.window.blit(self.surf, self.rect)

        if self.render_log:
            self.log_window.run = True
            self.log_window.draw(window, events=events)

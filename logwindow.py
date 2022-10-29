import pygame
from ui.gamewindow import Window
import string


class LogWindow():

    def __init__(self) -> None:
        self.logs: list[str] = []
        self.log_surface: pygame.Surface = self.create_log_surface(900)
        self.log_window: pygame.Surface = self.create_log_surface()
        self.scroll: bool = False
        self.run: bool = False
        self.x: int = 30
        self.y: int = 540
        self.scroll_y: int = 0

    def create_log_surface(self, height=278) -> pygame.Surface:
        surf = pygame.Surface((290, height), flags=pygame.SRCALPHA)
        surf.set_alpha(30)
        surf.fill((80, 83, 230))
        return surf

    # called when adding to log list
    def update_inner_window(self) -> None:

        log_surface = self.create_log_surface(900)

        y = 0
        f = pygame.font.SysFont('', 17)
        for l in self.logs[::-1]:
            log_surface.blit(
                f.render(l, True, (255, 255, 255)), (10, y))
            y += 20

        self.log_surface = log_surface
        return

    # add logs to list
    def append_to_log(self, text: str) -> None:
        self.logs.append(text)
        self.update_inner_window()

    def draw(self, window: Window, events: list) -> None:

        window.window.blit(self.log_window, (self.x, self.y))

        scroll_y = self.scroll_y

        for e in events:
            if e.type == pygame.MOUSEBUTTONDOWN:

                # mouse wheel up
                if e.button == 4:
                    scroll_y = min(scroll_y + 15, 0)

                # mousewheel down
                if e.button == 5:
                    scroll_y = max(scroll_y - 15, -400)

            # self.y = scroll_y
            self.scroll_y = scroll_y

        for i in range(120):
            window.window.blit(self.log_window, (self.x, self.y))
            self.log_window.blit(self.log_surface, (0, self.scroll_y))
        # pygame.display.flip()

        return

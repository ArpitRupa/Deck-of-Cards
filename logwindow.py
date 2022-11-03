import pygame
from ui.gamewindow import Window


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

    # render's lines so they do not flow outside of surface
    def render_line(self, surface: pygame.Surface, font: pygame.font.SysFont, color="White") -> None:

        lines = [line for line in self.logs[::-1]]
        words = [word.split(' ')
                 for word in lines]  # 2d array of lines of words

        space = font.size(' ')[0]
        surface_width = self.log_surface.get_width()

        x = 5
        y = 3

        line_number = len(self.logs)

        for line in words:

            line_number_text = font.render(str(line_number), True, "Black")
            surface.blit(line_number_text, (x, y))
            x += line_number_text.get_size()[0] + 3

            for word in line:

                word_surf = font.render(word, True, color)
                word_width, word_height = word_surf.get_size()

                # if length of word is outside of window
                if x + word_width >= surface_width:
                    x = 5  # reset the x pos to beginning of line
                    y += word_height  # adjust y value for next line
                surface.blit(word_surf, (x, y))
                x += word_width + space

            x = 5
            y += word_height + 5
            line_number -= 1

    # called when adding to log list
    def update_inner_window(self) -> None:

        log_surface = self.create_log_surface(900)

        font = pygame.font.SysFont('', 17)

        self.render_line(surface=log_surface, font=font)

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

            self.scroll_y = scroll_y

        for i in range(120):
            window.window.blit(self.log_window, (self.x, self.y))
            self.log_window.blit(self.log_surface, (0, self.scroll_y))

        return

import pygame
from ui.screens.gamewindow import Window
from ui.uiconfig import create_text_surface


class GameOverWindow():

    def __init__(self) -> None:
        self.game_over_text: pygame.Surface = create_text_surface(
            "GAME OVER", 100, "Red")
        self.game_over_window = self.init_window()
        self.winner_text: pygame.Surface = ""
        self.tie_text: pygame.Surface = ""
        self.loser_text: pygame.Surface = ""

    def init_window(self) -> pygame.Surface:
        game_over_window = pygame.Surface((500, 400), flags=pygame.SRCALPHA)
        game_over_window.set_alpha(10)
        game_over_window.fill((80, 83, 230))

        return game_over_window

    def set_winner_text(self, text: str) -> None:
        self.winner_text = text

    def set_tie_text(self, text: str) -> None:
        self.tie_text = text

    def set_loser_text(self, text: str) -> None:
        self.loser_text = text

    def draw_window_border(self, window: Window) -> None:
        rect = self.game_over_window.get_rect(center=(610, 560))
        rect.inflate(3, 3)
        pygame.draw.rect(window.window, "Black", rect, 6)

    def render_results(self) -> None:

        w_x, w_y = 40, 110
        t_x, t_y = 40, 210
        l_x, l_y = 40, 310

        font = pygame.font.SysFont('', 40)

        self.render_line(self.winner_text, (w_x, w_y), font, "Green")
        self.render_line(self.loser_text, (l_x, l_y), font, "Red")
        if self.tie_text != "":
            self.render_line(self.tie_text, (t_x, t_y), font, "Yellow")

    def render_line(self, text: str, start: tuple, font: pygame.font, color="Black") -> None:

        space = font.size(' ')[0]
        max_width = self.game_over_window.get_width()-40

        x = start[0]
        y = start[1]

        for word in text.split():
            word_surf = font.render(word, True, color)
            word_width, word_height = word_surf.get_size()

            # if len of word is outside of window
            if x + word_width >= max_width:
                x = 40  # reset to beginning
                y += word_height  # move render down

            self.game_over_window.blit(word_surf, (x, y))
            x += word_width + space

    def draw(self, window: Window) -> None:

        self.draw_window_border(window)

        for i in range(20):
            window.window.blit(self.game_over_window, (360, 360))
        window.window.blit(self.game_over_text, (400, 400))

        self.render_results()

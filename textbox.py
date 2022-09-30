from sre_parse import WHITESPACE
import pygame
from ui.uiconfig import WHITE, font_med


class Textbox:

    def __init__(self, x, y, width, height, color=WHITE) -> None:

        self.text = ""
        self.color = color
        self.active = False
        self.hovering = False
        self.rect = self.make_rect(x, y, width, height)
        self.surface = font_med.render(self.text, True, self.color)

    def make_rect(self, x, y, width, height):
        text_rect = font_med.render(self.text, True, "Black").get_rect()
        text_rect.midbottom = (x, y)
        text_rect.width = width
        text_rect.height = height

        return text_rect

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            print("clicked")
            if self.rect.collidepoint(pygame.mouse.get_pos()):
                print("Clicked box")
                self.active = True
            else:
                self.active = False

        if self.active and event.type == pygame.KEYDOWN:
            print("Entered:" + event.unicode)
            if event.key == pygame.K_BACKSPACE:
                if len(self.text) > 0:
                    self.text = self.text[:-1]
                else:
                    self.text += event.unicode

        self.surface = font_med.render(self.text, True, self.color)
        return

    def update(self):
        if self.rect.collidepoint(pygame.mouse.get_pos()):
            self.hovering = True
        else:
            self.hovering = False

        if self.active or self.hovering:
            self.color = 'lightskyblue3'
        else:
            self.color = WHITE

        self.rect.w = max(250, self.surface.get_width() + 10)

    def draw(self, screen):
        screen.blit(self.surface, (self.rect.x+5, self.rect.y+5))
        pygame.draw.rect(screen, self.color, self.rect)

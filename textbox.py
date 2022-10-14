import pygame
import time
from ui.uiconfig import WHITE, font_med


class Textbox:

    def __init__(self, x, y, width, height, color=WHITE, font_size=150, input_type=None) -> None:

        self.text = ""
        self.font_size = pygame.font.Font(None, font_size)
        self.color = color
        self.active = False
        self.hovering = False
        self.rect = self.make_rect(x, y, width, height)
        self.surface = self.make_font_surface()
        self.cursor = self.make_cursor()
        self.enter_pressed = False
        self.valid_enter = True
        self.text_was_empty = False
        self.input_type = input_type

    def make_rect(self, x, y, width, height):
        text_rect = font_med.render(self.text, True, "Black").get_rect()
        text_rect.midbottom = (x, y)
        text_rect.width = width
        text_rect.height = height

        return text_rect

    def make_font_surface(self):
        return self.font_size.render(self.text, True, "Black")

    def make_cursor(self):
        cursor = pygame.Rect(
            self.rect.topright, (3, self.rect.height-25))

        return cursor

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(pygame.mouse.get_pos()):
                self.active = True
            else:
                self.active = False

        if event.type == pygame.KEYDOWN:
            if self.active:
                if event.key == pygame.K_BACKSPACE:
                    if len(self.text) > 0:
                        self.text = self.text[:-1]
                elif (event.key == pygame.K_ESCAPE):
                    self.active = False
                elif (event.key == pygame.K_RETURN or event.key == pygame.K_KP_ENTER):
                    self.enter_pressed = True
                    self.check_if_empty()
                    self.handle_enter()
                else:
                    self.text += event.unicode
            else:
                # make active on enter press if not active
                if (event.key == pygame.K_RETURN or event.key == pygame.K_KP_ENTER):
                    self.active = True

        self.surface = self.make_font_surface()
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

        self.rect.w = max(150, self.surface.get_width() + 10)

    def draw(self, screen) -> None:
        # text box rect
        pygame.draw.rect(screen, self.color, self.rect)
        # text in the box
        screen.blit(self.surface, (self.rect.x+5, self.rect.y+5))

        if self.active:
            self.handle_cursor(screen)

    def handle_cursor(self, screen) -> None:

        if time.time() % 1 > .5:
            text_rect = self.surface.get_rect(
                topleft=(self.rect.x + 5, self.rect.y))
            self.cursor.midleft = text_rect.midright
            pygame.draw.rect(screen, "Black", self.cursor)

        return

    def handle_enter(self) -> None:
        if len(self.text) > 0:
            if self.input_type is not None:
                if self.input_type == "int":
                    if self.text.isnumeric() and int(self.text) > 1 and int(self.text) < 8:
                        self.valid_enter = True
                    else:
                        self.text = ""
                        self.valid_enter = False
                        self.enter_pressed = False

    # check if input is empty or just spaces
    def check_if_empty(self) -> None:
        if self.text and self.text.strip():
            self.text_was_empty = False
        else:
            self.text_was_empty = True
            self.enter_pressed = False

    def valid_input(self) -> bool:
        if self.valid_enter and self.enter_pressed and not self.text_was_empty:
            return True
        else:
            return False

import pygame
import os
from ui.uiconfig import WIDTH, HEIGHT, scale_aspect, font_big, font_med, font_small


class Splashscreen:

    def __init__(self) -> None:
        self.blackjack_surf = scale_aspect(pygame.image.load(os.path.join(
            "Assets", "games", "blackjack.png")).convert_alpha(), .75)
        self.war_surf = scale_aspect(pygame.image.load(os.path.join(
            "Assets", "games", "war.png")).convert_alpha(), .75)
        self.blackjack_rect = self.blackjack_surf.get_bounding_rect()
        self.war_rect = self.war_surf.get_bounding_rect()
        self.text = self.get_text()

        self.set_rect_bottom()

    def set_rect_bottom(self):
        self.blackjack_rect.midbottom = (WIDTH/3.2, HEIGHT/1.5)
        self.war_rect.midbottom = (WIDTH/1.46, HEIGHT/1.47)
        return

    def get_text(self):

        title_text = font_big.render("Deck of Cards", True, 'Black')
        instruction_text = font_med.render("Select a game:", True, "Black")
        blackjack_text = font_small.render("BlackJack", True, "Black")
        war_text = font_small.render("War", True, "Black")

        text = {"Title": title_text, "Instruction": instruction_text,
                "Blackjack": blackjack_text, "War": war_text}

        return text

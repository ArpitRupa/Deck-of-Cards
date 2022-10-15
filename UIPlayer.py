from tkinter.tix import WINDOW
from turtle import width
from typing import Text
from core.player import Player
from textbox import Textbox
from ui.uiconfig import WIDTH, HEIGHT, create_text_surface
from ui.gamewindow import Window
from UICard import UICard
import pygame

""""subclass of player class"""""


class UIPlayer(Player):

    def __init__(self, name="", dealer=False):
        super().__init__(name, dealer)
        self.name: str = name
        self.got_name: bool = False
        self.input_text: Textbox = None
        self.ui_name_surface = None
        self.ui_name_rect = None
        self.ui_button_rect = (0, 0)
        self.player_number: int = 0

        self.ui_cards: list = []

    def set_player_number(self, num: int) -> None:
        self.player_number = num

    def update_name_surface(self) -> None:
        self.ui_name_surface = create_text_surface(self.name, 40)
        self.ui_name_rect = self.ui_name_surface.get_rect()

    def set_ui_coordinates(self) -> None:
        match self.player_number:
            case 0:
                self.ui_name_rect.midbottom = (WIDTH/2, HEIGHT/3.4)
                self.ui_button_rect = (450, HEIGHT/1.5)
            case 1:
                self.ui_name_rect.midbottom = (WIDTH/1.95, HEIGHT/1.4)
                self.ui_button_rect = (450, HEIGHT/1.5)
            case 2:
                self.ui_name_rect.midbottom = (WIDTH/3.2, HEIGHT/1.4)
                self.ui_button_rect = (450, HEIGHT/1.5)
            case 3:
                self.ui_name_rect.midbottom = (WIDTH/1.371, HEIGHT/1.4)
                self.ui_button_rect = (450, HEIGHT/1.5)
            case 4:
                self.ui_name_rect.midbottom = (WIDTH/7.85, HEIGHT/1.75)
                self.ui_button_rect = (450, HEIGHT/1.5)
            case 5:
                self.ui_name_rect.midbottom = (WIDTH/1.15, HEIGHT/1.75)
                self.ui_button_rect = (450, HEIGHT/1.5)
                #         case "6":
                #         case "7":

        # print(self.ui_name_rect.midbottom)
        # print(self.ui_name_rect.midbottom[1])

    # displays the player name
    def display_name(self, screen: Window) -> None:
        screen.window.blit(self.ui_name_surface, self.ui_name_rect)
        return

    # create cards for the UI from the hand of the player
    def create_UI_cards(self) -> None:
        player_cards = self.hand.get_cards()
        for card in player_cards:
            value = card.get_card_value()
            suit = card.get_card_suit()
            uiCard = UICard(value, suit)

            # card x coordinate
            # only change for players 4 - 7
            match self.player_number:
                case 4:
                    card_x = self.ui_name_rect.midbottom[0] + 50

                case 5:
                    card_x = self.ui_name_rect.midbottom[0] - 100

                # case 6:

                # case 7:

                case default:
                    card_x = self.ui_name_rect.midbottom[0] - 20

            # handle y coordnate differently only if it is a dealer
            if self.player_number == 0:
                card_y = self.ui_name_rect.midbottom[1] + 100
            else:
                card_y = self.ui_name_rect.midbottom[1] - 30

            if player_cards.index(card) > 0:
                card_x = card_x + \
                    (player_cards.index(card)*40)

            uiCard.rect.midbottom = (card_x, card_y)
            self.ui_cards.append(uiCard)

    def __repr__(self) -> None:
        return (self.name)

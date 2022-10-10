from tkinter.tix import WINDOW
from typing import Text
from core.player import Player
from textbox import Textbox
from ui.uiconfig import WIDTH, HEIGHT, create_text_surface
from ui.gamewindow import Window
import pygame

""""subclass of player class"""""


class UIPlayer(Player):

    def __init__(self, name="", dealer=False):
        super().__init__(name, dealer)
        self.name: int = name
        self.got_name: bool = False
        self.input_text: Textbox = None
        self.ui_name_surface = None
        self.ui_name_rect = None
        self.ui_button_rect = (0, 0)
        self.player_number: int = 0

        self.ui_cards: list

    def set_player_number(self, num: int) -> None:
        self.player_number = num

    def update_name_surface(self) -> None:
        self.ui_name_surface = create_text_surface(self.name, 40)
        self.ui_name_rect = self.ui_name_surface.get_rect()

    def set_ui_coordinates(self) -> None:
        match self.player_number:
            case 1:
                self.ui_name_rect.midbottom = (WIDTH/1.92, HEIGHT/1.4)
                self.ui_button_rect = (450, HEIGHT/1.5)
            case 2:
                self.ui_name_rect.midbottom = (WIDTH/3.2, HEIGHT/1.4)
                self.ui_button_rect = (450, HEIGHT/1.5)
            case 3:
                self.ui_name_rect.midbottom = (WIDTH/1.371, HEIGHT/1.4)
                self.ui_button_rect = (450, HEIGHT/1.5)
            case 4:
                self.ui_name_rect = (WIDTH/8.25, HEIGHT/1.75)
                self.ui_button_rect = (450, HEIGHT/1.5)
            case 5:
                self.ui_name_rect = (WIDTH/1.2, HEIGHT/1.75)
                self.ui_button_rect = (450, HEIGHT/1.5)
                #         case "6":
                #         case "7":

    # displays the player name
    def display_name(self, screen: Window) -> None:
        screen.window.blit(self.ui_name_surface, self.ui_name_rect)
        return

    def __repr__(self) -> None:
        return (self.name)

from core.player import Player
from ui.components.textbox import Textbox
from ui.uiconfig import WIDTH, HEIGHT, create_text_surface
from ui.screens.gamewindow import Window
from ui.components.UICard import UICard
from core.card import Card
import pygame

""""subclass of player class"""""


class UIPlayer(Player):

    def __init__(self, name="", dealer=False):
        super().__init__(name, dealer)
        self.name: str = name
        self.name_color: tuple = (0, 0, 0)
        self.got_name: bool = False
        self.input_text: Textbox = None
        self.ui_name_surface: pygame.Surface = None
        self.ui_name_rect: pygame.Rect = None
        self.ui_button_rect = (0, 0)
        self.player_number: int = 0

        self.ui_cards: list[UICard] = []

    def set_player_number(self, num: int) -> None:
        self.player_number = num

    def update_name_surface(self) -> None:
        self.ui_name_surface = create_text_surface(
            self.name, 40, color=self.name_color)
        if not self.ui_name_rect:
            self.ui_name_rect = self.ui_name_surface.get_rect()

    def set_ui_coordinates(self) -> None:
        match self.player_number:
            # dealer position
            case 0:
                self.ui_name_rect.midbottom = (WIDTH/2, HEIGHT/3.4)
            case 1:
                self.ui_name_rect.midbottom = (WIDTH/1.95, HEIGHT/1.4)
            case 2:
                self.ui_name_rect.midbottom = (WIDTH/3.2, HEIGHT/1.4)
            case 3:
                self.ui_name_rect.midbottom = (WIDTH/1.371, HEIGHT/1.4)
            case 4:
                self.ui_name_rect.midbottom = (WIDTH/7.85, HEIGHT/1.75)
            case 5:
                self.ui_name_rect.midbottom = (WIDTH/1.15, HEIGHT/1.75)

    # displays the player name

    def display_name(self, screen: Window) -> None:

        # change color of text if player stands
        if self.didStand:
            self.name_color = (230, 227, 80)
            self.update_name_surface()

        screen.window.blit(self.ui_name_surface, self.ui_name_rect)

        # put a line through the name if the player busts
        if self.bust:
            # get info to make red line across name
            x = self.ui_name_rect.x
            y = self.ui_name_rect.centery
            width = self.ui_name_surface.get_width()

            pygame.draw.rect(screen.window, "Red", (x, y, width, 5))

        return

    # create cards for the UI from the hand of the player for blackjack
    def create_UI_cards_blk_jk(self, dealer_call: bool) -> None:
        # clear ui cards for cleaner rendering
        self.ui_cards.clear()

        player_cards = self.hand.get_cards()
        for card in player_cards:

            # only render dealer's first card if the dealer has not called
            is_dealer = self.player_number == 0
            is_not_first_card = player_cards.index(card) > 0
            if not dealer_call and is_dealer and is_not_first_card:
                uiCard = UICard()
            else:
                uiCard = self.get_ui_card(card)

            card_x, card_y = self.get_card_coordinates()

            # change placement of new card to the right of previous cards
            if player_cards.index(card) > 0:
                card_x = card_x + \
                    (player_cards.index(card)*40)

            uiCard.rect.midbottom = (card_x, card_y)
            self.ui_cards.append(uiCard)

    # create UI element for player deck in War
    def create_UI_cards_war(self, game) -> None:

        # clear ui cards for cleaner rendering
        self.ui_cards.clear()

        player_cards = self.hand.get_cards()

        if game.state == "Battle":
            deck_count = len(player_cards) - 1
        else:
            deck_count = len(player_cards)
        deck_count_surf = create_text_surface(str(deck_count), 35, "darkblue")

        # check if you render the player deck on the table
        if deck_count > 0:
            deck_UI = UICard()

            card_x, card_y = self.get_card_coordinates()
            deck_UI.image.blit(deck_count_surf, (17, 35))
            deck_UI.rect.midbottom = (card_x, card_y)
            self.ui_cards.append(deck_UI)

        # render top card of player deck
        if game.state == "Battle":
            if self in game.active_players:
                hand = self.hand.get_cards()
                card = hand[len(hand)-1]

                uiCard = self.get_ui_card(card)

                card_x, card_y = self.get_card_coordinates()
                card_x = card_x + 75
                uiCard.rect.midbottom = (card_x, card_y)

                self.ui_cards.append(uiCard)

        # if game in collect phase,
        if game.state == "Collect":
            # and player has card in dict,
            if self in game.total_round:
                #  render cards
                player_cards = game.total_round[self]
                for card in player_cards:
                    uiCard = self.get_ui_card(card)

                    card_x, card_y = self.get_card_coordinates()
                    card_x = card_x + 75

                    if player_cards.index(card) > 0:
                        card_x = card_x + player_cards.index(card)*30

                    uiCard.rect.midbottom = (card_x, card_y)
                    self.ui_cards.append(uiCard)

    def get_card_coordinates(self) -> tuple:

        # card x coordinate
        # only change for players 4 - 7
        match self.player_number:
            case 4:
                card_x = self.ui_name_rect.midbottom[0] + 50

            case 5:
                card_x = self.ui_name_rect.midbottom[0] - 100

            case default:
                card_x = self.ui_name_rect.midbottom[0] - 20

        # handle y coordinate differently only if it is a dealer
        if self.player_number == 0:
            card_y = self.ui_name_rect.midbottom[1] + 100
        else:
            card_y = self.ui_name_rect.midbottom[1] - 30

        return (card_x, card_y)

    def get_ui_card(self, card: Card) -> UICard:

        value = card.get_card_value()
        suit = card.get_card_suit()
        uiCard = UICard(value, suit)

        return uiCard

    def __repr__(self) -> None:
        return (self.name)

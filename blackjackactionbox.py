import pygame
from button import Button
from ui.uiconfig import create_text_surface, GREY


class BlackjackActionBox():

    def __init__(self, name: str = "Name") -> None:
        self.current_player: str = name
        self.current_player_surf: pygame.Surface = self.update_player_text()
        self.current_player_rect: pygame.Rect
        self.value_surf: pygame.Surface = self.update_value()
        self.value_rect: pygame.Rect
        self.background_surf: pygame.Surface = self.init_background_surf()
        self.hit_button: Button = Button(name="Hit", center=(1070, 813))
        self.stand_button: Button = Button(name="Stand", center=(1070, 863))

    # init the box's background
    def init_background_surf(self) -> pygame.Surface:
        surf = pygame.Surface((240, 188), flags=pygame.SRCALPHA)
        surf.set_alpha(10)
        surf.fill((80, 83, 230))

        return surf

    def draw_box_border(self, window) -> None:
        # top-left down
        pygame.draw.rect(window.window, "Black", (945, 700, 5, 188))
        # bottom-left right
        pygame.draw.rect(window.window, "Black", (945, 887, 245, 5))
        # top-left right
        pygame.draw.rect(window.window, "Black", (945, 700, 240, 5))
        # top-right down
        pygame.draw.rect(window.window, "Black", (1185, 700, 5, 188))
        return

    # updates player name
    def update_player(self, name) -> None:
        self.current_player = name
        self.update_player_text()
        self.update_player_rect()

        # clear the surface to display new name
        self.background_surf.fill((80, 83, 230))
        return

    # updates the text for the current player
    def update_player_text(self) -> pygame.Rect:
        surf = create_text_surface(
            self.current_player, 60, color=(247, 127, 0))
        self.current_player_surf = surf
        self.update_player_rect()

        return surf

    # update the rect for the current player
    def update_player_rect(self) -> None:
        rect = self.current_player_surf.get_rect()
        rect.midtop = (120, 5)
        self.current_player_rect = rect
        return

    def update_value(self, value: int = 0) -> None:

        value = create_text_surface(
            "Current Val: " + str(value), 35, color="Black")
        self.value_surf = value
        self.value_rect = self.value_surf.get_rect()
        self.value_rect.midtop = (120, 53)

        return value

    def draw(self, window) -> None:

        self.update_player_text()

        # draw border around action box
        self.draw_box_border(window)

        # draw the hit and stand buttons
        self.hit_button.draw(window)
        self.stand_button.draw(window)

        # display current player name
        self.background_surf.blit(
            self.current_player_surf, self.current_player_rect)

        # display current value
        self.background_surf.blit(self.value_surf, self.value_rect)
        # display the action box background
        window.window.blit(self.background_surf, (950, 702))
        return

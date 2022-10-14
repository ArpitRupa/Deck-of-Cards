from cgitb import grey
import pygame
from ui.uiconfig import create_text_surface, GREY


class BlackjackActionBox():

    def __init__(self) -> None:
        self.current_player: str = "Noob"
        self.current_player_surf: pygame.Surface = self.update_player_text()
        self.current_player_rect: pygame.Rect
        self.value_surf: pygame.Surface
        self.value_rect: pygame.Rect
        self.background_surf: pygame.Surface = self.init_background_surf()
        self.hit_surf: pygame.Surface
        self.hit_rect: pygame.Rect = self.init_hit_rect()
        self.stand_surf: pygame.Surface
        self.stand_rect: pygame.Rect = self.init_stand_rect()
        self.stand_fill: tuple = (230, 227, 80)
        self.hit_fill: tuple = (230, 227, 80)

    def init_background_surf(self) -> pygame.Surface:
        surf = pygame.Surface((240, 188))
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

    def create_action_rect(self, surf: pygame.Surface, x: int, y: int) -> pygame.Rect:
        rect = surf.get_rect(center=(x, y))
        return rect

    def init_hit_rect(self) -> pygame.Rect:
        hit_text = create_text_surface("Hit Me", 40)
        hit_rect = self.create_action_rect(hit_text, 1070, 813)
        self.hit_surf = hit_text

        return hit_rect

    def init_stand_rect(self) -> pygame.Rect:
        stand_text = create_text_surface("Stand", 40)
        stand_rect = self.create_action_rect(stand_text, 1070, 863)
        self.stand_surf = stand_text

        return stand_rect

    def update_player(self, name) -> None:
        self.current_player = name
        return

    def update_player_text(self) -> pygame.Rect:
        surf = create_text_surface(
            self.current_player, 60, color=(247, 127, 0))
        self.current_player_surf = surf
        self.update_player_rect()

        return surf

    def update_player_rect(self) -> None:
        rect = self.current_player_surf.get_rect()
        rect.midtop = (120, 5)
        self.current_player_rect = rect
        return

    def handle_hover(self, rect, type: str) -> None:

        # print("Rect": + ())
        if rect.collidepoint(pygame.mouse.get_pos()):
            fill_to_change = GREY
            print("Hovering....")
            print(type)
        else:
            fill_to_change = (230, 227, 80)
        match type:
            case "Hit":
                self.hit_fill = fill_to_change
            case "Stand":
                self.stand_fill = fill_to_change
        return

    def create_outer_rect(self, rect: pygame.Rect, scale: int = 10) -> pygame.Rect:
        outer_rect = rect.copy()

        outer_rect.width = outer_rect.width+scale
        outer_rect.height = outer_rect.height+scale
        outer_rect.x = outer_rect.x - scale/2
        outer_rect.y = outer_rect.y - scale/2

        return outer_rect

    def draw(self, window) -> None:
        self.update_player_text()
        self.handle_hover(rect=self.hit_rect, type="Hit")
        self.handle_hover(rect=self.stand_rect,  type="Stand")

        outer_rect_hit = self.create_outer_rect(self.hit_rect, scale=12)
        outer_rect_stand = self.create_outer_rect(self.stand_rect, scale=12)

        self.handle_hover(rect=self.hit_rect, type="Hit")
        self.handle_hover(rect=self.stand_rect,  type="Stand")

        self.draw_box_border(window)
        # borders around "hit" and "stand" buttons
        pygame.draw.rect(window.window, "Black", outer_rect_hit)
        pygame.draw.rect(window.window, "Black", outer_rect_stand)

        # fill of the 2 buttons
        pygame.draw.rect(window.window,
                         self.stand_fill, self.stand_rect)
        pygame.draw.rect(window.window, self.hit_fill, self.hit_rect)

        window.window.blit(self.hit_surf, self.hit_rect)
        window.window.blit(self.stand_surf, self.stand_rect)
        self.background_surf.blit(
            self.current_player_surf, self.current_player_rect)

        window.window.blit(self.background_surf, (950, 702))

        self.handle_hover(rect=self.hit_rect, type="Hit")
        self.handle_hover(rect=self.stand_rect,  type="Stand")

        return

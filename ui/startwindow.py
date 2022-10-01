import pygame
from ui.uiconfig import WIDTH, HEIGHT, GREY

# renders the start-game splash screen


def start_window(window, splash_screen, game):
    window.window.fill(GREY)

    # get variables from splashscreen to make it easier to reference
    blackjack_surf, blackjack_rect = splash_screen.blackjack_surf, splash_screen.blackjack_rect
    war_surf, war_rect = splash_screen.war_surf, splash_screen.war_rect

    title_text, instruction_text, blackjack_text, war_text = splash_screen.text[
        "Title"], splash_screen.text["Instruction"], splash_screen.text["Blackjack"], splash_screen.text["War"]

    # LOCATION OF RENDER
    game.render_background(window)
    window.window.blit(
        blackjack_surf, (blackjack_rect[0]-17, blackjack_rect[1]))
    window.window.blit(war_surf, (war_rect[0]-33, war_rect[1]))
    window.window.blit(title_text, ((225/800)*WIDTH, (50/600)*HEIGHT))
    window.window.blit(
        instruction_text, ((300/800)*WIDTH, (180/600)*HEIGHT))
    window.window.blit(blackjack_text, ((200/800)*WIDTH, (400/600)*HEIGHT))
    window.window.blit(war_text, ((530/800)*WIDTH, (400/600)*HEIGHT))

    # hover effect for blackjack icon
    if splash_screen.blackjack_rect.collidepoint(pygame.mouse.get_pos()):
        blackjack_surf.set_alpha(180)
        blackjack_text.set_alpha(140)
    else:
        blackjack_surf.set_alpha(255)
        blackjack_text.set_alpha(255)

    # hover effect for war icon
    if war_rect.collidepoint(pygame.mouse.get_pos()):
        war_surf.set_alpha(180)
        war_text.set_alpha(140)
    else:
        war_surf.set_alpha(255)
        war_text.set_alpha(255)

    # check which game the player clicks on
    for event in game.events:
        if event.type == pygame.MOUSEBUTTONDOWN:
            # change state based on which icon is clicked
            if blackjack_rect.collidepoint(pygame.mouse.get_pos()):
                game.game_title = "Blackjack"
            elif war_rect.collidepoint(pygame.mouse.get_pos()):
                game.game_title = "War"

        # update the splash-screen
        pygame.display.update()

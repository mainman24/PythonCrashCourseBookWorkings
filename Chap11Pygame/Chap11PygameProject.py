import pygame
from settings import Settings
from ship import Ship
import game_functions as gf
from pygame.sprite import Group


def run_game():
    pygame.init()

    ai_settings = Settings()
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height))
    ship = Ship(screen, ai_settings)
    pygame.display.set_caption("Alien Invasion")
    bullets = Group()

    while True:

        gf.check_events(ai_settings, screen, ship, bullets)
        ship.update()
        gf.update_bullets(bullets)  # After ship update before update screen
        # Updates position of bullets ^^^
        gf.update_screen(ai_settings, screen, ship, bullets)


run_game()

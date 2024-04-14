import pygame
from settings import Settings
from game_stats import GameStats
from ship import Ship
from alien import Alien
import game_functions as gf
from pygame.sprite import Group


def run_game():

    pygame.init()

    ai_settings = Settings()
    stats = GameStats(ai_settings)
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

    ship = Ship(screen, ai_settings)

    bullets = Group()
    aliens = Group()

    gf.create_fleet(ai_settings, screen, aliens, ship)

    while True:

        gf.check_events(ai_settings, screen, ship, bullets)
        if stats.game_active:
            ship.update()
            # After ship update before update screen
            gf.update_bullets(ai_settings, screen, ship, bullets, aliens)
            # Updates position of bullets ^^^
            gf.update_aliens(ai_settings, aliens, ship, screen, stats, bullets)
        gf.update_screen(ai_settings, screen, ship, bullets, aliens)


run_game()

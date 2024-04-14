import sys
import pygame
from bullet import Bullet
from alien import Alien
from time import sleep


def change_fleet_direction(ai_settings, aliens):
    for alien in aliens.sprites():
        alien.rect.y += ai_settings.fleet_drop_speed
    ai_settings.fleet_direction *= -1


def check_fleet_edges(ai_settings, aliens):
    for alien in aliens.sprites():
        if alien.check_edges():
            change_fleet_direction(ai_settings, aliens)
            break


def check_alien_bottom(ai_settings, screen, aliens, ship, stats, bullets):
    screen_rect = screen.get_rect()
    for alien in aliens.sprites():
        if alien.rect.bottom >= screen_rect.bottom:
            ship_hit(ai_settings, screen, aliens, ship, stats, bullets)
            break


def ship_hit(ai_settings, screen, aliens, ship, stats, bullets):

    if stats.ship_left > 0:
        stats.ship_left -= 1

        aliens.empty()
        bullets.empty()

        create_fleet(ai_settings, screen, aliens, ship)

        ship.center_ship()

        sleep(0.5)

    else:
        stats.game_active = False


def update_aliens(ai_settings, aliens, ship, screen, stats, bullets):
    check_fleet_edges(ai_settings, aliens)
    aliens.update()

    if pygame.sprite.spritecollideany(ship, aliens):
        ship_hit(ai_settings, screen, aliens, ship, stats, bullets)

    check_alien_bottom(ai_settings, screen, aliens, ship, stats, bullets)


def get_number_rows(ai_settings, ship_height, alien_height):
    available_space_y = (ai_settings.screen_height - (3 * alien_height) - ship_height)
    number_rows = int(available_space_y / (2 * alien_height))
    return number_rows


def get_number_aliens(ai_settings, alien_width):
    available_space_x = ai_settings.screen_width - 2 * alien_width
    number_of_aliens = int(available_space_x / (2 * alien_width))
    return number_of_aliens


def create_alien(ai_settings, screen, aliens, alien_number, row_number):
    alien = Alien(ai_settings, screen)
    alien_width = alien.rect.width
    alien.x = alien_width + 2 * alien_width * alien_number
    alien.rect.x = alien.x
    alien.rect.y = alien.rect.height + alien.rect.height * 2 * row_number
    aliens.add(alien)


def create_fleet(ai_settings, screen, aliens, ship):
    alien = Alien(ai_settings, screen)
    number_of_aliens = get_number_aliens(ai_settings, alien.rect.width)
    number_rows = get_number_rows(ai_settings, ship.rect.height, alien.rect.height)
    for row_number in range(number_rows):
        for alien_number in range(number_of_aliens):
            create_alien(ai_settings, screen, aliens, alien_number, row_number)


def check_bullet_alien_collision(ai_settings, screen, aliens, ship, bullets):
    collisions = pygame.sprite.groupcollide(bullets, aliens, True, True)
    if len(aliens) == 0:
        bullets.empty()
        create_fleet(ai_settings, screen, aliens, ship)


def update_bullets(ai_settings, screen, ship, bullets, aliens):
    bullets.update()
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
    check_bullet_alien_collision(ai_settings, screen, aliens, ship, bullets)


def fire_bullets(ai_settings, screen, ship, bullets):
    if ai_settings.bullets_allowed > len(bullets):
        new_bullet = Bullet(ai_settings, screen, ship)
        bullets.add(new_bullet)


def check_key_down_events(event, ship, ai_settings, screen, bullets):
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True
    elif event.key == pygame.K_SPACE:
        fire_bullets(ai_settings, screen, ship, bullets)


def check_key_up_events(event, ship):
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False


def check_events(ai_settings, screen, ship, bullets):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_key_down_events(event, ship, ai_settings, screen, bullets)
        elif event.type == pygame.KEYUP:
            check_key_up_events(event, ship)


def update_screen(ai_settings, screen, ship, bullets, aliens):
    screen.fill(ai_settings.bg_color)
    ship.blitme()  # Drawing the ship to the screen
    aliens.draw(screen)
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    pygame.display.flip()

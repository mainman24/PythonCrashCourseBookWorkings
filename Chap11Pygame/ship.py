import pygame


class Ship():

    def __init__(self, screen, ai_settings):
        self.screen = screen
        self.moving_right = False
        self.moving_left = False
        self.image = pygame.image.load("images/ship.bmp")
        self.ai_settings = ai_settings
        self.rect = self.image.get_rect()
        self.screen_rect = self.screen.get_rect()

        # Setting the location of rect image object

        self.rect.bottom = self.screen_rect.bottom
        self.rect.centerx = self.screen_rect.centerx
        self.center = float(self.rect.centerx)

    # To draw the image at the location of self.rect

    def blitme(self):
        self.screen.blit(self.image, self.rect)

    def update(self):
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.ai_settings.ship_speed_factor
        if self.moving_left and self.rect.left > 0:
            self.center -= self.ai_settings.ship_speed_factor

        self.rect.centerx = self.center

    def center_ship(self):
        self.rect.x = self.screen_rect.centerx

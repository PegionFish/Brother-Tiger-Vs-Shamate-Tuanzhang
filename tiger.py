import pygame

class HuGe():
    def __init__ (self, sys_settings, screen):
        self.screen = screen
        self.sys_settings = sys_settings
    # Load HuGe's image & vortex
        self.image = pygame.image.load("material/image/tiger.png")
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

    # Place it on the button middle of the screen
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

    # Store a decimal value for HuGe's center
        self.center = float(self.rect.centerx)
        self.bottom = float(self.rect.bottom)

    # Movement Flag
        self.moving_right = False
        self.moving_left = False

    def update(self):
        """Update HuGe's position based on moving flag"""
        # Update HuGe's center value, not the rect
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.sys_settings.HuGe_speed_factor
        elif self.moving_left and self.rect.left > 0:
            self.center -= self.sys_settings.HuGe_speed_factor
        
        # Update rect object from self.center
        self.rect.centerx = self.center
        self.rect.bottom = self.bottom

    def blitme(self):
        """Draw ship at given location"""
        self.screen.blit(self.image, self.rect)

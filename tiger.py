import pygame

class HuGe():
    def __init__ (self, screen):
        self.screen = screen

    # Load HuGe's image & vortex
        self.image = pygame.image.load("material/image/tiger.jpeg")
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

    # Place it on the button middle of the screen
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

    def blitme(self):
        self.screen.blit(self.image, self.rect)

    def update(tiger):
        if tiger.moving_right:
            self.rect.centerx += 1
        if tiger.moving_left:
            self.rect.centerx -= 1
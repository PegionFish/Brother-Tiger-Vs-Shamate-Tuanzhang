import pygame
from pygame.sprite import Sprite

class Huo(Sprite):
    """A Class to manage huo made by HuGe"""

    def __init__(self, sys_settings, screen, HuGe):
        """Create a huo object at HuGe's position"""
        super(Huo, self).__init__() # Python 2 method, works in Python 3 but writing as super().__init__() is better
        self.screen = screen

        # Create a huo rect @ (0,0) & set correct position
        self.rect = pygame.Rect(0, 0, sys_settings.huo_width, sys_settings.huo_height)
        self.rect.centerx = HuGe.rect.centerx
        self.rect.top = HuGe.rect.top

        # Store huo's position as a decimal value
        self.y = float(self.rect.y)

        self.color = sys_settings.huo_color
        self.speed_factor = sys_settings.huo_speed_factor

    def update(self):
        """Move huo up to screen"""
        # Update the decimal position of huo
        self.y -= self.speed_factor
        # Update the rect position
        self.rect.y = self.y

    def zheng_huo(self):
        """Zheng a Huo onto the screen"""
        pygame.draw.rect(self.screen, self.color, self.rect)
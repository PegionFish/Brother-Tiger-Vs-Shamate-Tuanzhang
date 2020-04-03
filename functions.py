import sys
import pygame
from tiger import HuGe

def check_events(tiger):
    for event in pygame.event.get():
        if event.type == pygame.quit:
            sys.exit()
        
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                #Move Right
                tiger.moving_right = True
            if event.key == pygame.K_LEFT:
                #Move Left
                tiger.moving_left = True

def update_screen(win_settings, screen, tiger):
    # Redo the screen every loop
    screen.fill(win_settings.bg_color)
    tiger.blitme()
    # Make the lateset screen visable
    pygame.display.flip()
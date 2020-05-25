import sys
import pygame
from huo import Huo

def check_keydown_events(event, sys_settings, screen, HuGe, huo):
    """Respond to keypresses"""
    if event.key == pygame.K_RIGHT:
        #Move the HuGe to the right
        HuGe.moving_right = True
    elif event.key == pygame.K_LEFT:
        #Move the HuGe to the left
        HuGe.moving_left = True

    elif event.key == pygame.K_SPACE:
        #Zheng Huo
        new_huo = Huo(sys_settings, screen, HuGe)
        huo.add(new_huo)
def check_keyup_events(event, HuGe):
    """Respond to key releases"""
    if event.key == pygame.K_RIGHT:
        #Stop moving the HuGe to the right
        HuGe.moving_right = False
    elif event.key == pygame.K_LEFT:
        #Stop moving the HuGe to the left
        HuGe.moving_left = False


def check_events(sys_settings, screen, HuGe, huo):
    """React to keyboard&Mouse events"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, sys_settings, screen, HuGe, huo)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, HuGe)
def update_screen(sys_settings, screen, HuGe,huo):
    """Update images on the screnn & flip to the new screen"""
    #Redraw the screen during each pass through the loop
    screen.fill(sys_settings.bg_color)

    #Rezhen all huo behind HuGe and Shamate
    for huo in huo.sprites():
        huo.zheng_huo()
    
    HuGe.blitme()

    #Make the most recently drawn screnn visible
    pygame.display.flip()
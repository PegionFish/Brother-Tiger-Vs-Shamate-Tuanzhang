import sys
import pygame

def check_keydown_events(event, HuGe):
    """Respond to keypresses"""
    if event.key == pygame.K_RIGHT:
        #Move the HuGe to the right
        HuGe.moving_right = True
    elif event.key == pygame.K_LEFT:
        #Move the HuGe to the left
        HuGe.moving_left = True
    elif event.key == pygame.K_UP:
        #Move the HuGe to the top
        HuGe.moving_up = True
    elif event.key == pygame.K_DOWN:
        #Move the HuGe to the bottom
        HuGe.moving_down = True
def check_keyup_events(event, HuGe):
    """Respond to key releases"""
    if event.key == pygame.K_RIGHT:
        #Stop moving the HuGe to the right
        HuGe.moving_right = False
    elif event.key == pygame.K_LEFT:
        #Stop moving the HuGe to the left
        HuGe.moving_left = False
    elif event.key == pygame.K_UP:
        #Stop moving the HuGe to the top
        HuGe.moving_up = False
    elif event.key == pygame.K_DOWN:
        #Stop moving the HuGe to the bottom
        HuGe.moving_down = False

def check_events(HuGe):
    """React to keyboard&Mouse events"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, HuGe)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, HuGe)
def update_screen(ai_settings, screen, HuGe):
    """Update images on the screnn & flip to the new screen"""
    #Redraw the screen during each pass through the loop
    screen.fill(ai_settings.bg_color)
    HuGe.blitme()

    #Make the most recently drawn screnn visible
    pygame.display.flip()
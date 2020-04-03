# Main program of Alien Invasion
import sys
import pygame
from setting import Settings
from tiger import HuGe

def run_game():
    pygame.init()
    win_settings = Settings()
    # Configuring screen res and title
    screen =  pygame.display.set_mode((win_settings.width, win_settings.height))
    pygame.display.set_caption("虎哥大战杀马特团长")

    tiger = HuGe(screen)

    while True:

        #Monitoring Keyboard & Mouse
        for event in pygame.event.get():
            if event.type == pygame.quit:
                sys.exit
        
        screen.fill(win_settings.bg_color)
        tiger.blitme()

        pygame.display.flip()

run_game()
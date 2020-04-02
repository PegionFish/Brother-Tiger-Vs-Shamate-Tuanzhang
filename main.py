# Main program of Alien Invasion
import sys
import pygame

def run_game():
    pygame.init()
    # Configuring screen res and title
    screen =  pygame.display.set_mode((1440, 900))
    bg_color = (40, 80, 100)
    pygame.display.set_caption("虎哥大战杀马特团长")

    while True:

        #Monitoring Keyboard & Mouse
        for event in pygame.event.get():
            if event.type == pygame.quit:
                sys.exit
        
        screen.fill(bg_color)
        pygame.display.flip()

run_game()
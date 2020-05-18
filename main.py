# Main program of Brother Tiger vs Shamate Tuanzhang
import sys
import pygame
from setting import Settings
from tiger import HuGe
import functions as gf

def run_game():
    pygame.init()
    sys_settings = Settings()
    # Configuring screen res and title
    screen =  pygame.display.set_mode((sys_settings.width, sys_settings.height))
    pygame.display.set_caption("虎哥大战杀马特团长")

    tiger = HuGe(sys_settings, screen)

    while True:
        gf.check_events(tiger)
        tiger.update()
        gf.update_screen(sys_settings, screen, tiger)
run_game()
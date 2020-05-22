# Main program of Brother Tiger vs Shamate Tuanzhang
import sys
import pygame
from setting import Settings
from tiger import HuGe
import functions as gf
from pygame.sprite import Group

def run_game():
    pygame.init()
    sys_settings = Settings()
    # Configuring screen res and title
    screen =  pygame.display.set_mode((sys_settings.width, sys_settings.height))
    pygame.display.set_caption("虎哥大战杀马特团长")

    # Generating HuGe
    tiger = HuGe(sys_settings, screen)

    # Generating group to store huo
    huo = Group()

    # Start gaming Loop
    while True:
        gf.check_events(sys_settings, screen, tiger, huo)
        tiger.update()
        huo.update()
        gf.update_screen(sys_settings, screen, tiger, huo)
run_game()
import game
import pygame
from Weathersim.kollarbalint.IdoScreen import *
from Weathersim.kollarbalint.IdoStage import *
from Weathersim.kollarbalint.IdoScreen import *
from Weathersim.kollarbalint.IdoActors import *
from Weathersim.kollarbalint.IdoSzoveg import *

class Ido(game.scene2d.MyGame):

    def __init__(self, width: int = 1280, height: int = 720, autorun: bool = False, autosize: bool = False):
        super().__init__(width, height, autorun, autosize)
        self.screen = MenuScr()
        self.set_on_key_down_listener(self.key_down)

    def key_down(self, sender, event):
        print(sender)
        print(event)
        if event.key == pygame.K_F11:
            pygame.display.toggle_fullscreen()
            print("'FULLSCREEN'")
        if event.key == pygame.K_BACKSPACE:
            self.screen = MenuScr()
            print("'VISSZA'")
        if event.key == pygame.K_1:
            self.screen = NapsutesScr()
        if event.key == pygame.K_2:
            self.screen = EsoScr()
        if event.key == pygame.K_3:
            self.screen = HavazasScr()
        if event.key == pygame.K_4:
            self.screen = HavasesoScr()
        if event.key == pygame.K_5:
            self.screen = EndScr()
            print("'VÉGE'")
        if event.key == pygame.K_ESCAPE:
            quit()
            print("'QUIT'")

Ido().run()
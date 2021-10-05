import game
import pygame
from Weathersim.kollarbalint.IdoScreen import *

class Ido(game.scene2d.MyGame):

    def __init__(self, width: int = 1280, height: int = 720, autorun: bool = False, autosize: bool = False):
        super().__init__(width, height, autorun, autosize)
        self.screen = MenuScr()
        self.set_on_mouse_down_listener(self.play)
        self.set_on_key_down_listener(self.key_down)

    def play(self,sender,event):
        print(sender)
        print(event)
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                self.screen = NapsutesScr()
                print("'PLAY'")

    def key_down(self, sender, event):
        print(sender)
        print(event)
        if event.key == pygame.K_BACKSPACE:
            self.screen = MenuScr()
            print("'BACK'")


Ido().run()
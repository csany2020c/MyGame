import pygame
from Weathersim.nemethcsongor1.Actorok import *
from Weathersim.nemethcsongor1.start.SaScreen import *


class SuStage(game.scene2d.MyStage):

    def __init__(self):
        super().__init__()
        self.S = Sunny()
        self.add_actor(self.S)

        self.Su = Sun()
        self.add_actor(self.Su)
        self.Su.x = 550
        self.Su.y = 5
        self.Su.set_size(width=350, height=350)

        self.Bg = Bg()
        self.add_actor(self.Bg)

        self.Ba = Back()
        self.add_actor(self.Ba)
        self.Ba.set_size(width=250, height=250)
        self.Ba.set_on_mouse_down_listener(self.klikk)

        self.set_on_key_down_listener(self.katt)

    def katt(self, sender, event):
        print(sender)
        print(event)
        if event.key == pygame.K_ESCAPE:
            quit()

    def klikk(self, sender, event):
        print(sender)
        if event.button == 1:
            self.screen.game.set_screen(SaScreen())

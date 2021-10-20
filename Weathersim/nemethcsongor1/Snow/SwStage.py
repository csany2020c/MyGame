from Weathersim.nemethcsongor1.Actorok import *
import Weathersim.nemethcsongor1.start.SaScreen
from Weathersim.nemethcsongor1.Font import *
import pygame


class SwStage(game.scene2d.MyStage):

    def __init__(self):
        super().__init__()
        self.C = Cloudy()
        self.add_actor(self.C)

        self.Bg = Snoww()
        self.add_actor(self.Bg)
        self.Bg.width = 1280
        self.Bg.height = 720

        self.Ff2 = Font3()
        self.add_actor(self.Ff2)
        self.Ff2.set_text("-10°C")
        self.Ff2.x = 1150
        self.Ff2.y = 10

        for i in range(30):
            self.S = Snow()
            self.add_actor(self.S)
            self.S.set_size(width=30, height=30)
            self.S.x = random.randint(a=0, b=1280)
            self.S.y = random.randint(a=-0, b=720)

        self.Ba = Back()
        self.add_actor(self.Ba)
        self.Ba.set_size(width=250, height=250)
        self.Ba.set_on_mouse_down_listener(self.klikk)

        self.set_on_key_down_listener(self.katt)

    def klikk(self, sender, event):
        print(sender)
        if event.button == 1:
            self.screen.game.set_screen(Weathersim.nemethcsongor1.start.SaScreen.SaScreen())

    def katt(self, sender, event):
        print(sender)
        if event.key == pygame.K_BACKSPACE:
            self.screen.game.set_screen(Weathersim.nemethcsongor1.start.SaScreen.SaScreen())

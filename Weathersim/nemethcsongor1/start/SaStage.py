from Weathersim.nemethcsongor1.Sun.SuScreen import *
from Weathersim.nemethcsongor1.Rain.RScreen import *
from Weathersim.nemethcsongor1.Snow.SwScreen import *
from Weathersim.nemethcsongor1.Blizzard.BScreen import *
from Weathersim.nemethcsongor1.Font import *
from Weathersim.nemethcsongor1.Credits import *
import pygame


class SaStage(game.scene2d.MyStage):
    def __init__(self):
        super().__init__()
        self.Bg = Bgg()
        self.add_actor(self.Bg)
        self.Bg.height = 720
        self.Bg.width = 1280

        self.Ff = Font()
        self.add_actor(self.Ff)
        self.Ff.set_text("WeatherSim")
        self.Ff.x = 450
        self.Ff.set_on_mouse_down_listener(self.katt5)

        self.Ff2 = Font2()
        self.add_actor(self.Ff2)
        self.Ff2.set_text("Kattintás az iconokra!")
        self.Ff2.x = 400
        self.Ff2.y = 550
        self.Ff2.set_color(12, 56, 196)

        self.S = FSun()
        self.add_actor(self.S)
        self.S.set_size(width=280, height=280)
        self.S.set_on_mouse_down_listener(self.katt)
        self.S.x = 100
        self.S.y = 150

        self.R = FRain()
        self.add_actor(self.R)
        self.R.set_size(width=56, height=56)
        self.R.set_on_mouse_down_listener(self.katt2)
        self.R.x = 500
        self.R.y = 270

        self.C = Cloud()
        self.add_actor(self.C)
        self.C.set_size(width=56, height=56)
        self.C.set_on_mouse_down_listener(self.katt3)
        self.C.x = 750
        self.C.y = 270

        self.Sw = FSnow()
        self.add_actor(self.Sw)
        self.Sw.set_size(width=56, height=56)
        self.Sw.set_on_mouse_down_listener(self.katt4)
        self.Sw.x = 1000
        self.Sw.y = 270

        self.Ff3 = Font2()
        self.add_actor(self.Ff3)
        self.Ff3.set_text("1")
        self.Ff3.set_color(0, 0, 0)
        self.Ff3.y = 425
        self.Ff3.x = 225
        self.Ff3.set_color(12, 56, 196)

        self.Ff5 = Font2()
        self.add_actor(self.Ff5)
        self.Ff5.set_text("2")
        self.Ff5.set_color(0, 0, 0)
        self.Ff5.y = 425
        self.Ff5.x = 505
        self.Ff5.set_color(12, 56, 196)

        self.Ff6 = Font2()
        self.add_actor(self.Ff6)
        self.Ff6.set_text("3")
        self.Ff6.set_color(0, 0, 0)
        self.Ff6.y = 425
        self.Ff6.x = 750
        self.Ff6.set_color(12, 56, 196)

        self.Ff7 = Font2()
        self.add_actor(self.Ff7)
        self.Ff7.set_text("4")
        self.Ff7.set_color(0, 0, 0)
        self.Ff7.y = 425
        self.Ff7.x = 1020
        self.Ff7.set_color(12, 56, 196)

        self.set_on_key_down_listener(self.klikk)

    def katt(self, sender, event):
        print(sender)
        if event.button == 1:
            self.screen.game.set_screen(SuScreen())

    def katt2(self, sender, event):
        print(sender)
        if event.button == 1:
            self.screen.game.set_screen(RScreen())

    def katt3(self, sender, event):
        print(sender)
        if event.button == 1:
            self.screen.game.set_screen(BScreen())

    def katt4(self, sender, event):
        print(sender)
        if event.button == 1:
            self.screen.game.set_screen(SwScreen())

    def katt5(self, sender, event):
        print(sender)
        if event.button == 1:
            self.screen.game.set_screen(CScreen())

    def klikk(self, sender, event):
        print(sender)
        if event.key == pygame.K_1:
            self.screen.game.set_screen(SuScreen())
        if event.key == pygame.K_2:
            self.screen.game.set_screen(RScreen())
        if event.key == pygame.K_3:
            self.screen.game.set_screen(BScreen())
        if event.key == pygame.K_4:
            self.screen.game.set_screen(SwScreen())
        if event.key == pygame.K_w:
            self.screen.game.set_screen(CScreen())

from Weathersim.nemethcsongor1.Sun.SuScreen import *
from Weathersim.nemethcsongor1.Rain.RScreen import *
from Weathersim.nemethcsongor1.Snow.SwScreen import *
from Weathersim.nemethcsongor1.Blizzard.BScreen import *
from Weathersim.nemethcsongor1.Font import *
from Weathersim.nemethcsongor1.Font2 import *


class SaStage(game.scene2d.MyStage):
    def __init__(self):
        super().__init__()
        self.Ff = Font()
        self.add_actor(self.Ff)
        self.Ff.set_text("WeatherSim")
        self.Ff.x = 450

        self.Ff2 = Font2()
        self.add_actor(self.Ff2)
        self.Ff2.set_text("Kattintás az iconokra!")
        self.Ff2.x = 400
        self.Ff2.y = 500

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


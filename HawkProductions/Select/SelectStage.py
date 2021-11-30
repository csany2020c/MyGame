import HawkProductions.menu.MenuScreen
from HawkProductions.Actors import *
from HawkProductions.Font import *
import HawkProductions.Game.GameScreen
import HawkProductions.Music
import pygame
import HawkProductions.Select.SelectScreen
from game.scene2d import MyBaseActor, MyActor


class SelectStage(game.scene2d.MyStage):
    def __init__(self):
        super().__init__()
        self.puska: int = 0
        self.t = Arrow()
        self.add_actor(self.t)
        self.t.w = 125
        self.t.hitbox_scale_h = 0.5
        self.t.hitbox_scale_w = 0.5
        self.t.set_on_mouse_down_listener(self.katt)

        self.f = Anything()
        self.add_actor(self.f)
        self.f.set_text("Black Ice")
        self.f.x = 500
        self.f.y = 100
        self.f.set_color(0, 0, 0)

        self.D = None
        self.frissites()

        self.a = Arrow()
        self.add_actor(self.a)
        self.a.x = 300
        self.a.y = 250
        self.a.w = 200
        self.a.hitbox_scale_h = 0.5
        self.a.hitbox_scale_w = 0.5
        self.a.set_on_mouse_down_listener(self.katt3)

        self.a2 = Arrow2()
        self.add_actor(self.a2)
        self.a2.x = 725
        self.a2.y = 250
        self.a2.w = 200
        self.a2.hitbox_scale_h = 0.5
        self.a2.hitbox_scale_w = 0.5
        self.a2.set_on_mouse_down_listener(self.katt4)

        self.s = Sellect()
        self.add_actor(self.s)
        self.s.x = 512.5
        self.s.y = 450
        self.s.w = 200
        self.s.set_on_mouse_down_listener(self.katt2)

    def katt(self, sender, event):
        print(sender)
        if event.button == 1:
            self.screen.game.set_screen(HawkProductions.menu.MenuScreen.MenuScreen())

    def katt2(self, sender, event):
        print(sender)
        if event.button == 1:
            self.screen.game.set_screen(HawkProductions.Game.GameScreen.GameScreen(self.puska))

    def katt3(self, sender, event):
        print(sender)
        if event.button == 1:
            self.puska = self.puska - 1
            if self.puska < 0:
                self.puska = 4
            self.frissites()
            # self.screen.game.set_screen(HawkProductions.Select.SelectScreen.SelectScreen2())

    def katt4(self, sender, event):
        print(sender)
        if event.button == 1:
            self.puska = self.puska + 1
            if self.puska > 4:
                self.puska = 0
            self.frissites()
            # self.screen.game.set_screen(HawkProductions.Select.SelectScreen.SelectScreen3())

    def frissites(self):
        if self.D == None:
            self.D = MyActor('image/goldengun1.png')
            self.add_actor(self.D)
        if self.puska == 0:
            self.D.image_url = 'image/goldengun1.png'
        if self.puska == 1:
            self.D.image_url = 'image/goldengun.png'
        if self.puska == 2:
            self.D.image_url = 'image/goldengun1.png'
        if self.puska == 3:
            self.D.image_url = 'image/goldengun.png'
        if self.puska == 4:
            self.D.image_url = 'image/goldengun1.png'
        self.D.x = 530
        self.D.y = 250
        self.D.width = 200

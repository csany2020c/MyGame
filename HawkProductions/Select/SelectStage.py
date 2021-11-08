import HawkProductions.menu.MenuScreen
from HawkProductions.Actors import *
from HawkProductions.Font import *
import HawkProductions.Game.GameScreen
import HawkProductions.Game2.GameScreen2
import HawkProductions.Music
import pygame
import HawkProductions.Select.SelectScreen


class SelectStgage(game.scene2d.MyStage):
    def __init__(self):
        super().__init__()
        pygame.mixer.init()
        pygame.mixer.music.load("../HawkProductions/Music/Sel.wav")
        pygame.mixer.music.play(-1)
        self.t = Arrow()
        self.add_actor(self.t)
        self.t.w = 125
        self.t.hitbox_scale_h = 0.5
        self.t.hitbox_scale_w = 0.5
        self.t.set_on_mouse_down_listener(self.katt)

        self.D = Deagle1()
        self.add_actor(self.D)
        self.D.x = 530
        self.D.y = 250
        self.D.width = 200

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
            self.screen.game.set_screen(HawkProductions.Game.GameScreen.GameScreen())

    def katt3(self, sender, event):
        print(sender)
        if event.button == 1:
            self.screen.game.set_screen(HawkProductions.Select.SelectScreen.SelectScreen2())

    def katt4(self, sender, event):
        print(sender)
        if event.button == 1:
            self.screen.game.set_screen(HawkProductions.Select.SelectScreen.SelectScreen3())


class SelectStage2(game.scene2d.MyStage):
    def __init__(self):
        super().__init__()
        pygame.mixer.init()
        pygame.mixer.music.load("../HawkProductions/Music/Sel.wav")
        pygame.mixer.music.play(-1)
        self.t = Arrow()
        self.add_actor(self.t)
        self.t.w = 125
        self.t.hitbox_scale_h = 0.5
        self.t.hitbox_scale_w = 0.5
        self.t.set_on_mouse_down_listener(self.katt)

        self.D = Deagle2()
        self.add_actor(self.D)
        self.D.x = 530
        self.D.y = 250
        self.D.width = 200

        self.a = Arrow()
        self.add_actor(self.a)
        self.a.x = 300
        self.a.y = 250
        self.a.w = 200
        self.a.hitbox_scale_h = 0.5
        self.a.hitbox_scale_w = 0.5
        self.a.set_on_mouse_down_listener(self.katt4)

        self.a2 = Arrow2()
        self.add_actor(self.a2)
        self.a2.x = 725
        self.a2.y = 250
        self.a2.w = 200
        self.a2.hitbox_scale_h = 0.5
        self.a2.hitbox_scale_w = 0.5
        self.a2.set_on_mouse_down_listener(self.katt3)

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
            self.screen.game.set_screen(HawkProductions.Game2.GameScreen2.GameScreen())

    def katt3(self, sender, event):
        print(sender)
        if event.button == 1:
            self.screen.game.set_screen(HawkProductions.Select.SelectScreen.SelectScreen())

    def katt4(self, sender, event):
        print(sender)
        if event.button == 1:
            self.screen.game.set_screen(HawkProductions.Select.SelectScreen.SelectScreen3())


class SelectStage3(game.scene2d.MyStage):
    def __init__(self):
        super().__init__()
        pygame.mixer.init()
        pygame.mixer.music.load("../HawkProductions/Music/Sel.wav")
        pygame.mixer.music.play(-1)
        self.t = Arrow()
        self.add_actor(self.t)
        self.t.w = 125
        self.t.hitbox_scale_h = 0.5
        self.t.hitbox_scale_w = 0.5
        self.t.set_on_mouse_down_listener(self.katt)

        self.D = Deagle3()
        self.add_actor(self.D)
        self.D.x = 500
        self.D.y = 250
        self.D.w = 300

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
            self.screen.game.set_screen(HawkProductions.Game2.GameScreen2.GameScreen())

    def katt3(self, sender, event):
        print(sender)
        if event.button == 1:
            self.screen.game.set_screen(HawkProductions.Select.SelectScreen.SelectScreen())

    def katt4(self, sender, event):
        print(sender)
        if event.button == 1:
            self.screen.game.set_screen(HawkProductions.Select.SelectScreen.SelectScreen2())

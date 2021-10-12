import Weathersim.faterlaszlo.f_screen1
import Weathersim.faterlaszlo.f_screen2
import Weathersim.faterlaszlo.f_screen3
import Weathersim.faterlaszlo.f_screen4
import Weathersim.faterlaszlo.f_screen_h
import game
from Weathersim.faterlaszlo.f_actors import *
from Weathersim.faterlaszlo.Arial import *
import pygame

class f_stage_m(game.scene2d.MyStage):
    def __init__(self):
        super().__init__()
        self.set_on_key_down_listener(self.key_down)
        self.bg = Bg1()
        self.add_actor(self.bg)
        self.bg.w = 1280
        self.bg.h = 720

        self.t = Arial()
        self.add_actor(self.t)
        self.t.set_text("Napsütés")
        self.t.x = 500
        self.t.y = 150
        self.t.set_on_mouse_down_listener(self.click)

        self.t1 = Arial()
        self.add_actor(self.t1)
        self.t1.set_text("Havas eső")
        self.t1.x = 500
        self.t1.y = 250
        self.t1.set_on_mouse_down_listener(self.click1)

        self.t2 = Arial()
        self.add_actor(self.t2)
        self.t2.set_text("Eső")
        self.t2.x = 500
        self.t2.y = 350
        self.t2.set_on_mouse_down_listener(self.click2)

        self.t3 = Arial()
        self.add_actor(self.t3)
        self.t3.set_text("Havazás")
        self.t3.x = 500
        self.t3.y = 450
        self.t3.set_on_mouse_down_listener(self.click3)

        self.t4 = Arial()
        self.add_actor(self.t4)
        self.t4.set_text("Kilépés")
        self.t4.x = 500
        self.t4.y = 600
        self.t4.set_on_mouse_down_listener(self.click4)

        self.t5 = Arial()
        self.add_actor(self.t5)
        self.t5.set_text("Weathersim")
        self.t5.set_font_underline("line")
        self.t5.x = 500
        self.t5.y = 50

        self.t6 = Arial()
        self.add_actor(self.t6)
        self.t6.set_text("Help")
        self.t6.x = 1160
        self.t6.y = 630
        self.t6.set_on_mouse_down_listener(self.click5)

    def key_down(self, sender, event):
        print(sender)
        print(event)
        if event.key == pygame.K_ESCAPE:
            print("Sikeresen be lett zárva")
            quit()
        if event.key == pygame.K_1:
            print("Nspsütés")
            self.screen.game.set_screen(Weathersim.faterlaszlo.f_screen1.f_screen1())
        if event.key == pygame.K_2:
            print("Havas eső")
            self.screen.game.set_screen(Weathersim.faterlaszlo.f_screen2.f_screen2())
        if event.key == pygame.K_3:
            print("Eső")
            self.screen.game.set_screen(Weathersim.faterlaszlo.f_screen3.f_screen3())
        if event.key == pygame.K_4:
            print("Havazás")
            self.screen.game.set_screen(Weathersim.faterlaszlo.f_screen4.f_screen4())

    def click(self, sender, event):
        print(sender)
        if event.button == 1:
            self.screen.game.set_screen(Weathersim.faterlaszlo.f_screen1.f_screen1())

    def click1(self, sender, event):
        print(sender)
        if event.button == 1:
            self.screen.game.set_screen(Weathersim.faterlaszlo.f_screen2.f_screen2())

    def click2(self, sender, event):
        print(sender)
        if event.button == 1:
            self.screen.game.set_screen(Weathersim.faterlaszlo.f_screen3.f_screen3())

    def click3(self, sender, event):
        print(sender)
        if event.button == 1:
            self.screen.game.set_screen(Weathersim.faterlaszlo.f_screen4.f_screen4())

    def click4(self, sender, event):
        print(sender)
        if event.button == 1:
            quit()

    def click5(self, sender, event):
        print(sender)
        if event.button == 1:
            self.screen.game.set_screen(Weathersim.faterlaszlo.f_screen_h.f_screen_h())

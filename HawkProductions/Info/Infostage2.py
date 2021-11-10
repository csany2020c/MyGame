from HawkProductions.Font import *
import game
import pygame
from HawkProductions.Actors import *
import HawkProductions.menu.MenuScreen
import HawkProductions.Info.InfoScreen


class Istage2(game.scene2d.MyStage):
    def __init__(self):
        super().__init__()
        self.t = Arial()
        self.add_actor(self.t)
        self.t.set_text("Írányitás")
        self.t.x = 520
        self.t.y = 50
        self.t.set_font_size(35)
        self.t.set_on_mouse_down_listener(self.valtas)

        self.t1 = Arial()
        self.add_actor(self.t1)
        self.t1.set_text("Játék menete")
        self.t1.x = 640
        self.t1.y = 50
        self.t1.set_font_size(35)
        self.t1.set_font_underline("line")

        self.Ba = Arrow()
        self.add_actor(self.Ba)
        self.Ba.width = 125

        self.Ba.set_on_mouse_down_listener(self.click1)
        self.set_on_key_down_listener(self.katt1)

    def click1(self, sender, event):
        print(sender)
        if event.button == 1:
            self.screen.game.set_screen(HawkProductions.menu.MenuScreen.MenuScreen())

    def katt1(self, sender, event):
        print(sender)
        if event.key == pygame.K_BACKSPACE:
            self.screen.game.set_screen(HawkProductions.menu.MenuScreen.MenuScreen())
        if event.key == pygame.K_ESCAPE:
            quit()

    def valtas(self, sender, event):
        if event.button == 1:
            self.screen.game.set_screen(HawkProductions.Info.InfoScreen.IScreen())

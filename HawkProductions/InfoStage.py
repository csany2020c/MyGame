from HawkProductions.Font import *
import game
import pygame
from HawkProductions.Actors import *
import HawkProductions.MenuScreen


class IStage(game.scene2d.MyStage):
    def __init__(self):
        super().__init__()
        self.H = Arial()
        self.add_actor(self.H)
        self.H.set_text("Az irányítás a bal klikk lenyomásával történik. A start-tal indul, quit-tel zárul.")
        self.H.x = 25
        self.H.y = 500
        self.H.set_font_size(45)

        self.H2 = Arial()
        self.add_actor(self.H2)
        self.H2.set_text("A balfelsö sarokban található icon-ra kattintva léphet a karakter menübe.")
        self.H2.x = 45
        self.H2.y = 250
        self.H2.set_font_size(45)

        self.Ba = Arrow()
        self.add_actor(self.Ba)
        self.Ba.width = 125

        self.Ba.set_on_mouse_down_listener(self.click1)
        self.set_on_key_down_listener(self.katt1)

    def click1(self, sender, event):
        print(sender)
        if event.button == 1:
            self.screen.game.set_screen(HawkProductions.MenuScreen.MenuScreen())

    def katt1(self, sender, event):
        print(sender)
        if event.key == pygame.K_BACKSPACE:

            self.screen.game.set_screen(HawkProductions.MenuScreen.MenuScreen())
        if event.key == pygame.K_ESCAPE:
            quit()

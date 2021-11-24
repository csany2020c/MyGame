from HawkProductions.Font import *
import game
import pygame
from HawkProductions.Actors import *
import HawkProductions.menu.MenuScreen
import HawkProductions.Info.InfoScreen2
import HawkProductions.image


class IStage(game.scene2d.MyStage):
    def __init__(self):
        super().__init__()
        self.t = Arial()
        self.add_actor(self.t)
        self.t.set_text("Írányitás")
        self.t.x = 520
        self.t.y = 50
        self.t.set_font_size(35)
        self.t.set_font_underline("line")

        self.t1 = Arial()
        self.add_actor(self.t1)
        self.t1.set_text("Készítők")
        self.t1.x = 640
        self.t1.y = 50
        self.t1.set_font_size(35)
        self.t1.set_on_mouse_down_listener(self.valtas1)

        self.H = Arial()
        self.add_actor(self.H)
        self.H.set_text("Az irányítás a W és az S billentyű nyomogatásával történik. A W a fel, az S a le.")
        self.H.x = 25
        self.H.y = 500
        self.H.set_font_size(25)

        self.H2 = Arial()
        self.add_actor(self.H2)
        self.H2.set_text("Pontokat érme felvételével lehet szerezni. 49 a maximum pontszám, aki azt eléri az a Flappy D Király.")
        self.H2.x = 45
        self.H2.y = 250
        self.H2.set_font_size(25)

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

    def valtas1(self, sender, event):
        if event.button == 1:
            self.screen.game.set_screen(HawkProductions.Info.InfoScreen2.IScreen2())



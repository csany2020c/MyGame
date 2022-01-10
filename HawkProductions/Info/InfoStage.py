from HawkProductions.font.Font import *
import game
from HawkProductions.Actors import *
import HawkProductions.menu.MenuScreen
import HawkProductions.Info.InfoScreen


class IStage(game.scene2d.MyStage):
    def __init__(self):
        super().__init__()
        self.bg = Sarga()
        self.add_actor(self.bg)
        self.bg.set_size(1280, 720)

        self.t = Strokes()
        self.add_actor(self.t)
        self.t.set_text("Irányitás")
        self.t.x = 450
        self.t.y = 50
        self.t.set_font_size(35)
        self.t.set_font_underline("line")
        self.t.set_color(0, 0, 0)

        self.t1 = Strokes()
        self.add_actor(self.t1)
        self.t1.set_text("Kreátorok")
        self.t1.x = 640
        self.t1.y = 50
        self.t1.set_font_size(35)
        self.t1.set_on_mouse_down_listener(self.valtas1)
        self.t1.set_color(0, 0, 0)

        self.H = Strokes()
        self.add_actor(self.H)
        self.H.set_text("A karakter a W-vel és az S-sel mozgatható. A W a fel, az S a le.")
        self.H.x = 235
        self.H.y = 380
        self.H.set_font_size(25)
        self.H.set_color(0, 0, 0)

        self.H2 = Strokes()
        self.add_actor(self.H2)
        self.H2.set_text("Pontokat érme felvételével lehet szerezni.")
        self.H2.x = 350
        self.H2.y = 125
        self.H2.set_font_size(25)
        self.H2.set_color(0, 0, 0)

        self.H2 = Strokes()
        self.add_actor(self.H2)
        self.H2.set_text("49 a maximum pontszám, aki azt eléri az a Flappy D Király.")
        self.H2.x = 300
        self.H2.y = 225
        self.H2.set_font_size(25)
        self.H2.set_color(0, 0, 0)

        self.Ba = Arrow()
        self.add_actor(self.Ba)
        self.Ba.width = 125

        self.Ba.set_on_mouse_down_listener(self.click1)
        self.set_on_key_down_listener(self.katt1)

        # self.L = Logo()
        # self.add_actor(self.L)
        # self.L.set_size(228, 172)
        # self.L.x = 850
        # self.L.y = 50

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
            self.screen.game.set_screen(HawkProductions.Info.InfoScreen.IScreen2())


class Istage2(game.scene2d.MyStage):
    def __init__(self):
        super().__init__()
        self.bg = Piros()
        self.add_actor(self.bg)
        self.bg.set_size(1290, 730)

        self.t = Strokes()
        self.add_actor(self.t)
        self.t.set_text("Irányitás")
        self.t.x = 450
        self.t.y = 50
        self.t.set_font_size(35)
        self.t.set_on_mouse_down_listener(self.valtas)

        self.t1 = Strokes()
        self.add_actor(self.t1)
        self.t1.set_text("Kreátorok")
        self.t1.x = 640
        self.t1.y = 50
        self.t1.set_font_size(35)
        self.t1.set_font_underline("line")

        self.Ba = Arrow()
        self.add_actor(self.Ba)
        self.Ba.width = 125

        self.Ba.set_on_mouse_down_listener(self.click1)
        self.set_on_key_down_listener(self.katt1)

        self.t2 = Strokes()
        self.add_actor(self.t2)
        self.t2.set_text("Fatér László")
        self.t2.x = 400
        self.t2.y = 160

        self.t3 = Strokes()
        self.add_actor(self.t3)
        self.t3.set_text("Ekler Dániel")
        self.t3.x = 400
        self.t3.y = 360

        self.t4 = Strokes()
        self.add_actor(self.t4)
        self.t4.set_text("Németh Csongor")
        self.t4.x = 350
        self.t4.y = 560

        # self.L = Logo()
        # self.add_actor(self.L)
        # self.L.set_size(228, 172)
        # self.L.x = 850
        # self.L.y = 50

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


from Weathersim.faterlaszlo.Arial import *
import Weathersim.faterlaszlo.f_screen_m
import game

class f_stage_h(game.scene2d.MyStage):
    def __init__(self):
        super().__init__()

        self.t = Arial()
        self.add_actor(self.t)
        self.t.set_text("A billentyűzet gombjainak használata")
        self.t.set_font_size(50)
        self.t.x = 360
        self.t.y = 0

        self.t1 = Arial()
        self.add_actor(self.t1)
        self.t1.set_text("Az 1-es gombra rányomva jelenik meg a napsütés")
        self.t1.x = 400
        self.t1.y = 100
        self.t1.set_font_size(30)

        self.t2 = Arial()
        self.add_actor(self.t2)
        self.t2.set_text("Az 2-es gombra rányomva jelenik meg a havas eső")
        self.t2.x = 400
        self.t2.y = 150
        self.t2.set_font_size(30)

        self.t3 = Arial()
        self.add_actor(self.t3)
        self.t3.set_text("Az 3-es gombra rányomva jelenik meg a eső")
        self.t3.x = 400
        self.t3.y = 200
        self.t3.set_font_size(30)

        self.t4 = Arial()
        self.add_actor(self.t4)
        self.t4.set_text("Az 4-es gombra rányomva jelenik meg a havazás")
        self.t4.x = 400
        self.t4.y = 250
        self.t4.set_font_size(30)

        self.t5 = Arial()
        self.add_actor(self.t5)
        self.t5.set_text("Köszönöm a végigolvasást")
        self.t5.x = 380
        self.t5.y = 300
        self.t5.set_font_size(30)

        self.t6 = Arial()
        self.add_actor(self.t6)
        self.t6.set_text("Vissza")
        self.t6.x = 0
        self.t6.y = 0
        self.t6.set_on_mouse_down_listener(self.click)

    def click(self, sneder, event):
        if event.button == 1:
            self.screen.game.set_screen(Weathersim.faterlaszlo.f_screen_m.f_stage_m())


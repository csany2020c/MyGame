import HawkProductions.MenuScreen
from HawkProductions.Actors import *
from HawkProductions.Font import *
import HawkProductions.Game.GameScreen


class SelectStgage(game.scene2d.MyStage):
    def __init__(self):
        super().__init__()

        self.D = Deagle_s()
        self.add_actor(self.D)
        self.D.x = 530
        self.D.y = 250
        self.D.width = 200

        self.t = Arrow()
        self.add_actor(self.t)
        self.t.set_on_mouse_down_listener(self.click)
        self.t.w = 125

        self.t1 = Sellect()
        self.add_actor(self.t1)
        self.t1.width = 200
        self.t1.x = 530
        self.t1.y = 400
        self.t1.set_on_mouse_down_listener(self.click1)

        self.arrow = Arrow()
        self.add_actor(self.arrow)
        self.arrow.x = 330
        self.arrow.y = 280
        self.arrow.w = 200
        self.arrow.set_on_mouse_down_listener(self.click2)

        self.arrow1 = Arrow()
        self.arrow1.x = 330
        self.arrow1.y = 280
        self.arrow1.w = 200
        self.arrow1.set_on_mouse_down_listener(self.click3)

        self.D1 = Deagle2()
        self.D1.x = 520
        self.D1.y = 280
        self.D1.w = 200

    def click(self, sender, event):
        if event.button == 1:
            self.screen.game.set_screen(HawkProductions.MenuScreen.MenuScreen())

    def click1(self, sender, event):
        if event.button == 1:
            self.screen.game.set_screen(HawkProductions.Game.GameScreen.GameScreen())

    def click2(self, sender, event):
        if event.button == 1:
            self.remove_actor(self.D)
            self.add_actor(self.D1)
            self.remove_actor(self.arrow)
            self.add_actor(self.arrow1)

    def click3(self, sender, event):
        if event.button == 1:
            self.remove_actor(self.D1)
            self.add_actor(self.D)
            self.remove_actor(self.arrow1)
            self.add_actor(self.arrow)



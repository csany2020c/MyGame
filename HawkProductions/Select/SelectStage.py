import HawkProductions.menu.MenuScreen
from HawkProductions.Actors import *
from HawkProductions.Font import *
import HawkProductions.Game.GameScreen
import HawkProductions.Game2.GameScreen2


class SelectStgage(game.scene2d.MyStage):
    def __init__(self):
        super().__init__()
        self.t = Arrow()
        self.add_actor(self.t)
        self.t.set_on_mouse_down_listener(self.click)
        self.t.w = 125

        self.D = Deagle1()
        self.add_actor(self.D)
        self.D.x = 530
        self.D.y = 250
        self.D.width = 200

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

        self.arrow3 = Arrow_r()
        self.add_actor(self.arrow3)
        self.arrow3.x = 730
        self.arrow3.y = 280
        self.arrow3.w = 200
        self.arrow3.set_on_mouse_down_listener(self.click3)

        self.arrow1 = Arrow()
        self.arrow1.x = 330
        self.arrow1.y = 280
        self.arrow1.w = 200
        self.arrow1.set_on_mouse_down_listener(self.click4)

        self.arrow2 = Arrow_r()
        self.arrow2.x = 730
        self.arrow2.y = 280
        self.arrow2.w = 200
        self.arrow2.set_on_mouse_down_listener(self.click5)

        self.arrow4 = Arrow()
        self.arrow4.x = 330
        self.arrow4.y = 280
        self.arrow4.w = 200

        self.arrow5 = Arrow_r()
        self.arrow5.x = 730
        self.arrow5.y = 280
        self.arrow5.w = 200

        self.D2 = Deagle2()
        self.D2.x = 520
        self.D2.y = 280
        self.D2.w = 200

        self.t2 = Sellect()
        self.t2.width = 200
        self.t2.x = 530
        self.t2.y = 400
        self.t2.set_on_mouse_down_listener(self.clickk1)

        self.D3 = Deagle3()
        self.D3.x = 520
        self.D3.y = 280
        self.D3.w = 200

    def click(self, sender, event):
        if event.button == 1:
            self.screen.game.set_screen(HawkProductions.menu.MenuScreen.MenuScreen())

    def click1(self, sender, event):
        if event.button == 1:
            self.screen.game.set_screen(HawkProductions.Game.GameScreen.GameScreen())

    def clickk1(self, sender, event):
        if event.button == 1:
            self.screen.game.set_screen(HawkProductions.Game2.GameScreen2.GameScreen())

    def click2(self, sender, event):
        if event.button == 1:
            self.remove_actor(self.D)
            self.add_actor(self.D2)
            self.remove_actor(self.arrow)
            self.add_actor(self.arrow1)
            self.add_actor(self.arrow2)
            self.remove_actor(self.arrow3)
            self.remove_actor(self.t1)
            self.add_actor(self.t2)

    def click3(self, sender, event):
        if event.button == 1:
            self.remove_actor(self.D)
            self.add_actor(self.D3)
            self.remove_actor(self.arrow)
            self.add_actor(self.arrow4)
            self.remove_actor(self.arrow3)
            self.add_actor(self.arrow5)

    def click4(self, sender, event):
        if event.button == 1:
            self.remove_actor(self.D2)
            self.add_actor(self.D3)
            self.remove_actor(self.arrow1)
            self.add_actor(self.arrow4)
            self.remove_actor(self.arrow2)
            self.add_actor(self.arrow5)

    def click5(self, sender, event):
        if event.button == 1:
            self.remove_actor(self.D2)
            self.add_actor(self.D)
            self.remove_actor(self.arrow1)
            self.add_actor(self.arrow)
            self.remove_actor(self.arrow2)
            self.add_actor(self.arrow3)
            self.remove_actor(self.t2)
            self.add_actor(self.t1)

from HawkProductions.Actors import *
import HawkProductions.Select.SelectScreen
import game


class WinStage(game.scene2d.MyStage):
    def __init__(self):
        super().__init__()
        self.a = Piros()#masik kep kell a Piros() helyere
        self.add_actor(self.a)

        self.arrow = Arrow()
        self.add_actor(self.arrow)
        self.arrow.x = 0
        self.arrow.y = -10
        self.arrow.w = 125
        self.arrow.set_on_mouse_down_listener(self.mouse_down)

    def mouse_down(self, sender, event):
        print(sender)
        if event.button == 1:
            self.screen.game.set_screen(HawkProductions.Select.SelectScreen.SelectScreen())
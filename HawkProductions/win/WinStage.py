from HawkProductions.Actors import *
import HawkProductions.Select.SelectScreen
from HawkProductions.font.Font import *
import game


class WinStage(game.scene2d.MyStage):
    def __init__(self):
        super().__init__()
        #self.a = Piros()
        #self.add_actor(self.a)

        self.a = Gameover()
        self.add_actor(self.a)
        self.a.set_text("!Nyertél!")
        self.a.x = 500
        self.a.y = 50
        self.a.set_font_size(250)

        self.b = Gameover()
        self.add_actor(self.b)
        self.b.set_text("Elérted a maximum pontszámot!")
        self.b.x = 440
        self.b.y = 180
        self.b.set_font_size(100)

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
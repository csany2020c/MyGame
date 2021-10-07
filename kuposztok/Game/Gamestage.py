import game
import kuposztok
from kuposztok.Game.GameActor import *
from kuposztok.Game.GameActor import *


class GameStage(game.scene2d.MyStage):

    def __init__(self):
        super().__init__()
        bg = BgActor()
        a = MyyActor()
        a.y = 0
        self.add_actor(bg)
        self.add_actor(a)
        self.button1 = Visszagomb()
        self.add_actor(self.button1)
        self.button1.width = 125
        self.button1.height = 75
        self.button1.y = 0
        self.button1.x = 0

        self.button1.set_on_mouse_down_listener(self.Klikk1)

    def Klikk1(self, sender, event):
        if event.button == 1:
            self.screen.game.set_screen(kuposztok.Menu.MenuScreen.MenuScreen())
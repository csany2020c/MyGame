import game
import kuposztok
from kuposztok.Menu.MenuBgActor import *
from kuposztok.Game.GameScreen import *
from kuposztok.Credit.CreditScreen import *


class MenuStage(game.scene2d.MyStage):

    def __init__(self):
        super().__init__()
        bg = MenuActor()
        self.add_actor(bg)

        self.button1 = creditact()
        self.add_actor(self.button1)
        self.button1.width = 125
        self.button1.height = 75
        self.button1.y = 800
        self.button1.x = 200

        self.button2 = exitact()
        self.add_actor(self.button2)
        self.button2.width = 125
        self.button2.height = 75
        self.button2.y = 800
        self.button2.x = 1600

        self.button3 = playact()
        self.add_actor(self.button3)
        self.button3.width = 125
        self.button3.height = 75
        self.button3.y = 500
        self.button3.x = 900

        self.button1.set_on_mouse_down_listener(self.Klikk1)
        self.button2.set_on_mouse_down_listener(self.Klikk2)
        self.button3.set_on_mouse_down_listener(self.Klikk3)

    def Klikk1(self, sender, event):
        if event.button == 1:
            self.screen.game.set_screen(kuposztok.Credit.CreditScreen.CreditScreen())

    def Klikk2(self, sender, event):
        if event.button == 1:
            self.screen.game.set_screen(quit())

    def Klikk3(self, sender, event):
        if event.button == 1:
            self.screen.game.set_screen(kuposztok.Game.GameScreen.GameScreen())

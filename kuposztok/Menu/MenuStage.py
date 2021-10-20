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
        height = pygame.display.get_surface().get_height()
        width = pygame.display.get_surface().get_width()
        bg.height = height
        bg.width = width
        print(width)

        button1 = Button1()
        button2 = Button2()
        button3 = Button3()
        button2.x = 600
        button2.y = 400
        button3.y = 500
        button3.x = 600
        button1.y = 300
        button1.x = 600
        self.add_actor(bg)
        self.add_actor(button3)
        self.add_actor(button1)
        self.add_actor(button2)

        button1.set_on_mouse_down_listener(self.Klikk1)
        button2.set_on_mouse_down_listener(self.Klikk2)
        button3.set_on_mouse_down_listener(self.Klikk3)

    def Klikk1(self, sender, event):
        if event.button == 1:
            self.screen.game.set_screen(kuposztok.Credit.CreditScreen.CreditScreen())

    def Klikk2(self, sender, event):
        if event.button == 1:
            self.screen.game.set_screen(quit())

    def Klikk3(self, sender, event):
        if event.button == 1:
            self.screen.game.set_screen(kuposztok.Game.GameScreen.GameScreen())

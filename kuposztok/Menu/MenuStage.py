import game
import kuposztok
from kuposztok.Menu.MenuBgActor import *
from kuposztok.Game.GameScreen import *
from kuposztok.Credit.CreditScreen import CreditScreen


class MenuStage(game.scene2d.MyStage):

    def __init__(self):
        super().__init__()
        bg = MenuActor()
        self.add_actor(bg)
        self.height = pygame.display.get_surface().get_height()
        self.width = pygame.display.get_surface().get_width()
        bg.height = self.height
        bg.width = self.width
        print(self.width)
        print(self.height)
        self.Ver = game.scene2d.MyLabel("Ver.:1.0.1")
        self.add_actor(self.Ver)
        self.Ver.x = self.width - 250
        self.Ver.y = self.height - 50
        self.Ver.width = 100
        self.Ver.height = 50
        button1 = Button1()
        button2 = Button2()
        button3 = Button3()
        button2.x = 000
        button2.y = 400
        button3.y = 500
        button3.x = 400
        button1.y = 300
        button1.x = 800
        self.add_actor(bg)
        self.add_actor(button3)
        self.add_actor(button1)
        self.add_actor(button2)


        button1.set_on_mouse_down_listener(self.Klikk1)
        button2.set_on_mouse_down_listener(self.Klikk2)
        button3.set_on_mouse_down_listener(self.Klikk3)

    def Klikk1(self, sender, event):
        if event.button == 1:
            self.screen.game.set_screen(kuposztok.Game.GameScreen.GameScreen())

    def Klikk2(self, sender, event):
        if event.button == 1:
            self.screen.game.set_screen(quit())

    def Klikk3(self, sender, event):
        if event.button == 1:
            self.screen.game.set_screen(kuposztok.Credit.CreditScreen.CreditScreen())





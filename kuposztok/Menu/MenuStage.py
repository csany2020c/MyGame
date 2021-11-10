import game
import kuposztok
from kuposztok.CaraValt.CaraValtScreen import CaraValtScreen
from kuposztok.Credit.CreditScreen import CreditScreen
from kuposztok.Menu.MenuBgActor import *


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
        self.Ver = game.scene2d.MyLabel("Ver.:1.0.4")
        self.Ver.set_color(0, 0, 0)
        self.add_actor(self.Ver)
        self.Ver.x = self.width - 250
        self.Ver.y = self.height - 50
        self.Ver.width = 100
        self.Ver.height = 50
        self.Ver.get_hitbox()
        self.Ver.hitbox_scale_w = 0.4
        self.Ver.hitbox_scale_h = 0.4
        self.Ver.hitbox_shape = game.simpleworld.ShapeType.Circle
        self.Ver.debug = True
        button1 = Button1()
        button2 = Button2()
        button3 = Button3()
        button2.x = self.width / 2 - 230
        button2.y = self.height / 2.5 + 130
        button3.y = self.height / 2.5 - 60
        button3.x = self.width / 2 - 150
        button1.y = self.height / 2 - 320
        button1.x = self.width / 2 - 190
        self.add_actor(bg)
        self.add_actor(button3)
        self.add_actor(button1)
        self.add_actor(button2)

        self.set_on_key_down_listener(self.katt)
        button1.set_on_mouse_down_listener(self.Klikk1)
        button2.set_on_mouse_down_listener(self.Klikk2)
        button3.set_on_mouse_down_listener(self.Klikk3)

    def Klikk1(self, sender, event):
        if event.button == 1:
            self.screen.game.set_screen(kuposztok.CaraValt.CaraValtScreen.CaraValtScreen())

    def Klikk2(self, sender, event):
        if event.button == 1:
            self.screen.game.set_screen(quit())

    def Klikk3(self, sender, event):
        if event.button == 1:
            self.screen.game.set_screen(kuposztok.Credit.CreditScreen.CreditScreen())

    def katt(self, sender, event):
        if event.key == pygame.K_ESCAPE:
            quit()





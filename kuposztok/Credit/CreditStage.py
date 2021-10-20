import kuposztok.Credit.CreditScreen
import pygame
from kuposztok.Credit.CreditActors import *
from kuposztok.Menu.MenuScreen import *


class CreditStage(game.scene2d.MyStage):

    def __init__(self):
        super().__init__()
        self.height = pygame.display.get_surface().get_height()
        self.width = pygame.display.get_surface().get_width()
        creditact = Creditlist()
        self.add_actor(creditact)
        creditact.width = self.width
        creditact.height = self.height

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



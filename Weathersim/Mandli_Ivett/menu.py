from Weathersim.Mandli_Ivett.esos import *
from Weathersim.Mandli_Ivett.havasesos import *
from Weathersim.Mandli_Ivett.havazos import *
from Weathersim.Mandli_Ivett.napsuteses import *
import pygame


class Menu(game.scene2d.MyGame):

    def __init__(self, width: int = 1280, height: int = 720, autorun: bool = False, autosize: bool = False,
                 debug: bool = False):
        super().__init__(width, height, autorun, autosize, debug)
        self.set_on_key_down_listener(self.key_down)
        self.screen = HavazosScreen()

    def key_down(self, sender, event):
        print(event)
        if event.key == pygame.K_1:
            self.screen = HavazosScreen()
        if event.key == pygame.K_2:
            self.screen = NapsutesesScreen()
        if event.key == pygame.K_3:
            self.screen = HavasesosScreen()
        if event.key == pygame.K_4:
            self.screen = EsosScreen()


Menu().run()

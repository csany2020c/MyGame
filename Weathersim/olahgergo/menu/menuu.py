import pygame
import Weathersim.olahgergo.Nap.napscreen
from Weathersim.olahgergo.actors import *
import Weathersim.olahgergo.menu.idojarasm
from Weathersim.olahgergo.menu.idojarasm import *


class MenuStage(game.scene2d.MyStage):

    def __init__(self):
        super().__init__()
        self.menuk = menukep()
        self.add_actor(self.menuk)
        self.menuk.width = 1280
        self.menuk.height = 720

        self.kilepes = kilep()
        self.add_actor(self.kilepes)
        self.kilepes.height = 46
        self.kilepes.width = 230
        self.kilepes.y = 402
        self.kilepes.x = 525

        self.imenu2 = idojarasok()
        self.add_actor(self.imenu2)
        self.imenu2.height = 46
        self.imenu2.width = 466
        self.imenu2.y = 272
        self.imenu2.x = 407

        self.set_on_key_down_listener(self.key_down)
        self.kilepes.set_on_mouse_down_listener(self.asd2)
        self.imenu2.set_on_mouse_down_listener(self.asd3)

    def asd2(self, sender, event):
        if event.button == 1:
            quit()

    def asd3(self, sender, event):
        if event.button == 1:
            self.screen.game.set_screen(Weathersim.olahgergo.menu.idojarasm.IMenuScreen())



    def key_down(self, sender, event):
        if event.key == pygame.K_ESCAPE:
            quit()


class MenuScreen(game.scene2d.MyScreen):

    def __init__(self):
        super().__init__()
        self.set_background_color(0, 0, 0)
        self.add_stage(MenuStage())
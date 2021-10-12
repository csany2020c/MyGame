import pygame
import Weathersim.olahgergo.Nap.napscreen
from Weathersim.olahgergo.Nap.napscreen import *
from Weathersim.olahgergo.actors import *

class MenuStage(game.scene2d.MyStage):

    def __init__(self):
        super().__init__()
        self.menuk = menukep()
        self.add_actor(self.menuk)
        self.menuk.width = 1280
        self.menuk.height = 720

        self.semmi = semmi()
        self.add_actor(self.semmi)
        self.semmi.height = 97
        self.semmi.width = 299
        self.semmi.y = 408
        self.semmi.x = 6

        self.semmi.set_on_mouse_down_listener(self.asd1)

    def asd1(self, sender, event):
        if event.button == 1:
            self.screen.game.set_screen(Weathersim.olahgergo.Nap.napscreen.NapScreen)

    def key_down(self, sender, event):
        if event.key == pygame.K_ESCAPE:
            quit()

class MenuScreen(game.scene2d.MyScreen):

    def __init__(self):
        super().__init__()
        self.set_background_color(0, 0, 0)
        self.add_stage(MenuStage())
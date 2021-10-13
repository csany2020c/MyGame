import pygame
import Weathersim.olahgergo.Nap.napscreen
from Weathersim.olahgergo.actors import *
import Weathersim.olahgergo.havazas
import Weathersim.olahgergo.havazas.hoscreen

class IMenuStage(game.scene2d.MyStage):

    def __init__(self):
        super().__init__()
        self.imenukk = menukep()
        self.add_actor(self.imenukk)
        self.imenukk.width = 1280
        self.imenukk.height = 720

        self.semmi = semmi()
        self.add_actor(self.semmi)
        self.semmi.height = 46
        self.semmi.width = 466
        self.semmi.y = 294
        self.semmi.x = 405

        self.set_on_key_down_listener(self.key_down)
        self.semmi.set_on_mouse_down_listener(self.asd1)

    def asd1(self, sender, event):
        if event.button == 1:
            self.screen.game.set_screen(Weathersim.olahgergo.havazas.hoscreen.HavStage())


    def key_down(self, sender, event):
        if event.key == pygame.K_ESCAPE:
            quit()

class IMenuScreen(game.scene2d.MyScreen):

    def __init__(self):
        super().__init__()
        self.set_background_color(0, 0, 0)
        self.add_stage(IMenuStage())


import pygame
import Weathersim.olahgergo.Nap.napscreen
from Weathersim.olahgergo.actors import *
from Weathersim.olahgergo.havazas.hoscreen import HavScreen
from Weathersim.olahgergo.havaseso.havasesoscreen import HavEsoScreen
from Weathersim.olahgergo.eso.esoscreen import EsoScreen


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

        self.semmi2 = semmi()
        self.add_actor(self.semmi2)
        self.semmi2.height = 46
        self.semmi2.width = 466
        self.semmi2.y = 520
        self.semmi2.x = 405

        self.semmi3 = semmi()
        self.add_actor(self.semmi3)
        self.semmi3.height = 46
        self.semmi3.width = 466
        self.semmi3.y = 520
        self.semmi3.x = 800

        self.set_on_key_down_listener(self.key_down)
        self.semmi.set_on_mouse_down_listener(self.asd1)
        self.semmi2.set_on_mouse_down_listener(self.asd2)
        self.semmi3.set_on_mouse_down_listener(self.asd3)

    def asd1(self, sender, event):
        if event.button == 1:
            self.screen.game.set_screen(Weathersim.olahgergo.havazas.hoscreen.HavScreen())

    def asd2(self, sender, event):
        if event.button == 1:
            self.screen.game.set_screen(Weathersim.olahgergo.havaseso.havasesoscreen.HavEsoScreen())

    def asd3(self, sender, event):
        if event.button == 1:
            self.screen.game.set_screen(Weathersim.olahgergo.eso.esoscreen.EsoScreen())


    def key_down(self, sender, event):
        if event.key == pygame.K_ESCAPE:
            quit()

class IMenuScreen(game.scene2d.MyScreen):

    def __init__(self):
        super().__init__()
        self.set_background_color(0, 0, 0)
        self.add_stage(IMenuStage())


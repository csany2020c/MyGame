import pygame
import Weathersim.olahgergo.Nap.napscreen
from Weathersim.olahgergo.actors import *
from Weathersim.olahgergo.havazas.hoscreen import HavScreen
from Weathersim.olahgergo.havaseso.havasesoscreen import HavEsoScreen
from Weathersim.olahgergo.eso.esoscreen import EsoScreen


class IMenuStage(game.scene2d.MyStage):

    def __init__(self):
        super().__init__()
        self.imenukk = imenukep()
        self.add_actor(self.imenukk)
        self.imenukk.width = 1280
        self.imenukk.height = 720

        self.havazask = havazaskatt()
        self.add_actor(self.havazask)
        self.havazask.height = 46
        self.havazask.width = 1320
        self.havazask.y = 55
        self.havazask.x = 136

        self.esosk = esoskatt()
        self.add_actor(self.esosk)
        self.esosk.height = 46
        self.esosk.width = 1320
        self.esosk.y = 55
        self.esosk.x = -206

        self.naposk = naposkatt()
        self.add_actor(self.naposk)
        self.naposk.height = 46
        self.naposk.width = 1320
        self.naposk.y = 55
        self.naposk.x = -522

        self.havasesosk = havasesoskatt()
        self.add_actor(self.havasesosk)
        self.havasesosk.height = 46
        self.havasesosk.width = 1320
        self.havasesosk.y = 55
        self.havasesosk.x = 472

        self.set_on_key_down_listener(self.key_down)
        self.havazask.set_on_mouse_down_listener(self.asd1)
        self.havasesosk.set_on_mouse_down_listener(self.asd2)
        self.esosk.set_on_mouse_down_listener(self.asd3)
        self.naposk.set_on_mouse_down_listener(self.asd4)

    def asd1(self, sender, event):
        if event.button == 1:
            self.screen.game.set_screen(Weathersim.olahgergo.havazas.hoscreen.HavScreen())

    def asd2(self, sender, event):
        if event.button == 1:
            self.screen.game.set_screen(Weathersim.olahgergo.havaseso.havasesoscreen.HavEsoScreen())

    def asd3(self, sender, event):
        if event.button == 1:
            self.screen.game.set_screen(Weathersim.olahgergo.eso.esoscreen.EsoScreen())

    def asd4(self, sender, event):
        if event.button == 1:
            self.screen.game.set_screen(Weathersim.olahgergo.Nap.napscreen.NapScreen())


    def key_down(self, sender, event):
        if event.key == pygame.K_ESCAPE:
            quit()

class IMenuScreen(game.scene2d.MyScreen):

    def __init__(self):
        super().__init__()
        self.set_background_color(0, 0, 0)
        self.add_stage(IMenuStage())


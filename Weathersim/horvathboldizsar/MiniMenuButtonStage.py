import pygame
import Weathersim.horvathboldizsar.GameScreen
from Weathersim.horvathboldizsar.MiniMenuActors import *

class MiniStage(game.scene2d.MyStage):

    def __init__(self):
        super().__init__()

        self.menubutton = menubutton()
        self.menubutton.width = 150
        self.menubutton.y = 650
        self.menubutton.x = 1125
        self.add_actor(self.menubutton)
        self.menubutton.set_on_mouse_down_listener(self.MenuButtonClick)

        self.minimenubutton = minimenubutton()
        self.minimenubutton.height = 50
        self.add_actor(self.minimenubutton)
        # self.minimenubutton.set_on_mouse_down_listener(self.MenuButtonClick)

        self.mininapbutton = mininapbutton()
        self.mininapbutton.height = 50
        self.mininapbutton.x = 50
        self.add_actor(self.mininapbutton)
        # self.mininapbutton.set_on_mouse_down_listener(self.MiniNapButtonClick)

        self.miniesobutton = miniesobutton()
        self.miniesobutton.height = 50
        self.miniesobutton.x = 100
        self.add_actor(self.miniesobutton)
        # self.miniesobutton.set_on_mouse_down_listener(self.MiniEsoButtonClick)

        self.minihavasesobutton = minihavasesobutton()
        self.minihavasesobutton.height = 50
        self.minihavasesobutton.x = 150
        self.add_actor(self.minihavasesobutton)
        # self.minihavasesobutton.set_on_mouse_down_listener(self.MiniHavasesoButtonClick)

        self.minihobutton = minihobutton()
        self.minihobutton.height = 50
        self.minihobutton.x = 200
        self.add_actor(self.minihobutton)
        # self.minihobutton.set_on_mouse_down_listener(self.MiniHoButtonClick)

    def MenuButtonClick(self, sender, event):
        if event.button == 1:
            self.screen.game.set_screen(Weathersim.horvathboldizsar.MenuScreen.MenuScreen())
    #
    # def MiniNapButtonClick(self, sender, event):
    #     if event.button == 1:
    #         self.screen.game.set_screen(Weathersim.horvathboldizsar.GameScreen.NaposStage())
    #
    # def MiniEsoButtonClick(self, sender, event):
    #     if event.button == 1:
    #         self.screen.game.set_screen(Weathersim.horvathboldizsar.GameScreen.EsosStage())
    #
    # def MiniHavasesoButtonClick(self, sender, event):
    #     if event.button == 1:
    #         self.screen.game.set_screen(Weathersim.horvathboldizsar.GameScreen.HavasesosStage())
    #
    # def MiniHoButtonClick(self, sender, event):
    #     if event.button == 1:
    #         self.screen.game.set_screen(Weathersim.horvathboldizsar.GameScreen.HavasStage())

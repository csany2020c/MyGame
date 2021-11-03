import game
import pygame
from Weathersim.marcontamas.HavasActorok import *
import Weathersim.marcontamas.MenuScreen
import Weathersim.marcontamas.EsosScreen
import Weathersim.marcontamas.HavasEsoScreen


class HoStage(game.scene2d.MyStage):
    def __init__(self):
        super().__init__()
        # landscape
        self.a = LandScape()
        self.add_actor(self.a)
        self.a.z_index = 0
        # felhos
        self.c = Eg()
        self.add_actor(self.c)
        self.c.z_index = -1
        # ho
        for i in range(100):
            self.snow = Snow()
            self.add_actor(self.snow)

        self.snow.z_index = 1

        self.set_on_key_down_listener(self.billentyu)

    def billentyu(self, sender, event):
        if event.key == pygame.K_BACKSPACE:
            self.screen.game.set_screen(Weathersim.marcontamas.MenuScreen.MenuScreen())
        if event.key == pygame.K_ESCAPE:
            quit()
        if event.key == pygame.K_LEFT:
            self.screen.game.set_screen(Weathersim.marcontamas.EsosScreen.EsoScreen())
        if event.key == pygame.K_RIGHT:
            self.screen.game.set_screen(Weathersim.marcontamas.HavasEsoScreen.HavasEsoScreen())
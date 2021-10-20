import game
import pygame
from Weathersim.marcontamas.EsoActorok import *
import Weathersim.marcontamas.MenuScreen
import Weathersim.marcontamas.NaposScreen
import Weathersim.marcontamas.HoScreen

class EsoStage(game.scene2d.MyStage):
    def __init__(self):
        super().__init__()
        #landscape
        self.a = Alap()
        self.add_actor(self.a)
        self.a.z_index = 0
        #felhos
        self.c = Felhos()
        self.add_actor(self.c)
        self.c.z_index = -1
        #eso
        for i in range(30):
            self.rain = Eso()
            self.add_actor(self.rain)

        self.rain.z_index = 1

        self.set_on_key_down_listener(self.billentyu)

    def billentyu(self, sender, event):
        if event.key == pygame.K_BACKSPACE:
            self.screen.game.set_screen(Weathersim.marcontamas.MenuScreen.MenuScreen())
        if event.key == pygame.K_ESCAPE:
            quit()
        if event.key == pygame.K_LEFT:
            self.screen.game.set_screen(Weathersim.marcontamas.NaposScreen.NaposScreen())
        if event.key == pygame.K_RIGHT:
            self.screen.game.set_screen(Weathersim.marcontamas.HoScreen.HoScreen())
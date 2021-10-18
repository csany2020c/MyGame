import pygame
import game
from Weathersim.marcontamas.NaposActorok import *
import Weathersim.marcontamas.MenuScreen
import Weathersim.marcontamas.EsosScreen
import Weathersim.marcontamas.HavasEsoScreen

class NaposStage(game.scene2d.MyStage):
    def __init__(self):
        super().__init__()
        #landscape
        self.a = Alap()
        self.add_actor(self.a)
        self.a.z_index = 1
        #ég
        self.s = Eg()
        self.add_actor(self.s)
        self.s.z_index = -1
        #nap
        self.n = Nap()
        self.add_actor(self.n)
        self.n.z_index = 0

        #listenerek
        self.set_on_key_down_listener(self.billentyu)

    def billentyu(self,sender,event):
        if event.key == pygame.K_BACKSPACE:
            self.screen.game.set_screen(Weathersim.marcontamas.MenuScreen.MenuScreen())
        if event.key == pygame.K_ESCAPE:
            quit()
        if event.key == pygame.K_RIGHT:
            self.screen.game.set_screen(Weathersim.marcontamas.EsosScreen.EsoScreen())
        if event.key == pygame.K_LEFT:
            self.screen.game.set_screen(Weathersim.marcontamas.HavasEsoScreen.HavasEsoScreen())
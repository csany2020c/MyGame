import game
import pygame
from HawkProductions.Font import *
import HawkProductions.menu.MenuScreen


class OverStage(game.scene2d.MyStage):
    def __init__(self):
        super().__init__()
        self.F = Arial()
        self.add_actor(self.F)
        self.F.set_text("Game Over")
        self.F.set_color(204, 0, 0)
        self.F.x = 500
        self.F.y = 250

        self.g = Arial()
        self.add_actor(self.g)
        self.g.set_text("Try again!")
        self.g.set_color(204, 0, 0)
        self.g.x = 500
        self.g.y = 310

        self.g.set_on_mouse_down_listener(self.click)

    def click(self, sender, event):
        print(sender)
        if event.button == 1:
            self.screen.game.set_screen(HawkProductions.menu.MenuScreen.MenuScreen())
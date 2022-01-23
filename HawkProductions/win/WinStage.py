from HawkProductions.Actors import *
import HawkProductions.Select.SelectScreen
from HawkProductions.font.Font import *
import HawkProductions.menu.MenuScreen
import game
import pygame


class WinStage(game.scene2d.MyStage):
    def __init__(self):
        super().__init__()
        self.c = Win()
        self.add_actor(self.c)
        self.c.set_size(1280, 720)

        self.arrow = Arrow_w()
        self.add_actor(self.arrow)
        self.arrow.x = 0
        self.arrow.y = 10
        self.arrow.w = 125
        self.arrow.set_on_mouse_down_listener(self.mouse_down)
        self.set_on_key_down_listener(self.button_down)

    def mouse_down(self, sender, event):
        print(sender)
        if event.button == 1:
            self.screen.game.set_screen(HawkProductions.Select.SelectScreen.SelectScreen())

    def button_down(self, sender, event):
        print(sender)
        if event.key == pygame.K_BACKSPACE:
            self.screen.game.set_screen(HawkProductions.menu.MenuScreen.MenuScreen())



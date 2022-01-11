import retardszisza.Stage
import game
import pygame
from retardszisza.menu_halal.HalalActor import *
from retardszisza.Screen import *
from retardszisza.menu_halal.MenuActor import *
from retardszisza.Screen import *
from retardszisza.menu_halal.MenuScreen import *

class halalstage(game.scene2d.MyStage):
    def __init__(self):
        super().__init__()
        self.hatter = halalhatter()
        self.restart = restartgomb()
        self.kilepes = kilepesactor()
        self.fomenu = fomenugomb()
        self.add_actor(self.restart)
        self.add_actor(self.kilepes)
        self.add_actor(self.hatter)

        self.fomenu.x = 500
        self.fomenu.y = 150

        self.restart.x = 500
        self.restart.y = 300

        self.kilepes.x = 500
        self.kilepes.y = 450

        self.kilepes.set_on_mouse_down_listener(self.button_down)
        self.restart.set_on_mouse_down_listener(self.button_down2)
        self.fomenu.set_on_mouse_down_listener(self.button_down3)

    def button_down(self, sender, event):
        if event.button == 1:
            quit()

    def button_down2(self, sender, event):
        if event.button == 1:
            self.screen.game.set_screen(menuscreen())

    def button_down3(self, sender, event):
        if event.button == 1:
            self.screen.game.set_screen(menuscreen())

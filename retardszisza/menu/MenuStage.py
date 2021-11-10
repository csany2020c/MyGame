import retardszisza.Stage
import game
import pygame
from retardszisza.menu.MenuActor import *
from retardszisza.Screen import *

class menustage(game.scene2d.MyStage):
    def __init__(self):
        super().__init__()
        self.actor1 = startactor()
        self.actor2 = kilepesactor()
        self.add_actor(self.actor1)
        self.add_actor(self.actor2)
        self.actor1.x = 500
        self.actor1.y = 200
        self.actor2.x = 500
        self.actor2.y = 400

        self.actor1.set_on_mouse_down_listener(self.button_down)
        self.actor2.set_on_mouse_down_listener(self.button_down2)

    def button_down(self, sender, event):
        if event.button == 1:
            self.screen.game.set_screen(retardszisza.Screen.GameScreen())

    def button_down2(self, sender, event):
        if event.button == 1:
            quit()
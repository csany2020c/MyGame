import game
import pygame
from Weathersim.bobicsbarnabas.actors import *

class napsutesstage(game.scene2d.MyStage):

    def __init__(self):
        super().__init__()
        self.nap = sunActor()
        self.hatter = sunnyActor()
        self.hatter2 = landscapeActor()
        self.add_actor(self.hatter)
        self.add_actor(self.nap)
        self.add_actor(self.hatter2)
        self.nap.z_index = 1
        self.hatter.z_index = 0
        self.hatter2.z_index = 2
        self.nap.y = -100
        self.nap.x = 100

        self.set_on_key_down_listener(self.key_down)

    def key_down(self, sender, event):
        if event.key == pygame.K_ESCAPE:
            quit()

class havazasstage(game.scene2d.MyStage):

    def __init__(self):
        super().__init__()
        self.add_actor()

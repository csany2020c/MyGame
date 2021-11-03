import Weathersim.olahgergo.menu.idojarasm
import Weathersim.olahgergo.menu.menuu
from Weathersim.olahgergo.actors import *
import pygame


class EsoStage(game.scene2d.MyStage):

    def __init__(self):
        super().__init__()
        self.hatter = hatterkep()
        self.hatter.width = 1280
        self.hatter.height = 720
        self.hatter.z_index = 3
        self.feg = felhoeg()
        self.feg.width = 1920
        self.feg.height = 1300
        self.feg.z_index = 1
        self.add_actor(self.hatter)
        self.add_actor(self.feg)

        for i in range(40):
            self.esoo = Eso()
            size = random.randint(a=20, b=100)
            self.esoo.height = size
            self.esoo.width = size
            self.esoo.x = random.randint(a=0, b=1280)
            self.esoo.y = random.randint(a=-0, b=720)
            self.add_actor(self.esoo)

        self.zsa = vissza()
        self.add_actor(self.zsa)
        self.zsa.width = 125
        self.zsa.height = 75
        self.zsa.y = 0
        self.zsa.x = 0

        self.set_on_key_down_listener(self.key_down)
        self.zsa.set_on_mouse_down_listener(self.asd4)

    def asd4(self, sender, event):
        if event.button == 1:
            self.screen.game.set_screen(Weathersim.olahgergo.menu.idojarasm.IMenuScreen())


    def key_down(self, sender, event):
        if event.key == pygame.K_ESCAPE:
            self.screen.game.set_screen(Weathersim.olahgergo.menu.idojarasm.IMenuScreen())
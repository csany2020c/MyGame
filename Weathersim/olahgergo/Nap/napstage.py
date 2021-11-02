import Weathersim.olahgergo.menu.idojarasm
from Weathersim.olahgergo.actors import *
import pygame

class NapStage(game.scene2d.MyStage):

    def __init__(self):
        super().__init__()
        self.hatter = hatterkep()
        self.hatter.width = 1280
        self.hatter.height = 720
        self.hatter.z_index = 3
        self.eg = vilagoseg()
        self.eg.width = 1920
        self.eg.height = 1300
        self.eg.z_index = 1
        self.nap = napnap()
        self.nap.width = 500
        self.nap.height = 500
        self.nap.y = 50
        self.nap.x = 500
        self.nap.z_index = 2
        self.add_actor(self.hatter)
        self.add_actor(self.eg)
        self.add_actor(self.nap)

        self.zsa = vissza()
        self.add_actor(self.zsa)
        self.zsa.width = 125
        self.zsa.height = 75
        self.zsa.y = 0
        self.zsa.x = 0

        self.set_on_key_down_listener(self.key_down)
        self.zsa.set_on_mouse_down_listener(self.asd2)

    def asd2(self, sender, event):
        if event.button == 1:
            self.screen.game.set_screen(Weathersim.olahgergo.menu.idojarasm.IMenuScreen())

    def key_down(self, sender, event):
        if event.key == pygame.K_ESCAPE:
            quit()



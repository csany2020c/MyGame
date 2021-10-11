import Weathersim.olahgergo.menu.menuu
from Weathersim.olahgergo.actors import *

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
        self.nap.width = 400
        self.nap.height = 400
        self.nap.y = -100
        self.nap.x = 500
        self.nap.z_index = 2
        self.add_actor(self.hatter)
        self.add_actor(self.eg)
        self.add_actor(self.nap)

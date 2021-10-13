import Weathersim.olahgergo.menu.idojarasm
import Weathersim.olahgergo.menu.menuu
from Weathersim.olahgergo.actors import *


class HavStage(game.scene2d.MyStage):

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


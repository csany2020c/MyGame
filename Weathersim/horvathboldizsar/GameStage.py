import game
from Weathersim.horvathboldizsar.GameActors import *

class NaposStage(game.scene2d.MyStage):

    def __init__(self):
        super().__init__()
        self.erdo = erdo()
        self.erdo.z_index = 2
        self.add_actor(self.erdo)
        self.naposeg = naposeg()
        self.naposeg.z_index = 1
        self.add_actor(self.naposeg)

class FelhosStage(game.scene2d.MyStage):
    def __init__(self):
        super().__init__()
        self.erdo = erdo()
        self.erdo.z_index = 2
        self.add_actor(self.erdo)
        self.felhoseg = felhoseg()
        self.felhoseg.z_index = 1
        self.add_actor(self.felhoseg)


class EsosStage(game.scene2d.MyStage, ):
    def __init__(self):
        super().__init__()
        self.erdo = erdo()
        self.erdo.z_index = 2
        self.add_actor(self.erdo)
        self.felhoseg = felhoseg()
        self.felhoseg.z_index = 1
        self.add_actor(self.felhoseg)
        self.esocsepp = esocsepp()
        self.esocsepp.z_index = 3
        self.add_actor(self.esocsepp)

class HavasStage(game.scene2d.MyStage):
    def __init__(self):
        super().__init__()
        self.erdo = erdo()
        self.erdo.z_index = 2
        self.add_actor(self.erdo)
        self.felhoseg = felhoseg()
        self.felhoseg.z_index = 1
        self.add_actor(self.felhoseg)
        self.hopehely = hopehely()
        self.hopehely.z_index = 3
        self.add_actor(self.hopehely)

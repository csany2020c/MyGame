import Weathersim.horvathboldizsar.MenuScreen
from Weathersim.horvathboldizsar.GameActors import *
from Weathersim.horvathboldizsar.MiniMenuButtonStage import *


class NaposStage(game.scene2d.MyStage):

    def __init__(self):
        super().__init__()

        self.erdo = erdo()
        self.add_actor(self.erdo)

        self.naposeg = naposeg()
        self.add_actor(self.naposeg)

        self.nap = nap()
        self.add_actor(self.nap)


class HavasesosStage(game.scene2d.MyStage):
    def __init__(self):
        super().__init__()

        self.erdo = erdo()
        self.add_actor(self.erdo)

        self.felhoseg = felhoseg()
        self.add_actor(self.felhoseg)

        for x in range(0, random.randint(80, 160)):
            e = esocsepp()
            e.y = random.randint(-500, 300)
            e.x = random.randint(0, 1280 - e.width)
            self.add_actor(e)

        for j in range(0, random.randint(150, 250)):
            h = hopehely()
            h.y = random.randint(-500, 300)
            h.x = random.randint(0, 1280 - h.width)
            self.add_actor(h)


class EsosStage(game.scene2d.MyStage):
    def __init__(self):
        super().__init__()

        self.erdo = erdo()
        self.add_actor(self.erdo)

        self.felhoseg = felhoseg()
        self.add_actor(self.felhoseg)

        for x in range(0, random.randint(100, 180)):
            e = esocsepp()
            e.y = random.randint(-500, 300)
            e.x = random.randint(0, 1280 - e.width)
            self.add_actor(e)

class HavasStage(game.scene2d.MyStage):
    def __init__(self):
        super().__init__()

        self.erdo = erdo()
        self.add_actor(self.erdo)

        self.felhoseg = felhoseg()
        self.add_actor(self.felhoseg)

        for j in range(0, random.randint(150, 250)):
            h = hopehely()
            h.y = random.randint(-500, 300)
            h.x = random.randint(0, 1280 - h.width)
            self.add_actor(h)








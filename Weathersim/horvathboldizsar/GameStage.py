from Weathersim.horvathboldizsar.GameActors import *
from Weathersim.horvathboldizsar.MiniMenuButtonStage import *


class NaposStage(game.scene2d.MyStage):

    def __init__(self):
        super().__init__()

        self.erdo = Erdo()
        self.add_actor(self.erdo)

        self.naposeg = Naposeg()
        self.add_actor(self.naposeg)

        self.nap = Nap()
        self.add_actor(self.nap)


class HavasesosStage(game.scene2d.MyStage):
    def __init__(self):
        super().__init__()

        self.erdo = Erdo()
        self.add_actor(self.erdo)

        self.felhoseg = Felhoseg()
        self.add_actor(self.felhoseg)

        for x in range(0, random.randint(80, 160)):
            e = Esocsepp()
            e.y = random.randint(-500, 300)
            e.x = random.randint(30, 1280) - e.width
            self.add_actor(e)

        for j in range(0, random.randint(150, 250)):
            h = Hopehely()
            h.y = random.randint(-500, 300)
            h.x = random.randint(30, 1280) - h.width
            self.add_actor(h)


class EsosStage(game.scene2d.MyStage):
    def __init__(self):
        super().__init__()

        self.erdo = Erdo()
        self.add_actor(self.erdo)

        self.felhoseg = Felhoseg()
        self.add_actor(self.felhoseg)

        for x in range(0, random.randint(100, 180)):
            e = Esocsepp()
            e.y = random.randint(-500, 300)
            e.x = random.randint(30, 1280) - e.width
            self.add_actor(e)


class HavasStage(game.scene2d.MyStage):
    def __init__(self):
        super().__init__()

        self.erdo = Erdo()
        self.add_actor(self.erdo)

        self.felhoseg = Felhoseg()
        self.add_actor(self.felhoseg)

        for j in range(0, random.randint(150, 250)):
            h = Hopehely()
            h.y = random.randint(-500, 300)
            h.x = random.randint(30, 1280) - h.width
            self.add_actor(h)

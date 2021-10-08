from SzBKActor import *
import random
from game.scene2d import MyTickTimer

class NaposStage(game.scene2d.MyStage):

    def __init__(self):
        super().__init__()
        self.add_actor(HatterActor())
        self.add_actor(NapocskaActor())
        self.add_actor(LandscapeActor())
        self.add_actor(Icon1Actor())
        self.add_actor(Icon2Actor())
        self.add_actor(Icon3Actor())
        self.add_actor(Icon4Actor())


class HavasStage(game.scene2d.MyStage):

    def __init__(self):
        super().__init__()
        self.add_actor(Hatter2Actor())
        self.add_actor(LandscapeActor())
        self.add_actor(HavzikActor())
        self.add_actor(Havzik3Actor())
        self.add_actor(Havzik4Actor())
        self.add_actor(Havzik5Actor())
        self.add_actor(Havzik2Actor())
        self.ho = HavzikActor()
        self.t = MyTickTimer(interval=1.5, func=self.tikk)
        self.add_timer(self.t)
        self.add_actor(Icon1Actor())
        self.add_actor(Icon2Actor())
        self.add_actor(Icon3Actor())
        self.add_actor(Icon4Actor())

    def tikk(self, sender):
        self.add_actor(HavzikActor())
        self.add_actor(Havzik2Actor())
        self.add_actor(Havzik3Actor())
        self.add_actor(Havzik4Actor())
        self.add_actor(Havzik5Actor())


class EsosStage(game.scene2d.MyStage):

    def __init__(self):
        super().__init__()
        self.add_actor(Hatter2Actor())
        self.add_actor(LandscapeActor())
        self.add_actor(CseppActor())
        self.t = MyTickTimer(interval=0.001, func=self.tikk)
        self.add_timer(self.t)
        self.add_actor(Icon1Actor())
        self.add_actor(Icon2Actor())
        self.add_actor(Icon3Actor())
        self.add_actor(Icon4Actor())

    def tikk(self, sender):
        self.csepp = (CseppActor())
        self.add_actor(self.csepp)
        self.csepp.x = random.Random().randint(-500, 1500)

class KettosStage(game.scene2d.MyStage):
    def __init__(self):
        super().__init__()
        self.add_actor(Hatter2Actor())
        self.add_actor(LandscapeActor())
        self.t = MyTickTimer(interval=0.001, func=self.tikk)
        self.add_timer(self.t)
        self.add_actor(HavzikActor())
        self.add_actor(Havzik3Actor())
        self.add_actor(Havzik4Actor())
        self.add_actor(Havzik5Actor())
        self.add_actor(Havzik2Actor())
        self.ho = HavzikActor()
        self.t2 = MyTickTimer(interval=1.5, func=self.tikk2)
        self.add_timer(self.t2)
        self.add_actor(Icon1Actor())
        self.add_actor(Icon2Actor())
        self.add_actor(Icon3Actor())
        self.add_actor(Icon4Actor())

    def tikk(self, sender):
        self.csepp = (CseppActor())
        self.add_actor(self.csepp)
        self.csepp.x = random.Random().randint(-500, 1500)

    def tikk2(self, sender):
        self.add_actor(HavzikActor())
        self.add_actor(Havzik2Actor())
        self.add_actor(Havzik3Actor())
        self.add_actor(Havzik4Actor())
        self.add_actor(Havzik5Actor())
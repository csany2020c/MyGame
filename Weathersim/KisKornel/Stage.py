from Weathersim.KisKornel.Actor import *
import random

class SunnyStage(game.scene2d.MyStage):
    def __init__(self):
        super().__init__()
        self.add_actor(skyActor())
        self.add_actor(backgroundActor())
        self.SunnyActor = SunnyActor()
        self.add_actor(self.SunnyActor)
        self.SunnyActor.x = 700
        self.SunnyActor.y = 0
        self.add_actor(vissza())


class SnowStage(game.scene2d.MyStage):
    def __init__(self):
        super().__init__()
        self.add_actor(CloudActor())
        self.add_actor(backgroundActor())
        a = 10
        for i in range(1, a):
            a = a + 1
        for i in range(a):
            self.SnowActor = SnowActor()
            self.add_actor(self.SnowActor)
            self.SnowActor.x = random.Random().randint(0, game.scene2d.MyGame.get_screen_width() - self.SnowActor.w)
            self.SnowActor.y = random.Random().randint(0, game.scene2d.MyGame.get_screen_height() - self.SnowActor.w)
        self.add_actor(vissza())
class RainStage(game.scene2d.MyStage):
    def __init__(self):
        super().__init__()
        self.add_actor(CloudActor())
        self.add_actor(backgroundActor())
        a = 10
        for i in range(1, a):
            a = a + 1
        for i in range(a):
            self.RainActor = RainActor()
            self.add_actor(self.RainActor)
            self.RainActor.x = random.Random().randint(0, game.scene2d.MyGame.get_screen_width() - self.RainActor.w)
            self.RainActor.y = random.Random().randint(0, game.scene2d.MyGame.get_screen_height() - self.RainActor.w)
        self.add_actor(vissza())
class MenuStage(game.scene2d.MyStage):
    def __init__(self):
        super().__init__()
        self.add_actor(CloudActor())
        self.egyesgomb = egyesgomb()
        self.add_actor(self.egyesgomb)
        self.egyesgomb.x = 440
        self.egyesgomb.y = 100
        self.kettesgomb = kettesgomb()
        self.add_actor(self.kettesgomb)
        self.kettesgomb.x = 440
        self.kettesgomb.y = 200
        self.harmasgomb = harmasgomb()
        self.add_actor(self.harmasgomb)
        self.harmasgomb.x = 440
        self.harmasgomb.y = 300
        #self.negyesgomb = negyesgomb()
        #self.add_actor(self.negyesgomb)
        #self.negyesgomb.x = 440
        #self.negyesgomb.y = 400


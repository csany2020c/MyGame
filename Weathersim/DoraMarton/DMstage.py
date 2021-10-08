import game
import random
from Weathersim.DoraMarton.DMactors import *

class sunnystage(game.scene2d.MyStage):

    def __init__(self):
        super().__init__()
        self.add_actor(sunny())
        self.add_actor(sun())
        self.add_actor(landscape())

class snowystage(game.scene2d.MyStage):

    def __init__(self):
        super().__init__()
        a = 10
        for i in range(1, a):
            a = a + 1
        self.add_actor(cloudy())
        self.add_actor(landscape())
        for i in range(a):
            self.snow = snow()
            self.add_actor(self.snow)
            self.snow.x = random.Random().randint(0, game.scene2d.MyGame.get_screen_width() - self.snow.w)
            self.snow.y = random.Random().randint(0, game.scene2d.MyGame.get_screen_height() - self.snow.w)

class rainystage(game.scene2d.MyStage):
    def __init__(self):
        super().__init__()
        a = 10
        for i in range(1, a):
            a = a + 1
        self.add_actor(cloudy())
        self.add_actor(landscape())
        for i in range(a):
            self.rain = rain()
            self.add_actor(self.rain)
            self.rain.x = random.Random().randint(0, game.scene2d.MyGame.get_screen_width() - self.rain.w)
            self.rain.y = random.Random().randint(0, game.scene2d.MyGame.get_screen_height() - self.rain.w)

class snowyrainy(game.scene2d.MyStage):
    def __init__(self):
        super().__init__()
        a = 10
        for i in range(1, a):
            a = a + 1
        self.add_actor(cloudy())
        self.add_actor(landscape())
        for i in range(a):
            self.rain = snow()
            self.add_actor(self.rain)
            self.rain.x = random.Random().randint(0, game.scene2d.MyGame.get_screen_width() - self.rain.w)
            self.rain.y = random.Random().randint(0, game.scene2d.MyGame.get_screen_height() - self.rain.w)

        for i in range(a):
            self.rain = rain()
            self.add_actor(self.rain)
            self.rain.x = random.Random().randint(0, game.scene2d.MyGame.get_screen_width() - self.rain.w)
            self.rain.y = random.Random().randint(0, game.scene2d.MyGame.get_screen_height() - self.rain.w)
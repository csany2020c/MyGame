import game
from game.simpleworld.MyCircle import *


class HelloActor(game.MyActor):

    def __init__(self):
        super().__init__("HelloWorld/fox.png")

    def act(self):
        super().act()
        self.r += 360 * self.get_delta_time()


class HelloStage(game.MyStage):

    def __init__(self):
        super().__init__()

    def create(self):
        super(HelloStage, self).create()
        self.h1 = HelloActor()
        self.h2 = HelloActor()
        self.add_actor(self.h1)
        self.add_actor(self.h2)
        self.h2.x = 280
        self.h2.y = 180
        self.h2.w = 10
        self.h2.w = 200
        #self.h2.r = 45

    def act(self):
        super().act()
        #self.h2.r = self.elapsed_time * 100


class HelloScreen(game.MyScreen):

    def create(self):
        super(HelloScreen, self).create()
        self.set_BackGroundColor(200, 100, 22)
        self.addStage(HelloStage())


class HelloWorld(game.MyGame):

    def create(self):
        super(HelloWorld, self).create()
        self.set_screen(HelloScreen())


# HelloWorld()

sh = MyCircle()
print(sh)


import game
from game.simpleworld.MyCircle import *

class EnemyActor(game.scene2d.MyActor):

    def __init__(self) -> 'EnemyActor':
        super().__init__()
        return self


class HelloActor(game.scene2d.MyActor):

    def __init__(self):
        super().__init__("fox.png")

    def act(self):
        super().act()
        self.r += 360 * self.get_delta_time()


class HelloStage(game.scene2d.MyStage):

    def __init__(self):
        super().__init__()
        self.h1 = HelloActor()
        self.h2 = HelloActor()
        self.add_actor(self.h1)
        self.add_actor(self.h2)
        self.h2.x = 10
        self.h2.y = 10
        self.h2.w = 10
        self.h2.w = 200
        self.h2.r = 45

    def act(self):
        super().act()
        #self.h2.r = self.elapsed_time * 100


class HelloScreen(game.scene2d.MyScreen):

    def create(self):
        super(HelloScreen, self).create()
        self.set_background_color(200, 100, 22)
        self.add_stage(HelloStage())


class HelloWorld(game.scene2d.MyGame):

    def create(self):
        super(HelloWorld, self).create()
        self.set_screen(HelloScreen())


if __name__ == "__main__":
    HelloWorld()


#sh = MyCircle(x=20, y=16, radius=2)
#print(sh)


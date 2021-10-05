import game
import random


class Bg(game.scene2d.MyActor):
    def __init__(self):
        super().__init__("imgae/landscape.png")


class Cloudy(game.scene2d.MyActor):
    def __init__(self):
        super().__init__("imgae/cloudy.png")


class Rain(game.scene2d.MyActor):
    def __init__(self):
        super().__init__("imgae/rain.png")

    def act(self, delta_time: float):
        self.y += 75 * delta_time


class Line(game.scene2d.MyActor):
    def __init__(self):
        super().__init__("imgae/line.png")


class Stage(game.scene2d.MyStage):

    def __init__(self):
        super().__init__()
        self.C = Cloudy()
        self.add_actor(self.C)

        self.Bg = Bg()
        self.add_actor(self.Bg)
        for i in range(23):
            self.R = Rain()
            self.add_actor(self.R)
            self.R.set_size(width=50, height=50)
            self.R.x = random.Random().randint(0, game.scene2d.MyGame.get_screen_width() - self.R.w)
            self.R.y = random.Random().randint(0, game.scene2d.MyGame.get_screen_height() - self.R.h)

        self.L = Line()
        self.add_actor(self.L)
        #self.L.set_size(width=720, height=10)
        self.L.y = 613


class Screen(game.scene2d.MyScreen):

    def __init__(self):
        super().__init__()
        self.add_stage(Stage())


class Game(game.scene2d.MyGame):

    def __init__(self):
        super().__init__()
        self.screen = Screen()


Game().run()

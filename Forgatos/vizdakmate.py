import game

class Actor(game.scene2d.MyActor):
    def __init__(self):
        super().__init__("car.png")


    def act(self, delta_time: float):
        self.rotate_with(0.6)
        super().act(delta_time)
class MasikActor(game.scene2d.MyActor):

    def __init__(self):
        super().__init__("car.png")

    def act(self, delta_time: float):
        self.rotate_with(-0.6)
        super().act(delta_time)

class Stage(game.scene2d.MyStage):
    def create(self):
        super().create()
        super().create()
        self.a = Actor()
        self.a.set_y(200)
        self.a.set_x(550)
        self.a.set_size(400, 400)

        self.add_actor(self.a)
        self.b = MasikActor()
        self.b.set_y(200)
        self.b.set_x(250)
        self.add_actor(self.b)

    def act(self, delta_time: float):
        super().act(delta_time)
        if self.a.overlaps(self.b):
            self.screen.b = 240
        else:
            self.screen.b = 0

class Scr(game.scene2d.MyScreen):
    def create(self):
        super().create()
        self.r = 110
        self.g = 110
        self.b = 34
        self.add_stage(Stage())


class Jatek(game.scene2d.MyGame):
    def create(self):
        super().create()
        self.screen = Scr()



Jatek()
import game

class Actor(game.scene2d.MyActor):
    def __init__(self):
        super().__init__('car.png')
    def act(self, delta_time: float):
        super().act(delta_time)
        self.x += delta_time * 100

class Scr(game.scene2d.MyScreen):
    def create(self):
        super().create()
        self.r = 100
        self.g = 0
        self.b = 100
        self.add_stage(Stage())

class Stage(game.scene2d.MyStage):
    def create(self):
        super().create()

        a = Actor
        a.y = 80
        self.add_actor(a)

        b = Actor
        b.r = 45
        self.add_actor(b)

class Car(game.scene2d.MyGame):
    def create(self):
        super().create()
        self.screen = Scr()

Car()
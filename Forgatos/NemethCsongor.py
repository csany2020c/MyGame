import game


class Auto1(game.scene2d.MyActor):

    def __init__(self):
        super().__init__("car.png")

    def act(self, delta_time: float):
        self.x += 100*delta_time
        self.y += 75*delta_time


class Auto2(game.scene2d.MyActor):

    def __init__(self):
        super().__init__("car.png")

    def act(self, delta_time: float):
        self.x += 10*delta_time


class Stage(game.scene2d.MyStage):

    def __init__(self):
        super().__init__()
        self.A = Auto1()
        self.A2 = Auto2()
        self.add_actor(self.A)
        self.add_actor(self.A2)
        self.A.y = 100
        self.A.x = 50
        self.A2.y = 400
        self.A2.x = 600

    def act(self, delta_time: float):
        super().act(delta_time)
        if self.A.overlaps(self.A2):
            self.screen.b = 80
        else:
            self.screen.b = 0


class Screen(game.scene2d.MyScreen):

    def create(self):
        super().create()
        self.r = 200
        self.g = 10
        self.b = 25
        self.add_stage(Stage())


class Game(game.scene2d.MyGame):

    def create(self):
        super().create()
        self.screen = Screen()


Game().run()

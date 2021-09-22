import game


class ActorA(game.scene2d.MyActor):

    def __init__(self):
        super().__init__("car.png")
        self.speed = 0

    def act(self, delta_time: float):
        super().act(delta_time)
        self.x-=delta_time* 20

class ActorB(game.scene2d.MyActor):

    def __init__(self):
        super().__init__("car.png")

    def act(self, delta_time: float):
        super().act(delta_time)
        self.x+=-delta_time*30


class Stage(game.scene2d.MyStage):

    def __init__(self):
        super().__init__()
        self.a = ActorA()
        self.b = ActorB()
        self.a.set_x(90).set_y(140)
        self.b.set_x(390).set_y(190)
        self.add_actor(self.a)
        self.add_actor(self.b)

    def act(self, delta_time: float):
        super().act(delta_time)
        if self.a.overlaps(self.b):
            self.screen.b = 80
        else:
            self.screen.b = 0

class Screen(game.scene2d.MyScreen):

    def __init__(self):
        super().__init__()
        self.add_stage(Stage())


class Start(game.scene2d.MyGame):
    def __init__(self, width: int = 1280, height: int = 720, autorun: bool = False):
        super().__init__(width, height, autorun)
        self.screen = Screen()

Start().run()

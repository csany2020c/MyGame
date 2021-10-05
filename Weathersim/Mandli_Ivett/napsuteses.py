import game


class ActorA(game.scene2d.MyActor):
    def __init__(self):
        super().__init__("sunny.png")


class ActorB(game.scene2d.MyActor):
    def __init__(self):
        super().__init__("sun.png")

    def act(self, delta_time: float):
        super().act(delta_time)
        self.r += -delta_time*10


class ActorC(game.scene2d.MyActor):
    def __init__(self):
        super().__init__("landscape.png")


class Stage(game.scene2d.MyStage):
    def __init__(self):
        super().__init__()
        self.a = ActorA()
        self.b = ActorB()
        self.c = ActorC()
        self.b.set_x(400).set_y(50)
        self.add_actor(self.a)
        self.add_actor(self.b)
        self.add_actor(self.c)


class Screen(game.scene2d.MyScreen):
    def __init__(self):
        super().__init__()
        self.add_stage(Stage())


class Start(game.scene2d.MyGame):
    def __init__(self, width: int = 1280, height: int = 720, autorun: bool = False):
        super().__init__(width, height, autorun)
        self.screen = Screen()


Start().run()

import game

class actor1(game.scene2d.MyActor):

    def __init__(self):
        super().__init__("car.png")
        self.speed = 0
        self.hitbox_scale_h = 0.5

    def act(self, delta_time: float):
        super().act(delta_time)
        self.x += delta_time * self.speed

class actor2(game.scene2d.MyActor):

    def __init__(self):
        super().__init__("car.png")
        self.speed = 0
        self.hitbox_scale_h = 0.5

    def act(self, delta_time: float):
        super().act(delta_time)
        self.x += delta_time * self.speed

class Stage(game.scene2d.MyStage):

    def __init__(self):
        super().__init__()
        self.a = actor1()
        self.b = actor2()
        self.a.speed = 180
        self.b.speed = 80
        self.a.set_x(30).set_y(140)
        self.b.set_x(90).set_y(140)
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

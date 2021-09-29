import game


class WarioActor(game.scene2d.MyActor):

    def __init__(self):
        super().__init__("fox.png")

    def act(self, delta_time: float):
        super().act(delta_time)
        self.x += delta_time * 50

class Wario2Actor(game.scene2d.MyActor):

    def __init__(self):
        super().__init__("fox.png")

    def act(self, delta_time: float):
        super().act(delta_time)
        self.y += delta_time * -10

class Wario3Actor(game.scene2d.MyActor):

    def __init__(self):
        super().__init__("fox.png")

    def act(self, delta_time: float):
        super().act(delta_time)
        self.y += delta_time * 80
        self.x += delta_time * 80

class Wario4Actor(game.scene2d.MyActor):

    def __init__(self):
        super().__init__("fox.png")

    def act(self, delta_time: float):
        super().act(delta_time)
        self.y += delta_time * 100
        self.x += delta_time * 50

class WarioStage(game.scene2d.MyStage):

    def __init__(self):
        super().__init__()
        self.add_actor(WarioActor())
        self.add_actor(Wario2Actor())
        self.add_actor(Wario3Actor())
        self.add_actor(Wario4Actor())


class Wario2Scr(game.scene2d.MyScreen):

    def __init__(self):
        super().__init__()
        self.r = 30
        self.g = 216
        self.b = 196
        self.add_stage(WarioStage())

    def act(self, delta_time: float):
        super().act(delta_time)
        if self.elapsed_time > 10:
            self.game.screen = WarioScr()

class WarioScr(game.scene2d.MyScreen):

    def __init__(self):
        super().__init__()
        self.r = 156
        self.g = 200
        self.b = 120
        self.add_stage(WarioStage())

    def act(self, delta_time: float):
        super().act(delta_time)
        if self.elapsed_time > 5:
            self.game.screen = Wario2Scr()

class Wario(game.scene2d.MyGame):

    def __init__(self):
        super().__init__()
        self.screen = WarioScr()

    pass


Wario()

import game


class WarioActor(game.scene2d.MyActor):

    def __init__(self):
        super().__init__("fox.png")

    def act(self, delta_time: float):
        super().act(delta_time)
        self.x += delta_time * 150

class Wario2Actor(game.scene2d.MyActor):

    def __init__(self):
        super().__init__("fox.png")

    def act(self, delta_time: float):
        super().act(delta_time)
        self.y += delta_time * -80

class Wario3Actor(game.scene2d.MyActor):

    def __init__(self):
        super().__init__("fox.png")

    def act(self, delta_time: float):
        super().act(delta_time)
        self.y += delta_time * 70
        self.x += delta_time * 70

class WarioStage(game.scene2d.MyStage):

    def create(self):
        super().create()
        self.add_actor(WarioActor())
        self.add_actor(Wario2Actor())
        self.add_actor(Wario3Actor())


class Wario2Scr(game.scene2d.MyScreen):

    def create(self):
        super().create()
        self.r = 30
        self.g = 216
        self.b = 196
        self.add_stage(WarioStage())

    def act(self, delta_time: float):
        super().act(delta_time)
        if self.elapsed_time > 8:
            self.game.screen = WarioScr()

class WarioScr(game.scene2d.MyScreen):

    def create(self):
        super().create()
        self.r = 189
        self.g = 225
        self.b = 99
        self.add_stage(WarioStage())

    def act(self, delta_time: float):
        super().act(delta_time)
        if self.elapsed_time > 5:
            self.game.screen = Wario2Scr()

class Wario(game.scene2d.MyGame):

    def create(self):
        super().create()
        self.screen = WarioScr()

    pass


Wario()

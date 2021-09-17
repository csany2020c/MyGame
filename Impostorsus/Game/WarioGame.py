import game


class WarioActor(game.scene2d.MyActor):

    def __init__(self):
        super().__init__("Kepek/Enemysus.png")

    def act(self, delta_time: float):
        super().act(delta_time)
        self.x += delta_time * 100

class Wario2Actor(game.scene2d.MyActor):

    def __init__(self):
        super().__init__("Kepek/Wario.png")

    def act(self, delta_time: float):
        super().act(delta_time)
        self.y += delta_time * 100

class Wario3Actor(game.scene2d.MyActor):

    def __init__(self):
        super().__init__("Kepek/Wario.png")

    def act(self, delta_time: float):
        super().act(delta_time)
        self.y += delta_time * 100
        self.x += delta_time * 100

class Wario4Actor(game.scene2d.MyActor):

    def __init__(self):
        super().__init__("Kepek/Wario.png")

    def act(self, delta_time: float):
        super().act(delta_time)
        self.y += delta_time * -100
        self.x += delta_time * -100

class WarioStage(game.scene2d.MyStage):

    def create(self):
        super().create()
        self.add_actor(WarioActor())
        self.add_actor(Wario2Actor())
        self.add_actor(Wario3Actor())
        self.add_actor(Wario4Actor())


class Wario2Scr(game.scene2d.MyScreen):

    def create(self):
        super().create()
        self.r = 71
        self.g = 245
        self.b = 233
        self.add_stage(WarioStage())

    def act(self, delta_time: float):
        super().act(delta_time)
        if self.elapsed_time > 5:
            self.game.screen = WarioScr()

class WarioScr(game.scene2d.MyScreen):

    def create(self):
        super().create()
        self.r = 245
        self.g = 71
        self.b = 146
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


Wario().run()
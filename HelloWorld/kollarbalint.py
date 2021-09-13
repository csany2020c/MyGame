import game

class MarioActor(game.scene2d.MyActor):

    def __init__(self):
        super().__init__("fox.png")

    def act(self, delta_time: float):
        super().act(delta_time)
        self.x += delta_time * 200

class MarioActor2(game.scene2d.MyActor):

    def __init__(self):
        super().__init__("fox.png")

    def act(self, delta_time: float):
        super().act(delta_time)
        self.y += delta_time * 100

class MarioActor3(game.scene2d.MyActor):

    def __init__(self):
        super().__init__("fox.png")

    def act(self, delta_time: float):
        super().act(delta_time)
        self.x += delta_time * 125
        self.y += delta_time * 125


class MarioActor4(game.scene2d.MyActor):

    def __init__(self):
        super().__init__("fox.png")

    def act(self, delta_time: float):
        super().act(delta_time)
        self.x += delta_time * 60
        self.y += delta_time * 60

class MarioStage(game.scene2d.MyStage):

    def create(self):
        super().create()
        self.add_actor(MarioActor())
        self.add_actor(MarioActor2())
        self.add_actor(MarioActor3())
        self.add_actor(MarioActor4())


class Marioskep(game.scene2d.MyScreen):

    def create(self):
        super().create()
        self.r = 255
        self.g = 111
        self.b = 0
        self.add_stage(MarioStage())

    def act(self, delta_time: float):
        super().act(delta_time)
        if self.elapsed_time > 3:
            self.game.screen = Masikkep()

class Masikkep(game.scene2d.MyScreen):

    def create(self):
        super().create()
        self.r = 50
        self.g = 168
        self.b = 166
        self.add_stage(MarioStage())

    def act(self, delta_time: float):
        super().act(delta_time)
        if self.elapsed_time > 3:
            self.game.screen = Marioskep()

class Mario(game.scene2d.MyGame):

    def create(self):
        super().create()
        self.screen = Marioskep()

Mario()
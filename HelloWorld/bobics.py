import game


class MarioActor(game.scene2d.MyActor):

    def __init__(self):
        super().__init__("fox.png")

    def act(self, delta_time: float):
        super().act(delta_time)
        self.x += delta_time * 100

class MarioActor2(game.scene2d.MyActor):
    def __init__(self):
        super().__init__("fox.png")

    def act(self, delta_time: float):
        super().act(delta_time)
        self.x += delta_time -10

class Mariostage(game.scene2d.MyStage):

    def __init__(self):
        super().__init__()

        self.add_actor(MarioActor())
        self.add_actor(aMarioActor2())


class marioscr(game.scene2d.MyScreen):

    def __init__(self):
        super().__init__()
        self.r = 150
        self.g = 40
        self.b = 10
        self.add_stage(Mariostage())

    def act(self, delta_time: float):
        super().act(delta_time)
        if self.elapsed_time > 1:
            self.game.screen = marioscr2()

class marioscr2(game.scene2d.MyScreen):

    def __init__(self):
        super().__init__()
        self.r = 100
        self.g = 0
        self.b = 150
        self.add_stage(Mariostage())

    def act(self, delta_time: float):
        super().act(delta_time)
        if self.elapsed_time > 1:
            self.game.screen = marioscr()



class Mario(game.scene2d.MyGame):

    def __init__(self):
        super().__init__()
        self.screen = marioscr2()

    pass


Mario()
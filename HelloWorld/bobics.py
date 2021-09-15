import game

class Marioactor(game.scene2d.MyActor):

    def __init__(self):
        super().__init__("fox.png")

    def act(self, delta_time: float):
        super().act(delta_time)
        self.x += delta_time * 100

class Mariostage(game.scene2d.MyStage):

    def create(self):
        super().create()
        self.add_actor(Marioactor)


class marioscr(game.scene2d.MyScreen):

    def create(self):
        super().create()
        self.r = 150
        self.g = 40
        self.b = 10

    def create(self):
        super().create()
        self.add_actor(Marioactor)

    def act(self, delta_time: float):
        super().act(delta_time)
        if self.elapsed_time > 1:
            self.game.screen = marioscr2()

class marioscr2(game.scene2d.MyScreen):

    def create(self):
        super().create()
        self.r = 40
        self.g = 70
        self.b = 100

    def create(self):
        super().create()
        self.add_actor(Marioactor)

    def act(self, delta_time: float):
        super().act(delta_time)
        if self.elapsed_time > 1:
            self.game.screen = marioscr()



class Mario(game.scene2d.MyGame):

    def create(self):
        super().create()
        self.screen = marioscr2()


Mario()
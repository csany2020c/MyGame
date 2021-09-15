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


class Marioscr(game.scene2d.MyScreen):


        def create(self):
            super().create()
            self.r = 0
            self.g = 1
            self.b = 0


        def act(self, delta_time: float):
            super().act(delta_time)
            if self.elapsed_time > 1:
                self.game.screen = Masikscr()


class Masikscr(game.scene2d.MyScreen):

    def create(self):
        super().create()
        self.r = 50
        self.g = 41
        self.b = 40

    def act(self, delta_time: float):
        super().act(delta_time)
        if self.elapsed_time > 1:
            self.game.screen = Marioscr()


class Mario(game.scene2d.MyGame):

    def create(self):
        super().create()
        self.screen = Masikscr()



Mario()
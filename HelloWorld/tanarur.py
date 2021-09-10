import game


class MarioActor(game.scene2d.MyActor):

    def __init__(self):
        super().__init__("fox.png")

    def act(self, delta_time: float):
        super().act(delta_time)
        self.x += delta_time * 100



class MarioStage(game.scene2d.MyStage):

    def create(self):
        super().create()
        self.add_actor(MarioActor())


class MasikScr(game.scene2d.MyScreen):

    def create(self):
        super().create()
        self.r = 10
        self.g = 250
        self.b = 88
        self.addStage(MarioStage())

    def act(self, delta_time: float):
        super().act(delta_time)
        if self.elapsed_time > 3:
            self.game.screen = MarioScr()


class MarioScr(game.scene2d.MyScreen):

    def create(self):
        super().create()
        self.r = 100
        self.g = 50
        self.b = 8
        self.addStage(MarioStage())

    def act(self, delta_time: float):
        super().act(delta_time)
        if self.elapsed_time > 3:
            self.game.screen = MasikScr()


class Mario(game.scene2d.MyGame):

    def create(self):
        super().create()
        self.screen = MarioScr()


Mario()

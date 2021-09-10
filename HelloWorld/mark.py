import game

class MarioActor(game.scene2d.MyActor):
    def __init__(self):
        super().__init__("fox.png")

    def act(self, delta_time: float):
        super().act(delta_time)
        self.x += delta_time*100


class MarioStage(game.scene2d.MyStage):

    def create(self):
        super().create()
        self.add_actor(MarioActor())


#class HarmadikScr(game.scene2d.MyScreen):
#    def create(self):
#        super().create()
#        self.r = 0
#        self.g = 0
#        self.b = 0
#        self.addStage(MarioStage())
#
#    def act(self, delta_time: float):
#        super().act(delta_time)
#        if self.elapsed_time > 3:
#            self.game.screen = MarioScr()
#
#
#
#
#class MasikScr(game.scene2d.MyScreen):
#
#    def create(self):
#        super().create()
#        self.r = 252
#        self.g = 3
#        self.b = 3
#        self.addStage(MarioStage())
#
#    def act(self, delta_time: float):
#        super().act(delta_time)
#        if self.elapsed_time > 3:
#            self.game.screen = HarmadikScr()

class MarioScr(game.scene2d.MyScreen):

    def create(self):
        super().create()
        self.r = 3
        self.g = 252
        self.b = 232
        self.addStage(MarioStage())

    def act(self, delta_time: float):
        super().act(delta_time)
        if self.elapsed_time > 3:
            self.game.screen = MarioScr()

class Mario(game.scene2d.MyGame):



    def create(self):
        super().create()
        self.screen = MarioScr()

Mario()
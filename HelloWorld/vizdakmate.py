import game

class MarioActor(game.scene2d.MyActor):

    def __init__(self):
        super().__init__("fox.png")

    def act(self, delta_time: float):
        super().act(delta_time)
        self.x += delta_time * 100




#class MarioActor2(game.scene2d.MyActor):

    #def __init__(self):
        #super().__init__("fox.png")

    #def act(self, delta_time: float):
        #super().act(delta_time)
        #self.y += delta_time * 300


class MarioActor3(game.scene2d.MyActor):

    def __init__(self):
        super().__init__("fox.png")

    def act(self, delta_time: float):
        super().act(delta_time)
        self.x += delta_time * 125
        self.set_size(600, 600)



class MarioActor4(game.scene2d.MyActor):

    def __init__(self):
        super().__init__("fox.png")

    def act(self, delta_time: float):
        super().act(delta_time)
        self.x += delta_time * 100
        self.y += delta_time * 59
        self.r += delta_time * 180



class MarioStage(game.scene2d.MyStage):

    def create(self):
        super().create()
        self.add_actor(MarioActor())
        #self.add_actor(MarioActor2())
        self.add_actor(MarioActor3())
        self.add_actor(MarioActor4())


class MarioScr(game.scene2d.MyScreen):

    def create(self):
        super().create()
        self.r = 192
        self.g = 45
        self.b = 56
        self.add_stage(MarioStage())

    def act(self, delta_time: float):
        super().act(delta_time)
        if self.elapsed_time > 8:
            self.game.screen = MasikScr()

class MasikScr(game.scene2d.MyScreen):

    def create(self):
        super().create()
        self.r = 110
        self.g = 110
        self.b = 34
        self.add_stage(MarioStage())

    def act(self, delta_time: float):
        super().act(delta_time)
        if self.elapsed_time > 8:
            self.game.screen = MarioScr()


class Mario(game.scene2d.MyGame):

    def create(self):
        super().create()
        self.screen = MarioScr()

Mario()
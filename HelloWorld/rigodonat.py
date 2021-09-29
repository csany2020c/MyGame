import game

class MarioActor(game.scene2d.MyActor):
    def __init__(self):
        super().__init__('fox.png')
    def act(self, delta_time: float):
        super().act(delta_time)
        self.x += delta_time * 100


class MarioStage(game.scene2d.MyStage):

    def __init__(self):
        super().__init__()

        a = MarioActor
        a.y = 80
        self.add_actor(a)

        b = MarioActor
        b.r = 45
        self.add_actor(b)



class MasikScr(game.scene2d.MyScreen):


    def __init__(self):
        super().__init__()
        self.r = 100
        self.g = 0
        self.b = 150

    def act(self, delta_time: float):
        super().act(delta_time)
        if self.elapsed_time > 1:
            self.game.screen = MarioScr()

class MarioScr(game.scene2d.MyScreen):


    def __init__(self):
        super().__init__()
        self.r = 100
        self.g = 0
        self.b = 100
        self.add_stage(MarioStage())

    def act(self, delta_time: float):
        super().act(delta_time)
        if self.elapsed_time > 1:
            self.game.screen = MasikScr()



class Mario(game.scene2d.MyGame):



    def __init__(self):
        super().__init__()
        self.screen = MasikScr()




Mario()
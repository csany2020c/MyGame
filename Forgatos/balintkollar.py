import game


class ElsoActor(game.scene2d.MyActor):

    def __init__(self):
        super().__init__("car.png")

    def act(self, delta_time: float):
        self.rotate_with(0.6)
        super().act(delta_time)



class MasikActor(game.scene2d.MyActor):

    def __init__(self):
        super().__init__("car.png")

    def act(self, delta_time: float):
        self.rotate_with(-0.6)
        super().act(delta_time)



class JatekStage(game.scene2d.MyStage):

    def create(self):
        super().create()
        self.a = ElsoActor()
        self.a.set_y(200)
        self.a.set_x(550)
        self.a.set_size(400, 400)

        self.add_actor(self.a)
        self.b = MasikActor()
        self.b.set_y(200)
        self.b.set_x(250)
        self.add_actor(self.b)

    def act(self, delta_time: float):
        super().act(delta_time)
        if self.a.overlaps(self.b):
            self.screen.b = 240
        else:
            self.screen.b = 0



class JatekScr(game.scene2d.MyScreen):

    def create(self):
        super().create()
        self.r = 71
        self.g = 245
        self.b = 233
        self.add_stage(JatekStage())

    #def act(self, delta_time: float):
        #super().act(delta_time)
        #if self.elapsed_time > 5:
            #self.game.screen = JatekScr()


class Jatek(game.scene2d.MyGame):

    def create(self):
        super().create()
        self.screen = JatekScr()

    pass

Jatek().run()



import game

class porgonc(game.scene2d.MyActor):
    def __init__(self):
        super().__init__("car.png")

    def act(self, delta_time: float):
        super().act(delta_time)
        self.r += delta_time * 360

class porgonc2(game.scene2d.MyActor):
    def __init__(self):
        super().__init__("car.png")

    def act(self, delta_time: float):
        super().act(delta_time)
        self.r += delta_time * -360

class porgoncstage(game.scene2d.MyStage):

    def __init__(self):
        super().__init__()


        a = porgonc()
        a.y = 300
        a.x = 100
        self.add_actor(a)

        b = porgonc2()
        b.y = 200
        b.x = 300
        self.add_actor(b)


class porgoncScreen(game.scene2d.MyScreen):

    def __init__(self):
        super().__init__()
        self.r = 0
        self.g = 1
        self.b = 0
        self.add_stage(porgoncstage())
    def act(self, delta_time: float):
            super().act(delta_time)
            if self.elapsed_time > 1:
                self.game.screen =porgoncScreen()

    class porgoncScreen(game.scene2d.MyScreen):

        def __init__(self):
            super().__init__()
            self.r = 50
            self.g = 41
            self.b = 40
            self.add_stage(porgoncstage())

        def act(self, delta_time: float()):
            super().act(delta_time)
            if self.elapsed_time > 1:
                self.game.screen = porgoncScreen()

class porgoncke(game.scene2d.MyGame):

    def create(self):
        self.screen = porgoncScreen()



porgoncke().run()
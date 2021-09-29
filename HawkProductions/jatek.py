import game


class Deagle(game.scene2d.MyActor):

    def __init__(self):
        super().__init__("image/bid2.png")

class Pile1(game.scene2d.MyActor):
    def __init__(self):
        super().__init__("image/oszlop.png")

class Pile2(game.scene2d.MyActor):
    def __init__(self):
        super().__init__("image/oszlop.png")

class Stage(game.scene2d.MyStage):

    def __init__(self):
        super().__init__()
        self.D = Deagle()
        self.add_actor(self.D)
        self.D.y = 100
        self.D.x = 50
        self.D.width = 100

        self.P1 = Pile1()
        self.add_actor(self.P1)

        self.P2 = Pile2()
        self.add_actor(self.P2)
        self.P2.set_x(250)
        self.P2.set_y(150)


class Screen(game.scene2d.MyScreen):

    def __init__(self):
        super().__init__()
        self.r = 200
        self.g = 10
        self.b = 25
        self.add_stage(Stage())


class Game(game.scene2d.MyGame):

    def __init__(self):
        super().__init__()
        self.screen = Screen()


Game().run()

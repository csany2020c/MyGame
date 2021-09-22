import game


class Deagle(game.scene2d.MyActor):

    def __init__(self):
        super().__init__("image/bid.jpg")


class Stage(game.scene2d.MyStage):

    def __init__(self):
        super().__init__()
        self.D = Deagle()
        self.add_actor(self.D)
        self.D.y = 100
        self.D.x = 50
        self.D.width = 100


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

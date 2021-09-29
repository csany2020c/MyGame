import game


class Enemy1Actor(game.scene2d.MyActor):

    def __init__(self):
        super().__init__("image/startb.png")

    def act(self, delta_time: float):
        super().act(delta_time)


class Enemy2Actor(game.scene2d.MyActor):

    def __init__(self):
        super().__init__("image/quitb.png")

    def act(self, delta_time: float):
        super().act(delta_time)


class GameStage(game.scene2d.MyStage):

    def __init__(self):
        super().__init__()
        self.h1 = Enemy1Actor()
        self.h2 = Enemy2Actor()
        self.add_actor(self.h1)
        self.add_actor(self.h2)
        self.h1.x = 525
        self.h1.y = 250
        self.h1.w = 200
        self.h2.x = 525
        self.h2.y = 400
        self.h2.w = 200


class GameScreen(game.scene2d.MyScreen):

    def __init__(self):
        super().__init__()
        self.set_background_color(0, 128, 0)
        self.add_stage(GameStage())


class Space(game.scene2d.MyGame):

    def __init__(self):
        super().__init__()
        self.set_screen(GameScreen())


Space().run()
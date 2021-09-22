import game


class Enemy1Actor(game.scene2d.MyActor):

    def __init__(self):
        super().__init__("image/my-caracter.png")

    def act(self, delta_time: float):
        super().act(delta_time)


class Enemy2Actor(game.scene2d.MyActor):

    def __init__(self):
        super().__init__("image/my-caracter.png")

    def act(self, delta_time: float):
        super().act(delta_time)

class GameStage(game.scene2d.MyStage):

    def __init__(self):
        super().__init__()

    def create(self):
        super(GameStage, self).create()
        self.h1 = Enemy1Actor()
        self.h2 = Enemy2Actor()
        self.add_actor(self.h1)
        self.add_actor(self.h2)
        self.h2.x = 20
        self.h2.y = 20
        self.h2.w = 200
        self.h2.hitbox_scale_w = 0.75


class GameScreen(game.scene2d.MyScreen):

    def create(self):
        super().create()
        self.set_background_color(0, 128, 0)
        self.add_stage(GameStage())


class Space(game.scene2d.MyGame):

    def create(self):
        super().create()
        self.set_screen(GameScreen())


Space()

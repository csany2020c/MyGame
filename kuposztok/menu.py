import game


class MenuActor(game.scene2d.MyActor):

    def __init__(self):
        super().__init__("randomkep")

    def act(self, delta_time: float):
        super().act(delta_time)
        self.x += delta_time * 100


class MenuStage(game.scene2d.MyStage):

    def create(self):
        super().create()

        a = MenuActor()
        a.y = 80
        self.add_actor(a)


class MenuScreen(game.scene2d.MyScreen):

    def create(self):
        super().create()
        self.r = 100
        self.g = 50
        self.b = 8
        self.add_stage(MenuStage())


class Menu(game.scene2d.MyGame):

    def create(self):
        super().create()
        self.screen = MenuScreen()


Menu()

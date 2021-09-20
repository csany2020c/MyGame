import game


class MenuActor(game.scene2d.MyActor):

    def __init__(self):
        super().__init__('image/my-caracter.png')

    def act(self, delta_time: float):
        super().act(delta_time)
        self.x += delta_time


class MenuStage(game.scene2d.MyStage):

    def create(self):
        super().create()

        a = MenuActor()
        a.y = 20
        self.add_actor(a)


class MenuScreen(game.scene2d.MyScreen):

    def create(self):
        super().create()
        self.r = 1
        self.g = 1
        self.b = 60
        self.add_stage(MenuStage())


class Menu(game.scene2d.MyGame):

    def create(self):
        super().create()
        self.screen = MenuScreen()


Menu().run()

import game


class BgActor(game.scene2d.MyActor):

    def __init__(self):
        super().__init__('image/menu.png')


class MenuActor(game.scene2d.MyActor):

    def __init__(self):
        super().__init__('image/my-caracter.png')

    def act(self, delta_time: float):
        super().act(delta_time)
        self.x += delta_time * 100


class MenuStage(game.scene2d.MyStage):

    def create(self):
        super().create()

        bg = BgActor()
        a = MenuActor()
        a.y = 0
        self.add_actor(bg)
        self.add_actor(a)
        print(self.s)

class MenuScreen(game.scene2d.MyScreen):

    def __init__(self):
        super().__init__()
        self.set_background_color(r=0,g=0, b=255)
        self.add_stage(MenuStage())



class Menu(game.scene2d.MyGame):

    def create(self):
        super().create()
        self.screen = MenuScreen()


Menu().run()

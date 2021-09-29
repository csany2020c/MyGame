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


    def __init__(self):
        super().__init__()
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


    def __init__(self, width: int = 1280, height: int = 720, autorun: bool = False, autosize: bool = False):
        super().__init__(width, height, autorun, autosize)
        self.screen = MenuScreen()


Menu().run()

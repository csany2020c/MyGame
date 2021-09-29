import game


class BgActor(game.scene2d.MyActor):

    def __init__(self):
        super().__init__('image/menu.png')


class MenuActor(game.scene2d.MyActor):

    def __init__(self):
        super().__init__('image/icon.png')


class MenuStage(game.scene2d.MyStage):


    def __init__(self):
        super().__init__()
        bg = BgActor()
        a = MenuActor()
        a.y = 0
        self.add_actor(bg)
        self.add_actor(a)
        print(a)

class MenuScreen(game.scene2d.MyScreen):

    def __init__(self):
        super().__init__()
        self.set_background_color(r=0,g=0, b=255)
        self.add_stage(MenuStage())



class Menu(game.scene2d.MyGame):

    def __init__(self, width: int = 1920, height: int = 1080, autorun: bool = False, autosize: bool = True):
        super().__init__(width, height, autorun, autosize)
        self.screen = MenuScreen()


Menu().run()

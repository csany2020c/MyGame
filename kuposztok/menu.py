import game


class BgActor(game.scene2d.MyActor):

    def __init__(self):
        super().__init__('image/menu.png')


class Button1(game.scene2d.MyActor):

    def __init__(self):
        super().__init__('image/play_button.png')

class Button2(game.scene2d.MyActor):

    def __init__(self):
        super().__init__('image/exit_button.png')

class Button3(game.scene2d.MyActor):

    def __init__(self):
        super().__init__('image/credit_button.png')

class MenuStage(game.scene2d.MyStage):


    def __init__(self):
        super().__init__()
        bg = BgActor()
        a = Button1()
        b = Button2()
        c = Button3()
        b.x = 600
        b.y = 400
        c.y = 500
        c.x = 600
        a.y = 300
        a.x = 600
        self.add_actor(bg)
        self.add_actor(c)
        self.add_actor(a)
        self.add_actor(b)
        print(a)

class MenuScreen(game.scene2d.MyScreen):

    def __init__(self):
        super().__init__()
        self.set_background_color(r=0,g=0, b=255)
        self.add_stage(MenuStage())



class Menu(game.scene2d.MyGame):


    def __init__(self, width: int = 1366, height: int = 768, autorun: bool = False, autosize: bool = False):
        super().__init__(width, height, autorun, autosize)
        self.screen = MenuScreen()


Menu().run()

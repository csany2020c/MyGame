import game
import pygame
from kuposztok.Menu.MenuScreen import *


class BgActor(game.scene2d.MyActor):

    def __init__(self):

        super().__init__('../image/menu.png')


class Button1(game.scene2d.MyActor):

    def __init__(self):
        super().__init__('../image/play_button.png')


class Button2(game.scene2d.MyActor):

    def __init__(self):
        super().__init__('../image/exit_button.png')


class Button3(game.scene2d.MyActor):

    def __init__(self):
        super().__init__('../image/credit_button.png')


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




class Menu(game.scene2d.MyGame):

    def __init__(self, width: int = 1366, height: int = 768, autorun: bool = False, autosize: bool = False):
        super().__init__(width, height, autorun, autosize)
        self.screen = MenuScreen()


Menu().run()

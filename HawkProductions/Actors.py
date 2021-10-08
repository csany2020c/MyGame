import game
from HawkProductions.GameScreen import *


class Enemy1Actor(game.scene2d.MyActor):

    def __init__(self):
        super().__init__("image/startb.png")
        #self.set_on_mouse_down_listener(self.klikk)

    def act(self, delta_time: float):
        super().act(delta_time)


    '''def klikk(self, event, sender):
        print(event)
        print(sender)
        self.set_screen(GameScreen())'''


class Enemy2Actor(game.scene2d.MyActor):

    def __init__(self):
        super().__init__("image/quitb.png")

    def act(self, delta_time: float):
        super().act(delta_time)


class Deagle(game.scene2d.MyActor):

    def __init__(self):
        super().__init__("image/bid2.png")

    def act(self, delta_time: float):
        self.y += 75*delta_time


class Pile1(game.scene2d.MyActor):
    def __init__(self):
        super().__init__("image/oszlop-f.png")

    def act(self, delta_time: float):
        self.x -= 75 * delta_time
        if self.x < 0:
            self.x = 1280


class Pile2(game.scene2d.MyActor):
    def __init__(self):
        super().__init__("image/oszlop-a.png")

    def act(self, delta_time: float):
        self.x -= 75*delta_time
        if self.x < 0:
            self.x = 1280


class Bg(game.scene2d.MyActor):
    def __init__(self):
        super().__init__("image/hat_kep_j.png")

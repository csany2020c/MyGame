import game

class Sellect(game.scene2d.MyActor):
    def __init__(self):
        super().__init__("image/sellect.jpg")

class Title(game.scene2d.MyActor):
    def __init__(self):
        super().__init__("image/title.png")

class Startb(game.scene2d.MyActor):

    def __init__(self):
        super().__init__("image/startb.png")

    def act(self, delta_time: float):
        super().act(delta_time)


class Exit(game.scene2d.MyActor):

    def __init__(self):
        super().__init__("image/quitb.png")

    def act(self, delta_time: float):
        super().act(delta_time)


class Deagle(game.scene2d.MyActor):

    def __init__(self):
        super().__init__("image/bid2.png")

    def act(self, delta_time: float):
        self.y += 75*delta_time
        self.r += 15*delta_time

class Deagle_s(game.scene2d.MyActor):

    def __init__(self):
        super().__init__("image/bid2.png")

class Deagle2(game.scene2d.MyActor):
    def __init__(self):
        super().__init__("image/Select.png")



class Pile(game.scene2d.MyActor):
    def __init__(self):
        super().__init__("image/oszlop.png")

    def act(self, delta_time: float):
        self.x -= 150 * delta_time
        if self.x < 0:
            self.x = 1280


class Bg(game.scene2d.MyActor):
    def __init__(self):
        super().__init__("image/hat_kep_j.png")


class Main(game.scene2d.MyActor):
    def __init__(self):
        super().__init__("image/main.png")


class Arrow(game.scene2d.MyActor):
    def __init__(self):
        super().__init__("image/nyil_main.png")

class Arrow_r(game.scene2d.MyActor):
    def __init__(self):
        super().__init__("image/nyil_main_f.png")

class Info(game.scene2d.MyActor):
    def __init__(self):
        super().__init__("image/info.png")


class Coin(game.scene2d.MyActor):
    def __init__(self):
        super().__init__("image/coin.png")

    def act(self, delta_time: float):
        self.x -= 150 * delta_time
        if self.x < 0:
            self.x = 1280

class Selectimage(game.scene2d.MyActor):
    def __init__(self):
        super().__init__("image/Select.png")

class Deagle2(game.scene2d.MyActor):
    def __init__(self):
        super().__init__("image/r6-uj-edit-d2.png")

class Deagle3(game.scene2d.MyActor):
    def __init__(self):
        super().__init__("image/r6-uj-edit-d3.png")

class Deagle4(game.scene2d.MyActor):
    def __init__(self):
        super().__init__("image/r6-uj-edit-d4.png")



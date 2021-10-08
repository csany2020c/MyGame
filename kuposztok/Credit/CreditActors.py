import game


class Creditlist(game.scene2d.MyActor):
    def __init__(self):
        self.credit = super().__init__('image/Credit_list.png')

class Visszagomb(game.scene2d.MyActor):
    def __init__(self):
        self.credit = super().__init__('image/Vissza.png')
import game


class Creditlist(game.scene2d.MyActor):
    def __init__(self):
        self.credit = super().__init__('image/credit.png')

class Visszagomb(game.scene2d.MyActor):
    def __init__(self):
        self.credit = super().__init__('image/back_to_menu_button.png')
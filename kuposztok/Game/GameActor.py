import game

class BgActor(game.scene2d.MyActor):

    def __init__(self):
        super().__init__('image/menu.png')


class MyyActor(game.scene2d.MyActor):

    def __init__(self):
        super().__init__('image/icon.png')
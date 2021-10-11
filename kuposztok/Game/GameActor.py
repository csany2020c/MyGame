import game

class BgActor(game.scene2d.MyActor):

    def __init__(self):
        super().__init__('../image/test.jpg')


class MyyActor(game.scene2d.MyActor):

    def __init__(self):
        super().__init__('../image/icon.png')

class Visszagomb(game.scene2d.MyActor):
    def __init__(self):
        self.credit = super().__init__('../image/Vissza.png')


class Joseph(game.scene2d.MyActor):
    def __init__(self):
        self.credit = super().__init__('image/my-caracter.png')
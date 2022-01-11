import game

class halalhatter(game.scene2d.MyActor):

    def __init__(self):
        super().__init__("images/halal.jpg")
        self.set_width(1300)

class restartgomb(game.scene2d.MyActor):

    def __init__(self):
        super().__init__("images/restart.png")

class fomenugomb(game.scene2d.MyActor):

    def __init__(self):
        super().__init__("images/fomenu.png")

class kilepesgomb(game.scene2d.MyGame):

    def __init__(self):
        super().__init__("images/kilepes.png")

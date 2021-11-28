import game


class menuhatter(game.scene2d.MyActor):

    def __init__(self):
        super().__init__("images/menuhatter.jpg")
        
class startactor(game.scene2d.MyActor):

    def __init__(self):
        super().__init__("images/start.png")

class kilepesactor(game.scene2d.MyActor):

    def __init__(self):
        super().__init__("images/kilepes.png")

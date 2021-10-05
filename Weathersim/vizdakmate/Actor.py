import game

class Sun(game.scene2d.MyActor):
    def __init__(self):
        super().__init__("sun.png")

class Background(game.scene2d.MyActor):
    def __init__(self):
        super().__init__("landscape.png")

class Sunny(game.scene2d.MyActor):
    def __init__(self):
        super().__init__("sunny.png")

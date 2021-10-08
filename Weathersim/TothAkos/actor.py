import game

class Sun(game.scene2d.MyActor):
    def __init__(self):
        super().__init__("images/sun.png")

class Landscape(game.scene2d.MyActor):
    def __init__(self):
        super().__init__("images/landscape.png")

class Sunny(game.scene2d.MyActor):
    def __init__(self):
        super().__init__("images/sunny.png")

class Snow (game.scene2d.MyActor):
    def __init__(self):
        super().__init__("images/snow.png")

class cloudy (game.scene2d.MyActor):
    def __init__(self):
        super().__init__("images/cloudy")
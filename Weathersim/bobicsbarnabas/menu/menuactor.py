import game

class menuactor(game.scene2d.MyActor):

    def __init__(self):
        super().__init__("resources/images/fox.png")
        self.width = 100
        self.height = 100
        self.x = 640
        self.y = 360
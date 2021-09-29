import game

class MenuActor1(game.scene2d.MyActor):
    def __init__(self, image_url: str = ""):
        super().__init__("../yetifc/Images/play.png")
        self.set_width(300)
        self.x = 500
        self.y = 10
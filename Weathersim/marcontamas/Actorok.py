import game

class MenuHatter(game.scene2d.MyActor):
    def __init__(self, image_url: str = "bg.jpg"):
        super().__init__(image_url)
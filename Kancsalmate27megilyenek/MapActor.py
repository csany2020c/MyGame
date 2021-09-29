import game

class Map(game.scene2d.MyActor):
    def __init__(self, image_url: str = "map/terkep.png"):
        super().__init__(image_url)
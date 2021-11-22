import game
from game.simpleworld.ShapeType import ShapeType

class GrassActor(game.scene2d.MyActor):
    def __init__(self, image_url: str = "Grass.png"):
        super().__init__(image_url)
        self.z_index = 0
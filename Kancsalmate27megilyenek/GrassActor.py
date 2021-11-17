import game

class GrassActor(game.scene2d.MyActor):
    def __init__(self, image_url: str = "Texture/Grass.png"):
        super().__init__(image_url)
        self.set_size(30,30)
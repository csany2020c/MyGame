import game
class WaterActor(game.scene2d.MyActor):
    def __init__(self, image_url: str = "WaterActor.png"):
        super().__init__(image_url)
        self.z_index = 0
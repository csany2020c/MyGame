import game

class WaterActor(game.scene2d.MyActor):
    def __init__(self, image_url: str = "Water.png"):
        super().__init__(image_url)
        self.set_size(64, 64)
        self.z_index = 0

class GrassActor(game.scene2d.MyActor):
    def __init__(self, image_url: str = "Grass.png"):
        super().__init__(image_url)
        self.set_size(64, 64)
        self.z_index = 0

class SandActor(game.scene2d.MyActor):
    def __init__(self, image_url: str = "Sand.png"):
        super().__init__(image_url)
        self.set_size(64, 64)
        self.z_index = 0

class StoneActor(game.scene2d.MyActor):
    def __init__(self, image_url: str = "Stone.png"):
        super().__init__(image_url)
        self.set_size(64, 64)
        self.z_index = 0
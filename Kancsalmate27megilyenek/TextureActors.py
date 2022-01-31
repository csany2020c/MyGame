import game

class WaterActor(game.scene2d.MyActor):
    def __init__(self, image_url: str = "Water.png"):
        super().__init__(image_url)
        self.set_size(64, 64)
        self.z_index = 0

class WaterActor2(game.scene2d.MyActor):

    def __init__(self, image_url: str = "water2.png"):
        super().__init__(image_url)
        self.set_size(64,64)
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

class PathActor(game.scene2d.MyActor):
    def __init__(self, image_url: str = "Path.png"):
        super().__init__(image_url)
        self.set_size(64, 64)
        self.z_index = 0

class HeartActor(game.scene2d.MyActor):
    def __init__(self, image_url: str = "Heart.png"):
        super().__init__(image_url)
        self.set_size(32, 32)
        self.z_index = 1

class DamageActor(game.scene2d.MyActor):
    def __init__(self, image_url: str = "lava.png"):
        super().__init__(image_url)
        self.z_index = 1
        self.set_size(64, 64)

class DamageActor(game.scene2d.MyActor):
    def __init__(self, image_url: str = "lava.png"):
        super().__init__(image_url)
        self.z_index = 1
        self.set_size(64, 64)

class HealActor(game.scene2d.MyActor):
    def __init__(self, image_url: str = "Heal.png"):
        super().__init__(image_url)
        self.z_index = 1
        self.set_size(64, 64)
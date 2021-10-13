import game

class Alap(game.scene2d.MyActor):
    def __init__(self, image_url: str = "landscape.png"):
        super().__init__(image_url)

class Eg(game.scene2d.MyActor):
    def __init__(self, image_url: str = "sunny.png"):
        super().__init__(image_url)

class Nap(game.scene2d.MyActor):
    def __init__(self, image_url: str = "sun.png"):
        super().__init__(image_url)
        self.set_size(400,400)
        self.x = 1280 - 300

    def act(self, delta_time: float):
        super().act(delta_time)
        self.x = self.x - 1.1
        if self.x <= 0-350:
            self.x = 1280
        self.rotation = self.rotation + 0.1

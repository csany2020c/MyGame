import game

class bruhActor(game.scene2d.MyActor):
    def __init__(self):
        super().__init__("Images/test.png")

    def act(self, delta_time: float):
        super().act(delta_time)
        self.x += delta_time * 100

class enemy1(game.scene2d.MyActor):
    def __init__(self):
        super().__init__("Images/Normal.png")
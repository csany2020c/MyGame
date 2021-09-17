import game

class bruhActor(game.scene2d.MyActor):
    def __init__(self):
        super().__init__("test.png")

    def act(self, delta_time: float):
        super().act(delta_time)
        self.x += delta_time * 50
import game

class Enemy1Actor(game.scene2d.MyActor):

    def __init__(self):
        super().__init__("image/startb.png")

    def act(self, delta_time: float):
        super().act(delta_time)
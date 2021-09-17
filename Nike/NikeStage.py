import game
from NikeEnemyActor import *


class NikeStage(game.scene2d.MyStage):

    def __init__(self):
        super().__init__()
        self.b = Enemy1Actor()
        self.add_actor(self.b)
        for j in range(0, 10):
            for i in range(0, 10):
                e = Enemy1Actor()
                e.y = i * 40
                e.x = j * 40
                # e.width = 10
                # e.height = 10
                self.add_actor(e)

    def act(self, delta_time: float):
        super().act(delta_time)
        self.actors[20].width = 200
        self.b.r -= 2


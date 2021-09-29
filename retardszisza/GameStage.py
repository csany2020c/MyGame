import game
from retardszisza.EnemyActor import *


class GameStage(game.scene2d.MyStage):

    def __init__(self):
        super().__init__()
        self.b = Enemy1Actor()
        self.add_actor(self.b)
        self.b.y = 150

    def act(self, delta_time: float):
        super().act(delta_time)





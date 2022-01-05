import game
from Kancsalmate27megilyenek.TextureActors import WaterActor, GrassActor, SandActor, StoneActor, PathActor
from game.scene2d import MyBaseActor
from Kancsalmate27megilyenek.PlayerActor import *
from Kancsalmate27megilyenek.Map import *

class ArenaStage(game.scene2d.MyStage):
    def __init__(self):
        super().__init__()
        self.map = Map(self,"arena")
        self.player = PlayerActor()
        self.add_actor(self.player)
        self.player.set_x = 500
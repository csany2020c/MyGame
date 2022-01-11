import game
from Kancsalmate27megilyenek.TextureActors import WaterActor, GrassActor, SandActor, StoneActor, PathActor
from game.scene2d import MyBaseActor
from Kancsalmate27megilyenek.PlayerActor import *
from Kancsalmate27megilyenek.Map import *
from random import Random
from Kancsalmate27megilyenek.Enemy import *


class ArenaStage(game.scene2d.MyStage):
    def __init__(self):
        super().__init__()
        self.map = Map(self,"arena")
        self.player = PlayerActor()
        self.add_actor(self.player)
        self.player.set_x = 500
        r = Random()

        enemys:int = int(r.randint(1,5))
        for i in range(enemys):
            type:int = r.randint(1,2)
            self.actor = MyActor()
            # if type==1:
            #     Enemy("cigany",self)
            # elif type==2:
            #     self.add_actor()Enemy("jani",self)


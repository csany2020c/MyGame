import game
from Kancsalmate27megilyenek.TextureActors import WaterActor, GrassActor, SandActor, StoneActor, PathActor
from game.scene2d import MyBaseActor
from Kancsalmate27megilyenek.PlayerActor import *
from Kancsalmate27megilyenek.Map import *
from random import Random
from Kancsalmate27megilyenek.Enemy import getDatas
from game.scene2d.MyActor import *


class ArenaStage(game.scene2d.MyStage):
    def __init__(self):
        super().__init__()
        self.map = Map(self,"arena")
        self.player = PlayerActor()
        self.add_actor(self.player)
        self.player.set_x = 500
        r = Random()

        enemys:int = int(r.randint(1,5))
        enemy = list()
        for i in range(enemys):
            type:int = int(r.randint(1,2))
            if type==1:
                self.enemy1 = getDatas(self,"jani")
                self.enemy1speed = self.enemy1.speed
                enemy.append(self.enemy1)
            elif type==2:
                self.enemy2 = getDatas(self,"cigany")
                enemy.append(self.enemy2)
        for i in (enemy):
            print("ENNYI VAN : " + str(len(enemy)))
    def act(self, delta_time: float):
        super().act(delta_time)





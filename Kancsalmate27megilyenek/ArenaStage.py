import game
from Kancsalmate27megilyenek.TextureActors import WaterActor, GrassActor, SandActor, StoneActor, PathActor
from game.scene2d import MyBaseActor
from game.scene2d import MyLabel
from Kancsalmate27megilyenek.PlayerActor import *
from Kancsalmate27megilyenek.Map import *
from random import Random
from Kancsalmate27megilyenek.Enemy import getDatas,Enemy
from game.scene2d.MyActor import *
from game.scene2d.MyGame import MyGame
from game.scene2d.MyActor import *


class ArenaStage(game.scene2d.MyStage):
    def __init__(self):
        super().__init__()
        self.map = Map(self,"arena")
        self.player = PlayerActor()
        self.add_actor(self.player)
        self.player.set_x = 500
        r = Random()



        enemys:int = int(r.randint(1,3))
        enemy:List['getDatas'] = list()
        enemyActor:List['Enemy'] = list()
        self.x:int = int(0)
        for i in range (enemys):
            type:int = int(r.randint(0,1))
            enemy.append(getDatas(self,type))
            enemyActor.append(enemy[0].getActor())
        for i in range(len(enemyActor)):
            enemyActor[i].drawhp(self, 0,0)
            if i!=0:
                enemyActor[i].y = enemyActor[i - 1].get_y() + 200
                enemyActor[i].drawhp(self,enemyActor[i].get_x(),enemyActor[i-1].get_y() + 200)
            self.add_actor(enemyActor[i])
            enemyActor[i].set_damage(enemy[i].damage)
            enemyActor[i].set_hp(enemy[i].hp)

            # print("pos: " + str(i.get_x))
            # print("Hossz:" + str(len(enemyActor)))



    def act(self, delta_time: float):
        super().act(delta_time)





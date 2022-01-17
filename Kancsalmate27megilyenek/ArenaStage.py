import game
from Kancsalmate27megilyenek.PickEnemy import *
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
from Kancsalmate27megilyenek.AttackActor import *
from game.scene2d.MyTimers import *
import pygame


class ArenaStage(game.scene2d.MyStage):
    def __init__(self):
        super().__init__()
        self.showAttack:bool = False
        pygame.init()
        self.info = pygame.display.Info()
        self.width = self.info.current_w
        self.height = self.info.current_h
        self.index:int = None
        self.map = Map(self,"arena")
        self.player = PlayerActor()
        self.add_actor(self.player)
        self.player.set_x = 500
        r = Random()


        enemys:int = int(r.randint(1,3))
        enemy:List['getDatas'] = list()
        self.enemyActor:List['Enemy'] = list()
        self.x:int = int(0)
        for i in range (enemys):
            type:int = int(r.randint(0,1))
            enemy.append(getDatas(self,type))
            self.enemyActor.append(enemy[0].getActor())
        for i in range(len(self.enemyActor)):
            self.enemyActor[i].drawhp(self, 0,0)
            if i!=0:
                self.enemyActor[i].y = self.enemyActor[i - 1].get_y() + 200
                self.enemyActor[i].drawhp(self,self.enemyActor[i].get_x(),self.enemyActor[i-1].get_y() + 200)
            self.add_actor(self.enemyActor[i])
            self.enemyActor[i].set_damage(enemy[i].damage)
            self.enemyActor[i].set_hp(enemy[i].hp)

        self.attack = AttackActor()
        self.attack.set_size(50,50)
        self.attack.x = self.width / 2 - self.attack.get_width() / 2
        self.attack.y = self.height - self.attack.get_height() - 20
        self.add_actor(self.attack)
        self.attack.set_on_mouse_down_listener(self.attackDef)

        # self.cooldown = MyIntervalTimer(func=self.cooldownTimer, start_time=1, stop_time=3)

        for i in range (len(self.pickEnemyList)):
            if len(self.pickEnemyList) > 0:
                self.pickEnemyList[i].set_on_mouse_down_listener(self.AttackEnemy)
                self.index = i



    def attackDef(self,sender,event):
        if event.button == 1:
            self.pickEnemyList: List['PickEnemy'] = list()
            for i in range(len(self.enemyActor)):
                self.pickenemy = PickEnemy()
                self.pickEnemyList.append(self.pickenemy)
            if self.showAttack == False:
                for i in range (len(self.pickEnemyList)):
                    self.add_actor(self.pickEnemyList[i])
                    self.pickEnemyList[i].y = self.attack.get_y() - self.attack.get_height() - 10
                    self.pickEnemyList[i].x = self.attack.get_x() + i * 100
                    self.pickEnemyList[i].set_size(50, 50)
                self.showAttack = True
            else:
                removeAbleActors: List['PickEnemy'] = list()
                for i in range (len(self.actors)):
                    if isinstance(self.actors[i], PickEnemy):
                        removeAbleActors.append(self.actors[i])
                for i in (removeAbleActors):
                    i.remove_from_stage()
                self.showAttack = False


    def AttackEnemy(self,sender,event):
        if self.index != None:
            self.player.x = self.enemyActor[self.index].get_x()
            self.player.y = self.enemyActor[self.index].get_y()
        # self.add_timer(self.cooldown)



    def cooldownTimer(self,sender,event):
        self.player.x = self.width/2  - self.player.get_width()/2
        self.player.y = self.height/2 - self.player.get_height()/2



            # print("pos: " + str(i.get_x))
            # print("Hossz:" + str(len(enemyActor)))



    def act(self, delta_time: float):
        super().act(delta_time)





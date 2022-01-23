import time

import game
from Kancsalmate27megilyenek.ArrowActor import ArrowActor
from Kancsalmate27megilyenek.DistanceBetween import intermediates
from Kancsalmate27megilyenek.EnemyActor import *
from Kancsalmate27megilyenek.HPBAR import *
from Kancsalmate27megilyenek.PickEnemy import *
from Kancsalmate27megilyenek.Test import Test
from Kancsalmate27megilyenek.TextureActors import WaterActor, GrassActor, SandActor, StoneActor, PathActor
from game.scene2d import MyBaseActor
from game.scene2d import MyLabel
from Kancsalmate27megilyenek.PlayerActor import *
from Kancsalmate27megilyenek.Map import *
from random import Random
from game.scene2d.MyActor import *
from game.scene2d.MyGame import MyGame
from game.scene2d.MyActor import *
from Kancsalmate27megilyenek.AttackActor import *
from Kancsalmate27megilyenek.Enemys import Enemy
from game.scene2d.MyTimers import *
import pygame


class ArenaStage(game.scene2d.MyStage):
    def __init__(self):
        super().__init__()
        self.selected = None
        #self.showAttack:bool = False
        #self.stageEnemys:List['Enemy'] = list()
        self.enemyList:List['EnemyActor'] = list()
        self.hpbarlist:List['HPBAR'] = list()
        self.labelList:List['MyLabel'] = list()
        pygame.init()
        self.info = pygame.display.Info()
        self.width = self.info.current_w
        self.height = self.info.current_h
        self.minHP:float = 0
        #self.index:int = None
        self.map = Map(self,"arena")
        self.circle = MyActor("redcircle.png")
        self.player = PlayerActor()
        self.add_actor(self.player)
        self.player.set_x = 500
        r = Random()

        self.intermediates = None
        self.arrow = None
        for i in range(2):
            #Ellenfelek létrehozása
            self.enemy = EnemyActor(i,100,int(self.height/12 + i*150))
            self.add_actor(self.enemy)
            self.enemy.set_size(int(self.width/16),int(self.width/16))
            self.enemyList.append(self.enemy)
            #HPBAR
            # self.hpbar = HPBAR(int(self.enemyList[i].get_x()) - 15,int(self.enemyList[i].get_y() - 15))
            # self.add_actor(self.hpbar)
            # self.hpbarlist.append(self.hpbar)
            # #redhp
            # for i in self.hpbarlist:
            #     self.redhp = REDHP(i.x,i.y)
            #     self.add_actor(self.redhp)
            #     self.redhplist.append(self.redhp)

            #Label
            self.hpLabel = MyLabel("","system",64,[255,0,0])
            self.add_actor(self.hpLabel)
            self.hpLabel.x = self.enemyList[i].get_x()
            self.hpLabel.y = self.enemyList[i].get_y() - 25
            self.labelList.append(self.hpLabel)


        for i in self.enemyList:
            i.set_on_mouse_down_listener(self.handleClick)


    def act(self, delta_time: float):
        super().act(delta_time)
        for a in self.actors:
            if isinstance(a,ArrowActor):
                for i in range(len(self.enemyList)):
                    self.minHP = 25/self.enemyList[i].maxHP
                    if a.overlaps(self.enemyList[i]):
                        a.remove_from_stage()
                        self.enemyList[i].hp = self.enemyList[i].hp - 20

                if a.fly == False:
                    a.remove_from_stage()

        for l in range(len(self.labelList)):
            if (self.enemyList[l].hp > 0):
                self.labelList[l].set_text(str(self.enemyList[l].hp))
            else:
                self.labelList[l].set_text(str(0))

    def handleClick(self,sender,event):
        if event.button == 1 and self.selected != sender:
            self.circle.x = sender.get_x() - 20
            self.circle.y = sender.get_y() - 20
            self.enemyC = sender
            if self.circle.get_stage is None:
                self.add_actor(self.circle)
            else:
                self.circle.remove_from_stage()
                self.add_actor(self.circle)
            self.selected = sender
            self.intermediates = intermediates([self.player.get_x(),self.player.get_y()],[sender.get_x(),sender.get_y()],nb_points=100)
            self.arrow = ArrowActor(self.intermediates)
            self.add_actor(self.arrow)





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
from game.scene2d.MyCamera import *
from Kancsalmate27megilyenek.ExplosionActor import *
import pygame


class ArenaStage(game.scene2d.MyStage):
    def __init__(self):
        super().__init__()
        self.selected = None
        #self.showAttack:bool = False
        #self.stageEnemys:List['Enemy'] = list()
        self.enemyList:List['EnemyActor'] = list()
        self.hphudlist:List['HPHUD'] = list()
        self.hpbarlist:List['HPBAR'] = list()
        self.labelList:List['MyLabel'] = list()
        self.xPos:float = 0
        pygame.init()
        self.info = pygame.display.Info()
        self.width = self.info.current_w
        self.height = self.info.current_h
        self.minHP:float = 0
        #self.index:int = None
        self.map = Map(self,"arena")
        self.circle = MyActor("redcircle.png")
        self.player = PlayerActor()
        self.camera.tracking = self.player
        self.add_actor(self.player)
        self.player.set_x = 500
        r = Random()

        self.intermediates = None
        self.arrow = None
        for i in range(2):
            #Ellenfelek létrehozása
            self.enemy = EnemyActor(i,100,int(self.height/12 + i*150),self)
            self.add_actor(self.enemy)
            self.enemy.set_size(int(self.width/16),int(self.width/16))
            self.enemyList.append(self.enemy)
            #HPHUD
            self.hphud = HPHUD(int(self.enemyList[i].get_x()) - 15,int(self.enemyList[i].get_y() - 105))
            self.add_actor(self.hphud)
            self.hphudlist.append(self.hphud)
            #HPBAR
        for i in range(len(self.hphudlist)):
            self.hpbar = HPBAR()
            self.add_actor(self.hpbar)
            self.hpbar.x = self.hphudlist[i].get_x() + self.hphudlist[i].get_width() * 0.3
            self.xPos = self.hpbar.get_x()
            self.hpbar.y = self.hphudlist[i].get_y() + self.hphudlist[i].get_height() * 0.33
            self.hpbarlist.append(self.hpbar)

            #Label
            # self.hpLabel = MyLabel("","system",64,[255,0,0])
            # self.add_actor(self.hpLabel)
            # self.hpLabel.x = self.enemyList[i].get_x()
            # self.hpLabel.y = self.enemyList[i].get_y() - 25
            # self.labelList.append(self.hpLabel)


        for i in range(len(self.enemyList)):
            print("INDEX:" + str(self.enemyList[i]))
            self.enemyList[i].set_on_mouse_down_listener(self.handleClick)


    def act(self, delta_time: float):
        super().act(delta_time)
        for a in self.actors:
            if isinstance(a,ArrowActor):
                for i in range(len(self.enemyList)):
                    self.minHP = self.hpbarlist[i].get_width()/self.enemyList[i].maxHP
                    if a.overlaps(self.enemyList[i]):
                        self.enemyList[i].hp = self.enemyList[i].hp - 25
                        a.remove_from_stage()
                        if self.minHP * self.enemyList[i].hp > 0:
                            self.hpbarlist[i].set_size(self.minHP * self.enemyList[i].hp,9)
                            self.hpbarlist[i].set_position(self.xPos,self.hphudlist[i].get_y() + self.hphudlist[i].get_height() * 0.33)
                        else:
                            self.hpbarlist[i].set_size(0,9)
                            self.hpbarlist[i].set_position(self.xPos,self.hphudlist[i].get_y() + self.hphudlist[i].get_height() * 0.33)

                if a.fly == False:
                    a.remove_from_stage()

    def handleClick(self,sender,event):
        if event.button == 1:
            for i in range(99):
                print("klikkbe benne")
            # self.circle.x = sender.get_x() - 20
            # self.circle.y = sender.get_y() - 20
            # self.enemyC = sender
            # if self.circle.get_stage is None:
            #     self.add_actor(self.circle)
            # else:
            #     self.circle.remove_from_stage()
            #     self.add_actor(self.circle)
            # self.selected = sender
            # self.intermediates = intermediates([self.player.get_x(),self.player.get_y()],[sender.get_x(),sender.get_y()],nb_points=100)
            # self.arrow = ArrowActor(self.intermediates)
            # self.add_actor(self.arrow)






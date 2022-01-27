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
        # Player cuccai
        self.player = PlayerActor()
        self.camera.tracking = self.player
        self.add_actor(self.player)
        self.player.set_x = 500
        self.pHpHUD = HPHUD(int(self.player.get_x()),int(self.player.get_y()))
        self.add_actor(self.pHpHUD)
        self.pHpBar = HPBAR()
        self.add_actor(self.pHpBar)
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
        #Billentyu kezelesek
        self.set_on_key_down_listener(self.handleKeyDown)
        #Delay
        self.delay = MyTickTimer(func=self.timeHandle,interval=1.5, start_delay=0,repeat=True)
            #Label
            # self.hpLabel = MyLabel("","system",64,[255,0,0])
            # self.add_actor(self.hpLabel)
            # self.hpLabel.x = self.enemyList[i].get_x()
            # self.hpLabel.y = self.enemyList[i].get_y() - 25
            # self.labelList.append(self.hpLabel)

    def timeHandle(self,sender):
        self.set_on_key_down_listener(self.handleKeyDown)
    def act(self, delta_time: float):
        super().act(delta_time)
        if self.pHpBar:
            self.pHpHUD.set_position(self.player.get_x(),self.player.get_y() - 105)
            self.pHpBar.set_position(self.pHpHUD.get_x() + self.pHpHUD.get_width() * 0.3,self.pHpHUD.get_y() + self.pHpHUD.get_height() * 0.33)
            self.pHpBar.set_size(140/self.player.max_hp * self.player.hp,9)

        for a in self.actors:
            if isinstance(a,ArrowActor):
                for i in range(len(self.enemyList)):
                    self.minHP = 140/self.enemyList[i].maxHP
                    if a.overlaps(self.enemyList[i]):
                        self.enemyList[i].hp = self.enemyList[i].hp - 25
                        a.remove_from_stage()
                        print("SZÉLESSÉG:" + str(self.minHP * self.enemyList[i].hp))
                        if self.minHP * self.enemyList[i].hp > 0:
                            self.hpbarlist[i].set_size(self.minHP * self.enemyList[i].hp,9)
                            self.hpbarlist[i].set_position(self.xPos,self.hphudlist[i].get_y() + self.hphudlist[i].get_height() * 0.33)
                        else:
                            self.remove_actor(self.enemyList[i])
                            self.remove_actor(self.hphudlist[i])
                            self.remove_actor(self.hpbarlist[i])
                            self.enemyList.remove(self.enemyList[i])
                            self.hphudlist.remove(self.hphudlist[i])
                            self.hpbarlist.remove(self.hpbarlist[i])
                if a.fly == False:
                    a.remove_from_stage()
            if isinstance(a,ExplosionActor):
                if a.overlaps(self.player):
                    print("Player hp-ja:" + str(self.player.hp))
                    self.player.hp = self.player.hp - self.player.max_hp * 0.001



    def handleKeyDown(self,sender,event):
        if event.key == pygame.K_1:
            self.smaller:float = 99999
            self.target = None
            for i in self.enemyList:
                if (math.sqrt((i.get_x() - self.player.get_x())**2 + (i.get_y() - self.player.get_y())**2) < self.smaller):
                    self.smaller = math.sqrt((i.get_x() - self.player.get_x())**2 + (i.get_y() - self.player.get_y())**2)
                    self.target = i


            self.intermediates = intermediates([self.player.get_x(),self.player.get_y()],[self.target.get_x(),self.target.get_y()],nb_points=100)
            self.arrow = ArrowActor(self.intermediates)
            self.add_actor(self.arrow)
            self.remove_on_key_down_listener()
            self.add_timer(self.delay)






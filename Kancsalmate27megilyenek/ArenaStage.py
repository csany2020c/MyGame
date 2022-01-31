import random
import time

from sympy import Point

import game
from Kancsalmate27megilyenek.AlertBox import *
from Kancsalmate27megilyenek.ArrowActor import ArrowActor
from Kancsalmate27megilyenek.DistanceBetween import intermediates
from Kancsalmate27megilyenek.EnemyActor import *
from Kancsalmate27megilyenek.HPBAR import *
from Kancsalmate27megilyenek.PickEnemy import *
from Kancsalmate27megilyenek.Test import Test
from Kancsalmate27megilyenek.TextureActors import WaterActor, GrassActor, SandActor, StoneActor, PathActor
from Kancsalmate27megilyenek.UltActor import UltActor
from Kancsalmate27megilyenek.WildPig import WildPig
from game.scene2d import MyBaseActor
from game.scene2d import MyLabel
from Kancsalmate27megilyenek.PlayerActor import *
from Kancsalmate27megilyenek.Map import *
from random import Random
from game.scene2d.MyActor import *
from game.scene2d.MyGame import MyGame
from game.scene2d.MyActor import *
from Kancsalmate27megilyenek.WinScreen import *
from Kancsalmate27megilyenek.AttackActor import *
from Kancsalmate27megilyenek.Enemys import Enemy
from game.scene2d.MyTimers import *
from game.scene2d.MyCamera import *
from Kancsalmate27megilyenek.ExplosionActor import *
from Kancsalmate27megilyenek.AngleCalc import *
import pygame


class ArenaStage(game.scene2d.MyStage):
    def __init__(self):
        super().__init__()
        self.selected = None
        self.ultimate = False
        self.isUltShowing = False
        self.ultactor = None
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
        self.pxpLabel = MyLabel()
        self.pxpLabel.set_text(str(int(self.player.playerDatas.playerpropertie.pLevel)))
        self.add_actor(self.pxpLabel)
        r = Random()
        self.wildpigTimer = MyTickTimer(func=self.wildpigGenerate,interval=5,start_delay=0,repeat=True)
        self.add_timer(self.wildpigTimer)

        self.alert = AlertBox(self,"Sikeresen legyőzted ezt a szintet!")

        self.intermediates = None
        self.arrow = None
        self.rand = random.randint(1,5)
        for i in range(self.rand):
            #Ellenfelek létrehozása
            self.enemy = EnemyActor(random.randint(0,1),100,int(self.height/12 + i*150),self)
            self.add_actor(self.enemy)
            self.enemy.set_size(int(self.width/16),int(self.width/16))
            if self.player.mLevel > 1:
                self.randLvl = random.randint(self.player.mLevel-1,self.player.mLevel)
                self.enemy.lvl = self.randLvl
                self.enemy.maxHP += self.enemy.lvl * 50
                self.enemy.hp += self.enemy.lvl * 50
                self.enemy.damage += self.enemy.lvl *25
            else:
                self.enemy.lvl = 1
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
            self.xpLabel = MyLabel()
            self.xpLabel.set_position(self.hphudlist[i].get_x() + 22,self.hphudlist[i].get_y() + self.hphudlist[i].get_height()/2 - 15)
            self.xpLabel.set_text(str(self.enemyList[i].lvl))
            self.add_actor(self.xpLabel)
            self.labelList.append(self.xpLabel)
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
    def wildpigGenerate(self,sender):
        for a in self.actors:
            if a.get_x() > self.width:
                a.remove_from_stage()
        self.add_actor(WildPig())
    def timeHandle(self,sender):
        self.set_on_key_down_listener(self.handleKeyDown)

    def index_in_list(self,a_list, index) -> bool:
        return(index < len(a_list))
    def act(self, delta_time: float):
        super().act(delta_time)

        if self.player.dealtDMG >= 150:
            self.ultimate = True
            self.isUltShowing = True

        if self.isUltShowing == True:
            if self.ultactor == None:
                self.ultactor = UltActor()
                self.add_actor(self.ultactor)
            else:
                self.ultactor.set_position(self.camera.x + self.width / 2 - self.ultactor.get_width()/2,self.camera.y)

        if self.pHpBar:
            self.pHpHUD.set_position(self.player.get_x(),self.player.get_y() - 105)
            self.pHpBar.set_position(self.pHpHUD.get_x() + self.pHpHUD.get_width() * 0.3,self.pHpHUD.get_y() + self.pHpHUD.get_height() * 0.33)
            self.pxpLabel.set_position(self.pHpHUD.get_x() + 22,self.pHpHUD.get_y() + self.pHpHUD.get_height()/2 - 15)
            if 140/self.player.max_hp * self.player.hp > 0:
                self.pHpBar.set_size(140/self.player.max_hp * self.player.hp,9)
            else:
                self.pHpBar.set_size(0,9)


        if len(self.enemyList) < 1:
            self.player.playerDatas.playerpropertie.mLevel +=1
            self.player.playerDatas.update()
            self.screen.game.set_screen(WinScreen(self.player.playerDatas.playerpropertie.mLevel,self.player.playerDatas.playerpropertie.pLevel))
        else:
            for i in range(len(self.hphudlist)):
                self.hphudlist[i].set_position(int(self.enemyList[i].get_x()) - 15,int(self.enemyList[i].get_y() - 105))
                self.hpbarlist[i].set_position(self.hphudlist[i].get_x() + self.hphudlist[i].get_width() * 0.3,self.hphudlist[i].get_y() + self.hphudlist[i].get_height() * 0.33)
                self.labelList[i].set_position(self.hphudlist[i].get_x() + 22,self.hphudlist[i].get_y() + self.hphudlist[i].get_height()/2 - 15)
        if self.player.hp <= 0:
            self.player.hp = 0
            self.screen.game.set_screen(LoseScreen(self.player.playerDatas.playerpropertie.mLevel,self.player.playerDatas.playerpropertie.pLevel))





        for a in self.actors:
            if isinstance(a,ArrowActor):
                for i in range(len(self.enemyList)):
                    if self.index_in_list(self.enemyList, i):
                        if a.overlaps(self.enemyList[i]):
                            self.minHP = 140 / self.enemyList[i].maxHP
                            self.enemyList[i].hp = self.enemyList[i].hp - self.player.playerDatas.playerpropertie.pDMG
                            self.player.dealtDMG += self.enemyList[i].hp - self.player.playerDatas.playerpropertie.pDMG
                            a.remove_from_stage()
                            if self.minHP * self.enemyList[i].hp > 0:
                                self.hpbarlist[i].set_size(self.minHP * self.enemyList[i].hp,9)
                                self.hpbarlist[i].set_position(self.xPos,self.hphudlist[i].get_y() + self.hphudlist[i].get_height() * 0.33)
                            else:
                                self.player.playerDatas.playerpropertie.pLevel += 0.2
                                self.remove_actor(self.enemyList[i])
                                self.remove_actor(self.hphudlist[i])
                                self.remove_actor(self.hpbarlist[i])
                                self.remove_actor(self.labelList[i])
                                self.enemyList.pop(i)
                                self.hphudlist.pop(i)
                                self.hpbarlist.pop(i)
                                self.labelList.pop(i)
                    else:
                        i+=1
                if a.fly == False:
                    a.remove_from_stage()
                else:
                    self.arrow.rotation = self.rot
            if isinstance(a,ExplosionActor):
                if a.overlaps(self.player):
                    self.player.hp -= a.dmg / 100

            if isinstance(a,ArrowActor2):
                if a.overlaps(self.player):
                    self.player.hp -= a.damage
                    a.remove_from_stage()

            if isinstance(a,WildPig):
                if a.overlaps(self.player):
                    self.player.hp -= 25

            if isinstance(a,WaterActor):
                if a.overlaps(self.player):
                    self.player.b = 2
            if isinstance(a, GrassActor):
                if a.overlaps(self.player):
                    self.player.b = 5

            if isinstance(a,SandActor):
                if a.overlaps(self.player):
                    self.player.set_position(200,600)
                    self.player.hp -= 20
            if isinstance(a, HealActor):
                if a.overlaps(self.player):
                    self.player.hp += 0.05
            if isinstance(a, DamageActor):
                if a.overlaps(self.player):
                    self.player.hp -= 0.1



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
            self.anglecalc = AngleCalc()
            self.rot = self.anglecalc.angle_between_points((self.player.get_x(),self.player.get_y() + self.player.get_height()/2),(self.target.get_x(),self.target.get_y()))

            self.remove_on_key_down_listener()
            self.add_timer(self.delay)

        elif event.key == pygame.K_2:
            if self.ultimate == True:
                self.player.hp += self.player.max_hp - self.player.hp
                self.ultimate = False
                self.player.dealtDMG = 0
                for i in self.actors:
                    if isinstance(i,UltActor):
                        i.remove_from_stage()
                        i = None







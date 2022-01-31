import random

import pygame
from pygame import mixer

import game
from Kancsalmate27megilyenek.AngleCalc import AngleCalc
from Kancsalmate27megilyenek.ArrowActor import ArrowActor, ArrowActor2
from Kancsalmate27megilyenek.DistanceBetween import intermediates
from Kancsalmate27megilyenek.Enemys import *
from Kancsalmate27megilyenek.ExplosionActor import *
from Kancsalmate27megilyenek.PlayerActor import PlayerActor
from game.scene2d import MyTickTimer, MyStage


class EnemyActor(game.scene2d.MyActor):

    def __init__(self,index:int,x:int, y:int,stage:MyStage):
        super().__init__("Heroamijó_1.png")
        pygame.init()
        self.szelesseg = pygame.display.get_surface().get_width()
        self.magassag = pygame.display.get_surface().get_height()
        self.rStage = stage
        self.selected:bool = False
        self.megy = True
        self.count = 0
        self.player = None
        for a in self.rStage.actors:
            if isinstance(a,PlayerActor):
                self.player = a
                break
        self.explosion = None
        self.enemyC = Enemys()
        self.ellenseg = None
        for i in range(len(self.enemyC.enemys)):
            if self.enemyC.enemys[index]:
                self.ellenseg = self.enemyC.enemys[index]
                break
            else:
                self.ellenseg = None
        self.x = x
        self.y = y
        self.image_url = self.ellenseg.image
        self.lvl:int = int(0)
        self.damage:int = int(self.ellenseg.damage)
        self.maxHP:int = int(self.ellenseg.hp)
        self.hp:int = int(self.maxHP)
        self.timer = MyTickTimer(self.generateCoords,interval=4.5,start_delay=0,repeat=True)
        self.timer2 = MyTickTimer(self.attack, interval=1, start_delay=0, repeat=True)
        self.timer3 = MyTickTimer(self.removeThose,interval=3, start_delay=0, repeat=True)
        self.add_timer(self.timer)
    def generateCoords(self,sender):
        if self.ellenseg.name == "Gnome":
            self.randX = random.randint(int(self.player.get_x() - 100),int(self.player.get_x() + 100))
            self.randY = random.randint(int(self.player.get_y() - 100),int(self.player.get_y() + 100))
            self.rStage.add_actor(RedCircle(self.randX,self.randY))
            self.add_timer(self.timer2)
        elif self.ellenseg.name == "Kardos":
            self.points = intermediates([self.get_x(), self.get_y()], [self.player.get_x(), self.player.get_y()], 100)
            self.arrow = ArrowActor2(self.points,self.damage)
            self.rStage.add_actor(self.arrow)
            self.anglecalc = AngleCalc()
            self.rot = self.anglecalc.angle_between_points((self.get_x(), self.get_y()),(self.player.get_x(), self.player.get_y() + self.player.get_height() / 2))
            self.arrow.rotation = self.rot
    def attack(self,sender):
        if self.ellenseg.name =="Gnome":
            self.rStage.explosion = ExplosionActor(self.randX, self.randY,self.damage)
            self.rStage.add_actor(self.rStage.explosion)
            self.remove_timer(self.timer2)
            self.add_timer(self.timer3)


    def removeThose(self,sender):
        for a in self.rStage.actors:
            if isinstance(a, RedCircle):
                self.rStage.remove_actor(a)
        self.remove_timer(self.timer3)


    def act(self, delta_time: float):
        super().act(delta_time)
        for a in self.rStage.actors:
            if isinstance(a,ExplosionActor):
                if a.image_url == "tile071.png":
                    self.rStage.remove_actor(a)






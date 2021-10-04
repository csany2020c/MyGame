import game
import pygame

from Kancsalmate27megilyenek.MapActor import *
from Kancsalmate27megilyenek.BackgroundActor import *

class InStage(game.scene2d.MyStage):
    def __init__(self):
        super().__init__()
        self.map = Map()
        self.bg = BackgroundActor()
        self.isWPressed : bool = False
        self.isAPressed : bool = False
        self.isSPressed : bool = False
        self.isDPressed : bool = False
        self.add_actor(self.bg)
        self.add_actor(self.map)
        self.bg.set_z_index(0)
        self.map.set_z_index(1)
        self.set_on_key_down_listener(self.moveKeys)
        self.set_on_key_up_listener(self.moveKeysOff)


    def moveKeys(self, sender, event):
        if event.key == pygame.K_w:
            if self.isAPressed == False and self.isSPressed == False and self.isDPressed == False:
                self.isWPressed = True
        if event.key == pygame.K_a:
            if self.isWPressed == False and self.isSPressed == False and self.isDPressed == False:
                        self.isAPressed = True
        if event.key == pygame.K_s:
            if self.isWPressed == False and self.isAPressed == False and self.isDPressed == False:
                        self.isSPressed = True
        if event.key == pygame.K_d:
            if self.isWPressed == False and self.isSPressed == False and self.isAPressed == False:
                        self.isDPressed = True

    def moveKeysOff(self,sender,event):
        if event.key == pygame.K_w:
            self.isWPressed = False
        if event.key == pygame.K_a:
            self.isAPressed = False
        if event.key == pygame.K_s:
            self.isSPressed = False
        if event.key == pygame.K_d:
            self.isDPressed = False

    def act(self, delta_time: float):
        super().act(delta_time)
        if self.isWPressed:
            self.map.y -= 4
        if self.isAPressed:
            self.map.x -= 4
        if self.isSPressed:
            self.map.y += 4
        if self.isDPressed:
            self.map.x += 4
        print(self.bg.x, self.bg.y)




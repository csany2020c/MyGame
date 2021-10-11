import game
import pygame

from Kancsalmate27megilyenek.MapActor import *
from Kancsalmate27megilyenek.BackgroundActor import *
from Kancsalmate27megilyenek.MenuScreen import *
from Kancsalmate27megilyenek.MapActor import *
from Kancsalmate27megilyenek.PlayerActor import *
from game.simpleworld.ShapeType import ShapeType
class InStage(game.scene2d.MyStage):
    def __init__(self):
        super().__init__()
        self.player = PlayerActor()
        self.bg = BackgroundActor()
        self.isWPressed : bool = False
        self.isAPressed : bool = False
        self.isSPressed : bool = False
        self.isDPressed : bool = False
        self.isEscPressed : bool = False
        self.isShiftPressed: bool = False
        self.add_actor(self.bg)
        self.add_actor(self.player)
        self.bg.set_z_index(0)
        self.player.set_z_index(1)
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
        if event.key == pygame.K_ESCAPE:
            self.isEscPressed = True
        if event.key == pygame.K_LSHIFT:
            self.isShiftPressed = True


    def moveKeysOff(self,sender,event):
        if event.key == pygame.K_w:
            self.isWPressed = False
        if event.key == pygame.K_a:
            self.isAPressed = False
        if event.key == pygame.K_s:
            self.isSPressed = False
        if event.key == pygame.K_d:
            self.isDPressed = False
        if event.key == pygame.K_m:
            self.isMPressed = False
        if event.key == pygame.K_LSHIFT:
            self.isShiftPressed = False

    def act(self, delta_time: float):
        super().act(delta_time)
        x = 5
        if self.isShiftPressed:
           x = x * 2
        if self.isWPressed:
            self.player.y -= x
        if self.isAPressed:
            self.player.x -= x
        if self.isSPressed:
            self.player.y += x
        if self.isDPressed:
            self.player.x += x
        if self.isEscPressed:
            quit()


        print(self.bg.x, self.bg.y)




import game
import pygame
from Kancsalmate27megilyenek.TextureActors import *
from Kancsalmate27megilyenek.MapActor import *
from Kancsalmate27megilyenek.BackgroundActor import *
from Kancsalmate27megilyenek.MenuScreen import *
from Kancsalmate27megilyenek.MapActor import *
from Kancsalmate27megilyenek.PlayerActor import *
from game.simpleworld.ShapeType import ShapeType
from Kancsalmate27megilyenek.Labels import *
from Kancsalmate27megilyenek.ArenaScreen import *
from game.scene2d import MyBaseActor
from Kancsalmate27megilyenek.Map import *
class InStage(game.scene2d.MyStage):
    def __init__(self):
        super().__init__()
        self.player = PlayerActor()
        self.eletero : int = 100
        self.heart = HeartActor()
        self.heart1 = HeartActor()
        self.heart2 = HeartActor()
        self.add_actor(self.heart)
        self.add_actor(self.heart1)
        self.add_actor(self.heart2)
        self.hp = Label()
        self.add_actor(self.hp)
        self.player = PlayerActor()
        self.hp.set_text("HP:" + self.eletero.__str__())
        self.hp.x = 500
        self.hp.y = 500
        self.isWPressed : bool = False
        self.isAPressed : bool = False
        self.isSPressed : bool = False
        self.isDPressed : bool = False
        self.isEscPressed : bool = False
        self.isShiftPressed: bool = False
        self.hp : int = 100
        self.add_actor(self.player)
        self.player.set_z_index(1)
        self.set_on_key_down_listener(self.moveKeys)
        self.set_on_key_up_listener(self.moveKeysOff)
        self.camera.tracking = self.player

        self.map = Map(self,"butamap")



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

        b = 5
        if self.isShiftPressed:
           b = b * 2
        if self.isWPressed:
            self.player.y -= b
        if self.isAPressed:
            self.player.x -= b
        if self.isSPressed:
            self.player.y += b
        if self.isDPressed:
            self.player.x += b
        if self.isEscPressed:
            quit()
        if self.player.overlaps(self.sand):
            self.screen.game.set_screen(ArenaScreen())
            print("kocc")


        self.heart.x = self.player.x - 15
        self.heart.y = self.player.y - 30
        self.heart1.x = self.player.x + 10
        self.heart1.y = self.player.y - 30
        self.heart2.x = self.player.x + 35
        self.heart2.y = self.player.y - 30
        if self.eletero < 65:
            self.heart2.remove_from_stage()
        if self.eletero < 30:
            self.heart1.remove_from_stage()
        if self.eletero < 0:
            self.heart.remove_from_stage()


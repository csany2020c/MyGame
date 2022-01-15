import game
import pygame


from game.simpleworld.ShapeType import ShapeType
from Kancsalmate27megilyenek import MenuScreen
from Kancsalmate27megilyenek.TextureActors import *
from Kancsalmate27megilyenek.ArenaScreen import *
from Kancsalmate27megilyenek.Map import *
from game.scene2d import MyTickTimer
from spritesheetanim import SpriteStripAnim

class PlayerActor(game.scene2d.MyActor):
    def __init__(self, image_url: str = "Heroamijó_1.png"):
        super().__init__(image_url)
        self.leftImages:List['str'] = ("Heroamijó_1.png","Heroamijó_2.png","Heroamijó_3.png","Heroamijó_4.png","Heroamijó_5.png","Heroamijó_6.png","Heroamijó_7.png","Heroamijó_8.png")
        self.z_index = 1
        self.info = pygame.display.Info()
        self.width = self.info.current_w
        self.height = self.info.current_h
        self.set_size(64, 64)
        self.hitbox_scale_h = 1
        self.hitbox_scale_w = 1
        self.hitbox_shape = ShapeType.Rectangle
        self.isWPressed : bool = False
        self.isAPressed : bool = False
        self.isSPressed : bool = False
        self.isDPressed : bool = False
        self.set_on_key_down_listener(self.keyHandling)
        self.set_on_key_up_listener(self.keyhandlingOff)
        self.timer = MyTickTimer(func=self.timeHandling,interval=0.1,start_delay=0,repeat=True)
        self.add_timer(self.timer)


    def keyHandling(self,sender,event):
        if event.key == pygame.K_w:
            self.isWPressed = True
        if event.key == pygame.K_a:
            self.isAPressed = True
        if event.key == pygame.K_s:
            self.isSPressed = True
        if event.key == pygame.K_d:
            self.isDPressed = True
        if event.key == pygame.K_ESCAPE:
            self.stage.screen.game.set_screen(MenuScreen.MenuScreen3())


    def keyhandlingOff(self,sender,event):
        if event.key == pygame.K_w:
            self.isWPressed = False
            self.image_url = "Heroamijó_1.png"
        if event.key == pygame.K_a:
            self.isAPressed = False
            self.image_url = "Heroamijó_1.png"
        if event.key == pygame.K_s:
            self.isSPressed = False
            self.image_url = "Heroamijó_1.png"
        if event.key == pygame.K_d:
            self.isDPressed = False
            self.image_url = "Heroamijó_1.png"

    def timeHandling(self,sender):
        if self.isAPressed:
           if self.get_image_url() == self.leftImages[0]:
               self.image_url = self.leftImages[1]
           elif self.get_image_url() == self.leftImages[1]:
                self.image_url = self.leftImages[2]
           elif self.get_image_url() == self.leftImages[2]:
                self.image_url = self.leftImages[3]
           elif self.get_image_url() == self.leftImages[3]:
                self.image_url = self.leftImages[4]
           elif self.get_image_url() == self.leftImages[4]:
                self.image_url = self.leftImages[5]
           elif self.get_image_url() == self.leftImages[5]:
                self.image_url = self.leftImages[6]
           elif self.get_image_url() == self.leftImages[6]:
                self.image_url = self.leftImages[7]
           elif self.get_image_url() == self.leftImages[7]:
                self.image_url = self.leftImages[0]

    def act(self, delta_time: float):
        super().act(delta_time)
        b=5
        if self.isWPressed:
            self.y -= b
        if self.isAPressed:
            self.x -= b
        if self.isSPressed:
            self.y += b
        if self.isDPressed:
            self.x += b




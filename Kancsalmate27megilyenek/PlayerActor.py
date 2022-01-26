import game
import pygame


from game.simpleworld.ShapeType import ShapeType
from Kancsalmate27megilyenek import MenuScreen
from Kancsalmate27megilyenek.TextureActors import *
from Kancsalmate27megilyenek.ArenaScreen import *
from Kancsalmate27megilyenek.Map import *
from game.scene2d import MyTickTimer

class PlayerActor(game.scene2d.MyActor):
    def __init__(self, image_url: str = "Heroamijó_1.png"):
        super().__init__(image_url)
        self.leftImages: List['str'] = ("Heroamijó_1.png","Heroamijó_2.png","Heroamijó_3.png","Heroamijó_4.png","Heroamijó_5.png","Heroamijó_6.png","Heroamijó_7.png","Heroamijó_8.png")
        self.rightImages: List['str'] = ("Heroamijó_1_right.png", "Heroamijó_2_right.png", "Heroamijó_3_right.png", "Heroamijó_4_right.png", "Heroamijó_5_right.png","Heroamijó_6_right.png", "Heroamijó_7_right.png", "Heroamijó_8_right.png")
        self.z_index = 1
        self.info = pygame.display.Info()
        self.width = self.info.current_w
        self.height = self.info.current_h
        self.hp:int = 100
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
            self.isSPressed = False
        if event.key == pygame.K_a:
            self.isAPressed = True
            self.isDPressed = False
            self.image_url = "Heroamijó_1.png"
        if event.key == pygame.K_s:
            self.isSPressed = True
            self.isWPressed = False
        if event.key == pygame.K_d:
            self.isDPressed = True
            self.image_url = "Heroamijó_1_right.png"
            self.isAPressed = False
        if event.key == pygame.K_ESCAPE:
            self.stage.screen.game.set_screen(MenuScreen.MenuScreen3())



    def keyhandlingOff(self,sender,event):
        if event.key == pygame.K_w:
            self.isWPressed = False
            if self.isAPressed == True:
                self.image_url = "Heroamijó_1.png"
            else:
                self.image_url = "Heroamijó_1_right.png"
        if event.key == pygame.K_a:
            self.isAPressed = False
            if self.isDPressed == True:
                self.image_url = "Heroamijó_1_right.png"
            else:
                self.image_url = "Heroamijó_1.png"
        if event.key == pygame.K_s:
            self.isSPressed = False
            if self.isAPressed == True:
                self.image_url = "Heroamijó_1.png"
            else:
                self.image_url = "Heroamijó_1_right.png"
        if event.key == pygame.K_d:
            self.isDPressed = False
            if self.isAPressed == True:
                self.image_url = "Heroamijó_1.png"
            else:
                self.image_url = "Heroamijó_1_right.png"
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

        elif self.isDPressed:
           if self.get_image_url() == self.rightImages[0]:
               self.image_url = self.rightImages[1]
           elif self.get_image_url() == self.rightImages[1]:
                self.image_url = self.rightImages[2]
           elif self.get_image_url() == self.rightImages[2]:
                self.image_url = self.rightImages[3]
           elif self.get_image_url() == self.rightImages[3]:
                self.image_url = self.rightImages[4]
           elif self.get_image_url() == self.rightImages[4]:
                self.image_url = self.rightImages[5]
           elif self.get_image_url() == self.rightImages[5]:
                self.image_url = self.rightImages[6]
           elif self.get_image_url() == self.rightImages[6]:
                self.image_url = self.rightImages[7]
           elif self.get_image_url() == self.rightImages[7]:
                self.image_url = self.rightImages[0]

    def act(self, delta_time: float):
        super().act(delta_time)
        b = 5
        if self.isWPressed:
            self.y -= b
        if self.isAPressed:
            self.x -= b
        if self.isSPressed:
            self.y += b
        if self.isDPressed:
            self.x += b




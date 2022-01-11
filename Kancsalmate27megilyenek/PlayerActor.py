import game
import pygame
from game.simpleworld.ShapeType import ShapeType
from Kancsalmate27megilyenek import MenuScreen

class PlayerActor(game.scene2d.MyActor):
    def __init__(self, image_url: str = "Heroamijó_1.png"):
        super().__init__(image_url)
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
        if event.key == pygame.K_a:
            self.isAPressed = False
        if event.key == pygame.K_s:
            self.isSPressed = False
        if event.key == pygame.K_d:
            self.isDPressed = False

    def act(self, delta_time: float):
        super().act(delta_time)
        b=5
        if self.isWPressed:
            print("jó")
            self.y -= b
        if self.isAPressed:
            self.x -= b
        if self.isSPressed:
            self.y += b
        if self.isDPressed:
            self.x += b



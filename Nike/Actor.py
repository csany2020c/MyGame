import pygame
import game
import pygame
from game.simpleworld.ShapeType import ShapeType


class FatJordanAct(game.scene2d.MyActor):
    def __init__(self):
        super().__init__("images/fatjordanact.png")
        self.set_on_key_press_listener(self.key_down)
        self.set_size(200, 100)
        self.hitbox_scale_h = 0.9
        self.hitbox_scale_w = 0.9

        # self.hitbox_shape = ShapeType.Rectangle

    def key_down(self, sender, event):
        print(sender)
        print(event)
        if event.key == pygame.K_d:
            self.x += 4
        if event.key == pygame.K_w:
            self.y -= 4
        if event.key == pygame.K_a:
            self.x -= 4
        if event.key == pygame.K_s:
            self.y += 4


class MenuJordan(game.scene2d.MyActor):
    def __init__(self):
        super().__init__("images/fatjordanact.png")
        self.y = 350
        self.x = 500

class StoneAct(game.scene2d.MyActor):
    def __init__(self):
        super().__init__("images/Stone.jpg")
        self.set_size(65, 65)

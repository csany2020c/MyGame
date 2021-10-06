import game
import pygame
from game.simpleworld.ShapeType import ShapeType

class PlayerActor(game.scene2d.MyActor):
    def __init__(self, image_url: str = "../map/terkep.png"):
        super().__init__(image_url)
        self.info = pygame.display.Info()
        self.width = self.info.current_w
        self.height = self.info.current_h
        self.set_size(50, 50)
        self.hitbox_scale_h = 1
        self.hitbox_scale_w = 1
        self.hitbox_shape = ShapeType.Rectangle

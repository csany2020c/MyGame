import pygame
import game
import pygame
from game.simpleworld.ShapeType import ShapeType

class fohos(game.scene2d.MyActor):
    def __init__(self):
        super().__init__("Images/legokatona.png")
        self.set_on_key_press_listener(self.key_down)
        self.set_size(200, 100)
        self.hitbox_scale_h = 0.9
        self.hitbox_scale_w = 0.9
        self.hitbox_shape = ShapeType.Rectangle

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

class enemy1(game.scene2d.MyActor):
    def __init__(self):
        super().__init__("Images/katona.png")

class horthy (game.scene2d.MyActor):
    def __init__(self):
        super().__init__("Images/horthy.png")

class enemy2 (game.scene2d.MyActor):
    def __init__(self):
        super().__init__("Images/bumsteve.png")

    def act(self, delta_time: float):
        super().act(delta_time)
        self.x += delta_time * 100

class map(game.scene2d.MyActor):
    def __init__(self):
        super().__init__("Images/map.jpg")

class kapu(game.scene2d.MyActor):
    def __init__(self):
        super().__init__("Images/kkapu.png")
        self.hitbox_scale_h = 0.9
        self.hitbox_scale_w = 0.9
        # self.hitbox_shape = ShapeType.Rectangle
import pygame
import game
import pygame
from game.simpleworld.ShapeType import ShapeType

class bruhActor(game.scene2d.MyActor):
    def __init__(self):
        super().__init__("Images/legokatona.png")

        self.hitbox_shape = ShapeType.Circle

        def key_down(sender, event):
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

        self.set_on_key_press_listener(key_down)
        self.set_size(200, 100)
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
        super().__init__("Images/horthy.png")
        self.x = 1000
        self.y =400
        self.hitbox_shape = ShapeType.Circle
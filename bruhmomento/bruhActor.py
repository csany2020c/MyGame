import pygame
import game
import pygame
from game.simpleworld.ShapeType import ShapeType

class lovedek(game.scene2d.MyActor):


    def act(self, delta_time: float):
        super().act(delta_time)
        if self.irany == 1:
            self.x += 1000*delta_time
        elif self.irany == 2:
            self.x -= 1000*delta_time
        if self.irany == 3:
            self.y += 1000*delta_time
        elif self.irany == 4:
            self.y -= 1000*delta_time
        self.distance += 1000*delta_time

        if self.distance > 1000:
            self.remove_from_stage()
    def __init__(self, irany: int):
        super().__init__("Images/lovedek.png")
        self.irany = irany
        self.distance = 0
        self.set_size(40, 40)

        self.hitbox_scale_h = 0.9
        self.hitbox_scale_w = 0.9
        # self.set_on_key_press_listener(self.key_down)
    # def key_down(self, sender, event):
    #     print(event)
    #     print(sender)
    #     if event.key == pygame.K_LEFT:
    #         self.x -= 150
    #     if event.key == pygame.K_RIGHT:
    #         self.x += 150




class fohos(game.scene2d.MyActor):
    def __init__(self):
        super().__init__("Images/legokatona.png")
        # self.set_on_key_press_listener(self.key_down)
        self.set_size(200, 100)
        self.hitbox_scale_h = 0.9
        self.hitbox_scale_w = 0.9

        #self.hitbox_shape = ShapeType.Rectangle
    #
    # def key_down(self, sender, event):
    #     print(sender)
    #     print(event)
    #     if event.key == pygame.K_d:
    #         self.x += 4
    #     if event.key == pygame.K_w:
    #         self.y -= 4
    #     if event.key == pygame.K_a:
    #         self.x -= 4
    #     if event.key == pygame.K_s:
    #         self.y += 4

class enemy1(game.scene2d.MyActor):
    def __init__(self):
        super().__init__("Images/katona.png")


class horthy (game.scene2d.MyActor):
    def __init__(self):
        super().__init__("Images/horthy.png")

class enemy2 (game.scene2d.MyActor):
    def __init__(self):
        super().__init__("Images/bumsteve.png")
        self.rotate_with(180)

#class map(game.scene2d.MyActor):
    #def __init__(self):
        #super().__init__("Images/palya.png")
        #self.set_width(1200)
        #self.y -= 100


class kapu(game.scene2d.MyActor):
    def __init__(self):
        super().__init__("Images/kkapu.png")
        self.hitbox_scale_h = 0.9
        self.hitbox_scale_w = 0.9
        self.hitbox_shape = ShapeType.Rectangle

class wall(game.scene2d.MyActor):
    def __init__(self):
        super().__init__("Images/fal.jpg")
        self.set_size(65, 65)

class startgomb(game.scene2d.MyActor):
    def __init__(self):
        super().__init__("Images/lessgo2.png")

class wall2(game.scene2d.MyActor):
    def __init__(self):
        super().__init__("Images/gedvasfal.png")
        self.set_size(65, 65)

class kulcs(game.scene2d.MyActor):
    def __init__(self):
        super().__init__("Images/kulcs.png")
        self.set_size(150,150)

class zartajto(game.scene2d.MyActor):
    def __init__(self):
        super().__init__("Images/oszlop.png")
        self.set_size(100, 200)

class eastereggtabla(game.scene2d.MyActor):
    def __init__(self):
        super().__init__("Images/tabla.png")

class easteregg(game.scene2d.MyActor):
    def __init__(self):
        super().__init__("Images/ffpog.png")
        self.set_size(150, 150)
class csakany(game.scene2d.MyActor):
    def __init__(self):
        super().__init__("Images/csakany.png")
        self.set_size(150, 150)

class quit(game.scene2d.MyActor):
    def __init__(self):
        super().__init__("Images/quit.png")
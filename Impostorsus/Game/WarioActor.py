import game
import pygame
from game.simpleworld.ShapeType import ShapeType


class WarioActor(game.scene2d.MyActor):

    def __init__(self):
        super().__init__("Kepek/actorsusus.png")
        self.jump: float = 0
        self.go = True
        self.set_width(64)
        self.hitbox_scale_h = 1.030
        self.hitbox_scale_w = 0.9
        self.hitbox_shape = ShapeType.Rectangle

    def act(self, delta_time: float):
        super().act(delta_time)

        if self.jump > 0:
            self.y -= 450 * delta_time
            self.jump -= 450 * delta_time
            #if self.elapsed_time > 5:
                #self.jump = True

        else:
            if self.go:
                self.y += 6

        # self.stage.camera.x = self.x
        # self.stage.camera.y = self.y


    def ugras(self):
        self.jump = 220

        if self.go > 0:
            self.jump = False

    def start(self):
        self.go = True

    def stop(self):
        self.go = False
class GroundActor(game.scene2d.MyActor):
    def __init__(self):
        super().__init__("Kepek/foldriosus.png")
        self.set_width(200)
        # self.hitbox_scale_h = 0.9
        #self.hitbox_scale_w = 0.2
        self.hitbox_shape = ShapeType.Rectangle

class SecretGroundActor(game.scene2d.MyActor):
    def __init__(self):
        super().__init__("Kepek/foldriosus.png")
        self.set_width(200)
        # self.hitbox_scale_h = 0.9
        #self.hitbox_scale_w = 0.2
        self.hitbox_shape = ShapeType.Rectangle


class HatterActor1(game.scene2d.MyActor):
    def __init__(self):
        super().__init__("Kepek/hattersus.png")
        self.y -= 100
        self.set_width(1300)

class EnemyActor(game.scene2d.MyActor):
    def __init__(self):
        super().__init__("Kepek/Enemysus.png")

class InvisActor(game.scene2d.MyActor):
    def __init__(self):
        super().__init__("Kepek/halal.png")
        self.hitbox_scale_h = 0.2
        self.hitbox_shape = ShapeType.Rectangle

class Question(game.scene2d.MyActor):
    def __init__(self):
        super().__init__("Kepek/kerdosus.png")
        self.hitbox_shape = ShapeType.Rectangle
        self.set_width(100)

class Kocka(game.scene2d.MyActor):
    def __init__(self):
        super().__init__("Kepek/kockasus.png")
        self.set_height(64)
        self.set_width(64)
        self.hitbox_shape = ShapeType.Rectangle

class Gomb(game.scene2d.MyActor):
    def __init__(self):
        super().__init__("Kepek/Wario.png")
        self.set_height(64)
        self.set_width(64)


class Gemba(game.scene2d.MyActor):
    def __init__(self):
        super().__init__("Kepek/gembasus.png")
        self.set_size(80, 80)
        self.go = True
        self.hitbox_scale_h = 0.7
        self.hitbox_shape = ShapeType.Rectangle

    def act(self, delta_time: float):
        super().act(delta_time)
        self.jump: float = 0
        self.x += 4

        if self.jump > 0:
            self.y -= 450 * delta_time
            self.jump -= 450 * delta_time
        # if self.elapsed_time > 5:
        # self.jump = True

        else:
            if self.go:
                self.y += 6

    def ugras(self):
        self.jump = 210


    def start(self):
        self.go = True


    def stop(self):
        self.go = False

class MenuSzoveg(game.scene2d.MyLabel):

    def __init__(self, string: str = "MyText") -> None:
            game.scene2d.MyLabel.__init__(self, string=string, font_name="arial")

class Play(game.scene2d.MyActor):
    def __init__(self):
        super().__init__("Kepek/Playbutton.png")
        self.set_height(150)
        self.set_width(150)

class SuperWario(game.scene2d.MyActor):
    def __init__(self):
        super().__init__("Kepek/SuperWario.png")
        self.set_height(550)
        self.set_width(550)

class BackGround(game.scene2d.MyActor):
    def __init__(self):
        super().__init__("Kepek/BackGround.png")
        self.set_width(1300)

class Exit(game.scene2d.MyActor):
    def __init__(self):
        super().__init__("Kepek/ExitButton.png")
        self.set_height(150)
        self.set_width(150)

class FullScreen(game.scene2d.MyActor):
    def __init__(self):
        super().__init__("Kepek/Fullscreen.png")
        self.set_height(375)
        self.set_width(375)

class Credit(game.scene2d.MyActor):
    def __init__(self):
        super().__init__("Kepek/Credit.png")
        self.set_height(225)
        self.set_width(225)

class Bindings(game.scene2d.MyActor):
    def __init__(self):
        super().__init__("Kepek/bindings.png")
        self.set_height(275)
        self.set_width(275)

class Halalkep(game.scene2d.MyActor):
    def __init__(self):
        super().__init__("Kepek/halalkep.png")
        self.set_height(450)
        self.set_width(450)









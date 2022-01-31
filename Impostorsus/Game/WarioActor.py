import game
import pygame
from game.simpleworld.ShapeType import ShapeType
from game.scene2d import MyTickTimer


class WarioActor(game.scene2d.MyActor):

    def __init__(self):
        super().__init__("Kepek/actorsusus.png")
        self.jump: float = 0
        self.go = True
        self.set_width(64)
        self.hitbox_scale_h = 1.030
        self.hitbox_scale_w = 1
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

class Ground2Actor(game.scene2d.MyActor):
    def __init__(self):
        super().__init__("Kepek/foldsus.png")
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
        self.set_width(1)

class CannonActor(game.scene2d.MyActor):
    def __init__(self):
        super().__init__("Kepek/cannon.png")
        self.hitbox_scale_h = 0.58
        self.hitbox_scale_w = 1


class BillActor(game.scene2d.MyActor):
    def __init__(self):
        super().__init__("Kepek/bill.png")
        self.hitbox_scale_h = 0.35
        self.hitbox_scale_w = 1.2

    def act(self, delta_time: float):
        super().act(delta_time)
        self.x -= 400 * delta_time

class EnemyActor(game.scene2d.MyActor):
    def __init__(self):
        super().__init__("Kepek/Enemysus.png")

#class BossActor(game.scene2d.MyActor):
    #def __init__(self):
        #super().__init__("Kepek/gael.gif")
        #self.set_width(20)
        #self.set_height(20)

class InvisActor(game.scene2d.MyActor):
    def __init__(self):
        super().__init__("Kepek/halal.png")
        self.hitbox_scale_h = 0.2
        self.hitbox_shape = ShapeType.Rectangle

class Question(game.scene2d.MyActor):
    def __init__(self):
        super().__init__("Kepek/kerdosus.png")
        self.hitbox_shape = ShapeType.Rectangle
        self.set_width(80)

class Kocka(game.scene2d.MyActor):
    def __init__(self):
        super().__init__("Kepek/kockasus.png")
        self.set_height(64)
        self.set_width(64)
        self.hitbox_shape = ShapeType.Rectangle


class KockaHalf(game.scene2d.MyActor):
    def __init__(self):
        super().__init__("Kepek/kockahalf.png")
        self.set_height(64)
        self.set_width(64)
        self.hitbox_shape = ShapeType.Rectangle

    def tikk(self, sender, delta_time: float):
        self.x -= 40 * delta_time



    def act(self, delta_time: float):
        super().act(delta_time)
        if self.elapsed_time > 0:
            self.x += 80 * delta_time
        if self.elapsed_time > 7:
            self.x -= 160 * delta_time
        if self.elapsed_time > 14:
            self.x += 160 * delta_time
        if self.elapsed_time > 21:
            self.x -= 160 * delta_time
        if self.elapsed_time > 28:
            self.x += 160 * delta_time
        if self.elapsed_time > 31.5:
            self.x -= 80 * delta_time


class Kockasl(game.scene2d.MyActor):
    def __init__(self):
        super().__init__("Kepek/slimekockasus.png")
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
        self.jump = 240


    def start(self):
        self.go = True


    def stop(self):
        self.go = False

class MenuSzoveg(game.scene2d.MyLabel):

    def __init__(self, string: str = "MyText") -> None:
            game.scene2d.MyLabel.__init__(self, string=string, font_name="8-BIT WONDER.TTF")

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

class Road(game.scene2d.MyActor):
    def __init__(self):
        super().__init__("Kepek/road.jpg")
        self.set_width(1280)

    def act(self, delta_time: float):
        super().act(delta_time)
        if self.elapsed_time > 3:
            self.y -= 60 * delta_time

class Finish(game.scene2d.MyActor):
    def __init__(self):
        super().__init__("Kepek/finish.png")
        self.set_width(1050)
        self.hitbox_scale_h = 0.1
        self.hitbox_scale_w = 1.5
    def act(self, delta_time: float):
        super().act(delta_time)
        if self.elapsed_time > 3:
            self.y -= 60 * delta_time

class KartEnemy(game.scene2d.MyActor):
    def __init__(self):
        super().__init__("Kepek/cactus.png")
        self.set_width(100)
        self.hitbox_scale_h = 0.9
        self.hitbox_scale_w = 0.6

class WarioKart(game.scene2d.MyActor):
    def __init__(self):
        super().__init__("Kepek/wariokart.png")

    def act(self, delta_time: float):
        super().act(delta_time)
        if self.elapsed_time > 3:
            self.y += 200 * delta_time

class WarioKartSkin(game.scene2d.MyActor):
    def __init__(self):
        super().__init__("Kepek/wariokart.png")

class MarioKartSkin(game.scene2d.MyActor):
    def __init__(self):
        super().__init__("Kepek/mariokart.png")

class TodKartSkin(game.scene2d.MyActor):
    def __init__(self):
        super().__init__("Kepek/todkart.png")

class DonkeyKartSkin(game.scene2d.MyActor):
    def __init__(self):
        super().__init__("Kepek/donkeykart.png")

class LuigiKartSkin(game.scene2d.MyActor):
    def __init__(self):
        super().__init__("Kepek/luigikart.png")

class Barrel(game.scene2d.MyActor):
    def __init__(self):
        super().__init__("Kepek/barrel.png")
        self.set_width(120)
        self.hitbox_scale_h = 1
        self.hitbox_scale_w = 0.6

class Blue(game.scene2d.MyActor):
    def __init__(self):
        super().__init__("Kepek/blue.png")
        self.set_width(1300)


class LathatatlanKart(game.scene2d.MyActor):
    def __init__(self):
        super().__init__("Kepek/Lathatatlan.png")
        self.set_width(80)
        self.hitbox_scale_h = 2
        self.hitbox_scale_w = 2

    def act(self, delta_time: float):
        super().act(delta_time)
        if self.elapsed_time > 3:
            self.y += 200 * delta_time

class LathatatlanKart2(game.scene2d.MyActor):
    def __init__(self):
        super().__init__("Kepek/Lathatatlan.png")
        self.set_width(80)
        self.hitbox_scale_h = 2
        self.hitbox_scale_w = 2

    def act(self, delta_time: float):
        super().act(delta_time)
        if self.elapsed_time > 3:
            self.y += 200 * delta_time
class LathatatlanKart3(game.scene2d.MyActor):
    def __init__(self):
        super().__init__("Kepek/Lathatatlan.png")
        self.set_width(1)

class Ramp(game.scene2d.MyActor):
    def __init__(self):
        super().__init__("Kepek/ramp.png")
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

class Pipe(game.scene2d.MyActor):
    def __init__(self):
        super().__init__("Kepek/pipe.png")
        self.set_height(375)
        self.set_width(375)
        self.hitbox_scale_h = 0.6
        self.hitbox_scale_w = 0.3

class Pipe1(game.scene2d.MyActor):
    def __init__(self):
        super().__init__("Kepek/pipe.png")
        self.set_height(375)
        self.set_width(375)
        self.hitbox_scale_h = 0.6
        self.hitbox_scale_w = 0.3


class Cloud(game.scene2d.MyActor):
    def __init__(self):
        super().__init__("Kepek/cloud.png")
        self.set_height(75)
        self.set_width(75)

    def act(self, delta_time: float):
        super().act(delta_time)
        if self.elapsed_time > 0:
            self.x += 20 * delta_time

class Cloud3(game.scene2d.MyActor):
    def __init__(self):
        super().__init__("Kepek/cloud3.png")
        self.set_height(150)
        self.set_width(150)

    def act(self, delta_time: float):
        super().act(delta_time)
        if self.elapsed_time > 0:
            self.x += 20 * delta_time

class Ladder(game.scene2d.MyActor):
    def __init__(self):
        super().__init__("Kepek/ladder.png")
        self.set_width(180)
        self.hitbox_scale_w = 0.3

class Keret(game.scene2d.MyActor):
    def __init__(self):
        super().__init__("Kepek/keret.png")
        self.set_width(400)

class Keret2(game.scene2d.MyActor):
    def __init__(self):
        super().__init__("Kepek/keret2.png")

class BackGround2(game.scene2d.MyActor):
    def __init__(self):
        super().__init__("Kepek/kartmenukep.png")

class Map1(game.scene2d.MyActor):
    def __init__(self):
        super().__init__("Kepek/map1.png")
        self.set_width(330)

class Map2(game.scene2d.MyActor):
    def __init__(self):
        super().__init__("Kepek/map2.png")
        self.set_width(290)

class Pause(game.scene2d.MyActor):
    def __init__(self):
        super().__init__("Kepek/musicpause.png")
        self.set_height(45)
        self.set_width(45)

class Start(game.scene2d.MyActor):
    def __init__(self):
        super().__init__("Kepek/musicstart.png")
        self.set_height(44)
        self.set_width(44)

class Next(game.scene2d.MyActor):
    def __init__(self):
        super().__init__("Kepek/musicnext.png")
        self.set_height(45)
        self.set_width(45)

class Last(game.scene2d.MyActor):
    def __init__(self):
        super().__init__("Kepek/musiclast.png")
        self.set_height(42)
        self.set_width(42)

class KunuM(game.scene2d.MyActor):
    def __init__(self):
        super().__init__("Kepek/mario.png")
        self.set_height(200)
        self.set_width(200)
        self.hitbox_scale_h = 0.9
        self.hitbox_scale_w = 0.5

    def act(self, delta_time: float):
        super().act(delta_time)

        if self.elapsed_time > 0:
            self.y -= delta_time * 250

class Web(game.scene2d.MyActor):
    def __init__(self):
        super().__init__("Kepek/websitei.png")
        self.set_height(275)
        self.set_width(275)

class Halalkep(game.scene2d.MyActor):
    def __init__(self):
        super().__init__("Kepek/halalkep.png")
        self.set_height(450)
        self.set_width(450)

class Lathatatlan(game.scene2d.MyActor):
    def __init__(self):
        super().__init__("Kepek/Lathatatlan.png")
        self.set_height(64)
        self.set_width(64)
        self.hitbox_scale_h = 0.1
        self.hitbox_scale_w = 1

class Lathatatlan2(game.scene2d.MyActor):
    def __init__(self):
        super().__init__("Kepek/Lathatatlan.png")
        self.set_height(64)
        self.set_width(64)
        self.hitbox_scale_h = 0.1
        self.hitbox_scale_w = 1

class Lathatatlan3(game.scene2d.MyActor):
    def __init__(self):
        super().__init__("Kepek/Lathatatlan.png")
        self.set_height(1)
        self.set_width(200)
        self.hitbox_scale_h = 0.8
        self.hitbox_scale_w = 1.1

class Lathatatlan4(game.scene2d.MyActor):
    def __init__(self):
        super().__init__("Kepek/Lathatatlan.png")
        self.set_height(1)
        self.set_width(200)
        self.hitbox_scale_h = 0.8
        self.hitbox_scale_w = 1.1

class Tabla(game.scene2d.MyActor):
    def __init__(self):
        super().__init__("Kepek/Tabla.png")
        self.set_height(100)
        self.set_width(100)


class Zaszlo(game.scene2d.MyActor):
    def __init__(self):
        super().__init__("Kepek/zaszlo.png")
        self.set_height(250)
        self.set_width(250)
        self.hitbox_scale_h = 2
        self.hitbox_scale_w = 0.4

class Zaszlo2(game.scene2d.MyActor):
    def __init__(self):
        super().__init__("Kepek/zaszlo.png")
        self.set_width(175)
        self.hitbox_scale_h = 1
        self.hitbox_scale_w = 0.2

class Winkep(game.scene2d.MyActor):
    def __init__(self):
        super().__init__("Kepek/win.png")
        self.set_height(450)
        self.set_width(450)

class Skin(game.scene2d.MyActor):
    def __init__(self):
        super().__init__("Kepek/skin.png")
        self.set_height(150)
        self.set_width(150)











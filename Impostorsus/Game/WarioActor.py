import game
from game.simpleworld.ShapeType import ShapeType


class WarioActor(game.scene2d.MyActor):

    def __init__(self):
        super().__init__("Kepek/actorsusus.png")
        self.jump: float = 0
        self.go = True
        self.set_width(100)
        self.hitbox_scale_h = 0.9
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





    def ugras(self):
        self.jump = 210

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


class HatterActor1(game.scene2d.MyActor):
    def __init__(self):
        super().__init__("Kepek/hattersus.png")
        self.y -= 100
        self.set_width(1300)


class Question(game.scene2d.MyActor):
    def __init__(self):
        super().__init__("Kepek/kerdosus.png")
        self.hitbox_shape = ShapeType.Rectangle

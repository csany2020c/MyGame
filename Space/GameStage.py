import game
from EnemyActor import *
from Arial32 import *


class GameStage(game.scene2d.MyStage):

    def __init__(self):
        super().__init__()
        self.b = Enemy1Actor()
        self.add_actor(self.b)
        for j in range(0, 10):
            for i in range(0, 10):
                e = Enemy1Actor()
                e.y = i * 40
                e.x = j * 40
                e.width = 20
                e.height = 20
                self.add_actor(e)
#                e.set_on_key_up_listener(self.click)
        self.b.z = 3000
        self.a = Arial32()
        self.a.hitbox_shape = game.simpleworld.ShapeType.Circle
        self.add_actor(self.a)
        self.a.set_text("asd")
        self.a.set_bg_red(0)
        self.a.set_font_underline(True)
        self.a.set_alpha(128)
        self.add_actor(game.scene2d.MyLabel("ASD"))
        self.asd = game.scene2d.MyActor("resources/images/enemy1.png")
        self.asd.x = 200
        self.asd.w = 200
        self.asd.hitbox_scale_w = 0.4
        self.asd.hitbox_scale_h = 0.4
        self.asd.hitbox_shape = game.simpleworld.ShapeType.Circle
        self.add_actor(self.asd)

    def act(self, delta_time: float):
        super().act(delta_time)
        #self.actors[20].width = 200
        #self.b.r -= 2
        # print(self.asd.overlaps(self.a))





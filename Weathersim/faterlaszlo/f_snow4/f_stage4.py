import game
import random
from Weathersim.faterlaszlo.Arial import *
from Weathersim.faterlaszlo.f_actors import *

class f_stage4(game.scene2d.MyStage):
    def __init__(self):
        super().__init__()
        self.bg = bg_actor_s()
        self.felho = felhos_actor()
        self.add_actor(self.bg)
        self.add_actor(self.felho)
        self.felho.z_index = 0

        self.t = Arial()
        self.add_actor(self.t)
        self.t.set_text("Vissza_n")
        self.t.set_color(1, 1, 1)
        self.t.x = 0
        self.t.y = 0

        self.snowman = snowman()
        self.add_actor(self.snowman)
        self.snowman.h = 200
        self.snowman.x = 500
        self.snowman.y = 500

        for i in range(24):
            self.havazik = havazas()
            self.add_actor(self.havazik)
            self.havazik.h = 20
            self.havazik.w = 45
            self.havazik.x = random.Random().randint(0, game.scene2d.MyGame.get_screen_width() - self.havazik.w)
            self.havazik.y = random.Random().randint(0, game.scene2d.MyGame.get_screen_height() - self.havazik.h)

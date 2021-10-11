import game
from game.scene2d.MyScreen import *
import random

class Screen(game.scene2d.MyScreen):

    def __init__(self):
        super().__init__()
        self.add_stage(GameStage())


class hatter(game.scene2d.MyActor):

    def __init__(self):
        self.hatter = super().__init__('../!_resources/images/cloudy.png')


class taj(game.scene2d.MyActor):

    def __init__(self):
        self.tajocska = super().__init__('havas_landscape.png')


class ho(game.scene2d.MyActor):

    def __init__(self):
        self.ho = super().__init__('../!_resources/images/snow.png')

    def act(self, delta_time: float):
        super().act(delta_time)
        self.y += delta_time * 100
        if self.y > 640:
            self.y = -50

class eso(game.scene2d.MyActor):

    def __init__(self):
        self.eso = super().__init__('../!_resources/images/rain.png')

    def act(self, delta_time: float):
        super().act(delta_time)
        self.y += delta_time * 150
        if self.y > 640:
            self.y = -50


class GameStage(game.scene2d.MyStage):

    def __init__(self):
        super().__init__()
        self.hatter = hatter()
        self.hatter.width = 1280
        self.hatter.height = 720
        self.taj = taj()
        self.taj.width = 1280
        self.taj.height = 720
        self.taj.set_on_key_down_listener(self.key_down)
        for i in range(60):
            self.ho = ho()
            self.ho.width = 32
            self.ho.height = 32
            self.ho.x = random.randint(a=0, b=1200)
            self.ho.y = random.randint(a=0, b=640)
            self.add_actor(self.ho)
        for i in range(60):
            self.eso = eso()
            self.eso.width = 32
            self.eso.height = 32
            self.eso.x = random.randint(a=0, b=1200)
            self.eso.y = random.randint(a=0, b=640)
            self.add_actor(self.eso)
        self.add_actor(self.hatter)
        self.add_actor(self.taj)

    def key_down(self, sender, event):
        if event.key == pygame.K_ESCAPE:
            quit()


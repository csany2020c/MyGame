import game
from Weathersim.marcontamas.Actorok import *
from Weathersim.marcontamas.IdojarasLabel import *

class MenuStage(game.scene2d.MyStage):
    def __init__(self):
        super().__init__()
        self.bg = MenuHatter()
        self.label = IdojarasLabel()
        self.add_actor(self.label)
        self.add_actor(self.bg)
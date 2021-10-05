import game
from Weathersim.KeleLorand.Actorok import *

class Stage(game.scene2d.MyStage):
    def __init__(self):
        hatter = CloudyActor()
        self.add_actor(hatter)
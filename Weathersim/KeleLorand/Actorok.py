import game
from Weathersim.KeleLorand import *

class CloudyActor(game.scene2d.MyActor):
    def __init__(self, image_url = ""):
        super().__init__("cloudy.png")
        self.set_width(300)
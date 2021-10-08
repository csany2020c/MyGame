from Weathersim.NemethCsongor.blizzard import *
from Weathersim.NemethCsongor.snow import *
from Weathersim.NemethCsongor.rain import *
from Weathersim.NemethCsongor.sun import *
import game


class Game(game.scene2d.MyGame):
    def __init__(self):
        super().__init__()
        self.screen = Screen()
        self.run()


Game().run()

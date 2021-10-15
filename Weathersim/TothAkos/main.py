from Weathersim.TothAkos.screen import *
from Weathersim.TothAkos.stage import *
class Main(game.scene2d.MyGame):

    def __init__(self):
        super().__init__()
        self.screen = Sunnyscr()

Main().run()
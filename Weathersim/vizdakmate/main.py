from Weathersim.vizdakmate.screen import *

class Main(game.scene2d.MyGame):

    def __init__(self):
        super().__init__()
        self.screen = Screen()

Main().run()
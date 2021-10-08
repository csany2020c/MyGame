from Weathersim.TothAkos.screen import *
import game

class Main(game.scene2d.MyGame):

    def __init__(self):
        super().__init__()
        self.screen = Sunnyscr()
        #self.screen = Snowyscr()
        #self.screen = Rainyscr()



Main().run()
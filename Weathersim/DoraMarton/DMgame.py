import game
from Weathersim.DoraMarton.DMscreen import *

class main(game.scene2d.MyGame):

    def __init__(self):
        super().__init__()
        self.screen = sunnyscreen()
        self.run()

main()

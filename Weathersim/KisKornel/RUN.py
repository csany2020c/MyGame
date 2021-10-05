from Weathersim.KisKornel.Screen import *
import game



class RUN(game.scene2d.MyGame):

    def __init__(self):
        super().__init__()
        self.screen = SunnyScreen()



RUN().run()
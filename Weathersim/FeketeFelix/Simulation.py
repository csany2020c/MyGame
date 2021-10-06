import game
from Weathersim.FeketeFelix.Kepernyok import *

class Sim(game.scene2d.MyGame):

    def __init__(self, width: int = 1280, height: int = 720):
        super().__init__(width, height)
        self.screen = SunnyScreen()

        def key_down(sender, event):
            print(sender)
            print(event)
            if event.key == pygame.K_ESCAPE:
                self.exit()


        self.set_on_key_press_listener(key_down)






Sim().run()
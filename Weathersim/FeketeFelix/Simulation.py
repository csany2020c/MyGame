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

            if event.key == pygame.K_q:
                self.screen = RainScreen()

            if event.key == pygame.K_w:
                self.screen = SnowScreen()

            if event.key == pygame.K_e:
                self.screen = SnowRainScreen()

            if event.key == pygame.K_r:
                self.screen = SunnyScreen()




        self.set_on_key_press_listener(key_down)






Sim().run()
import game

from Weathersim.DoraMarton.DMscreen import *

class main(game.scene2d.MyGame):

    def __init__(self, width: int = 1280, height: int = 720, autorun: bool = False, autosize: bool = False):
        super().__init__(width, height, autorun, autosize)
        def key_down(sender, event):
            print(sender)
            print(event)
            if event.key == pygame.K_1:
                self.screen = Sunnyscreen()
            if event.key == pygame.K_2:
                self.screen = Rainyscreen()
            if event.key == pygame.K_3:
                self.screen = Snowyscreen()
            if event.key == pygame.K_4:
                self.screen = snowyrainyscreen()
            if event.key == pygame.K_0:
                self.screen = Menuscreen()
            if event.key == pygame.K_ESCAPE:
                self.exit()

        self.set_on_key_down_listener(key_down)
        self.screen = Menuscreen()
        self.run()
main()

import game

from Weathersim.DoraMarton.DMscreen import *

class main(game.scene2d.MyGame):

    def __init__(self):
        super().__init__()
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
            if event.key == pygame.K_ESCAPE:
                self.screen = Menuscreen()
        self.set_on_key_down_listener(key_down)
        self.screen = Menuscreen()
        self.run()
main()

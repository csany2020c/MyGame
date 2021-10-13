from Weathersim.horvathboldizsar.GameScreen import *
from Weathersim.horvathboldizsar.MenuScreen import *


class Simulator(game.scene2d.MyGame):

    def __init__(self, width: int = 1280, height: int = 720):
        super().__init__(width, height)
        self.screen = MenuScreen()

        def key_down(sender, event):

            if event.key == pygame.K_ESCAPE:
                print("Exit! Viszlát :(")
                quit()

            if event.key == pygame.K_0:
                self.screen = MenuScreen()
                print("Menü Screen")

            if event.key == pygame.K_1:
                self.screen = NaposScreen()
                print("Napos Screen")

            if event.key == pygame.K_2:
                self.screen = EsosScreen()
                print("Esős Screen")

            if event.key == pygame.K_3:
                self.screen = HavasesoScreen()
                print("Havasesős Screen")

            if event.key == pygame.K_4:
                self.screen = HavasScreen()
                print("Havas Screen")

        self.set_on_key_press_listener(key_down)


Simulator().run()

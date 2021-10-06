import game
from game.scene2d import *
from Weathersim.KeleLorand.Game import *

class MyLabel(game.scene2d.MyLabel):
    def __init__(self, string: str = "Play", font_size: int = 64):
        super().__init__("Play")

        self.set_on_mouse_down_listener(self.tesztklik)

    def tesztklik(self, sender, event):
        self.screen.game.set_screen(GameScreen)


class HatterMenuAct(game.scene2d.MyActor):
    def __init__(self):
        super().__init__("!_resources/images/landscape.png")


class NaposMenuAct(game.scene2d.MyActor):
    def __init__(self):
        super().__init__("!_resources/images/sunny.png")


class GameMenuStage(game.scene2d.MyStage):
    def __init__(self):
        super().__init__()

        self.mylabel = MyLabel()

        self.hatter_bg_menu = HatterMenuAct()
        self.napos_bg_menu = NaposMenuAct()
        self.nap_bg_menu = NapMenuAct()


        self.hatter_bg_menu.z_index = 6
        self.napos_bg_menu.z_index = 4
        self.nap_bg_menu.z_index = 5



        self.nap_bg_menu.x = 900
        self.nap_bg_menu.y = -100

        self.add_actor(self.mylabel)
        self.add_actor(self.hatter_bg_menu)
        self.add_actor(self.napos_bg_menu)
        self.add_actor(self.nap_bg_menu)


class NapMenuAct(game.scene2d.MyActor):
    def __init__(self):
        super().__init__("!_resources/images/sun.png")





class GameMenuScreen(game.scene2d.MyScreen):
    def __init__(self):
        super().__init__()
        self.add_stage(GameMenuStage())


class GameMenuSelf(game.scene2d.MyGame):
    def __init__(self, width: int = 1280, height: int = 720, autorun: bool = False):
        super().__init__(width, height, autorun)
        self.screen = GameMenuScreen()

        self.set_on_key_down_listener(self.teszt)

    def teszt(self, sender, event):
        if event.key == pygame.K_ESCAPE:
            exit()



GameMenuSelf().run()
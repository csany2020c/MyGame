import game
from game.scene2d import *
from game.scene2d.MyScreen import *

class HatterAct(game.scene2d.MyActor):
    def __init__(self):
        super().__init__("!_resources/images/landscape.png")

class NaposAct(game.scene2d.MyActor):
    def __init__(self):
        super().__init__("!_resources/images/sunny.png")

class NapAct(game.scene2d.MyActor):
    def __init__(self):
        super().__init__("!_resources/images/sun.png")
        self.set_on_mouse_down_listener(self.teszt)


    def teszt(self, sender, event):
        exit()



class GameStage(game.scene2d.MyStage):
    def __init__(self):
        super().__init__()
        self.hatter_bg = HatterAct()
        self.napos_bg = NaposAct()
        self.nap_bg = NapAct()


        self.hatter_bg.z_index = 6
        self.napos_bg.z_index = 4
        self.nap_bg.z_index = 5

        self.nap_bg.x = 900
        self.nap_bg.y = -100

        self.add_actor(self.hatter_bg)
        self.add_actor(self.napos_bg)
        self.add_actor(self.nap_bg)




class GameScreen(game.scene2d.MyScreen):
    def __init__(self):
        super().__init__()
        self.add_stage(GameStage())


class GameSelf(game.scene2d.MyGame):
    def __init__(self, width: int = 1280, height: int = 720, autorun: bool = False):
        super().__init__(width, height, autorun)
        self.screen = GameScreen()




GameSelf().run()




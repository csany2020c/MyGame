from kuposztok.MenuBgActor import *


class MenuStage(game.scene2d.MyStage):


    def __init__(self):
        super().__init__()
        bg = MenuBgActor()
        self.add_actor(bg)
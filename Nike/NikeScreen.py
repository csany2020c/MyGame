import game
from Nike.NikeStage import *

class Menu(game.scene2d.MyScreen):
    def __init__(self):
        super().__init__()
        self.set_background_color(155, 0, 0)
        self.add_stage(MenuStage())

class Credit(game.scene2d.MyScreen):
    def __init__(self):
        super().__init__()
        self.set_background_color(155, 0, 0)
        self.add_stage(CreditStage())

class Game(game.scene2d.MyScreen):
    def __init__(self):
        super().__init__()
        self.add_stage(GameStage1())

class Game2(game.scene2d.MyScreen):
    def __init__(self):
        super().__init__()
        self.add_stage(GameStage2())

class Win(game.scene2d.MyScreen):
    def __init__(self):
        super().__init__()
        self.set_background_color(100, 0, 100)
        self.add_stage(WinStage())

    def act(self, delta_time: float):
        super().act(delta_time)
        if self.elapsed_time > 4:
            self.game.screen = Menu()

class Lose(game.scene2d.MyScreen):
    def __init__(self):
        super().__init__()
        self.set_background_color(100, 0, 100)
        self.add_stage(LoseStage())

    def act(self, delta_time: float):
        super().act(delta_time)
        if self.elapsed_time > 4:
            self.game.screen = Game()


class Info(game.scene2d.MyScreen):
    def __init__(self):
        super().__init__()
        self.set_background_color(100,0,100)
        self.add_stage(InfoStage())
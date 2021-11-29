from HawkProductions.Game.GameStage import *


class GameScreen(game.scene2d.MyScreen):
    def __init__(self):
        super().__init__()
        self.add_stage(GameStage())


class GameScreen1(game.scene2d.MyScreen):
    def __init__(self):
        super().__init__()
        self.add_stage(GameStage1())


class GameScreen2(game.scene2d.MyScreen):
    def __init__(self):
        super().__init__()
        self.add_stage(GameStage2())


class GameScreen3(game.scene2d.MyScreen):
    def __init__(self):
        super().__init__()
        self.add_stage(GameStage3())


class GameScreen4(game.scene2d.MyScreen):
    def __init__(self):
        super().__init__()
        self.add_stage(GameStage4())
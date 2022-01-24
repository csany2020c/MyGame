import game
from kuposztok.Game.CarOsszesStage import CarOsszesStage


class CarOsszesScreen(game.scene2d.MyScreen):

    def __init__(self, carvalt: int, money: int, maxScore: int):
        super().__init__()
        self.set_background_color(r=0, g=0, b=0)
        self.add_stage(CarOsszesStage(carvalt=carvalt, money=money, maxScore=maxScore))

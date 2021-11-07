import game
from kuposztok.Game.Car3Multi.Car3StageMultiP import Car3StageMultiP


class Car3ScreenMultiP(game.scene2d.MyScreen):

    def __init__(self):
        super().__init__()
        self.set_background_color(r=0,g=0, b=0)
        self.add_stage(Car3StageMultiP())

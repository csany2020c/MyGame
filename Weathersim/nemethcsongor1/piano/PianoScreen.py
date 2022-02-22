from Weathersim.nemethcsongor1.piano.PianoStage import *


class PianoScreen(game.scene2d.MyScreen):

    def __init__(self):
        super().__init__()
        self.add_stage(PianoStage())

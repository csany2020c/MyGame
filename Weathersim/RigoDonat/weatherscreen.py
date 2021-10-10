import game
from weatherstages import*

class WeatherScreen(game.scene2d.MyScreen):

    def __init__(self):
        super().__init__()
        self.set_background_color(0, 0, 150)
        self.add_stage(WeatherStage())
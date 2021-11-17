import game
from yetiactor import Start

class MenuStage(game.scene2d.MyStage):
    def __init__(self):
        super().__init__()
        self.start = Start()
        self.start.x = 390
        self.add_actor(self.start)

import game

class PacalStage(game.scene2d.MyStage):

    def __init__(self):
        super().__init__("..fujpacal/Images/bogrács.png")
        self.set_width(300)
        self.x = 500
        self.y = 50


PacalStage()
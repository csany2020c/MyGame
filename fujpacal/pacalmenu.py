import game

class PacalStage(game.scene2d.MyStage):

    def __init__(self):
        super().__init__("bogrács.png")
        self.run()

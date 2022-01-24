import game
class TestActor(game.scene2d.MyActor):
    def __init__(self,x,y):
        super().__init__("Water.png")
        self.x = x
        self.y = y
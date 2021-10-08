import game
from weatherscreen import*

class RigoDonat(game.scene2d.MyGame):

    def __init__(self):
        super().__init__(1280, 720)
        self.set_screen(())
        self.run()
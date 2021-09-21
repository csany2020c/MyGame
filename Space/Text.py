from game.scene2d.MyLabel import *

class Arial32(MyLabel):

    def __init__(self, string: str = "MyText") -> None:
        super().__init__(font_name="arial", font_size=32)

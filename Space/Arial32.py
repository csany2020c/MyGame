from game.scene2d.MyLabel import *

class Arial32(MyLabel):

    def __init__(self, string: str = "MyText") -> None:
        MyLabel.__init__(self, string=string, font_name="arial")

    def act(self, delta_time: float):
        MyLabel.act(self, delta_time)
        if self.x + self.width < self.screen_width:
            self.x += delta_time * 20
            self.rotate_with(delta_time * 20)

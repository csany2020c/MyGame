import game

class Arial32(game.scene2d.MyLabel):

    def __init__(self, string: str = "MyText") -> None:
        game.scene2d.MyLabel.__init__(self, string=string, font_name="arial")

    def act(self, delta_time: float):
        game.scene2d.MyLabel.act(self, delta_time)
        if self.x + self.width < game.scene2d.MyGame.get_screen_width():
            self.x += delta_time * 20
            self.rotate_with(delta_time * 20)

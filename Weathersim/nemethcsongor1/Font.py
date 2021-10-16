import game


class Font(game.scene2d.MyLabel):
    def __init__(self, string: str = "MyText") -> None:
        game.scene2d.MyLabel.__init__(self, string=string, font_name="Comic Sans MS")

    def act(self, delta_time: float):
        game.scene2d.MyLabel.act(self, delta_time)


class Font2(game.scene2d.MyLabel):
    def __init__(self, string: str = "MyText") -> None:
        game.scene2d.MyLabel.__init__(self, string=string, font_name="fonts/Rockabye-Regular.otf")

    def act(self, delta_time: float):
        game.scene2d.MyLabel.act(self, delta_time)


class Font3(game.scene2d.MyLabel):
    def __init__(self, string: str = "MyText") -> None:
        game.scene2d.MyLabel.__init__(self, string=string, font_name="fonts/OldLondon.ttf")

    def act(self, delta_time: float):
        game.scene2d.MyLabel.act(self, delta_time)
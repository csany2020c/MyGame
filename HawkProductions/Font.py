import game


class Anything(game.scene2d.MyLabel):
    def __init__(self, string: str = "MyText") -> None:
        game.scene2d.MyLabel.__init__(self, string=string, font_name="Anything Better Font by 7NTypes.otf")

    def act(self, delta_time: float):
        game.scene2d.MyLabel.act(self, delta_time)


class Helvetica(game.scene2d.MyLabel):
        def __init__(self, string: str = "MyText") -> None:
            game.scene2d.MyLabel.__init__(self, string=string, font_name="HelveticaUltraComp.ttf")

        def act(self, delta_time: float):
            game.scene2d.MyLabel.act(self, delta_time)

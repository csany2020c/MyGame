import game

class Label(game.scene2d.MyLabel):
    def __init__(self, string: str = "HP: ", font_name: str = "system", font_size: int = 64):
        super().__init__(string, font_name, font_size)
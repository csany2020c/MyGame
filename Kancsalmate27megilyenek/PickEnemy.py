import game

class PickEnemy(game.scene2d.MyActor):
    def __init__(self, image_url: str = ""):
        super().__init__("Sand.png")
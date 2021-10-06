import game

class MenuActor1(game.scene2d.MyActor):
    def __init__(self, image_url: str = ""):
        super().__init__("Exitbutton.png")


class MenuActor2(game.scene2d.MyActor):
    def __init__(self, image_url: str = ""):
        super().__init__("Startbutton.png")

class MenuActor3(game.scene2d.MyActor):
    def __init__(self, image_url: str = ""):
        super().__init__("Infobutton.png")

class MenuActor4(game.scene2d.MyActor):
    def __init__(self, image_url: str = ""):
        super().__init__("Optionsbutton.png")
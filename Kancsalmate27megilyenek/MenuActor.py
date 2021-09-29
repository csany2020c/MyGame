import game

class MenuActor1(game.scene2d.MyActor):
    def __init__(self, image_url: str = ""):
        super().__init__("Texture/Exitbutton.png")


class MenuActor2(game.scene2d.MyActor):
    def __init__(self, image_url: str = ""):
        super().__init__("Texture/Startbutton.png")

class MenuActor3(game.scene2d.MyActor):
    def __init__(self, image_url: str = ""):
        super().__init__("Texture/Infobutton.png")

class MenuActor4(game.scene2d.MyActor):
    def __init__(self, image_url: str = ""):
        super().__init__("Texture/Optionsbutton.png")
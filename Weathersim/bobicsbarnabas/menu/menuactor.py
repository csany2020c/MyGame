import game

class menuactor1(game.scene2d.MyActor):

    def __init__(self):
        super().__init__("resources/images/gomb1.png")

class menuactor2(game.scene2d.MyActor):

    def __init__(self):
        super().__init__("resources/images/gomb2.png")

class menuactor3(game.scene2d.MyActor):

    def __init__(self):
        super().__init__("resources/images/gomb3.png")

class menuactor4(game.scene2d.MyActor):

    def __init__(self):
        super().__init__("resources/images/gomb4.png")

class menuhatter(game.scene2d.MyActor):

    def __init__(self):
        super().__init__("resources/images/menuhatterx.png")

class exit(game.scene2d.MyActor):

    def __init__(self):
        super().__init__("resources/images/exit.png")
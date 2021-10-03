import game

class testActor(game.scene2d.MyActor):
    def __init__(self, image_url: str = "bg.png"):
        super().__init__(image_url)

class startActor(game.scene2d.MyActor):

    def __init__(self, image_url: str = "start.png"):
        super().__init__(image_url)
        self.width = 300
        self.x = 1280 - 300 - 25
        self.y = 200

class startActorClick(game.scene2d.MyActor):
    def __init__(self, image_url: str = "startOnClick.png"):
        super().__init__(image_url)
        self.width = 300
        self.x = 1280 - 300 - 25
        self.y = 200

class exitActor(game.scene2d.MyActor):
    def __init__(self, image_url: str = "exit.png"):
        super().__init__(image_url)
        self.width = 300
        self.x = 1280 - 300 - 25
        self.y = 350

class exitActorClick(game.scene2d.MyActor):
    def __init__(self, image_url: str = "exitOnClick.png"):
        super().__init__(image_url)
        self.width = 300
        self.x = 1280 - 300 - 25
        self.y = 350
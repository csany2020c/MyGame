import game

class menubackground(game.scene2d.MyActor):
    def __init__(self):
        self.map = super().__init__('!_resources/images/menubackground.png')

class exitbutton(game.scene2d.MyActor):
    def __init__(self):
        self.map = super().__init__('!_resources/images/exitbutton.png')

class naposbutton(game.scene2d.MyActor):
    def __init__(self):
        self.map = super().__init__('!_resources/images/naposbutton.png')

class esosbutton(game.scene2d.MyActor):
    def __init__(self):
        self.map = super().__init__('!_resources/images/esosbutton.png')

class havasbutton(game.scene2d.MyActor):
    def __init__(self):
        self.map = super().__init__('!_resources/images/havasbutton.png')
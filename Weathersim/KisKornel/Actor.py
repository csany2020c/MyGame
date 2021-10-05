import game

class SunnyActor(game.scene2d.MyActor):
    def __init__(self):
        super().__init__("sun.png")





class backgroundActor(game.scene2d.MyActor):
    def __init__(self):
        super().__init__("landscape.png")



class skyActor(game.scene2d.MyActor):
    def __init__(self):
        super().__init__("sunny.png")
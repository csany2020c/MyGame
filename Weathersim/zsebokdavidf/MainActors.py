import game


class Background(game.scene2d.MyActor):

    def __init__(self):
        super().__init__('../!_resources/images/landscape.png')


class Cloud(game.scene2d.MyActor):

    def __init__(self):
        super().__init__('images/Cloud.png')


class SnowyGround(game.scene2d.MyActor):

    def __init__(self):
        super().__init__('images/SnowyGround.png')


class Ice(game.scene2d.MyActor):

    def __init__(self):
        super().__init__('images/Ice.png')

class Snow(game.scene2d.MyActor):

    def __init__(self):
        super().__init__('../!_resources/images/snow.png')





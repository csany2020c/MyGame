import game


class MenuButton(game.scene2d.MyActor):
    def __init__(self):
        self.map = super().__init__('!_resources/images/menubutton.png')
        self.z_index = 6


class MiniMenuButton(game.scene2d.MyActor):
    def __init__(self):
        self.map = super().__init__('!_resources/images/minimenubutton.png')
        self.z_index = 6


class MiniNapButton(game.scene2d.MyActor):
    def __init__(self):
        self.map = super().__init__('!_resources/images/mininapbutton.png')
        self.z_index = 6


class MiniEsoButton(game.scene2d.MyActor):
    def __init__(self):
        self.map = super().__init__('!_resources/images/miniesobutton.png')
        self.z_index = 6


class MiniHavasesoButton(game.scene2d.MyActor):
    def __init__(self):
        self.map = super().__init__('!_resources/images/minihavasesobutton.png')
        self.z_index = 6


class MiniHoButton(game.scene2d.MyActor):
    def __init__(self):
        self.map = super().__init__('!_resources/images/minihobutton.png')
        self.z_index = 6

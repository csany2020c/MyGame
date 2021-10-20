import game


class BgActor(game.scene2d.MyActor):

    def __init__(self):
        super().__init__('image/menu.png')

    def act(self, delta_time: float):
        super().act(delta_time)
        self.y += delta_time * 500


class Visszagomb(game.scene2d.MyActor):
    def __init__(self):
        self.credit = super().__init__('image/back_to_menu_button.png')


class Joseph(game.scene2d.MyActor):
    def __init__(self):
        self.credit = super().__init__('image/my-caracter.png')


class Enemy(game.scene2d.MyActor):
    def __init__(self):
        self.credit = super().__init__('image/my-caracter.png')

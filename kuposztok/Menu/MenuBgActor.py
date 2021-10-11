import game

class MenuActor(game.scene2d.MyActor):

    def __init__(self):
        super().__init__('../image/menu.png')

class creditact(game.scene2d.MyActor):

    def __init__(self):
        super().__init__('../image/credit_button.png')

class exitact(game.scene2d.MyActor):

    def __init__(self):
        super().__init__('../image/exit_button.png')

class playact(game.scene2d.MyActor):

    def __init__(self):
        super().__init__('../image/play_button.png')

class Button1(game.scene2d.MyActor):

    def __init__(self):
        super().__init__('../image/play_button.png')


class Button2(game.scene2d.MyActor):

    def __init__(self):
        super().__init__('../image/exit_button.png')


class Button3(game.scene2d.MyActor):

    def __init__(self):
        super().__init__('../image/credit_button.png')
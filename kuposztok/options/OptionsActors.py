import game

class BgActor(game.scene2d.MyActor):

    def __init__(self):
        super().__init__('image/snow.png')

class Sound_Max(game.scene2d.MyActor):

    def __init__(self):
        super().__init__('image/sound_max.png')

class Sound_Mid(game.scene2d.MyActor):

    def __init__(self):
        super().__init__('image/sound_mid.png')

class Sound_Min(game.scene2d.MyActor):

    def __init__(self):
        super().__init__('image/sound_low.png')

class Sound_No(game.scene2d.MyActor):

    def __init__(self):
        super().__init__('image/sound_no.png')

class SaveButton(game.scene2d.MyActor):

    def __init__(self):
        super().__init__('image/save.png')
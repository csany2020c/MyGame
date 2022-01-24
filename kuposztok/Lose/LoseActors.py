import game
import pygame

class BgActor(game.scene2d.MyActor):
    def __init__(self):
        super().__init__('image/snow.png')

class NewGame(game.scene2d.MyActor):
    def __init__(self):
        super().__init__('image/new_game.png')

class Menub(game.scene2d.MyActor):
    def __init__(self):
        super().__init__('image/back_to_menu_button.png')
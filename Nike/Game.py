from Nike.Screen import *
from Nike.Actor import *
from  Nike.Stage import *
import game

class Game(game.scene2d.MyGame):
    def __init__(self, width: int = 1280, height: int = 720):
        super().__init__(width, height)

Game().run()
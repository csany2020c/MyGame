import webbrowser

import game
import pygame
from Kancsalmate27megilyenek.TextureActors import *
from Kancsalmate27megilyenek.MapActor import *
from Kancsalmate27megilyenek.BackgroundActor import *
from Kancsalmate27megilyenek.MenuScreen import *
from Kancsalmate27megilyenek.MapActor import *
from game.simpleworld.ShapeType import ShapeType
from Kancsalmate27megilyenek.Labels import *
from Kancsalmate27megilyenek.ArenaScreen import *
from game.scene2d import MyBaseActor
from Kancsalmate27megilyenek.PlayerActor import *
from Kancsalmate27megilyenek.Map import *
class InStage(game.scene2d.MyStage):
    def __init__(self):
        super().__init__()
        self.eletero : int = 100
        self.heart = HeartActor()
        self.heart1 = HeartActor()
        self.heart2 = HeartActor()
        self.add_actor(self.heart)
        self.add_actor(self.heart1)
        self.add_actor(self.heart2)
        self.player = PlayerActor()
        self.add_actor(self.player)
        self.player.set_z_index(1)
        # self.set_on_key_down_listener(self.moveKeys)
        # self.set_on_key_up_listener(self.moveKeysOff)
        self.camera.tracking = self.player
        self.map = Map(self, "butamap")




    def act(self, delta_time: float):
        super().act(delta_time)
        self.heart.x = self.player.x - 15
        self.heart.y = self.player.y - 30
        self.heart1.x = self.player.x + 10
        self.heart1.y = self.player.y - 30
        self.heart2.x = self.player.x + 35
        self.heart2.y = self.player.y - 30
        if self.eletero < 65:
            self.heart2.remove_from_stage()
        if self.eletero < 30:
            self.heart1.remove_from_stage()
        if self.eletero < 0:
            self.heart.remove_from_stage()
        if self.eletero > 65:
            self.add_actor(self.heart2)
        if self.eletero > 30:
            self.add_actor(self.heart1)
        if self.player.overlaps(self.sand):
            self.screen.game.set_screen(ArenaScreen())

        if self.player.overlaps(self.water2):
            webbrowser.open("https://www.youtube.com/watch?v=rX7XZLcGAxw")


import game
from Kancsalmate27megilyenek.MenuGame import *

class MusicActor(game.scene2d.MyActor):
    def __init__(self, image_url: str = ""):
        super().__init__("musicOn.png")
        self.menugame = MainGame()
        self.isMuted:bool = False

    def changeState(self):
        self.isMuted = not self.isMuted
        self.changeImage()
        self.menugame.handleMusic()

    def getState(self) -> bool:
        return self.isMuted

    def changeImage(self):
        if self.isMuted == False:
            self.image_url = "musicOn.png"
        else:
            self.image_url = "musicOff.png"
        self.set_size(75,45)
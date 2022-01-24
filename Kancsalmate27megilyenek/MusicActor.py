import game
from pygame import mixer

class MusicActor(game.scene2d.MyActor):
    def __init__(self, image_url: str = ""):
        super().__init__("musicOn.png")
        self.isMuted:bool = False
        mixer.init()
        mixer.music.load("music.wav")
        mixer.music.set_volume(1)
        mixer.music.play(-1)

    def changeState(self):
        self.isMuted = not self.isMuted
        self.changeImage()

    def getState(self) -> bool:
        return self.isMuted

    def changeImage(self):
        if self.isMuted == False:
            mixer.music.unpause()
            self.image_url = "musicOn.png"
        else:
            mixer.music.pause()
            self.image_url = "musicOff.png"
        self.set_size(75,45)
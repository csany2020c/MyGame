from pygame import mixer
import game
from Kancsalmate27megilyenek.MusicActor import *
from Kancsalmate27megilyenek.MenuScreen import *



class MainGame(game.scene2d.MyGame):

    def __init__(self, width: int = 1280, height: int = 720, autorun: bool = False, autosize: bool = True):
        super().__init__(width, height, autorun, autosize)
        self.screen = MenuScreen3()
        self.run()
        self.musicActor = MusicActor()
        self.state:bool = False
        mixer.init()
        mixer.music.load("music.mp3")
        mixer.music.set_volume(0.5)
        mixer.music.play(1)

    def handleMusic(self):
        if self.state == False:
            pygame.mixer.music.unpause()
        else:
            pygame.mixer.music.pause()
MainGame()

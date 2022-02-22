import game
import pygame
from Weathersim.nemethcsongor1.piano.PianoAct import *


class PianoStage(game.scene2d.MyStage):
    def __init__(self):
        super().__init__()

        pygame.mixer.init()

        self.bg = Bg()
        self.add_actor(self.bg)

        self.sign = Gabriola()
        self.add_actor(self.sign)
        self.sign.set_text("Piano Simulator")
        self.sign.x = 150
        self.sign.y = 425
        self.sign.width = 1000

        self.klav = Klaviatura()
        self.add_actor(self.klav)
        self.klav.y = -70
        self.klav.x = -30
        self.klav.set_size(1335, 350)

        self.set_on_key_down_listener(self.gomb)

    def gomb(self, sender, event):
        print(sender)
        if event.key == pygame.K_a:
            pygame.mixer.music.load("../piano/pianoC.wav")
            pygame.mixer.music.play()
        if event.key == pygame.K_w:
            pygame.mixer.music.load("../piano/pianoCisz.wav")
            pygame.mixer.music.play()
        if event.key == pygame.K_s:
            pygame.mixer.music.load("../piano/pianoD.wav")
            pygame.mixer.music.play()
        if event.key == pygame.K_s:
            pygame.mixer.music.load("../piano/pianoD.wav")
            pygame.mixer.music.play()
        if event.key == pygame.K_d:
            pygame.mixer.music.load("../piano/pianoE.wav")
            pygame.mixer.music.play()
        if event.key == pygame.K_f:
            pygame.mixer.music.load("../piano/pianoF.wav")
            pygame.mixer.music.play()
        if event.key == pygame.K_g:
            pygame.mixer.music.load("../piano/pianoG.wav")
            pygame.mixer.music.play()
        if event.key == pygame.K_h:
            pygame.mixer.music.load("../piano/pianoA.wav")
            pygame.mixer.music.play()
        if event.key == pygame.K_j:
            pygame.mixer.music.load("../piano/pianoB.wav")
            pygame.mixer.music.play()
        if event.key == pygame.K_u:
            pygame.mixer.music.load("../piano/pianoBb.wav")
            pygame.mixer.music.play()
        if event.key == pygame.K_k:
            pygame.mixer.music.load("../piano/pianoC5.wav")
            pygame.mixer.music.play()
        if event.key == pygame.K_SPACE:
            pygame.mixer.music.stop()

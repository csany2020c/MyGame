import time
import game
import pygame
import random
from HawkProductions.Actors import *
import HawkProductions.menu.MenuScreen
import HawkProductions.over.OverScreen


class GameStage(game.scene2d.MyStage):
    def __init__(self):
        super().__init__()
        pygame.mixer.init()
        pygame.mixer.music.load("../HawkProductions/Music/Nixon.wav")
        pygame.mixer.music.play(-1)
        pygame.mixer.music.set_volume(0.2)
        pygame.mixer.music.fadeout(145000)
        self.Bg = Bg()
        self.add_actor(self.Bg)
        self.Bg.set_size(width=1280, height=720)

        self.D = Deagle()
        self.add_actor(self.D)
        self.D.y = 250
        self.D.x = 300
        self.D.width = 95

        self.arrow = Arrow()
        self.add_actor(self.arrow)
        self.arrow.x = 0
        self.arrow.y = 5
        self.arrow.w = 125
        self.arrow.set_on_mouse_down_listener(self.click2)


        self.add_timer(game.scene2d.MyTickTimer(self.add_asd, 5))
        self.add_timer(game.scene2d.MyTickTimer(self.add_asd2, 8))

        self.set_on_key_down_listener(self.katt)



    def add_asd(self, sender):
        #self.P1 még nem jó
        self.P1 = Pile_f()
        self.add_actor(self.P1)
        self.P1.set_hitbox_scale_h = 0
        self.P1.set_hitbox_scale_w = 0
        self.P1.h = 350
        self.P1.y = random.randint(-70, -15)
        #self.P1.width = 600

        self.P2 = Pile_a()
        self.add_actor(self.P2)
        self.P2.h = 370
        self.P2.set_hitbox_scale_h = 0
        self.P2.set_hitbox_scale_w = 0
        self.P2.y = random.randint(550, 700)


        #nem jó
        #if self.D.overlaps(self.P1 or self.P2):
         #   self.screen.game.set_screen(HawkProductions.over.OverScreen.OverScreen())


    def add_asd2(self, sender):
        self.C = Coin()
        self.add_actor(self.C)
        self.C.x = 1280
        self.C.y = random.randint(10, 500)
        self.C.width = 300

    def click2(self, sender, event):
         if event.button == 1:
            self.screen.game.set_screen(HawkProductions.menu.MenuScreen.MenuScreen())

    def katt(self, sender, event):
        print(sender)
        if event.key == pygame.K_BACKSPACE:
            self.screen.game.set_screen(HawkProductions.menu.MenuScreen.MenuScreen())
        if event.key == pygame.K_ESCAPE:
            quit()
        if event.key == pygame.K_w:
            self.D.y -= 50
            self.D.r -= 7.5
            effect = pygame.mixer.Sound('../Hawkproductions/Music/Shoot.wav')
            effect.play()
        if event.key == pygame.K_s:
            self.D.y += 50
            self.D.r += 7.5
            effect = pygame.mixer.Sound('../Hawkproductions/Music/Shoot.wav')
            effect.play()

import time
import game
import pygame
import random
from HawkProductions.Actors import *
import HawkProductions.menu.MenuScreen
import HawkProductions.over.OverScreen
from HawkProductions.Font import *


class GameStage12(game.scene2d.MyStage):
    def __init__(self):
        super().__init__()
        pygame.mixer.init()
        pygame.mixer.music.load("../HawkProductions/Music/Nixon.wav")
        pygame.mixer.music.play(-1)
        pygame.mixer.music.set_volume(0.2)
        #pygame.mixer.music.fadeout(145000)
        self.Bg = Bg()
        self.add_actor(self.Bg)
        self.Bg.set_size(width=1280, height=720)

        self.D = Deagle_2()
        self.add_actor(self.D)
        self.D.y = 250
        self.D.x = 300
        self.D.width = 95
        self.D.hitbox_scale_h = 0.55
        self.D.hitbox_scale_w = 0.75

        self.arrow = Arrow()
        self.add_actor(self.arrow)
        self.arrow.x = 0
        self.arrow.y = 5
        self.arrow.w = 125
        self.arrow.set_on_mouse_down_listener(self.click2)

        self.add_timer(game.scene2d.MyTickTimer(self.add_asd, 5))
        self.add_timer(game.scene2d.MyTickTimer(self.add_asd1, 7))
        self.add_timer(game.scene2d.MyTickTimer(self.add_asd2, 9))
        self.add_timer(game.scene2d.MyTickTimer(self.add_asd3, 11))
        self.add_timer(game.scene2d.MyTickTimer(self.add_asd4, 6))
        self.add_timer(game.scene2d.MyTickTimer(self.add_asd5, 8))
        self.add_timer(game.scene2d.MyTickTimer(self.add_asd6, 10))

        self.set_on_key_down_listener(self.katt)

        self.P1 = Pile_f()
        self.P2 = Pile_a()
        self.P3 = Pile_f()
        self.P4 = Pile_a()
        self.P5 = Pile_f()
        self.P6 = Pile_a()
        self.P7 = Pile_f()
        self.P8 = Pile_a()
        self.C = Coin()
        self.C1 = Coin()
        self.C2 = Coin()

    def add_asd(self, sender):
        print(sender)
        self.add_actor(self.P1)
        self.P1.set_hitbox_scale_h = 0
        self.P1.set_hitbox_scale_w = 0
        self.P1.h = 365
        self.P1.y = random.randint(-70, -20)
        if self.elapsed_time > 15:
            self.P1.y = random.randint(-20, 100)
        if self.elapsed_time > 20:
            self.P1.y = random.randint(-20, 100)

        self.add_actor(self.P2)
        self.P2.h = 370
        self.P2.set_hitbox_scale_h = 0
        self.P2.set_hitbox_scale_w = 0
        self.P2.y = random.randint(550, 700)
        if self.elapsed_time > 15:
            self.P2.y = random.randint(550, 700)
        if self.elapsed_time > 20:
            self.P2.y = random.randint(550, 700)

    def add_asd1(self, sender):
        self.add_actor(self.P3)
        self.P3.set_hitbox_scale_h = 0
        self.P3.set_hitbox_scale_w = 0
        self.P3.h = 365
        self.P3.y = -25
        if self.elapsed_time > 21:
            self.P3.y = -42
        if self.elapsed_time > 28:
            self.P3.y = -52

        self.add_actor(self.P4)
        self.P4.h = 370
        self.P4.set_hitbox_scale_h = 0
        self.P4.set_hitbox_scale_w = 0
        self.P4.y = 600
        if self.elapsed_time > 21:
            self.P4.y = 590
        if self.elapsed_time > 28:
            self.P4.y = 610

    def add_asd2(self, sender):
        self.add_actor(self.P5)
        self.P5.set_hitbox_scale_h = 0
        self.P5.set_hitbox_scale_w = 0
        self.P5.h = 365
        self.P5.y = -28
        if self.elapsed_time > 27:
            self.P5.y = -24
        if self.elapsed_time > 35:
            self.P5.y = -55

        self.add_actor(self.P6)
        self.P6.h = 370
        self.P6.set_hitbox_scale_h = 0
        self.P6.set_hitbox_scale_w = 0
        self.P6.y = 570
        if self.elapsed_time > 27:
            self.P6.y = 515
        if self.elapsed_time > 35:
            self.P6.y = 545

    def add_asd3(self, sender):
        self.add_actor(self.P7)
        self.P7.set_hitbox_scale_h = 0
        self.P7.set_hitbox_scale_w = 0
        self.P7.h = 365
        self.P7.y = -28

        self.add_actor(self.P8)
        self.P8.h = 370
        self.P8.set_hitbox_scale_h = 0
        self.P8.set_hitbox_scale_w = 0
        self.P8.y = 570

    def add_asd4(self, sender):
        self.add_actor(self.C)
        self.C.x = 1180
        self.C.y = 420
        self.C.width = 300

    def add_asd5(self, sender):
        self.add_actor(self.C1)
        self.C1.x = 1200
        self.C1.y = random.randint(200, 500)
        self.C1.width = 300

    def add_asd6(self, sender):
        self.add_actor(self.C2)
        self.C2.x = 1200
        self.C2.y = random.randint(200, 500)
        self.C2.width = 300

    def act(self, delta_time: float):
        super().act(delta_time)
        if self.D.overlaps(self.P1 or self.P2):
            self.screen.game.set_screen(HawkProductions.over.OverScreen.OverScreen())
        if self.D.overlaps(self.P3 or self.P4):
            self.screen.game.set_screen(HawkProductions.over.OverScreen.OverScreen())
        if self.D.overlaps(self.P5 or self.P6):
            self.screen.game.set_screen(HawkProductions.over.OverScreen.OverScreen())
        if self.D.overlaps(self.P7 or self.P8):
            self.screen.game.set_screen(HawkProductions.over.OverScreen.OverScreen())

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


import HawkProductions.menu.MenuScreen
from HawkProductions.Actors import *
from HawkProductions.Font import *
import HawkProductions.Game.GameScreen
import HawkProductions.Game2.GameScreen2
import HawkProductions.Music
import pygame


class SelectStgage(game.scene2d.MyStage):
    def __init__(self):
        super().__init__()
        pygame.mixer.init()
        pygame.mixer.music.load("../HawkProductions/Music/Sel.wav")
        pygame.mixer.music.play(-1)
        self.t = Arrow()
        self.add_actor(self.t)
        self.t.set_on_mouse_down_listener(self.click_m)
        self.t.w = 125

        self.D = Deagle1()
        self.add_actor(self.D)
        self.D.x = 530
        self.D.y = 250
        self.D.width = 200

        self.s1 = Sellect()
        self.add_actor(self.s1)
        self.s1.width = 200
        self.s1.x = 530
        self.s1.y = 400
        self.s1.set_on_mouse_down_listener(self.click_g1)

        self.arrow_l1 = Arrow()
        self.add_actor(self.arrow_l1)
        self.arrow_l1.x = 330
        self.arrow_l1.y = 280
        self.arrow_l1.w = 200
        self.arrow_l1.set_on_mouse_down_listener(self.click_l1)

        self.arrow_r1 = Arrow_r()
        self.add_actor(self.arrow_r1)
        self.arrow_r1.x = 730
        self.arrow_r1.y = 280
        self.arrow_r1.w = 200
        self.arrow_r1.set_on_mouse_down_listener(self.click_r1)

        self.arrow_l2 = Arrow()
        self.arrow_l2.x = 330
        self.arrow_l2.y = 280
        self.arrow_l2.w = 200
        self.arrow_l2.set_on_mouse_down_listener(self.click_l2)

        self.arrow_r2 = Arrow_r()
        self.arrow_r2.x = 730
        self.arrow_r2.y = 280
        self.arrow_r2.w = 200
        self.arrow_r2.set_on_mouse_down_listener(self.click_r2)

        self.arrow_l3 = Arrow()
        self.arrow_l3.x = 330
        self.arrow_l3.y = 280
        self.arrow_l3.w = 200
        self.arrow_l3.set_on_mouse_down_listener(self.click_l3)

        self.arrow_r3 = Arrow_r()
        self.arrow_r3.x = 730
        self.arrow_r3.y = 280
        self.arrow_r3.w = 200
        self.arrow_r3.set_on_mouse_down_listener(self.click_r3)

        self.D2 = Deagle2()
        self.D2.x = 520
        self.D2.y = 280
        self.D2.w = 200

        self.s2 = Sellect()
        self.s2.width = 200
        self.s2.x = 530
        self.s2.y = 400
        self.s2.set_on_mouse_down_listener(self.click_g2)

        self.D3 = Deagle3()
        self.D3.x = 520
        self.D3.y = 280
        self.D3.w = 200

        self.s3 = Sellect()
        self.s3.width = 200
        self.s3.x = 630
        self.s3.y = 400
        self.s3.set_on_mouse_down_listener(self.click_g3)

        self.D4 = Deagle4()
        self.D4.x = 520
        self.D4.y = 280
        self.D4.w = 250

        self.s4 = Sellect()
        self.s4.width = 200
        self.s4.x = 630
        self.s4.y = 400
        self.s4.set_on_mouse_down_listener(self.click_g4)

        self.arrow_l4 = Arrow()
        self.arrow_l4.x = 330
        self.arrow_l4.y = 280
        self.arrow_l4.w = 200

        self.arrow_r4 = Arrow_r()
        self.arrow_r4.x = 730
        self.arrow_r4.y = 280
        self.arrow_r4.w = 200


    def click_m(self, sender, event):
        if event.button == 1:
            self.screen.game.set_screen(HawkProductions.menu.MenuScreen.MenuScreen())

    def click_g1(self, sender, event):
        if event.button == 1:
            self.screen.game.set_screen(HawkProductions.Game.GameScreen.GameScreen())

    def click_g2(self, sender, event):
        if event.button == 1:
            self.screen.game.set_screen(HawkProductions.Game2.GameScreen2.GameScreen())

    def click_g3(self, sender, event):
        if event.button == 1:
            self.screen.game.set_screen(HawkProductions.Game.GameScreen.GameScreen())

    def click_g4(self, sender, event):
        if event.button == 1:
            self.screen.game.set_screen(HawkProductions.Game.GameScreen.GameScreen())

    def click_g5(self, sender, event):
        if event.button == 1:
            self.screen.game.set_screen(HawkProductions.Game.GameScreen.GameScreen())

    def click_l1(self, sender, event):
        if event.button == 1:
            self.remove_actor(self.D)
            self.add_actor(self.D2)
            self.remove_actor(self.arrow_l1)
            self.add_actor(self.arrow_l2)
            self.add_actor(self.arrow_r2)
            self.remove_actor(self.arrow_r1)
            self.remove_actor(self.s1)
            self.add_actor(self.s2)


    def click_r1(self, sender, event):
        if event.button == 1:
            self.remove_actor(self.D)
            self.add_actor(self.D3)
            self.remove_actor(self.arrow_l1)
            self.add_actor(self.arrow_l3)
            self.remove_actor(self.arrow_r1)
            self.add_actor(self.arrow_r3)
            self.remove_actor(self.s1)
            self.add_actor(self.s2)

    def click_l2(self, sender, event):
        if event.button == 1:
            self.remove_actor(self.D2)
            self.add_actor(self.D3)
            self.remove_actor(self.arrow_l2)
            self.add_actor(self.arrow_l3)
            self.remove_actor(self.arrow_r2)
            self.add_actor(self.arrow_r3)
            self.remove_actor(self.s2)
            self.add_actor(self.s3)

    def click_r2(self, sender, event):
        if event.button == 1:
            self.remove_actor(self.D2)
            self.add_actor(self.D)
            self.remove_actor(self.arrow_l2)
            self.add_actor(self.arrow_l1)
            self.remove_actor(self.arrow_r2)
            self.add_actor(self.arrow_r1)
            self.add_actor(self.s1)
            self.remove_actor(self.s2)

    def click_l3(self, sender, event):
        if event.button == 1:
            self.remove_actor(self.D3)
            self.add_actor(self.D4)
            self.remove_actor(self.arrow_l3)
            self.add_actor(self.arrow_l4)
            self.remove_actor(self.arrow_r3)
            self.add_actor(self.arrow_r4)
            self.remove_actor(self.s3)
            self.add_actor(self.s4)

    def click_r3(self, sender, event):
        if event.button == 1:
            self.remove_actor(self.D3)
            self.add_actor(self.D2)
            self.remove_actor(self.arrow_l3)
            self.add_actor(self.arrow_l2)
            self.remove_actor(self.arrow_r3)
            self.add_actor(self.arrow_r2)
            self.remove_actor(self.s3)
            self.add_actor(self.s2)

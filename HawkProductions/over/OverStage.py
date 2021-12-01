from HawkProductions.Font import *
import pygame
import HawkProductions.menu.MenuScreen


class OverStage(game.scene2d.MyStage):
    def __init__(self):
        super().__init__()
        pygame.mixer.init()
        pygame.mixer.music.load("../HawkProductions/Music/Over.wav")
        pygame.mixer.music.play(-1)
        self.F = Gameover()
        #self.add_actor(self.F)
        self.F.set_text("Játék Túl")
        self.F.x = 360
        self.F.y = 10
        self.F.set_color(255, 255, 255)
        self.F.set_font_size(300)
        self.F.set_text("Game Over")
        self.F.x = 500
        self.F.y = 225
        self.F.set_color(204, 20, 0)
        self.F.x = 500
        self.F.y = 100

        self.g = Gameover()
        self.add_actor(self.g)
        self.g.set_text("Próbáld újra!")
        self.g.set_color(255, 255, 255)
        self.g.x = 390
        self.g.y = 250
        self.g.set_font_size(100)

        self.g.set_on_mouse_down_listener(self.click)

    def click(self, sender, event):
        print(sender)
        if event.button == 1:
            self.screen.game.set_screen(HawkProductions.Select.SelectScreen.SelectScreen())


class OverStage2(game.scene2d.MyStage):
    def __init__(self):
        super().__init__()
        pygame.mixer.init()
        pygame.mixer.music.load("../HawkProductions/Music/Over.wav")
        pygame.mixer.music.play(-1)
        self.F = Arial()
        self.add_actor(self.F)
        self.F.set_text("Túl magasra repültél!")
        self.F.x = 500
        self.F.y = 225
        self.F.set_color(204, 0, 0)

        self.g = Arial()
        self.add_actor(self.g)
        self.g.set_text("Try again!")
        self.g.set_color(204, 0, 0)
        self.g.x = 500
        self.g.y = 310

        self.g.set_on_mouse_down_listener(self.click)

    def click(self, sender, event):
        print(sender)
        if event.button == 1:
            self.screen.game.set_screen(HawkProductions.menu.MenuScreen.MenuScreen())
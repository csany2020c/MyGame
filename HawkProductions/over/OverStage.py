from HawkProductions.font.Font import *
import pygame
import HawkProductions.menu.MenuScreen


class OverStage(game.scene2d.MyStage):
    def __init__(self):
        super().__init__()
        pygame.mixer.init()
        pygame.mixer.music.load("../HawkProductions/Music/Over.wav")
        pygame.mixer.music.play(-1)
        #self.c = HawkProductions.Gaymover()
        #self.add_actor(self.c)

        self.F = Gameover()
        self.add_actor(self.F)
        self.F.set_color(255, 0, 0)
        self.F.set_font_size(300)
        self.F.set_text("Game Over")
        self.F.x = 400
        self.F.y = 100

        self.g = Gameover()
        self.add_actor(self.g)
        self.g.set_text("Próbáld újra!")
        self.g.set_color(255, 255, 255)
        self.g.x = 525
        self.g.y = 300
        self.g.set_font_size(100)
        self.g.set_on_mouse_down_listener(self.click)
        self.g.set_on_key_down_listener(self.back_button)

        self.pointl = Gameover("")
        self.update_point()
        self.add_actor(self.pointl)
        self.pointl.set_color(255, 0, 0)
        self.pointl.x = 520
        self.pointl.set_font_size(100)
        self.pointl.y = 645

    def update_point(self):
        f = open("../HawkProductions/eredmenyek/eredmenyek.txt", "r")
        self.score: str = f.readline()
        self.pointl.set_text("Your score: {point}".format(point=self.score))

    def click(self, sender, event):
        print(sender)
        if event.button == 1:
            self.screen.game.set_screen(HawkProductions.Select.SelectScreen.SelectScreen())

    def back_button(self, sender, event):
        print(sender)
        if event.key == pygame.K_SPACE:
            self.screen.game.set_screen(HawkProductions.Select.SelectScreen.SelectScreen())


class OverStage2(game.scene2d.MyStage):
    def __init__(self):
        super().__init__()
        pygame.mixer.init()
        pygame.mixer.music.load("../HawkProductions/Music/Over.wav")
        pygame.mixer.music.play(-1)
        self.F = Gameover()
        self.add_actor(self.F)
        self.F.set_text("Túl magasra szálltál!")
        self.F.x = 100
        self.F.y = 150
        self.F.set_color(255, 255, 255)
        self.F.set_font_size(290)

        self.g = Gameover()
        self.add_actor(self.g)
        self.g.set_text("Try again!")
        self.g.set_color(204, 0, 0)
        self.g.x = 510
        self.g.y = 310
        self.g.set_on_mouse_down_listener(self.click)
        self.g.set_font_size(100)

        self.pointl = Gameover("")
        self.update_point()
        self.add_actor(self.pointl)
        self.pointl.set_color(255, 0, 0)
        self.pointl.x = 500
        self.pointl.set_font_size(100)
        self.pointl.y = 555

    def update_point(self):
        f = open("../HawkProductions/eredmenyek/eredmenyek.txt", "r")
        self.score: str = f.readline()
        self.pointl.set_text("Your score: {point}".format(point=self.score))

    def click(self, sender, event):
        print(sender)
        if event.button == 1:
            self.screen.game.set_screen(HawkProductions.menu.MenuScreen.MenuScreen())


class OverStage3(game.scene2d.MyStage):
    def __init__(self):
        super().__init__()
        pygame.mixer.init()
        pygame.mixer.music.load("../HawkProductions/Music/Over.wav")
        pygame.mixer.music.play(-1)
        self.F = Gameover()
        self.add_actor(self.F)
        self.F.set_text("Túl alacsonyan szálltál!")
        self.F.x = 10
        self.F.y = 150
        self.F.set_color(255, 255, 255)
        self.F.set_font_size(300)

        self.g = Gameover()
        self.add_actor(self.g)
        self.g.set_text("Try again!")
        self.g.set_color(204, 0, 0)
        self.g.x = 510
        self.g.y = 310
        self.g.set_on_mouse_down_listener(self.click)
        self.g.set_font_size(100)

        self.pointl = Gameover("")
        self.update_point()
        self.add_actor(self.pointl)
        self.pointl.set_color(255, 0, 0)
        self.pointl.x = 500
        self.pointl.set_font_size(100)
        self.pointl.y = 555

    def update_point(self):
        f = open("../HawkProductions/eredmenyek/eredmenyek.txt", "r")
        self.score: str = f.readline()
        self.pointl.set_text("Your score: {point}".format(point=self.score))

    def click(self, sender, event):
        print(sender)
        if event.button == 1:
            self.screen.game.set_screen(HawkProductions.menu.MenuScreen.MenuScreen())

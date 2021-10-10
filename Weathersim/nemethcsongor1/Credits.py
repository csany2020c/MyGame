import game
from Font import *
from Weathersim.nemethcsongor1.Actorok import *
import Weathersim.nemethcsongor1.start.SaScreen
import pygame


class CStage(game.scene2d.MyStage):
    def __init__(self):
        super().__init__()
        self.F = Font()
        self.add_actor(self.F)
        self.F.set_text("Készítette Németh Csongor, külön köszönet: Csibész Csabinak.")
        self.F.height = 61.5
        self.F.y = 309

        self.Bb = Bobi()
        self.add_actor(self.Bb)
        self.Bb.width = 150
        self.Bb.x = 575
        self.Bb.y = 20

        self.Zi = Zongi()
        self.add_actor(self.Zi)
        self.Zi.width = 150
        self.Zi.x = 570
        self.Zi.y = 450

        self.Ba = Back()
        self.add_actor(self.Ba)
        self.Ba.set_size(width=250, height=250)
        self.Ba.set_on_mouse_down_listener(self.klikk)

        self.set_on_key_down_listener(self.katt)

    def klikk(self, sender, event):
        print(sender)
        if event.button == 1:
            self.screen.game.set_screen(Weathersim.nemethcsongor1.start.SaScreen.SaScreen())

    def katt(self, sender, event):
        print(sender)
        if event.key == pygame.K_BACKSPACE:
            self.screen.game.set_screen(Weathersim.nemethcsongor1.start.SaScreen.SaScreen())


class CScreen(game.scene2d.MyScreen):
    def __init__(self):
        super().__init__()
        self.add_stage(CStage())
        self.set_background_color(69, 190, 179)

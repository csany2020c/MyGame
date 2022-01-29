import game
import pygame
import kuposztok.Menu.MenuScreen
from kuposztok.options.OptionsActors import *


class OptionsStage(game.scene2d.MyStage):

    def __init__(self):
        super().__init__()
        self.height = pygame.display.get_surface().get_height()
        self.width = pygame.display.get_surface().get_width()
        self.bg = BgActor()
        self.bg.width = self.width
        self.bg.height = self.height
        self.add_actor(self.bg)
        self.sound_max = Sound_Max()
        self.sound_max.set_position(self.width / 5, self.height / 2)
        self.add_actor(self.sound_max)
        self.sound_mid = Sound_Mid()
        self.sound_mid.set_position(self.width / 2.8, self.height / 2)
        self.add_actor(self.sound_mid)
        self.sound_min = Sound_Min()
        self.sound_min.set_position(self.width / 1.7, self.height / 2)
        self.add_actor(self.sound_min)
        self.sound_no = Sound_No()
        self.sound_no.set_position(self.width / 1.3, self.height / 2)
        self.add_actor(self.sound_no)
        self.save = SaveButton()
        self.save.set_position(self.width / 2 - self.save.get_width() / 2, self.height / 1.5)
        self.add_actor(self.save)
        self.soundvalt = 0
        self.valtoztat = False

        self.set_on_key_down_listener(self.Escape)
        self.sound_max.set_on_mouse_down_listener(self.Sound_max)
        self.sound_mid.set_on_mouse_down_listener(self.Sound_mid)
        self.sound_min.set_on_mouse_down_listener(self.Sound_low)
        self.sound_no.set_on_mouse_down_listener(self.Sound_no)
        self.save.set_on_mouse_down_listener(self.savebutton)

    def Escape(self, sender, event):
        if event.key == pygame.K_ESCAPE:
            self.screen.game.set_screen(kuposztok.Menu.MenuScreen.MenuScreen())

    def Sound_max(self, sender, event):
        if event.button == 1:
            self.soundvalt = 1
            self.valtoztat = True

    def Sound_mid(self, sender, event):
        if event.button == 1:
            self.soundvalt = 2
            self.valtoztat = True


    def Sound_low(self, sender, event):
        if event.button == 1:
            self.soundvalt = 3
            self.valtoztat = True


    def Sound_no(self, sender, event):
        if event.button == 1:
            self.soundvalt = 4
            self.valtoztat = True

    def filebaolvasas(self):
        with open('../kuposztok/Save/options.txt', 'r') as file:
            self.soundbe = int(file.readline())
            file.close()

    def filebairas(self):
        with open('../kuposztok/Save/options.txt', 'w') as file:
            if self.valtoztat == False:
                file.write(str(self.soundbe))
            else:
                file.write(str(self.soundvalt))
            file.close()

    def savebutton(self, sender, event):
        if event.button == 1:
            self.filebairas()
            self.screen.game.set_screen(kuposztok.Menu.MenuScreen.MenuScreen())

    def act(self, delta_time: float):
        super().act(delta_time)
        print(self.soundvalt)
        self.filebaolvasas()



import game
import pygame
import kuposztok.Menu.MenuScreen
from kuposztok.options.OptionsActors import *


class OptionsStage(game.scene2d.MyStage):

    def __init__(self):
        super().__init__()
        self.filebaolvasas()
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
        self.optinoslabel = game.scene2d.MyLabel("Hangbeállítások:")
        self.optinoslabel.set_position(self.width / 2 - self.optinoslabel.get_width() * 2, self.height / 2 - self.optinoslabel.get_height() * 2)
        self.optinoslabel.set_color(0, 0, 0)
        self.add_actor(self.optinoslabel)
        self.soundmaxlabel = game.scene2d.MyLabel("100%")
        self.soundmaxlabel.set_position(self.sound_max.get_x(), self.sound_max.get_y() - self.soundmaxlabel.get_height())
        self.soundmaxlabel.set_color(0, 0, 0)
        self.add_actor(self.soundmaxlabel)
        self.soundmidlabel = game.scene2d.MyLabel("50%")
        self.soundmidlabel.set_position(self.sound_mid.get_x(), self.sound_mid.get_y() - self.soundmidlabel.get_height())
        self.soundmidlabel.set_color(0, 0, 0)
        self.add_actor(self.soundmidlabel)
        self.soundminlabel = game.scene2d.MyLabel("25%")
        self.soundminlabel.set_position(self.sound_min.get_x(), self.sound_min.get_y() - self.soundminlabel.get_height())
        self.soundminlabel.set_color(0, 0, 0)
        self.add_actor(self.soundminlabel)
        self.mutelabel = game.scene2d.MyLabel("Mute")
        self.mutelabel.set_position(self.sound_no.get_x(), self.sound_no.get_y() - self.mutelabel.get_height())
        self.mutelabel.set_color(0, 0, 0)
        self.add_actor(self.mutelabel)
        self.musicaselect = 0
        self.musica1label = game.scene2d.MyLabel("8 Bit / Dungeon Boss")
        self.musica1label.set_position(self.width / 5 - self.musica1label.get_width() / 2, self.height / 7)
        self.musica1label.set_color(0, 0, 0)
        self.add_actor(self.musica1label)
        self.musica2label = game.scene2d.MyLabel("Mountain Trials")
        self.musica2label.set_position(self.width / 5 - self.musica2label.get_width() / 2, self.height / 5)
        self.musica2label.set_color(0, 0, 0)
        self.add_actor(self.musica2label)
        self.musica3label = game.scene2d.MyLabel("Pixelland")
        self.musica3label.set_position(self.width / 2 - self.musica3label.get_width() / 2, self.height / 7)
        self.musica3label.set_color(0, 0, 0)
        self.add_actor(self.musica3label)
        self.musica4label = game.scene2d.MyLabel("Digestive biscui")
        self.musica4label.set_position(self.width / 2 - self.musica4label.get_width() / 2, self.height / 5)
        self.musica4label.set_color(0, 0, 0)
        self.add_actor(self.musica4label)
        self.musica5label = game.scene2d.MyLabel("8 Bit / Itty Bitty")
        self.musica5label.set_position(self.width / 1.5, self.height / 7)
        self.musica5label.set_color(0, 0, 0)
        self.add_actor(self.musica5label)
        self.soundben =self.soundbe
        self.select = Select()
        self.select.set_size(150, 125)
        if self.soundben == 1 or self.soundben == 0:
            self.select.set_position(self.sound_max.get_x(), self.sound_max.get_y())
        if self.soundben == 2:
            self.select.set_position(self.sound_mid.get_x(), self.sound_mid.get_y())
        if self.soundben == 3:
            self.select.set_position(self.sound_min.get_x(), self.sound_min.get_y())
        if self.soundben == 4:
            self.select.set_position(self.sound_no.get_x(), self.sound_no.get_y())
        self.add_actor(self.select)
        self.musicaselectkep = Select()
        self.musicaselectkep.set_size(150, 125)
        if self.musicaselect == 1 or self.musicaselect == 0:
            self.musicaselectkep.set_position(self.musica1label.get_x() - 10, self.musica1label.get_y())
            self.musicaselectkep.set_size(self.musica1label.get_width() + 20, self.musica1label.get_height())
        if self.musicaselect == 2:
            self.musicaselectkep.set_position(self.musica2label.get_x() - 10, self.musica2label.get_y())
            self.musicaselectkep.set_size(self.musica2label.get_width() + 20, self.musica2label.get_height())
        if self.musicaselect == 3:
            self.musicaselectkep.set_position(self.musica3label.get_x() - 10, self.musica3label.get_y())
            self.musicaselectkep.set_size(self.musica3label.get_width() + 20, self.musica3label.get_height())
        if self.musicaselect == 4:
            self.musicaselectkep.set_position(self.musica4label.get_x() - 10, self.musica4label.get_y())
            self.musicaselectkep.set_size(self.musica4label.get_width() + 20, self.musica4label.get_height())
        if self.musicaselect == 5:
            self.musicaselectkep.set_position(self.musica5label.get_x() - 10, self.musica5label.get_y())
            self.musicaselectkep.set_size(self.musica5label.get_width() + 20, self.musica5label.get_height())
        self.add_actor(self.musicaselectkep)

        self.set_on_key_down_listener(self.Escape)
        self.sound_max.set_on_mouse_down_listener(self.Sound_max)
        self.sound_mid.set_on_mouse_down_listener(self.Sound_mid)
        self.sound_min.set_on_mouse_down_listener(self.Sound_low)
        self.sound_no.set_on_mouse_down_listener(self.Sound_no)
        self.musica1label.set_on_mouse_down_listener(self.gamemusica1)
        self.musica2label.set_on_mouse_down_listener(self.gamemusica2)
        self.musica3label.set_on_mouse_down_listener(self.gamemusica3)
        self.musica4label.set_on_mouse_down_listener(self.gamemusica4)
        self.musica5label.set_on_mouse_down_listener(self.gamemusica5)
        self.save.set_on_mouse_down_listener(self.savebutton)

    def Escape(self, sender, event):
        if event.key == pygame.K_ESCAPE:
            self.screen.game.set_screen(kuposztok.Menu.MenuScreen.MenuScreen())

    def Sound_max(self, sender, event):
        if event.button == 1:
            self.soundvalt = 1
            self.valtoztat = True
            self.select.set_position(self.sound_max.get_x(), self.sound_max.get_y())

    def Sound_mid(self, sender, event):
        if event.button == 1:
            self.soundvalt = 2
            self.valtoztat = True
            self.select.set_position(self.sound_mid.get_x(), self.sound_mid.get_y())


    def Sound_low(self, sender, event):
        if event.button == 1:
            self.soundvalt = 3
            self.valtoztat = True
            self.select.set_position(self.sound_min.get_x(), self.sound_min.get_y())

    def Sound_no(self, sender, event):
        if event.button == 1:
            self.soundvalt = 4
            self.valtoztat = True
            self.select.set_position(self.sound_no.get_x(), self.sound_no.get_y())

    def gamemusica1(self, sender, event):
        if event.button == 1:
            self.musicaselect = 1
            self.musicaselectkep.set_position(self.musica1label.get_x() - 10, self.musica1label.get_y())
            self.musicaselectkep.set_size(self.musica1label.get_width() + 20, self.musica1label.get_height())

    def gamemusica2(self, sender, event):
        if event.button == 1:
            self.musicaselect = 2
            self.musicaselectkep.set_position(self.musica2label.get_x() - 10, self.musica2label.get_y())
            self.musicaselectkep.set_size(self.musica2label.get_width() + 20, self.musica2label.get_height())

    def gamemusica3(self, sender, event):
        if event.button == 1:
            self.musicaselect = 3
            self.musicaselectkep.set_position(self.musica3label.get_x() - 10, self.musica3label.get_y())
            self.musicaselectkep.set_size(self.musica3label.get_width() + 20, self.musica3label.get_height())

    def gamemusica4(self, sender, event):
        if event.button == 1:
            self.musicaselect = 4
            self.musicaselectkep.set_position(self.musica4label.get_x() - 10, self.musica4label.get_y())
            self.musicaselectkep.set_size(self.musica4label.get_width() + 20, self.musica4label.get_height())

    def gamemusica5(self, sender, event):
        if event.button == 1:
            self.musicaselect = 5
            self.musicaselectkep.set_position(self.musica5label.get_x() - 10, self.musica5label.get_y())
            self.musicaselectkep.set_size(self.musica5label.get_width() + 20, self.musica5label.get_height())

    def filebaolvasas(self):
        with open('../kuposztok/Save/options.txt', 'r') as file:
            self.soundbe = int(file.readline())
            self.musica = int(file.readline())
            file.close()

    def filebairas(self):
        with open('../kuposztok/Save/options.txt', 'w') as file:
            if self.valtoztat == False:
                file.write(str(self.soundbe))
            else:
                file.write(str(self.soundvalt))
            file.write('\n' + str(self.musicaselect))
            file.close()

    def savebutton(self, sender, event):
        if event.button == 1:
            self.filebairas()
            self.screen.game.set_screen(kuposztok.Menu.MenuScreen.MenuScreen())

    def act(self, delta_time: float):
        super().act(delta_time)
        print(self.soundvalt)




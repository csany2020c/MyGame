import game
import pygame
from Weathersim.kollarbalint.IdoActors import *
from Weathersim.kollarbalint.IdoSzoveg import *
from Weathersim.kollarbalint.IdoScreen import *
import Weathersim.kollarbalint.IdoScreen
import Weathersim.kollarbalint.IdoActors
import Weathersim.kollarbalint.IdoSzoveg
import random
from game.scene2d import MyTickTimer


class NapsutesStage(game.scene2d.MyStage):

    def __init__(self):
        super().__init__()
        self.NapActor1 = SunnyImg()
        self.add_actor(self.NapActor1)
        self.NapActor2 = SunImg()
        self.add_actor(self.NapActor2)
        self.NapActor3 = LandscapeImg()
        self.add_actor(self.NapActor3)
        self.NapActor2.x += 850
        self.NapActor2.y += -110

    def act(self, delta_time: float):
        super().act(delta_time)
        self.NapActor2.rotate_with(delta_time * 25)
        if self.elapsed_time > 0:
            self.NapActor2.x -= delta_time * 75
        if self.elapsed_time > 6:
            self.NapActor2.x += delta_time * 150
        if self.elapsed_time > 13:
            self.NapActor2.x -= delta_time * 150
        if self.elapsed_time > 20:
            self.NapActor2.x += delta_time * 150
        if self.elapsed_time > 25:
            self.NapActor2.x -= delta_time * 75




class EsoStage(game.scene2d.MyStage):

    def __init__(self):
        super().__init__()
        self.EsoA = CloudyImg()
        self.add_actor(self.EsoA)
        self.EsoA2 = LandscapeImg()
        self.add_actor(self.EsoA2)
        self.EsoCS = RainImg()
        self.add_actor(self.EsoCS)
        self.EsoCS2 = RainImg()
        self.add_actor(self.EsoCS2)
        self.EsoCS3 = RainImg()
        self.add_actor(self.EsoCS3)
        self.EsoCS4 = RainImg()
        self.add_actor(self.EsoCS4)
        self.EsoCS5 = RainImg()
        self.add_actor(self.EsoCS5)
        self.EsoCS.x += 620
        self.EsoCS.y += 100
        self.EsoCS2.x += 700
        self.EsoCS2.y += 190
        self.EsoCS3.x += 810
        self.EsoCS3.y += 140
        self.EsoCS4.x += 900
        self.EsoCS4.y += 270
        self.EsoCS5.x += 1100
        self.EsoCS5.y += 120

    def act(self, delta_time: float):
        super().act(delta_time)
        if self.elapsed_time > 0:
            self.EsoCS.y += delta_time * 15
            self.EsoCS2.y += delta_time * 14
            self.EsoCS3.y += delta_time * 15
            self.EsoCS4.y += delta_time * 16
            self.EsoCS5.y += delta_time * 13


class HavazasStage(game.scene2d.MyStage):

    def __init__(self):
        super().__init__()
        self.HavA = CloudyImg()
        self.add_actor(self.HavA)
        self.HavA2 = LandscapeImg()
        self.add_actor(self.HavA2)
        self.timer = MyTickTimer(interval=0.25, func=self.idocucc)
        self.add_timer(self.timer)

    def idocucc(self, sender):
        self.Ho = (SnowImg())
        self.add_actor(self.Ho)
        self.Ho.x = random.Random().randint(-150, 1150)


    def key_down(self, sender, event):
        print(sender)
        print(event)
        if event.key == pygame.K_ESCAPE:
            print("'QUIT'")
            quit()

class HavasesoStage(game.scene2d.MyStage):

    def __init__(self):
        super().__init__()
        self.Hatter = CloudyImg()
        self.add_actor(self.Hatter)
        self.Hatter2 = LandscapeImg()
        self.add_actor(self.Hatter2)
        self.Ho = SnowImg()
        self.add_actor(self.Ho)
        self.Eso = RainImg()
        self.add_actor(self.Eso)
        self.EsoA = CloudyImg()
        self.add_actor(self.EsoA)
        self.EsoA2 = LandscapeImg()
        self.add_actor(self.EsoA2)
        self.EsoCS = RainImg()
        self.add_actor(self.EsoCS)
        self.EsoCS2 = RainImg()
        self.add_actor(self.EsoCS2)
        self.EsoCS3 = RainImg()
        self.add_actor(self.EsoCS3)
        self.EsoCS4 = RainImg()
        self.add_actor(self.EsoCS4)
        self.EsoCS5 = RainImg()
        self.add_actor(self.EsoCS5)
        self.EsoCS6 = RainImg()
        self.add_actor(self.EsoCS6)
        self.EsoCS7 = RainImg()
        self.add_actor(self.EsoCS7)
        self.EsoCS8 = RainImg()
        self.add_actor(self.EsoCS8)
        self.EsoCS.x += 620
        self.EsoCS.y += 100
        self.EsoCS2.x += 700
        self.EsoCS2.y += 190
        self.EsoCS3.x += 810
        self.EsoCS3.y += 140
        self.EsoCS4.x += 900
        self.EsoCS4.y += 270
        self.EsoCS5.x += 1100
        self.EsoCS5.y += 280
        self.EsoCS6.x += 110
        self.EsoCS6.y += 240
        self.EsoCS7.x += 250
        self.EsoCS7.y += 230
        self.EsoCS8.x += 500
        self.EsoCS8.y += 200
        self.timer = MyTickTimer(interval=0.5, func=self.idocucc)
        self.add_timer(self.timer)


    def idocucc(self, sender):
        self.Ho = (SnowImg())
        self.add_actor(self.Ho)
        self.Ho.x = random.Random().randint(-150, 1150)

    def act(self, delta_time: float):
        super().act(delta_time)
        if self.elapsed_time > 0:
            self.EsoCS.y += delta_time * 15
            self.EsoCS2.y += delta_time * 14
            self.EsoCS3.y += delta_time * 15
            self.EsoCS4.y += delta_time * 16
            self.EsoCS5.y += delta_time * 13
            self.EsoCS6.y += delta_time * 15
            self.EsoCS7.y += delta_time * 14
            self.EsoCS8.y += delta_time * 15

class MenuStage(game.scene2d.MyStage):

    def __init__(self):
        super().__init__()
        self.felho = FelhoImg()
        self.add_actor(self.felho)
        self.felho.x += -10
        self.felho.y += 0
        self.felho.set_width(280)
        self.felho.set_height(280)
        self.felho2 = FelhoImg()
        self.add_actor(self.felho2)
        self.felho2.x += 950
        self.felho2.y += 0
        self.felho2.set_width(280)
        self.felho2.set_height(280)
        self.Kilep = MenuSzoveg()
        self.add_actor(self.Kilep)
        self.Kilep.set_text("Kilépés")
        self.Kilep.set_alpha(500)
        self.Kilep.set_width(65)
        self.Kilep.set_height(65)
        self.Kilep.x += 530
        self.Kilep.y += 515
        self.Kilep.set_on_mouse_down_listener(self.click)
        self.szoveg = MenuSzoveg()
        self.add_actor(self.szoveg)
        self.szoveg.set_text("Időjárás Szimulátor")
        self.szoveg.set_alpha(500)
        self.szoveg.set_width(80)
        self.szoveg.set_height(80)
        self.szoveg.x += 360
        self.szoveg.y += 50
        self.Jatek = MenuSzoveg()
        self.add_actor(self.Jatek)
        self.Jatek.set_text("Játék")
        self.Jatek.set_alpha(500)
        self.Jatek.set_width(65)
        self.Jatek.set_height(65)
        self.Jatek.x += 550
        self.Jatek.y += 240
        self.Jatek.set_on_mouse_down_listener(self.play)
        self.infosz = MenuSzoveg()
        self.add_actor(self.infosz)
        self.infosz.set_text("Info")
        self.infosz.set_alpha(500)
        self.infosz.set_width(65)
        self.infosz.set_height(65)
        self.infosz.x += 575
        self.infosz.y += 325
        self.infosz.set_on_mouse_down_listener(self.infogomb)
        self.fullscreen = MenuSzoveg()
        self.add_actor(self.fullscreen)
        self.fullscreen.set_text("FullScreen")
        self.fullscreen.set_alpha(500)
        self.fullscreen.set_width(65)
        self.fullscreen.set_height(65)
        self.fullscreen.x += 490
        self.fullscreen.y += 420
        self.fullscreen.set_on_mouse_down_listener(self.fullscreengomb)



    def click(self, sender, event):
        print(sender)
        print(event)
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                print("'QUIT'")
                quit()

    def play(self,sender,event):
        print(sender)
        print(event)
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                self.screen.game.set_screen(Weathersim.kollarbalint.IdoScreen.NapsutesScr())
                print("'PLAY'")

    def infogomb(self, sender, event):
        print(sender)
        print(event)
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                self.screen.game.set_screen(Weathersim.kollarbalint.IdoScreen.InfoScr())
                print("'INFO'")

    def fullscreengomb(self, sender, event):
        print(sender)
        print(event)
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                print("'FULLSCREEN'")
                pygame.display.toggle_fullscreen()



class InfoStage(game.scene2d.MyStage):

    def __init__(self):
        super().__init__()
        self.infoa = MenuSzoveg()
        self.add_actor(self.infoa)
        self.infoa.set_text("BACKSPACE = Menübe való visszatérés")
        self.infoa.set_alpha(500)
        self.infoa.set_width(45)
        self.infoa.set_height(45)
        self.infoa.x += 320
        self.infoa.y += 330
        self.infob = MenuSzoveg()
        self.add_actor(self.infob)
        self.infob.set_text("ESC = Játékból való kilépés")
        self.infob.set_alpha(500)
        self.infob.set_width(45)
        self.infob.set_height(45)
        self.infob.x += 320
        self.infob.y += 390
        self.infoc = MenuSzoveg()
        self.add_actor(self.infoc)
        self.infoc.set_text("Információ")
        self.infoc.set_alpha(500)
        self.infoc.set_width(85)
        self.infoc.set_height(85)
        self.infoc.x += 475
        self.infoc.y += 40
        self.infod = MenuSzoveg()
        self.add_actor(self.infod)
        self.infod.set_text("13 másodpercenként változik az időjárás")
        self.infod.set_alpha(500)
        self.infod.set_width(45)
        self.infod.set_height(45)
        self.infod.x += 320
        self.infod.y += 270
        self.infoe = MenuSzoveg()
        self.add_actor(self.infoe)
        self.infoe.set_text("1, 2, 3, 4 = Gombokkal váltható az időjárás")
        self.infoe.set_alpha(500)
        self.infoe.set_width(45)
        self.infoe.set_height(45)
        self.infoe.x += 320
        self.infoe.y += 450
        self.infof = MenuSzoveg()
        self.add_actor(self.infof)
        self.infof.set_text("5 = Szimuláció vége")
        self.infof.set_alpha(500)
        self.infof.set_width(45)
        self.infof.set_height(45)
        self.infof.x += 320
        self.infof.y += 515
        self.infok = MenuSzoveg()
        self.add_actor(self.infok)
        self.infok.set_text("F11 = FULLSCREEN")
        self.infok.set_alpha(500)
        self.infok.set_width(45)
        self.infok.set_height(45)
        self.infok.x += 320
        self.infok.y += 580



class EndStage(game.scene2d.MyStage):

    def __init__(self):
        super().__init__()
        self.szoveg = MenuSzoveg()
        self.add_actor(self.szoveg)
        self.szoveg.set_text("A szimuláció vége")
        self.szoveg.set_alpha(500)
        self.szoveg.set_width(75)
        self.szoveg.set_height(75)
        self.szoveg.x += 365
        self.szoveg.y += 75
        self.menu = MenuSzoveg()
        self.add_actor(self.menu)
        self.menu.set_text("Menü")
        self.menu.set_alpha(500)
        self.menu.set_width(65)
        self.menu.set_height(65)
        self.menu.x += 560
        self.menu.y += 350
        self.menu.set_on_mouse_down_listener(self.menugomb)

    def menugomb(self, sender, event):
        print(sender)
        print(event)
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                self.screen.game.set_screen(Weathersim.kollarbalint.IdoScreen.MenuScr())
                print("'MENÜ'")


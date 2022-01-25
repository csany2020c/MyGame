import game
from Nike.NikeScreen import *
from Nike.NikeActor import *
import Nike.NikeScreen
import random
import pygame
from game.simpleworld.ShapeType import ShapeType
from game.scene2d import MyPermanentTimer, MyOneTickTimer, MyBaseActor, MyTickTimer, MyIntervalTimer

class MenuStage(game.scene2d.MyStage):
    def __init__(self):
        super().__init__()
        self.FatJordan = FatJordan()
        self.add_actor(FatJordan())
        self.text = MenuText()
        self.add_actor(self.text)
        self.text.set_text("Fat Jordan")
        self.text.set_alpha(500)
        self.text.set_width(80)
        self.text.set_height(80)
        self.text.x += 500
        self.text.y += 150
        self.start = MenuText()
        self.add_actor(self.start)
        self.start.set_text("Start")
        self.start.set_alpha(500)
        self.start.set_width(80)
        self.start.set_height(80)
        self.start.x += 300
        self.start.y += 250
        self.start.set_on_mouse_down_listener(self.play)
        self.exit = MenuText()
        self.add_actor(self.exit)
        self.exit.set_text("Exit")
        self.exit.set_alpha(500)
        self.exit.set_width(80)
        self.exit.set_height(80)
        self.exit.x += 850
        self.exit.y += 250
        self.exit.set_on_mouse_down_listener(self.exitbut)
        self.credit = MenuText()
        self.add_actor(self.credit)
        self.credit.set_text("Credit")
        self.credit.set_alpha(500)
        self.credit.set_width(80)
        self.credit.set_height(80)
        self.credit.x += 550
        self.credit.y += 550
        self.credit.set_on_mouse_down_listener(self.creditbut)
        self.info = Info()
        self.add_actor(self.info)
        self.info.set_alpha(200)
        self.info.set_width(80)
        self.info.set_height(80)
        self.info.x += 350
        self.info.y += 300
        self.info.set_on_mouse_down_listener(self.infobut)


    def play(self, sender, event):
        print(sender)
        print(event)
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                self.screen.game.set_screen(Nike.NikeScreen.Game())

    def exitbut(self, sender, event):
        print(sender)
        print(event)
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                quit()

    def creditbut(self, sender, event):
        print(sender)
        print(event)
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                self.screen.game.set_screen(Nike.NikeScreen.Credit())

    def infobut(self, sender, event):
        print(sender)
        print(event)
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                self.screen.game.set_screen(Nike.NikeScreen.Info())



class CreditStage(game.scene2d.MyStage):
    def __init__(self):
        super().__init__()
        self.creators = MenuText()
        self.add_actor(self.creators)
        self.creators.set_text("Creators:")
        self.creators.set_alpha(500)
        self.creators.set_width(80)
        self.creators.set_height(80)
        self.creators.x += 500
        self.creators.y += 50
        self.akos = MenuText()
        self.add_actor(self.akos)
        self.akos.set_text("Tóth Ákos")
        self.akos.set_alpha(500)
        self.akos.set_width(80)
        self.akos.set_height(80)
        self.akos.x += 500
        self.akos.y += 150
        self.mate = MenuText()
        self.add_actor(self.mate)
        self.mate.set_text("Vizdák Máté")
        self.mate.set_alpha(500)
        self.mate.set_width(80)
        self.mate.set_height(80)
        self.mate.x += 470
        self.mate.y += 220
        self.donat = MenuText()
        self.add_actor(self.donat)
        self.donat.set_text("Rigó Donát")
        self.donat.set_alpha(500)
        self.donat.set_width(80)
        self.donat.set_height(80)
        self.donat.x += 480
        self.donat.y += 290
        self.back = MenuText()
        self.add_actor(self.back)
        self.back.set_text("Back")
        self.back.set_alpha(500)
        self.back.set_width(80)
        self.back.set_height(80)
        self.back.x += 560
        self.back.y += 600
        self.back.set_on_mouse_down_listener(self.backbut)
        self.mate.set_on_mouse_down_listener(self.letsgo)

    def backbut(self, sender, event):
        print(sender)
        print(event)
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                self.screen.game.set_screen(Nike.NikeScreen.Menu())

    def letsgo(self, sender, event):
        print(sender)
        print(event)
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                pygame.mixer.music.load("sounds/letsgo.wav")
                pygame.mixer.music.play()
                pygame.mixer.music.set_volume(50)




class GameStage(game.scene2d.MyStage):
    def __init__(self):
        super().__init__()
        self.set_on_key_down_listener(self.backtomenu)
        self.GameBg =GameBg()
        self.add_actor(self.GameBg)
        self.GameBg2 = GameBg2()
        self.add_actor(self.GameBg2)
        self.Sztrit = Sztrit()
        self.add_actor(self.Sztrit)
        self.FatJordanact = FatJordanact()
        self.add_actor(self.FatJordanact)
        self.LeBron = LeBron()
        self.aventador = aventador()
        self.add_actor(self.aventador)
        self.house = house()
        self.add_actor(self.house)


        self.camera.set_tracking(self.FatJordanact)
        self.FatJordanact.set_on_key_press_listener(self.press)

        self.t = game.scene2d.MyTickTimer(interval=2 , func=self.tikk)
        self.add_timer(self.t)

    def tikk(self, sender):

        for j in range(1):
            self.LeBron = LeBron()
            self.add_actor(self.LeBron)
            self.LeBron.y = 500
            self.LeBron.x = 3800




    def press(self, sender, event):
        if self.FatJordanact.y == 450:
            if event.key == pygame.K_w:
                sender.y = 100
                pygame.mixer.music.load("sounds/jump.wav")
                pygame.mixer.music.play()
                pygame.mixer.music.set_volume(0.2)
        if sender.y == 500:
            sender.y += 0
        if event.key == pygame.K_d:
            sender.x += 5
            self.camera.set_tracking_window(0.2, 0.2, 0.7, -0.2)



    def act(self, delta_time: float):
        super().act(delta_time)
        print(self.FatJordanact)
        if self.LeBron.overlaps(other=self.FatJordanact):
            self.screen.game.set_screen(Nike.NikeScreen.Lose())
            pygame.mixer.music.load("sounds/lose.wav")
            pygame.mixer.music.play()
            pygame.mixer.music.set_volume(100)
        if self.elapsed_time > 0:
            self.FatJordanact.y += delta_time * 250
        if self.FatJordanact.y > 450:
            self.FatJordanact.y = 450
        if self.aventador.overlaps(other=self.FatJordanact):
            self.screen.game.set_screen(Nike.NikeScreen.Win())
            pygame.mixer.music.load("sounds/win.wav")
            pygame.mixer.music.play()
            pygame.mixer.music.set_volume(100)



    def backtomenu(self,sender,event):
        if event.key == pygame.K_ESCAPE:
            self.screen.game.set_screen(Nike.NikeScreen.Menu())

class WinStage(game.scene2d.MyStage):
    def __init__(self):
        super().__init__()
        self.win = win()
        self.add_actor(self.win)



class LoseStage(game.scene2d.MyStage):
    def __init__(self):
        super().__init__()
        self.lose = lose()
        self.add_actor(self.lose)

class InfoStage(game.scene2d.MyStage):
    def __init__(self):
        super().__init__()
        self.info = Info()
        self.add_actor(self.info)
        self.info.set_text("Infooo")
        self.info.set_alpha(500)
        self.info.set_width(80)
        self.info.set_height(80)
        self.info.x += 500
        self.info.y += 50
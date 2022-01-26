import game
import pygame
from game.scene2d import MyTickTimer
import webbrowser
from Impostorsus.Game.WarioActor import *
from game.scene2d import MyBaseActor
import Impostorsus.Game.WarioScr
import sys
class ASD(game.scene2d.MyStage):

    def __init__(self):
        super().__init__()
        pygame.mouse.set_visible(0)
        # # for i in range(100):
        # #     h = HatterActor1()
        # #     h.x = i * h.w + -150
        # #     self.add_actor(h)
        # self.add_actor(HatterActor1())
        f = open("palya2.txt", "r")

        y: int = 0
        while True:
            line = f.readline().strip()
            if line:
                x: int = 0
                for c in line:
                    a: MyBaseActor = None
                    a1: MyBaseActor = None
                    a2: MyBaseActor = None
                    a3: MyBaseActor = None
                    a4: MyBaseActor = None
                    if c == "y":
                        a = Kocka()
                    if c == "b":
                        a = BillActor()
                    if c == "o":
                        a = Kocka()
                        a1 = Lathatatlan()
                    if c == "p":
                        a = Kocka()
                        a2 = Lathatatlan2()
                    if c == "B":
                        a = CannonActor()
                    if c == "g":
                        a = GroundActor()
                    if c == "j":
                        a = GroundActor()
                        a3 = Lathatatlan3()
                    if c == "k":
                        a = GroundActor()
                        a4 = Lathatatlan4()
                    if c == "l":
                        a = Ground2Actor()
                    if c == "x":
                        a = InvisActor()
                    if c == "S":
                        a = Tabla()
                    if c == "z":
                        a = Zaszlo()
                    if c == "W":
                        self.wario = WarioActor()
                        a = self.wario
                        a1 = self.wario
                        a2 = self.wario
                        a3 = self.wario
                        a4 = self.wario
                    if a is not None:
                        a.x = x * 64
                        a.y = y * 64
                        self.add_actor(a)
                    if a1 is not None:
                        a1.x = x * 64
                        a1.y = y * 64
                        self.add_actor(a1)
                    if a2 is not None:
                        a2.x = x * 64
                        a2.y = y * 64
                        self.add_actor(a2)
                    if a3 is not None:
                        a3.x = x * 64
                        a3.y = y * 64
                        self.add_actor(a3)
                    if a4 is not None:
                        a4.x = x * 64
                        a4.y = y * 64
                        self.add_actor(a4)
                        print(c)
                    x += 1
            else:
                break
            y += 1

        f.close()

        # self.kocka = Kocka()
        # self.add_actor(self.kocka)
        # self.kocka.x = 250
        # self.kocka.y = 350
        # self.kerdo = Question()
        # self.gomba = Gemba()
        # self.add_actor(self.kerdo)
        # self.kerdo.x = 200
        # self.kerdo.y = 350
        # self.wario = WarioActor()
        self.camera.tracking = self.wario
        # self.add_actor(self.wario)
        self.wario.set_on_key_press_listener(self.press)
        self.wario.set_on_key_down_listener(self.key_down)
        #
        #
        # for i in range(100):
        #     g = GroundActor()
        #     g.y = 615
        #     g.x = i * g.w + -150
        #     self.add_actor(g)
        self.sz = MenuSzoveg()
        self.add_actor(self.sz)
        self.sz.set_text("Nyomj")
        self.sz.set_alpha(500)
        self.sz.set_width(25)
        self.sz.set_height(25)
        self.sz.x += 3410
        self.sz.y += 715
        self.sz2 = MenuSzoveg()
        self.add_actor(self.sz2)
        self.sz2.set_text("E-t")
        self.sz2.set_alpha(500)
        self.sz2.set_width(25)
        self.sz2.set_height(25)
        self.sz2.x += 3430
        self.sz2.y += 740
        self.t = MyTickTimer(interval=2.3, func=self.tikk)
        self.add_timer(self.t)
        self.t2 = MyTickTimer(interval=0.4, func=self.tikk2)
        self.add_timer(self.t2)
        self.t3 = MyTickTimer(interval=0.8, func=self.tikk3)
        self.add_timer(self.t3)
        self.q = Question()
        self.add_actor(self.q)
        self.q.y = 320
        self.q.x = 2900


    def tikk(self, sender):
        self.b = BillActor()
        self.add_actor(self.b)
        self.b.x = +1100
        self.b.y = +700

    def tikk2(self, sender):
        self.wario.image_url = 'Kepek/actorsusus.png'

    def tikk3(self, sender):
        self.wario.image_url = 'Kepek/actorsusus2.png'



    def press(self, sender, event):
        # print(event.key)
        if event.key == pygame.K_d:
            sender.x += 10
            self.camera.set_tracking_window(0.2, 0.2, 0.7, -0.2)
        if event.key == pygame.K_a:
            sender.x -= 10
            self.wario.image_url = 'Kepek/actorsusus3.png'
            self.camera.set_tracking_window(0.4, 0.2, 0.2, -0.2)
        if event.key == pygame.K_RIGHT:
            sender.x += 10
            self.camera.set_tracking_window(0.2, 0.2, 0.7, -0.2)
        if event.key == pygame.K_LEFT:
            sender.x -= 10
            self.camera.set_tracking_window(0.4, 0.2, 0.2, -0.2)


    def interval(self, sender):
        self.wario.x += 100 * self.get_delta_time()
        self.gomba.x += 100 * self.get_delta_time()
        pass

    def key_down(self, sender, event):
        jump_fx = pygame.mixer.Sound("audio/jumpsound.mp3")
        jump_fx.set_volume(0.015)
        print(sender)
        print(event)
        if event.key == pygame.K_w:
            print("'hoppáré'")
            self.wario.ugras()
            jump_fx.play()

        if event.key == pygame.K_SPACE:
            print("'hoppáré'")
            self.wario.ugras()
            jump_fx.play()
        if event.key == pygame.K_UP:
            print("'hoppáré'")
            self.wario.ugras()
            jump_fx.play()
        if event.key == pygame.K_e:
            pygame.mixer.music.load("audio/jebait.mp3")
            pygame.mixer.music.play()
            pygame.mixer.music.set_volume(0.04)
            self.screen.game.set_screen(Impostorsus.Game.WarioScr.WarioScr())


    def act(self, delta_time: float):
        super().act(delta_time)
        overlapsASD: bool = False
        overASD: bool = False
        dead_fx = pygame.mixer.Sound("audio/battya.mp3")
        dead_fx.set_volume(0.04)
        win_fx = pygame.mixer.Sound("audio/winsound.mp3")
        win_fx.set_volume(0.04)

        g = None
        for actorASD in self.actors:
            if isinstance(actorASD, Gemba):
                if actorASD.elapsed_time > 0.5:
                    if self.wario.overlaps(actorASD):
                        # self.gomba = Gemba()
                        self.wario.set_height(200)
                        self.wario.set_width(200)
                        g = actorASD
            if isinstance(actorASD, Kocka):
                if actorASD.y - actorASD.h > self.wario.y:
                    if self.wario.overlaps(actorASD):
                        overlapsASD = True
                        break
            if isinstance(actorASD, GroundActor):
                if self.wario.overlaps(actorASD):
                    overlapsASD = True
                    break
            if isinstance(actorASD, CannonActor):
                if self.wario.overlaps(actorASD):
                    overlapsASD = True
                    break

            if isinstance(actorASD, InvisActor):
                if self.wario.overlaps(actorASD):
                    overASD = True
                    break
            if isinstance(actorASD, Kocka):
                if self.wario.overlaps(actorASD):
                    self.wario.y += 7.5
            if isinstance(actorASD, Lathatatlan):
                if self.wario.overlaps(actorASD):
                    self.wario.x -= 12
            if isinstance(actorASD, Lathatatlan2):
                if self.wario.overlaps(actorASD):
                    self.wario.x += 12
            if isinstance(actorASD, Lathatatlan3):
                if self.wario.overlaps(actorASD):
                    self.wario.x -= 12
            if isinstance(actorASD, Lathatatlan4):
                if self.wario.overlaps(actorASD):
                    self.wario.x += 12
            if isinstance(actorASD, BillActor):
                if self.wario.overlaps(actorASD):
                    dead_fx.play()
                    self.screen.game.set_screen(Impostorsus.Game.WarioScr.HalalScreen())
            if isinstance(actorASD, Zaszlo):
                if self.wario.overlaps(actorASD):
                    win_fx.play()
                    self.screen.game.set_screen(Impostorsus.Game.WarioScr.WinScreen())
            if isinstance(actorASD, Question):
                if self.wario.overlaps(actorASD):
                    self.remove_actor(self.q)
                    self.k = KunuM()
                    self.add_actor(self.k)
                    self.k.x = 2850
                    self.k.y = 900


            if g is not None:
                g.remove_from_stage()
        #
        # for actorASD in self.actors:
        #     if isinstance(actorASD, GroundActor):
        #         if self.gomba.overlaps(actorASD):
        #             overlapsASD = True
        #             break
        # if overlapsASD:
        #     self.gomba.stop()
        # else:
        #     self.gomba.start()
        #
        # for actorASD in self.actors:
        #     if isinstance(actorASD, Question):
        #         if self.wario.overlaps(actorASD):
        #             overlapsASD = True
        #             break
        # if overlapsASD:
        #     self.wario.stop()
        #     self.add_actor(self.gomba)
        #     self.gomba.x += 200
        #     self.gomba.y += 400
        #     self.remove_actor(self.kerdo)
        #
        # else:
        #     self.wario.start()
        #
        # for actorASD in self.actors:
        #     if isinstance(actorASD, Kocka):
        #         if self.wario.overlaps(actorASD):
        #             overlapsASD = True
        #             break
        # if overlapsASD:
        #     self.wario.stop()
        # else:
        #     self.wario.start()
        #
        # for actorASD in self.actors:
        #     if isinstance(actorASD, GroundActor):
        #         if self.wario.overlaps(actorASD):
        #             overlapsASD = True
        #             break
        if overlapsASD:
            self.wario.stop()
        else:
            self.wario.start()

        if overASD:
            dead_fx.play()
            self.screen.game.set_screen(Impostorsus.Game.WarioScr.HalalScreen())


class ASD2 (game.scene2d.MyStage):
    def __init__(self):
        super().__init__()
        pygame.mixer.music.load('audio/rajosan.mp3')
        pygame.mixer.music.play()
        pygame.mixer.music.set_volume(0.03)
        pygame.mouse.set_visible(10)
        self.b = BackGround()
        self.add_actor(self.b)
        self.b.x += 0
        self.b.y += 0
        self.p = Play()
        self.add_actor(self.p)
        self.p.x += 535
        self.p.y += 180
        self.s = SuperWario()
        self.add_actor(self.s)
        self.s.x += 350
        self.s.y += 75
        self.e = Exit()
        self.add_actor(self.e)
        self.e.x += 535
        self.e.y += 550
        self.f = FullScreen()
        self.add_actor(self.f)
        self.f.x += 425
        self.f.y += 475
        self.c = Credit()
        self.add_actor(self.c)
        self.c.x += 500
        self.c.y += 400
        self.bi = Bindings()
        self.add_actor(self.bi)
        self.bi.x += 475
        self.bi.y += 325
        self.w = Web()
        self.add_actor(self.w)
        self.w.x += 475
        self.w.y += 255
        self.stop = Pause()
        self.add_actor(self.stop)
        self.stop.x += 1030
        self.stop.y += 215
        self.start = Start()
        self.add_actor(self.start)
        self.start.x += 1030
        self.start.y += 215
        self.remove_actor(self.start)
        self.a = MenuSzoveg()
        self.add_actor(self.a)
        self.a.set_text("MARIO - Rajosan - OFFICIAL MUSIC VIDEO")
        self.a.set_alpha(1000)
        self.a.set_width(17)
        self.a.set_height(17)
        self.a.x += 900
        self.a.y += 190
        self.next = Next()
        self.add_actor(self.next)
        self.next.x += 1095
        self.next.y += 215
        self.b = MenuSzoveg()
        self.add_actor(self.b)
        self.b.set_text("Jonas Emil - Spártai Kemál Veretőgép")
        self.b.set_alpha(1000)
        self.b.set_width(18)
        self.b.set_height(18)
        self.b.x += 910
        self.b.y += 190
        self.remove_actor(self.b)
        self.stop1 = Pause()
        self.add_actor(self.stop1)
        self.stop1.x += 1030
        self.stop1.y += 215
        self.remove_actor(self.stop1)
        self.start1 = Start()
        self.add_actor(self.start1)
        self.start1.x += 1030
        self.start1.y += 215
        self.remove_actor(self.start1)
        self.last = Last()
        self.add_actor(self.last)
        self.last.x += 965
        self.last.y += 215
        self.remove_actor(self.last)
        self.c = MenuSzoveg()
        self.add_actor(self.c)
        self.c.set_text("25%")
        self.c.set_alpha(1000)
        self.c.set_width(18)
        self.c.set_height(18)
        self.c.x += 1200
        self.c.y += 220
        self.d = MenuSzoveg()
        self.add_actor(self.d)
        self.d.set_text("50%")
        self.d.set_alpha(1000)
        self.d.set_width(18)
        self.d.set_height(18)
        self.d.x += 1200
        self.d.y += 245
        self.e = MenuSzoveg()
        self.add_actor(self.e)
        self.e.set_text("25%")
        self.e.set_alpha(1000)
        self.e.set_width(18)
        self.e.set_height(18)
        self.e.x += 1200
        self.e.y += 220
        self.remove_actor(self.e)
        self.f = MenuSzoveg()
        self.add_actor(self.f)
        self.f.set_text("50%")
        self.f.set_alpha(1000)
        self.f.set_width(18)
        self.f.set_height(18)
        self.f.x += 1200
        self.f.y += 245
        self.remove_actor(self.f)
        self.p.set_on_mouse_down_listener(self.play)
        self.e.set_on_mouse_down_listener(self.exit)
        self.f.set_on_mouse_down_listener(self.fullscreen)
        self.bi.set_on_mouse_down_listener(self.bind)
        self.c.set_on_mouse_down_listener(self.creator)
        self.w.set_on_mouse_down_listener(self.website)
        self.stop.set_on_mouse_down_listener(self.stopgomb)
        self.start.set_on_mouse_down_listener(self.startgomb)
        self.next.set_on_mouse_down_listener(self.nextgomb)
        self.stop1.set_on_mouse_down_listener(self.stopgomb1)
        self.start1.set_on_mouse_down_listener(self.startgomb1)
        self.last.set_on_mouse_down_listener(self.lastgomb)
        self.c.set_on_mouse_down_listener(self.volume)
        self.d.set_on_mouse_down_listener(self.volume1)
        self.e.set_on_mouse_down_listener(self.volume2)
        self.f.set_on_mouse_down_listener(self.volume3)

    def volume3(self, sender, event):
        print(sender)
        print(event)
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                pygame.mixer.music.load('audio/spartai.mp3')
                pygame.mixer.music.play()
                pygame.mixer.music.set_volume(0.08)

    def volume2(self, sender, event):
        print(sender)
        print(event)
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                pygame.mixer.music.load('audio/spartai.mp3')
                pygame.mixer.music.play()
                pygame.mixer.music.set_volume(0.04)

    def volume1(self, sender, event):
        print(sender)
        print(event)
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                pygame.mixer.music.load('audio/rajosan.mp3')
                pygame.mixer.music.play()
                pygame.mixer.music.set_volume(0.08)

    def volume(self, sender, event):
        print(sender)
        print(event)
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                pygame.mixer.music.load('audio/rajosan.mp3')
                pygame.mixer.music.play()
                pygame.mixer.music.set_volume(0.04)


    def nextgomb(self, sender, event):
        print(sender)
        print(event)
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                pygame.mixer.music.load('audio/rajosan.mp3')
                pygame.mixer.music.stop()
                pygame.mixer.music.load('audio/spartai.mp3')
                pygame.mixer.music.play()
                self.remove_actor(self.a)
                self.add_actor(self.b)
                self.add_actor(self.stop1)
                self.remove_actor(self.stop)
                self.remove_actor(self.next)
                self.add_actor(self.last)
                self.remove_actor(self.c)
                self.remove_actor(self.d)
                self.add_actor(self.e)
                self.add_actor(self.f)

    def lastgomb(self, sender, event):
        print(sender)
        print(event)
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                pygame.mixer.music.load('audio/spartai.mp3')
                pygame.mixer.music.stop()
                pygame.mixer.music.load('audio/rajosan.mp3')
                pygame.mixer.music.play()
                self.remove_actor(self.b)
                self.add_actor(self.a)
                self.remove_actor(self.stop1)
                self.add_actor(self.stop)
                self.add_actor(self.next)
                self.remove_actor(self.last)
                self.add_actor(self.c)
                self.add_actor(self.d)
                self.remove_actor(self.e)
                self.remove_actor(self.f)

    def stopgomb1(self, sender, event):
        print(sender)
        print(event)
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                pygame.mixer.music.load('audio/spartai.mp3')
                pygame.mixer.music.stop()
                self.remove_actor(self.stop1)
                self.add_actor(self.start1)
                self.remove_actor(self.last)
                self.remove_actor(self.e)
                self.remove_actor(self.f)

    def startgomb1(self, sender, event):
        print(sender)
        print(event)
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                pygame.mixer.music.load('audio/spartai.mp3')
                pygame.mixer.music.play()
                self.remove_actor(self.start1)
                self.add_actor(self.stop1)
                self.add_actor(self.last)
                self.add_actor(self.e)
                self.add_actor(self.f)


    def stopgomb(self, sender, event):
        print(sender)
        print(event)
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                pygame.mixer.music.load('audio/rajosan.mp3')
                pygame.mixer.music.stop()
                self.remove_actor(self.stop)
                self.add_actor(self.start)
                self.remove_actor(self.next)
                self.remove_actor(self.c)
                self.remove_actor(self.d)

    def startgomb(self, sender, event):
        print(sender)
        print(event)
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                pygame.mixer.music.load('audio/rajosan.mp3')
                pygame.mixer.music.play()
                self.remove_actor(self.start)
                self.add_actor(self.stop)
                self.add_actor(self.next)
                self.add_actor(self.c)
                self.add_actor(self.d)


    def creator(self, sender, event):
        print(sender)
        print(event)
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                self.screen.game.set_screen(Impostorsus.Game.WarioScr.CreditScreen())
    def website(self, sender, event):
        print(sender)
        print(event)
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                webbrowser.open('https://pbs.twimg.com/media/EPsvEreWsAEVHip?format=jpg&name=large')

    def bind(self, sender, event):
        print(sender)
        print(event)
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                self.screen.game.set_screen(Impostorsus.Game.WarioScr.BindingsScreen())

    def exit(self, sender, event):
        print(sender)
        print(event)
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                quit()

    def play(self, sender, event):
        print(sender)
        print(event)
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                self.screen.game.set_screen(Impostorsus.Game.WarioScr.WarioScr())

    def fullscreen(self, sender, event):
        print(sender)
        print(event)
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                pygame.display.toggle_fullscreen()


class BindingsStage (game.scene2d.MyStage):
    def __init__(self):
        super().__init__()
        pygame.mouse.set_visible(0)
        self.a = MenuSzoveg()
        self.add_actor(self.a)
        self.a.set_text("Gombok:")
        self.a.set_alpha(500)
        self.a.set_width(75)
        self.a.set_height(75)
        self.a.x += 250
        self.a.y += 50
        self.b = MenuSzoveg()
        self.add_actor(self.b)
        self.b.set_text("W,A,D,SPACE = Irányítás")
        self.b.set_alpha(500)
        self.b.set_width(50)
        self.b.set_height(50)
        self.b.x += 250
        self.b.y += 175
        self.c = MenuSzoveg()
        self.add_actor(self.c)
        self.c.set_text("F11 = FullScreen")
        self.c.set_alpha(500)
        self.c.set_width(50)
        self.c.set_height(50)
        self.c.x += 250
        self.c.y += 250
        self.d = MenuSzoveg()
        self.add_actor(self.d)
        self.d.set_text("BACKSPACE = Menü")
        self.d.set_alpha(500)
        self.d.set_width(50)
        self.d.set_height(50)
        self.d.x += 250
        self.d.y += 325
        self.e = MenuSzoveg()
        self.add_actor(self.e)
        self.e.set_text("ESC = Kilépés")
        self.e.set_alpha(500)
        self.e.set_width(50)
        self.e.set_height(50)
        self.e.x += 250
        self.e.y += 400
        self.f = MenuSzoveg()
        self.add_actor(self.f)
        self.f.set_text("CTRL= Zene megállítása")
        self.f.set_alpha(500)
        self.f.set_width(50)
        self.f.set_height(50)
        self.f.x += 250
        self.f.y += 475


class CreditStage (game.scene2d.MyStage):
    def __init__(self):
        super().__init__()
        self.height = pygame.display.get_surface().get_height()
        self.width = pygame.display.get_surface().get_width()
        self.a = MenuSzoveg()
        self.add_actor(self.a)
        self.a.set_text("Készítők:")
        self.a.set_alpha(500)
        self.a.set_width(75)
        self.a.set_height(75)
        self.a.x += self.width /3 - self.a.get_width() / 2
        self.a.y += self.height /6 - self.a.get_height() / 2
        self.b = MenuSzoveg()
        self.add_actor(self.b)
        self.b.set_text("K.Bálint")
        self.b.set_alpha(500)
        self.b.set_width(50)
        self.b.set_height(50)
        self.b.x += 250
        self.b.y += 175
        self.c = MenuSzoveg()
        self.add_actor(self.c)
        self.c.set_text("Sz.Bálint")
        self.c.set_alpha(500)
        self.c.set_width(50)
        self.c.set_height(50)
        self.c.x += 250
        self.c.y += 250
        self.d = MenuSzoveg()
        self.add_actor(self.d)
        self.d.set_text("Márk")
        self.d.set_alpha(500)
        self.d.set_width(50)
        self.d.set_height(50)
        self.d.x += 250
        self.d.y += 325

class HalalStage (game.scene2d.MyStage):
    def __init__(self):
        super().__init__()
        self.h = Halalkep()
        self.add_actor(self.h)
        self.height = pygame.display.get_surface().get_height()
        self.width = pygame.display.get_surface().get_width()
        self.h.x += self.width /2 - self.h.get_width() / 2
        self.h.y += self.height /2 - self.h.get_height() / 2

class WinStage(game.scene2d.MyStage):
    def __init__(self):
        super().__init__()
        self.w = Winkep()
        self.add_actor(self.w)
        self.height = pygame.display.get_surface().get_height()
        self.width = pygame.display.get_surface().get_width()
        self.w.x += self.width /2 - self.w.get_width() / 2
        self.w.y += self.height /2 - self.w.get_height() / 2



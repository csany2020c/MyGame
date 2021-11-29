import game
import pygame
from Impostorsus.Game.WarioActor import *
from game.scene2d import MyBaseActor
import Impostorsus.Game.WarioScreen



class ASD(game.scene2d.MyStage):

    def __init__(self):
        super().__init__()

        # # for i in range(100):
        # #     h = HatterActor1()
        # #     h.x = i * h.w + -150
        # #     self.add_actor(h)
        #
        # self.add_actor(HatterActor1())

        f = open("palya.txt", "r")

        y: int = 0
        while True:
            line = f.readline().strip()
            if line:
                x: int = 0
                for c in line:
                    a: MyBaseActor = None
                    if c == "o":
                        a = Kocka()
                    if c == "T":
                        a = Question()
                    if c == "g":
                        a = GroundActor()
                    if c == "x":
                        a = InvisActor()
                    if c == "W":
                        self.wario = WarioActor()
                        a = self.wario
                    if a is not None:
                        a.x = x * 64
                        a.y = y * 64
                        self.add_actor(a)
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

    def press(self, sender, event):
        # print(event.key)
        if event.key == pygame.K_d:
            sender.x += 10
            self.camera.set_tracking_window(0.2, 0.2, 0.6, 0.2)
        if event.key == pygame.K_a:
            sender.x -= 10
            self.camera.set_tracking_window(0.6, 0.2, 0.2, 0.2)

    def interval(self, sender):
        self.wario.x += 100 * self.get_delta_time()
        self.gomba.x += 100 * self.get_delta_time()
        pass

    def key_down(self, sender, event):
        print(sender)
        print(event)
        if event.key == pygame.K_w:
            print("'hoppáré'")
            self.wario.ugras()

        if event.key == pygame.K_SPACE:
            print("'hoppáré'")
            self.wario.ugras()

    def act(self, delta_time: float):
        super().act(delta_time)
        overlapsASD: bool = False
        overASD: bool = False

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

            if isinstance(actorASD, InvisActor):
                if self.wario.overlaps(actorASD):
                    overASD = True
                    break

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
            self.screen.game.set_screen(Impostorsus.Game.WarioScreen.MenuScreen())

class ASD2 (game.scene2d.MyStage):
    def __init__(self):
        super().__init__()
        self.b = BackGround()
        self.add_actor(self.b)
        self.b.x += 0
        self.b.y += 0
        self.p = Play()
        self.add_actor(self.p)
        self.p.x += 535
        self.p.y += 250
        self.s = SuperWario()
        self.add_actor(self.s)
        self.s.x += 400
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
        self.p.set_on_mouse_down_listener(self.play)
        self.e.set_on_mouse_down_listener(self.exit)
        self.f.set_on_mouse_down_listener(self.fullscreen)
        self.bi.set_on_mouse_down_listener(self.bind)
        self.c.set_on_mouse_down_listener(self.creator)

    def creator(self, sender, event):
        print(sender)
        print(event)
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                self.screen.game.set_screen(Impostorsus.Game.WarioScreen.CreditScreen())

    def bind(self, sender, event):
        print(sender)
        print(event)
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                self.screen.game.set_screen(Impostorsus.Game.WarioScreen.BindingsScreen())

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
                self.screen.game.set_screen(Impostorsus.Game.WarioScreen.WarioScreen())

    def fullscreen(self, sender, event):
        print(sender)
        print(event)
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                pygame.display.toggle_fullscreen()

class BindingsStage (game.scene2d.MyStage):
    def __init__(self):
        super().__init__()


class CreditStage (game.scene2d.MyStage):
    def __init__(self):
        super().__init__()
        self.a = MenuSzoveg()
        self.add_actor(self.a)
        self.a.set_text("Készítők:")
        self.a.set_alpha(500)
        self.a.set_width(75)
        self.a.set_height(75)
        self.a.x += 250
        self.a.y += 50
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







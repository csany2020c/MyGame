import game
import pygame
from Impostorsus.Game.WarioActor import *
class WarioStage1(game.scene2d.MyStage):

    def __init__(self):
        super().__init__()

        for i in range(100):
            h = HatterActor1()
            h.x = i * h.w + -150
            self.add_actor(h)

        self.add_actor(HatterActor1())
        self.kocka = Kocka()
        self.add_actor(self.kocka)
        self.kocka.x = 250
        self.kocka.y = 350
        self.kerdo = Question()
        self.gomba = Gemba()
        self.add_actor(self.kerdo)
        self.kerdo.x = 200
        self.kerdo.y = 350
        self.wario = WarioActor()
        self.camera.tracking = self.wario
        self.add_actor(self.wario)
        self.wario.set_on_key_press_listener(self.press)
        self.wario.set_on_key_down_listener(self.key_down)


        for i in range(100):
            g = GroundActor()
            g.y = 615
            g.x = i * g.w + -150
            self.add_actor(g)

    def press(self, sender, event):
        # print(event.key)
        if event.key == pygame.K_d:
            sender.x += 10
        if event.key == pygame.K_a:
            sender.x -= 10

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

        for actorASD in self.actors:
            if isinstance(actorASD, Gemba):
                if self.wario.overlaps(actorASD):
                    overlapsASD = True
                    break
        if overlapsASD:
            self.gomba = Gemba()
            self.wario.set_height(200)
            self.wario.set_width(200)
            self.remove_actor(self.gomba)

        for actorASD in self.actors:
            if isinstance(actorASD, GroundActor):
                if self.gomba.overlaps(actorASD):
                    overlapsASD = True
                    break
        if overlapsASD:
            self.gomba.stop()
        else:
            self.gomba.start()

        for actorASD in self.actors:
            if isinstance(actorASD, Question):
                if self.wario.overlaps(actorASD):
                    overlapsASD = True
                    break
        if overlapsASD:
            self.wario.stop()
            self.add_actor(self.gomba)
            self.gomba.x += 200
            self.gomba.y += 400
            self.remove_actor(self.kerdo)

        else:
            self.wario.start()

        for actorASD in self.actors:
            if isinstance(actorASD, Kocka):
                if self.wario.overlaps(actorASD):
                    overlapsASD = True
                    break
        if overlapsASD:
            self.wario.stop()
        else:
            self.wario.start()

        for actorASD in self.actors:
            if isinstance(actorASD, GroundActor):
                if self.wario.overlaps(actorASD):
                    overlapsASD = True
                    break
        if overlapsASD:
            self.wario.stop()
        else:
            self.wario.start()

import game
import pygame
from game.scene2d import  MyPermanentTimer, MyOneTickTimer, MyBaseActor, MyTickTimer, MyIntervalTimer
import random
from game.scene2d import MyTimers




class Enemy1Actor(game.scene2d.MyActor):

    def __init__(self):
        super().__init__("images/fatjordan.png")
        self.asd = None
        self.life = 5
        self.set_on_key_down_listener(self.key_down)

        self.t = MyTickTimer(interval=1.5, func=self.tikk)
        self.add_timer(self.t)

        self.t2 = MyIntervalTimer(func=self.interval, start_time=3, stop_time=5)
        self.add_timer(self.t2)


    def act(self, delta_time: float):
        super().act(delta_time)
        if self.x + self.width < game.scene2d.MyGame.get_screen_width():
            self.x += delta_time * 60
            self.rotate_with(delta_time * 20)

    def key_down(self, sender, event):
        print(sender)
        print(event)
        if event.key == pygame.K_f:
            print("FFFFFFFFFFFFFFFFFFFFFFFFFFF")
            self.asd.x += 4

    def tikk(self, sender):
        self.x = random.Random().randint(0, game.scene2d.MyGame.get_screen_width() - self.w)
        self.y = random.Random().randint(0, game.scene2d.MyGame.get_screen_height() - self.h)

    def interval(self, sender):
        selff.x += 100 * self.get_delta_time()
        pass

   
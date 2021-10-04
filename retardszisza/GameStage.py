import game
from retardszisza.EnemyActor import *
import abc
from game.scene2d.MyElapsedTime import *
import random
import pygame


class GameStage(game.scene2d.MyStage):

    def __init__(self):
        super().__init__()
        self.b = Enemy1Actor()
        self.add_actor(self.b)
        self.b.y = 150

    def act(self, delta_time: float):
        super().act(delta_time)


class MyBaseTimer(MyElapsedTime, metaclass=abc.ABCMeta):

    def __init__(self, func=None):
        MyElapsedTime.__init__(self)
        self._listener = func
        self._enabled: bool = True
        self.correction: float = 0
        self.parent: 'game.scene2d.MyTimers' = None

    def set_timer_listener(self, func):
        self._listener = func

    def remove_timer_listener(self, func):
        self._listener = None

    def start(self):
        self._enabled = True

    def stop(self):
        self._enabled = False

    def act(self, delta_time: float):
        if self._enabled:
            # print(delta_time)
            MyElapsedTime.act(self, delta_time)
            self._do_timer()

    def _do_timer(self):
        pass

    def remove(self):
        if self.parent == None:
            return
        self.parent.remove_timer(self)
        self.parent = None


class MyTickTimer(MyBaseTimer):

    def __init__(self, func=None, interval: float = 1, start_delay: float = 0, repeat: bool = True):
        super().__init__(func)
        self.interval: float = interval
        self.elapsed_time = -start_delay
        self.repeat: bool = repeat

    def _do_timer(self):
        if not self._enabled:
            return
        if self.elapsed_time >= self.interval:
            self.correction = self.elapsed_time-self.interval
            if self._listener is not None:
                self._listener(self)
            if not self.repeat:
                self.stop()
            else:
                self.elapsed_time = self.correction

    def interval(self, sender):
        self.asd.x += 100*self.get_delta_time()
        pass

    def tikk(self, sender):
        self.asd.x = random.Random().randint(0, game.scene2d.MyGame.get_screen_width() - self.asd.w)
        self.asd.y = random.Random().randint(0, game.scene2d.MyGame.get_screen_height() - self.asd.h)

        self.asd.set_on_key_press_listener(self.press)

    def press(self, sender, event):
        # print(event.key)
        if event.key == pygame.K_RIGHT:
            sender.x += 1
        if event.key == pygame.K_LEFT:
            sender.x -= 1
        if event.key == pygame.K_UP:
            sender.y -= 1
        if event.key == pygame.K_DOWN:
            sender.y += 1
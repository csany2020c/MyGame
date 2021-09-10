import pygame
import time
from game.scene2d.MyLifeCycles import *
from game.scene2d.MyTimers import *

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from __type_checking__ import *


class MyGame(MyTimers):

    def __init__(self, width: int = 1280, height: int = 720):
        MyTimers.__init__(self)
        pygame.init()
        self._screenWidth: int = width
        self._screenHeight: int = height
        self._p_et: float = 0
        self._elapsed_time: float = 0
        self._frameLimiter: float = 60
        self._frame_count: float = 0
        self._deltaTime: float = 1.0 / self._frameLimiter
        self._getTicksLastFrame: int = 0
        self._screen: 'MyScreen' = None
        self.pgScreen: pygame.Surface = pygame.display.set_mode(size=(width, height))
        self.create()
        self._running = True
        self.loop()

    def act(self, delta_time: float):
        MyLifeCycles.act(self, delta_time)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.exit()
            if event.type == pygame.KEYDOWN:
                pass
            if event.type == pygame.KEYUP:
                pass
        self._elapsed_time += self.get_delta_time()
        self._screen.act(delta_time)

    def draw(self):
        MyLifeCycles.draw(self)
        self._frame_count += 1
        self._screen.draw()
        if int(self._elapsed_time) != int(self._p_et):
            print("FPS: " + str(self._frame_count))
            self._frame_count = 0
            self._p_et = self._elapsed_time
        pass

    # Folyamatosan fut, amíg be nem zárjuk a programot. Alapesetben itt kap helyet a képernyők megjelenítését kezelő
    # program is, azaz lehet vele a képernyőket cserélgetni. Itt érzékeli a felhasználói bemeneteket is.
    # Amennyiben az előre megírt algoritmusok megfelelők, ezt nem kell lecserélni az öröklődéskor.
    def loop(self):
        while self._running:
            t = pygame.time.get_ticks()
            self.act(self._deltaTime)
            self.draw()
            pygame.display.update()
            sleep: float = 1.0 / self._frameLimiter - (pygame.time.get_ticks() - t) / 1000.0
            if sleep > 0:
                time.sleep(sleep)
            self._deltaTime = (t - self._getTicksLastFrame) / 1000.0
            self._getTicksLastFrame = t
        self.hide()
        self.dispose()

    def set_screen(self, screen: 'MyScreen'):
        if self._screen is not None:
            self._screen.set_game(None)
        self._screen = screen
        self._screen.set_game(self)

    def exit(self):
        self._running = False

    def get_screen(self) -> 'MyScreen':
        return self._screen

    def get_delta_time(self) -> float:
        return self._deltaTime

    def get_elapsed_time(self) -> float:
        return self._elapsed_time

    def dispose(self):
        MyTimers.dispose(self)
        self._screen.dispose()
        pass

    def get_screen_width(self):
        return self._screenWidth

    def get_screen_height(self):
        return self._screenHeight

    delta_time: float = property(get_delta_time)
    elapsed_time: float = property(get_elapsed_time)
    screen: 'MyScreen' = property(get_screen, set_screen)
    screen_width: int = property(get_screen_width)
    screen_height: int = property(get_screen_height)

    #
    # public static void printStackTrace(){
    #     for (StackTraceElement ste : Thread.currentThread().getStackTrace()) {
    #         Gdx.app.log("Stack", ste.toString());
    #     }
    # }

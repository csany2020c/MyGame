import time
import pygame
from game.scene2d.MyLifeCycles import *


class MyGame(MyLifeCycles):

    def __init__(self, width: int = 1280, height: int = 720):
        pygame.init()
        self._p_et: float = 0
        self.elapsed_time: float = 0
        self.__frameLimiter: float = 60
        self._frame_count: float = 0
        self.__deltaTime: float = 1.0 / self.__frameLimiter
        self.__getTicksLastFrame: int = 0
        self.__screen = None
        self.pgScreen = pygame.display.set_mode(size=(width, height))
        self.create()
        self.__running = True
        self.loop()

    def act(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.exit()
            if event.type == pygame.KEYDOWN:
                pass
            if event.type == pygame.KEYUP:
                pass
        self.elapsed_time += self.get_delta_time()
        self.__screen.act()



    def draw(self):
        self._frame_count += 1
        self.__screen.draw()
        if int(self.elapsed_time) != int(self._p_et):
            print("FPS: " + str(self._frame_count))
            self._frame_count = 0
            self._p_et = self.elapsed_time
        pass

    # Folyamatosan fut, amíg be nem zárjuk a programot. Alapesetben itt kap helyet a képernyők megjelenítését kezelő
    # program is, azaz lehet vele a képernyőket cserélgetni. Itt érzékeli a felhasználói bemeneteket is.
    # Amennyiben az előre megírt algoritmusok megfelelők, ezt nem kell lecserélni az öröklődéskor.
    def loop(self):
        while self.__running:
            t = pygame.time.get_ticks()
            self.act()
            self.draw()
            pygame.display.update()
            sleep: float = 1.0 / self.__frameLimiter - (pygame.time.get_ticks() - t) / 1000.0
            if sleep > 0:
                time.sleep(sleep)
            self.__deltaTime = (t - self.__getTicksLastFrame) / 1000.0
            self.__getTicksLastFrame = t
        self.hide()
        self.dispose()

    def set_screen(self, screen):
        if self.__screen != None:
            self.__screen.set_game(None)
        self.__screen = screen
        self.__screen.set_game(self)

    def exit(self):
        self.__running = False

    def get_screen(self):
        return self.__screen

    def get_delta_time(self) -> float:
        return self.__deltaTime

    def dispose(self):
        super(MyGame, self).dispose()
        self.__screen.dispose()
        pass

    #
    # public static void printStackTrace(){
    #     for (StackTraceElement ste : Thread.currentThread().getStackTrace()) {
    #         Gdx.app.log("Stack", ste.toString());
    #     }
    # }

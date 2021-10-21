import abc

import pygame

from game.scene2d import MyLabel
from game.scene2d.MyStage import *
from typing import List

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from __type_checking__ import *


class MyMathFunction(metaclass=abc.ABCMeta):

    def __init__(self, color=(255, 255, 255)) -> None:
        super().__init__()
        self.color = color

    @abc.abstractmethod
    def f(x: float) -> float:
        pass


class MyMathGraphStage(MyStage):

    def draw_function(self, func: MyMathFunction):
        x: float = (-self.screen.game.get_screen_width() / 2.0 + self.offset_x) / self.zoom
        while x < (self.screen.game.get_screen_width() / 2 + self.offset_x) / self.zoom:
            pygame.draw.line(self.screen.game.surface, color=func.color,
                             start_pos=(x * self.zoom + self.screen.game.get_screen_width() / 2.0 - self.offset_x,
                                        (-func.f(
                                            x)) * self.zoom + self.screen.game.get_screen_height() / 2.0 + self.offset_y),
                             end_pos=((
                                                  x + 1.0 / self.zoom) * self.zoom + self.screen.game.get_screen_width() / 2.0 - self.offset_x,
                                      (-func.f(
                                          x + 1 / self.zoom)) * self.zoom + self.screen.game.get_screen_height() / 2.0 + self.offset_y))
            x += 1.0 / self.zoom

    def __init__(self):
        super().__init__()
        self.zoom: float = 64
        self.offset_x = 200
        self.offset_y = 200
        self._math_functions: List = list()
        self._xlabel = MyLabel()
        self._ylabel = MyLabel()
        self._lash_hover_x = 0
        self._lash_hover_y = 0
        self._ylabel.y = self._xlabel.h
        self.add_actor(self._xlabel)
        self.add_actor(self._ylabel)
        self.set_on_mouse_move_listener(self.onhover)
        self.set_on_mouse_wheel_listener(self.onwheel)
        self.set_on_key_press_listener(self.onkeypress)

    def _update(self):
        x = (self._lash_hover_x - self.screen.game.get_screen_width() / 2 + self.offset_x) / self.zoom
        y = -((self._lash_hover_y - self.screen.game.get_screen_height() / 2 - self.offset_y) / self.zoom)
        self._xlabel.set_text("x: " + str(x))
        self._ylabel.set_text("y: " + str(y))

    def add_math_function(self, math_function: MyMathFunction):
        self._math_functions.append(math_function)

    def draw(self):
        super().draw()
        # x: float = 0
        # while x < self.screen.game.get_screen_width() / 2:
        #     pygame.draw.line(self.screen.game.surface, color=(40, 40, 27, 128),
        #                      start_pos=(self.screen.game.get_screen_width() / 2 + x, 0), end_pos=(
        #         self.screen.game.get_screen_width() / 2 + x, self.screen.game.get_screen_height()))
        #     pygame.draw.line(self.screen.game.surface, color=(40, 40, 27, 128),
        #                      start_pos=(self.screen.game.get_screen_width() / 2 - x, 0), end_pos=(
        #         self.screen.game.get_screen_width() / 2 - x, self.screen.game.get_screen_height()))
        #     x += self.zoom
        #
        # y: float = 0
        # while y < self.screen.game.get_screen_height() / 2:
        #     pygame.draw.line(self.screen.game.surface, color=(40, 40, 27, 128),
        #                      start_pos=(0, self.screen.game.get_screen_height() / 2 - y), end_pos=(
        #             self.screen.game.get_screen_width(), self.screen.game.get_screen_height() / 2 - y))
        #     pygame.draw.line(self.screen.game.surface, color=(40, 40, 27, 128),
        #                      start_pos=(0, self.screen.game.get_screen_height() / 2 + y), end_pos=(
        #             self.screen.game.get_screen_width(), self.screen.game.get_screen_height() / 2 + y))
        #     y += self.zoom

        pygame.draw.line(self.screen.game.surface, color=(200, 200, 27, 128),
                         start_pos=(0, self.screen.game.get_screen_height() / 2 + self.offset_y),
                         end_pos=(self.screen.game.get_screen_width(), self.screen.game.get_screen_height() / 2 + self.offset_y))
        pygame.draw.line(self.screen.game.surface, color=(200, 200, 27, 128),
                         start_pos=(self.screen.game.get_screen_width() / 2 - self.offset_x, 0),
                         end_pos=(self.screen.game.get_screen_width() / 2 - self.offset_x, self.screen.game.get_screen_height()))
        for f in self._math_functions:
            self.draw_function(f)

    def onwheel(self, sender, event):
        print(event)
        self.zoom += event.y * self.zoom / 10
        if self.zoom < 1:
            self.zoom = 1

    def onhover(self, sender, event):
        self._lash_hover_x = event.pos[0]
        self._lash_hover_y = event.pos[1]
        self._update()

    def onkeypress(self, sender, event):
        if event.key == pygame.K_UP or event.key == pygame.K_w:
            self.offset_y += self.zoom * self.get_delta_time() * 10
            self._update()
        if event.key == pygame.K_DOWN or event.key == pygame.K_s:
            self.offset_y -= self.zoom * self.get_delta_time() * 10
            self._update()
        if event.key == pygame.K_LEFT or event.key == pygame.K_a:
            self.offset_x -= self.zoom * self.get_delta_time() * 10
            self._update()
        if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
            self.offset_x += self.zoom * self.get_delta_time() * 10
            self._update()
        if event.key == pygame.K_PLUS or event.key == pygame.K_1:
            self.zoom += self.zoom / 10 * self.get_delta_time() * 10
            self._update()
        if event.key == pygame.K_MINUS or event.key == pygame.K_2:
            self.zoom -= self.zoom / 10 * self.get_delta_time() * 10
            self._update()
        if event.key == pygame.K_SLASH or event.key == pygame.K_0:
            self.offset_x = 0
            self.offset_y = 0
            self._update()

    def act(self, delta_time: float):
        super().act(delta_time)
        # self.zoom += delta_time * 10

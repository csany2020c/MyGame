import abc

from game.scene2d import MyLabel
from game.scene2d.MyStage import *
from typing import List

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from __type_checking__ import *


class MyMathFunction(metaclass=abc.ABCMeta):

    def __init__(self, color=(255,255,255)) -> None:
        super().__init__()
        self.color = color

    @abc.abstractmethod
    def f(x:float)->float:
        pass


class MyMathGraphStage(MyStage):

    def draw_function(self, func: MyMathFunction):
        x: float = -self.screen.game.get_screen_width() / 2.0 / self.zoom
        while x < self.screen.game.get_screen_width() / 2 / self.zoom:
            pygame.draw.line(self.screen.game.surface, color=func.color,
                             start_pos=(x * self.zoom + self.screen.game.get_screen_width() / 2.0,
                                        (-func.f(x))*self.zoom + self.screen.game.get_screen_height() / 2.0),
                             end_pos=((x + 1.0 / self.zoom) * self.zoom + self.screen.game.get_screen_width() / 2.0,
                                      (-func.f(x+1/self.zoom))*self.zoom + self.screen.game.get_screen_height() / 2.0))
            x += 1.0 / self.zoom

    def __init__(self):
        super().__init__()
        self.zoom: float = 64
        self.math_functions: List = list()
        self.xlabel = MyLabel()
        self.ylabel = MyLabel()
        self.ylabel.y = self.xlabel.h
        self.add_actor(self.xlabel)
        self.add_actor(self.ylabel)
        self.update(0,0)
        self.set_on_mouse_move_listener(self.onhover)
        self.set_on_mouse_wheel_listener(self.onwheel)

    def update(self, x: float, y: float):
        self.xlabel.set_text("x: " + str(x))
        self.ylabel.set_text("y: " + str(y))

    def add_math_function(self, math_function: MyMathFunction):
        self.math_functions.append(math_function)

    def draw(self):
        super().draw()
        x: float = 0
        while x < self.screen.game.get_screen_width() / 2:
            pygame.draw.line(self.screen.game.surface, color=(40, 40, 27), start_pos=(self.screen.game.get_screen_width() / 2 + x, 0), end_pos=(self.screen.game.get_screen_width() / 2 + x, self.screen.game.get_screen_height()))
            pygame.draw.line(self.screen.game.surface, color=(40, 40, 27), start_pos=(self.screen.game.get_screen_width() / 2 - x, 0), end_pos=(self.screen.game.get_screen_width() / 2 - x, self.screen.game.get_screen_height()))
            x += self.zoom

        y: float = 0
        while y < self.screen.game.get_screen_height() / 2:
            pygame.draw.line(self.screen.game.surface, color=(40, 40, 27),
                             start_pos=(0, self.screen.game.get_screen_height() / 2 - y), end_pos=(
                self.screen.game.get_screen_width(), self.screen.game.get_screen_height() / 2 - y))
            pygame.draw.line(self.screen.game.surface, color=(40, 40, 27),
                             start_pos=(0, self.screen.game.get_screen_height() / 2 + y), end_pos=(
                self.screen.game.get_screen_width(), self.screen.game.get_screen_height() / 2 + y))
            y += self.zoom

        pygame.draw.line(self.screen.game.surface, color=(200, 200, 27), start_pos=(0, self.screen.game.get_screen_height() / 2), end_pos=(self.screen.game.get_screen_width(), self.screen.game.get_screen_height() / 2))
        pygame.draw.line(self.screen.game.surface, color=(200, 200, 27), start_pos=(self.screen.game.get_screen_width() / 2, 0), end_pos=(self.screen.game.get_screen_width() / 2, self.screen.game.get_screen_height()))
        for f in self.math_functions:
            self.draw_function(f)

    def onwheel(self, sender, event):
        print(event)
        self.zoom += event.y * self.zoom / 10
        if self.zoom < 1:
            self.zoom = 1

    def onhover(self, sender, event):
        self.update((event.pos[0] - self.screen.game.get_screen_width() / 2) / self.zoom,
                    -(event.pos[1] - self.screen.game.get_screen_height() / 2) / self.zoom)

    def act(self, delta_time: float):
        super().act(delta_time)
        # self.zoom += delta_time * 10
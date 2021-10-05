from typing import List

import pygame

from game.scene2d.MyDebug import *
from game.scene2d.MyTimers import *
from game.scene2d.MyMouseListeners import *
from game.scene2d.MyElapsedTime import *
from game.scene2d.MyKeyboardListeners import *

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from game.scene2d.__type_checking__ import *


class MyScreen(MyTimers, MyElapsedTime, MyMouseListeners, MyKeyboardListeners, MyDebug):

    def __init__(self):
        MyElapsedTime.__init__(self)
        MyTimers.__init__(self)
        MyMouseListeners.__init__(self)
        MyKeyboardListeners.__init__(self)
        MyDebug.__init__(self)
        self.r: float = 0
        self.g: float = 0
        self.b: float = 0
        self._game: 'MyGame' = None
        self._stages: List['MyStage'] = list()
        self._stages_reverse: List['MyStage'] = list()

    def get_game(self) -> 'MyGame':
        return self._game

    def set_game(self, game: 'MyGame'):
        if game is None:
            self.hide()
        else:
            self.show()
        self._game = game

    def set_background_color(self, r: int, g: int, b: int) -> 'MyScreen':
        self.r = r
        self.g = g
        self.b = b
        return self

    def act(self, delta_time: float):
        MyElapsedTime.act(self, delta_time)
        MyTimers.act(self, delta_time)
#        MyMouseListeners.act(self, delta_time)
        for s in self._stages:
            if s.visible and not s.pause:
                s.act(delta_time)
        MyKeyboardListeners.do_keypress_event(self)

    def draw(self):
        if pygame.display.get_active():
            self._game.surface.fill((self.r, self.g, self.b))
            for s in self._stages:
                if s.visible:
                    s.draw()

    def add_stage(self, stage: 'MyStage') -> 'MyScreen':
        self._stages.append(stage)
        stage.debug = self.debug
        stage.set_screen(self)
        self._stages_reverse = list(reversed(self._stages))
        return self

    def remove_stage(self, stage: 'MyStage') -> 'MyScreen':
        self._stages.remove(stage)
        stage.set_screen(None)
        self._stages_reverse = list(reversed(self._stages))
        return self

    def get_stages(self) -> List['MyStage']:
        return self._stages

    def get_stages_reverse(self) -> List['MyStage']:
        return self._stages_reverse

    def set_debug(self, debug: bool):
        super().set_debug(debug)
        for obj in self._stages:
            obj.debug = debug

    def get_debug(self) -> bool:
        return self._debug

    game = property(get_game, set_game)
    # screen_width: int = property(get_screen_width)
    # screen_height: int = property(get_screen_height)
    stages: List["MyStage"] = property(get_stages)
    stages_reverse: List["MyStage"] = property(get_stages_reverse)
    debug: bool = property(get_debug, set_debug)

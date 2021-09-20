from typing import List
from game.scene2d.MyTimers import *
from game.scene2d.MyBaseListeners import *
from game.scene2d.MyElapsedTime import *

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from __type_checking__ import *


class MyScreen(MyTimers, MyElapsedTime, MyBaseListeners):

    def __init__(self):
        MyElapsedTime.__init__(self)
        MyTimers.__init__(self)
        MyBaseListeners.__init__(self)
        self.r: float = 0
        self.g: float = 0
        self.b: float = 0
        self._game: 'MyGame' = None
        self._stages: List['MyStage'] = list()
        self.create()

    def dispose(self):
        for s in self._stages:
            s.dispose()

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
        MyBaseListeners.act(self, delta_time)
        for s in self._stages:
            if s.visible and not s.pause:
                s.act(delta_time)

    def draw(self):
        self._game.surface.fill((self.r, self.g, self.b))
        for s in self._stages:
            # g = game.MyStage.MyStage(s)
            if s.visible:
                s.draw()

    def add_stage(self, stage: 'MyStage') -> 'MyScreen':
        self._stages.append(stage)
        stage.set_screen(self)
        return self

    def remove_stage(self, stage: 'MyStage') -> 'MyScreen':
        self._stages.remove(stage)
        stage.set_screen(None)
        return self

    def get_screen_width(self) -> int:
        return self.stage.game.screen_width

    def get_screen_height(self) -> int:
        return self.stage.game.screen_height

    def get_stages(self) -> List['MyStage']:
        return self._stages

    game = property(get_game, set_game)
    screen_width: int = property(get_screen_width)
    screen_height: int = property(get_screen_height)
    stages: List["MyStage"] = property(get_stages)


from game.scene2d.MyElapsedTime import *
from game.scene2d.MyTimers import *
from game.scene2d.MyMouseListeners import *
from game.scene2d.MyKeyboardListeners import *
from game.scene2d.MyZIndex import *

from typing import TYPE_CHECKING
from typing import List

if TYPE_CHECKING:
    from __type_checking__ import *


class MyStage(MyMouseListeners, MyKeyboardListeners, MyElapsedTime, MyZIndex, MyTimers):

    def __init__(self):
        MyMouseListeners.__init__(self)
        MyKeyboardListeners.__init__(self)
        MyElapsedTime.__init__(self)
        MyZIndex.__init__(self)
        MyTimers.__init__(self)
        self._visible: bool = True
        self._pause: bool = False
        self._screen: 'MyScreen' = None
        self._actors: List['MyBaseActor'] = list()
        self._actors_reverse: List['MyBaseActor'] = list()

    def act(self, delta_time: float):
        MyElapsedTime.act(self, self.get_delta_time())
#        MyTimers.act(self, self.get_delta_time())
        for obj in self._actors:
            obj.act(delta_time)

    def draw(self):
        for obj in self._actors:
            obj.draw()

    def add_actor(self, actor: 'MyBaseActor') -> 'MyStage':
        # https://stackoverflow.com/questions/2461907/python-circular-imports-needed-for-type-checking
        # The best solution is to not check types.
        # XD
        # XD
        #if isinstance(actor, 'MyBaseActor'):
        self._actors.append(actor)
        if actor.stage is not None:
            print("A következő actor át lett helyezve a " + str(id(actor._stage)) + " stageből a " + str(id(self)) + " stagebe.")
            actor.remove_from_stage()
        actor.set_stage(self)
        self._actors.sort()
        self._actors_reverse = list(reversed(self._actors))
        return self
        #else:
        #    print("ERROR: Az objektum példány nem adható hozzá a staghez, mert nem a MyBaseActor leszármazottja.")

    def remove_actor(self, actor: 'MyBaseActor') -> 'MyStage':
        self._actors.remove(actor)
        actor.set_stage(0)
        self._actors_reverse = list(reversed(self._actors))
        return self

    def remove_stage_from_screen(self):
        self._screen.remove_stage(self)

    def set_screen(self, screen: 'MyScreen'):
        self._screen = screen
        if screen is None:
            self.hide()
        else:
            self.show()

    def get_delta_time(self) -> float:
        if self.screen is not None and self.screen.game is not None:
            return self._screen.game.get_delta_time()
        else:
            return 0

    def get_screen(self) -> 'MyScreen':
        return self._screen

    def get_actors(self) -> List['MyBaseActor']:
        return self._actors

    def get_actors_reverse(self) -> List['MyBaseActor']:
        return self._actors_reverse

    def is_pause(self) -> bool:
        return self._pause

    def set_pause(self, pause: bool):
        self._pause = pause

    def is_visible(self) -> bool:
        return self._visible

    def set_visible(self, visible: bool):
        self._visible = visible

    def get_z_index(self) -> int:
        return super().get_z_index()

    def set_z_index(self, z_index: int):
        super().set_z_index(z_index)
        if self._screen is not None:
            self._screen.stages.sort()

    z: int = property(get_z_index, set_z_index)
    set_z_index: int = property(get_z_index, set_z_index)
    screen: 'MyScreen' = property(get_screen, set_screen)
    actors: List['MyBaseActor'] = property(get_actors)
    actors_reverse: List['MyBaseActor'] = property(get_actors_reverse)
    # screen_width: int = property(get_screen_width)
    # screen_height: int = property(get_screen_height)
    pause: bool = property(is_pause, set_pause)
    visible: bool = property(is_visible, set_visible)

from game.scene2d.MyLifeCycles import *
from typing import List

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from __type_checking__ import *


class MyTimers(MyLifeCycles):

    def __init__(self) -> None:
        MyLifeCycles.__init__(self)
        self._timers: List['MyBaseTimer'] = list()

    def act(self, delta_time: float):
        for obj in self._timers:
            obj.act(delta_time)

    def add_timer(self, timer: 'MyBaseTimer'):
        # if isinstance(timer, MyBaseTimer):
        self._timers.append(timer)
        if timer.base_actor != 0:
            timer.remove()
        timer.base_actor = self
        # else:
        #    print("ERROR: Az objektum példány nem adható hozzá a staghez, mert nem a MyBaseTimer leszármazottja.")

    def remove_timer(self, timer: 'MyBaseTimer'):
        try:
            self._timers.remove(timer)
            timer.base_actor = 0
        except ValueError:
            print("A következő objektum már el lett távolítva korábban: " + str(id(self)))

    def get_timers(self) -> List['MyBaseTimer']:
        return self._timers

    timers: List['MyBaseTimer'] = property(get_timers)

from game.scene2d.MyLifeCycles import *


class MyElapsedTime(MyLifeCycles):

    def __init__(self) -> None:
        self._elapsed_time: float = 0

    def act(self, delta_time: float):
        MyLifeCycles.act(self, delta_time)
        self._elapsed_time += delta_time

    def get_elapsed_time(self) -> float:
        return self._elapsed_time

    elapsed_time: float = property(get_elapsed_time)


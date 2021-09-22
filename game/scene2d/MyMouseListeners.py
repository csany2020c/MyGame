from game.scene2d.MyLifeCycles import *


class MyMouseListeners(MyLifeCycles):

    def __init__(self) -> None:
        MyLifeCycles.__init__(self)
        self._on_mouse_down_listener = None
        self._on_mouse_up_listener = None
        self._on_mouse_move_listener = None

    def remove_on_mouse_down_listener(self):
        self._on_mouse_down_listener = None

    def remove_on_mouse_up_listener(self):
        self._on_mouse_up_listener = None

    def remove_on_mouse_move_listener(self):
        self._on_mouse_move_listener = None

    def set_on_mouse_move_listener(self, func):
        self._on_mouse_move_listener = func

    def set_on_mouse_up_listener(self, func):
        self._on_mouse_up_listener = func

    def set_on_mouse_down_listener(self, func):
        self._on_mouse_down_listener = func

    def act(self, delta_time: float):
        super().act(delta_time)

    def is_mouse_event_present(self)->bool:
        return self._on_mouse_down_listener is not None or self._on_mouse_up_listener is not None or self._on_mouse_move_listener is not None
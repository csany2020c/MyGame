from game.scene2d.MyLifeCycles import *


class MyMouseListeners(MyLifeCycles):

    def __init__(self) -> None:
        MyLifeCycles.__init__(self)
        self._on_key_up_listener = None
        self._on_key_down_listener = None

    def remove_on_key_down_listener(self):
        self._on_key_down_listener = None

    def remove_on_key_up_listener(self):
        self._on_key_up_listener = None

    def set_on_key_down_listener(self, func):
        self._on_key_down_listener = func

    def set_on_key_up_listener(self, func):
        self._on_key_up_listener = func

    def act(self, delta_time: float):
        super().act(delta_time)

    def is_keyboard_event_present(self)->bool:
        return self._on_key_up_listener is not None or self._on_key_down_listener is not None

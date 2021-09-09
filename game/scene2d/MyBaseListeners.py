class MyBaseListeners:

    def __init__(self) -> None:
        self._on_mouse_down_listener = 0
        self._on_mouse_up_listener = 0
        self._on_mouse_move_listener = 0
        self._on_key_up_listener = 0
        self._on_key_down_listener = 0

    def remove_on_mouse_down_listener(self):
        self._on_mouse_down_listener = 0

    def remove_on_mouse_up_listener(self):
        self._on_mouse_up_listener = 0

    def remove_on_mouse_move_listener(self):
        self._on_mouse_move_listener = 0

    def remove_on_key_down_listener(self):
        self._on_key_down_listener = 0

    def remove_on_key_up_listener(self):
        self._on_key_up_listener = 0

    def set_on_key_down_listener(self, func):
        self._on_key_down_listener = func

    def set_on_key_up_listener(self, func):
        self._on_key_up_listener = func

    def set_on_mouse_move_listener(self, func):
        self._on_mouse_move_listener = func

    def set_on_mouse_up_listener(self, func):
        self._on_mouse_up_listener = func

    def set_on_mouse_down_listener(self, func):
        self._on_mouse_down_listener = func


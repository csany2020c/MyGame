import pygame


class MyMouseListeners:

    def __init__(self) -> None:
        self._on_mouse_down_listener = None
        self._on_mouse_up_listener = None
        self._on_mouse_move_listener = None
        self._on_mouse_wheel_listener = None

    def remove_on_mouse_down_listener(self):
        self._on_mouse_down_listener = None

    def remove_on_mouse_up_listener(self):
        self._on_mouse_up_listener = None

    def remove_on_mouse_move_listener(self):
        self._on_mouse_move_listener = None

    def remove_on_mouse_wheel_listener(self):
        self._on_mouse_wheel_listener = None

    def set_on_mouse_move_listener(self, func):
        self._on_mouse_move_listener = func

    def set_on_mouse_up_listener(self, func):
        self._on_mouse_up_listener = func

    def set_on_mouse_down_listener(self, func):
        self._on_mouse_down_listener = func

    def set_on_mouse_wheel_listener(self, func):
        self._on_mouse_wheel_listener = func

    def is_mouse_event_present(self) -> bool:
        return (self._on_mouse_down_listener is not None) or (self._on_mouse_up_listener is not None) or (self._on_mouse_move_listener is not None)

    def on_mouse_down(self, sender: object, event: pygame.event.Event) -> bool:
        if self._on_mouse_down_listener is not None:
            self._on_mouse_down_listener(sender, event)
            return True

    def on_mouse_up(self, sender: object, event: pygame.event.Event) -> bool:
        if self._on_mouse_up_listener is not None:
            self._on_mouse_up_listener(sender, event)
            return True

    def on_mouse_move(self, sender: object, event: pygame.event.Event) -> bool:
        if self._on_mouse_move_listener is not None:
            self._on_mouse_move_listener(sender, event)
            return True

    def do_mouse_event(self, sender: object, event: pygame.event.Event) -> bool:
        ret: bool = False
        if event.type == pygame.MOUSEMOTION:
            if self.on_mouse_move(sender, event):
                ret = True
        if event.type == pygame.MOUSEBUTTONUP:
            if self.on_mouse_up(sender, event):
                ret = True
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.on_mouse_down(sender, event):
                ret = True
        if event.type == pygame.MOUSEWHEEL:
            if self.on_mouse_wheel(sender, event):
                ret = True
        return ret

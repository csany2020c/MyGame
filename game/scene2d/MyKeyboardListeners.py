import pygame

from game.scene2d.MyLifeCycles import *


class MyKeyboardListeners:

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

    def is_keyboard_event_present(self) -> bool:
        return self._on_key_up_listener is not None or self._on_key_down_listener is not None

    def on_key_up(self, sender: object, event: pygame.event.Event) -> bool:
        if self._on_key_up_listener is not None:
            self._on_key_up_listener(sender, event)

    def on_key_down(self, sender: object, event: pygame.event.Event) -> bool:
        if self._on_key_down_listener is not None:
            self._on_key_down_listener(sender, event)

    def do_key_event(self, sender: object, event: pygame.event.Event) -> bool:
        # ret: bool = False
        if event.type == pygame.KEYUP:
            if self.on_key_up(sender, event):
                pass
                # ret = True
        if event.type == pygame.KEYDOWN:
            if self.on_key_down(sender, event):
                pass
                # ret = True
        return False
